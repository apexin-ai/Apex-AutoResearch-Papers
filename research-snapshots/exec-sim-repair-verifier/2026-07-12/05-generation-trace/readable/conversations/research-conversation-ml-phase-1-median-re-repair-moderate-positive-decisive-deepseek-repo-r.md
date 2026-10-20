# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Re-repair moderate positive 但非 decisive + DeepSeek repo 结果可解读但有噪声 核心假设：['R

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/4bcf59e4-5609-46cc-bcbe-3510a988b4fa.jsonl`
- **Structured JSON:** [`2b2af48acd5c737c5dbc.json`](../../sessions/2b/2b2af48acd5c737c5dbc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T03:45:56.138Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T03:45:56.138Z",
  "sessionId": "4bcf59e4-5609-46cc-bcbe-3510a988b4fa",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Re-repair moderate positive 但非 decisive + DeepSeek repo 结果可解读但有噪声\n核心假设：['Re-repair phase1 显示 CLS-diagnostic (B) 比 control (A1) 提升 3-8pp，统计显著性边缘 (p=0.05-0.10)', 'Oracle (C) > B 但梯度不够陡，或 Random (D) 也有部分提升（稀释 CLS-specific 贡献）', 'DeepSeek repo CWM unparseable 15-40%，结果方向明确但 gap 较小或 seed variance 大', 'Re-repair 在部分 prompt format 有效、部分无效（robustness check 不完全通过）']\n关键指标范围：{'re_repair_resolve_delta_B_vs_A1_pp': [3, 9], 're_repair_oracle_vs_cls_delta_pp': [2, 8], 'deepseek_repo_cls_accuracy': [75, 82], 'deepseek_repo_cwm_accuracy': [68, 79], 'deepseek_repo_cwm_unparseable_pct': [15, 40], 'deepseek_repo_cls_cwm_gap_pp': [0, 8]}\n叙事方向：Re-repair 作为 supplementary evidence 而非独立贡献。写法: \"preliminary evidence suggests diagnostic granularity enables targeted re-repair (Section 6.2)\" 但不列入 core claims。 降低 claim 强度为 \"diagnostic information has potential downstream utility\"。 主线仍是三个 core claims (equivalence / divergence / granularity)。DeepSeek 结果 支持 design space 叙事但需要 hedge language (\"in our experimental setting\")。 仍投 EMNLP Main，但 accept 概率依赖 novelty perception；准备 Findings 作 realistic landing。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: exec-sim-repair-verifier\nfocus: 评估加入 re-repair downstream utility section 后论文的整体说服力。重点关注：(1) re-repair 结果是否能有效回应 'no downstream utility' reviewer concern, (2) 即使 re-repair 是 moderate positive (+5-10pp) 而非 strong positive，论文整体是否足够, (3) 如果 re-repair negative，论文是否仍可投稿\n\n## paper_framing.md\n\n# Paper Framing — exec-sim-repair-verifier\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Extended fallback: ICSE 2027 (Jun 23 abstract, Jun 30 paper)\n- Deadline: ARR May 25, 2026 (9 days remaining)\n\n## D116 Framing Pivot (2026-05-16)\n\n**前 framing**: \"CLS scales where generation fails\" (CLS advocacy)\n**新 framing**: \"The Formulation Design Space for Neural Code Verification\" (empirical characterization)\n\n核心转变：不再主张任何 formulation 普遍更好，而是 characterize 何时用什么。\n最强贡献重新定位：\n1. CWM 失败模式是 **tokenizer/model-specific** 而非 formulation-inherent（Qwen 93% unparseable vs DeepSeek 11.8%）\n2. Error complementarity: CLS/CWM 有系统性互补错误模式，oracle ensemble +2-3pp\n3. 复杂度是 formulation 选择的关键维度（func-level 等价，repo-level 分化）\n\n## Core Claims (revised per D116)\n\n1. **Formulation Equivalence at Low Complexity**: At function-level, CLS, CWM, and TRAJ achieve statistically equivalent accuracy across two model families (Qwen3: 88.4/87.2/86.3%; DeepSeek: 86.9/86.8/84.2%). Formulation choice does not matter when execution outputs are short and structured.\n\n2. **Complexity-Dependent Divergence (Model-Contingent)**: At repo-level, formulation effectiveness depends on model/tokenizer properties:\n   - Qwen3: CLS dominates CWM by 19-26pp due to 54-93% unparseable rate (tokenizer-specific CWM collapse)\n   - DeepSeek: ⏳ **PENDING** — results determine narrative direction:\n     - If CLS > CWM: \"complexity-dependent advantage is consistent across model families\"\n     - If CWM ≥ CLS: \"advantage is model/tokenizer-contingent; CWM works when tokenizer supports structured generation\"\n   - Either outcome supports the design space characterization framing\n\n3. **Diagnostic Granularity Without Accuracy Cost**: Per-test CLS achieves TOST equivalence with trajectory-level scoring (p=0.007, ±2pp margin, Qwen3) while providing per-test failure localization. Efficiency advantage: 6-9x inference speedup, 8x batch capacity on 24GB GPU.\n\n## Story Spine (D116 revision)\n\n**Problem**: Execution-free verification for code repair can be formulated in multiple ways (per-test classification, execution output generation, trajectory-level scoring), but no systematic comparison exists. Practitioners lack guidance on which formulation to use under what conditions.\n\n**Existing approaches & gaps**: Code World Models generate execution outputs but suffer from format compliance failures at scale. Trajectory-level verifiers (SWE-RM) provide coarse binary signals without per-test diagnostics. Classification-based verifiers (LEVER, CodeT) rank candidates but don't provide per-test failure localization. No work provides a controlled comparison across these formulations holding model, data, and compute constant.\n\n**Our contribution**: We present the first controlled comparison of three verification formulations (CLS, CWM, TRAJ) across 2 model families, 2 complexity levels, and multiple seeds. Key findings:\n1. Formulations are equivalent at function-level (null result establishing baseline)\n2. Formulations diverge at repo-level in a model-contingent manner\n3. CWM failure at repo-level is tokenizer-specific (not formulation-inherent): unparseable rate drops from 93% (Qwen) to [X]% (DeepSeek)\n4. CLS and CWM exhibit complementary error patterns (oracle ensemble: 90.63%)\n5. Per-test CLS matches trajectory-level accuracy while providing diagnostic granularity at 6-9x lower inference cost\n\n**Headline result template (dual-path)**:\n- Path A (CLS > CWM on DeepSeek): \"Classification consistently outperforms generation at repo-level across model families, but the magnitude depends on tokenizer-specific format compliance. We characterize when and why each formulation succeeds.\"\n- Path B (CWM ≥ CLS on DeepSeek): \"No single formulation dominates: CLS wins on Qwen (tokenizer-induced CWM collapse) while CWM matches/exceeds CLS on DeepSeek. The formulation design space is model-contingent, and we provide the empirical characterization needed to navigate it.\"\n\n## Venue Fit Risks\n\n1. **Novelty concern (Dream consensus)**: \"Classification > generation when outputs are complex\" is predictable. Mitigation: novelty is in (a) empirical demonstration that it's tokenizer-specific not formulation-inherent, (b) error complementarity analysis, (c) systematic controlled comparison methodology. Frame as \"empirical characterization with actionable insights\" not \"method contribution.\"\n\n2. **EMNLP vs SE venue**: Mitigation: (a) process vs outcome supervision parallel (Lightman et al., 2023; Uesato et al., 2022), (b) general NLP methodology insight about classification vs generation.\n\n3. **CWM comparison fairness**: Original CWM is 32B with mid-training on execution traces; we compare 4-8B LoRA. Mitigation: explicitly scope as \"same-size LoRA comparison\" and discuss that generation may need more capacity. This limitation actually strengthens the practical guidance: \"at practical deployment sizes (4-8B), classification is the safer choice.\"\n\n4. **Re-repair null result**: Downstream utility unvalidated. Mitigation: frame efficiency + diagnostic granularity as the practical benefit, not re-repair. Re-repair is future work.\n\n## Anticipated Reviewer Concerns & Mitigations (updated per Dream)\n\n| Concern | Mitigation |\n|---------|------------|\n| \"Limited novelty — obvious that classification is easier\" | Func-level null result proves it's NOT trivially easier; advantage is complexity+tokenizer-dependent. Strongest novelty: CWM failure is tokenizer-specific |\n| \"CWM comparison unfair (4-8B LoRA vs 32B full)\" | Explicitly scope as same-size comparison; discuss scale as limitation; practical guidance framing |\n| \"Single-seed repo-level\" | Multi-seed replication (2 seeds × 2 formulations × DeepSeek, running) |\n| \"Cross-model validation incomplete\" | DeepSeek repo experiments (running); whichever direction supports the design space characterization |\n| \"No downstream utility\" | Efficiency benefit (6-9x) is practical; re-repair honestly framed as future work |\n| \"Claims outrun evidence\" | D116: remove all advocacy language; report what evidence supports, nothing more |\n| \"Process vs outcome supervision parallel\" | Add Lightman et al. 2023, Uesato et al. 2022 to Related Work |\n\n## Related Work Additions Needed (Dream feedback)\n- Process vs outcome supervision: Lightman et al. 2023, Uesato et al. 2022 (CLS vs TRAJ parallel)\n- CodeRL, AlphaCode, Reflexion (verification-in-the-loop repair)\n- Predictive mutation testing literature (per-test binary classification precedent)\n\n\n## experiment_plan (with registry status)\n\n- id: cwm-baseline\n  claim: 1\n  description: Train CWM generation baseline (Qwen3-4B LoRA, same data/config as MVP-B)\n    to predict execution output instead of pass/fail. Compare per-class F1 against\n    classification model (87.1/87.9%).\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - mvp-b-train\n  status: DONE\n  registry_id: cwm-baseline\n  conclusion: negative\n  metrics:\n    overall_accuracy: 87.51\n    pass_f1: 87.31\n    fail_f1: 87.71\n    pass_precision: 92.06\n    pass_recall: 83.03\n    fail_precision: 83.53\n    fail_recall: 92.32\n    exact_match_rate: 84.02\n    train_loss: 0.2534\n    eval_loss: 0.0644\n    train_runtime_sec: 3439\n    test_set_size: 1890\n    unparseable_predictions: 0\n- id: multi-seed-core\n  claim: 1\n  description: 'Multi-seed validation for core comparison: run classification (mvp-b-train)\n    and CWM baseline each with seeds {0, 1, 42}. Report mean +/- std F1. Statistical\n    significance via paired t-test or bootstrap CI. Required for any claim of ''significantly\n    better''.'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - cwm-baseline\n  registry_id: traj-level-seed0\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 85.66\n    unresolved_f1: 87.37\n    resolved_f1: 83.41\n    unresolved_precision: 82.71\n    unresolved_recall: 92.59\n    resolved_precision: 90.07\n    resolved_recall: 77.66\n    consistency_rate: 79.55\n    train_loss: 0.225\n    eval_loss_epoch1: 0.0949\n    eval_loss_epoch2: 0.0885\n    eval_loss_epoch3: 0.1011\n    train_runtime_sec: 4071.3\n- id: trace-then-judge\n  claim: 1\n  description: 'Trace-then-Judge ablation (chain-of-thought, NOT pipeline): single\n    Qwen3-4B model trained to first generate a brief execution reasoning trace (~50\n    tokens describing expected behavior), then output pass/fail. Same LoRA config/data.\n    Tests whether explicit execution reasoning helps or hurts compared to direct classification.\n    If trace-then-judge >= direct classification, the advantage is from task simplicity,\n    not from skipping reasoning.'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - cwm-baseline\n  registry_id: trace-then-judge\n  status: DONE\n  conclusion: failed\n- id: traj-level-finetuned\n  claim: 1\n  description: 'Same-size fine-tuned trajectory-level baseline: Qwen3-4B LoRA trained\n    to predict resolved/unresolved. Data construction: for each problem_id, aggregate\n    all (code, test) pairs into (code, all_tests_concatenated) -> resolved (original\n    code passes all tests) / unresolved (mutated code fails any test). Same train/val/test\n    split by problem_id. Isolates granularity effect.'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - mvp-b-data-prep\n  registry_id: traj-level-finetuned\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.66\n    unresolved_f1: 87.5\n    resolved_f1: 83.18\n    per_test_consistency: 79.94\n- id: model-size-scaling\n  claim: 1\n  description: Scale classification model from 4B to 8B. Measure accuracy improvement\n    and compare with CWM at 8B. Determine if classification advantage holds across\n    scales.\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - cwm-baseline\n  registry_id: model-size-scaling-cls8b\n  sub_experiments:\n  - registry_id: model-size-scaling-cls8b\n    gpu: seetacloud cuda:0\n    description: Qwen3-8B LoRA classification\n  - registry_id: model-size-scaling-cwm8b\n    gpu: seetacloud cuda:1\n    description: Qwen3-8B LoRA CWM generation\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 90.48\n    pass_f1: 90.86\n    fail_f1: 90.06\n    pass_precision: 90.22\n    pass_recall: 91.51\n    fail_precision: 90.76\n    fail_recall: 89.36\n    train_loss: 0.3125\n    eval_loss_epoch1: 0.0723\n    eval_loss_epoch2: 0.0741\n    eval_loss_epoch3: 0.0783\n    train_runtime_sec: 5614\n    unparseable: 0\n- id: diagnostic-rerepair\n  claim: 2\n  description: 'Downstream proof-of-concept: give repair agent per-test failure predictions\n    vs no per-test info, compare resolve rate on 200 instances. Uses SWE-agent or\n    similar repair framework.'\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - cwm-baseline\n  - traj-level-finetuned\n  status: planned\n- id: per-test-precision-recall\n  claim: 2\n  description: Measure per-test failure prediction precision/recall against ground-truth\n    failing tests on full test set. Evaluate diagnostic signal quality without downstream\n    execution.\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-b-train\n  registry_id: per-test-precision-recall\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.51\n    fail_precision: 82.75\n    fail_recall: 93.64\n    fail_f1: 87.86\n    pass_precision: 93.24\n    pass_recall: 81.8\n    pass_f1: 87.15\n    FP_count: 58\n    FN_count: 178\n    best_mutation: return_value (97.26%)\n    worst_mutation: off_by_one (82.56%)\n    bucket_6_10_acc: 96.3\n    bucket_11plus_acc: 87.12\n- id: oracle-f2p-stratified\n  claim: 3\n  description: Stratified oracle analysis by F2P test count (T=1, T=2, T=3+). Report\n    per-test advantage breakdown showing advantage concentrates in multi-test instances.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - mvp-a-oracle-sim\n  registry_id: oracle-f2p-stratified\n  status: DONE\n  conclusion: success\n  metrics:\n    T1_pct: 68.7\n    T1_block_adv: -0.09\n    T2_pct: 19.1\n    T2_block_adv: 31.69\n    T3_5_pct: 7.1\n    T3_5_block_adv: 40.74\n    T6plus_pct: 5.1\n    T6plus_block_adv: 40.06\n    overall_block_adv: 10.93\n    T2_contribution_pct: 55.3\n- id: oracle-total-validated\n  claim: 3\n  description: Oracle study with Total (F2P+P2P) distribution at empirically measured\n    regression rates. Validate when P2P tests help vs hurt.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - p2p-regression-rate\n  status: DONE\n  registry_id: mvp-a-oracle-sim\n  conclusion: success\n  metrics:\n    original_T12:\n      iid_adv_70_85: 0.1849\n      block_adv_70_85: 0.3618\n    sensitivity_T3:\n      iid_adv_70_85: 0.0761\n      block_adv_70_85: 0.3839\n    sensitivity_T7:\n      iid_adv_70_85: 0.1351\n      block_adv_70_85: 0.3833\n    sensitivity_T11:\n      iid_adv_70_85: 0.1863\n      block_adv_70_85: 0.3639\n    real_f2p_T1:\n      iid_adv_70_85: 0.0198\n      block_adv_70_85: 0.1088\n      pct_T1: 0.687\n      T_median: 1\n      T_mean: 2.3\n    swebench_f2p_stats:\n      median: 1\n      mean: 3\n      P75: 2\n      P90: 3\n    total_reg5pct:\n      iid_adv_70_85: -0.01\n      block_adv_70_85: -0.005\n      pass: false\n    total_reg10pct:\n      iid_adv_70_85: 0.132\n      block_adv_70_85: 0.083\n      pass: true\n    total_reg20pct:\n      iid_adv_70_85: 0.357\n      block_adv_70_85: 0.278\n      pass: true\n- id: block-corr-empirical\n  claim: 3\n  description: 'Empirically validate block-correlation assumption: measure actual\n    prediction error correlation structure from trained model''s test-level predictions,\n    compare with i.i.d. and block-correlated simulation models.'\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - mvp-b-train\n  registry_id: block-corr-empirical\n  status: DONE\n  conclusion: success\n  metrics:\n    icc: 0.1909\n    icc_p_value: 0\n    design_effect: 3.9676\n    overall_error_rate: 0.1249\n    all_correct_observed: 46\n    all_correct_expected_iid: 16.35\n    all_correct_ratio: 2.81\n    error_std_observed: 0.1531\n    error_std_expected_iid: 0.0811\n    error_std_ratio: 1.89\n    n_samples: 1890\n    n_problems: 114\n    inference_precision: bfloat16\n    version: v2_corrected\n- id: swebench-pertest-data\n  claim:\n  - 1\n  - 2\n  - 3\n  description: Docker re-evaluation of SWE-bench Verified patches to extract per-test\n    labels. Build SWE-bench-PerTest dataset (500 instances x 16 candidates). Resource\n    contribution.\n  priority: P1\n  gpu_budget_hours: 0\n  compute_note: CPU/Docker only, ~16-24h with 16 parallel containers. Start early\n    to parallelize with GPU experiments.\n  deps: []\n  status: planned\n- id: repo-level-training\n  claim:\n  - 1\n  - 2\n  description: Fine-tune Qwen3-4B/8B on repo-level (patched_code, test_code) -> pass/fail\n    using SWE-bench-PerTest data. Evaluate on held-out instances.\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - swebench-pertest-data\n  registry_id: repo-level-cwm-v3\n  status: DONE\n  conclusion: failed\n- id: llm-judge-baseline\n  claim:\n  - 1\n  - 3\n  description: Qwen3-8B/32B zero-shot LLM-as-judge baselines (trajectory-level and\n    per-test). Reference points for Pareto frontier.\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: llm-judge-8b-zeroshot\n  sub_experiments:\n  - registry_id: llm-judge-8b-zeroshot\n    gpu: seetacloud cuda:2\n    description: Qwen3-8B zero-shot per-test + trajectory-level\n  - registry_id: llm-judge-32b-zeroshot\n    gpu: seetacloud cuda:3\n    description: Qwen3-32B 4-bit quantized zero-shot\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 64.4\n    fail_precision: 57.9\n    fail_recall: 95.8\n    fail_f1: 72.2\n    pass_precision: 90\n    pass_recall: 35.1\n    pass_f1: 50.5\n    majority_baseline: 51.7\n    accuracy_vs_baseline_gap: 12.6\n    traj_accuracy: 99.1\n    traj_problems: 114\n    traj_true_resolved: 1\n    traj_pred_resolved: 0\n    confusion:\n      TP_fail: 874\n      FN_fail: 38\n      FP_fail: 635\n      TN_fail: 343\n- id: per-test-majority-voting\n  claim: 1\n  description: Per-test majority voting (K=3) with classification model. Test if self-consistency\n    improves per-test accuracy.\n  priority: P2\n  gpu_budget_hours: 3\n  deps:\n  - mvp-b-train\n  registry_id: per-test-majority-voting\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy_greedy: 87.51\n    accuracy_majority_vote_K3: 86.83\n    delta_accuracy: -0.69\n    fail_f1_greedy: 87.86\n    fail_f1_mv: 87.29\n    pass_f1_greedy: 87.15\n    pass_f1_mv: 86.33\n    unanimous_rate: 93.3\n    split_samples: 127\n    flipped_correct_to_wrong: 28\n    flipped_wrong_to_correct: 15\n    net_flips: -13\n    per_pass_accuracy:\n    - 86.72\n    - 86.83\n    - 87.62\n    wall_time_greedy_sec: 30\n    wall_time_mv_sec: 120\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-a-oracle-sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    original_T12:\n      iid_adv_70_85: 0.1849\n      block_adv_70_85: 0.3618\n    sensitivity_T3:\n      iid_adv_70_85: 0.0761\n      block_adv_70_85: 0.3839\n    sensitivity_T7:\n      iid_adv_70_85: 0.1351\n      block_adv_70_85: 0.3833\n    sensitivity_T11:\n      iid_adv_70_85: 0.1863\n      block_adv_70_85: 0.3639\n    real_f2p_T1:\n      iid_adv_70_85: 0.0198\n      block_adv_70_85: 0.1088\n      pct_T1: 0.687\n      T_median: 1\n      T_mean: 2.3\n    swebench_f2p_stats:\n      median: 1\n      mean: 3\n      P75: 2\n      P90: 3\n    total_reg5pct:\n      iid_adv_70_85: -0.01\n      block_adv_70_85: -0.005\n      pass: false\n    total_reg10pct:\n      iid_adv_70_85: 0.132\n      block_adv_70_85: 0.083\n      pass: true\n    total_reg20pct:\n      iid_adv_70_85: 0.357\n      block_adv_70_85: 0.278\n      pass: true\n- exp_id: mvp-b-data-prep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp-b-train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 0.875\n    pass_f1: 0.871\n    fail_f1: 0.879\n    pass_precision: 0.9324\n    pass_recall: 0.818\n    fail_precision: 0.8275\n    fail_recall: 0.9364\n    majority_baseline: 0.52\n    accuracy_vs_majority_gap: 0.355\n- exp_id: p2p-regression-rate\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: cwm-baseline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    overall_accuracy: 87.51\n    pass_f1: 87.31\n    fail_f1: 87.71\n    pass_precision: 92.06\n    pass_recall: 83.03\n    fail_precision: 83.53\n    fail_recall: 92.32\n    exact_match_rate: 84.02\n    train_loss: 0.2534\n    eval_loss: 0.0644\n    train_runtime_sec: 3439\n    test_set_size: 1890\n    unparseable_predictions: 0\n- exp_id: multi-seed-core\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seed42:\n      accuracy: 87.83\n      pass_f1: 88.06\n      fail_f1: 87.59\n      pass_precision: 89.45\n      pass_recall: 86.71\n      fail_precision: 86.2\n      fail_recall: 89.04\n    seed123:\n      accuracy: 89.52\n      pass_f1: 89.64\n      fail_f1: 89.4\n      pass_precision: 91.76\n      pass_recall: 87.63\n      fail_precision: 87.34\n      fail_recall: 91.56\n    seed456:\n      accuracy: 87.88\n      pass_f1: 87.53\n      fail_f1: 88.21\n      pass_precision: 93.6\n      pass_recall: 82.21\n      fail_precision: 83.12\n      fail_recall: 93.97\n    mean:\n      accuracy: 88.41\n      pass_f1: 88.41\n      fail_f1: 88.4\n    std:\n      accuracy: 0.96\n      pass_f1: 1.1\n      fail_f1: 0.92\n- exp_id: trace-then-judge\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: traj-level-finetuned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.66\n    unresolved_f1: 87.5\n    resolved_f1: 83.18\n    per_test_consistency: 79.94\n- exp_id: model-size-scaling-cls8b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 90.48\n    pass_f1: 90.86\n    fail_f1: 90.06\n    pass_precision: 90.22\n    pass_recall: 91.51\n    fail_precision: 90.76\n    fail_recall: 89.36\n    train_loss: 0.3125\n    eval_loss_epoch1: 0.0723\n    eval_loss_epoch2: 0.0741\n    eval_loss_epoch3: 0.0783\n    train_runtime_sec: 5614\n    unparseable: 0\n- exp_id: model-size-scaling-cwm8b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.67\n    pass_f1: 87.57\n    fail_f1: 87.77\n    pass_precision: 91.53\n    pass_recall: 83.95\n    fail_precision: 84.19\n    fail_recall: 91.67\n    exact_match_rate: 84.39\n    train_loss: 0.229\n    eval_loss_epoch1: 0.0554\n    eval_loss_epoch2: 0.0512\n    eval_loss_epoch3: 0.0564\n    train_runtime_sec: 5570\n    unparseable: 0\n- exp_id: llm-judge-8b-zeroshot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 64.4\n    fail_precision: 57.9\n    fail_recall: 95.8\n    fail_f1: 72.2\n    pass_precision: 90\n    pass_recall: 35.1\n    pass_f1: 50.5\n    majority_baseline: 51.7\n    accuracy_vs_baseline_gap: 12.6\n    traj_accuracy: 99.1\n    traj_problems: 114\n    traj_true_resolved: 1\n    traj_pred_resolved: 0\n    confusion:\n      TP_fail: 874\n      FN_fail: 38\n      FP_fail: 635\n      TN_fail: 343\n- exp_id: llm-judge-32b-zeroshot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 71.69\n    majority_baseline: 51.75\n    accuracy_vs_baseline_gap: 19.95\n    fail_precision: 64.4\n    fail_recall: 92.43\n    fail_f1: 75.91\n    pass_precision: 88.12\n    pass_recall: 52.35\n    pass_f1: 65.68\n    unparseable_predictions: 0\n    trajectory_accuracy: 99.12\n    trajectory_total_problems: 114\n    trajectory_correct: 113\n    trajectory_true_resolved: 1\n    trajectory_pred_resolved: 0\n- exp_id: per-test-precision-recall\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.51\n    fail_precision: 82.75\n    fail_recall: 93.64\n    fail_f1: 87.86\n    pass_precision: 93.24\n    pass_recall: 81.8\n    pass_f1: 87.15\n    FP_count: 58\n    FN_count: 178\n    best_mutation: return_value (97.26%)\n    worst_mutation: off_by_one (82.56%)\n    bucket_6_10_acc: 96.3\n    bucket_11plus_acc: 87.12\n- exp_id: oracle-f2p-stratified\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    T1_pct: 68.7\n    T1_block_adv: -0.09\n    T2_pct: 19.1\n    T2_block_adv: 31.69\n    T3_5_pct: 7.1\n    T3_5_block_adv: 40.74\n    T6plus_pct: 5.1\n    T6plus_block_adv: 40.06\n    overall_block_adv: 10.93\n    T2_contribution_pct: 55.3\n- exp_id: traj-level-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 85.47\n    unresolved_f1: 87\n    resolved_f1: 83.52\n    unresolved_precision: 83.53\n    unresolved_recall: 90.78\n    resolved_precision: 88.17\n    resolved_recall: 79.33\n    consistency_rate: 78.59\n- exp_id: traj-level-seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 87.4\n    unresolved_f1: 88.7\n    resolved_f1: 85.8\n    unresolved_precision: 85.7\n    unresolved_recall: 91.9\n    resolved_precision: 89.7\n    resolved_recall: 82.3\n    consistency_rate: 78.8\n- exp_id: per-test-majority-voting\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy_greedy: 87.51\n    accuracy_majority_vote_K3: 86.83\n    delta_accuracy: -0.69\n    fail_f1_greedy: 87.86\n    fail_f1_mv: 87.29\n    pass_f1_greedy: 87.15\n    pass_f1_mv: 86.33\n    unanimous_rate: 93.3\n    split_samples: 127\n    flipped_correct_to_wrong: 28\n    flipped_wrong_to_correct: 15\n    net_flips: -13\n    per_pass_accuracy:\n    - 86.72\n    - 86.83\n    - 87.62\n    wall_time_greedy_sec: 30\n    wall_time_mv_sec: 120\n- exp_id: block-corr-empirical\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    icc: 0.1909\n    icc_p_value: 0\n    design_effect: 3.9676\n    overall_error_rate: 0.1249\n    all_correct_observed: 46\n    all_correct_expected_iid: 16.35\n    all_correct_ratio: 2.81\n    error_std_observed: 0.1531\n    error_std_expected_iid: 0.0811\n    error_std_ratio: 1.89\n    n_samples: 1890\n    n_problems: 114\n    inference_precision: bfloat16\n    version: v2_corrected\n- exp_id: traj-level-seed789\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 87.31\n    unresolved_f1: 88.27\n    resolved_f1: 86.17\n    unresolved_precision: 87.41\n    unresolved_recall: 89.15\n    resolved_precision: 87.18\n    resolved_recall: 85.18\n    consistency_rate: 76.74\n    eval_loss: 0.1115\n    train_loss: 0.2255\n    train_runtime_sec: 2055.9\n- exp_id: traj-level-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 85.66\n    unresolved_f1: 87.37\n    resolved_f1: 83.41\n    unresolved_precision: 82.71\n    unresolved_recall: 92.59\n    resolved_precision: 90.07\n    resolved_recall: 77.66\n    consistency_rate: 79.55\n    train_loss: 0.225\n    eval_loss_epoch1: 0.0949\n    eval_loss_epoch2: 0.0885\n    eval_loss_epoch3: 0.1011\n    train_runtime_sec: 4071.3\n- exp_id: cls8b-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 89.4\n    pass_f1: 89.5\n    fail_f1: 89.2\n    pass_precision: 91.2\n    pass_recall: 87.9\n    fail_precision: 87.5\n    fail_recall: 90.9\n    train_loss: 0.3087\n    eval_loss: 0.0848\n    train_runtime_sec: 5666\n    unparseable: 0\n- exp_id: cwm8b-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 86.98\n    pass_f1: 86.83\n    fail_f1: 87.13\n    pass_precision: 91.12\n    pass_recall: 82.92\n    fail_precision: 83.3\n    fail_recall: 91.34\n    exact_match_rate: 84.13\n    unparseable: 0\n    test_set_size: 1890\n- exp_id: cls-seed789\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 89\n    pass_f1: 88.9\n    fail_f1: 89.1\n    pass_precision: 93.3\n    pass_recall: 84.9\n    fail_precision: 85.2\n    fail_recall: 93.4\n- exp_id: cls-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.94\n    pass_f1: 87.79\n    fail_f1: 88.08\n    pass_precision: 92.13\n    pass_recall: 83.84\n    fail_precision: 84.2\n    fail_recall: 92.32\n    train_loss: 0.2347\n    eval_loss: 0.0963\n    train_runtime_sec: 4976.75\n    unparseable: 0\n- exp_id: repo-level-cls\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cwm-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 87.2\n    pass_f1: 86.95\n    fail_f1: 87.44\n    exact_match_rate: 84.44\n    majority_baseline_accuracy: 51.75\n    accuracy_vs_baseline_gap_pp: 35.45\n    test_set_size: 1890\n    unparseable_predictions: 0\n- exp_id: cwm-seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 86.98\n    pass_f1: 86.66\n    fail_f1: 87.29\n    pass_precision: 92.26\n    pass_recall: 81.7\n    fail_precision: 82.52\n    fail_recall: 92.65\n    exact_match_rate: 84.02\n    train_loss: 0.2525\n    eval_loss_best: 0.0551\n    eval_loss_final: 0.0635\n    train_runtime_sec: 3440\n    unparseable: 0\n- exp_id: cwm-seed789\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 86.67\n    pass_f1: 86.74\n    fail_f1: 86.6\n    exact_match_rate: 83.97\n    baseline_gap_pp: 34.92\n    test_set_size: 1890\n    unparseable_predictions: 0\n    per_class:\n      fail:\n        precision: 84.09\n        recall: 89.25\n        f1: 86.6\n      pass:\n        precision: 89.37\n        recall: 84.25\n        f1: 86.74\n- exp_id: cwm-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 87.57\n    fail_f1: 87.93\n    fail_precision: 82.71\n    fail_recall: 93.86\n    pass_f1: 87.18\n    pass_precision: 93.45\n    pass_recall: 81.7\n    exact_match_rate: 84.29\n    eval_loss: 0.0665\n    train_loss: 0.2554\n    train_runtime_sec: 3586\n- exp_id: 5-paired-clustered-bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pooled_gap_pp: -0.45\n    pooled_ci_lower: -1.71\n    pooled_ci_upper: 0.84\n    pooled_p_value: 0.499\n    tost_p_value: 0.0071\n    tost_margin_pp: 2\n    seed_level_paired_t_p: 0.425\n    seed_level_mean_gap: -0.48\n    n_variants_pooled: 523\n    n_clusters: 114\n    per_seed_gaps:\n      seed42: -0.97\n      seed123: 1.45\n      seed456: -1.84\n      seed789: -0.78\n      seed0: -0.29\n- exp_id: cwm8b-seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 86.24\n    pass_f1: 85.96\n    fail_f1: 86.51\n    pass_precision: 91.08\n    pass_recall: 81.39\n    fail_precision: 82.09\n    fail_recall: 91.45\n    exact_match_rate: 82.8\n    train_loss: 0.2279\n    eval_loss: 0.0583\n    unparseable: 0\n    test_set_size: 1890\n    majority_baseline_accuracy: 51.75\n    accuracy_vs_baseline_gap_pp: 34.5\n- exp_id: cls8b-seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 88.31\n    pass_f1: 88.2\n    fail_f1: 88.41\n    pass_precision: 92.29\n    pass_recall: 84.46\n    fail_precision: 84.72\n    fail_recall: 92.43\n    train_loss: 0.3105\n    eval_loss: 0.0928\n    unparseable: 0\n    test_set_size: 1890\n- exp_id: repo-level-cls-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-home\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6611\n    f1_macro: 0.5661\n    f1_pass: 0.769\n    f1_fail: 0.363\n    precision_pass: 0.765\n    recall_pass: 0.774\n    precision_fail: 0.369\n    recall_fail: 0.357\n    majority_baseline: 0.7296\n    n_unparseable: 132\n    best_checkpoint: checkpoint-200\n    early_stop: D045\n- exp_id: cls8b-eval-seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 90.48\n    pass_f1: 90.86\n    fail_f1: 90.06\n    pass_precision: 90.22\n    pass_recall: 91.51\n    fail_precision: 90.76\n    fail_recall: 89.36\n    unparseable: 0\n    test_set_size: 1890\n- exp_id: cls8b-eval-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 89.37\n    pass_f1: 89.54\n    fail_f1: 89.19\n    pass_precision: 91.2\n    pass_recall: 87.93\n    fail_precision: 87.54\n    fail_recall: 90.9\n    unparseable: 0\n    test_set_size: 1890\n- exp_id: matched-seed-8b-predictions\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: repo-level-cwm-v4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: repo-level-cwm-v5\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v6\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v7\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v8\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v9\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-seed123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: repo-level-cwm-seed123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: repo-level-cwm-v10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6991\n    f1_macro: 0.4671\n    f1_pass: 0.8187\n    f1_fail: 0.1154\n    precision_pass: 0.7304\n    recall_pass: 0.9314\n    precision_fail: 0.2815\n    recall_fail: 0.0726\n    majority_baseline: 0.7296\n    n_unparseable: 9102\n    n_unparseable_pct: 0.93\n    n_truncated: 478\n    n_truncated_pct: 0.0489\n    truncated_accuracy: 0.2176\n    best_checkpoint: checkpoint-400\n    early_stop: D045\n    eval_invalid: max_new_tokens=64 caused 93% unparseable (D047)\n- exp_id: repo-level-cls-v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checkpoint_sweep:\n      ckpt_600:\n        accuracy: 76.74\n        f1_macro: 73.74\n        fail_f1: 64.88\n        pass_f1: 82.61\n      ckpt_4000:\n        accuracy: 81.51\n        f1_macro: 72.56\n        fail_f1: 56.9\n        pass_f1: 88.23\n      ckpt_4200:\n        accuracy: 80.64\n        f1_macro: 72.1\n        fail_f1: 56.66\n        pass_f1: 87.54\n      ckpt_4400:\n        accuracy: 82.11\n        f1_macro: 73.94\n        fail_f1: 59.34\n        fail_precision: 77.02\n        fail_recall: 48.26\n      ckpt_4600:\n        accuracy: 82.35\n        f1_macro: 74.74\n        fail_f1: 60.87\n        pass_f1: 88.6\n        fail_precision: 76\n        fail_recall: 50.76\n    best_checkpoint_accuracy: checkpoint-4600\n    best_checkpoint_f1: checkpoint-4600\n    eval_samples: 9784\n    accuracy: 82.35\n    f1_macro: 74.74\n    unparseable: 132\n    unparseable_pct: 1.3\n    majority_baseline: 72.96\n    gap_vs_baseline: 9.39\n    eval_server: home-1x5090\n    eval_env: transformers 4.57.6\n    note: Test set sweep complete. ckpt-4600 best on both accuracy (82.35%) and f1_macro\n      (74.74%).\n    val_2048:\n      ckpt_600:\n        accuracy: 77.25\n        f1_macro: 70.81\n        fail_f1: 57.11\n        pass_f1: 84.52\n      ckpt_4000:\n        accuracy: 83.32\n        f1_macro: 70.26\n        fail_f1: 50.56\n        pass_f1: 89.97\n      ckpt_4200:\n        accuracy: 82.82\n        f1_macro: 69.54\n        fail_f1: 49.43\n        pass_f1: 89.65\n      ckpt_4400:\n        accuracy: 83.49\n        f1_macro: 71.63\n        fail_f1: 53.29\n        pass_f1: 89.97\n      ckpt_4600:\n        accuracy: 83.63\n        f1_macro: 71.72\n        fail_f1: 53.36\n        pass_f1: 90.07\n      eval_samples: 9335\n      unparseable: 1883\n      unparseable_pct: 20.2\n      val_best_f1: ckpt-4600\n      val_best_acc: ckpt-4600\n      note: 'val-test 一致: 都是 ckpt-4600'\n- exp_id: repo-level-cwm-v11\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    eval_checkpoint: checkpoint-600\n    eval_samples: 500\n    eval_type: subset500_tok1024\n    accuracy: 66.6\n    fail_f1: 27.7\n    pass_f1: 78.3\n    f1_macro: 52.99\n    fail_precision: 33.3\n    fail_recall: 23.7\n    pass_precision: 74.5\n    pass_recall: 82.5\n    unparseable: 376\n    unparseable_pct: 75.2\n    majority_baseline: 73\n    gap_vs_baseline: -6.4\n    gen_length_mean: 3398.1\n    gen_length_median: 3307.5\n    gen_length_max: 7582\n    confusion:\n      TP: 301\n      TN: 32\n      FP: 103\n      FN: 64\n- exp_id: repo-level-cls-8b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    eval_checkpoint: checkpoint-200\n    eval_samples: 9784\n    accuracy: 71.37\n    fail_f1: 60.57\n    pass_f1: 77.53\n    f1_macro: 69.05\n    fail_precision: 48.26\n    fail_recall: 81.29\n    pass_precision: 90.71\n    pass_recall: 67.69\n    unparseable: 136\n    unparseable_pct: 1.39\n    majority_baseline: 73\n    gap_vs_baseline: -1.63\n    confusion:\n      TP: 4832\n      TN: 2151\n      FP: 495\n      FN: 2306\n    eval_server: westd-48478\n    eval_env: transformers 5.8.0\n- exp_id: repo-level-cls-seed123-home\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    val_2048:\n      n: 9335\n      unparseable: 1883\n      ckpt_200:\n        accuracy: 62.51\n        f1_macro: 55.54\n        f1_pass: 73.14\n        f1_fail: 37.94\n      ckpt_400:\n        accuracy: 80.72\n        f1_macro: 67.03\n        f1_pass: 88.27\n        f1_fail: 45.78\n      ckpt_600:\n        accuracy: 76.78\n        f1_macro: 66.81\n        f1_pass: 85\n        f1_fail: 48.63\n      ckpt_800:\n        accuracy: 81.81\n        f1_macro: 69.14\n        f1_pass: 88.91\n        f1_fail: 49.37\n      ckpt_1000:\n        accuracy: 82.3\n        f1_macro: 67.63\n        f1_pass: 89.42\n        f1_fail: 45.84\n      best_f1: ckpt_800\n      best_acc: ckpt_1000\n    val_4096:\n      n: 9335\n      unparseable: 1406\n      ckpt_400:\n        accuracy: 82.57\n        f1_macro: 71.24\n        f1_pass: 89.29\n        f1_fail: 53.18\n      ckpt_600:\n        accuracy: 79.18\n        f1_macro: 70.73\n        f1_pass: 86.45\n        f1_fail: 55\n      ckpt_800:\n        accuracy: 83.7\n        f1_macro: 73.31\n        f1_pass: 90\n        f1_fail: 56.7\n      best_f1: ckpt_800\n      best_acc: ckpt_800\n    val_5120:\n      n: 9335\n      unparseable: 0\n      truncated: 234\n      ckpt_400:\n        accuracy: 86.01\n        f1_macro: 79.66\n        f1_pass: 91.02\n        f1_fail: 68.3\n      ckpt_600:\n        accuracy: 81.89\n        f1_macro: 77.01\n        f1_pass: 87.6\n        f1_fail: 66.43\n      ckpt_800:\n        accuracy: 87.92\n        f1_macro: 81.95\n        f1_pass: 92.33\n        f1_fail: 71.57\n      best_f1: ckpt_800\n      best_acc: ckpt_800\n- exp_id: repo-level-cwm-v12\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    eval_test_accuracy: 58.04\n    eval_test_f1_macro: 51.67\n    eval_test_f1_fail: 34.12\n    eval_test_f1_pass: 69.22\n    eval_test_unparseable: 5255\n    eval_test_total: 9784\n    eval_test_unparseable_rate: 53.7\n    eval_checkpoint: checkpoint-500\n- exp_id: repo-level-cwm-seed123-conda\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    eval_test_accuracy: 59.09\n    eval_test_f1_macro: 43.43\n    eval_test_f1_fail: 13.67\n    eval_test_f1_pass: 73.19\n    eval_test_unparseable: 6574\n    eval_test_total: 9784\n    eval_test_unparseable_rate: 67.2\n    eval_checkpoint: checkpoint-500\n- exp_id: repo-level-cls-8b-conda\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    val_8192:\n      ckpt_200:\n        accuracy: 63.52\n        f1_macro: 61.17\n        f1_fail: 51.6\n        f1_pass: 70.7\n        unparseable: 9\n      ckpt_400:\n        accuracy: 80.96\n      ckpt_600:\n        accuracy: 85\n      best_acc: ckpt_600\n    val_5120:\n      ckpt_400:\n        accuracy: 80.47\n        f1_macro: 75.84\n    test_2048:\n      ckpt_400:\n        accuracy: 84.52\n        f1_macro: 80.89\n      ckpt_600:\n        accuracy: 78.51\n    test_8192:\n      ckpt_400:\n        accuracy: 84.79\n        f1_macro: 81.18\n        f1_fail: 72.93\n        f1_pass: 89.43\n        unparseable: 0\n        total: 9784\n      ckpt_600:\n        accuracy: 79.05\n        f1_macro: 75.12\n        f1_fail: 65.24\n        f1_pass: 85\n        unparseable: 0\n        total: 9784\n- exp_id: repo-level-cls-v5-conda\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checkpoint_sweep:\n      ckpt_200:\n        accuracy: 52.96\n        f1_macro: 52.89\n        fail_f1: 51.02\n        pass_f1: 54.76\n      ckpt_400:\n        accuracy: 78.43\n        f1_macro: 68.41\n        fail_f1: 50.61\n        pass_f1: 86.21\n        fail_precision: 66.48\n        fail_recall: 40.85\n        pass_precision: 80.82\n        pass_recall: 92.36\n      ckpt_600:\n        accuracy: 76.37\n        f1_macro: 71.17\n        fail_f1: 58.93\n        pass_f1: 83.41\n        fail_precision: 55.6\n        fail_recall: 62.7\n        pass_precision: 85.49\n        pass_recall: 81.44\n    best_checkpoint_accuracy: checkpoint-400\n    best_checkpoint_f1: checkpoint-600\n    eval_samples: 9784\n    accuracy: 78.43\n    f1_macro: 71.17\n    unparseable: 132\n    unparseable_pct: 1.35\n    majority_baseline: 72.96\n    eval_server: westd-48478\n    eval_env: conda, transformers 4.57.6\n- exp_id: repo-level-cwm-8b-conda\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-8b-seed123-conda\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-8b-conda-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-8b-seed123-conda-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-8b-conda-v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-8b-seed123-conda-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: repo-level-cwm-8b-conda-v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-ckpt3000-test-eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-ckpt3000-test-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt3000-val-eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: repo-level-cls-8b-s42-ckpt200-val\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt3000-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 88.69\n    f1_macro: 81.73\n    f1_fail: 70.5\n    f1_pass: 93\n    precision_fail: 95.2\n    precision_pass: 87.6\n    recall_fail: 55.9\n    recall_pass: 99.1\n    majority_baseline: 75.9\n    gap_vs_majority_pp: 12.8\n    unparseable: 9\n    total: 9335\n- exp_id: cls8b-s42-ckpt400-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.79\n    f1_macro: 81.18\n    f1_fail: 72.93\n    f1_pass: 89.43\n    precision_fail: 70.32\n    precision_pass: 90.74\n    recall_fail: 75.74\n    recall_pass: 88.15\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 11.84\n    unparseable: 0\n    total: 9784\n- exp_id: cls4b-seed123-ckpt800-val5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.92\n    f1_macro: 81.95\n    f1_pass: 92.33\n    f1_fail: 71.57\n    unparseable: 0\n    truncated: 234\n    total: 9335\n- exp_id: cls8b-s42-ckpt600-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 79.05\n    f1_macro: 75.12\n    f1_fail: 65.24\n    f1_pass: 85\n    precision_fail: 59.16\n    precision_pass: 88.95\n    recall_fail: 72.71\n    recall_pass: 81.4\n    unparseable: 0\n    total: 9784\n    majority_baseline: 73\n    gap_vs_majority_pp: 6.09\n- exp_id: repo-level-cls-8b-s42-resume\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_steps: 6633\n    epochs: 3\n    train_time_sec: 74425\n    final_train_loss: 0.4284\n    final_eval_loss: 0.4768\n    best_eval_loss_resume: 0.2516\n    best_eval_loss_resume_step: 4200\n    best_eval_loss_overall: 0.0796\n    best_eval_loss_overall_step: 200\n    checkpoints_saved: 32\n    overfitting: true\n    note: Severe overfitting after epoch 2. Resume-best=ckpt-4200. Val sweep running\n      on cuda:0.\n- exp_id: cls8b-s42-ckpt200-val8192-eval-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 63.52\n    f1_macro: 61.17\n    f1_fail: 51.6\n    f1_pass: 70.7\n    unparseable: 9\n    total: 9335\n- exp_id: cls4b-v5-val5120-sweep-home\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-v5-ckpt600-val5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 82.82\n    f1_macro: 79.81\n    f1_fail: 72.03\n    f1_pass: 87.6\n    precision_fail: 59.3\n    recall_fail: 91.7\n    unparseable: 0\n    total: 9335\n- exp_id: cls8b-s42-ckpt800-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.5\n    f1_macro: 79.2\n- exp_id: cls4b-v5-ckpt4000-val5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 89.84\n    f1_macro: 84.25\n    f1_fail: 74.85\n    f1_pass: 93.64\n    precision_fail: 92.95\n    recall_fail: 62.66\n    precision_pass: 89.24\n    recall_pass: 98.49\n    unparseable: 0\n    truncated: 234\n    total: 9335\n- exp_id: cls8b-s42-ckpt1000-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 88.23\n    f1_macro: 82.72\n    f1_fail: 73\n    f1_pass: 92.5\n    precision_fail: 81.8\n    recall_fail: 65.8\n    precision_pass: 89.8\n    recall_pass: 95.3\n    unparseable: 9\n    total_instances: 9335\n- exp_id: cls4b-v5-ckpt4400-val5120-eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    accuracy_partial_70pct: 89.69\n    f1_macro_partial_70pct: 84.61\n    samples_completed: 6544\n    samples_total: 9335\n- exp_id: cls8b-s42-ckpt1000-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.52\n    f1_macro: 77.5\n    f1_fail: 65.85\n    f1_pass: 89.14\n    precision_fail: 74.93\n    recall_fail: 58.73\n    precision_pass: 85.84\n    recall_pass: 92.72\n    majority_baseline: 72.96\n    gap_vs_majority: 10.56\n    unparseable_count: 0\n    unparseable_rate: 0\n    total_samples: 9784\n    tp: 6618\n    fp: 1092\n    fn: 520\n    tn: 1554\n- exp_id: cls4b-v5-ckpt4400-val5120-eval-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1200-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1400-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.97\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 10.09\n    f1_macro: 77.15\n    f1_fail: 62.95\n    f1_pass: 91.34\n    precision_fail: 86.68\n    precision_pass: 85.85\n    recall_fail: 49.42\n    recall_pass: 97.59\n    n_instances: 9335\n    n_unparseable: 9\n    confusion_matrix:\n      tn: 1113\n      fp: 1139\n      fn: 171\n      tp: 6912\n- exp_id: cls8b-s42-ckpt1600-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-v5-val-sweep-ckpt4600\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 90.07\n    f1_macro: 85.04\n    f1_fail: 76.37\n    f1_pass: 93.71\n    precision_fail: 89.65\n    recall_fail: 66.52\n    precision_pass: 90.16\n    recall_pass: 97.56\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 14.19\n    unparseable_count: 0\n    total_samples: 9335\n    n_truncated: 234\n- exp_id: cls4b-v5-val-sweep-ckpt4200\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 89.06\n    f1_macro: 83.07\n    f1_fail: 73\n    f1_pass: 93.1\n    precision_fail: 90.3\n    recall_fail: 61.3\n    precision_pass: 88.8\n    recall_pass: 97.9\n- exp_id: cls4b-v5-val-sweep-ckpt4400\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1200-val8192\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-v5-val-sweep-ckpt4400-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 89.96\n    f1_macro: 84.94\n    f1_fail: 76.25\n    f1_pass: 93.64\n    precision_fail: 88.84\n    precision_pass: 90.21\n    recall_fail: 66.79\n    recall_pass: 97.33\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 14.09\n    n_instances: 9335\n    n_truncated: 234\n    n_unparseable: 0\n- exp_id: cls8b-s42-ckpt1200-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.84\n    f1_macro: 77.47\n    f1_fail: 65.49\n    f1_pass: 89.45\n    precision_fail: 77.52\n    recall_fail: 56.69\n    precision_pass: 85.4\n    recall_pass: 93.91\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 10.89\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-s42-ckpt1400-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.47\n    f1_macro: 78.9\n    f1_fail: 67.13\n    f1_pass: 90.67\n    precision_fail: 86.43\n    recall_fail: 54.88\n    precision_pass: 85.27\n    recall_pass: 96.81\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 12.51\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-s42-ckpt1600-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.99\n    f1_macro: 78.94\n    f1_fail: 67.65\n    f1_pass: 90.22\n    precision_fail: 81.06\n    recall_fail: 58.05\n    precision_pass: 85.93\n    recall_pass: 94.97\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 12.03\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-s42-ckpt1200-val8192-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1200-val8192-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.76\n    f1_macro: 81.25\n    f1_fail: 70.2\n    f1_pass: 92.3\n    precision_fail: 85\n    recall_fail: 59.8\n    precision_pass: 88.3\n    recall_pass: 96.7\n    majority_baseline: 75.9\n    gap_vs_majority: 11.9\n    unparseable: 9\n- exp_id: cls8b-s42-ckpt1600-val8192-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 86.75\n    f1_macro: 78.94\n    f1_fail: 66.12\n    f1_pass: 91.76\n    precision_fail: 86.28\n    precision_pass: 86.83\n    recall_fail: 53.6\n    recall_pass: 97.29\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 10.87\n    unparseable: 9\n    total: 9335\n- exp_id: cls8b-s42-ckpt800-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.53\n    f1_macro: 78.97\n    f1_fail: 69.17\n    f1_pass: 88.77\n    precision_fail: 70.07\n    recall_fail: 68.29\n    precision_pass: 88.36\n    recall_pass: 89.18\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 10.58\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6600-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.23\n    f1_macro: 79.02\n    f1_fail: 65.9\n    f1_pass: 92.14\n    precision_fail: 92.6\n    recall_fail: 51.15\n    precision_pass: 86.4\n    recall_pass: 98.7\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 11.36\n    unparseable_count: 9\n    total_samples: 9335\n- exp_id: cls4b-v5-ckpt4600-test-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.63\n    f1_macro: 75.63\n    f1_fail: 61.67\n    f1_pass: 89.59\n    precision_fail: 84.03\n    recall_fail: 48.72\n    precision_pass: 83.55\n    recall_pass: 96.57\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 10.67\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6400-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.48\n    f1_macro: 79.66\n    f1_fail: 67.04\n    f1_pass: 92.27\n    precision_fail: 91.81\n    recall_fail: 52.8\n    precision_pass: 86.78\n    recall_pass: 98.5\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 11.6\n    unparseable_count: 9\n    total_samples: 9335\n- exp_id: cls8b-seed123-ckpt6200-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.52\n    f1_macro: 79.26\n    f1_fail: 66.16\n    f1_pass: 92.35\n    precision_fail: 95.63\n    recall_fail: 50.58\n    precision_pass: 86.33\n    recall_pass: 99.27\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 11.64\n    unparseable_count: 9\n    total_samples: 9335\n- exp_id: cls4b-v5-ckpt4400-test5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.24\n    f1_macro: 74.44\n    f1_fail: 59.45\n    f1_pass: 89.44\n    precision_fail: 85.98\n    recall_fail: 45.43\n    precision_pass: 82.78\n    recall_pass: 97.25\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 10.28\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt3000-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.6\n    f1_macro: 78.38\n    f1_fail: 65.89\n    f1_pass: 90.87\n    precision_fail: 91.65\n    recall_fail: 51.44\n    precision_pass: 84.52\n    recall_pass: 98.26\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 12.64\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6633-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.1\n    f1_macro: 78.79\n    f1_fail: 65.52\n    f1_pass: 92.07\n    precision_fail: 92.26\n    recall_fail: 50.8\n    precision_pass: 86.31\n    recall_pass: 98.64\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 11.23\n    unparseable_count: 9\n    total_samples: 9335\n- exp_id: cls8b-seed123-ckpt3000-test8192-eval-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-seed123-ckpt800-test5120-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-seed123-ckpt800-test5120-eval-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 75.33\n    f1_macro: 67.03\n    f1_fail: 50.5\n    f1_pass: 83.6\n    precision_fail: 55.2\n    recall_fail: 46.5\n    precision_pass: 81.3\n    recall_pass: 86\n    majority_baseline: 73\n    gap_vs_majority_pp: 2.4\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6200-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt6400-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt200-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt6200-test-eval-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.7\n    f1_fail: 63.71\n    f1_pass: 90.31\n    f1_macro: 77.01\n    precision_fail: 88.84\n    precision_pass: 83.96\n    recall_fail: 49.66\n    recall_pass: 97.69\n    n_instances: 9784\n    n_cls_unparseable: 0\n- exp_id: cls8b-seed123-ckpt6400-test-eval-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.08\n    f1_fail: 65.32\n    f1_pass: 90.49\n    f1_macro: 77.91\n    precision_fail: 87.92\n    precision_pass: 84.54\n    recall_fail: 51.97\n    recall_pass: 97.35\n    n_instances: 9784\n    n_cls_unparseable: 0\n- exp_id: cls4b-v5-ckpt600-test5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 77.74\n    f1_macro: 74.74\n    f1_fail: 66.03\n    f1_pass: 83.44\n    precision_fail: 56.21\n    recall_fail: 80.01\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 4.78\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6600-test-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.9\n    f1_macro: 77.58\n    pass_f1: 90.4\n    fail_f1: 64.8\n    pass_precision: 84.3\n    pass_recall: 97.4\n    fail_precision: 87.8\n    fail_recall: 51.3\n    n_samples: 9784\n    n_pass: 7138\n    n_fail: 2646\n    majority_baseline: 73\n    unparseable: 0\n    confusion_matrix:\n      fail_as_fail: 1357\n      fail_as_pass: 1289\n      pass_as_fail: 188\n      pass_as_pass: 6950\n- exp_id: cls8b-s42-ckpt200-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 70.07\n    f1_macro: 68.18\n    pass_f1: 75.9\n    fail_f1: 60.4\n    pass_precision: 91.8\n    pass_recall: 64.7\n    fail_precision: 47\n    fail_recall: 84.5\n    n_samples: 9784\n    n_pass: 7138\n    n_fail: 2646\n    majority_baseline: 73\n    unparseable: 0\n    confusion_matrix:\n      fail_as_fail: 2235\n      fail_as_pass: 411\n      pass_as_fail: 2517\n      pass_as_pass: 4621\n- exp_id: cls8b-s42-ckpt1000-test-seq2048-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 82.83\n    f1_macro: 76.88\n    fail_precision: 72.2\n    fail_recall: 59.3\n    fail_f1: 65.2\n    pass_precision: 85.9\n    pass_recall: 91.5\n    pass_f1: 88.6\n    unparseable: 136\n- exp_id: cls4b-v5-ckpt4000-test5120-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt6633-test-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.89\n    f1_macro: 77.56\n    f1_fail: 64.7\n    f1_pass: 90.4\n    precision_fail: 87.8\n    recall_fail: 51.2\n    precision_pass: 84.3\n    recall_pass: 97.4\n    majority_baseline: 73\n    gap_vs_majority_pp: 11.9\n    total_samples: 9784\n    unparseable_count: 0\n- exp_id: cls8b-seed123-ckpt200-test-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 72.55\n    f1_macro: 70.18\n    pass_f1: 78.58\n    fail_f1: 61.78\n    pass_precision: 91.21\n    pass_recall: 69.02\n    fail_precision: 49.54\n    fail_recall: 82.05\n    n_samples: 9784\n    n_pass: 7138\n    n_fail: 2646\n    majority_baseline: 72.96\n    unparseable: 0\n    confusion_matrix:\n      tn: 2171\n      fp: 475\n      fn: 2211\n      tp: 4927\n- exp_id: cwm8b-ckpt400-test-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cwm-rank32-ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm-4b-rank32-ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm-rank32-ablation-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87\n    exact_match_rate: 83.4\n    fail_f1: 87.1\n    pass_f1: 86.9\n    train_loss_final: 0.0152\n    train_loss_avg: 0.2536\n    eval_loss: 0.0688\n    train_runtime_sec: 5003\n    test_set_size: 1890\n    vs_rank16_baseline: -0.51\n    rank16_baseline_accuracy: 87.51\n- exp_id: cwm-rank64-ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm-4b-rank64-ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: s42-extended-val-sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cwm-rank32-alpha64-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.04\n    pass_f1: 86.79\n    fail_f1: 87.27\n    f1_macro: 87.03\n    pass_precision: 91.8\n    pass_recall: 82.3\n    fail_precision: 82.9\n    fail_recall: 92.1\n    exact_match_rate: 84.55\n    train_loss: 0.2069\n    eval_loss: 0.0606\n    n_instances: 1890\n    vs_rank16_baseline: -0.47\n    rank16_baseline_accuracy: 87.51\n- exp_id: cls8b-s42-extended-val-sweep\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: s42-extended-val-sweep-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep-seq8192\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep-seq4096\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep-seq8192-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: repo-level-cwm-8b-conda-v5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep-gpu1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-resume-ckpt1000-test-mutation\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1000-test-mutation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-ckpt3600-test\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: cls8b-s42-resume-ckpt3600-mutation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 84.4849\n    overall_correct: 8266\n    overall_total: 9784\n    gold_accuracy: 96.2443\n    gold_correct: 4459\n    gold_total: 4633\n    mutation_operator_swap_accuracy: 81.3822\n    mutation_operator_swap_correct: 2732\n    mutation_operator_swap_total: 3357\n    mutation_off_by_one_accuracy: 86.8852\n    mutation_off_by_one_correct: 159\n    mutation_off_by_one_total: 183\n    mutation_return_value_accuracy: 75.4448\n    mutation_return_value_correct: 424\n    mutation_return_value_total: 562\n    mutation_boundary_removal_accuracy: 46.9018\n    mutation_boundary_removal_correct: 492\n    mutation_boundary_removal_total: 1049\n- exp_id: cls8b-s42-ckpt3600-seq2048-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.04\n    f1_macro: 76.8\n    unparseable: 136\n    n_samples: 9784\n    seq_length: 2048\n- exp_id: repo-level-cwm-8b-conda-v6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm8b-ckpt400-test-eval-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm8b-ckpt400-test-eval-v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-ckpt3600-test-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.48\n    f1_macro: 78.17\n    fail_recall: 56.8\n    pass_recall: 94.8\n    n_samples: 9784\n    note: reproduces v1 exactly\n- exp_id: cls8b-seed123-ckpt3000-mutation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.6\n    boundary_removal: 44.9\n    operator_swap: 82.6\n    return_value: 66.4\n    off_by_one: 79.2\n    gold: 99.6\n    n_samples: 9784\n- exp_id: cwm8b-ckpt400-test-eval-shard2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: cls4b-ckpt4600-test-mutation-pr\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.63\n    gold_acc: 98.25\n    operator_swap_acc: 78.91\n    return_value_acc: 67.97\n    off_by_one_acc: 58.47\n    boundary_removal_acc: 46.9\n    n_instances: 9784\n    note: off_by_one recall_fail=0 (all predicted pass); boundary_removal identical\n      to 8B\n- exp_id: cwm4b-s42-mutation-breakdown\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 58.04\n    parseable_rate: 46.3\n    parseable_only_accuracy: 42.9\n    gold_parse_rate: 43.5\n    gold_parseable_acc: 23.5\n    operator_swap_parse_rate: 56.9\n    operator_swap_parseable_acc: 63.1\n    off_by_one_parse_rate: 4.4\n    off_by_one_parseable_acc: 0\n    return_value_parse_rate: 48.8\n    return_value_parseable_acc: 27\n    boundary_removal_parse_rate: 30.6\n    boundary_removal_parseable_acc: 59.2\n    n_instances: 9784\n- exp_id: cwm8b-ckpt400-test-eval-shard3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cwm8b-ckpt400-test-eval-shard4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: deepseek-cls-repo\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: deepseek-cwm-func\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.04292\n    train_time_seconds: 5215\n    test_accuracy: 85.77\n    test_f1_macro: 85.73\n    test_precision_fail: 80.07\n    test_precision_pass: 93.18\n    test_recall_fail: 93.86\n    test_recall_pass: 78.22\n    test_unparseable_rate: 0\n    test_n: 1890\n- exp_id: deepseek-cls-func\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.0701\n    train_time_seconds: 5444\n    test_accuracy: 86.93\n    test_f1_macro: 86.92\n    test_precision_fail: 86.42\n    test_precision_pass: 87.41\n    test_recall_fail: 86.51\n    test_recall_pass: 87.32\n    test_n: 1890\n- exp_id: deepseek-cwm-func-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.0408\n    train_time_seconds: 5244\n    test_accuracy: 87.88\n    test_f1_macro: 87.88\n    test_precision_fail: 83.78\n    test_precision_pass: 92.61\n    test_recall_fail: 92.87\n    test_recall_pass: 83.23\n    test_unparseable_rate: 0\n    test_n: 1890\n- exp_id: deepseek-cwm-repo\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: re-repair-phase0\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    control_mean_sim: 0.82\n    cls_diag_mean_sim: 0.818\n    oracle_diag_mean_sim: 0.809\n    random_diag_mean_sim: 0.719\n    n_instances: 10\n    n_conditions: 4\n    samples_per_condition: 3\n- exp_id: deepseek-cls-func-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.06753\n    train_time_seconds: 5391\n    test_accuracy: 86.77\n    test_f1_macro: 86.77\n    test_precision_fail: 84.99\n    test_precision_pass: 88.56\n    test_recall_fail: 88.16\n    test_recall_pass: 85.48\n    test_unparseable_rate: 0\n    test_n: 1890\n- exp_id: deepseek-traj-func\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss_epoch1: 0.0943\n    eval_loss_epoch2: 0.0793\n    eval_loss_epoch3: 0.0884\n    best_eval_loss: 0.0793\n    best_step: 1008\n    best_epoch: 2\n    train_loss: 0.1131\n    train_runtime_sec: 2910.6\n- exp_id: deepseek-traj-func-s123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: deepseek-traj-func-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.0796\n    best_step: 504\n    test_accuracy: 0.8324\n    majority_baseline: 0.5359\n    train_loss: 0.0857\n    train_runtime_seconds: 3069.6\n- exp_id: deepseek-traj-func-v2-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.077\n    best_step: 504\n    test_accuracy: 0.8508\n    majority_baseline: 0.5359\n    train_loss: 0.0842\n    train_runtime_seconds: 3021\n    per_test_consistency: 0.782\n- exp_id: deepseek-traj-func-v2-fixed\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: deepseek-traj-func-v2-s123-fixed\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: deepseek-traj-repo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 0.771\n    best_eval_loss: 0.111\n    best_step: 98\n    train_loss: 0.12\n    unparseable_rate: 0.167\n    resolved_recall: 0.962\n    unresolved_recall: 0.545\n    total_test: 48\n- exp_id: deepseek-traj-repo-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 0.771\n    best_eval_loss: 0.1147\n    best_step: 98\n    train_loss: 0.12\n    unparseable_rate: 0.167\n    resolved_recall: 0.962\n    unresolved_recall: 0.545\n    total_test: 48\n- exp_id: deepseek-traj-repo-8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 81.25\n    unparseable: 0\n    best_eval_loss: 0.1216\n    best_epoch: 2\n    train_truncated_pct: 2.1\n    gpu_mem_mib: 22475\n    resolved_f1: 84.21\n    unresolved_f1: 76.92\n- exp_id: deepseek-traj-repo-8k-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 75\n    unparseable: 0\n    best_eval_loss: 0.1182\n    best_epoch: 2\n    train_truncated_pct: 2.1\n    gpu_mem_mib: 21399\n    resolved_f1: 76.92\n    unresolved_f1: 72.73\n- exp_id: deepseek-traj-repo-8k-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 75\n    f1_macro: 72.68\n    majority_baseline: 54.2\n    gap_vs_majority_pp: 20.8\n    unresolved_f1: 64.7\n    resolved_f1: 80.6\n    unresolved_precision: 91.7\n    unresolved_recall: 50\n    resolved_precision: 69.4\n    resolved_recall: 96.2\n    per_test_consistency: 75\n    unparseable_rate: 0\n    test_n: 48\n    train_loss_final: 0.2125\n    eval_loss_best: 0.1013\n- exp_id: deepseek-traj-repo-8k-s789\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 66.67\n    resolved_f1: 75\n    unresolved_f1: 50\n    best_eval_loss: 0.1295\n    unparseable: 0\n- exp_id: deepseek-traj-repo-8k-s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 75\n    unparseable: 0\n    best_eval_loss: 0.1547\n    resolved_f1: 75\n    unresolved_f1: 75\n    f1_macro: 75\n    train_loss: 0.2176\n- exp_id: deepseek-traj-repo-8k-s999\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 79.2\n    unparseable: 0\n    best_eval_loss: 0.1565\n    resolved_f1: 82.1\n    unresolved_f1: 75\n    f1_macro: 78.57\n    train_loss: 0.2184\n- exp_id: deepseek-cls-repo-s123\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: deepseek-cwm-repo-s123\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: deepseek-cls-repo-resume\n  name: ''\n  status: ALLOCATED\n  conclusion: killed\n  metrics: {}\n- exp_id: deepseek-cls-repo-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: deepseek-cls-repo-v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: deepseek-cls-repo-v4\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n\n## what_if (hypothetical experiments — additive)\n\n- name: re-repair-phase1-instruct\n  claim: 'Downstream Utility: Diagnostic-Guided Re-repair'\n  description: 'Re-repair experiment with fixed confounds: Qwen3-8B-Instruct on 50-80\n    SWE-bench Verified instances. 5 conditions (A1-minimal control, A2-test-names-only,\n    B-CLS-diagnostic, C-oracle-diagnostic, D-random). Docker-based resolve rate eval\n    (pass@1, pass@5). Paired design. Two prompt formats for robustness. Expected outcome:\n    CLS-diagnostic (B) improves resolve rate by 5-15pp over A1/A2; Oracle (C) as upper\n    bound; Random (D) as lower bound.'\n  estimated_gpu_hours: 0.0\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T03:45:56.141Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T03:45:56.141Z",
  "sessionId": "4bcf59e4-5609-46cc-bcbe-3510a988b4fa"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-17T03:45:56.168Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Re-repair moderate positive 但非 decisive + DeepSeek repo 结果可解读但有噪声
核心假设：['Re-repair phase1 显示 CLS-diagnostic (B) 比 control (A1) 提升 3-8pp，统计显著性边缘 (p=0.05-0.10)', 'Oracle (C) > B 但梯度不够陡，或 Random (D) 也有部分提升（稀释 CLS-specific 贡献）', 'DeepSeek repo CWM unparseable 15-40%，结果方向明确但 gap 较小或 seed variance 大', 'Re-repair 在部分 prompt format 有效、部分无效（robustness check 不完全通过）']
关键指标范围：{'re_repair_resolve_delta_B_vs_A1_pp': [3, 9], 're_repair_oracle_vs_cls_delta_pp': [2, 8], 'deepseek_repo_cls_accuracy': [75, 82], 'deepseek_repo_cwm_accuracy': [68, 79], 'deepseek_repo_cwm_unparseable_pct': [15, 40], 'deepseek_repo_cls_cwm_gap_pp': [0, 8]}
叙事方向：Re-repair 作为 supplementary evidence 而非独立贡献。写法: "preliminary evidence suggests diagnostic granularity enables targeted re-repair (Section 6.2)" 但不列入 core claims。 降低 claim 强度为 "diagnostic information has potential downstream utility"。 主线仍是三个 core claims (equivalence / divergence / granularity)。DeepSeek 结果 支持 design space 叙事但需要 hedge language ("in our experimental setting")。 仍投 EMNLP Main，但 accept 概率依赖 novelty perception；准备 Findings 作 realistic landing。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: exec-sim-repair-verifier
focus: 评估加入 re-repair downstream utility section 后论文的整体说服力。重点关注：(1) re-repair 结果是否能有效回应 'no downstream utility' reviewer concern, (2) 即使 re-repair 是 moderate positive (+5-10pp) 而非 strong positive，论文整体是否足够, (3) 如果 re-repair negative，论文是否仍可投稿

## paper_framing.md

# Paper Framing — exec-sim-repair-verifier

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25, 2026)
- Fallback: EMNLP 2026 Findings
- Extended fallback: ICSE 2027 (Jun 23 abstract, Jun 30 paper)
- Deadline: ARR May 25, 2026 (9 days remaining)

## D116 Framing Pivot (2026-05-16)

**前 framing**: "CLS scales where generation fails" (CLS advocacy)
**新 framing**: "The Formulation Design Space for Neural Code Verification" (empirical characterization)

核心转变：不再主张任何 formulation 普遍更好，而是 characterize 何时用什么。
最强贡献重新定位：
1. CWM 失败模式是 **tokenizer/model-specific** 而非 formulation-inherent（Qwen 93% unparseable vs DeepSeek 11.8%）
2. Error complementarity: CLS/CWM 有系统性互补错误模式，oracle ensemble +2-3pp
3. 复杂度是 formulation 选择的关键维度（func-level 等价，repo-level 分化）

## Core Claims (revised per D116)

1. **Formulation Equivalence at Low Complexity**: At function-level, CLS, CWM, and TRAJ achieve statistically equivalent accuracy across two model families (Qwen3: 88.4/87.2/86.3%; DeepSeek: 86.9/86.8/84.2%). Formulation choice does not matter when execution outputs are short and structured.

2. **Complexity-Dependent Divergence (Model-Contingent)**: At repo-level, formulation effectiveness depends on model/tokenizer properties:
   - Qwen3: CLS dominates CWM by 19-26pp due to 54-93% unparseable rate (tokenizer-specific CWM collapse)
   - DeepSeek: ⏳ **PENDING** — results determine narrative direction:
     - If CLS > CWM: "complexity-dependent advantage is consistent across model families"
     - If CWM ≥ CLS: "advantage is model/tokenizer-contingent; CWM works when tokenizer supports structured generation"
   - Either outcome supports the design space characterization framing

3. **Diagnostic Granularity Without Accuracy Cost**: Per-test CLS achieves TOST equivalence with trajectory-level scoring (p=0.007, ±2pp margin, Qwen3) while providing per-test failure localization. Efficiency advantage: 6-9x inference speedup, 8x batch capacity on 24GB GPU.

## Story Spine (D116 revision)

**Problem**: Execution-free verification for code repair can be formulated in multiple ways (per-test classification, execution output generation, trajectory-level scoring), but no systematic comparison exists. Practitioners lack guidance on which formulation to use under what conditions.

**Existing approaches & gaps**: Code World Models generate execution outputs but suffer from format compliance failures at scale. Trajectory-level verifiers (SWE-RM) provide coarse binary signals without per-test diagnostics. Classification-based verifiers (LEVER, CodeT) rank candidates but don't provide per-test failure localization. No work provides a controlled comparison across these formulations holding model, data, and compute constant.

**Our contribution**: We present the first controlled comparison of three verification formulations (CLS, CWM, TRAJ) across 2 model families, 2 complexity levels, and multiple seeds. Key findings:
1. Formulations are equivalent at function-level (null result establishing baseline)
2. Formulations diverge at repo-level in a model-contingent manner
3. CWM failure at repo-level is tokenizer-specific (not formulation-inherent): unparseable rate drops from 93% (Qwen) to [X]% (DeepSeek)
4. CLS and CWM exhibit complementary error patterns (oracle ensemble: 90.63%)
5. Per-test CLS matches trajectory-level accuracy while providing diagnostic granularity at 6-9x lower inference cost

**Headline result template (dual-path)**:
- Path A (CLS > CWM on DeepSeek): "Classification consistently outperforms generation at repo-level across model families, but the magnitude depends on tokenizer-specific format compliance. We characterize when and why each formulation succeeds."
- Path B (CWM ≥ CLS on DeepSeek): "No single formulation dominates: CLS wins on Qwen (tokenizer-induced CWM collapse) while CWM matches/exceeds CLS on DeepSeek. The formulation design space is model-contingent, and we provide the empirical characterization needed to navigate it."

## Venue Fit Risks

1. **Novelty concern (Dream consensus)**: "Classification > generation when outputs are complex" is predictable. Mitigation: novelty is in (a) empirical demonstration that it's tokenizer-specific not formulation-inherent, (b) error complementarity analysis, (c) systematic controlled comparison methodology. Frame as "empirical characterization with actionable insights" not "method contribution."

2. **EMNLP vs SE venue**: Mitigation: (a) process vs outcome supervision parallel (Lightman et al., 2023; Uesato et al., 2022), (b) general NLP methodology insight about classification vs generation.

3. **CWM comparison fairness**: Original CWM is 32B with mid-training on execution traces; we compare 4-8B LoRA. Mitigation: explicitly scope as "same-size LoRA comparison" and discuss that generation may need more capacity. This limitation actually strengthens the practical guidance: "at practical deployment sizes (4-8B), classification is the safer choice."

4. **Re-repair null result**: Downstream utility unvalidated. Mitigation: frame efficiency + diagnostic granularity as the practical benefit, not re-repair. Re-repair is future work.

## Anticipated Reviewer Concerns & Mitigations (updated per Dream)

| Concern | Mitigation |
|---------|------------|
| "Limited novelty — obvious that classification is easier" | Func-level null result proves it's NOT trivially easier; advantage is complexity+tokenizer-dependent. Strongest novelty: CWM failure is tokenizer-specific |
| "CWM comparison unfair (4-8B LoRA vs 32B full)" | Explicitly scope as same-size comparison; discuss scale as limitation; practical guidance framing |
| "Single-seed repo-level" | Multi-seed replication (2 seeds × 2 formulations × DeepSeek, running) |
| "Cross-model validation incomplete" | DeepSeek repo experiments (running); whichever direction supports the design space characterization |
| "No downstream utility" | Efficiency benefit (6-9x) is practical; re-repair honestly framed as future work |
| "Claims outrun evidence" | D116: remove all advocacy language; report what evidence supports, nothing more |
| "Process vs outcome supervision parallel" | Add Lightman et al. 2023, Uesato et al. 2022 to Related Work |

## Related Work Additions Needed (Dream feedback)
- Process vs outcome supervision: Lightman et al. 2023, Uesato et al. 2022 (CLS vs TRAJ parallel)
- CodeRL, AlphaCode, Reflexion (verification-in-the-loop repair)
- Predictive mutation testing literature (per-test binary classification precedent)


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
  status: DONE
  conclusion: failed
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
  status: DONE
  conclusion: killed
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
  status: DONE
  conclusion: success
  metrics:
    test_accuracy: 0.771
    best_eval_loss: 0.111
    best_step: 98
    train_loss: 0.12
    unparseable_rate: 0.167
    resolved_recall: 0.962
    unresolved_recall: 0.545
    total_test: 48
- exp_id: deepseek-traj-repo-s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    test_accuracy: 0.771
    best_eval_loss: 0.1147
    best_step: 98
    train_loss: 0.12
    unparseable_rate: 0.167
    resolved_recall: 0.962
    unresolved_recall: 0.545
    total_test: 48
- exp_id: deepseek-traj-repo-8k
  name: ''
  status: DONE
  conclusion: success
  metrics:
    test_accuracy: 81.25
    unparseable: 0
    best_eval_loss: 0.1216
    best_epoch: 2
    train_truncated_pct: 2.1
    gpu_mem_mib: 22475
    resolved_f1: 84.21
    unresolved_f1: 76.92
- exp_id: deepseek-traj-repo-8k-s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    test_accuracy: 75
    unparseable: 0
    best_eval_loss: 0.1182
    best_epoch: 2
    train_truncated_pct: 2.1
    gpu_mem_mib: 21399
    resolved_f1: 76.92
    unresolved_f1: 72.73
- exp_id: deepseek-traj-repo-8k-s0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    test_accuracy: 75
    f1_macro: 72.68
    majority_baseline: 54.2
    gap_vs_majority_pp: 20.8
    unresolved_f1: 64.7
    resolved_f1: 80.6
    unresolved_precision: 91.7
    unresolved_recall: 50
    resolved_precision: 69.4
    resolved_recall: 96.2
    per_test_consistency: 75
    unparseable_rate: 0
    test_n: 48
    train_loss_final: 0.2125
    eval_loss_best: 0.1013
- exp_id: deepseek-traj-repo-8k-s789
  name: ''
  status: DONE
  conclusion: success
  metrics:
    test_accuracy: 66.67
    resolved_f1: 75
    unresolved_f1: 50
    best_eval_loss: 0.1295
    unparseable: 0
- exp_id: deepseek-traj-repo-8k-s456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    test_accuracy: 75
    unparseable: 0
    best_eval_loss: 0.1547
    resolved_f1: 75
    unresolved_f1: 75
    f1_macro: 75
    train_loss: 0.2176
- exp_id: deepseek-traj-repo-8k-s999
  name: ''
  status: DONE
  conclusion: success
  metrics:
    test_accuracy: 79.2
    unparseable: 0
    best_eval_loss: 0.1565
    resolved_f1: 82.1
    unresolved_f1: 75
    f1_macro: 78.57
    train_loss: 0.2184
- exp_id: deepseek-cls-repo-s123
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: deepseek-cwm-repo-s123
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: deepseek-cls-repo-resume
  name: ''
  status: ALLOCATED
  conclusion: killed
  metrics: {}
- exp_id: deepseek-cls-repo-v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: deepseek-cls-repo-v3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: deepseek-cls-repo-v4
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}


## what_if (hypothetical experiments — additive)

- name: re-repair-phase1-instruct
  claim: 'Downstream Utility: Diagnostic-Guided Re-repair'
  description: 'Re-repair experiment with fixed confounds: Qwen3-8B-Instruct on 50-80
    SWE-bench Verified instances. 5 conditions (A1-minimal control, A2-test-names-only,
    B-CLS-diagnostic, C-oracle-diagnostic, D-random). Docker-based resolve rate eval
    (pass@1, pass@5). Paired design. Two prompt formats for robustness. Expected outcome:
    CLS-diagnostic (B) improves resolve rate by 5-15pp over A1/A2; Oracle (C) as upper
    bound; Random (D) as lower bound.'
  estimated_gpu_hours: 0.0

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
  "promptId": "5ce255d6-e9fc-479f-a121-5fcb7b733e27",
  "type": "user",
  "uuid": "f978a1b3-5771-4a42-98b5-154f6f95a82c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "4bcf59e4-5609-46cc-bcbe-3510a988b4fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T03:45:56.166Z_

```json
{
  "parentUuid": "f978a1b3-5771-4a42-98b5-154f6f95a82c",
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
  "uuid": "892ce7df-1dd1-44dd-a3c8-f7327f641c51",
  "timestamp": "2026-05-17T03:45:56.166Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "4bcf59e4-5609-46cc-bcbe-3510a988b4fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T03:45:56.166Z_

```json
{
  "parentUuid": "892ce7df-1dd1-44dd-a3c8-f7327f641c51",
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
  "uuid": "db64c251-eb03-456e-a4b3-e8d3ae9f7cf6",
  "timestamp": "2026-05-17T03:45:56.166Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "4bcf59e4-5609-46cc-bcbe-3510a988b4fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-17T03:45:56.166Z_

```json
{
  "parentUuid": "db64c251-eb03-456e-a4b3-e8d3ae9f7cf6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b5b85158-d2d8-4a63-88f6-d2702fae3035",
  "timestamp": "2026-05-17T03:45:56.166Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "4bcf59e4-5609-46cc-bcbe-3510a988b4fa",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Re-repair moderate positive 但非 decisive + DeepSeek repo 结果可解读但有噪声 核心假设：['Re-repair phase1 显示 CLS-diagnostic (B) 比 control (A1) 提升 3-8pp，统计显著性边缘 (p=0.05-0…",
  "leafUuid": "b5b85158-d2d8-4a63-88f6-d2702fae3035",
  "sessionId": "4bcf59e4-5609-46cc-bcbe-3510a988b4fa"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterize re-repair downstream utility at median evidence tier",
  "sessionId": "4bcf59e4-5609-46cc-bcbe-3510a988b4fa"
}
```

---

### Assistant

_source line 9 · 2026-05-17T03:46:41.073Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment in the experiment_plan, based on the "median" tier definition they provided. Let me identify the planned experiments:

1. **diagnostic-rerepair** (status: planned) - Downstream proof-of-concept: give repair agent per-test failure predictions vs no per-test info, compare resolve rate on 200 instances.

2. **swebench-pertest-data** (status: planned) - Docker re-evaluation of SWE-bench Verified patches to extract per-test labels.


3. **re-repair-phase1-instruct** (from what_if section) - Re-repair experiment with fixed confounds.

I'm also noting the several RUNNING experiments currently in progress, and looking back at the median tier definition to understand the expected outcomes: re-repair should show moderate positive but non-decisive results, with DeepSeek repo results being interpretable but noisy, and the core assumption that re-repair phase1 shows CLS-diagnostic outperforming control by 3 points.

The challenge is that the improvement is marginal at 8 percentage points with borderline statistical significance, the oracle condition doesn't show a steep enough gradient, and the random baseline is also improving somewhat which muddies the CLS-specific effect. Meanwhile, the DeepSeek repo results have substantial unparseable outputs ranging from 15-40%, the direction is clear but the magnitude is small or varies with seed, and re-repair only works consistently across some prompt formats rather than all of them.

Now I'm looking at which experiments are actually marked as planned versus running or hypothetical. I need to focus on the diagnostic-rerepair and swebench-pertest-data experiments since those are the ones with planned status, though there are also several DeepSeek variants currently running that I should track. I need to identify which experiments lack final results and should be included in the detailed predictions. The planned experiments (diagnostic-rerepair, swebench-pertest-data) and the what_if section's re-repair-phase1-instruct all need coverage, along with the currently running DeepSeek repo experiments. Now I'm pulling together baseline performance data from previous DeepSeek trajectory and Qwen results to ground my predictions in the median tier assumptions, then I'll generate the YAML with detailed forecasts for each incomplete experiment. Looking at the CWM results, the unparseable rate is notably lower than Qwen's highly variable performance, though still somewhat inconsistent. The diagnostic-rerepair experiment is essentially replaced by the more refined re-repair-phase1-instruct version, which shows only marginal improvements of 3-8 percentage points between conditions, with oracle performance providing some signal but not dramatically better results. The swebench-pertest-data is purely about data construction metrics rather than accuracy measurements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5b85158-d2d8-4a63-88f6-d2702fae3035",
  "isSidechain": false,
  "requestId": "req_011Cb7THyLYrWGNeX1TyH3t7",
  "type": "assistant",
  "uuid": "1feab5d6-104d-46f2-8228-12edaf0030b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "4bcf59e4-5609-46cc-bcbe-3510a988b4fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SyZZgUBwxNHRKraBsTc16f",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 33551,
      "cache_read_input_tokens": 11447,
      "output_tokens": 7080,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 7080,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 33551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33551
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

_source line 10 · 2026-05-17T03:48:25.309Z_

```yaml
tier: median
narrative_guidance: "Re-repair 作为 supplementary evidence 而非独立贡献。写法: 'preliminary evidence suggests diagnostic granularity enables targeted re-repair (Section 6.2)' 但不列入 core claims。降低 claim 强度为 'diagnostic information has potential downstream utility'。主线仍是三个 core claims。DeepSeek 结果支持 design space 叙事但需要 hedge language ('in our experimental setting')。仍投 EMNLP Main，准备 Findings 作 realistic landing。"

imagined_experiments:
  - name: deepseek-cls-repo-v4
    plan_id: repo-level-training
    description: "DeepSeek-R1-0528 4B LoRA CLS on repo-level SWE-bench-PerTest data, seed 42. 与 Qwen3 repo-level CLS 对标。"
    expected_results:
      accuracy: 79.3
      f1_macro: 73.8
      f1_fail: 63.5
      f1_pass: 84.1
      precision_fail: 72.4
      recall_fail: 56.4
      precision_pass: 81.8
      recall_pass: 86.5
      unparseable_pct: 1.8
      majority_baseline: 73.0
      gap_vs_majority_pp: 6.3
      total_samples: 9784
    result_rationale: "DeepSeek tokenizer 对 repo-level 长序列处理能力与 Qwen3 不同。CLS 任务本身简单（binary），DeepSeek 应能达到合理水平但不如 Qwen3-4B 的 82-83%。原因：(1) DeepSeek base 在 code understanding 上略弱于 Qwen3 同规模，(2) repo-level 长上下文中 DeepSeek 的 attention pattern 不同导致 fail recall 偏低，(3) 但 format compliance 无问题（CLS 只需输出 pass/fail），unparseable 接近 0。与 Qwen3-4B ckpt-4600 的 82.35% 差 ~3pp，符合 median 档 'gap 较小' 预期。"
    tables:
      - name: "Table: DeepSeek vs Qwen3 Repo-Level CLS (seed 42)"
        rows:
          - {model: "Qwen3-4B", accuracy: 82.35, f1_macro: 74.74, fail_f1: 60.87}
          - {model: "Qwen3-8B", accuracy: 84.79, f1_macro: 81.18, fail_f1: 72.93}
          - {model: "DeepSeek-4B", accuracy: 79.3, f1_macro: 73.8, fail_f1: 63.5}
    figures_description:
      - "Bar chart comparing repo-level CLS accuracy across 3 models (Qwen3-4B, Qwen3-8B, DeepSeek-4B)"
    analysis: "DeepSeek CLS 低于 Qwen3 同规模 ~3pp，但仍高于 majority baseline 6.3pp。说明 CLS formulation 在不同 model family 上都可行，但绝对水平有差异。这支持 'design space is model-contingent' 叙事。"

  - name: deepseek-cls-repo-s123
    plan_id: repo-level-training
    description: "DeepSeek-R1-0528 4B LoRA CLS on repo-level, seed 123. Multi-seed validation for DeepSeek repo CLS."
    expected_results:
      accuracy: 77.1
      f1_macro: 71.5
      f1_fail: 60.2
      f1_pass: 82.8
      precision_fail: 69.8
      recall_fail: 53.1
      precision_pass: 79.9
      recall_pass: 85.8
      unparseable_pct: 2.1
      total_samples: 9784
    result_rationale: "Seed variance 在 DeepSeek repo-level 比 func-level 大（small test set effect + repo-level 难度高）。seed123 比 seed42 低 ~2pp，反映了 median 档 'seed variance 大' 的假设。两 seed 均值 ~78.2%，落在 [75,82] 范围内。这种 variance 使得统计显著性主张需要更多 seed 或 bootstrap CI，weakens any strong claim。"
    tables: []
    figures_description:
      - "Seed variance plot: DeepSeek repo-level CLS across seeds with error bars"
    analysis: "两 seed 差异 2.2pp（79.3 vs 77.1），std ~1.6pp。相比 Qwen3 func-level 的 std 0.96pp，repo-level DeepSeek 的 variance 更大。需 hedge：'results are directionally consistent but seed-to-seed variation at repo-level is non-negligible'。"

  - name: deepseek-cwm-repo
    plan_id: repo-level-training
    description: "DeepSeek-R1-0528 4B LoRA CWM generation on repo-level, seed 42. 关键实验：验证 CWM unparseable 是否是 Qwen3 tokenizer-specific。"
    expected_results:
      accuracy: 72.8
      f1_macro: 62.4
      f1_fail: 42.1
      f1_pass: 82.7
      unparseable_pct: 23.5
      unparseable_count: 2300
      parseable_accuracy: 78.6
      exact_match_rate: 31.2
      precision_fail: 55.3
      recall_fail: 33.9
      precision_pass: 76.8
      recall_pass: 89.4
      total_samples: 9784
      majority_baseline: 73.0
      gap_vs_majority_pp: -0.2
    result_rationale: "Median 档核心假设：DeepSeek CWM unparseable 15-40%，远低于 Qwen3 的 54-93%。这证明 CWM failure 是 tokenizer-specific 而非 formulation-inherent。但 23.5% unparseable 仍然 non-trivial，导致 overall accuracy 被拉低至 majority baseline 附近。parseable subset 上 accuracy 78.6% 说明 CWM 在 DeepSeek 上'可以工作'但 format compliance 仍是瓶颈。gap vs CLS 约 6.5pp（79.3 vs 72.8），落在 [0,8] 范围内。这个结果 interpretable（方向明确：CLS > CWM）但 not decisive（gap 可能被 unparseable handling 策略影响）。"
    tables:
      - name: "Table: CWM Unparseable Rate Comparison"
        rows:
          - {model: "Qwen3-4B func-level", unparseable_pct: 0, accuracy: 87.51}
          - {model: "Qwen3-4B repo-level", unparseable_pct: 93.0, accuracy: 58.04}
          - {model: "DeepSeek-4B func-level", unparseable_pct: 0, accuracy: 85.77}
          - {model: "DeepSeek-4B repo-level", unparseable_pct: 23.5, accuracy: 72.8}
    figures_description:
      - "Stacked bar: parseable vs unparseable breakdown by model×level"
      - "Accuracy comparison: overall vs parseable-only, showing format compliance bottleneck"
    analysis: "CWM unparseable 从 Qwen3 的 93% 降至 DeepSeek 的 23.5%（-69.5pp），强力支持 'tokenizer-specific failure' claim。但 23.5% 仍不可忽略，说明 repo-level CWM 固有难度。CLS-CWM gap 6.5pp 在 parseable-only 上缩小到 0.7pp，进一步证明差异主要来自 format compliance 而非理解能力。"

  - name: deepseek-cwm-repo-s123
    plan_id: repo-level-training
    description: "DeepSeek-R1-0528 4B LoRA CWM generation on repo-level, seed 123."
    expected_results:
      accuracy: 69.4
      f1_macro: 58.9
      f1_fail: 37.6
      f1_pass: 80.2
      unparseable_pct: 28.7
      unparseable_count: 2808
      parseable_accuracy: 75.3
      exact_match_rate: 28.9
      total_samples: 9784
    result_rationale: "CWM generation 对 seed 更敏感（generation diversity → format compliance variance）。seed123 unparseable 比 seed42 高 5pp（28.7% vs 23.5%），导致 accuracy 再降 3.4pp。这种 high variance 是 median 档特征：'结果方向明确但 seed variance 大'。两 seed 均值 accuracy ~71.1%，CLS-CWM gap 均值 ~7.1pp。p-value 对这个 gap 在 2 seeds 下 likely 不显著（n=2 paired），需要更多 seed 或换 bootstrap。"
    tables: []
    figures_description: []
    analysis: "DeepSeek CWM 两 seed 差 3.4pp（72.8 vs 69.4），unparseable 差 5.2pp。variance 大于 CLS（2.2pp），符合 generation task 固有 instability。如果取 mean，CLS-CWM gap ~7pp，但 CI 很宽。写法需要：'CLS outperforms CWM on DeepSeek by 5-9pp depending on seed, though the gap is smaller than on Qwen3 (19-26pp) and primarily attributable to format compliance'。"

  - name: swebench-pertest-data
    plan_id: swebench-pertest-data
    description: "Docker re-evaluation of SWE-bench Verified patches to extract per-test labels. 500 instances × 16 candidates."
    expected_results:
      instances_completed: 467
      instances_failed_docker: 33
      total_test_pairs: 74720
      avg_tests_per_instance: 10.0
      avg_candidates_per_instance: 16
      pass_rate_gold: 0.98
      pass_rate_mutant: 0.52
      docker_timeout_pct: 4.2
      wall_clock_hours: 22
      parallel_containers: 16
    result_rationale: "500 instances 中约 33 个 Docker 环境构建失败（dependency issues, deprecated packages），这在 SWE-bench 社区经验中正常（~6-7% failure rate）。467 个成功 instance 足以构建 dataset。per-test label extraction 本身是 deterministic（run test, check exit code），无 noise。主要 overhead 是 Docker build time 和 test suite execution time，16 parallel containers 下约 22h。"
    tables: []
    figures_description: []
    analysis: "Data construction step，无 accuracy 结论。467 instances 足以支撑后续 repo-level 训练（已有 repo-level-cls-v5 用此数据）。缺失的 33 instances 不影响 representativeness（random failure，非 systematic bias）。"

  - name: diagnostic-rerepair
    plan_id: diagnostic-rerepair
    description: "Downstream POC: repair agent with per-test failure predictions vs no info. 200 instances, SWE-agent style."
    expected_results:
      control_resolve_rate: 0.22
      cls_diagnostic_resolve_rate: 0.27
      oracle_diagnostic_resolve_rate: 0.32
      random_diagnostic_resolve_rate: 0.24
      delta_cls_vs_control_pp: 5.0
      delta_oracle_vs_cls_pp: 5.0
      delta_random_vs_control_pp: 2.0
      n_instances: 200
      p_value_cls_vs_control: 0.078
      ci_95_lower_cls_delta: -0.5
      ci_95_upper_cls_delta: 10.5
      prompt_format_1_delta: 7.0
      prompt_format_2_delta: 3.0
    result_rationale: "Median 档预期 CLS-diagnostic (B) 比 control (A1) 提升 3-8pp，统计显著性边缘。这里取 5pp（22% → 27%）。基线 22% resolve rate 合理（SWE-bench 上 open-source agent 通常 20-30%）。Oracle (C) 比 B 高 5pp（27% → 32%），说明 diagnostic info 有 room for improvement 但 CLS predictions 已捕捉大部分 signal。Random (D) 也有 2pp 提升（24%），这是 median 档的关键 'dilution' 因素：即使 random test feedback 也有些价值（给 agent 任何额外 context 都有帮助），稀释了 CLS-specific 贡献。p=0.078 边缘不显著（n=200, paired McNemar），CI 包含 0。两种 prompt format 效果不一致（7pp vs 3pp），robustness check 不完全通过。"
    tables:
      - name: "Table: Re-repair Resolve Rate by Condition"
        rows:
          - {condition: "A1-control (no diagnostic)", resolve_rate: 0.22, n: 200}
          - {condition: "B-CLS diagnostic", resolve_rate: 0.27, n: 200}
          - {condition: "C-Oracle diagnostic", resolve_rate: 0.32, n: 200}
          - {condition: "D-Random diagnostic", resolve_rate: 0.24, n: 200}
        caption: "Resolve rate (pass@1). p(B>A1)=0.078, McNemar paired test."
    figures_description:
      - "Bar chart with 4 conditions showing resolve rate + 95% CI error bars"
      - "Prompt format interaction: 2×4 heatmap showing resolve rate by (format × condition)"
    analysis: "5pp improvement 在方向上支持 diagnostic utility，但 p=0.078 不满足 conventional significance。Random (D) 的 2pp lift 说明 'any feedback helps' confound 存在。写法：'CLS-guided re-repair shows a trend toward higher resolve rate (+5pp, p=0.078), though the effect does not reach statistical significance at α=0.05 in our 200-instance evaluation. We note that even random test feedback provides marginal benefit (+2pp), suggesting the advantage is partially attributable to providing any per-test context rather than CLS-specific diagnostics.' 这足以回应 'no downstream utility' concern，但不能作为 core claim。"

  - name: re-repair-phase1-instruct
    plan_id: re-repair-phase1-instruct
    description: "Re-repair with Qwen3-8B-Instruct, 60 instances, 5 conditions (A1/A2/B/C/D), Docker eval, 2 prompt formats."
    expected_results:
      n_instances: 60
      conditions:
        A1_minimal:
          resolve_rate_format1: 0.20
          resolve_rate_format2: 0.22
          mean_resolve_rate: 0.21
        A2_test_names:
          resolve_rate_format1: 0.23
          resolve_rate_format2: 0.23
          mean_resolve_rate: 0.23
        B_cls_diagnostic:
          resolve_rate_format1: 0.28
          resolve_rate_format2: 0.24
          mean_resolve_rate: 0.26
        C_oracle_diagnostic:
          resolve_rate_format1: 0.33
          resolve_rate_format2: 0.30
          mean_resolve_rate: 0.315
        D_random_diagnostic:
          resolve_rate_format1: 0.25
          resolve_rate_format2: 0.22
          mean_resolve_rate: 0.235
      delta_B_vs_A1_pp: 5.0
      delta_C_vs_B_pp: 5.5
      delta_B_vs_D_pp: 2.5
      delta_A2_vs_A1_pp: 2.0
      p_value_B_vs_A1: 0.092
      p_value_C_vs_A1: 0.018
      robustness_format1_passes: true
      robustness_format2_passes: false
      pass_at_5:
        A1: 0.35
        B: 0.42
        C: 0.48
        D: 0.37
    result_rationale: "60 instances 比 200 instances 方案更现实但 power 更低。Median 档核心特征：(1) B vs A1 +5pp 但 p=0.092（n=60 太小，McNemar power 不足），(2) C vs A1 +10.5pp 显著（p=0.018），证明 oracle diagnostic 有 clear value，(3) B vs D 仅 +2.5pp，CLS-specific contribution 被稀释，(4) Format 1 效果明显（B=28%）但 Format 2 退化（B=24%），robustness 不通过。A2（test names only）比 A1 高 2pp 说明即使只给 test name 也有些帮助，进一步稀释了 per-test pass/fail prediction 的 exclusive contribution。pass@5 差距更大（A1:35% vs B:42%），suggestion that diagnostic info helps exploration diversity。"
    tables:
      - name: "Table: Re-repair Phase 1 Results (Qwen3-8B-Instruct, N=60)"
        rows:
          - {condition: "A1-minimal", format1: 0.20, format2: 0.22, mean: 0.21}
          - {condition: "A2-test-names", format1: 0.23, format2: 0.23, mean: 0.23}
          - {condition: "B-CLS-diag", format1: 0.28, format2: 0.24, mean: 0.26}
          - {condition: "C-Oracle-diag", format1: 0.33, format2: 0.30, mean: 0.315}
          - {condition: "D-Random-diag", format1: 0.25, format2: 0.22, mean: 0.235}
      - name: "Table: Statistical Tests"
        rows:
          - {comparison: "B vs A1", delta_pp: 5.0, p_value: 0.092, significant: "no (α=0.05)"}
          - {comparison: "C vs A1", delta_pp: 10.5, p_value: 0.018, significant: "yes"}
          - {comparison: "B vs D", delta_pp: 2.5, p_value: 0.34, significant: "no"}
          - {comparison: "C vs B", delta_pp: 5.5, p_value: 0.065, significant: "no (marginal)"}
    figures_description:
      - "Ladder plot: 5 conditions ranked by mean resolve rate with bootstrap CIs"
      - "Format robustness: paired difference (Format1 - Format2) per condition, showing B is format-sensitive"
      - "Instance-level scatter: per-instance resolve outcome (binary) across conditions, highlighting 'swing' instances where diagnostic flips result"
    analysis: "Oracle (C) 显著优于 control 证明 per-test diagnostic information 有 intrinsic value for re-repair。但 CLS (B) 与 control 的差异不够显著（p=0.092），且 B vs D 差异更小（p=0.34），意味着 CLS prediction quality（87.5% accuracy）不足以完全 unlock 这个 value — 当 CLS 预测错误时反而 misleads agent。写法建议：'Oracle-guided re-repair significantly outperforms the control (p=0.018), establishing that per-test diagnostic information has downstream utility. CLS-guided re-repair shows a positive trend (+5pp) but does not reach significance, suggesting that prediction accuracy is a bottleneck for realizing the full potential of diagnostic-guided repair.' 这 honestly frames the limitation while still demonstrating the concept。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1feab5d6-104d-46f2-8228-12edaf0030b7",
  "isSidechain": false,
  "requestId": "req_011Cb7THyLYrWGNeX1TyH3t7",
  "type": "assistant",
  "uuid": "9d81a7c3-c896-4530-9c38-23a5a7145c52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "4bcf59e4-5609-46cc-bcbe-3510a988b4fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SyZZgUBwxNHRKraBsTc16f",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 33551,
      "cache_read_input_tokens": 11447,
      "output_tokens": 7080,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 7080,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 33551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33551
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Re-repair moderate positive 但非 decisive + DeepSeek repo 结果可解读但有噪声 核心假设：['Re-repair phase1 显示 CLS-diagnostic (B) 比 control (A1) 提升 3-8pp，统计显著性边缘 (p=0.05-0…",
  "leafUuid": "9d81a7c3-c896-4530-9c38-23a5a7145c52",
  "sessionId": "4bcf59e4-5609-46cc-bcbe-3510a988b4fa"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterize re-repair downstream utility at median evidence tier",
  "sessionId": "4bcf59e4-5609-46cc-bcbe-3510a988b4fa"
}
```

---
