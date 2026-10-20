# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：DeepSeek repo-level 全部失败（延续 v1-v4 的 pattern），只有 Qwen 单模型族的 repo-level 数据，cr

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/8924b315-2a19-4485-9a63-be59f1a2ff4b.jsonl`
- **Structured JSON:** [`d13b4171fa854f57ad22.json`](../../sessions/d1/d13b4171fa854f57ad22.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T17:24:59.559Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T17:24:59.559Z",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：DeepSeek repo-level 全部失败（延续 v1-v4 的 pattern），只有 Qwen 单模型族的 repo-level 数据，cross-model 验证仅限 func-level\n核心假设：['deepseek-cls-repo-v5 训练失败或 acc ≤ majority baseline（~73%）', 'deepseek-cwm-repo eval 不可用（crash、unparseable >80%、或 acc 远低于 baseline）', 'Repo-level 结论完全依赖 Qwen 单模型族——reviewer 会质疑 generalizability', 'DeepSeek TRAJ repo 是唯一跑通的 DeepSeek repo-level 实验，但 n=48 太小', 'Func-level 双模型族数据完整且 clean，但 repo-level 是 paper 的 differentiator']\n关键指标范围：{'deepseek_cls_repo_acc': [50, 73], 'deepseek_cwm_repo_acc': [40, 60], 'deepseek_cwm_repo_unparseable_pct': [70, 95], 'qwen_cls_repo_best_acc': [83, 86], 'qwen_cwm_repo_best_parseable_acc': [42, 58], 'func_level_all_formulations_acc_range': [83, 90], 'expected_reviewer_score': [2.5, 3.0]}\n叙事方向：核心 reframe: 放弃 repo-level 作为 main contribution，转为 secondary finding。 新 angle 选项 (仍冲 EMNLP main): (1) \"Per-Test vs Trajectory-Level Verification: A Controlled Study\" — 将 CLS vs TRAJ 的 粒度-效率 tradeoff 提为核心贡献（双模型族 func-level 数据完整 + Qwen repo-level 作 case study）。 强调 per-test 在 accuracy 不损失前提下提供 diagnostic granularity + 6-9x speedup。 TOST equivalence p=0.007 是 solid statistical result。 (2) Block-correlation empirical validation (ICC=0.19, design effect=4.0) 作为 methodological contribution——揭示 per-test evaluation 中 i.i.d. 假设不成立的系统性偏差。 (3) CWM repo-level failure analysis 降为一个 section 而非 core claim，explicitly scope 为 \"Qwen3 case study, cross-model validation as future work\"。 Re-repair negative result 诚实报告为 future work motivation。 Efficiency + diagnostic granularity + statistical methodology 三条线撑起 paper。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: exec-sim-repair-verifier\nfocus: 论文经过 D116 framing pivot、D126 三层 framing、D135 overtraining→evaluation sensitivity 重设计后，和 Round 1 时已大幅改变。重点评估：(1) R2-W1 新颖性是否足以达到 EMNLP main 4.0; (2) 当前 contribution framing 是否清晰有力; (3) 写作质量和 story 连贯性; (4) 还有什么具体改进能把分数从 borderline 推到 accept\n\n## paper_framing.md\n\n# Paper Framing — exec-sim-repair-verifier\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Extended fallback: ICSE 2027 (Jun 23 abstract, Jun 30 paper)\n- Deadline: ARR May 25, 2026 (9 days remaining)\n\n## D116 Framing Pivot (2026-05-16)\n\n**前 framing**: \"CLS scales where generation fails\" (CLS advocacy)\n**新 framing**: \"The Formulation Design Space for Neural Code Verification\" (empirical characterization)\n\n核心转变：不再主张任何 formulation 普遍更好，而是 characterize 何时用什么。\n最强贡献重新定位：\n1. CWM 失败模式是 **tokenizer/model-specific** 而非 formulation-inherent（Qwen 93% unparseable vs DeepSeek 11.8%）\n2. Error complementarity: CLS/CWM 有系统性互补错误模式，oracle ensemble +2-3pp\n3. 复杂度是 formulation 选择的关键维度（func-level 等价，repo-level 分化）\n\n## Core Claims (revised per D116)\n\n1. **Formulation Equivalence at Low Complexity**: At function-level, CLS, CWM, and TRAJ achieve statistically equivalent accuracy across two model families (Qwen3: 88.4/87.2/86.3%; DeepSeek: 86.9/86.8/84.2%). Formulation choice does not matter when execution outputs are short and structured.\n\n2. **Complexity-Dependent Divergence (Model-Contingent)**: At repo-level, formulation effectiveness depends on model/tokenizer properties:\n   - Qwen3: CLS dominates CWM by 19-26pp due to 54-93% unparseable rate (tokenizer-specific CWM collapse)\n   - DeepSeek: ⏳ **PENDING** — results determine narrative direction:\n     - If CLS > CWM: \"complexity-dependent advantage is consistent across model families\"\n     - If CWM ≥ CLS: \"advantage is model/tokenizer-contingent; CWM works when tokenizer supports structured generation\"\n   - Either outcome supports the design space characterization framing\n\n3. **Diagnostic Granularity Without Accuracy Cost**: Per-test CLS achieves TOST equivalence with trajectory-level scoring (p=0.007, ±2pp margin, Qwen3) while providing per-test failure localization. Efficiency advantage: 6-9x inference speedup, 8x batch capacity on 24GB GPU.\n\n## Story Spine (D116 revision)\n\n**Problem**: Execution-free verification for code repair can be formulated in multiple ways (per-test classification, execution output generation, trajectory-level scoring), but no systematic comparison exists. Practitioners lack guidance on which formulation to use under what conditions.\n\n**Existing approaches & gaps**: Code World Models generate execution outputs but suffer from format compliance failures at scale. Trajectory-level verifiers (SWE-RM) provide coarse binary signals without per-test diagnostics. Classification-based verifiers (LEVER, CodeT) rank candidates but don't provide per-test failure localization. No work provides a controlled comparison across these formulations holding model, data, and compute constant.\n\n**Our contribution**: We present the first controlled comparison of three verification formulations (CLS, CWM, TRAJ) across 2 model families, 2 complexity levels, and multiple seeds. Key findings:\n1. Formulations are equivalent at function-level (null result establishing baseline)\n2. Formulations diverge at repo-level in a model-contingent manner\n3. CWM failure at repo-level is tokenizer-specific (not formulation-inherent): unparseable rate drops from 93% (Qwen) to [X]% (DeepSeek)\n4. CLS and CWM exhibit complementary error patterns (oracle ensemble: 90.63%)\n5. Per-test CLS matches trajectory-level accuracy while providing diagnostic granularity at 6-9x lower inference cost\n\n**Headline result template (dual-path)**:\n- Path A (CLS > CWM on DeepSeek): \"Classification consistently outperforms generation at repo-level across model families, but the magnitude depends on tokenizer-specific format compliance. We characterize when and why each formulation succeeds.\"\n- Path B (CWM ≥ CLS on DeepSeek): \"No single formulation dominates: CLS wins on Qwen (tokenizer-induced CWM collapse) while CWM matches/exceeds CLS on DeepSeek. The formulation design space is model-contingent, and we provide the empirical characterization needed to navigate it.\"\n\n## Venue Fit Risks\n\n1. **Novelty concern (Dream consensus)**: \"Classification > generation when outputs are complex\" is predictable. Mitigation: novelty is in (a) empirical demonstration that it's tokenizer-specific not formulation-inherent, (b) error complementarity analysis, (c) systematic controlled comparison methodology. Frame as \"empirical characterization with actionable insights\" not \"method contribution.\"\n\n2. **EMNLP vs SE venue**: Mitigation: (a) process vs outcome supervision parallel (Lightman et al., 2023; Uesato et al., 2022), (b) general NLP methodology insight about classification vs generation.\n\n3. **CWM comparison fairness**: Original CWM is 32B with mid-training on execution traces; we compare 4-8B LoRA. Mitigation: explicitly scope as \"same-size LoRA comparison\" and discuss that generation may need more capacity. This limitation actually strengthens the practical guidance: \"at practical deployment sizes (4-8B), classification is the safer choice.\"\n\n4. **Re-repair null result**: Downstream utility unvalidated. Mitigation: frame efficiency + diagnostic granularity as the practical benefit, not re-repair. Re-repair is future work.\n\n## Anticipated Reviewer Concerns & Mitigations (updated per Dream)\n\n| Concern | Mitigation |\n|---------|------------|\n| \"Limited novelty — obvious that classification is easier\" | Func-level null result proves it's NOT trivially easier; advantage is complexity+tokenizer-dependent. Strongest novelty: CWM failure is tokenizer-specific |\n| \"CWM comparison unfair (4-8B LoRA vs 32B full)\" | Explicitly scope as same-size comparison; discuss scale as limitation; practical guidance framing |\n| \"Single-seed repo-level\" | Multi-seed replication (2 seeds × 2 formulations × DeepSeek, running) |\n| \"Cross-model validation incomplete\" | DeepSeek repo experiments (running); whichever direction supports the design space characterization |\n| \"No downstream utility\" | Efficiency benefit (6-9x) is practical; re-repair honestly framed as future work |\n| \"Claims outrun evidence\" | D116: remove all advocacy language; report what evidence supports, nothing more |\n| \"Process vs outcome supervision parallel\" | Add Lightman et al. 2023, Uesato et al. 2022 to Related Work |\n\n## Related Work Additions Needed (Dream feedback)\n- Process vs outcome supervision: Lightman et al. 2023, Uesato et al. 2022 (CLS vs TRAJ parallel)\n- CodeRL, AlphaCode, Reflexion (verification-in-the-loop repair)\n- Predictive mutation testing literature (per-test binary classification precedent)\n\n\n## experiment_plan (with registry status)\n\n- id: cwm-baseline\n  claim: 1\n  description: Train CWM generation baseline (Qwen3-4B LoRA, same data/config as MVP-B)\n    to predict execution output instead of pass/fail. Compare per-class F1 against\n    classification model (87.1/87.9%).\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - mvp-b-train\n  status: DONE\n  registry_id: cwm-baseline\n  conclusion: negative\n  metrics:\n    overall_accuracy: 87.51\n    pass_f1: 87.31\n    fail_f1: 87.71\n    pass_precision: 92.06\n    pass_recall: 83.03\n    fail_precision: 83.53\n    fail_recall: 92.32\n    exact_match_rate: 84.02\n    train_loss: 0.2534\n    eval_loss: 0.0644\n    train_runtime_sec: 3439\n    test_set_size: 1890\n    unparseable_predictions: 0\n- id: multi-seed-core\n  claim: 1\n  description: 'Multi-seed validation for core comparison: run classification (mvp-b-train)\n    and CWM baseline each with seeds {0, 1, 42}. Report mean +/- std F1. Statistical\n    significance via paired t-test or bootstrap CI. Required for any claim of ''significantly\n    better''.'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - cwm-baseline\n  registry_id: traj-level-seed0\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 85.66\n    unresolved_f1: 87.37\n    resolved_f1: 83.41\n    unresolved_precision: 82.71\n    unresolved_recall: 92.59\n    resolved_precision: 90.07\n    resolved_recall: 77.66\n    consistency_rate: 79.55\n    train_loss: 0.225\n    eval_loss_epoch1: 0.0949\n    eval_loss_epoch2: 0.0885\n    eval_loss_epoch3: 0.1011\n    train_runtime_sec: 4071.3\n- id: trace-then-judge\n  claim: 1\n  description: 'Trace-then-Judge ablation (chain-of-thought, NOT pipeline): single\n    Qwen3-4B model trained to first generate a brief execution reasoning trace (~50\n    tokens describing expected behavior), then output pass/fail. Same LoRA config/data.\n    Tests whether explicit execution reasoning helps or hurts compared to direct classification.\n    If trace-then-judge >= direct classification, the advantage is from task simplicity,\n    not from skipping reasoning.'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - cwm-baseline\n  registry_id: trace-then-judge\n  status: DONE\n  conclusion: failed\n- id: traj-level-finetuned\n  claim: 1\n  description: 'Same-size fine-tuned trajectory-level baseline: Qwen3-4B LoRA trained\n    to predict resolved/unresolved. Data construction: for each problem_id, aggregate\n    all (code, test) pairs into (code, all_tests_concatenated) -> resolved (original\n    code passes all tests) / unresolved (mutated code fails any test). Same train/val/test\n    split by problem_id. Isolates granularity effect.'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - mvp-b-data-prep\n  registry_id: traj-level-finetuned\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.66\n    unresolved_f1: 87.5\n    resolved_f1: 83.18\n    per_test_consistency: 79.94\n- id: model-size-scaling\n  claim: 1\n  description: Scale classification model from 4B to 8B. Measure accuracy improvement\n    and compare with CWM at 8B. Determine if classification advantage holds across\n    scales.\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - cwm-baseline\n  registry_id: model-size-scaling-cls8b\n  sub_experiments:\n  - registry_id: model-size-scaling-cls8b\n    gpu: seetacloud cuda:0\n    description: Qwen3-8B LoRA classification\n  - registry_id: model-size-scaling-cwm8b\n    gpu: seetacloud cuda:1\n    description: Qwen3-8B LoRA CWM generation\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 90.48\n    pass_f1: 90.86\n    fail_f1: 90.06\n    pass_precision: 90.22\n    pass_recall: 91.51\n    fail_precision: 90.76\n    fail_recall: 89.36\n    train_loss: 0.3125\n    eval_loss_epoch1: 0.0723\n    eval_loss_epoch2: 0.0741\n    eval_loss_epoch3: 0.0783\n    train_runtime_sec: 5614\n    unparseable: 0\n- id: diagnostic-rerepair\n  claim: 2\n  description: 'Downstream proof-of-concept: give repair agent per-test failure predictions\n    vs no per-test info, compare resolve rate on 200 instances. Uses SWE-agent or\n    similar repair framework.'\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - cwm-baseline\n  - traj-level-finetuned\n  status: planned\n- id: per-test-precision-recall\n  claim: 2\n  description: Measure per-test failure prediction precision/recall against ground-truth\n    failing tests on full test set. Evaluate diagnostic signal quality without downstream\n    execution.\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-b-train\n  registry_id: per-test-precision-recall\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.51\n    fail_precision: 82.75\n    fail_recall: 93.64\n    fail_f1: 87.86\n    pass_precision: 93.24\n    pass_recall: 81.8\n    pass_f1: 87.15\n    FP_count: 58\n    FN_count: 178\n    best_mutation: return_value (97.26%)\n    worst_mutation: off_by_one (82.56%)\n    bucket_6_10_acc: 96.3\n    bucket_11plus_acc: 87.12\n- id: oracle-f2p-stratified\n  claim: 3\n  description: Stratified oracle analysis by F2P test count (T=1, T=2, T=3+). Report\n    per-test advantage breakdown showing advantage concentrates in multi-test instances.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - mvp-a-oracle-sim\n  registry_id: oracle-f2p-stratified\n  status: DONE\n  conclusion: success\n  metrics:\n    T1_pct: 68.7\n    T1_block_adv: -0.09\n    T2_pct: 19.1\n    T2_block_adv: 31.69\n    T3_5_pct: 7.1\n    T3_5_block_adv: 40.74\n    T6plus_pct: 5.1\n    T6plus_block_adv: 40.06\n    overall_block_adv: 10.93\n    T2_contribution_pct: 55.3\n- id: oracle-total-validated\n  claim: 3\n  description: Oracle study with Total (F2P+P2P) distribution at empirically measured\n    regression rates. Validate when P2P tests help vs hurt.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - p2p-regression-rate\n  status: DONE\n  registry_id: mvp-a-oracle-sim\n  conclusion: success\n  metrics:\n    original_T12:\n      iid_adv_70_85: 0.1849\n      block_adv_70_85: 0.3618\n    sensitivity_T3:\n      iid_adv_70_85: 0.0761\n      block_adv_70_85: 0.3839\n    sensitivity_T7:\n      iid_adv_70_85: 0.1351\n      block_adv_70_85: 0.3833\n    sensitivity_T11:\n      iid_adv_70_85: 0.1863\n      block_adv_70_85: 0.3639\n    real_f2p_T1:\n      iid_adv_70_85: 0.0198\n      block_adv_70_85: 0.1088\n      pct_T1: 0.687\n      T_median: 1\n      T_mean: 2.3\n    swebench_f2p_stats:\n      median: 1\n      mean: 3\n      P75: 2\n      P90: 3\n    total_reg5pct:\n      iid_adv_70_85: -0.01\n      block_adv_70_85: -0.005\n      pass: false\n    total_reg10pct:\n      iid_adv_70_85: 0.132\n      block_adv_70_85: 0.083\n      pass: true\n    total_reg20pct:\n      iid_adv_70_85: 0.357\n      block_adv_70_85: 0.278\n      pass: true\n- id: block-corr-empirical\n  claim: 3\n  description: 'Empirically validate block-correlation assumption: measure actual\n    prediction error correlation structure from trained model''s test-level predictions,\n    compare with i.i.d. and block-correlated simulation models.'\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - mvp-b-train\n  registry_id: block-corr-empirical\n  status: DONE\n  conclusion: success\n  metrics:\n    icc: 0.1909\n    icc_p_value: 0\n    design_effect: 3.9676\n    overall_error_rate: 0.1249\n    all_correct_observed: 46\n    all_correct_expected_iid: 16.35\n    all_correct_ratio: 2.81\n    error_std_observed: 0.1531\n    error_std_expected_iid: 0.0811\n    error_std_ratio: 1.89\n    n_samples: 1890\n    n_problems: 114\n    inference_precision: bfloat16\n    version: v2_corrected\n- id: swebench-pertest-data\n  claim:\n  - 1\n  - 2\n  - 3\n  description: Docker re-evaluation of SWE-bench Verified patches to extract per-test\n    labels. Build SWE-bench-PerTest dataset (500 instances x 16 candidates). Resource\n    contribution.\n  priority: P1\n  gpu_budget_hours: 0\n  compute_note: CPU/Docker only, ~16-24h with 16 parallel containers. Start early\n    to parallelize with GPU experiments.\n  deps: []\n  status: planned\n- id: repo-level-training\n  claim:\n  - 1\n  - 2\n  description: Fine-tune Qwen3-4B/8B on repo-level (patched_code, test_code) -> pass/fail\n    using SWE-bench-PerTest data. Evaluate on held-out instances.\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - swebench-pertest-data\n  registry_id: repo-level-cwm-v3\n  status: DONE\n  conclusion: failed\n- id: llm-judge-baseline\n  claim:\n  - 1\n  - 3\n  description: Qwen3-8B/32B zero-shot LLM-as-judge baselines (trajectory-level and\n    per-test). Reference points for Pareto frontier.\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: llm-judge-8b-zeroshot\n  sub_experiments:\n  - registry_id: llm-judge-8b-zeroshot\n    gpu: seetacloud cuda:2\n    description: Qwen3-8B zero-shot per-test + trajectory-level\n  - registry_id: llm-judge-32b-zeroshot\n    gpu: seetacloud cuda:3\n    description: Qwen3-32B 4-bit quantized zero-shot\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 64.4\n    fail_precision: 57.9\n    fail_recall: 95.8\n    fail_f1: 72.2\n    pass_precision: 90\n    pass_recall: 35.1\n    pass_f1: 50.5\n    majority_baseline: 51.7\n    accuracy_vs_baseline_gap: 12.6\n    traj_accuracy: 99.1\n    traj_problems: 114\n    traj_true_resolved: 1\n    traj_pred_resolved: 0\n    confusion:\n      TP_fail: 874\n      FN_fail: 38\n      FP_fail: 635\n      TN_fail: 343\n- id: per-test-majority-voting\n  claim: 1\n  description: Per-test majority voting (K=3) with classification model. Test if self-consistency\n    improves per-test accuracy.\n  priority: P2\n  gpu_budget_hours: 3\n  deps:\n  - mvp-b-train\n  registry_id: per-test-majority-voting\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy_greedy: 87.51\n    accuracy_majority_vote_K3: 86.83\n    delta_accuracy: -0.69\n    fail_f1_greedy: 87.86\n    fail_f1_mv: 87.29\n    pass_f1_greedy: 87.15\n    pass_f1_mv: 86.33\n    unanimous_rate: 93.3\n    split_samples: 127\n    flipped_correct_to_wrong: 28\n    flipped_wrong_to_correct: 15\n    net_flips: -13\n    per_pass_accuracy:\n    - 86.72\n    - 86.83\n    - 87.62\n    wall_time_greedy_sec: 30\n    wall_time_mv_sec: 120\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-a-oracle-sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    original_T12:\n      iid_adv_70_85: 0.1849\n      block_adv_70_85: 0.3618\n    sensitivity_T3:\n      iid_adv_70_85: 0.0761\n      block_adv_70_85: 0.3839\n    sensitivity_T7:\n      iid_adv_70_85: 0.1351\n      block_adv_70_85: 0.3833\n    sensitivity_T11:\n      iid_adv_70_85: 0.1863\n      block_adv_70_85: 0.3639\n    real_f2p_T1:\n      iid_adv_70_85: 0.0198\n      block_adv_70_85: 0.1088\n      pct_T1: 0.687\n      T_median: 1\n      T_mean: 2.3\n    swebench_f2p_stats:\n      median: 1\n      mean: 3\n      P75: 2\n      P90: 3\n    total_reg5pct:\n      iid_adv_70_85: -0.01\n      block_adv_70_85: -0.005\n      pass: false\n    total_reg10pct:\n      iid_adv_70_85: 0.132\n      block_adv_70_85: 0.083\n      pass: true\n    total_reg20pct:\n      iid_adv_70_85: 0.357\n      block_adv_70_85: 0.278\n      pass: true\n- exp_id: mvp-b-data-prep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp-b-train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 0.875\n    pass_f1: 0.871\n    fail_f1: 0.879\n    pass_precision: 0.9324\n    pass_recall: 0.818\n    fail_precision: 0.8275\n    fail_recall: 0.9364\n    majority_baseline: 0.52\n    accuracy_vs_majority_gap: 0.355\n- exp_id: p2p-regression-rate\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: cwm-baseline\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    overall_accuracy: 87.51\n    pass_f1: 87.31\n    fail_f1: 87.71\n    pass_precision: 92.06\n    pass_recall: 83.03\n    fail_precision: 83.53\n    fail_recall: 92.32\n    exact_match_rate: 84.02\n    train_loss: 0.2534\n    eval_loss: 0.0644\n    train_runtime_sec: 3439\n    test_set_size: 1890\n    unparseable_predictions: 0\n- exp_id: multi-seed-core\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seed42:\n      accuracy: 87.83\n      pass_f1: 88.06\n      fail_f1: 87.59\n      pass_precision: 89.45\n      pass_recall: 86.71\n      fail_precision: 86.2\n      fail_recall: 89.04\n    seed123:\n      accuracy: 89.52\n      pass_f1: 89.64\n      fail_f1: 89.4\n      pass_precision: 91.76\n      pass_recall: 87.63\n      fail_precision: 87.34\n      fail_recall: 91.56\n    seed456:\n      accuracy: 87.88\n      pass_f1: 87.53\n      fail_f1: 88.21\n      pass_precision: 93.6\n      pass_recall: 82.21\n      fail_precision: 83.12\n      fail_recall: 93.97\n    mean:\n      accuracy: 88.41\n      pass_f1: 88.41\n      fail_f1: 88.4\n    std:\n      accuracy: 0.96\n      pass_f1: 1.1\n      fail_f1: 0.92\n- exp_id: trace-then-judge\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: traj-level-finetuned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.66\n    unresolved_f1: 87.5\n    resolved_f1: 83.18\n    per_test_consistency: 79.94\n- exp_id: model-size-scaling-cls8b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 90.48\n    pass_f1: 90.86\n    fail_f1: 90.06\n    pass_precision: 90.22\n    pass_recall: 91.51\n    fail_precision: 90.76\n    fail_recall: 89.36\n    train_loss: 0.3125\n    eval_loss_epoch1: 0.0723\n    eval_loss_epoch2: 0.0741\n    eval_loss_epoch3: 0.0783\n    train_runtime_sec: 5614\n    unparseable: 0\n- exp_id: model-size-scaling-cwm8b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.67\n    pass_f1: 87.57\n    fail_f1: 87.77\n    pass_precision: 91.53\n    pass_recall: 83.95\n    fail_precision: 84.19\n    fail_recall: 91.67\n    exact_match_rate: 84.39\n    train_loss: 0.229\n    eval_loss_epoch1: 0.0554\n    eval_loss_epoch2: 0.0512\n    eval_loss_epoch3: 0.0564\n    train_runtime_sec: 5570\n    unparseable: 0\n- exp_id: llm-judge-8b-zeroshot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 64.4\n    fail_precision: 57.9\n    fail_recall: 95.8\n    fail_f1: 72.2\n    pass_precision: 90\n    pass_recall: 35.1\n    pass_f1: 50.5\n    majority_baseline: 51.7\n    accuracy_vs_baseline_gap: 12.6\n    traj_accuracy: 99.1\n    traj_problems: 114\n    traj_true_resolved: 1\n    traj_pred_resolved: 0\n    confusion:\n      TP_fail: 874\n      FN_fail: 38\n      FP_fail: 635\n      TN_fail: 343\n- exp_id: llm-judge-32b-zeroshot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 71.69\n    majority_baseline: 51.75\n    accuracy_vs_baseline_gap: 19.95\n    fail_precision: 64.4\n    fail_recall: 92.43\n    fail_f1: 75.91\n    pass_precision: 88.12\n    pass_recall: 52.35\n    pass_f1: 65.68\n    unparseable_predictions: 0\n    trajectory_accuracy: 99.12\n    trajectory_total_problems: 114\n    trajectory_correct: 113\n    trajectory_true_resolved: 1\n    trajectory_pred_resolved: 0\n- exp_id: per-test-precision-recall\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.51\n    fail_precision: 82.75\n    fail_recall: 93.64\n    fail_f1: 87.86\n    pass_precision: 93.24\n    pass_recall: 81.8\n    pass_f1: 87.15\n    FP_count: 58\n    FN_count: 178\n    best_mutation: return_value (97.26%)\n    worst_mutation: off_by_one (82.56%)\n    bucket_6_10_acc: 96.3\n    bucket_11plus_acc: 87.12\n- exp_id: oracle-f2p-stratified\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    T1_pct: 68.7\n    T1_block_adv: -0.09\n    T2_pct: 19.1\n    T2_block_adv: 31.69\n    T3_5_pct: 7.1\n    T3_5_block_adv: 40.74\n    T6plus_pct: 5.1\n    T6plus_block_adv: 40.06\n    overall_block_adv: 10.93\n    T2_contribution_pct: 55.3\n- exp_id: traj-level-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 85.47\n    unresolved_f1: 87\n    resolved_f1: 83.52\n    unresolved_precision: 83.53\n    unresolved_recall: 90.78\n    resolved_precision: 88.17\n    resolved_recall: 79.33\n    consistency_rate: 78.59\n- exp_id: traj-level-seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 87.4\n    unresolved_f1: 88.7\n    resolved_f1: 85.8\n    unresolved_precision: 85.7\n    unresolved_recall: 91.9\n    resolved_precision: 89.7\n    resolved_recall: 82.3\n    consistency_rate: 78.8\n- exp_id: per-test-majority-voting\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy_greedy: 87.51\n    accuracy_majority_vote_K3: 86.83\n    delta_accuracy: -0.69\n    fail_f1_greedy: 87.86\n    fail_f1_mv: 87.29\n    pass_f1_greedy: 87.15\n    pass_f1_mv: 86.33\n    unanimous_rate: 93.3\n    split_samples: 127\n    flipped_correct_to_wrong: 28\n    flipped_wrong_to_correct: 15\n    net_flips: -13\n    per_pass_accuracy:\n    - 86.72\n    - 86.83\n    - 87.62\n    wall_time_greedy_sec: 30\n    wall_time_mv_sec: 120\n- exp_id: block-corr-empirical\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    icc: 0.1909\n    icc_p_value: 0\n    design_effect: 3.9676\n    overall_error_rate: 0.1249\n    all_correct_observed: 46\n    all_correct_expected_iid: 16.35\n    all_correct_ratio: 2.81\n    error_std_observed: 0.1531\n    error_std_expected_iid: 0.0811\n    error_std_ratio: 1.89\n    n_samples: 1890\n    n_problems: 114\n    inference_precision: bfloat16\n    version: v2_corrected\n- exp_id: traj-level-seed789\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 87.31\n    unresolved_f1: 88.27\n    resolved_f1: 86.17\n    unresolved_precision: 87.41\n    unresolved_recall: 89.15\n    resolved_precision: 87.18\n    resolved_recall: 85.18\n    consistency_rate: 76.74\n    eval_loss: 0.1115\n    train_loss: 0.2255\n    train_runtime_sec: 2055.9\n- exp_id: traj-level-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 85.66\n    unresolved_f1: 87.37\n    resolved_f1: 83.41\n    unresolved_precision: 82.71\n    unresolved_recall: 92.59\n    resolved_precision: 90.07\n    resolved_recall: 77.66\n    consistency_rate: 79.55\n    train_loss: 0.225\n    eval_loss_epoch1: 0.0949\n    eval_loss_epoch2: 0.0885\n    eval_loss_epoch3: 0.1011\n    train_runtime_sec: 4071.3\n- exp_id: cls8b-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 89.4\n    pass_f1: 89.5\n    fail_f1: 89.2\n    pass_precision: 91.2\n    pass_recall: 87.9\n    fail_precision: 87.5\n    fail_recall: 90.9\n    train_loss: 0.3087\n    eval_loss: 0.0848\n    train_runtime_sec: 5666\n    unparseable: 0\n- exp_id: cwm8b-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 86.98\n    pass_f1: 86.83\n    fail_f1: 87.13\n    pass_precision: 91.12\n    pass_recall: 82.92\n    fail_precision: 83.3\n    fail_recall: 91.34\n    exact_match_rate: 84.13\n    unparseable: 0\n    test_set_size: 1890\n- exp_id: cls-seed789\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 89\n    pass_f1: 88.9\n    fail_f1: 89.1\n    pass_precision: 93.3\n    pass_recall: 84.9\n    fail_precision: 85.2\n    fail_recall: 93.4\n- exp_id: cls-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.94\n    pass_f1: 87.79\n    fail_f1: 88.08\n    pass_precision: 92.13\n    pass_recall: 83.84\n    fail_precision: 84.2\n    fail_recall: 92.32\n    train_loss: 0.2347\n    eval_loss: 0.0963\n    train_runtime_sec: 4976.75\n    unparseable: 0\n- exp_id: repo-level-cls\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cwm-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 87.2\n    pass_f1: 86.95\n    fail_f1: 87.44\n    exact_match_rate: 84.44\n    majority_baseline_accuracy: 51.75\n    accuracy_vs_baseline_gap_pp: 35.45\n    test_set_size: 1890\n    unparseable_predictions: 0\n- exp_id: cwm-seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 86.98\n    pass_f1: 86.66\n    fail_f1: 87.29\n    pass_precision: 92.26\n    pass_recall: 81.7\n    fail_precision: 82.52\n    fail_recall: 92.65\n    exact_match_rate: 84.02\n    train_loss: 0.2525\n    eval_loss_best: 0.0551\n    eval_loss_final: 0.0635\n    train_runtime_sec: 3440\n    unparseable: 0\n- exp_id: cwm-seed789\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 86.67\n    pass_f1: 86.74\n    fail_f1: 86.6\n    exact_match_rate: 83.97\n    baseline_gap_pp: 34.92\n    test_set_size: 1890\n    unparseable_predictions: 0\n    per_class:\n      fail:\n        precision: 84.09\n        recall: 89.25\n        f1: 86.6\n      pass:\n        precision: 89.37\n        recall: 84.25\n        f1: 86.74\n- exp_id: cwm-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 87.57\n    fail_f1: 87.93\n    fail_precision: 82.71\n    fail_recall: 93.86\n    pass_f1: 87.18\n    pass_precision: 93.45\n    pass_recall: 81.7\n    exact_match_rate: 84.29\n    eval_loss: 0.0665\n    train_loss: 0.2554\n    train_runtime_sec: 3586\n- exp_id: 5-paired-clustered-bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pooled_gap_pp: -0.45\n    pooled_ci_lower: -1.71\n    pooled_ci_upper: 0.84\n    pooled_p_value: 0.499\n    tost_p_value: 0.0071\n    tost_margin_pp: 2\n    seed_level_paired_t_p: 0.425\n    seed_level_mean_gap: -0.48\n    n_variants_pooled: 523\n    n_clusters: 114\n    per_seed_gaps:\n      seed42: -0.97\n      seed123: 1.45\n      seed456: -1.84\n      seed789: -0.78\n      seed0: -0.29\n- exp_id: cwm8b-seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 86.24\n    pass_f1: 85.96\n    fail_f1: 86.51\n    pass_precision: 91.08\n    pass_recall: 81.39\n    fail_precision: 82.09\n    fail_recall: 91.45\n    exact_match_rate: 82.8\n    train_loss: 0.2279\n    eval_loss: 0.0583\n    unparseable: 0\n    test_set_size: 1890\n    majority_baseline_accuracy: 51.75\n    accuracy_vs_baseline_gap_pp: 34.5\n- exp_id: cls8b-seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 88.31\n    pass_f1: 88.2\n    fail_f1: 88.41\n    pass_precision: 92.29\n    pass_recall: 84.46\n    fail_precision: 84.72\n    fail_recall: 92.43\n    train_loss: 0.3105\n    eval_loss: 0.0928\n    unparseable: 0\n    test_set_size: 1890\n- exp_id: repo-level-cls-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-home\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6611\n    f1_macro: 0.5661\n    f1_pass: 0.769\n    f1_fail: 0.363\n    precision_pass: 0.765\n    recall_pass: 0.774\n    precision_fail: 0.369\n    recall_fail: 0.357\n    majority_baseline: 0.7296\n    n_unparseable: 132\n    best_checkpoint: checkpoint-200\n    early_stop: D045\n- exp_id: cls8b-eval-seed42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 90.48\n    pass_f1: 90.86\n    fail_f1: 90.06\n    pass_precision: 90.22\n    pass_recall: 91.51\n    fail_precision: 90.76\n    fail_recall: 89.36\n    unparseable: 0\n    test_set_size: 1890\n- exp_id: cls8b-eval-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 89.37\n    pass_f1: 89.54\n    fail_f1: 89.19\n    pass_precision: 91.2\n    pass_recall: 87.93\n    fail_precision: 87.54\n    fail_recall: 90.9\n    unparseable: 0\n    test_set_size: 1890\n- exp_id: matched-seed-8b-predictions\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: repo-level-cwm-v4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: repo-level-cwm-v5\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v6\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v7\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v8\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-v9\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-seed123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: repo-level-cwm-seed123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: repo-level-cwm-v10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6991\n    f1_macro: 0.4671\n    f1_pass: 0.8187\n    f1_fail: 0.1154\n    precision_pass: 0.7304\n    recall_pass: 0.9314\n    precision_fail: 0.2815\n    recall_fail: 0.0726\n    majority_baseline: 0.7296\n    n_unparseable: 9102\n    n_unparseable_pct: 0.93\n    n_truncated: 478\n    n_truncated_pct: 0.0489\n    truncated_accuracy: 0.2176\n    best_checkpoint: checkpoint-400\n    early_stop: D045\n    eval_invalid: max_new_tokens=64 caused 93% unparseable (D047)\n- exp_id: repo-level-cls-v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checkpoint_sweep:\n      ckpt_600:\n        accuracy: 76.74\n        f1_macro: 73.74\n        fail_f1: 64.88\n        pass_f1: 82.61\n      ckpt_4000:\n        accuracy: 81.51\n        f1_macro: 72.56\n        fail_f1: 56.9\n        pass_f1: 88.23\n      ckpt_4200:\n        accuracy: 80.64\n        f1_macro: 72.1\n        fail_f1: 56.66\n        pass_f1: 87.54\n      ckpt_4400:\n        accuracy: 82.11\n        f1_macro: 73.94\n        fail_f1: 59.34\n        fail_precision: 77.02\n        fail_recall: 48.26\n      ckpt_4600:\n        accuracy: 82.35\n        f1_macro: 74.74\n        fail_f1: 60.87\n        pass_f1: 88.6\n        fail_precision: 76\n        fail_recall: 50.76\n    best_checkpoint_accuracy: checkpoint-4600\n    best_checkpoint_f1: checkpoint-4600\n    eval_samples: 9784\n    accuracy: 82.35\n    f1_macro: 74.74\n    unparseable: 132\n    unparseable_pct: 1.3\n    majority_baseline: 72.96\n    gap_vs_baseline: 9.39\n    eval_server: home-1x5090\n    eval_env: transformers 4.57.6\n    note: Test set sweep complete. ckpt-4600 best on both accuracy (82.35%) and f1_macro\n      (74.74%).\n    val_2048:\n      ckpt_600:\n        accuracy: 77.25\n        f1_macro: 70.81\n        fail_f1: 57.11\n        pass_f1: 84.52\n      ckpt_4000:\n        accuracy: 83.32\n        f1_macro: 70.26\n        fail_f1: 50.56\n        pass_f1: 89.97\n      ckpt_4200:\n        accuracy: 82.82\n        f1_macro: 69.54\n        fail_f1: 49.43\n        pass_f1: 89.65\n      ckpt_4400:\n        accuracy: 83.49\n        f1_macro: 71.63\n        fail_f1: 53.29\n        pass_f1: 89.97\n      ckpt_4600:\n        accuracy: 83.63\n        f1_macro: 71.72\n        fail_f1: 53.36\n        pass_f1: 90.07\n      eval_samples: 9335\n      unparseable: 1883\n      unparseable_pct: 20.2\n      val_best_f1: ckpt-4600\n      val_best_acc: ckpt-4600\n      note: 'val-test 一致: 都是 ckpt-4600'\n- exp_id: repo-level-cwm-v11\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    eval_checkpoint: checkpoint-600\n    eval_samples: 500\n    eval_type: subset500_tok1024\n    accuracy: 66.6\n    fail_f1: 27.7\n    pass_f1: 78.3\n    f1_macro: 52.99\n    fail_precision: 33.3\n    fail_recall: 23.7\n    pass_precision: 74.5\n    pass_recall: 82.5\n    unparseable: 376\n    unparseable_pct: 75.2\n    majority_baseline: 73\n    gap_vs_baseline: -6.4\n    gen_length_mean: 3398.1\n    gen_length_median: 3307.5\n    gen_length_max: 7582\n    confusion:\n      TP: 301\n      TN: 32\n      FP: 103\n      FN: 64\n- exp_id: repo-level-cls-8b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    eval_checkpoint: checkpoint-200\n    eval_samples: 9784\n    accuracy: 71.37\n    fail_f1: 60.57\n    pass_f1: 77.53\n    f1_macro: 69.05\n    fail_precision: 48.26\n    fail_recall: 81.29\n    pass_precision: 90.71\n    pass_recall: 67.69\n    unparseable: 136\n    unparseable_pct: 1.39\n    majority_baseline: 73\n    gap_vs_baseline: -1.63\n    confusion:\n      TP: 4832\n      TN: 2151\n      FP: 495\n      FN: 2306\n    eval_server: westd-48478\n    eval_env: transformers 5.8.0\n- exp_id: repo-level-cls-seed123-home\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    val_2048:\n      n: 9335\n      unparseable: 1883\n      ckpt_200:\n        accuracy: 62.51\n        f1_macro: 55.54\n        f1_pass: 73.14\n        f1_fail: 37.94\n      ckpt_400:\n        accuracy: 80.72\n        f1_macro: 67.03\n        f1_pass: 88.27\n        f1_fail: 45.78\n      ckpt_600:\n        accuracy: 76.78\n        f1_macro: 66.81\n        f1_pass: 85\n        f1_fail: 48.63\n      ckpt_800:\n        accuracy: 81.81\n        f1_macro: 69.14\n        f1_pass: 88.91\n        f1_fail: 49.37\n      ckpt_1000:\n        accuracy: 82.3\n        f1_macro: 67.63\n        f1_pass: 89.42\n        f1_fail: 45.84\n      best_f1: ckpt_800\n      best_acc: ckpt_1000\n    val_4096:\n      n: 9335\n      unparseable: 1406\n      ckpt_400:\n        accuracy: 82.57\n        f1_macro: 71.24\n        f1_pass: 89.29\n        f1_fail: 53.18\n      ckpt_600:\n        accuracy: 79.18\n        f1_macro: 70.73\n        f1_pass: 86.45\n        f1_fail: 55\n      ckpt_800:\n        accuracy: 83.7\n        f1_macro: 73.31\n        f1_pass: 90\n        f1_fail: 56.7\n      best_f1: ckpt_800\n      best_acc: ckpt_800\n    val_5120:\n      n: 9335\n      unparseable: 0\n      truncated: 234\n      ckpt_400:\n        accuracy: 86.01\n        f1_macro: 79.66\n        f1_pass: 91.02\n        f1_fail: 68.3\n      ckpt_600:\n        accuracy: 81.89\n        f1_macro: 77.01\n        f1_pass: 87.6\n        f1_fail: 66.43\n      ckpt_800:\n        accuracy: 87.92\n        f1_macro: 81.95\n        f1_pass: 92.33\n        f1_fail: 71.57\n      best_f1: ckpt_800\n      best_acc: ckpt_800\n- exp_id: repo-level-cwm-v12\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    eval_test_accuracy: 58.04\n    eval_test_f1_macro: 51.67\n    eval_test_f1_fail: 34.12\n    eval_test_f1_pass: 69.22\n    eval_test_unparseable: 5255\n    eval_test_total: 9784\n    eval_test_unparseable_rate: 53.7\n    eval_checkpoint: checkpoint-500\n- exp_id: repo-level-cwm-seed123-conda\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    eval_test_accuracy: 59.09\n    eval_test_f1_macro: 43.43\n    eval_test_f1_fail: 13.67\n    eval_test_f1_pass: 73.19\n    eval_test_unparseable: 6574\n    eval_test_total: 9784\n    eval_test_unparseable_rate: 67.2\n    eval_checkpoint: checkpoint-500\n- exp_id: repo-level-cls-8b-conda\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    val_8192:\n      ckpt_200:\n        accuracy: 63.52\n        f1_macro: 61.17\n        f1_fail: 51.6\n        f1_pass: 70.7\n        unparseable: 9\n      ckpt_400:\n        accuracy: 80.96\n      ckpt_600:\n        accuracy: 85\n      best_acc: ckpt_600\n    val_5120:\n      ckpt_400:\n        accuracy: 80.47\n        f1_macro: 75.84\n    test_2048:\n      ckpt_400:\n        accuracy: 84.52\n        f1_macro: 80.89\n      ckpt_600:\n        accuracy: 78.51\n    test_8192:\n      ckpt_400:\n        accuracy: 84.79\n        f1_macro: 81.18\n        f1_fail: 72.93\n        f1_pass: 89.43\n        unparseable: 0\n        total: 9784\n      ckpt_600:\n        accuracy: 79.05\n        f1_macro: 75.12\n        f1_fail: 65.24\n        f1_pass: 85\n        unparseable: 0\n        total: 9784\n- exp_id: repo-level-cls-v5-conda\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checkpoint_sweep:\n      ckpt_200:\n        accuracy: 52.96\n        f1_macro: 52.89\n        fail_f1: 51.02\n        pass_f1: 54.76\n      ckpt_400:\n        accuracy: 78.43\n        f1_macro: 68.41\n        fail_f1: 50.61\n        pass_f1: 86.21\n        fail_precision: 66.48\n        fail_recall: 40.85\n        pass_precision: 80.82\n        pass_recall: 92.36\n      ckpt_600:\n        accuracy: 76.37\n        f1_macro: 71.17\n        fail_f1: 58.93\n        pass_f1: 83.41\n        fail_precision: 55.6\n        fail_recall: 62.7\n        pass_precision: 85.49\n        pass_recall: 81.44\n    best_checkpoint_accuracy: checkpoint-400\n    best_checkpoint_f1: checkpoint-600\n    eval_samples: 9784\n    accuracy: 78.43\n    f1_macro: 71.17\n    unparseable: 132\n    unparseable_pct: 1.35\n    majority_baseline: 72.96\n    eval_server: westd-48478\n    eval_env: conda, transformers 4.57.6\n- exp_id: repo-level-cwm-8b-conda\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-8b-seed123-conda\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-8b-conda-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-8b-seed123-conda-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cwm-8b-conda-v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: repo-level-cls-8b-seed123-conda-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: repo-level-cwm-8b-conda-v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-ckpt3000-test-eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-ckpt3000-test-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt3000-val-eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: repo-level-cls-8b-s42-ckpt200-val\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt3000-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 88.69\n    f1_macro: 81.73\n    f1_fail: 70.5\n    f1_pass: 93\n    precision_fail: 95.2\n    precision_pass: 87.6\n    recall_fail: 55.9\n    recall_pass: 99.1\n    majority_baseline: 75.9\n    gap_vs_majority_pp: 12.8\n    unparseable: 9\n    total: 9335\n- exp_id: cls8b-s42-ckpt400-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.79\n    f1_macro: 81.18\n    f1_fail: 72.93\n    f1_pass: 89.43\n    precision_fail: 70.32\n    precision_pass: 90.74\n    recall_fail: 75.74\n    recall_pass: 88.15\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 11.84\n    unparseable: 0\n    total: 9784\n- exp_id: cls4b-seed123-ckpt800-val5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.92\n    f1_macro: 81.95\n    f1_pass: 92.33\n    f1_fail: 71.57\n    unparseable: 0\n    truncated: 234\n    total: 9335\n- exp_id: cls8b-s42-ckpt600-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 79.05\n    f1_macro: 75.12\n    f1_fail: 65.24\n    f1_pass: 85\n    precision_fail: 59.16\n    precision_pass: 88.95\n    recall_fail: 72.71\n    recall_pass: 81.4\n    unparseable: 0\n    total: 9784\n    majority_baseline: 73\n    gap_vs_majority_pp: 6.09\n- exp_id: repo-level-cls-8b-s42-resume\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_steps: 6633\n    epochs: 3\n    train_time_sec: 74425\n    final_train_loss: 0.4284\n    final_eval_loss: 0.4768\n    best_eval_loss_resume: 0.2516\n    best_eval_loss_resume_step: 4200\n    best_eval_loss_overall: 0.0796\n    best_eval_loss_overall_step: 200\n    checkpoints_saved: 32\n    overfitting: true\n    note: Severe overfitting after epoch 2. Resume-best=ckpt-4200. Val sweep running\n      on cuda:0.\n- exp_id: cls8b-s42-ckpt200-val8192-eval-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 63.52\n    f1_macro: 61.17\n    f1_fail: 51.6\n    f1_pass: 70.7\n    unparseable: 9\n    total: 9335\n- exp_id: cls4b-v5-val5120-sweep-home\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-v5-ckpt600-val5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 82.82\n    f1_macro: 79.81\n    f1_fail: 72.03\n    f1_pass: 87.6\n    precision_fail: 59.3\n    recall_fail: 91.7\n    unparseable: 0\n    total: 9335\n- exp_id: cls8b-s42-ckpt800-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.5\n    f1_macro: 79.2\n- exp_id: cls4b-v5-ckpt4000-val5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 89.84\n    f1_macro: 84.25\n    f1_fail: 74.85\n    f1_pass: 93.64\n    precision_fail: 92.95\n    recall_fail: 62.66\n    precision_pass: 89.24\n    recall_pass: 98.49\n    unparseable: 0\n    truncated: 234\n    total: 9335\n- exp_id: cls8b-s42-ckpt1000-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 88.23\n    f1_macro: 82.72\n    f1_fail: 73\n    f1_pass: 92.5\n    precision_fail: 81.8\n    recall_fail: 65.8\n    precision_pass: 89.8\n    recall_pass: 95.3\n    unparseable: 9\n    total_instances: 9335\n- exp_id: cls4b-v5-ckpt4400-val5120-eval\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    accuracy_partial_70pct: 89.69\n    f1_macro_partial_70pct: 84.61\n    samples_completed: 6544\n    samples_total: 9335\n- exp_id: cls8b-s42-ckpt1000-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.52\n    f1_macro: 77.5\n    f1_fail: 65.85\n    f1_pass: 89.14\n    precision_fail: 74.93\n    recall_fail: 58.73\n    precision_pass: 85.84\n    recall_pass: 92.72\n    majority_baseline: 72.96\n    gap_vs_majority: 10.56\n    unparseable_count: 0\n    unparseable_rate: 0\n    total_samples: 9784\n    tp: 6618\n    fp: 1092\n    fn: 520\n    tn: 1554\n- exp_id: cls4b-v5-ckpt4400-val5120-eval-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1200-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1400-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.97\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 10.09\n    f1_macro: 77.15\n    f1_fail: 62.95\n    f1_pass: 91.34\n    precision_fail: 86.68\n    precision_pass: 85.85\n    recall_fail: 49.42\n    recall_pass: 97.59\n    n_instances: 9335\n    n_unparseable: 9\n    confusion_matrix:\n      tn: 1113\n      fp: 1139\n      fn: 171\n      tp: 6912\n- exp_id: cls8b-s42-ckpt1600-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-v5-val-sweep-ckpt4600\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 90.07\n    f1_macro: 85.04\n    f1_fail: 76.37\n    f1_pass: 93.71\n    precision_fail: 89.65\n    recall_fail: 66.52\n    precision_pass: 90.16\n    recall_pass: 97.56\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 14.19\n    unparseable_count: 0\n    total_samples: 9335\n    n_truncated: 234\n- exp_id: cls4b-v5-val-sweep-ckpt4200\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 89.06\n    f1_macro: 83.07\n    f1_fail: 73\n    f1_pass: 93.1\n    precision_fail: 90.3\n    recall_fail: 61.3\n    precision_pass: 88.8\n    recall_pass: 97.9\n- exp_id: cls4b-v5-val-sweep-ckpt4400\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1200-val8192\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-v5-val-sweep-ckpt4400-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 89.96\n    f1_macro: 84.94\n    f1_fail: 76.25\n    f1_pass: 93.64\n    precision_fail: 88.84\n    precision_pass: 90.21\n    recall_fail: 66.79\n    recall_pass: 97.33\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 14.09\n    n_instances: 9335\n    n_truncated: 234\n    n_unparseable: 0\n- exp_id: cls8b-s42-ckpt1200-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.84\n    f1_macro: 77.47\n    f1_fail: 65.49\n    f1_pass: 89.45\n    precision_fail: 77.52\n    recall_fail: 56.69\n    precision_pass: 85.4\n    recall_pass: 93.91\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 10.89\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-s42-ckpt1400-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.47\n    f1_macro: 78.9\n    f1_fail: 67.13\n    f1_pass: 90.67\n    precision_fail: 86.43\n    recall_fail: 54.88\n    precision_pass: 85.27\n    recall_pass: 96.81\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 12.51\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-s42-ckpt1600-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.99\n    f1_macro: 78.94\n    f1_fail: 67.65\n    f1_pass: 90.22\n    precision_fail: 81.06\n    recall_fail: 58.05\n    precision_pass: 85.93\n    recall_pass: 94.97\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 12.03\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-s42-ckpt1200-val8192-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1200-val8192-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.76\n    f1_macro: 81.25\n    f1_fail: 70.2\n    f1_pass: 92.3\n    precision_fail: 85\n    recall_fail: 59.8\n    precision_pass: 88.3\n    recall_pass: 96.7\n    majority_baseline: 75.9\n    gap_vs_majority: 11.9\n    unparseable: 9\n- exp_id: cls8b-s42-ckpt1600-val8192-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 86.75\n    f1_macro: 78.94\n    f1_fail: 66.12\n    f1_pass: 91.76\n    precision_fail: 86.28\n    precision_pass: 86.83\n    recall_fail: 53.6\n    recall_pass: 97.29\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 10.87\n    unparseable: 9\n    total: 9335\n- exp_id: cls8b-s42-ckpt800-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.53\n    f1_macro: 78.97\n    f1_fail: 69.17\n    f1_pass: 88.77\n    precision_fail: 70.07\n    recall_fail: 68.29\n    precision_pass: 88.36\n    recall_pass: 89.18\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 10.58\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6600-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.23\n    f1_macro: 79.02\n    f1_fail: 65.9\n    f1_pass: 92.14\n    precision_fail: 92.6\n    recall_fail: 51.15\n    precision_pass: 86.4\n    recall_pass: 98.7\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 11.36\n    unparseable_count: 9\n    total_samples: 9335\n- exp_id: cls4b-v5-ckpt4600-test-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.63\n    f1_macro: 75.63\n    f1_fail: 61.67\n    f1_pass: 89.59\n    precision_fail: 84.03\n    recall_fail: 48.72\n    precision_pass: 83.55\n    recall_pass: 96.57\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 10.67\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6400-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.48\n    f1_macro: 79.66\n    f1_fail: 67.04\n    f1_pass: 92.27\n    precision_fail: 91.81\n    recall_fail: 52.8\n    precision_pass: 86.78\n    recall_pass: 98.5\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 11.6\n    unparseable_count: 9\n    total_samples: 9335\n- exp_id: cls8b-seed123-ckpt6200-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.52\n    f1_macro: 79.26\n    f1_fail: 66.16\n    f1_pass: 92.35\n    precision_fail: 95.63\n    recall_fail: 50.58\n    precision_pass: 86.33\n    recall_pass: 99.27\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 11.64\n    unparseable_count: 9\n    total_samples: 9335\n- exp_id: cls4b-v5-ckpt4400-test5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.24\n    f1_macro: 74.44\n    f1_fail: 59.45\n    f1_pass: 89.44\n    precision_fail: 85.98\n    recall_fail: 45.43\n    precision_pass: 82.78\n    recall_pass: 97.25\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 10.28\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt3000-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.6\n    f1_macro: 78.38\n    f1_fail: 65.89\n    f1_pass: 90.87\n    precision_fail: 91.65\n    recall_fail: 51.44\n    precision_pass: 84.52\n    recall_pass: 98.26\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 12.64\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6633-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.1\n    f1_macro: 78.79\n    f1_fail: 65.52\n    f1_pass: 92.07\n    precision_fail: 92.26\n    recall_fail: 50.8\n    precision_pass: 86.31\n    recall_pass: 98.64\n    majority_baseline: 75.88\n    gap_vs_majority_pp: 11.23\n    unparseable_count: 9\n    total_samples: 9335\n- exp_id: cls8b-seed123-ckpt3000-test8192-eval-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-seed123-ckpt800-test5120-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls4b-seed123-ckpt800-test5120-eval-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 75.33\n    f1_macro: 67.03\n    f1_fail: 50.5\n    f1_pass: 83.6\n    precision_fail: 55.2\n    recall_fail: 46.5\n    precision_pass: 81.3\n    recall_pass: 86\n    majority_baseline: 73\n    gap_vs_majority_pp: 2.4\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6200-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt6400-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt200-val8192-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt6200-test-eval-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.7\n    f1_fail: 63.71\n    f1_pass: 90.31\n    f1_macro: 77.01\n    precision_fail: 88.84\n    precision_pass: 83.96\n    recall_fail: 49.66\n    recall_pass: 97.69\n    n_instances: 9784\n    n_cls_unparseable: 0\n- exp_id: cls8b-seed123-ckpt6400-test-eval-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.08\n    f1_fail: 65.32\n    f1_pass: 90.49\n    f1_macro: 77.91\n    precision_fail: 87.92\n    precision_pass: 84.54\n    recall_fail: 51.97\n    recall_pass: 97.35\n    n_instances: 9784\n    n_cls_unparseable: 0\n- exp_id: cls4b-v5-ckpt600-test5120-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 77.74\n    f1_macro: 74.74\n    f1_fail: 66.03\n    f1_pass: 83.44\n    precision_fail: 56.21\n    recall_fail: 80.01\n    majority_baseline: 72.96\n    gap_vs_majority_pp: 4.78\n    unparseable_count: 0\n    total_samples: 9784\n- exp_id: cls8b-seed123-ckpt6600-test-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.9\n    f1_macro: 77.58\n    pass_f1: 90.4\n    fail_f1: 64.8\n    pass_precision: 84.3\n    pass_recall: 97.4\n    fail_precision: 87.8\n    fail_recall: 51.3\n    n_samples: 9784\n    n_pass: 7138\n    n_fail: 2646\n    majority_baseline: 73\n    unparseable: 0\n    confusion_matrix:\n      fail_as_fail: 1357\n      fail_as_pass: 1289\n      pass_as_fail: 188\n      pass_as_pass: 6950\n- exp_id: cls8b-s42-ckpt200-test8192-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 70.07\n    f1_macro: 68.18\n    pass_f1: 75.9\n    fail_f1: 60.4\n    pass_precision: 91.8\n    pass_recall: 64.7\n    fail_precision: 47\n    fail_recall: 84.5\n    n_samples: 9784\n    n_pass: 7138\n    n_fail: 2646\n    majority_baseline: 73\n    unparseable: 0\n    confusion_matrix:\n      fail_as_fail: 2235\n      fail_as_pass: 411\n      pass_as_fail: 2517\n      pass_as_pass: 4621\n- exp_id: cls8b-s42-ckpt1000-test-seq2048-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 82.83\n    f1_macro: 76.88\n    fail_precision: 72.2\n    fail_recall: 59.3\n    fail_f1: 65.2\n    pass_precision: 85.9\n    pass_recall: 91.5\n    pass_f1: 88.6\n    unparseable: 136\n- exp_id: cls4b-v5-ckpt4000-test5120-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-seed123-ckpt6633-test-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.89\n    f1_macro: 77.56\n    f1_fail: 64.7\n    f1_pass: 90.4\n    precision_fail: 87.8\n    recall_fail: 51.2\n    precision_pass: 84.3\n    recall_pass: 97.4\n    majority_baseline: 73\n    gap_vs_majority_pp: 11.9\n    total_samples: 9784\n    unparseable_count: 0\n- exp_id: cls8b-seed123-ckpt200-test-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 72.55\n    f1_macro: 70.18\n    pass_f1: 78.58\n    fail_f1: 61.78\n    pass_precision: 91.21\n    pass_recall: 69.02\n    fail_precision: 49.54\n    fail_recall: 82.05\n    n_samples: 9784\n    n_pass: 7138\n    n_fail: 2646\n    majority_baseline: 72.96\n    unparseable: 0\n    confusion_matrix:\n      tn: 2171\n      fp: 475\n      fn: 2211\n      tp: 4927\n- exp_id: cwm8b-ckpt400-test-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cwm-rank32-ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm-4b-rank32-ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm-rank32-ablation-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87\n    exact_match_rate: 83.4\n    fail_f1: 87.1\n    pass_f1: 86.9\n    train_loss_final: 0.0152\n    train_loss_avg: 0.2536\n    eval_loss: 0.0688\n    train_runtime_sec: 5003\n    test_set_size: 1890\n    vs_rank16_baseline: -0.51\n    rank16_baseline_accuracy: 87.51\n- exp_id: cwm-rank64-ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm-4b-rank64-ablation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: s42-extended-val-sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cwm-rank32-alpha64-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 87.04\n    pass_f1: 86.79\n    fail_f1: 87.27\n    f1_macro: 87.03\n    pass_precision: 91.8\n    pass_recall: 82.3\n    fail_precision: 82.9\n    fail_recall: 92.1\n    exact_match_rate: 84.55\n    train_loss: 0.2069\n    eval_loss: 0.0606\n    n_instances: 1890\n    vs_rank16_baseline: -0.47\n    rank16_baseline_accuracy: 87.51\n- exp_id: cls8b-s42-extended-val-sweep\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: s42-extended-val-sweep-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep-seq8192\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep-seq4096\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep-seq8192-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: repo-level-cwm-8b-conda-v5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: cls8b-s42-resume-val-sweep-gpu1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-resume-ckpt1000-test-mutation\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cls8b-s42-ckpt1000-test-mutation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-ckpt3600-test\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: cls8b-s42-resume-ckpt3600-mutation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 84.4849\n    overall_correct: 8266\n    overall_total: 9784\n    gold_accuracy: 96.2443\n    gold_correct: 4459\n    gold_total: 4633\n    mutation_operator_swap_accuracy: 81.3822\n    mutation_operator_swap_correct: 2732\n    mutation_operator_swap_total: 3357\n    mutation_off_by_one_accuracy: 86.8852\n    mutation_off_by_one_correct: 159\n    mutation_off_by_one_total: 183\n    mutation_return_value_accuracy: 75.4448\n    mutation_return_value_correct: 424\n    mutation_return_value_total: 562\n    mutation_boundary_removal_accuracy: 46.9018\n    mutation_boundary_removal_correct: 492\n    mutation_boundary_removal_total: 1049\n- exp_id: cls8b-s42-ckpt3600-seq2048-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.04\n    f1_macro: 76.8\n    unparseable: 136\n    n_samples: 9784\n    seq_length: 2048\n- exp_id: repo-level-cwm-8b-conda-v6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm8b-ckpt400-test-eval-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cwm8b-ckpt400-test-eval-v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: cls8b-s42-resume-ckpt3600-test-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 84.48\n    f1_macro: 78.17\n    fail_recall: 56.8\n    pass_recall: 94.8\n    n_samples: 9784\n    note: reproduces v1 exactly\n- exp_id: cls8b-seed123-ckpt3000-mutation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 85.6\n    boundary_removal: 44.9\n    operator_swap: 82.6\n    return_value: 66.4\n    off_by_one: 79.2\n    gold: 99.6\n    n_samples: 9784\n- exp_id: cwm8b-ckpt400-test-eval-shard2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: cls4b-ckpt4600-test-mutation-pr\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 83.63\n    gold_acc: 98.25\n    operator_swap_acc: 78.91\n    return_value_acc: 67.97\n    off_by_one_acc: 58.47\n    boundary_removal_acc: 46.9\n    n_instances: 9784\n    note: off_by_one recall_fail=0 (all predicted pass); boundary_removal identical\n      to 8B\n- exp_id: cwm4b-s42-mutation-breakdown\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_accuracy: 58.04\n    parseable_rate: 46.3\n    parseable_only_accuracy: 42.9\n    gold_parse_rate: 43.5\n    gold_parseable_acc: 23.5\n    operator_swap_parse_rate: 56.9\n    operator_swap_parseable_acc: 63.1\n    off_by_one_parse_rate: 4.4\n    off_by_one_parseable_acc: 0\n    return_value_parse_rate: 48.8\n    return_value_parseable_acc: 27\n    boundary_removal_parse_rate: 30.6\n    boundary_removal_parseable_acc: 59.2\n    n_instances: 9784\n- exp_id: cwm8b-ckpt400-test-eval-shard3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: cwm8b-ckpt400-test-eval-shard4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: deepseek-cls-repo\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: deepseek-cwm-func\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.04292\n    train_time_seconds: 5215\n    test_accuracy: 85.77\n    test_f1_macro: 85.73\n    test_precision_fail: 80.07\n    test_precision_pass: 93.18\n    test_recall_fail: 93.86\n    test_recall_pass: 78.22\n    test_unparseable_rate: 0\n    test_n: 1890\n- exp_id: deepseek-cls-func\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.0701\n    train_time_seconds: 5444\n    test_accuracy: 86.93\n    test_f1_macro: 86.92\n    test_precision_fail: 86.42\n    test_precision_pass: 87.41\n    test_recall_fail: 86.51\n    test_recall_pass: 87.32\n    test_n: 1890\n- exp_id: deepseek-cwm-func-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.0408\n    train_time_seconds: 5244\n    test_accuracy: 87.88\n    test_f1_macro: 87.88\n    test_precision_fail: 83.78\n    test_precision_pass: 92.61\n    test_recall_fail: 92.87\n    test_recall_pass: 83.23\n    test_unparseable_rate: 0\n    test_n: 1890\n- exp_id: deepseek-cwm-repo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.021\n    eval_loss: NaN\n    total_steps: 13266\n    epochs: 3\n    wall_clock_seconds: 112680\n    gpu_hours: 31.3\n    note: eval_loss=NaN is known DeepSeek issue, does not affect training quality\n- exp_id: re-repair-phase0\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    control_mean_sim: 0.82\n    cls_diag_mean_sim: 0.818\n    oracle_diag_mean_sim: 0.809\n    random_diag_mean_sim: 0.719\n    n_instances: 10\n    n_conditions: 4\n    samples_per_condition: 3\n- exp_id: deepseek-cls-func-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.06753\n    train_time_seconds: 5391\n    test_accuracy: 86.77\n    test_f1_macro: 86.77\n    test_precision_fail: 84.99\n    test_precision_pass: 88.56\n    test_recall_fail: 88.16\n    test_recall_pass: 85.48\n    test_unparseable_rate: 0\n    test_n: 1890\n- exp_id: deepseek-traj-func\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss_epoch1: 0.0943\n    eval_loss_epoch2: 0.0793\n    eval_loss_epoch3: 0.0884\n    best_eval_loss: 0.0793\n    best_step: 1008\n    best_epoch: 2\n    train_loss: 0.1131\n    train_runtime_sec: 2910.6\n- exp_id: deepseek-traj-func-s123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: deepseek-traj-func-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.0796\n    best_step: 504\n    test_accuracy: 0.8324\n    majority_baseline: 0.5359\n    train_loss: 0.0857\n    train_runtime_seconds: 3069.6\n- exp_id: deepseek-traj-func-v2-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_eval_loss: 0.077\n    best_step: 504\n    test_accuracy: 0.8508\n    majority_baseline: 0.5359\n    train_loss: 0.0842\n    train_runtime_seconds: 3021\n    per_test_consistency: 0.782\n- exp_id: deepseek-traj-func-v2-fixed\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: deepseek-traj-func-v2-s123-fixed\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: deepseek-traj-repo\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 0.771\n    best_eval_loss: 0.111\n    best_step: 98\n    train_loss: 0.12\n    unparseable_rate: 0.167\n    resolved_recall: 0.962\n    unresolved_recall: 0.545\n    total_test: 48\n- exp_id: deepseek-traj-repo-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 0.771\n    best_eval_loss: 0.1147\n    best_step: 98\n    train_loss: 0.12\n    unparseable_rate: 0.167\n    resolved_recall: 0.962\n    unresolved_recall: 0.545\n    total_test: 48\n- exp_id: deepseek-traj-repo-8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 81.25\n    unparseable: 0\n    best_eval_loss: 0.1216\n    best_epoch: 2\n    train_truncated_pct: 2.1\n    gpu_mem_mib: 22475\n    resolved_f1: 84.21\n    unresolved_f1: 76.92\n- exp_id: deepseek-traj-repo-8k-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 75\n    unparseable: 0\n    best_eval_loss: 0.1182\n    best_epoch: 2\n    train_truncated_pct: 2.1\n    gpu_mem_mib: 21399\n    resolved_f1: 76.92\n    unresolved_f1: 72.73\n- exp_id: deepseek-traj-repo-8k-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 75\n    f1_macro: 72.68\n    majority_baseline: 54.2\n    gap_vs_majority_pp: 20.8\n    unresolved_f1: 64.7\n    resolved_f1: 80.6\n    unresolved_precision: 91.7\n    unresolved_recall: 50\n    resolved_precision: 69.4\n    resolved_recall: 96.2\n    per_test_consistency: 75\n    unparseable_rate: 0\n    test_n: 48\n    train_loss_final: 0.2125\n    eval_loss_best: 0.1013\n- exp_id: deepseek-traj-repo-8k-s789\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 66.67\n    resolved_f1: 75\n    unresolved_f1: 50\n    best_eval_loss: 0.1295\n    unparseable: 0\n- exp_id: deepseek-traj-repo-8k-s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 75\n    unparseable: 0\n    best_eval_loss: 0.1547\n    resolved_f1: 75\n    unresolved_f1: 75\n    f1_macro: 75\n    train_loss: 0.2176\n- exp_id: deepseek-traj-repo-8k-s999\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 79.2\n    unparseable: 0\n    best_eval_loss: 0.1565\n    resolved_f1: 82.1\n    unresolved_f1: 75\n    f1_macro: 78.57\n    train_loss: 0.2184\n- exp_id: deepseek-cls-repo-s123\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n- exp_id: deepseek-cwm-repo-s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: deepseek-cls-repo-resume\n  name: ''\n  status: ALLOCATED\n  conclusion: killed\n  metrics: {}\n- exp_id: deepseek-cls-repo-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: deepseek-cls-repo-v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: deepseek-cls-repo-v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    train_loss_final: 0.0065\n    eval_loss: NaN (all epochs)\n    total_steps_completed: 4422\n    max_steps: 6633\n    error: Process killed during epoch 3 eval (49% progress); eval_loss=NaN at all\n      epochs; no best checkpoint; last saved checkpoint=step-4422\n- exp_id: re-repair-docker-eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    A1_pass1: 52.3\n    A2_pass1: 43.2\n    B_pass1: 36.4\n    C_pass1: 38.6\n    D_pass1: 40.9\n    n_instances: 44\n    error_rate: 38.6\n    total_samples: 1475\n- exp_id: qwen3-8b-traj-func-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 87.6\n    eval_loss: 0.0975\n    train_loss: 0.0312\n    unparseable: 0\n    pass_f1: 85.96\n    fail_f1: 88.89\n    per_test_consistency: 78.78\n    total_steps: 756\n    test_set_size: 1032\n    eval_script: eval_traj_verifier_8b.py\n    note: 87.98% from eval_traj_verifier.py (model.cuda) also valid; 4/1032 samples\n      differ due to bf16 placement\n- exp_id: qwen3-8b-traj-func-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    test_accuracy: 87.79\n    best_eval_loss: 0.0782\n    pass_f1: 86.74\n    fail_f1: 88.69\n    unparseable: 0\n    per_test_consistency: 76.07\n    total_steps: 756\n    test_set_size: 1032\n    eval_script: eval_traj_verifier_8b.py\n- exp_id: deepseek-cls-repo-v5\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: deepseek-cwm-repo-s42-epoch2-eval\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: repo-level-0shot-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.499\n    pass_f1: 0.4895\n    fail_f1: 0.5081\n    unparseable_rate: 0\n    unparseable_count: 0\n    total_samples: 9784\n    runtime_seconds: 1018.2\n    confusion:\n      TP: 2350\n      FP: 114\n      TN: 2532\n      FN: 4788\n- exp_id: repo-level-3shot-baseline\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: deepseek-0shot-repo-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.4854\n    pass_f1: 0.647\n    fail_f1: 0.0509\n    unparseable_rate: 0.087\n    unparseable_count: 851\n    total_samples: 9784\n    runtime_seconds: 1545\n    confusion:\n      TP: 4614\n      FP: 2511\n      TN: 135\n      FN: 2524\n- exp_id: qwen3-0shot-func-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6873\n    pass_f1: 0.655\n    fail_f1: 0.7141\n    unparseable_rate: 0.0032\n    unparseable_count: 6\n    total_samples: 1890\n    runtime_seconds: 96\n    confusion:\n      TP: 561\n      FP: 174\n      TN: 738\n      FN: 417\n- exp_id: deepseek-0shot-func-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6302\n    pass_f1: 0.7196\n    fail_f1: 0.4569\n    unparseable_rate: 0.0106\n    unparseable_count: 20\n    total_samples: 1890\n    runtime_seconds: 113\n    confusion:\n      TP: 897\n      FP: 618\n      TN: 294\n      FN: 81\n- exp_id: D124-cwm-s42-epoch2-eval\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-18T17:24:59.563Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T17:24:59.563Z",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b"
}
```

---

## Round 1

34 recorded events

### User

_source line 3 · 2026-05-18T17:24:59.588Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：DeepSeek repo-level 全部失败（延续 v1-v4 的 pattern），只有 Qwen 单模型族的 repo-level 数据，cross-model 验证仅限 func-level
核心假设：['deepseek-cls-repo-v5 训练失败或 acc ≤ majority baseline（~73%）', 'deepseek-cwm-repo eval 不可用（crash、unparseable >80%、或 acc 远低于 baseline）', 'Repo-level 结论完全依赖 Qwen 单模型族——reviewer 会质疑 generalizability', 'DeepSeek TRAJ repo 是唯一跑通的 DeepSeek repo-level 实验，但 n=48 太小', 'Func-level 双模型族数据完整且 clean，但 repo-level 是 paper 的 differentiator']
关键指标范围：{'deepseek_cls_repo_acc': [50, 73], 'deepseek_cwm_repo_acc': [40, 60], 'deepseek_cwm_repo_unparseable_pct': [70, 95], 'qwen_cls_repo_best_acc': [83, 86], 'qwen_cwm_repo_best_parseable_acc': [42, 58], 'func_level_all_formulations_acc_range': [83, 90], 'expected_reviewer_score': [2.5, 3.0]}
叙事方向：核心 reframe: 放弃 repo-level 作为 main contribution，转为 secondary finding。 新 angle 选项 (仍冲 EMNLP main): (1) "Per-Test vs Trajectory-Level Verification: A Controlled Study" — 将 CLS vs TRAJ 的 粒度-效率 tradeoff 提为核心贡献（双模型族 func-level 数据完整 + Qwen repo-level 作 case study）。 强调 per-test 在 accuracy 不损失前提下提供 diagnostic granularity + 6-9x speedup。 TOST equivalence p=0.007 是 solid statistical result。 (2) Block-correlation empirical validation (ICC=0.19, design effect=4.0) 作为 methodological contribution——揭示 per-test evaluation 中 i.i.d. 假设不成立的系统性偏差。 (3) CWM repo-level failure analysis 降为一个 section 而非 core claim，explicitly scope 为 "Qwen3 case study, cross-model validation as future work"。 Re-repair negative result 诚实报告为 future work motivation。 Efficiency + diagnostic granularity + statistical methodology 三条线撑起 paper。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: exec-sim-repair-verifier
focus: 论文经过 D116 framing pivot、D126 三层 framing、D135 overtraining→evaluation sensitivity 重设计后，和 Round 1 时已大幅改变。重点评估：(1) R2-W1 新颖性是否足以达到 EMNLP main 4.0; (2) 当前 contribution framing 是否清晰有力; (3) 写作质量和 story 连贯性; (4) 还有什么具体改进能把分数从 borderline 推到 accept

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
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.021
    eval_loss: NaN
    total_steps: 13266
    epochs: 3
    wall_clock_seconds: 112680
    gpu_hours: 31.3
    note: eval_loss=NaN is known DeepSeek issue, does not affect training quality
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
  status: ANALYZING
  conclusion: ''
  metrics: {}
- exp_id: deepseek-cwm-repo-s123
  name: ''
  status: DONE
  conclusion: failed
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
  status: DONE
  conclusion: failed
  metrics:
    train_loss_final: 0.0065
    eval_loss: NaN (all epochs)
    total_steps_completed: 4422
    max_steps: 6633
    error: Process killed during epoch 3 eval (49% progress); eval_loss=NaN at all
      epochs; no best checkpoint; last saved checkpoint=step-4422
- exp_id: re-repair-docker-eval
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    A1_pass1: 52.3
    A2_pass1: 43.2
    B_pass1: 36.4
    C_pass1: 38.6
    D_pass1: 40.9
    n_instances: 44
    error_rate: 38.6
    total_samples: 1475
- exp_id: qwen3-8b-traj-func-s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    test_accuracy: 87.6
    eval_loss: 0.0975
    train_loss: 0.0312
    unparseable: 0
    pass_f1: 85.96
    fail_f1: 88.89
    per_test_consistency: 78.78
    total_steps: 756
    test_set_size: 1032
    eval_script: eval_traj_verifier_8b.py
    note: 87.98% from eval_traj_verifier.py (model.cuda) also valid; 4/1032 samples
      differ due to bf16 placement
- exp_id: qwen3-8b-traj-func-s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    test_accuracy: 87.79
    best_eval_loss: 0.0782
    pass_f1: 86.74
    fail_f1: 88.69
    unparseable: 0
    per_test_consistency: 76.07
    total_steps: 756
    test_set_size: 1032
    eval_script: eval_traj_verifier_8b.py
- exp_id: deepseek-cls-repo-v5
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: deepseek-cwm-repo-s42-epoch2-eval
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: repo-level-0shot-baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.499
    pass_f1: 0.4895
    fail_f1: 0.5081
    unparseable_rate: 0
    unparseable_count: 0
    total_samples: 9784
    runtime_seconds: 1018.2
    confusion:
      TP: 2350
      FP: 114
      TN: 2532
      FN: 4788
- exp_id: repo-level-3shot-baseline
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: deepseek-0shot-repo-baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.4854
    pass_f1: 0.647
    fail_f1: 0.0509
    unparseable_rate: 0.087
    unparseable_count: 851
    total_samples: 9784
    runtime_seconds: 1545
    confusion:
      TP: 4614
      FP: 2511
      TN: 135
      FN: 2524
- exp_id: qwen3-0shot-func-baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.6873
    pass_f1: 0.655
    fail_f1: 0.7141
    unparseable_rate: 0.0032
    unparseable_count: 6
    total_samples: 1890
    runtime_seconds: 96
    confusion:
      TP: 561
      FP: 174
      TN: 738
      FN: 417
- exp_id: deepseek-0shot-func-baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.6302
    pass_f1: 0.7196
    fail_f1: 0.4569
    unparseable_rate: 0.0106
    unparseable_count: 20
    total_samples: 1890
    runtime_seconds: 113
    confusion:
      TP: 897
      FP: 618
      TN: 294
      FN: 81
- exp_id: D124-cwm-s42-epoch2-eval
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}

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
  "promptId": "4d7675b4-77fa-4209-a180-3e83688a8172",
  "type": "user",
  "uuid": "ffe032e3-a03e-461b-abdd-c0b69330c3e7",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T17:24:59.586Z_

```json
{
  "parentUuid": "ffe032e3-a03e-461b-abdd-c0b69330c3e7",
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
  "uuid": "1de3199f-062a-402e-bd59-329d0b00955c",
  "timestamp": "2026-05-18T17:24:59.586Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T17:24:59.586Z_

```json
{
  "parentUuid": "1de3199f-062a-402e-bd59-329d0b00955c",
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
  "uuid": "4aaf0df8-a431-4e7b-b305-105cd759e23a",
  "timestamp": "2026-05-18T17:24:59.586Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-18T17:24:59.586Z_

```json
{
  "parentUuid": "4aaf0df8-a431-4e7b-b305-105cd759e23a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f3dc6ce0-a5f0-4787-bc29-48752385c5f1",
  "timestamp": "2026-05-18T17:24:59.586Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：DeepSeek repo-level 全部失败（延续 v1-v4 的 pattern），只有 Qwen 单模型族的 repo-level 数据，cross-model 验证仅限 func-level 核心假设：['deepseek-cls-repo-v5 训练失败或 acc ≤ majority base…",
  "leafUuid": "f3dc6ce0-a5f0-4787-bc29-48752385c5f1",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Design space characterization for neural code verification",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b"
}
```

---

### Assistant

_source line 9 · 2026-05-18T17:25:02.493Z_

Let me review the experiment plan and registry data to generate detailed worst-tier predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3dc6ce0-a5f0-4787-bc29-48752385c5f1",
  "isSidechain": false,
  "requestId": "req_011CbARZTh59cLKnPtd1DaES",
  "type": "assistant",
  "uuid": "d8f29671-34e2-439d-947b-192249a41b58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ULgA768F4MNo15cQvZeigu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 34927,
      "cache_read_input_tokens": 11447,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34927,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 228,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 34927,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34927
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

_source line 10 · 2026-05-18T17:25:07.271Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015o3uNFQHf89PoTWa8EGPJG`</summary>

```json
{
  "description": "Find experiment plan details",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_16, search for files related to experiment_plan, planned experiments, and any YAML/JSON files that define experiments with status \"planned\" or \"PREPARING\". I need to find all experiments that are not yet DONE — specifically those with status \"planned\", \"PREPARING\", or \"ALLOCATED\". Look in files like experiment_plan.yaml, registry.yaml, CLAUDE.md, and any other config files. Report the full content of any such entries.",
  "subagent_type": "Explore"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8f29671-34e2-439d-947b-192249a41b58",
  "isSidechain": false,
  "requestId": "req_011CbARZTh59cLKnPtd1DaES",
  "type": "assistant",
  "uuid": "3b8ed7ef-33b2-43ed-915f-bc07fa4ce797",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ULgA768F4MNo15cQvZeigu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 34927,
      "cache_read_input_tokens": 11447,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34927,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 228,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 34927,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34927
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

_source line 11 · 2026-05-18T17:25:41.343Z_

<details><summary>↩ Tool result · `toolu_015o3uNFQHf89PoTWa8EGPJG`</summary>

```text
Perfect! Now let me create a comprehensive summary by reading the content of the experiment_plan.yaml more carefully and extracting all PREPARING entries:

Based on my comprehensive search of the directory `/home/ubuntu/.agent-ml-research-idea_gen_0509_16`, I have found extensive information about experiments with status "PREPARING" (not yet done). Here's the complete report:

## Summary of Found Experiments

**Main Registry File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/global/registry.yaml`

**Experiment Plan File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/experiment_plan.yaml`

---

## Experiments with Status "PREPARING" (43 total)

All of the following experiments have `status: PREPARING` in the registry:

### Training/Core Experiments:
1. **repo-level-cls-8b-seed123-conda-v2** - CLS 8B resume attempt (failed with FileNotFoundError)
2. **cls8b-seed123-ckpt3000-val8192-eval** - Evaluation of CLS 8B checkpoint-3000 on val split
3. **repo-level-cls-8b-s42-resume** - Resume CLS 8B s42 training from ckpt-600 with checkpoint sweep
4. **repo-level-cwm-8b-conda-v4** - CWM 8B training (failed due to timeout at step 5273/6633, needs resume)
5. **cls8b-s42-resume-val-sweep-seq8192-v2** - Validation sweep on 21 checkpoints (1800-5800) at seq8192
6. **repo-level-cwm-8b-conda-v5** - CWM 8B resume from ckpt-5200 (started successfully)

### Killed/Superseded Experiments:
7. **cls8b-s42-ckpt1000-test-mutation** - Superseded (val-best changed from ckpt-1000 to ckpt-3600)
8. **cls8b-s42-resume-ckpt1000-test-mutation** - Superseded (val-best changed from ckpt-1000 to ckpt-3600)

### DeepSeek TRAJ Function-Level:
9. **deepseek-traj-func** - TRAJ func-level on DeepSeek (has metrics but status PREPARING)
10. **deepseek-traj-func-v2-fixed** - TRAJ func-level v2-fixed (correct train_traj_verifier.py)
11. **deepseek-traj-func-v2-s123-fixed** - TRAJ func-level v2-fixed seed=123

### DeepSeek TRAJ Repo-Level (Multi-seed):
12. **deepseek-traj-repo-8k-s123** - TRAJ repo-level seed=123 replication
13. **deepseek-traj-repo-8k-s0** - TRAJ repo-level seed=0 replication
14. **deepseek-traj-repo-8k-s789** - TRAJ repo-level seed=789 replication
15. **deepseek-traj-repo-8k-s456** - TRAJ repo-level seed=456 replication

### DeepSeek CWM:
16. **deepseek-cwm-func-s123** - DeepSeek CWM func-level seed=123

### Qwen Repo-Level:
17. **p2p-regression-rate** - Per-test verifier pass-to-pass regression detection study
18. **repo-level-cls-8b-conda** - CLS 8B conda retrain (transformers 4.57.6)
19. **repo-level-cls-v5-conda** - CLS 4B seed42 conda retrain for cross-server comparison

### Checkpoint Evals & Ablations:
20. **cls8b-s42-resume-ckpt3600-test-v2** - CLS 8B ckpt-3600 test eval v2 (verify 84.48% accuracy)
21. **cls8b-s42-ckpt400-test8192-eval** - Early CLS 8B ckpt-400 test eval at seq8192
22. **cls8b-s42-ckpt1600-val8192-v2** - CLS 8B ckpt-1600 val eval at seq8192
23. **cls4b-v5-val-sweep-ckpt4200** - CLS 4B v5 ckpt-4200 val eval at seq5120
24. **cls4b-ckpt4600-test-mutation-pr** - CLS 4B ckpt-4600 per-mutation breakdown

### CWM Ablations/Shards:
25. **cwm4b-s42-mutation-breakdown** - CWM 4B mutation breakdown analysis
26. **cwm8b-ckpt400-test-eval-shard2** - CWM 8B ckpt-400 test eval shard 2 (partial)

### Multi-Seed Core Studies:
27. **cls-seed0** - CLS seed=0 replication (parent: multi-seed-core)
28. **cls-seed789** - CLS seed=789 replication (parent: multi-seed-core)
29. **cwm-seed0** - CWM seed=0 replication (parent: cwm-baseline)
30. **cwm-seed123** - CWM seed=123 replication (parent: cwm-baseline)
31. **cwm-seed456** - CWM seed=456 replication (parent: cwm-baseline)
32. **cwm-seed789** - CWM seed=789 replication (parent: cwm-baseline)
33. **traj-level-seed456** - Trajectory-level seed=456 replication (parent: traj-level-finetuned)

### Model Size Scaling:
34. **cls8b-seed123** - CLS 8B seed=123 (parent: model-size-scaling-cls8b)
35. **cls8b-seed456** - CLS 8B seed=456 (parent: model-size-scaling-cls8b)
36. **cwm8b-seed123** - CWM 8B seed=123 (parent: model-size-scaling-cwm8b)
37. **cwm8b-seed456** - CWM 8B seed=456 (parent: model-size-scaling-cwm8b)

### DeepSeek CLS Repo-Level (Versions):
38. **repo-level-cls-v4** - CLS parent experiment v4
39. **cwm-rank32-ablation-v2** - CWM rank32 ablation v2
40. **deepseek-cls-repo-v2** - DeepSeek CLS repo-level v2
41. **deepseek-cls-repo-v3** - DeepSeek CLS repo-level v3

### CWM Epoch Comparisons (D132 Series):
42. **D132-cwm-s42-epoch2-seq4096** - CWM s42 epoch 2 @seq4096 (killed, superseded)
43. **D132-cwm-s123-epoch3-seq4096** - CWM s123 epoch 3 @seq4096 (killed, superseded)
44. **D132-cwm-s42-e2-seq2048** - CWM s42 epoch 2 @seq2048 canonical (killed, superseded)
45. **D132-cwm-s123-e2-seq2048** - CWM s123 epoch 2 @seq2048 canonical

---

## Experiments with Status "ALLOCATED" (11 total)

These are checkpoint files indicating allocation to GPU/compute resources:
1. D124-cwm-s42-epoch2-eval
2. D131-cwm-s42-epoch3-seq2048
3. cls8b-s42-ckpt3600-seq2048-ablation
4. deepseek-cls-func-s123
5. deepseek-cls-repo-s123
6. deepseek-cls-repo-v4
7. deepseek-cls-repo-v5
8. deepseek-cwm-repo-s123
9. deepseek-cwm-repo-s42-epoch2-eval
10. deepseek-traj-repo-s123
11. deepseek-traj-repo

---

## Key Notes:

- **Location of registry:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/global/registry.yaml`
- **Location of experiment plan:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/experiment_plan.yaml`
- **RUNNING experiments (3):** `deepseek-cwm-repo-s123`, `deepseek-cls-repo-v5`, `D131-cwm-s42-epoch3-seq2048`, `D133-cwm-s42-e2-seq2048-home`
- Most PREPARING experiments are hypothesis-driven multi-seed validations, ablation studies, and checkpoint evaluations for paper Table reporting
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b8ed7ef-33b2-43ed-915f-bc07fa4ce797",
  "isSidechain": false,
  "promptId": "4d7675b4-77fa-4209-a180-3e83688a8172",
  "type": "user",
  "uuid": "e09b63ac-d4d7-4ec6-bc5c-7dbef5bf9804",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_16, search for files related to experiment_plan, planned experiments, and any YAML/JSON files that define experiments with status \"planned\" or \"PREPARING\". I need to find all experiments that are not yet DONE — specifically those with status \"planned\", \"PREPARING\", or \"ALLOCATED\". Look in files like experiment_plan.yaml, registry.yaml, CLAUDE.md, and any other config files. Report the full content of any such entries.",
    "agentId": "a3a7db43986499ae0",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me create a comprehensive summary by reading the content of the experiment_plan.yaml more carefully and extracting all PREPARING entries:\n\nBased on my comprehensive search of the directory `/home/ubuntu/.agent-ml-research-idea_gen_0509_16`, I have found extensive information about experiments with status \"PREPARING\" (not yet done). Here's the complete report:\n\n## Summary of Found Experiments\n\n**Main Registry File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/global/registry.yaml`\n\n**Experiment Plan File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/experiment_plan.yaml`\n\n---\n\n## Experiments with Status \"PREPARING\" (43 total)\n\nAll of the following experiments have `status: PREPARING` in the registry:\n\n### Training/Core Experiments:\n1. **repo-level-cls-8b-seed123-conda-v2** - CLS 8B resume attempt (failed with FileNotFoundError)\n2. **cls8b-seed123-ckpt3000-val8192-eval** - Evaluation of CLS 8B checkpoint-3000 on val split\n3. **repo-level-cls-8b-s42-resume** - Resume CLS 8B s42 training from ckpt-600 with checkpoint sweep\n4. **repo-level-cwm-8b-conda-v4** - CWM 8B training (failed due to timeout at step 5273/6633, needs resume)\n5. **cls8b-s42-resume-val-sweep-seq8192-v2** - Validation sweep on 21 checkpoints (1800-5800) at seq8192\n6. **repo-level-cwm-8b-conda-v5** - CWM 8B resume from ckpt-5200 (started successfully)\n\n### Killed/Superseded Experiments:\n7. **cls8b-s42-ckpt1000-test-mutation** - Superseded (val-best changed from ckpt-1000 to ckpt-3600)\n8. **cls8b-s42-resume-ckpt1000-test-mutation** - Superseded (val-best changed from ckpt-1000 to ckpt-3600)\n\n### DeepSeek TRAJ Function-Level:\n9. **deepseek-traj-func** - TRAJ func-level on DeepSeek (has metrics but status PREPARING)\n10. **deepseek-traj-func-v2-fixed** - TRAJ func-level v2-fixed (correct train_traj_verifier.py)\n11. **deepseek-traj-func-v2-s123-fixed** - TRAJ func-level v2-fixed seed=123\n\n### DeepSeek TRAJ Repo-Level (Multi-seed):\n12. **deepseek-traj-repo-8k-s123** - TRAJ repo-level seed=123 replication\n13. **deepseek-traj-repo-8k-s0** - TRAJ repo-level seed=0 replication\n14. **deepseek-traj-repo-8k-s789** - TRAJ repo-level seed=789 replication\n15. **deepseek-traj-repo-8k-s456** - TRAJ repo-level seed=456 replication\n\n### DeepSeek CWM:\n16. **deepseek-cwm-func-s123** - DeepSeek CWM func-level seed=123\n\n### Qwen Repo-Level:\n17. **p2p-regression-rate** - Per-test verifier pass-to-pass regression detection study\n18. **repo-level-cls-8b-conda** - CLS 8B conda retrain (transformers 4.57.6)\n19. **repo-level-cls-v5-conda** - CLS 4B seed42 conda retrain for cross-server comparison\n\n### Checkpoint Evals & Ablations:\n20. **cls8b-s42-resume-ckpt3600-test-v2** - CLS 8B ckpt-3600 test eval v2 (verify 84.48% accuracy)\n21. **cls8b-s42-ckpt400-test8192-eval** - Early CLS 8B ckpt-400 test eval at seq8192\n22. **cls8b-s42-ckpt1600-val8192-v2** - CLS 8B ckpt-1600 val eval at seq8192\n23. **cls4b-v5-val-sweep-ckpt4200** - CLS 4B v5 ckpt-4200 val eval at seq5120\n24. **cls4b-ckpt4600-test-mutation-pr** - CLS 4B ckpt-4600 per-mutation breakdown\n\n### CWM Ablations/Shards:\n25. **cwm4b-s42-mutation-breakdown** - CWM 4B mutation breakdown analysis\n26. **cwm8b-ckpt400-test-eval-shard2** - CWM 8B ckpt-400 test eval shard 2 (partial)\n\n### Multi-Seed Core Studies:\n27. **cls-seed0** - CLS seed=0 replication (parent: multi-seed-core)\n28. **cls-seed789** - CLS seed=789 replication (parent: multi-seed-core)\n29. **cwm-seed0** - CWM seed=0 replication (parent: cwm-baseline)\n30. **cwm-seed123** - CWM seed=123 replication (parent: cwm-baseline)\n31. **cwm-seed456** - CWM seed=456 replication (parent: cwm-baseline)\n32. **cwm-seed789** - CWM seed=789 replication (parent: cwm-baseline)\n33. **traj-level-seed456** - Trajectory-level seed=456 replication (parent: traj-level-finetuned)\n\n### Model Size Scaling:\n34. **cls8b-seed123** - CLS 8B seed=123 (parent: model-size-scaling-cls8b)\n35. **cls8b-seed456** - CLS 8B seed=456 (parent: model-size-scaling-cls8b)\n36. **cwm8b-seed123** - CWM 8B seed=123 (parent: model-size-scaling-cwm8b)\n37. **cwm8b-seed456** - CWM 8B seed=456 (parent: model-size-scaling-cwm8b)\n\n### DeepSeek CLS Repo-Level (Versions):\n38. **repo-level-cls-v4** - CLS parent experiment v4\n39. **cwm-rank32-ablation-v2** - CWM rank32 ablation v2\n40. **deepseek-cls-repo-v2** - DeepSeek CLS repo-level v2\n41. **deepseek-cls-repo-v3** - DeepSeek CLS repo-level v3\n\n### CWM Epoch Comparisons (D132 Series):\n42. **D132-cwm-s42-epoch2-seq4096** - CWM s42 epoch 2 @seq4096 (killed, superseded)\n43. **D132-cwm-s123-epoch3-seq4096** - CWM s123 epoch 3 @seq4096 (killed, superseded)\n44. **D132-cwm-s42-e2-seq2048** - CWM s42 epoch 2 @seq2048 canonical (killed, superseded)\n45. **D132-cwm-s123-e2-seq2048** - CWM s123 epoch 2 @seq2048 canonical\n\n---\n\n## Experiments with Status \"ALLOCATED\" (11 total)\n\nThese are checkpoint files indicating allocation to GPU/compute resources:\n1. D124-cwm-s42-epoch2-eval\n2. D131-cwm-s42-epoch3-seq2048\n3. cls8b-s42-ckpt3600-seq2048-ablation\n4. deepseek-cls-func-s123\n5. deepseek-cls-repo-s123\n6. deepseek-cls-repo-v4\n7. deepseek-cls-repo-v5\n8. deepseek-cwm-repo-s123\n9. deepseek-cwm-repo-s42-epoch2-eval\n10. deepseek-traj-repo-s123\n11. deepseek-traj-repo\n\n---\n\n## Key Notes:\n\n- **Location of registry:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/global/registry.yaml`\n- **Location of experiment plan:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/experiment_plan.yaml`\n- **RUNNING experiments (3):** `deepseek-cwm-repo-s123`, `deepseek-cls-repo-v5`, `D131-cwm-s42-epoch3-seq2048`, `D133-cwm-s42-e2-seq2048-home`\n- Most PREPARING experiments are hypothesis-driven multi-seed validations, ablation studies, and checkpoint evaluations for paper Table reporting"
      }
    ],
    "totalDurationMs": 34065,
    "totalTokens": 73437,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 70093,
      "output_tokens": 2318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1020
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2318,
          "cache_read_input_tokens": 70093,
          "cache_creation_input_tokens": 1020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1020,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 1,
      "bashCount": 7,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "3b8ed7ef-33b2-43ed-915f-bc07fa4ce797",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T17:25:43.730Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K1yaqwi8F8xJQ8boXqCvEw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e09b63ac-d4d7-4ec6-bc5c-7dbef5bf9804",
  "isSidechain": false,
  "requestId": "req_011CbARcY5a8W3rwpbDMoeu5",
  "type": "assistant",
  "uuid": "a12711c8-6978-4fd2-9871-55d9c7b180c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rt5DM9WjCWgp1qTdqtiij9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2555,
      "cache_read_input_tokens": 46374,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 46374,
          "cache_creation_input_tokens": 2555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2555
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

_source line 13 · 2026-05-18T17:25:43.739Z_

<details><summary>↩ Tool result · `toolu_01K1yaqwi8F8xJQ8boXqCvEw`</summary>

```text
1	experiments:
2	- id: cwm-baseline
3	  claim: 1
4	  description: Train CWM generation baseline (Qwen3-4B LoRA, same data/config as MVP-B)
5	    to predict execution output instead of pass/fail. Compare per-class F1 against
6	    classification model (87.1/87.9%).
7	  priority: P0
8	  gpu_budget_hours: 2
9	  deps:
10	  - mvp-b-train
11	  status: PREPARING
12	  registry_id: cwm-baseline
13	- id: multi-seed-core
14	  claim: 1
15	  description: 'Multi-seed validation for core comparison: run classification (mvp-b-train)
16	    and CWM baseline each with seeds {0, 1, 42}. Report mean +/- std F1. Statistical
17	    significance via paired t-test or bootstrap CI. Required for any claim of ''significantly
18	    better''.'
19	  priority: P0
20	  gpu_budget_hours: 8
21	  deps:
22	  - cwm-baseline
23	  registry_id: traj-level-seed0
24	- id: trace-then-judge
25	  claim: 1
26	  description: 'Trace-then-Judge ablation (chain-of-thought, NOT pipeline): single
27	    Qwen3-4B model trained to first generate a brief execution reasoning trace (~50
28	    tokens describing expected behavior), then output pass/fail. Same LoRA config/data.
29	    Tests whether explicit execution reasoning helps or hurts compared to direct classification.
30	    If trace-then-judge >= direct classification, the advantage is from task simplicity,
31	    not from skipping reasoning.'
32	  priority: P0
33	  gpu_budget_hours: 4
34	  deps:
35	  - cwm-baseline
36	  registry_id: trace-then-judge
37	- id: traj-level-finetuned
38	  claim: 1
39	  description: 'Same-size fine-tuned trajectory-level baseline: Qwen3-4B LoRA trained
40	    to predict resolved/unresolved. Data construction: for each problem_id, aggregate
41	    all (code, test) pairs into (code, all_tests_concatenated) -> resolved (original
42	    code passes all tests) / unresolved (mutated code fails any test). Same train/val/test
43	    split by problem_id. Isolates granularity effect.'
44	  priority: P0
45	  gpu_budget_hours: 2
46	  deps:
47	  - mvp-b-data-prep
48	  registry_id: traj-level-finetuned
49	- id: model-size-scaling
50	  claim: 1
51	  description: Scale classification model from 4B to 8B. Measure accuracy improvement
52	    and compare with CWM at 8B. Determine if classification advantage holds across
53	    scales.
54	  priority: P1
55	  gpu_budget_hours: 8
56	  deps:
57	  - cwm-baseline
58	  registry_id: model-size-scaling-cls8b
59	  sub_experiments:
60	  - registry_id: model-size-scaling-cls8b
61	    gpu: seetacloud cuda:0
62	    description: Qwen3-8B LoRA classification
63	  - registry_id: model-size-scaling-cwm8b
64	    gpu: seetacloud cuda:1
65	    description: Qwen3-8B LoRA CWM generation
66	- id: diagnostic-rerepair
67	  claim: 2
68	  description: 'Downstream proof-of-concept: give repair agent per-test failure predictions
69	    vs no per-test info, compare resolve rate on 200 instances. Uses SWE-agent or
70	    similar repair framework.'
71	  priority: P1
72	  gpu_budget_hours: 12
73	  deps:
74	  - cwm-baseline
75	  - traj-level-finetuned
76	- id: per-test-precision-recall
77	  claim: 2
78	  description: Measure per-test failure prediction precision/recall against ground-truth
79	    failing tests on full test set. Evaluate diagnostic signal quality without downstream
80	    execution.
81	  priority: P0
82	  gpu_budget_hours: 1
83	  deps:
84	  - mvp-b-train
85	  registry_id: per-test-precision-recall
86	- id: oracle-f2p-stratified
87	  claim: 3
88	  description: Stratified oracle analysis by F2P test count (T=1, T=2, T=3+). Report
89	    per-test advantage breakdown showing advantage concentrates in multi-test instances.
90	  priority: P0
91	  gpu_budget_hours: 0
92	  deps:
93	  - mvp-a-oracle-sim
94	  registry_id: oracle-f2p-stratified
95	- id: oracle-total-validated
96	  claim: 3
97	  description: Oracle study with Total (F2P+P2P) distribution at empirically measured
98	    regression rates. Validate when P2P tests help vs hurt.
99	  priority: P0
100	  gpu_budget_hours: 0
101	  deps:
102	  - p2p-regression-rate
103	  status: DONE
104	  registry_id: mvp-a-oracle-sim
105	- id: block-corr-empirical
106	  claim: 3
107	  description: 'Empirically validate block-correlation assumption: measure actual
108	    prediction error correlation structure from trained model''s test-level predictions,
109	    compare with i.i.d. and block-correlated simulation models.'
110	  priority: P2
111	  gpu_budget_hours: 1
112	  deps:
113	  - mvp-b-train
114	  registry_id: block-corr-empirical
115	- id: swebench-pertest-data
116	  claim:
117	  - 1
118	  - 2
119	  - 3
120	  description: Docker re-evaluation of SWE-bench Verified patches to extract per-test
121	    labels. Build SWE-bench-PerTest dataset (500 instances x 16 candidates). Resource
122	    contribution.
123	  priority: P1
124	  gpu_budget_hours: 0
125	  compute_note: CPU/Docker only, ~16-24h with 16 parallel containers. Start early
126	    to parallelize with GPU experiments.
127	  deps: []
128	- id: repo-level-training
129	  claim:
130	  - 1
131	  - 2
132	  description: Fine-tune Qwen3-4B/8B on repo-level (patched_code, test_code) -> pass/fail
133	    using SWE-bench-PerTest data. Evaluate on held-out instances.
134	  priority: P1
135	  gpu_budget_hours: 12
136	  deps:
137	  - swebench-pertest-data
138	  registry_id: repo-level-cwm-v3
139	- id: llm-judge-baseline
140	  claim:
141	  - 1
142	  - 3
143	  description: Qwen3-8B/32B zero-shot LLM-as-judge baselines (trajectory-level and
144	    per-test). Reference points for Pareto frontier.
145	  priority: P1
146	  gpu_budget_hours: 8
147	  deps: []
148	  registry_id: llm-judge-8b-zeroshot
149	  sub_experiments:
150	  - registry_id: llm-judge-8b-zeroshot
151	    gpu: seetacloud cuda:2
152	    description: Qwen3-8B zero-shot per-test + trajectory-level
153	  - registry_id: llm-judge-32b-zeroshot
154	    gpu: seetacloud cuda:3
155	    description: Qwen3-32B 4-bit quantized zero-shot
156	- id: per-test-majority-voting
157	  claim: 1
158	  description: Per-test majority voting (K=3) with classification model. Test if self-consistency
159	    improves per-test accuracy.
160	  priority: P2
161	  gpu_budget_hours: 3
162	  deps:
163	  - mvp-b-train
164	  registry_id: per-test-majority-voting
165	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a12711c8-6978-4fd2-9871-55d9c7b180c3",
  "isSidechain": false,
  "promptId": "4d7675b4-77fa-4209-a180-3e83688a8172",
  "type": "user",
  "uuid": "430f5fce-4817-4494-a55a-76ee8de89d83",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/experiment_plan.yaml",
      "content": "experiments:\n- id: cwm-baseline\n  claim: 1\n  description: Train CWM generation baseline (Qwen3-4B LoRA, same data/config as MVP-B)\n    to predict execution output instead of pass/fail. Compare per-class F1 against\n    classification model (87.1/87.9%).\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - mvp-b-train\n  status: PREPARING\n  registry_id: cwm-baseline\n- id: multi-seed-core\n  claim: 1\n  description: 'Multi-seed validation for core comparison: run classification (mvp-b-train)\n    and CWM baseline each with seeds {0, 1, 42}. Report mean +/- std F1. Statistical\n    significance via paired t-test or bootstrap CI. Required for any claim of ''significantly\n    better''.'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - cwm-baseline\n  registry_id: traj-level-seed0\n- id: trace-then-judge\n  claim: 1\n  description: 'Trace-then-Judge ablation (chain-of-thought, NOT pipeline): single\n    Qwen3-4B model trained to first generate a brief execution reasoning trace (~50\n    tokens describing expected behavior), then output pass/fail. Same LoRA config/data.\n    Tests whether explicit execution reasoning helps or hurts compared to direct classification.\n    If trace-then-judge >= direct classification, the advantage is from task simplicity,\n    not from skipping reasoning.'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - cwm-baseline\n  registry_id: trace-then-judge\n- id: traj-level-finetuned\n  claim: 1\n  description: 'Same-size fine-tuned trajectory-level baseline: Qwen3-4B LoRA trained\n    to predict resolved/unresolved. Data construction: for each problem_id, aggregate\n    all (code, test) pairs into (code, all_tests_concatenated) -> resolved (original\n    code passes all tests) / unresolved (mutated code fails any test). Same train/val/test\n    split by problem_id. Isolates granularity effect.'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - mvp-b-data-prep\n  registry_id: traj-level-finetuned\n- id: model-size-scaling\n  claim: 1\n  description: Scale classification model from 4B to 8B. Measure accuracy improvement\n    and compare with CWM at 8B. Determine if classification advantage holds across\n    scales.\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - cwm-baseline\n  registry_id: model-size-scaling-cls8b\n  sub_experiments:\n  - registry_id: model-size-scaling-cls8b\n    gpu: seetacloud cuda:0\n    description: Qwen3-8B LoRA classification\n  - registry_id: model-size-scaling-cwm8b\n    gpu: seetacloud cuda:1\n    description: Qwen3-8B LoRA CWM generation\n- id: diagnostic-rerepair\n  claim: 2\n  description: 'Downstream proof-of-concept: give repair agent per-test failure predictions\n    vs no per-test info, compare resolve rate on 200 instances. Uses SWE-agent or\n    similar repair framework.'\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - cwm-baseline\n  - traj-level-finetuned\n- id: per-test-precision-recall\n  claim: 2\n  description: Measure per-test failure prediction precision/recall against ground-truth\n    failing tests on full test set. Evaluate diagnostic signal quality without downstream\n    execution.\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - mvp-b-train\n  registry_id: per-test-precision-recall\n- id: oracle-f2p-stratified\n  claim: 3\n  description: Stratified oracle analysis by F2P test count (T=1, T=2, T=3+). Report\n    per-test advantage breakdown showing advantage concentrates in multi-test instances.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - mvp-a-oracle-sim\n  registry_id: oracle-f2p-stratified\n- id: oracle-total-validated\n  claim: 3\n  description: Oracle study with Total (F2P+P2P) distribution at empirically measured\n    regression rates. Validate when P2P tests help vs hurt.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - p2p-regression-rate\n  status: DONE\n  registry_id: mvp-a-oracle-sim\n- id: block-corr-empirical\n  claim: 3\n  description: 'Empirically validate block-correlation assumption: measure actual\n    prediction error correlation structure from trained model''s test-level predictions,\n    compare with i.i.d. and block-correlated simulation models.'\n  priority: P2\n  gpu_budget_hours: 1\n  deps:\n  - mvp-b-train\n  registry_id: block-corr-empirical\n- id: swebench-pertest-data\n  claim:\n  - 1\n  - 2\n  - 3\n  description: Docker re-evaluation of SWE-bench Verified patches to extract per-test\n    labels. Build SWE-bench-PerTest dataset (500 instances x 16 candidates). Resource\n    contribution.\n  priority: P1\n  gpu_budget_hours: 0\n  compute_note: CPU/Docker only, ~16-24h with 16 parallel containers. Start early\n    to parallelize with GPU experiments.\n  deps: []\n- id: repo-level-training\n  claim:\n  - 1\n  - 2\n  description: Fine-tune Qwen3-4B/8B on repo-level (patched_code, test_code) -> pass/fail\n    using SWE-bench-PerTest data. Evaluate on held-out instances.\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - swebench-pertest-data\n  registry_id: repo-level-cwm-v3\n- id: llm-judge-baseline\n  claim:\n  - 1\n  - 3\n  description: Qwen3-8B/32B zero-shot LLM-as-judge baselines (trajectory-level and\n    per-test). Reference points for Pareto frontier.\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: llm-judge-8b-zeroshot\n  sub_experiments:\n  - registry_id: llm-judge-8b-zeroshot\n    gpu: seetacloud cuda:2\n    description: Qwen3-8B zero-shot per-test + trajectory-level\n  - registry_id: llm-judge-32b-zeroshot\n    gpu: seetacloud cuda:3\n    description: Qwen3-32B 4-bit quantized zero-shot\n- id: per-test-majority-voting\n  claim: 1\n  description: Per-test majority voting (K=3) with classification model. Test if self-consistency\n    improves per-test accuracy.\n  priority: P2\n  gpu_budget_hours: 3\n  deps:\n  - mvp-b-train\n  registry_id: per-test-majority-voting\n",
      "numLines": 165,
      "startLine": 1,
      "totalLines": 165
    }
  },
  "sourceToolAssistantUUID": "a12711c8-6978-4fd2-9871-55d9c7b180c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14 · 2026-05-18T17:25:43.772Z_

````json
{
  "parentUuid": "430f5fce-4817-4494-a55a-76ee8de89d83",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**exec-sim-repair-verifier**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"exec-sim-repair-verifier\")` 或 `load_project_config(\"exec-sim-repair-verifier\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### paper-writing-norms\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **ssh-env-setup** — 远程服务器 Python/CUDA 环境搭建规范——discovery-first 流程、PEP 668 处理、PyTorch 版本选择。当需要在远程服务器搭建训练环境时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ssh-env-setup.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/exec-sim-repair-verifier/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "11391a1b-7b0d-479f-8e09-331fd356e14c",
  "timestamp": "2026-05-18T17:25:43.772Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：DeepSeek repo-level 全部失败（延续 v1-v4 的 pattern），只有 Qwen 单模型族的 repo-level 数据，cross-model 验证仅限 func-level 核心假设：['deepseek-cls-repo-v5 训练失败或 acc ≤ majority base…",
  "leafUuid": "11391a1b-7b0d-479f-8e09-331fd356e14c",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Design space characterization for neural code verification",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b"
}
```

---

### Assistant

_source line 17 · 2026-05-18T17:28:28.614Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view of the experiment plan and registry data. Let me identify all the "planned" or "PREPARING" experiments that need worst-tier predictions, focusing on the ones defined in the experiment_plan that are still planned or whose results are pending in the worst-case scenario.

Looking at the experiment_plan entries and the worst-tier definition:

**Worst tier core assumptions:**
1. deepseek-cls-repo-v5 训练失败或 acc ≤ majority baseline (~73%)
2. deepseek-cwm-repo eval 不可用 (crash、unparseable >80%、或 acc 远低于 baseline)


3. Repo-level 结论完全依赖 Qwen 单模型族
4. DeepSeek TRAJ repo 是唯一跑通的 DeepSeek repo-level 实验，但 n=48 太小
5. Func-level 双模型族数据完整且 clean，但 repo-level 是 paper 的 differentiator

For the worst-case scenario, I'm setting metric ranges where deepseek_cls_repo_acc falls between 50-73%, deepseek_cwm_repo_acc between 40-60%, unparseable rates spike to 70-95%, while qwen_cls_repo_best_acc stays around 83%.

Now I'm going through the experiment checklist to see what's been completed and what still needs work. Most of the core experiments are done—cwm-baseline, multi-seed-core, trace-then-judge, traj-level-finetuned, model-size-scaling, per-test-precision-recall, and oracle-f2p-stratified are all finished. Diagnostic-rerepair is still in the planning stage, and I need to continue reviewing the remaining experiments on the list.

Looking at the rest of the experiments, oracle-total-validated, block-corr-empirical, and per-test-majority-voting are complete, while swebench-pertest-data is still planned. The repo-level-training experiment failed, and llm-judge-baseline is done. So the only truly pending experiments are diagnostic-rerepair and swebench-pertest-data.

But the user is asking me to predict worst-case results for all experiments in the plan, not just the ones still running. I need to go through each one and provide worst-tier predictions, treating even the completed ones as if I'm imagining the worst possible outcome before they were run. Looking at the experiment_plan structure more carefully, I see that most entries have explicit status fields — the completed ones are marked DONE with their conclusions, while diagnostic-rerepair and per-test-precision-recall are the ones flagged as planned. I need to focus on expanding those planned experiments with worst-case scenario data. I need to reconsider what the user is actually asking for. They want worst-case scenario predictions for every experiment in the plan, not just the ones marked as planned. The experiments that are already complete have real results, but for the ones still running or pending—like the deepseek variants that are currently preparing—I should generate what their worst-tier outcomes would look like based on the assumptions we've defined.

Looking at the pending experiments, the critical ones are the deepseek-cls-repo, deepseek-cwm-repo, and the diagnostic experiments, since those directly map to the worst-tier hypotheses about DeepSeek's performance ceiling and data usability. Let me focus on predicting results for those key experiments under the worst-case assumptions. I'm realizing the user wants predictions for all experiments in the worst-case scenario—for completed ones, I can compare actual results against the worst-tier baseline, but for pending experiments, I need to generate predicted values that fit that worst-tier narrative. I need to be more comprehensive here. Beyond the experiment_plan entries, there are several PREPARING and running experiments in the registry that are crucial for supporting the paper's core claims, so I should include those as well. Let me map out the full scope: the 14 items from experiment_plan plus the key registry experiments that feed into worst-case scenarios, then enumerate what I'm actually covering. I need to focus on the experiment_plan entries specifically, since that's what was requested. Most of those are already completed, so for the worst-tier scenario I should generate predictions for the pending ones and incorporate the critical DeepSeek experiments that aren't in the plan. The key narrative for worst-tier is that DeepSeek's repo-level approaches fail entirely while only Qwen has viable repo-level data, which fundamentally changes the outcome.

Now I'm going through each completed experiment with actual results to establish the baseline, then I'll layer in worst-tier predictions for the pending ones. Looking at the remaining pending experiments, I see diagnostic re-repair has already shown negative results across its phases, so that confirms no improvement from diagnostic feedback. The swebench per-test dataset construction is CPU-bound and might not finish in time or produce quality data. For the DeepSeek variants, I'm expecting the worst case where classification accuracy stays at or below the majority baseline of 73%, or the training fails entirely, and for the CWM repo eval, unparseable outputs exceed 80% with usable accuracy far below baseline. Now I'm putting together the complete YAML focusing on the experiments still pending, since those are the ones being projected for worst-case scenarios.

Actually, re-reading the request more carefully, I should be covering all 14 experiments in the plan, not just the pending ones. For experiments already completed, the worst-tier result is essentially their actual result since they've already run. For the planned and pending ones, I'll project worst-case outcomes. Most of the experiments in the plan are Qwen function-level and oracle simulations that complete regardless of tier, so the distinction matters more for the repo-level DeepSeek experiments where the model tends to struggle.

The DeepSeek experiments weren't part of the original plan—they came later as part of cross-model validation. So I should focus on the 14 formal plan items but also highlight the critical additional experiments like DeepSeek repo-level and re-repair work that shape the worst-tier narrative. Let me structure the YAML to cover all 14 plan items with their actual or predicted results, then add the key supplementary experiments.

For the worst-tier story, the func-level results across Qwen and DeepSeek are actually consistent, which is solid. The repo-level Qwen results show CLS hitting 82-86% accuracy and CWM reaching around 93% with unparseable handling. I'll organize everything by category and include both pending and completed experiments to give a full picture.

Now looking at the specific numbers: DeepSeek's repo-level CLS has failed consistently through v4 (66.1% accuracy, below the 73% majority baseline), and I'm predicting v5 will also fall short at around 68%. The CWM approach produces mostly unparseable outputs or accuracy far below baseline, while TRAJ works but the sample size of 48 is too small to be meaningful. The re-repair experiments came back negative, and while the diagnostic granularity work is solid, there's no downstream evidence it helps. I'll be specific with these numbers in the YAML. I need to compile the full list of experiment plan IDs, including the ones still in preparation. Beyond the seven I already identified, there are several more critical experiments to track: the deepseek variants across different seeds and epochs, the Qwen model evaluation, re-repair experiments with their existing negative data, and the repo-level baselines. Let me make sure I capture all twenty-one experiments in my output.

I'm also checking the deepseek function-level results from the registry—those are all complete and consistently show strong performance across different approaches and seeds, which validates the function-level equivalence claim. Now I need to verify what's happening with the repo-level deepseek experiments to ensure I have the full picture before compiling everything together. Looking at the trajectory model results across different seed configurations, the 8k variant performs best at 81.25%, while the multi-seed average comes out to about 75.35%.

Now I'm reviewing the Qwen results—the classifier models show stronger performance with the 8B seed123 variant reaching 85.6% on test data, though the CWM repo experiments all encountered parsing failures. I have enough data now to compile the full results into a structured format.

I need to clarify what the user is asking for: whether to treat all experiments as scenario predictions or just the pending ones. Looking back at the request, it seems they want me to focus specifically on the "planned" experiments from the experiment_plan, plus the critical deepseek repo-level runs. For completed experiments, I'll use the actual results; for pending ones, I'll provide predictions based on the worst-case scenario. Let me organize each experiment with its name, plan ID, description, expected results, rationale, and implications for the paper. is to compile worst-tier predictions for incomplete experiments alongside actual results from finished ones, organized by theme to show the full picture. I'll use real data for done experiments like the baseline results and multi-seed comparisons, then predict conservative outcomes for the pending ones, explaining the reasoning behind each.

Now I'm reviewing the actual results from completed experiments—the model scaling shows CLS outperforming CWM at 8B, precision-recall metrics are solid around 87-88%, the oracle stratification found meaningful tier contributions, and the LLM judge baseline shows expected scaling with model size, though majority voting surprisingly went negative. For the preparing experiments, I'm predicting lower performance like 68% accuracy for the DeepSeek variants, which would fall below the majority baseline threshold.

Looking back at what's actually failing, I need to clarify my worst-tier definition more carefully. The core issue is that DeepSeek repo-level approaches aren't producing usable results—either the models crash during training or fall short of the baseline—while the Qwen single-model-family setup is the only one that's somewhat viable, and even the 3-shot approach isn't improving over the zero-shot version.

Now I'm examining the performance ranges across these different configurations. DeepSeek's classification and CWM repo accuracies are stuck in the 40-73% range with massive unparseable rates, whereas Qwen's repo-level work reaches 83-86% on classification but struggles with CWM parsing. The function-level data across both model families is performing much better at 83-90%, which suggests the repo-level formulation is where things break down. Given the expected reviewer score range of 2.5-3.0, I need to focus on which experiments are actually still pending and worth running versus which ones I should deprioritize based on these patterns.

Looking at what's left to execute, I've got the planned diagnostic and swebench experiments, plus several critical DeepSeek and Qwen repo-level runs that are either preparing or already allocated. Some have already failed, which is useful context for understanding where the approach struggles. I should also verify the status of those trajectory-based function-level experiments to see if they're worth including in the final analysis.

Now I'm compiling the aggregate performance metrics across the multi-seed runs for both the CLS and CWM approaches at the function level, which will give me a clearer picture of variance and consistency across different random seeds. I've compiled enough performance data across the different seeds and model variants. Now I need to check what the experiment_plan file actually contains — the user mentioned tracking planned experiments, and while the YAML file only showed 14 entries with sparse status information, the CLAUDE.md context has the complete picture with status and conclusions for all of them. Let me structure the output to cover all pending experiments from the plan along with the key additional results I've gathered.

I'm organizing the experiments into three main categories: the function-level baseline experiments with actual data that establish the worst-tier performance, the cross-model validation experiments using DeepSeek at the function level, and the repository-level experiments with Qwen, which is the only model family with repo-level results so far.

For the repo-level work, I'm tracking the Qwen experiments that are mostly done, the DeepSeek repo-level experiments that are still being prepared or have failed, and then the diagnostic and downstream analyses along with baseline comparisons.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11391a1b-7b0d-479f-8e09-331fd356e14c",
  "isSidechain": false,
  "requestId": "req_011CbARciSuzndDVoRo72pj9",
  "type": "assistant",
  "uuid": "e1f4dd4b-14f0-404b-93d1-e70bf37240be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tiUzQzAoGgkT6AGrnpLJZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8845,
      "cache_read_input_tokens": 48929,
      "output_tokens": 8745,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8845,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8745,
          "cache_read_input_tokens": 48929,
          "cache_creation_input_tokens": 8845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8845
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

_source line 18 · 2026-05-18T17:28:28.617Z_

Let me check the registry for pending experiments to complete the picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1f4dd4b-14f0-404b-93d1-e70bf37240be",
  "isSidechain": false,
  "requestId": "req_011CbARciSuzndDVoRo72pj9",
  "type": "assistant",
  "uuid": "e9770abb-f476-45d1-804c-3b29e068747b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tiUzQzAoGgkT6AGrnpLJZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8845,
      "cache_read_input_tokens": 48929,
      "output_tokens": 8745,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8845,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8745,
          "cache_read_input_tokens": 48929,
          "cache_creation_input_tokens": 8845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8845
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

_source line 19 · 2026-05-18T17:28:30.859Z_

<details open><summary>🔧 Tool call — Grep · `toolu_016HKiQkUNFUHDAWbxd9GhDf`</summary>

```json
{
  "pattern": "status: (PREPARING|ALLOCATED|RUNNING|ANALYZING)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/global/registry.yaml",
  "output_mode": "content",
  "-B": 3,
  "head_limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9770abb-f476-45d1-804c-3b29e068747b",
  "isSidechain": false,
  "requestId": "req_011CbARciSuzndDVoRo72pj9",
  "type": "assistant",
  "uuid": "8c2e32a3-8105-4fb1-a4fd-4e970585a5f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tiUzQzAoGgkT6AGrnpLJZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8845,
      "cache_read_input_tokens": 48929,
      "output_tokens": 8745,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8845,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8745,
          "cache_read_input_tokens": 48929,
          "cache_creation_input_tokens": 8845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8845
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

_source line 20 · 2026-05-18T17:28:30.904Z_

<details><summary>↩ Tool result · `toolu_016HKiQkUNFUHDAWbxd9GhDf`</summary>

```text
1-baseline: null
2-experiments:
3-  repo-level-cls-8b-seed123-conda-v2:
4:    status: PREPARING
--
12-      Last checkpoint from v1: checkpoint-3000 (May 15 00:55). Fix: use --resume_from_checkpoint
13-      /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-3000'
14-  cls8b-seed123-ckpt3000-val8192-eval:
15:    status: PREPARING
--
129-    conclusion: killed
130-    completed_at: '2026-05-15T23:24:40.422Z'
131-  repo-level-cls-8b-s42-resume:
132:    status: PREPARING
--
141-      task
142-    parent: repo-level-cls-8b-conda
143-  repo-level-cwm-8b-conda-v4:
144:    status: PREPARING
--
208-          parse_rate: 27.32
209-          parseable_acc: 38
210-  cls8b-s42-resume-val-sweep-seq8192-v2:
211:    status: PREPARING
--
216-      ✓. max_seq_length=8192, batch_size=1 ✓. 当前 ckpt-1800 (1/21), 1360/9335, running_acc=87.9%.
217-      速率 ~6.0 samples/sec, 每 ckpt ~26min. 总剩余 ~9h, ETA ~May 16 10:50 UTC.'
218-  repo-level-cwm-8b-conda-v5:
219:    status: PREPARING
--
340-      across mutation types (gold, operator_swap, boundary_removal, return_value,
341-      off_by_one), informing error complementarity analysis between CLS and CWM
342-  cls8b-s42-ckpt1000-test-mutation:
343:    status: PREPARING
--
348-      ckpt-3600 test+mutation eval running.'
349-    conclusion: killed
350-  cls8b-s42-resume-ckpt1000-test-mutation:
351:    status: PREPARING
--
423-    completed_at: '2026-05-16T11:54:57.575Z'
424-    parent: deepseek-cls-func
425-  deepseek-traj-func:
426:    status: PREPARING
--
535-    completed_at: '2026-05-16T14:34:00.760Z'
536-    parent: deepseek-traj-func-v2
537-  deepseek-traj-func-v2-fixed:
538:    status: PREPARING
--
542-    hypothesis: 'DeepSeek TRAJ func-level v2-fixed (correct train_traj_verifier.py,
543-      resolved/unresolved): verify CLS≈TRAJ equivalence across model families'
544-  deepseek-traj-func-v2-s123-fixed:
545:    status: PREPARING
--
639-    hypothesis: 同上 seed=999
640-    parent: deepseek-traj-repo-8k
641-  deepseek-traj-repo-8k-s123:
642:    status: PREPARING
--
648-      reviewer concern about single-seed instability (n=48 test set)'
649-    parent: deepseek-traj-repo-8k
650-  deepseek-traj-repo-8k-s0:
651:    status: PREPARING
--
657-      variance across seeds'
658-    parent: deepseek-traj-repo-8k
659-  deepseek-traj-repo-8k-s789:
660:    status: PREPARING
--
666-      causes high variance across seeds'
667-    parent: deepseek-traj-repo-8k
668-  deepseek-traj-repo-8k-s456:
669:    status: PREPARING
--
675-      causes high variance across seeds'
676-    parent: deepseek-traj-repo-8k
677-  deepseek-cwm-func-s123:
678:    status: PREPARING
--

[Showing results with pagination = limit: 80]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c2e32a3-8105-4fb1-a4fd-4e970585a5f6",
  "isSidechain": false,
  "promptId": "4d7675b4-77fa-4209-a180-3e83688a8172",
  "type": "user",
  "uuid": "0db2ee4c-3565-46a1-8bc5-2fbe990af53a",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1-baseline: null\n2-experiments:\n3-  repo-level-cls-8b-seed123-conda-v2:\n4:    status: PREPARING\n--\n12-      Last checkpoint from v1: checkpoint-3000 (May 15 00:55). Fix: use --resume_from_checkpoint\n13-      /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-3000'\n14-  cls8b-seed123-ckpt3000-val8192-eval:\n15:    status: PREPARING\n--\n129-    conclusion: killed\n130-    completed_at: '2026-05-15T23:24:40.422Z'\n131-  repo-level-cls-8b-s42-resume:\n132:    status: PREPARING\n--\n141-      task\n142-    parent: repo-level-cls-8b-conda\n143-  repo-level-cwm-8b-conda-v4:\n144:    status: PREPARING\n--\n208-          parse_rate: 27.32\n209-          parseable_acc: 38\n210-  cls8b-s42-resume-val-sweep-seq8192-v2:\n211:    status: PREPARING\n--\n216-      ✓. max_seq_length=8192, batch_size=1 ✓. 当前 ckpt-1800 (1/21), 1360/9335, running_acc=87.9%.\n217-      速率 ~6.0 samples/sec, 每 ckpt ~26min. 总剩余 ~9h, ETA ~May 16 10:50 UTC.'\n218-  repo-level-cwm-8b-conda-v5:\n219:    status: PREPARING\n--\n340-      across mutation types (gold, operator_swap, boundary_removal, return_value,\n341-      off_by_one), informing error complementarity analysis between CLS and CWM\n342-  cls8b-s42-ckpt1000-test-mutation:\n343:    status: PREPARING\n--\n348-      ckpt-3600 test+mutation eval running.'\n349-    conclusion: killed\n350-  cls8b-s42-resume-ckpt1000-test-mutation:\n351:    status: PREPARING\n--\n423-    completed_at: '2026-05-16T11:54:57.575Z'\n424-    parent: deepseek-cls-func\n425-  deepseek-traj-func:\n426:    status: PREPARING\n--\n535-    completed_at: '2026-05-16T14:34:00.760Z'\n536-    parent: deepseek-traj-func-v2\n537-  deepseek-traj-func-v2-fixed:\n538:    status: PREPARING\n--\n542-    hypothesis: 'DeepSeek TRAJ func-level v2-fixed (correct train_traj_verifier.py,\n543-      resolved/unresolved): verify CLS≈TRAJ equivalence across model families'\n544-  deepseek-traj-func-v2-s123-fixed:\n545:    status: PREPARING\n--\n639-    hypothesis: 同上 seed=999\n640-    parent: deepseek-traj-repo-8k\n641-  deepseek-traj-repo-8k-s123:\n642:    status: PREPARING\n--\n648-      reviewer concern about single-seed instability (n=48 test set)'\n649-    parent: deepseek-traj-repo-8k\n650-  deepseek-traj-repo-8k-s0:\n651:    status: PREPARING\n--\n657-      variance across seeds'\n658-    parent: deepseek-traj-repo-8k\n659-  deepseek-traj-repo-8k-s789:\n660:    status: PREPARING\n--\n666-      causes high variance across seeds'\n667-    parent: deepseek-traj-repo-8k\n668-  deepseek-traj-repo-8k-s456:\n669:    status: PREPARING\n--\n675-      causes high variance across seeds'\n676-    parent: deepseek-traj-repo-8k\n677-  deepseek-cwm-func-s123:\n678:    status: PREPARING\n--",
    "numLines": 80,
    "appliedLimit": 80
  },
  "sourceToolAssistantUUID": "8c2e32a3-8105-4fb1-a4fd-4e970585a5f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：DeepSeek repo-level 全部失败（延续 v1-v4 的 pattern），只有 Qwen 单模型族的 repo-level 数据，cross-model 验证仅限 func-level 核心假设：['deepseek-cls-repo-v5 训练失败或 acc ≤ majority base…",
  "leafUuid": "0db2ee4c-3565-46a1-8bc5-2fbe990af53a",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Design space characterization for neural code verification",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b"
}
```

---

### Tool call

_source line 23 · 2026-05-18T17:28:35.903Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01QTMS2A5a7Q2i7oRgKYTXiQ`</summary>

```json
{
  "pattern": "deepseek-cls-repo-v5|deepseek-cwm-repo-s42-epoch2|deepseek-cls-repo-s123|D124-cwm|repo-level-3shot|deepseek-cwm-repo-s123",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/global/registry.yaml",
  "output_mode": "content",
  "-A": 15,
  "head_limit": 120
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0db2ee4c-3565-46a1-8bc5-2fbe990af53a",
  "isSidechain": false,
  "requestId": "req_011CbARq3Bd34f8UAFka3g1s",
  "type": "assistant",
  "uuid": "41884318-f1fb-4b1c-a1dd-f2660325d33d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017SJ2DjY7TKfQRS1SG75cis",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9839,
      "cache_read_input_tokens": 57774,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 57774,
          "cache_creation_input_tokens": 9839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9839
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

_source line 24 · 2026-05-18T17:28:35.918Z_

<details><summary>↩ Tool result · `toolu_01QTMS2A5a7Q2i7oRgKYTXiQ`</summary>

```text
835:  deepseek-cls-repo-s123:
836-    status: DONE
837-    retry_count: 0
838-    created_at: '2026-05-17T03:04:22.909Z'
839-    updated_at: '2026-05-18T03:27:12.928Z'
840-    parent: deepseek-cls-repo-v4
841-    hypothesis: 'DeepSeek CLS repo-level seed 123 replication: 与 s42 对比提供 multi-seed
842-      证据，预期 CLS 跨 seed 稳定 (R1-N1)'
843-    spec:
844-      command: python eval_repo_cls.py --checkpoint best --seq_length 8192
845-      server: seetacloud-westd-4x5090
846-      data_path: /home/sonny/exec-sim-repair-verifier/data/repo_test
847-      data_count: 9784
848-      model_name: deepseek-coder-6.7b-instruct
849-      seed: 123
850-      gpu: cuda:2
--
852:      checkpoint_source: deepseek-cls-repo-s123 best checkpoint
853-      eval_data: repo_test (9784 instances)
854-    metrics:
855-      eval_repo_8192:
856-        accuracy: 0.7493
857-        f1_macro: 0.5394
858-        f1_pass: 0.8503
859-        f1_fail: 0.2284
860-        unparseable_rate: 0
861-        precision_fail: 0.6811
862-        recall_fail: 0.1372
863-        precision_pass: 0.7532
864-        recall_pass: 0.9762
865-        confusion:
866-          TP: 6968
867-          FP: 2283
--
874:  deepseek-cwm-repo-s123:
875-    status: RUNNING
876-    retry_count: 0
877-    created_at: '2026-05-17T03:04:23.406Z'
878-    updated_at: '2026-05-17T23:34:27.820Z'
879-    parent: deepseek-cwm-repo
880-    hypothesis: 'DeepSeek CWM repo-level seed 123 replication: 与 s42 对比验证 CWM repo-level
881-      退化是否跨 seed 一致，支撑 formulation-inherent 论点'
882-    spec:
883-      command: python eval_repo_cwm.py --checkpoint /root/autodl-tmp/checkpoints_repo_cwm_deepseek_s123/checkpoint-8844
884-        --seq_length 4096
885-      server: seetacloud-westd-4x5090
886-      data_path: /home/sonny/exec-sim-repair-verifier/data/repo_test
887-      data_count: 9784
888-      model_name: deepseek-coder-6.7b-instruct
889-      seed: 123
--
955:  deepseek-cwm-repo-s42-epoch2-eval:
956-    status: RUNNING
957-    retry_count: 0
958-    created_at: '2026-05-17T23:33:30.418Z'
959-    updated_at: '2026-05-18T03:24:21.026Z'
960-    hypothesis: 'CWM s42 epoch 2 checkpoint eval: 如果 epoch 2 accuracy >> epoch 3 (58.7%),
961-      则 CWM repo-level 在 epoch 3 过拟合; 如果 epoch 2 ≈ epoch 3, 则退化是 formulation-inherent
962-      (D124)'
963-    spec:
964-      command: python eval_repo_cwm.py --checkpoint s42-epoch2 --seq_length 4096
965-      server: seetacloud-westd-4x5090
966-      data_path: /home/sonny/exec-sim-repair-verifier/data/repo_test
967-      data_count: 9784
968-      model_name: deepseek-coder-6.7b-instruct
969-      seed: 42
970-      gpu: cuda:1
--
974:  deepseek-cls-repo-v5:
975-    status: RUNNING
976-    retry_count: 0
977-    created_at: '2026-05-18T02:48:05.911Z'
978-    updated_at: '2026-05-18T02:49:48.286Z'
979-    hypothesis: 'DeepSeek CLS repo-level v5 完整 3 epoch 训练: v4 只跑了 2 epoch 导致 repo-level
980-      accuracy 71.29% 低于 majority baseline, v5 跑满 3 epoch 验证是否 epoch 3 能恢复到合理水平 (parent
981-      v4 只训 2/3 epoch 就中断)'
982-    parent: deepseek-cls-repo-v4
983-    spec:
984-      command: cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1
985-        /root/miniconda3/bin/python train_unified.py --data_dir data/ --task cls --model_name_or_path
986-        /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --output_dir
987:        /root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/ --run_name deepseek-cls-repo-v5
988-        --seed 42 --max_seq_length 2048 --batch_size 2 --grad_accumulation 16 --lr
989-        2e-4 --epochs 3 --no_wandb
990-      server: seetacloud-westd-4x5090
991-      gpu:
992-      - cuda:0
993-      pid: '698033'
994:      log_path: ~/runs/deepseek-cls-repo-v5.log
995-      submitted_at: '2026-05-18T02:49:47.671Z'
996-      submitted_via: submit_training_job
997-      backend: tmux
998-      account: root
999-    server: seetacloud-westd-4x5090
1000-    gpu: cuda:0
1001-    pid: '698033'
1002:    log_path: ~/runs/deepseek-cls-repo-v5.log
1003-    reproduce:
1004-      command: cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1
1005-        /root/miniconda3/bin/python train_unified.py --data_dir data/ --task cls --model_name_or_path
1006-        /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --output_dir
1007:        /root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/ --run_name deepseek-cls-repo-v5
1008-        --seed 42 --max_seq_length 2048 --batch_size 2 --grad_accumulation 16 --lr
1009-        2e-4 --epochs 3 --no_wandb
1010:  D124-cwm-s42-epoch2-eval:
1011-    status: DONE
1012-    retry_count: 0
1013-    created_at: '2026-05-18T03:24:23.989Z'
1014-    updated_at: '2026-05-18T13:52:18.739Z'
1015-    hypothesis: 'CWM s42 epoch 2 eval (checkpoint-8844): 如果 acc ~63% (与 s123 epoch
1016-      2 一致) → 过拟合确认; 如果 acc ~57% (与 s42 epoch 3 一致) → seed 差异。判定 CWM repo-level epoch
1017-      3 退化是过拟合还是 formulation-inherent 的关键实验。'
1018:    parent: deepseek-cwm-repo-s42-epoch2-eval
1019-    spec:
1020-      server: seetacloud-westd-4x5090
1021-      gpu: cuda:2
1022-      checkpoint_source: checkpoint-8844 (epoch 2)
1023-      eval_data: repo_test (9784 instances)
1024-      data_path: /home/sonny/exec-sim-repair-verifier/data/repo_test
1025-      data_count: 9784

[Showing results with pagination = limit: 120]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41884318-f1fb-4b1c-a1dd-f2660325d33d",
  "isSidechain": false,
  "promptId": "4d7675b4-77fa-4209-a180-3e83688a8172",
  "type": "user",
  "uuid": "4d7e18ab-8db1-4f49-a22c-b63753a125a7",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "835:  deepseek-cls-repo-s123:\n836-    status: DONE\n837-    retry_count: 0\n838-    created_at: '2026-05-17T03:04:22.909Z'\n839-    updated_at: '2026-05-18T03:27:12.928Z'\n840-    parent: deepseek-cls-repo-v4\n841-    hypothesis: 'DeepSeek CLS repo-level seed 123 replication: 与 s42 对比提供 multi-seed\n842-      证据，预期 CLS 跨 seed 稳定 (R1-N1)'\n843-    spec:\n844-      command: python eval_repo_cls.py --checkpoint best --seq_length 8192\n845-      server: seetacloud-westd-4x5090\n846-      data_path: /home/sonny/exec-sim-repair-verifier/data/repo_test\n847-      data_count: 9784\n848-      model_name: deepseek-coder-6.7b-instruct\n849-      seed: 123\n850-      gpu: cuda:2\n--\n852:      checkpoint_source: deepseek-cls-repo-s123 best checkpoint\n853-      eval_data: repo_test (9784 instances)\n854-    metrics:\n855-      eval_repo_8192:\n856-        accuracy: 0.7493\n857-        f1_macro: 0.5394\n858-        f1_pass: 0.8503\n859-        f1_fail: 0.2284\n860-        unparseable_rate: 0\n861-        precision_fail: 0.6811\n862-        recall_fail: 0.1372\n863-        precision_pass: 0.7532\n864-        recall_pass: 0.9762\n865-        confusion:\n866-          TP: 6968\n867-          FP: 2283\n--\n874:  deepseek-cwm-repo-s123:\n875-    status: RUNNING\n876-    retry_count: 0\n877-    created_at: '2026-05-17T03:04:23.406Z'\n878-    updated_at: '2026-05-17T23:34:27.820Z'\n879-    parent: deepseek-cwm-repo\n880-    hypothesis: 'DeepSeek CWM repo-level seed 123 replication: 与 s42 对比验证 CWM repo-level\n881-      退化是否跨 seed 一致，支撑 formulation-inherent 论点'\n882-    spec:\n883-      command: python eval_repo_cwm.py --checkpoint /root/autodl-tmp/checkpoints_repo_cwm_deepseek_s123/checkpoint-8844\n884-        --seq_length 4096\n885-      server: seetacloud-westd-4x5090\n886-      data_path: /home/sonny/exec-sim-repair-verifier/data/repo_test\n887-      data_count: 9784\n888-      model_name: deepseek-coder-6.7b-instruct\n889-      seed: 123\n--\n955:  deepseek-cwm-repo-s42-epoch2-eval:\n956-    status: RUNNING\n957-    retry_count: 0\n958-    created_at: '2026-05-17T23:33:30.418Z'\n959-    updated_at: '2026-05-18T03:24:21.026Z'\n960-    hypothesis: 'CWM s42 epoch 2 checkpoint eval: 如果 epoch 2 accuracy >> epoch 3 (58.7%),\n961-      则 CWM repo-level 在 epoch 3 过拟合; 如果 epoch 2 ≈ epoch 3, 则退化是 formulation-inherent\n962-      (D124)'\n963-    spec:\n964-      command: python eval_repo_cwm.py --checkpoint s42-epoch2 --seq_length 4096\n965-      server: seetacloud-westd-4x5090\n966-      data_path: /home/sonny/exec-sim-repair-verifier/data/repo_test\n967-      data_count: 9784\n968-      model_name: deepseek-coder-6.7b-instruct\n969-      seed: 42\n970-      gpu: cuda:1\n--\n974:  deepseek-cls-repo-v5:\n975-    status: RUNNING\n976-    retry_count: 0\n977-    created_at: '2026-05-18T02:48:05.911Z'\n978-    updated_at: '2026-05-18T02:49:48.286Z'\n979-    hypothesis: 'DeepSeek CLS repo-level v5 完整 3 epoch 训练: v4 只跑了 2 epoch 导致 repo-level\n980-      accuracy 71.29% 低于 majority baseline, v5 跑满 3 epoch 验证是否 epoch 3 能恢复到合理水平 (parent\n981-      v4 只训 2/3 epoch 就中断)'\n982-    parent: deepseek-cls-repo-v4\n983-    spec:\n984-      command: cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1\n985-        /root/miniconda3/bin/python train_unified.py --data_dir data/ --task cls --model_name_or_path\n986-        /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --output_dir\n987:        /root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/ --run_name deepseek-cls-repo-v5\n988-        --seed 42 --max_seq_length 2048 --batch_size 2 --grad_accumulation 16 --lr\n989-        2e-4 --epochs 3 --no_wandb\n990-      server: seetacloud-westd-4x5090\n991-      gpu:\n992-      - cuda:0\n993-      pid: '698033'\n994:      log_path: ~/runs/deepseek-cls-repo-v5.log\n995-      submitted_at: '2026-05-18T02:49:47.671Z'\n996-      submitted_via: submit_training_job\n997-      backend: tmux\n998-      account: root\n999-    server: seetacloud-westd-4x5090\n1000-    gpu: cuda:0\n1001-    pid: '698033'\n1002:    log_path: ~/runs/deepseek-cls-repo-v5.log\n1003-    reproduce:\n1004-      command: cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1\n1005-        /root/miniconda3/bin/python train_unified.py --data_dir data/ --task cls --model_name_or_path\n1006-        /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --output_dir\n1007:        /root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/ --run_name deepseek-cls-repo-v5\n1008-        --seed 42 --max_seq_length 2048 --batch_size 2 --grad_accumulation 16 --lr\n1009-        2e-4 --epochs 3 --no_wandb\n1010:  D124-cwm-s42-epoch2-eval:\n1011-    status: DONE\n1012-    retry_count: 0\n1013-    created_at: '2026-05-18T03:24:23.989Z'\n1014-    updated_at: '2026-05-18T13:52:18.739Z'\n1015-    hypothesis: 'CWM s42 epoch 2 eval (checkpoint-8844): 如果 acc ~63% (与 s123 epoch\n1016-      2 一致) → 过拟合确认; 如果 acc ~57% (与 s42 epoch 3 一致) → seed 差异。判定 CWM repo-level epoch\n1017-      3 退化是过拟合还是 formulation-inherent 的关键实验。'\n1018:    parent: deepseek-cwm-repo-s42-epoch2-eval\n1019-    spec:\n1020-      server: seetacloud-westd-4x5090\n1021-      gpu: cuda:2\n1022-      checkpoint_source: checkpoint-8844 (epoch 2)\n1023-      eval_data: repo_test (9784 instances)\n1024-      data_path: /home/sonny/exec-sim-repair-verifier/data/repo_test\n1025-      data_count: 9784",
    "numLines": 120,
    "appliedLimit": 120
  },
  "sourceToolAssistantUUID": "41884318-f1fb-4b1c-a1dd-f2660325d33d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T17:28:40.841Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01CVPfLBHGuPPeMcmRrJJYkQ`</summary>

```json
{
  "pattern": "D124-cwm-s42-epoch2-eval",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/global/registry.yaml",
  "output_mode": "content",
  "-A": 40,
  "head_limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d7e18ab-8db1-4f49-a22c-b63753a125a7",
  "isSidechain": false,
  "requestId": "req_011CbARqRdjkcniQrABvrLor",
  "type": "assistant",
  "uuid": "ac61564f-e065-4246-b133-7432fc6b46c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0125p11T5B6cJR78BLEvGteJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2568,
      "cache_read_input_tokens": 67613,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2568,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 67613,
          "cache_creation_input_tokens": 2568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2568
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

_source line 26 · 2026-05-18T17:28:40.854Z_

<details><summary>↩ Tool result · `toolu_01CVPfLBHGuPPeMcmRrJJYkQ`</summary>

```text
1010:  D124-cwm-s42-epoch2-eval:
1011-    status: DONE
1012-    retry_count: 0
1013-    created_at: '2026-05-18T03:24:23.989Z'
1014-    updated_at: '2026-05-18T13:52:18.739Z'
1015-    hypothesis: 'CWM s42 epoch 2 eval (checkpoint-8844): 如果 acc ~63% (与 s123 epoch
1016-      2 一致) → 过拟合确认; 如果 acc ~57% (与 s42 epoch 3 一致) → seed 差异。判定 CWM repo-level epoch
1017-      3 退化是过拟合还是 formulation-inherent 的关键实验。'
1018-    parent: deepseek-cwm-repo-s42-epoch2-eval
1019-    spec:
1020-      server: seetacloud-westd-4x5090
1021-      gpu: cuda:2
1022-      checkpoint_source: checkpoint-8844 (epoch 2)
1023-      eval_data: repo_test (9784 instances)
1024-      data_path: /home/sonny/exec-sim-repair-verifier/data/repo_test
1025-      data_count: 9784
1026-      model_name: deepseek-coder-6.7b-instruct
1027-      seed: 42
1028-      pid: 700398
1029-      command: python eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/checkpoint-8844
1030-        --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct
1031-        --split test --max_seq_length 8192 --max_new_tokens 512 --batch_size 1 --device
1032-        cuda:0
1033-    conclusion: killed
1034-    notes: 'Killed at 31% (3002/9784, running_acc 66.9%) per D131: seq8192 非 canonical
1035-      (canonical=2048)，结果不可用于 Table 4。替代实验: D131-cwm-s42-epoch3-seq2048'
1036-    completed_at: '2026-05-18T13:52:18.739Z'
1037-  D131-cwm-s42-epoch3-seq2048:
1038-    status: RUNNING
1039-    retry_count: 0
1040-    created_at: '2026-05-18T13:50:25.467Z'
1041-    updated_at: '2026-05-18T13:53:32.536Z'
1042-    hypothesis: 'DeepSeek CWM s42 epoch 3 eval at canonical seq2048: Table 4 主数字，与
1043-      Qwen CWM repo (65.17% seq2048) 直接可比。预期 ~56% 基于 seq4096 running_acc 趋势。'
1044:    parent: D124-cwm-s42-epoch2-eval
1045-    spec:
1046-      server: seetacloud-westd-4x5090
1047-      gpu: cuda:2
1048-      data_path: /home/sonny/exec-sim-repair-verifier/data/repo_test
1049-      data_count: 9784
1050-      model_name: deepseek-coder-6.7b-instruct
1051-      seed: 42
1052-      checkpoint_source: checkpoint-13266 (epoch 3)
1053-      eval_data: repo_test (9784 instances)
1054-      pid: 734440
1055-      command: python eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/checkpoint-13266
1056-        --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct
1057-        --split test --max_seq_length 2048 --max_new_tokens 512 --batch_size 1 --device
1058-        cuda:0
1059-  D132-cwm-s42-epoch2-seq4096:
1060-    status: PREPARING
1061-    retry_count: 0
1062-    created_at: '2026-05-18T13:54:17.376Z'
1063-    updated_at: '2026-05-18T13:55:15.261Z'
1064-    hypothesis: 'CWM s42 epoch 2 eval @seq4096: 与 s42 epoch 3 @seq4096 (GPU 1 当前在跑)
1065-      形成 clean overtraining 对比（同 seed 同 seq，仅 epoch 不同）。预期 acc > epoch 3 (~56%) 则确认过拟合。'
1066-    parent: deepseek-cwm-repo-s42-epoch2-eval
1067-    conclusion: killed
1068-    notes: 'Superseded by D132v2: seq4096→seq2048 (canonical). 替代实验: D132-cwm-s42-e2-seq2048'
1069-  D132-cwm-s123-epoch3-seq4096:

[Showing results with pagination = limit: 60]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac61564f-e065-4246-b133-7432fc6b46c2",
  "isSidechain": false,
  "promptId": "4d7675b4-77fa-4209-a180-3e83688a8172",
  "type": "user",
  "uuid": "7e55f28c-338b-4321-8b7e-c725f0654fc2",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1010:  D124-cwm-s42-epoch2-eval:\n1011-    status: DONE\n1012-    retry_count: 0\n1013-    created_at: '2026-05-18T03:24:23.989Z'\n1014-    updated_at: '2026-05-18T13:52:18.739Z'\n1015-    hypothesis: 'CWM s42 epoch 2 eval (checkpoint-8844): 如果 acc ~63% (与 s123 epoch\n1016-      2 一致) → 过拟合确认; 如果 acc ~57% (与 s42 epoch 3 一致) → seed 差异。判定 CWM repo-level epoch\n1017-      3 退化是过拟合还是 formulation-inherent 的关键实验。'\n1018-    parent: deepseek-cwm-repo-s42-epoch2-eval\n1019-    spec:\n1020-      server: seetacloud-westd-4x5090\n1021-      gpu: cuda:2\n1022-      checkpoint_source: checkpoint-8844 (epoch 2)\n1023-      eval_data: repo_test (9784 instances)\n1024-      data_path: /home/sonny/exec-sim-repair-verifier/data/repo_test\n1025-      data_count: 9784\n1026-      model_name: deepseek-coder-6.7b-instruct\n1027-      seed: 42\n1028-      pid: 700398\n1029-      command: python eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/checkpoint-8844\n1030-        --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct\n1031-        --split test --max_seq_length 8192 --max_new_tokens 512 --batch_size 1 --device\n1032-        cuda:0\n1033-    conclusion: killed\n1034-    notes: 'Killed at 31% (3002/9784, running_acc 66.9%) per D131: seq8192 非 canonical\n1035-      (canonical=2048)，结果不可用于 Table 4。替代实验: D131-cwm-s42-epoch3-seq2048'\n1036-    completed_at: '2026-05-18T13:52:18.739Z'\n1037-  D131-cwm-s42-epoch3-seq2048:\n1038-    status: RUNNING\n1039-    retry_count: 0\n1040-    created_at: '2026-05-18T13:50:25.467Z'\n1041-    updated_at: '2026-05-18T13:53:32.536Z'\n1042-    hypothesis: 'DeepSeek CWM s42 epoch 3 eval at canonical seq2048: Table 4 主数字，与\n1043-      Qwen CWM repo (65.17% seq2048) 直接可比。预期 ~56% 基于 seq4096 running_acc 趋势。'\n1044:    parent: D124-cwm-s42-epoch2-eval\n1045-    spec:\n1046-      server: seetacloud-westd-4x5090\n1047-      gpu: cuda:2\n1048-      data_path: /home/sonny/exec-sim-repair-verifier/data/repo_test\n1049-      data_count: 9784\n1050-      model_name: deepseek-coder-6.7b-instruct\n1051-      seed: 42\n1052-      checkpoint_source: checkpoint-13266 (epoch 3)\n1053-      eval_data: repo_test (9784 instances)\n1054-      pid: 734440\n1055-      command: python eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/checkpoint-13266\n1056-        --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct\n1057-        --split test --max_seq_length 2048 --max_new_tokens 512 --batch_size 1 --device\n1058-        cuda:0\n1059-  D132-cwm-s42-epoch2-seq4096:\n1060-    status: PREPARING\n1061-    retry_count: 0\n1062-    created_at: '2026-05-18T13:54:17.376Z'\n1063-    updated_at: '2026-05-18T13:55:15.261Z'\n1064-    hypothesis: 'CWM s42 epoch 2 eval @seq4096: 与 s42 epoch 3 @seq4096 (GPU 1 当前在跑)\n1065-      形成 clean overtraining 对比（同 seed 同 seq，仅 epoch 不同）。预期 acc > epoch 3 (~56%) 则确认过拟合。'\n1066-    parent: deepseek-cwm-repo-s42-epoch2-eval\n1067-    conclusion: killed\n1068-    notes: 'Superseded by D132v2: seq4096→seq2048 (canonical). 替代实验: D132-cwm-s42-e2-seq2048'\n1069-  D132-cwm-s123-epoch3-seq4096:",
    "numLines": 60,
    "appliedLimit": 60
  },
  "sourceToolAssistantUUID": "ac61564f-e065-4246-b133-7432fc6b46c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T17:28:44.451Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01BoRrXgUWLh5HMHqSxg9X2H`</summary>

```json
{
  "pattern": "D13[123].*cwm|D133",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/global/registry.yaml",
  "output_mode": "content",
  "-A": 25,
  "head_limit": 120
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e55f28c-338b-4321-8b7e-c725f0654fc2",
  "isSidechain": false,
  "requestId": "req_011CbARqmmhodf8iCRUBaxJN",
  "type": "assistant",
  "uuid": "ad268b2b-87b7-4ae2-8903-5949e370d822",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sda6g4CvDfGcoVfwtegvAg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1615,
      "cache_read_input_tokens": 70181,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1615,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 70181,
          "cache_creation_input_tokens": 1615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1615
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

_source line 28 · 2026-05-18T17:28:44.471Z_

<details><summary>↩ Tool result · `toolu_01BoRrXgUWLh5HMHqSxg9X2H`</summary>

```text
1035:      (canonical=2048)，结果不可用于 Table 4。替代实验: D131-cwm-s42-epoch3-seq2048'
1036-    completed_at: '2026-05-18T13:52:18.739Z'
1037:  D131-cwm-s42-epoch3-seq2048:
1038-    status: RUNNING
1039-    retry_count: 0
1040-    created_at: '2026-05-18T13:50:25.467Z'
1041-    updated_at: '2026-05-18T13:53:32.536Z'
1042-    hypothesis: 'DeepSeek CWM s42 epoch 3 eval at canonical seq2048: Table 4 主数字，与
1043-      Qwen CWM repo (65.17% seq2048) 直接可比。预期 ~56% 基于 seq4096 running_acc 趋势。'
1044-    parent: D124-cwm-s42-epoch2-eval
1045-    spec:
1046-      server: seetacloud-westd-4x5090
1047-      gpu: cuda:2
1048-      data_path: /home/sonny/exec-sim-repair-verifier/data/repo_test
1049-      data_count: 9784
1050-      model_name: deepseek-coder-6.7b-instruct
1051-      seed: 42
1052-      checkpoint_source: checkpoint-13266 (epoch 3)
1053-      eval_data: repo_test (9784 instances)
1054-      pid: 734440
1055-      command: python eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/checkpoint-13266
1056-        --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct
1057-        --split test --max_seq_length 2048 --max_new_tokens 512 --batch_size 1 --device
1058-        cuda:0
1059:  D132-cwm-s42-epoch2-seq4096:
1060-    status: PREPARING
1061-    retry_count: 0
1062-    created_at: '2026-05-18T13:54:17.376Z'
1063-    updated_at: '2026-05-18T13:55:15.261Z'
1064-    hypothesis: 'CWM s42 epoch 2 eval @seq4096: 与 s42 epoch 3 @seq4096 (GPU 1 当前在跑)
1065-      形成 clean overtraining 对比（同 seed 同 seq，仅 epoch 不同）。预期 acc > epoch 3 (~56%) 则确认过拟合。'
1066-    parent: deepseek-cwm-repo-s42-epoch2-eval
1067-    conclusion: killed
1068:    notes: 'Superseded by D132v2: seq4096→seq2048 (canonical). 替代实验: D132-cwm-s42-e2-seq2048'
1069:  D132-cwm-s123-epoch3-seq4096:
1070-    status: PREPARING
1071-    retry_count: 0
1072-    created_at: '2026-05-18T13:54:19.989Z'
1073-    updated_at: '2026-05-18T13:55:17.132Z'
1074-    hypothesis: 'CWM s123 epoch 3 eval @seq4096: 与 s123 epoch 2 @seq4096 (GPU 3 当前在跑,
1075-      ~61%) 形成 clean overtraining 对比，同时与 s42 epoch 3 @seq4096 (~56%) 形成 clean seed
1076-      对比（同 epoch 同 seq，仅 seed 不同）。'
1077-    parent: deepseek-cwm-repo-s123
1078-    conclusion: killed
1079-    notes: 'Superseded by D132v2: s123 e3 无 checkpoint (训练中途死亡), 改为 s123 e2 @seq2048.
1080:      替代实验: D132-cwm-s123-e2-seq2048'
1081:  D132-cwm-s42-e2-seq2048:
1082-    status: PREPARING
1083-    retry_count: 0
1084-    created_at: '2026-05-18T13:55:22.692Z'
1085-    updated_at: '2026-05-18T14:49:07.086Z'
1086-    hypothesis: 'CWM s42 epoch 2 eval @seq2048 (canonical): 与 D131 s42 e3 @seq2048
1087-      对比 = clean overtraining（同 seed 同 seq，仅 epoch 不同）。预期 acc > e3 (~56%) 则确认过拟合。'
1088:    parent: D131-cwm-s42-epoch3-seq2048
1089:    notes: 'Superseded by D133: home 5090 接管 s42 e2 @seq2048。替代实验: D133-cwm-s42-e2-seq2048-home'
1090-    conclusion: killed
1091:  D132-cwm-s123-e2-seq2048:
1092-    status: PREPARING
1093-    retry_count: 0
1094-    created_at: '2026-05-18T13:55:25.420Z'
1095-    updated_at: '2026-05-18T14:49:08.489Z'
1096-    hypothesis: 'CWM s123 epoch 2 eval @seq2048 (canonical): 与 D132 s42 e2 @seq2048
1097-      对比 = clean seed variance（同 epoch 同 seq，仅 seed 不同）。s123 e3 checkpoint 不存在（训练中途死亡）。'
1098-    parent: deepseek-cwm-repo-s123
1099:    notes: 'D133 修改: 从 GPU 3 follow-up 改为 GPU 1 follow-up。GPU 1 当前跑 s42 e3 @seq4096
1100-      完成后接力。GPU 3 follow-up 取消。'
1101:  D133-cwm-s42-e2-seq2048-home:
1102-    status: RUNNING
1103-    retry_count: 0
1104-    created_at: '2026-05-18T15:08:23.581Z'
1105-    updated_at: '2026-05-18T15:08:37.351Z'
1106-    hypothesis: 'CWM s42 epoch 2 eval @seq2048 on home 5090: overtraining baseline。与
1107-      D131 s42 e3 @seq2048 对比 = clean overtraining（同 seed 同 seq，仅 epoch 不同）。'
1108:    parent: D131-cwm-s42-epoch3-seq2048
1109-    spec:
1110-      server: home-1x5090
1111-      gpu: cuda:0
1112-      pid: 4141145
1113-      data_path: /home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl
1114-      data_count: 9784
1115-      model_name: deepseek-coder-6.7b-instruct
1116-      seed: 42
1117-      checkpoint_source: checkpoint-8844 (epoch 2, SCP from seetacloud)
1118-      eval_data: repo_test (9784 instances)
1119-      command: python3 eval_repo_cwm.py --checkpoint_dir /home/sonny/exec-sim-repair-verifier/checkpoints/deepseek_cwm_repo_s42_epoch2/
1120-        --model_name deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/swebench_full
1121-        --max_seq_length 2048 --device cuda:0 --output_dir eval_results/deepseek_cwm_repo_s42_e2_seq2048/
1122-        --split test
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad268b2b-87b7-4ae2-8903-5949e370d822",
  "isSidechain": false,
  "promptId": "4d7675b4-77fa-4209-a180-3e83688a8172",
  "type": "user",
  "uuid": "987d2570-c613-4a9f-bb2e-37078b62d650",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1035:      (canonical=2048)，结果不可用于 Table 4。替代实验: D131-cwm-s42-epoch3-seq2048'\n1036-    completed_at: '2026-05-18T13:52:18.739Z'\n1037:  D131-cwm-s42-epoch3-seq2048:\n1038-    status: RUNNING\n1039-    retry_count: 0\n1040-    created_at: '2026-05-18T13:50:25.467Z'\n1041-    updated_at: '2026-05-18T13:53:32.536Z'\n1042-    hypothesis: 'DeepSeek CWM s42 epoch 3 eval at canonical seq2048: Table 4 主数字，与\n1043-      Qwen CWM repo (65.17% seq2048) 直接可比。预期 ~56% 基于 seq4096 running_acc 趋势。'\n1044-    parent: D124-cwm-s42-epoch2-eval\n1045-    spec:\n1046-      server: seetacloud-westd-4x5090\n1047-      gpu: cuda:2\n1048-      data_path: /home/sonny/exec-sim-repair-verifier/data/repo_test\n1049-      data_count: 9784\n1050-      model_name: deepseek-coder-6.7b-instruct\n1051-      seed: 42\n1052-      checkpoint_source: checkpoint-13266 (epoch 3)\n1053-      eval_data: repo_test (9784 instances)\n1054-      pid: 734440\n1055-      command: python eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/checkpoint-13266\n1056-        --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct\n1057-        --split test --max_seq_length 2048 --max_new_tokens 512 --batch_size 1 --device\n1058-        cuda:0\n1059:  D132-cwm-s42-epoch2-seq4096:\n1060-    status: PREPARING\n1061-    retry_count: 0\n1062-    created_at: '2026-05-18T13:54:17.376Z'\n1063-    updated_at: '2026-05-18T13:55:15.261Z'\n1064-    hypothesis: 'CWM s42 epoch 2 eval @seq4096: 与 s42 epoch 3 @seq4096 (GPU 1 当前在跑)\n1065-      形成 clean overtraining 对比（同 seed 同 seq，仅 epoch 不同）。预期 acc > epoch 3 (~56%) 则确认过拟合。'\n1066-    parent: deepseek-cwm-repo-s42-epoch2-eval\n1067-    conclusion: killed\n1068:    notes: 'Superseded by D132v2: seq4096→seq2048 (canonical). 替代实验: D132-cwm-s42-e2-seq2048'\n1069:  D132-cwm-s123-epoch3-seq4096:\n1070-    status: PREPARING\n1071-    retry_count: 0\n1072-    created_at: '2026-05-18T13:54:19.989Z'\n1073-    updated_at: '2026-05-18T13:55:17.132Z'\n1074-    hypothesis: 'CWM s123 epoch 3 eval @seq4096: 与 s123 epoch 2 @seq4096 (GPU 3 当前在跑,\n1075-      ~61%) 形成 clean overtraining 对比，同时与 s42 epoch 3 @seq4096 (~56%) 形成 clean seed\n1076-      对比（同 epoch 同 seq，仅 seed 不同）。'\n1077-    parent: deepseek-cwm-repo-s123\n1078-    conclusion: killed\n1079-    notes: 'Superseded by D132v2: s123 e3 无 checkpoint (训练中途死亡), 改为 s123 e2 @seq2048.\n1080:      替代实验: D132-cwm-s123-e2-seq2048'\n1081:  D132-cwm-s42-e2-seq2048:\n1082-    status: PREPARING\n1083-    retry_count: 0\n1084-    created_at: '2026-05-18T13:55:22.692Z'\n1085-    updated_at: '2026-05-18T14:49:07.086Z'\n1086-    hypothesis: 'CWM s42 epoch 2 eval @seq2048 (canonical): 与 D131 s42 e3 @seq2048\n1087-      对比 = clean overtraining（同 seed 同 seq，仅 epoch 不同）。预期 acc > e3 (~56%) 则确认过拟合。'\n1088:    parent: D131-cwm-s42-epoch3-seq2048\n1089:    notes: 'Superseded by D133: home 5090 接管 s42 e2 @seq2048。替代实验: D133-cwm-s42-e2-seq2048-home'\n1090-    conclusion: killed\n1091:  D132-cwm-s123-e2-seq2048:\n1092-    status: PREPARING\n1093-    retry_count: 0\n1094-    created_at: '2026-05-18T13:55:25.420Z'\n1095-    updated_at: '2026-05-18T14:49:08.489Z'\n1096-    hypothesis: 'CWM s123 epoch 2 eval @seq2048 (canonical): 与 D132 s42 e2 @seq2048\n1097-      对比 = clean seed variance（同 epoch 同 seq，仅 seed 不同）。s123 e3 checkpoint 不存在（训练中途死亡）。'\n1098-    parent: deepseek-cwm-repo-s123\n1099:    notes: 'D133 修改: 从 GPU 3 follow-up 改为 GPU 1 follow-up。GPU 1 当前跑 s42 e3 @seq4096\n1100-      完成后接力。GPU 3 follow-up 取消。'\n1101:  D133-cwm-s42-e2-seq2048-home:\n1102-    status: RUNNING\n1103-    retry_count: 0\n1104-    created_at: '2026-05-18T15:08:23.581Z'\n1105-    updated_at: '2026-05-18T15:08:37.351Z'\n1106-    hypothesis: 'CWM s42 epoch 2 eval @seq2048 on home 5090: overtraining baseline。与\n1107-      D131 s42 e3 @seq2048 对比 = clean overtraining（同 seed 同 seq，仅 epoch 不同）。'\n1108:    parent: D131-cwm-s42-epoch3-seq2048\n1109-    spec:\n1110-      server: home-1x5090\n1111-      gpu: cuda:0\n1112-      pid: 4141145\n1113-      data_path: /home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl\n1114-      data_count: 9784\n1115-      model_name: deepseek-coder-6.7b-instruct\n1116-      seed: 42\n1117-      checkpoint_source: checkpoint-8844 (epoch 2, SCP from seetacloud)\n1118-      eval_data: repo_test (9784 instances)\n1119-      command: python3 eval_repo_cwm.py --checkpoint_dir /home/sonny/exec-sim-repair-verifier/checkpoints/deepseek_cwm_repo_s42_epoch2/\n1120-        --model_name deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/swebench_full\n1121-        --max_seq_length 2048 --device cuda:0 --output_dir eval_results/deepseek_cwm_repo_s42_e2_seq2048/\n1122-        --split test",
    "numLines": 88
  },
  "sourceToolAssistantUUID": "ad268b2b-87b7-4ae2-8903-5949e370d822",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：DeepSeek repo-level 全部失败（延续 v1-v4 的 pattern），只有 Qwen 单模型族的 repo-level 数据，cross-model 验证仅限 func-level 核心假设：['deepseek-cls-repo-v5 训练失败或 acc ≤ majority base…",
  "leafUuid": "987d2570-c613-4a9f-bb2e-37078b62d650",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Design space characterization for neural code verification",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b"
}
```

---

### Assistant

_source line 31 · 2026-05-18T17:30:00.584Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also check for deepseek-cls-repo-s123 which is DONE with metrics.

The key experiments in play:
1. **deepseek-cls-repo-v5**: RUNNING - training v5 (full 3 epochs)
2. **deepseek-cls-repo-s123**: DONE - acc=74.93% (barely above majority 72.96%)
3. **deepseek-cwm-repo-s42-epoch2-eval**: RUNNING 


4. **D131-cwm-s42-epoch3-seq2048**: RUNNING
5. **D133-cwm-s42-e2-seq2048-home**: RUNNING
6. **deepseek-cwm-repo-s123**: RUNNING

Looking at the worst tier predictions, deepseek-cls-repo-s123 finished with 74.93% accuracy, which is barely above the majority baseline of 72.96%, so deepseek-cls-repo-v5 with the same seed but full 3 epochs would likely perform similarly or worse.

Examining the data more closely, deepseek-cls-repo-v4 had NaN eval losses across all epochs with no best checkpoint, while deepseek-cls-repo-s123 achieved 74.93% accuracy and 53.94% F1 macro. For the worst tier scenario, deepseek-cls-repo-v5 would probably land around 71% accuracy (below baseline) or at best around 75% (barely above, like s123), suggesting the DeepSeek CLS repo doesn't provide meaningful signal.

Now I'm compiling all the predictions and need to generate the YAML output, covering both the planned experiments like diagnostic-rerepair and swebench-pertest-data, as well as the completed ones that define the worst-case scenarios. tier context):**
3. cwm-baseline → actual 87.51%
4. multi-seed-core → actual CLS 88.41±0.96%
5. trace-then-judge → actual: failed
6. traj-level-finetuned → actual: 85.66%
7. model-size-scaling → actual: CLS-8B 90.48%
8. per-test-precision-recall → actual: 87.51%
9. oracle-f2p-stratified → actual
10. oracle-total-validated → actual
11. block-corr-empirical → actual: ICC=0.19
12. repo-level-training → actual: failed
13. llm-judge-baseline → actual: 64.4%/71.7%
14. per-test-majority-voting → actual: negative

Now looking at the experiments still in progress or preparing—several deepseek variants are running with the CLS and CWM approaches, one traj-based experiment completed with around 75.35% mean accuracy, and a couple others that are either preparing or have failed. I need to organize all of this into YAML format. category and include both done and predicted experiments.

Actually, I should focus on the experiments that are still PENDING (planned/RUNNING/PREPARING) since the done ones are actual data. The worst tier is about what happens with the pending experiments.

Let me list the experiments to predict:
1. diagnostic-rerepair (planned)
2. swebench-pertest-data (planned)
3. deepseek-cls-repo-v5 (RUNNING)
4. D131-cwm-s42-epoch3-seq2048 (RUNNING)
5. D133-cwm-s42-e2-seq2048-home (RUNNING)
6. deepseek-cwm-repo-s123 (RUNNING)
7. deepseek-cwm-repo-s42-epoch2-eval (RUNNING, parent of D133)

Plus I should include the done experiments as context with actual data.

Now I'm working through the worst-case predictions for each pending experiment. For deepseek-cls-repo-v5, I'm looking at how v4 failed with NaN loss after just 2 epochs, while the s123 variant barely exceeded the 73% majority baseline at 74.93%. The v5 run uses the full 3-epoch schedule with s42 and a 2048 token sequence length, but given DeepSeek-Coder's 6.7B architecture with its multi-head attention and limited context window training, I'm predicting it'll either fall below the baseline around 71.5% or plateau right at the majority baseline level of 73.2%, which wouldn't represent meaningful improvement. The LoRA capacity seems insufficient for compressing repo-level context at that sequence length.

For the DeepSeek CWM repo experiment at epoch 3 with 2048 sequence length, I'm comparing against Qwen's CWM performance which hit 65.17% at the same sequence length. The partial evaluation at 8192 tokens showed 66.9% before being interrupted, but the 2048 truncation will likely cause severe degradation in generation quality. I'm predicting an 82% unparseable rate with only 48% accuracy on parseable outputs, since most repo-level outputs exceed 2048 tokens and the model has already overfit by epoch 3.

Epoch 2 shows slightly better results with 75% unparseable rate and 55% parseable accuracy, suggesting less overfitting but the same fundamental bottleneck—the DeepSeek tokenizer struggles with structured output generation at the repository level regardless of training duration. The s123 training run failed mid-training and would likely exceed 80% unparseable rate even if it completed, confirming that the issue isn't training stability but rather the model's inherent difficulty with this task at repo scale.

For the diagnostic repair approach, I'm seeing that adding classifier predictions to the repair agent's prompt doesn't help—the agent already has test names and assertion messages available, and the 12.5% error rate in the classifier just introduces noise. The swebench-pertest-data experiment is still in planning stages.

The Docker evaluation task is likely to be only partially done by the deadline since it's CPU-only and getting deprioritized behind GPU work. Even if instances do run, Docker reproducibility issues with SWE-bench patches will cause some failures. Now I'm thinking through how to structure the full experiment results—I need to include all 14 planned experiments plus the critical additional ones, and for completed experiments, I'll use their actual results as the worst-case tier since that's what already happened.

I'm pulling together the aggregated metrics from the function-level experiments to populate the YAML with precise numbers. I'm finishing the standard deviation calculation for the CWM baseline results, which comes out to about 0.375%. Now I'm looking at the performance metrics for the function-level TRAJ approach with Qwen 4B across four seeds, averaging 86.46% with a standard deviation of 0.96%, and the function-level CLS approach with Qwen 8B showing a mean of 89.42% with 0.89% standard deviation. Looking at the function-level results across different models and methods now. The Qwen 8B TRAJ experiments show a mean of 87.70% across two seeds, while DeepSeek results are slightly lower across all three methods—CLS at 86.85%, CWM at 86.83%, and TRAJ at 84.16%. Moving to repo-level evaluation, the Qwen 4B CLS checkpoint achieves 83.63% accuracy, which is a meaningful improvement over the 72.96% majority baseline.

For Qwen 8B at the repo level, I'm seeing the best performance at 85.60% from the seed123 checkpoint, though the CWM variants all failed with high unparseable rates. The DeepSeek repo-level CLS results are disappointing—only 74.93% for seed123, barely above the baseline, while the other variants either failed or are still running.

Now I'm looking at the DeepSeek CWM results, which have training completed but are still evaluating, and the TRAJ results across six seeds showing a mean of 75.35% with notable variance—seed42 performing strongest at 81.25% while seed789 lags at 66.67%. I'm about to compile all these results into a comprehensive YAML format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "987d2570-c613-4a9f-bb2e-37078b62d650",
  "isSidechain": false,
  "requestId": "req_011CbARr38BLiRN9BW4WmgAC",
  "type": "assistant",
  "uuid": "eb859273-26da-40fd-b34a-2347e39acedf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018vgRviCfyzgN9cg1uP24NH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2408,
      "cache_read_input_tokens": 71796,
      "output_tokens": 17582,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17582,
          "cache_read_input_tokens": 71796,
          "cache_creation_input_tokens": 2408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2408
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

_source line 32 · 2026-05-18T17:34:26.927Z_

Now I have the full picture of all pending and completed experiments. Let me compile the worst-tier predictions.

```yaml
tier: worst
narrative_guidance: |
  核心 reframe: repo-level 降为 secondary finding（Qwen-only case study），paper 主体转向
  func-level 双模型族 controlled comparison + per-test diagnostic granularity + block-correlation
  methodological insight。DeepSeek repo-level 全线失败延续 v1-v4 pattern，CLS 至多勉强达到
  majority baseline 水平，CWM 因 unparseable 率过高不可用。TRAJ repo n=48 只能作 supplementary
  evidence。Reviewer 预期反应：novelty 不足（func-level 等价是 predictable null result），
  repo-level generalizability 缺失（单模型族），downstream utility 未验证。
  最终定位：EMNLP Findings（reviewer score 2.5-3.0），需要强调 methodology contribution
  （block-correlation、TOST equivalence testing）和 practical guidance 来补偿 novelty 不足。

imagined_experiments:
  # ============================================================
  # A. Func-level 核心对比（已完成，actual data — 各 tier 共享）
  # ============================================================

  - name: "CWM Generation Baseline (Qwen3-4B)"
    plan_id: cwm-baseline
    status: DONE
    description: "Qwen3-4B LoRA CWM 生成 baseline，预测 execution output 而非 pass/fail"
    expected_results:
      overall_accuracy: 87.51
      pass_f1: 87.31
      fail_f1: 87.71
      exact_match_rate: 84.02
      unparseable_predictions: 0
    result_rationale: |
      Func-level execution output 短且结构化（通常 <50 tokens），Qwen3-4B 能完美解析。
      CWM 与 CLS 在 func-level 本质上等价：CWM 先生成 output 再隐式比较，CLS 直接二分类，
      当 output 空间小时两者信息量一致。87.51% 与 CLS seed42 的 87.83% 在噪声范围内。
    tables: ["Table 2: Func-level formulation comparison"]
    figures_description: []
    analysis: |
      func-level CWM=CLS 是 worst tier 的基础支撑——证明 formulation 选择在低复杂度下不重要，
      这是一个有 statistical backing 的 null result（TOST p=0.007）。

  - name: "Multi-seed Core Comparison (CLS vs CWM vs TRAJ, Qwen3-4B)"
    plan_id: multi-seed-core
    status: DONE
    description: "CLS/CWM 各 5 seeds + TRAJ 4 seeds 的 func-level 多种子验证"
    expected_results:
      cls_4b_mean_acc: 88.43
      cls_4b_std: 0.73
      cls_4b_seeds: {s42: 87.83, s123: 89.52, s456: 87.88, s789: 89.00, s0: 87.94}
      cwm_4b_mean_acc: 87.19
      cwm_4b_std: 0.37
      cwm_4b_seeds: {s42: 87.51, s123: 87.20, s456: 86.98, s789: 86.67, s0: 87.57}
      traj_4b_mean_acc: 86.46
      traj_4b_std: 1.01
      traj_4b_seeds: {s0: 85.66, s123: 85.47, s456: 87.40, s789: 87.31}
      pooled_cls_cwm_gap_pp: -0.45
      tost_p_value: 0.0071
      tost_margin_pp: 2.0
      cls_vs_traj_gap_pp: 1.97
    result_rationale: |
      5-seed CLS 和 CWM 的 pooled gap 仅 0.45pp（CWM 略高），TOST 等价检验 p=0.007 在
      ±2pp margin 内确认统计等价。TRAJ 略低 ~2pp 但方差更大（std=1.01 vs 0.73/0.37），
      反映 trajectory-level aggregation 引入的 problem-level 随机性。三种 formulation
      在 func-level 的差异不具有实际意义。
    tables: ["Table 2: Func-level formulation comparison", "Table 3: Multi-seed statistics"]
    figures_description: ["Fig 2: Box plot of per-seed accuracy across formulations"]
    analysis: |
      这是 paper 最 solid 的 statistical result。TOST p=0.007 是 reviewer 难以反驳的。
      但 novelty concern 在于：func-level 等价本身是 predictable 的（output 短 → 生成不难）。

  - name: "Trace-then-Judge Ablation (Qwen3-4B)"
    plan_id: trace-then-judge
    status: DONE
    description: "Chain-of-thought 式先推理后判断，测试显式 execution reasoning 是否有帮助"
    expected_results:
      conclusion: failed
      training_outcome: "模型未能学会生成有意义的 execution trace，输出退化为模板化文本"
    result_rationale: |
      4B LoRA 容量不足以同时学习 execution reasoning 和 pass/fail 判断。Trace 生成
      引入了额外的 teacher-forcing 误差累积，且训练数据中没有 ground-truth trace 作为监督。
      模型要么忽略 trace 直接跳到 label（使 trace 无意义），要么在 trace 阶段积累错误
      导致最终判断变差。
    tables: []
    figures_description: []
    analysis: |
      负面结果但有叙事价值：证明 "更多推理步骤" 在小模型 + LoRA 场景下不一定有帮助，
      支持直接分类的 simplicity argument。在 worst tier 下降为 footnote。

  - name: "Trajectory-level Finetuned Baseline (Qwen3-4B)"
    plan_id: traj-level-finetuned
    status: DONE
    description: "Qwen3-4B LoRA trajectory-level verifier (resolved/unresolved)"
    expected_results:
      accuracy: 85.66
      unresolved_f1: 87.50
      resolved_f1: 83.18
      per_test_consistency: 79.94
    result_rationale: |
      Trajectory-level 将多个 test 聚合为单一 resolved/unresolved 标签，丢失了 per-test
      粒度信息。85.66% accuracy 低于 per-test CLS 的 88.43% mean，差异来自 aggregation
      信息损失——当一个 problem 有 n 个 test 时，trajectory 模型需要从更长的拼接 input
      中做出单一判断，而 CLS 可以独立判断每个 test。per_test_consistency=79.94% 表明
      约 20% 的 per-test 判断与 trajectory 结论不一致。
    tables: ["Table 2"]
    figures_description: []
    analysis: |
      CLS vs TRAJ 的 ~2pp 差距支持 "per-test 粒度不损失精度" 的 claim。但 worst tier
      下这个差距在 multi-seed 中有时反转（seed456 TRAJ=87.4% > CLS=87.88% 差距仅 0.48pp），
      需要依赖 TOST 而非 point estimate 来论证。

  - name: "Model Size Scaling (Qwen3-8B CLS vs CWM)"
    plan_id: model-size-scaling
    status: DONE
    description: "8B 模型规模下的 CLS vs CWM 对比"
    expected_results:
      cls_8b_mean_acc: 89.39
      cls_8b_seeds: {s42: 90.48, s123: 89.37, s456: 88.31}
      cwm_8b_mean_acc: 86.96
      cwm_8b_seeds: {s42: 87.67, s123: 86.98, s456: 86.24}
      cls_8b_vs_cwm_8b_gap_pp: 2.43
      cls_4b_vs_8b_gain_pp: 0.96
      cwm_4b_vs_8b_gain_pp: -0.23
    result_rationale: |
      CLS 从 4B→8B 提升约 1pp（88.43→89.39%），CWM 几乎不变（87.19→86.96%，甚至略降）。
      这表明 CWM 的瓶颈不在模型容量而在 formulation 本身——生成 exact output 的 ceiling
      由 exact_match 约束决定，更大模型不能突破。CLS 因为是 binary classification 任务，
      更大模型的 representation capacity 能略微提升边界样本的判断。8B 规模下 CLS 首次
      明确超过 CWM（2.43pp gap，超出 multi-seed 噪声范围）。
    tables: ["Table 2"]
    figures_description: []
    analysis: |
      8B CLS > CWM 的 gap 比 4B 更明显，但仍然在 func-level。这个结果在所有 tier 共享，
      worst tier 下支持 "scaling 不帮助 CWM" 的 finding。

  - name: "LLM Judge Zero-shot Baseline (Qwen3-8B/32B)"
    plan_id: llm-judge-baseline
    status: DONE
    description: "零样本 LLM-as-judge 基线，per-test + trajectory-level"
    expected_results:
      per_test_8b_acc: 64.4
      per_test_32b_acc: 71.69
      majority_baseline: 51.75
      traj_8b_acc: 99.1
      traj_32b_acc: 99.12
      traj_8b_true_resolved: 1
      traj_8b_pred_resolved: 0
    result_rationale: |
      Per-test 零样本表现远低于 fine-tuned（64-72% vs 87-90%），因为模型需要理解
      mutation 引入的 subtle 错误并预测 test 行为，而非简单的 pattern matching。
      Trajectory-level 99.1% 是虚假高分——模型几乎总是预测 "unresolved"，在 114 个
      problem 中只有 1 个是 resolved，majority baseline 就是 99.1%。这暴露了零样本
      trajectory-level 评估在极度 imbalanced 场景下的无效性。
    tables: ["Table 2: as baseline row"]
    figures_description: []
    analysis: |
      Fine-tuned vs zero-shot 的巨大 gap（87% vs 64-72%）证明 task-specific training
      的必要性。Zero-shot TRAJ 的 99.1%（=majority baseline）是 cautionary result。

  - name: "Per-test Majority Voting (K=3)"
    plan_id: per-test-majority-voting
    status: DONE
    description: "Self-consistency 多数投票，测试 K=3 采样是否提升准确率"
    expected_results:
      accuracy_greedy: 87.51
      accuracy_majority_vote: 86.83
      delta_pp: -0.69
      net_flips: -13
      wall_time_ratio: 4.0
    result_rationale: |
      Greedy decoding 在 classification 任务上已接近模型能力上限。K=3 采样引入的随机性
      对 high-confidence 正确预测无帮助，反而对 low-confidence 边界样本引入噪声：
      28 个正确→错误 vs 15 个错误→正确 = net -13 flips。CLS 的 decision boundary 是
      deterministic 的（logit > 0 → pass），temperature sampling 只会模糊这个边界。
      这与 generation 任务（如 code generation）中 majority voting 有效不同。
    tables: []
    figures_description: []
    analysis: |
      负面结果。排除了一个简单的 improvement avenue，但不影响核心叙事。
      在 worst tier 下可以放入 appendix 或完全省略。

  # ============================================================
  # B. Func-level DeepSeek 跨模型验证（已完成，actual data）
  # ============================================================

  - name: "DeepSeek Func-level Cross-model Validation (CLS + CWM + TRAJ)"
    plan_id: multi-seed-core  # extension
    status: DONE
    description: "DeepSeek-Coder-6.7B 上重复 func-level 三种 formulation 对比"
    expected_results:
      deepseek_cls_mean: 86.85
      deepseek_cls_seeds: {s42: 86.93, s123: 86.77}
      deepseek_cwm_mean: 86.83
      deepseek_cwm_seeds: {s42: 85.77, s123: 87.88}
      deepseek_traj_mean: 84.16
      deepseek_traj_seeds: {v2: 83.24, v2_s123: 85.08}
      deepseek_cwm_unparseable_rate: 0.0
      cross_model_cls_cwm_gap_pp: 0.02
      cross_model_cls_traj_gap_pp: 2.69
    result_rationale: |
      DeepSeek func-level 重现了 Qwen 的 pattern：CLS≈CWM（86.85 vs 86.83%，gap 0.02pp），
      TRAJ 略低（84.16%，gap ~2.7pp）。注意 DeepSeek CWM unparseable=0%，与 Qwen CWM
      func-level 一致——func-level output 足够短，两种 tokenizer 都能完美解析。
      DeepSeek TRAJ 比 Qwen TRAJ 低 ~2pp，可能因为 DeepSeek-Coder 的 instruction-following
      能力在 trajectory aggregation 场景下略弱。
    tables: ["Table 2: DeepSeek rows"]
    figures_description: []
    analysis: |
      Func-level 双模型族验证完整且 clean。CLS≈CWM 在两个模型族都成立。
      这是 worst tier 最强的跨模型证据，但 reviewer 会认为 func-level 等价本身 novelty 低。

  # ============================================================
  # C. Per-test Diagnostic 分析（已完成，actual data）
  # ============================================================

  - name: "Per-test Failure Prediction Precision/Recall"
    plan_id: per-test-precision-recall
    status: DONE
    description: "Per-test 粒度的 failure 预测精度分析"
    expected_results:
      accuracy: 87.51
      fail_precision: 82.75
      fail_recall: 93.64
      fail_f1: 87.86
      best_mutation: "return_value (97.26%)"
      worst_mutation: "off_by_one (82.56%)"
    result_rationale: |
      High recall (93.64%) 意味着模型捕获了绝大多数真实 failure，但 precision (82.75%)
      说明约 17% 的 failure 预测是误报。这在 diagnostic 场景下是可接受的——宁可多报
      failure 也不要漏掉（fail-safe 偏好）。Mutation type 分析显示 return_value mutations
      最容易检测（明显的输出差异），off_by_one 最难（微妙的边界差异）。
    tables: ["Table 5: Per-test diagnostic quality"]
    figures_description: ["Fig 4: Per-mutation-type accuracy breakdown"]
    analysis: |
      Diagnostic granularity 分析完整。但没有 downstream 验证（re-repair 为负），
      worst tier 下只能声称 "potentially useful for debugging" 而非 "proven useful"。

  - name: "Oracle F2P Stratified Analysis"
    plan_id: oracle-f2p-stratified
    status: DONE
    description: "按 failing test 数量分层的 oracle advantage 分析"
    expected_results:
      T1_pct: 68.7
      T1_block_adv: -0.09
      T2_pct: 19.1
      T2_block_adv: 31.69
      T3_5_block_adv: 40.74
      T6plus_block_adv: 40.06
      overall_block_adv: 10.93
      T2_contribution_pct: 55.3
    result_rationale: |
      68.7% 的 instances 只有 1 个 failing test (T=1)，此时 per-test 和 trajectory-level
      信息等价（只有一个 test 决定成败）。Per-test 优势集中在 T≥2（31.5% 的 instances），
      其中 T=2 贡献了 55.3% 的总 advantage。这是因为 T=2 时 per-test 能区分 "一个 test fail"
      vs "两个 test fail" 而 trajectory 只能说 "unresolved"。T≥3 的 advantage 更大但
      instance 更少。SWE-bench 的 median F2P=1 限制了 per-test 的 practical impact。
    tables: ["Table 6"]
    figures_description: ["Fig 5: Advantage by T-bucket"]
    analysis: |
      Oracle analysis 显示 per-test 的理论优势存在但受限于 T=1 dominance。
      Worst tier 下 reviewer 会指出 "68.7% 的 instances per-test 不提供额外信息"。

  - name: "Block Correlation Empirical Validation"
    plan_id: block-corr-empirical
    status: DONE
    description: "验证 per-test predictions 的 intra-problem 相关性结构"
    expected_results:
      icc: 0.1909
      icc_p_value: 0.0
      design_effect: 3.9676
      all_correct_observed: 46
      all_correct_expected_iid: 16.35
      all_correct_ratio: 2.81
    result_rationale: |
      ICC=0.19 表明同一 problem 内的 per-test 预测错误有显著相关性（p<0.001），
      design effect=3.97 意味着 effective sample size 约为 nominal 的 1/4。
      Observed all-correct rate (46/114=40.4%) 远高于 i.i.d. 预期 (14.3%)，
      ratio=2.81 说明模型错误在 problem 内是 clustered 的——要么全对，要么错多个。
      这挑战了 per-test evaluation 中常见的 i.i.d. 假设。
    tables: ["Table 7: Block correlation analysis"]
    figures_description: []
    analysis: |
      这是一个 methodological contribution：揭示 per-test evaluation 中 i.i.d. 假设
      不成立，标准 CI 会低估 variance。ICC=0.19 + DE=3.97 是 clean statistical result。
      Worst tier 下这可能是最独特的贡献——之前没有工作量化过 per-test verification 中的
      intra-problem correlation。但 reviewer 可能认为这更适合 statistics 会议。

  - name: "Oracle Total (F2P+P2P) Validated"
    plan_id: oracle-total-validated
    status: DONE
    description: "包含 P2P regression tests 的 oracle advantage 验证"
    expected_results:
      total_reg5pct_block_adv: -0.005
      total_reg10pct_block_adv: 0.083
      total_reg20pct_block_adv: 0.278
      total_reg5pct_pass: false
      total_reg10pct_pass: true
    result_rationale: |
      P2P regression rate ≤5% 时 per-test advantage 消失（-0.5pp），因为 P2P tests
      几乎全 pass，不提供 discriminative 信息。只有 regression rate ≥10% 时 per-test
      才有正 advantage。实际 regression rate 通常 <5%（高质量修复），这意味着
      per-test 的优势主要在 F2P tests 上，P2P tests 是 noise source。
    tables: ["Table 6 extended"]
    figures_description: []
    analysis: |
      P2P 在低 regression rate 下无帮助甚至有害。Worst tier 下这个发现缩窄了 per-test
      的 applicable scope，reviewer 会用这个来质疑 practical significance。

  # ============================================================
  # D. Repo-level Qwen 实验（mostly done，defines worst-tier Qwen ceiling）
  # ============================================================

  - name: "Repo-level CLS (Qwen3-4B, best checkpoint)"
    plan_id: repo-level-training  # part of repo-level training family
    status: DONE
    description: "Qwen3-4B LoRA repo-level classification，最优 checkpoint 评估"
    expected_results:
      best_checkpoint: ckpt-4600
      test_accuracy: 83.63
      test_f1_macro: 75.63
      test_fail_f1: 61.67
      test_pass_f1: 89.59
      majority_baseline: 72.96
      gap_vs_baseline_pp: 10.67
      val_accuracy: 90.07
      val_test_gap_pp: 6.44
    result_rationale: |
      Repo-level CLS 在 Qwen3-4B 上达到 83.63% test accuracy，显著超过 majority baseline
      10.67pp。但 val-test gap 高达 6.44pp 暴露了 overfitting 或 distribution shift。
      Fail_f1 仅 61.67%（vs func-level 88%），说明 repo-level 的长 context + 复杂依赖
      大幅增加了分类难度。这是 worst tier Qwen repo-level 的 reference point。
    tables: ["Table 4: Repo-level comparison"]
    figures_description: []
    analysis: |
      83.63% 在 worst tier 范围 [83, 86] 的下端。只有 Qwen 一个模型族达到这个水平，
      reviewer 会质疑 generalizability。

  - name: "Repo-level CLS (Qwen3-8B, best configurations)"
    plan_id: repo-level-training
    status: DONE
    description: "Qwen3-8B LoRA repo-level classification，多 seed 多 checkpoint"
    expected_results:
      best_s42_ckpt: ckpt-400
      best_s42_test_acc: 84.79
      best_s123_ckpt: ckpt-3000
      best_s123_test_acc: 85.60
      best_s123_val_acc: 88.69
      majority_baseline: 72.96
    result_rationale: |
      8B 比 4B 提升 1-2pp（84.79/85.60 vs 83.63），但 s42 和 s123 的 best checkpoint
      差异巨大（ckpt-400 vs ckpt-3000），暗示 repo-level 训练对 seed 和 checkpoint
      选择极度敏感。Overfitting 严重——s42 继续训练到 ckpt-1000+ 后 accuracy 反而
      下降到 83-84%。这种 instability 是 reviewer concern 的来源。
    tables: ["Table 4"]
    figures_description: []
    analysis: |
      85.60% 是 Qwen repo-level CLS 的 ceiling。但 checkpoint 选择的高度敏感性
      削弱了结果的可靠性。Worst tier 下 reviewer 会质问 "你怎么选 checkpoint"。

  - name: "Repo-level CWM (Qwen, all versions)"
    plan_id: repo-level-training
    status: DONE
    description: "Qwen3 repo-level CWM generation，v3-v12 全部尝试"
    expected_results:
      v10_accuracy: 69.91
      v10_unparseable_pct: 93.0
      v11_accuracy: 66.6
      v11_unparseable_pct: 75.2
      v12_accuracy: 58.04
      v12_unparseable_pct: 53.7
      best_parseable_accuracy: "~42-58% (估计)"
      all_versions_below_majority: true
    result_rationale: |
      Qwen tokenizer 在 repo-level 长 output 生成中灾难性失败。v10（max_new_tokens=64）
      93% unparseable——token budget 太小无法生成完整 execution output。放宽到更大 budget
      后 v12 unparseable 降到 53.7% 但 accuracy 更差（58%）——模型在长生成中 drift。
      Qwen3 的 tokenizer 对结构化 execution output 的 token 效率极低，是 model-specific
      failure 而非 formulation-inherent failure。
    tables: ["Table 4: CWM row"]
    figures_description: []
    analysis: |
      CWM repo-level 在 Qwen 上彻底失败。Worst tier 下无法报告有意义的 CWM repo accuracy，
      只能报告 unparseable rate 作为 negative finding。但这反而支持 "CWM failure 是
      tokenizer-specific" 的 claim——如果 DeepSeek CWM repo 也失败（worst tier 假设），
      则需要修改为 "CWM repo failure 可能是 formulation-inherent at small model scale"。

  # ============================================================
  # E. Repo-level DeepSeek（RUNNING/PREPARING — worst-tier 关键预测）
  # ============================================================

  - name: "DeepSeek CLS Repo-level v5 (seed42, full 3 epochs)"
    plan_id: repo-level-training  # extension to DeepSeek
    status: RUNNING
    description: "DeepSeek-Coder-6.7B repo-level CLS，v5 完整 3 epoch 训练"
    expected_results:
      training_outcome: "完成但 acc 未超过 majority baseline"
      test_accuracy: 71.5
      f1_macro: 54.2
      f1_fail: 28.3
      f1_pass: 80.1
      majority_baseline: 72.96
      gap_vs_baseline_pp: -1.46
      unparseable_rate: 0.01
      confusion_pattern: "严重偏向预测 pass，recall_fail < 20%"
    result_rationale: |
      v4（2 epoch 不完整）eval_loss=NaN 所有 epoch，process killed。v5 是 v4 的完整重跑。
      v4 已有的 ckpt-200 eval（71.37% acc）低于 majority baseline。s123 的完整训练
      也只达到 74.93%（勉强高于 73% baseline），且 recall_fail=13.72% 几乎不识别 fail。
      DeepSeek-Coder 在 repo-level 的核心问题：(1) max_seq_length=2048 对 repo context
      截断过多（平均 repo input ~5000 tokens），丢失关键依赖信息；(2) 6.7B LoRA 容量
      不足以学习 repo-level 的复杂 pass/fail pattern；(3) eval_loss=NaN 暗示训练不稳定，
      3 epoch 可能过拟合或 loss landscape 有 pathological region。
      Worst tier 预测 v5 在 70-73% 范围，不超过 majority baseline。
    tables: ["Table 4: DeepSeek CLS row — 标注为 ≈baseline 或 below baseline"]
    figures_description: []
    analysis: |
      DeepSeek CLS repo v1-v5 全部失败。s123 的 74.93% 是唯一勉强高于 baseline 的数据点，
      但 f1_fail=22.84% 说明模型几乎不能识别 failure（几乎全预测 pass）。
      Worst tier 叙事：DeepSeek repo-level CLS 不可用，repo-level 比较仅限 Qwen。

  - name: "DeepSeek CLS Repo-level s123 (seed123)"
    plan_id: repo-level-training
    status: DONE
    description: "DeepSeek-Coder-6.7B repo-level CLS seed=123 的评估结果"
    expected_results:
      test_accuracy: 74.93
      f1_macro: 53.94
      f1_fail: 22.84
      f1_pass: 85.03
      recall_fail: 13.72
      recall_pass: 97.62
      majority_baseline: 72.96
      gap_vs_baseline_pp: 1.97
    result_rationale: |
      74.93% 仅比 majority baseline 高 1.97pp。F1_fail=22.84% 揭示模型几乎完全
      collapse 到 majority class (pass)：recall_fail=13.72% 意味着 86% 的真实 failure
      被误判为 pass。这不是一个有用的分类器——一个简单的 "always predict pass" baseline
      就能达到 73%。Gap 1.97pp 在 multi-seed 噪声范围内不可靠。
    tables: ["Table 4"]
    figures_description: []
    analysis: |
      这个结果已经 confirm worst-tier 假设。DeepSeek CLS repo essentially at majority baseline。
      Combined with v5 prediction, worst tier 叙事完全成立。

  - name: "DeepSeek CWM Repo-level s42 Epoch 3 (canonical seq2048)"
    plan_id: repo-level-training
    status: RUNNING
    description: "D131: DeepSeek CWM repo s42 epoch 3 在 canonical seq2048 下的评估"
    expected_results:
      test_accuracy: 52.3
      f1_macro: 44.8
      f1_fail: 18.5
      f1_pass: 71.1
      unparseable_rate: 82.0
      unparseable_count: 8023
      parseable_only_accuracy: 48.5
      majority_baseline: 72.96
      gap_vs_baseline_pp: -20.66
    result_rationale: |
      seq2048 比 seq4096/8192 截断更严重，留给 output generation 的 token budget 更少。
      D124 在 seq8192 下 running_acc=66.9%（31% 完成时 killed），seq4096 下 partial eval
      显示更差的趋势。seq2048 进一步限制 context → 更多 truncation → 更多 unparseable。
      Qwen CWM repo 在 seq2048 下 65.17% accuracy（已是 failure），DeepSeek 预期更差因为：
      (1) DeepSeek-Coder tokenizer 的 token 效率对 Python execution output 更低；
      (2) Epoch 3 过拟合（训练 loss 从 0.021 降到极低但 eval 退化）；
      (3) 93% unparseable 在 Qwen 上的 pattern 在 DeepSeek 上可能同样严重或更严重。
      Worst tier 预测 unparseable ≥80%，可用 accuracy 远低于 baseline。
    tables: ["Table 4: DeepSeek CWM row — 标注为 N/A 或 'unparseable >80%'"]
    figures_description: []
    analysis: |
      CWM repo 在 DeepSeek 上也失败（worst tier 假设核心之一）。如果两个模型族的 CWM repo
      都失败，则不能说 "CWM failure 是 tokenizer-specific"——需要修改为 "CWM repo failure
      appears formulation-inherent at 4-8B LoRA scale"。这削弱了原 framing 中
      "tokenizer-specific" 这个最有 novelty 的 finding。

  - name: "DeepSeek CWM Repo-level s42 Epoch 2 (overtraining baseline)"
    plan_id: repo-level-training
    status: RUNNING
    description: "D133: DeepSeek CWM repo s42 epoch 2 在 seq2048 下的评估，用于 overtraining 对比"
    expected_results:
      test_accuracy: 56.8
      f1_macro: 47.2
      f1_fail: 21.3
      f1_pass: 73.1
      unparseable_rate: 76.0
      parseable_only_accuracy: 53.2
      epoch3_accuracy: 52.3
      overtraining_gap_pp: 4.5
    result_rationale: |
      Epoch 2 应比 epoch 3 略好（less overfitting），但差异可能很小（~4pp）。
      原因：(1) CWM repo 的根本问题是 generation 任务本身在 repo-level context 下太难，
      不仅仅是 overfitting；(2) eval_loss=NaN 在所有 epoch（已知 DeepSeek issue），
      无法通过 eval loss 选择最优 epoch；(3) unparseable 问题在 epoch 2 就已存在，
      epoch 3 只是略微恶化。
      Worst tier 下 epoch 2 仍然不可用——unparseable ≥76%，accuracy 远低于 baseline。
      Overtraining 可能存在但不是主要原因（根本原因是 formulation + scale mismatch）。
    tables: ["Appendix: overtraining analysis"]
    figures_description: []
    analysis: |
      即使 epoch 2 比 epoch 3 好 4-5pp，仍然在 majority baseline 以下。
      结论变为 "CWM repo failure 不仅是 overfitting，也是 capacity limitation"。
      这对叙事有双重影响：(1) 削弱 "只需更多训练调优" 的反驳；
      (2) 也削弱 "tokenizer-specific" 的 claim（两个模型都失败）。

  - name: "DeepSeek CWM Repo-level s123 (seed 123 replication)"
    plan_id: repo-level-training
    status: RUNNING
    description: "DeepSeek CWM repo seed=123 训练+评估"
    expected_results:
      training_outcome: "训练中途死亡或仅完成 2 epochs"
      eval_accuracy: 55.0
      unparseable_rate: 80.0
      f1_macro: 42.5
    result_rationale: |
      Registry 显示 s123 训练已中断（D132 notes 提到 "s123 e3 checkpoint 不存在，
      训练中途死亡"）。只有 epoch 2 checkpoint 可用。Worst tier 下评估结果与 s42
      类似或更差：unparseable ≥80%，accuracy 远低于 baseline。训练不稳定进一步
      证实 DeepSeek CWM repo 的 unreliability。
    tables: ["Table 4: or Appendix"]
    figures_description: []
    analysis: |
      训练中断 + 评估不可用 = deepseek-cwm-repo 完全不可报告。
      Worst tier 下 Table 4 的 DeepSeek CWM 列标注为 "training failed" 或 "—"。

  - name: "DeepSeek TRAJ Repo-level (multi-seed, n=48)"
    plan_id: repo-level-training
    status: DONE
    description: "DeepSeek-Coder-6.7B trajectory-level repo verifier，6 seeds"
    expected_results:
      seed_results:
        s42: {acc: 81.25, f1_macro: 80.58}
        s123: {acc: 75.0, f1_macro: 74.83}
        s0: {acc: 75.0, f1_macro: 72.68}
        s789: {acc: 66.67, f1_macro: 62.50}
        s456: {acc: 75.0, f1_macro: 75.0}
        s999: {acc: 79.2, f1_macro: 78.57}
      mean_accuracy: 75.35
      std_accuracy: 4.89
      majority_baseline: 54.2
      gap_vs_baseline_pp: 21.15
      test_set_size: 48
    result_rationale: |
      TRAJ repo 是唯一跑通的 DeepSeek repo-level formulation。Mean 75.35% 显著超过
      majority baseline (54.2%)，但 (1) n=48 太小，CI 极宽；(2) std=4.89% 跨 seed
      方差巨大（66.67%-81.25%）；(3) 无法与 Qwen TRAJ repo 直接对比因为 Qwen TRAJ repo
      不存在（只有 CLS 和 CWM）。TRAJ 的 "成功" 可能因为 task 更简单——只需判断
      resolved/unresolved 而非预测每个 test 的 pass/fail，对 input 质量要求更低。
    tables: ["Table 4: DeepSeek TRAJ row"]
    figures_description: []
    analysis: |
      n=48 是 worst tier 的关键弱点。Reviewer 会指出：6 seeds 的 mean 75.35% 的 95% CI
      约 [70.4, 80.3]（基于 t-distribution），如此宽的 CI 无法做任何有意义的 formulation
      对比。只能作为 "supplementary evidence that TRAJ is feasible at repo-level" 而非
      core finding。

  # ============================================================
  # F. 0-shot Baselines（已完成，actual data）
  # ============================================================

  - name: "Zero-shot Baselines (Qwen + DeepSeek, func + repo)"
    plan_id: llm-judge-baseline  # related
    status: DONE
    description: "Qwen3-4B 和 DeepSeek-Coder-6.7B 的零样本基线"
    expected_results:
      qwen_0shot_func_acc: 68.73
      deepseek_0shot_func_acc: 63.02
      qwen_0shot_repo_acc: 49.9
      deepseek_0shot_repo_acc: 48.54
      repo_majority_baseline: 72.96
      func_majority_baseline: 51.75
    result_rationale: |
      0-shot 在 func-level 超过 majority baseline (68.7/63.0 vs 51.75%)，但在 repo-level
      几乎是 random（49.9/48.5% vs majority 73%）。Repo-level 0-shot 甚至低于 majority
      baseline 24pp，说明无 finetuning 的模型完全无法处理 repo-level context。
      DeepSeek 0-shot 比 Qwen 差 ~5pp，一致 pattern。
    tables: ["Table 2 & 4: 0-shot baseline row"]
    figures_description: []
    analysis: |
      0-shot baseline 建立了 fine-tuning 必要性的论证。Repo-level 0-shot 的灾难表现
      也解释了为什么 repo-level fine-tuning 如此困难——task 本身在 0-shot 下不可解。

  # ============================================================
  # G. 下游应用（planned — worst-tier 预测）
  # ============================================================

  - name: "Diagnostic Re-repair (downstream proof-of-concept)"
    plan_id: diagnostic-rerepair
    status: planned
    description: "用 per-test failure 预测辅助 repair agent 的下游验证"
    expected_results:
      prediction: "负面结果或未完成"
      control_pass1: 41.0
      cls_diagnostic_pass1: 42.5
      oracle_diagnostic_pass1: 44.0
      random_diagnostic_pass1: 38.0
      improvement_over_control_pp: 1.5
      p_value: 0.42
      n_instances: 44
    result_rationale: |
      已有两个 preliminary 实验的负面结果：
      - re-repair-phase0 (n=10): control 0.82, cls_diag 0.818, oracle_diag 0.809
      - re-repair-docker-eval (n=44): A1=52.3, A2=43.2, B=36.4, C=38.6, D=40.9
      两者都未显示 diagnostic information 的有意义改善。核心原因：(1) LLM repair agent
      已经从 test source code 和 error message 中获取了大部分 diagnostic 信息，
      per-test classifier 预测（87.5% acc）的额外信号被模型已有信息淹没；
      (2) 12.5% 的错误预测会误导 repair agent；(3) 样本量太小（n=44）无法检测
      微小效应。Worst tier 下该实验要么不运行（deadline 压力），要么确认负面结果。
    tables: []
    figures_description: []
    analysis: |
      Re-repair 负面结果是 worst tier 最大的 downstream utility gap。
      Paper 必须将 efficiency（6-9x speedup）和 diagnostic granularity 定位为
      independent contribution，而非依赖 re-repair 作为 downstream validation。
      Reviewer 会问 "so what's the point of per-test if it doesn't help repair?"——
      回答需要是 "per-test enables fine-grained verification feedback for developers,
      not just automated repair" + "efficiency advantage is standalone"。

  - name: "SWE-bench PerTest Dataset Construction"
    plan_id: swebench-pertest-data
    status: planned
    description: "Docker re-evaluation 构建 SWE-bench per-test 数据集"
    expected_results:
      prediction: "未完成或仅部分完成"
      instances_attempted: 500
      instances_completed: 280
      instances_with_clean_labels: 220
      completion_rate: 0.44
      label_quality_issues: "Docker 环境差异导致约 20% 的 test 结果与原始不一致"
    result_rationale: |
      9 天到 deadline，Docker re-evaluation 需要 16-24h 计算 + 环境调试时间。
      SWE-bench Docker 复现已知困难：(1) Python 版本依赖；(2) package version conflicts；
      (3) test framework compatibility（pytest vs unittest）；(4) 部分 repo 需要
      system-level dependencies (C extensions, database servers)。
      Worst tier 下优先级低于 GPU 实验（deepseek repo-level），可能被搁置。
      即使部分完成，数据质量可能不足以支撑 paper 中的 resource contribution claim。
    tables: []
    figures_description: []
    analysis: |
      SWE-bench PerTest 作为 resource contribution 在 worst tier 下不可用。
      Paper 只能使用现有 func-level 数据集（CRUXEval-based）+ Qwen repo-level 数据。
      这进一步限制了 paper 的 contribution breadth。

  # ============================================================
  # H. Qwen CWM Repo Epoch 对比（D124 系列，partially done）
  # ============================================================

  - name: "Qwen CWM Repo Epoch 2 Eval (D124)"
    plan_id: repo-level-training
    status: PREPARING
    description: "Qwen CWM repo-level s42 epoch 2 评估，验证 overtraining"
    expected_results:
      prediction: "略好于最终 epoch 但仍不可用"
      accuracy: 55.0
      unparseable_rate: 88.0
      parseable_accuracy: 48.0
      epoch3_comparison: "与 epoch 3 差异 <5pp"
    result_rationale: |
      Qwen CWM repo v10-v12 在最终 epoch 的 unparseable rate 53-93%。Epoch 2 理论上
      过拟合更少，但 CWM 的核心问题是 generation task 本身对 repo-level 太难，
      不是 epoch 数量的问题。Qwen tokenizer 在 repo-level output 上的低效率
      导致即使 epoch 2 也有极高 unparseable rate。如果使用与 v10 相同的
      max_new_tokens=64，unparseable 不会显著下降。
    tables: ["Appendix: overtraining analysis"]
    figures_description: []
    analysis: |
      Overtraining analysis 可以放 appendix 作为 methodological rigor 的证据，
      但不改变 "CWM repo 在 Qwen 上失败" 的核心结论。

  # ============================================================
  # I. 汇总分析
  # ============================================================

  - name: "Worst-Tier Repo-level Summary Table 预测"
    plan_id: repo-level-training
    status: "imagined_aggregate"
    description: "Table 4 在 worst tier 下的完整面貌"
    expected_results:
      qwen_cls_4b_test: 83.63
      qwen_cls_8b_best_test: 85.60
      qwen_cwm_4b_test: "N/A (93% unparseable)"
      qwen_cwm_8b_test: "N/A (75% unparseable)"
      qwen_traj_4b_test: "N/A (not trained)"
      deepseek_cls_test: "71.5 (≈majority baseline 73%)"
      deepseek_cwm_test: "N/A (82% unparseable)"
      deepseek_traj_test: "75.35±4.89 (n=48)"
      majority_baseline: 72.96
      cross_model_validated: false
      single_model_only: "Qwen CLS"
    result_rationale: |
      Table 4 只有两个有意义的 cell：Qwen CLS 4B (83.63%) 和 Qwen CLS 8B (85.60%)。
      所有 CWM repo 都失败（双模型族）。DeepSeek CLS repo 在 majority baseline 附近。
      DeepSeek TRAJ repo 有数据但 n=48 + high variance。
      这意味着 repo-level 的 formulation comparison 完全不成立——
      只有一种 formulation (CLS) 在一个模型族 (Qwen) 上有效。
    tables: ["Table 4"]
    figures_description: []
    analysis: |
      Worst tier 的 Table 4 本质上是一个 Qwen CLS 表，其他 cell 都是 N/A 或 ≈baseline。
      这导致 paper 无法 claim "CLS > CWM at repo-level"（CWM 数据不可用，不是 CLS 更好），
      也无法 claim cross-model consistency（只有 Qwen）。
      Paper 必须重新定位 repo-level：不是 "formulation comparison" 而是
      "case study showing that classification transfers to repo-level while generation collapses"。

  - name: "Worst-Tier Paper Contribution 重评估"
    plan_id: null
    status: "meta_analysis"
    description: "Worst tier 下 paper 三条贡献线的强度评估"
    expected_results:
      contribution_1_formulation_equivalence:
        strength: "medium"
        evidence: "func-level 双模型族 5-seed TOST p=0.007"
        weakness: "func-level 等价是 predictable; repo-level 无法比较"
        reviewer_likely_score: 3.0
      contribution_2_diagnostic_granularity:
        strength: "medium-weak"
        evidence: "CLS vs TRAJ 2pp gap + 6-9x speedup + per-test diagnostics"
        weakness: "no downstream validation; 68.7% instances T=1 无额外信息"
        reviewer_likely_score: 2.5
      contribution_3_methodology:
        strength: "medium"
        evidence: "ICC=0.19, DE=3.97 block-correlation; TOST framework"
        weakness: "niche contribution; may not excite NLP reviewers"
        reviewer_likely_score: 3.0
      overall_expected_score: 2.75
      venue_outcome: "Borderline Findings (2.5-3.0)"
    result_rationale: |
      Worst tier 下三条线都有 solid 数据但没有 breakthrough：
      (1) Func-level 等价是 well-executed null result 但 predictable；
      (2) Diagnostic granularity 缺 downstream proof，efficiency 是 engineering 而非 science；
      (3) Block-correlation 是 novel 但 niche（statistics contribution in NLP venue）。
      没有一条线单独能达到 EMNLP main 4.0。组合起来 2.5-3.0 = Findings 水平。
      如果写作极好（clear story + honest scoping），可能 push 到 3.0-3.5。
    tables: []
    figures_description: []
    analysis: |
      Worst tier 的 paper 策略：
      1. 放弃 repo-level 作为 core contribution → 降为 "exploratory case study"
      2. 主推 func-level controlled comparison methodology + statistical rigor
      3. Block-correlation 作为 "unexpected methodological finding"
      4. Re-repair 负面结果诚实报告为 future work motivation
      5. 标题改为聚焦 func-level："Per-Test vs Trajectory-Level Verification:
         A Controlled Study across Formulations and Model Families"
      6. 投稿目标现实调整：EMNLP Findings 作为 primary goal
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb859273-26da-40fd-b34a-2347e39acedf",
  "isSidechain": false,
  "requestId": "req_011CbARr38BLiRN9BW4WmgAC",
  "type": "assistant",
  "uuid": "bb1d84be-a89d-4729-8dd8-37b239e4bd81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018vgRviCfyzgN9cg1uP24NH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2408,
      "cache_read_input_tokens": 71796,
      "output_tokens": 17582,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17582,
          "cache_read_input_tokens": 71796,
          "cache_creation_input_tokens": 2408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2408
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：DeepSeek repo-level 全部失败（延续 v1-v4 的 pattern），只有 Qwen 单模型族的 repo-level 数据，cross-model 验证仅限 func-level 核心假设：['deepseek-cls-repo-v5 训练失败或 acc ≤ majority base…",
  "leafUuid": "bb1d84be-a89d-4729-8dd8-37b239e4bd81",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Design space characterization for neural code verification",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：DeepSeek repo-level 全部失败（延续 v1-v4 的 pattern），只有 Qwen 单模型族的 repo-level 数据，cross-model 验证仅限 func-level 核心假设：['deepseek-cls-repo-v5 训练失败或 acc ≤ majority base…",
  "leafUuid": "bb1d84be-a89d-4729-8dd8-37b239e4bd81",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Design space characterization for neural code verification",
  "sessionId": "8924b315-2a19-4485-9a63-be59f1a2ff4b"
}
```

---
