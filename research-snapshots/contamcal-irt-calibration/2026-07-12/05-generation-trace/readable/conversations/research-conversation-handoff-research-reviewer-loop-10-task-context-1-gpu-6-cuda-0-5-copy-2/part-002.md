# Research conversation: [HANDOFF] 你是 Research Reviewer，这是 Loop #10。 ## 上一轮交接 (task_context) ### 1. 🔴 硬约束 / 红线 - **GPU 白名单**: 全部 6 张卡 (cuda:0-5)  — Part 2 of 2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-handoff-research-reviewer-loop-10-task-context-1-gpu-6-cuda-0-5-copy-2.md) · [Structured JSON](../../../sessions/fb/fbb22ded3c85e286284b.json)

## Round 9

### Tool result

_source line 161 · 2026-05-15T15:12:17.962Z_

<details><summary>↩ Tool result · `toolu_01THqf1N9GyqQW9QcUgDtGAE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml\", \"content\": \"_next_id: 51\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:26 UTC\\n  summary: MVP 用 simulation identifiability test 验证 4PL+γ IRT 核心假设，放弃 EMNLP 2026 May\\n    ARR\\n  rationale: 核心假设是 γ 与 θ 可分离——这在合成数据上可验证，无需 GPU。12 天内完成完整论文不现实，目标改为 AAAI 2027 / ICLR\\n    2027。MVP 通过后再配置 GPU 进入 research 阶段。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:29 UTC\\n  summary: 采纳 Reviewer 3 个 warning：扩展 simulation grid + 加 θ-exposure confounding +\\n    加 FPR/FNR 噪声模型\\n  rationale: Reviewer 指出原 MVP simulation 条件过于理想化。θ-exposure confounding 是 γ identifiability\\n    的核心威胁，必须在 MVP 阶段覆盖。参数 grid 扩展（18 conditions）和 FPR/FNR 噪声增量成本约 4-8h CPU，不影响时间线。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 10:57 UTC\\n  summary: Phase A PASS：4PL+γ 在 N_items=300 下成功分离 γ 和 θ；θ_RMSE 阈值从 0.2 放宽至 0.30\\n  rationale: 'Variant A (N_items=300, 4PL NUTS): γ_rel_bias=6.8%, θ_corr=0.943, 收敛完美。N_items=100\\n    的 borderline fail 确认为信息量不足（c/d 参数估计需要更多 items），非方法论缺陷。θ_RMSE 阈值从 0.2 放宽至 0.30，Reviewer\\n    论证理论最优 SE≈0.18-0.26，0.2 在 N=50 models 下不可达。ADVI 在 4PL 上彻底失败（bad local mode），MVP\\n    阶段放弃 ADVI，仅用 NUTS。2PL+γ 在 4PL 生成数据上严重 misspecified（γ=0.16），确认 4PL 的必要性。'\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: primary\\n    result: Phase A PASS (Variant A)\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-13 15:45 UTC\\n  summary: MVP 通过，进入 Research 阶段\\n  rationale: Phase A (identifiability) 和 P2 (confounding robustness) 两个 gate 全部 PASS。4PL+γ\\n    NUTS 在 N_items=300 条件下 γ 相对偏差 <8%，θ 相关性 >0.94，混淆分离后残差相关 0.058。ADVI 和 2PL 被排除。核心假设\\\"IRT\\n    模型可分离污染效应与真实能力\\\"在合成数据上得到验证。\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: Phase A identifiability\\n    result: PASS at N_items=300\\n  - exp_id: mvp_sim_confounding\\n    role: P2 confounding robustness\\n    result: PASS with confound_corr=0.38\\n  depends_on:\\n  - D002\\n  - D003\\n- id: D005\\n  date: 2026-05-13 17:11 UTC\\n  summary: Dream 审稿分析：best=5/10, median=5/10, worst=4/10。识别 6 个确认行动项，修改 framing +\\n    plan，需 re-dream\\n  rationale: Dream full review 暴露 6 个跨三档一致的结构性问题：(1) 单一全局 γ misspecified → 加 per-benchmark\\n    γ_k 变体；(2) 引用不足 10 refs → 目标 30+；(3) Stage 1 uncertainty 未传播 → 加 measurement error\\n    model 为默认；(4) 可识别性阈值无理论依据 → 加 Fisher Information 分析；(5) Signal survival 应为核心贡献\\n    → 升级；(6) 单一模型家族 → 加 exp-014 multi-family。DCR baseline 此前已修复。RL regret ground truth\\n    明确为 held-out clean benchmark。Local independence 加显式讨论。方向正确但执行需加强，不降 venue。\\n  related_experiments:\\n  - exp_id: dream_20260513T155040\\n    role: Dream simulation\\n    result: best=5/10, median=5/10, worst=4/10\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 17:14 UTC\\n  summary: 投稿目标改回 EMNLP 2026 ARR May 25（撤销 D001），12 天冲刺\\n  rationale: 用户明确指令：改回 EMNLP 2026 ARR May 25，承诺提供充足资源，不担心 DDL。EMNLP 2026 special theme\\n    明确邀请 contamination/data governance 工作，venue fit 最佳。12 天冲刺计划：4+ GPU 并行 SFT injection，AI\\n    团队 24/7，Day-8 contingency 保底。P2 实验和 exp-014 (multi-family) 推迟到 camera-ready 或\\n    rebuttal。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n  - D005\\n- id: D007\\n  date: 2026-05-13 17:23 UTC\\n  summary: Re-dream gate 从阻塞改为 advisory：D2 结果不再阻塞 P0 实验启动，改为 advisory 参考\\n  rationale: D006 确立 12 天冲刺后，re-dream 等待时间（~25min）虽短但 GPU 到位后不应因 dream 结果阻塞实验启动。Dream\\n    D2 结果仍会分析并据此调整 framing/plan，但不作为 P0 实验的 hard gate。准备工作（代码/数据/环境）立即并行推进。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-13 18:45 UTC\\n  summary: Dream D2 分析：best=4/10, median=5/10, worst=4/10。Best 降分因 imagined data 质量问题（非结构性）。6\\n    个跨档结构性行动项已确认并持久化。Per D007 advisory gate, 继续推进实验。\\n  rationale: D2 三档评分：best=4(R1 因 imagined data suspicious patterns 给 3/10), median=5,\\n    worst=4。结构改进被审稿认可（per-benchmark γ_k, ME model, signal survival）。跨档一致的结构性问题：(1)\\n    Fisher Information 推导缺失 [B][M][W], (2) DIF 文献缺失 [B][M][W], (3) 零图表 [B], (4) ML\\n    calibration 歧义 [M][W], (5) Conformal prediction 未讨论 [M][W], (6) 因果推断类比未形式化 [B][M][W]。数据依赖问题（coverage\\n    gap, significance, RRF vs single signal）留待真实实验验证。Best 降分主要因 R1 对 imagined data\\n    的 \\\"suspicious patterns\\\" 严厉打分——真实实验数据不会有此问题。Per D007 advisory gate, 不阻塞实验。\\n  related_experiments:\\n  - exp_id: dream_20260513T171200\\n    role: re-dream validation\\n    result: best=4/10 median=5/10 worst=4/10\\n  depends_on:\\n  - D005\\n  - D007\\n- id: D009\\n  date: 2026-05-13 19:15 UTC\\n  summary: HumanEval demoted to appendix case study; main experiments use MMLU/GSM8K/ARC-Challenge\\n  rationale: HumanEval paraphrase QC pass rate only 16% (26/164) with Qwen2.5-7B-Instruct\\n    — code paraphrasing is fundamentally harder than text/math paraphrasing. N=164\\n    already flagged as potential 4PL estimation limitation in paper_framing.md. Dream\\n    median/worst reviews both identified HumanEval convergence issues (ESS=85, R̂=1.12).\\n    Keeping 3 strong benchmarks (MMLU 14K, GSM8K 1.3K, ARC-C) with high QC pass rates\\n    provides robust validation. HumanEval results reported in appendix with paraphrase\\n    quality caveat.\\n  related_experiments:\\n  - exp_id: exp_001_sft_injection\\n    role: paraphrase generation\\n    result: HumanEval 16% QC pass rate vs expected >80% for text benchmarks\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-13 20:12 UTC\\n  summary: Use all paraphrases for SFT injection regardless of QC; QC filtering only\\n    for ConStat signal\\n  rationale: 'QC pass rate (cosine>0.85 + BLEU<0.3) is systematically low across all\\n    benchmarks due to 7B model producing overly lexically similar paraphrases. Two\\n    distinct use cases: (1) SFT contamination injection — high-BLEU paraphrases still\\n    contaminate the model effectively, QC irrelevant. (2) ConStat signal — needs divergent\\n    paraphrases, use QC-passed items only. In our controlled setup we KNOW which items\\n    are contaminated (ground truth labels), so n-gram decontamination evasion is motivation,\\n    not operational requirement. Re-running generation would cost ~2h on critical\\n    path — unacceptable in 12-day sprint. Report QC stats transparently in paper.'\\n  related_experiments:\\n  - exp_id: exp_001_sft_injection\\n    role: paraphrase generation\\n    result: BLEU>0.3 across benchmarks, QC pass rates expected 15-40%\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-14 00:45 UTC\\n  summary: Real-data IRT pipeline 改用 CmdStanPy Bayesian 推断，弃用 PyTorch MLE\\n  rationale: Reviewer CRITICAL：(1) MLE SE 计算失效（Hessian 对角线接近零，49/50 items 回退到上限值）；(2)\\n    MLE γ 恢复退化（corr=0.629 vs Stan ~0.94）；(3) 论文 framing 为 Bayesian Calibration，方法论必须与模拟验证一致。复用\\n    mvp_sim 已验证的 Stan 模型文件，posterior SD 自然提供 SE。\\n  related_experiments:\\n  - exp_id: exp_006\\n    role: trigger\\n    result: PyTorch MLE gamma_corr=0.629, SE全部失效\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: reference\\n    result: Stan NUTS theta_corr~0.94, gamma bias<8%\\n  depends_on: []\\n- id: D012\\n  date: 2026-05-14 00:55 UTC\\n  summary: d100_qc_only ablation 列为 P1：noisy vs clean contamination confound 需隔离，但不阻塞\\n    Phase 3 主矩阵\\n  rationale: Reviewer 指出 d100 使用全部 paraphrase（含 QC fail，GSM8K QC 仅 17.3%）导致 noisy\\n    contamination confound——若 d100 calibration error 不显著高于 d000，无法区分\\\"污染无影响\\\"vs\\\"噪声稀释信号\\\"。解决方案：(1)\\n    当前 d100 frame 为 conservative/realistic test（真实污染也有噪声）；(2) 补 d100_qc_only（仅 QC\\n    pass 样本）作为 P1 ablation，seed=0 主矩阵完成后启动。不阻塞当前 Phase 3。\\n  related_experiments:\\n  - exp_id: exp_001_sft_d100_05B\\n    role: trigger\\n    result: success, but noisy contamination confound identified\\n  depends_on: []\\n- id: D013\\n  date: 2026-05-14 01:19 UTC\\n  summary: 正式实验使用 Simple IRT model，弃用 Analytic ME model\\n  rationale: 诊断实验表明 Analytic ME 模型不仅未改善 γ 偏差，反而加剧（59.2% vs Simple 的 57.5%，N=30, σ_e=0.1）。ME\\n    模型理论上更优但在有限样本下无法胜过 simple model。exp-006 及后续正式实验统一使用 simple model。\\n  related_experiments:\\n  - exp_id: exp_005_diag_nmodels50\\n    role: evidence\\n    result: N=50 simple model γ bias +23.6%, CI covers true value\\n  - exp_id: exp_005_diag_analytic_me\\n    role: evidence\\n    result: ME model γ bias +59.2%, worse than simple model\\n  depends_on: []\\n- id: D014\\n  date: 2026-05-14 01:19 UTC\\n  summary: C1 claim 需加条件限定：γ recovery 依赖 N≥50 且 σ_e≥0.3；论文需含 bias characterization\\n    section\\n  rationale: 诊断实验显示 N=30/σ_e=0.1 时 γ 正偏差达 57.5%，N=50 仍有 23.6%。Phase 3 预计 N~30-45 处于\\n    bias 敏感区。论文必须：(1) C1 加条件限定，(2) 加 simulation calibration section 披露 bias 特性（透明度对审稿人加分），(3)\\n    优先报 interval estimates。最终 N vs bias 曲线待 exp-004 sweep 确认。\\n  related_experiments:\\n  - exp_id: exp_005_diag_nmodels50\\n    role: evidence\\n    result: N=50 bias +23.6%, σ_e=0.1\\n  - exp_id: exp_005_noise_prop_v2\\n    role: evidence\\n    result: N=30 bias +57.5%, σ_e=0.1\\n  - exp_id: exp_005_diag_nmodels50\\n    role: evidence\\n    result: N=30 σ_e=0.3 bias only -8.4%, well-calibrated\\n  depends_on: []\\n- id: D015\\n  date: 2026-05-14 04:11 UTC\\n  summary: C2 \\\"cliff-like\\\" claim 需条件限定：无 RL 中间 checkpoint 时降级为 \\\"significant degradation\\\"；exp-008\\n    代码扩展为 N-regime 支持\\n  rationale: Reviewer 审查 exp-008 代码发现：当前只支持 SFT vs RL 两个 regime pairwise 对比，2 个数据点无法区分\\n    cliff 和 gradual 退化形状。paper_framing.md Figure 2 要求 4 regime heatmap（base/SFT-clean/SFT-contaminated/RL）。决定：(1)\\n    代码扩展为 N-regime 矩阵输出；(2) 若提交时无 RL 中间 checkpoint 数据，claim 措辞从 \\\"cliff-like, not gradual\\\"\\n    降级为 \\\"significant degradation under RL\\\"。\\n  related_experiments:\\n  - exp_id: exp-008\\n    role: signal survival analysis\\n    result: code pass with warning\\n  depends_on: []\\n- id: D016\\n  date: 2026-05-14 06:31 UTC\\n  summary: Min-K++ 参考模型使用 0% dosage fine-tuned model（非裸基座），隔离污染效应\\n  rationale: Min-K++ delta = target - reference 的 log-likelihood 差。若 reference = 裸基座，delta\\n    混入 fine-tuning 效应 + 污染效应，无法隔离。用 0% dosage model 作 reference，delta 仅反映污染注入的记忆化效应，与论文\\n    story（精确量化污染程度）一致。代码注释 `e.g., 0% dosage` 也暗示此意图。\\n  related_experiments:\\n  - exp_id: exp_002_signal_pipeline\\n    role: affected\\n    result: 需新增 --ref-adapter-path 参数\\n  depends_on: []\\n- id: D017\\n  date: 2026-05-14 07:07 UTC\\n  summary: MC 评估改用 \\\"The answer is\\\" 前缀（方案 C），不重训模型\\n  rationale: SFT 训练格式 \\\"The answer is X\\\" 与评估的 \\\"Answer:\\\" 前缀不匹配，导致 logprob 退化为 token\\n    先验。方案 A（改训练格式）需重训全部模型，DDL 前不可行。方案 B（改生成式）失去 per-item logprob 细粒度，影响 IRT 分析。方案\\n    C（评估 prompt 加 \\\"The answer is\\\" 前缀）最小侵入：不需重训、保留 logprob 评估、d000 模型也有 5674 条同格式训练数据所以不会退化。需先在\\n    d000 上验证方案 C 不引入负面效应。\\n  related_experiments:\\n  - exp_id: exp_001_eval_05B_d005\\n    role: evidence\\n    result: MMLU=0.293 A-collapse, 证实格式冲突\\n  - exp_id: exp_001_eval_05B_d000_s42_v5\\n    role: baseline\\n    result: MMLU=0.418, 同格式但无污染语义相似性\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-14 09:57 UTC\\n  summary: 3B GSM8K 崩塌归因为 LoRA SFT CoT 遗忘，排除出 dose-response 分析，作为发现报告\\n  rationale: 3B raw GSM8K=60.5%，d000 SFT 后=11.7%（-48.8pp），两个 seed 一致，排除格式/提取问题。根因是\\n    LoRA r=16/alpha=32 对 3B 的 CoT 推理过于激进。修复需~20h GPU 重训+eval，DDL 紧张且可能引入新问题。3B MC\\n    benchmarks（MMLU=0.634, ARC=0.822）不受影响，保留在 dose-response 中。论文 claim 调整为\\\"3 model\\n    sizes on MC, 2 sizes (0.5B/1.5B) on generative\\\"，Discussion 讨论 SFT 对 CoT 的 scale-dependent\\n    side effect。\\n  related_experiments:\\n  - exp_id: exp_001_eval_3B_d000_s42\\n    role: evidence\\n    result: GSM8K=0.117, 确认 SFT 后 CoT 崩塌\\n  - exp_id: exp_001_eval_3B_raw_gen\\n    role: evidence\\n    result: GSM8K=0.605, 确认 base model 正常\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-14 15:21 UTC\\n  summary: 'd005 position bias confound: contamination SFT 将 \\\"选A\\\" 比例从 40% 推高到 55%，需\\n    position-debiased analysis'\\n  rationale: Reviewer 发现 d005 (5% dosage, noisy QC-fail paraphrases) 模型退化为\\\"大多选A\\\"。contamination\\n    gap (orig-para accuracy) 被 degeneracy noise 污染，不能直接作为 contamination signal 证据。需要：(1)\\n    在 contamination gap 计算前做 position-debiased accuracy；(2) 检查 d100 是否有同样问题；(3) 论文中标注\\n    d005 含 QC-fail paraphrases。不重训 d005——d005 是次要剂量点，core result 基于 d000 vs d100。\\n  related_experiments:\\n  - exp_id: exp_001_eval_05B_aligned_batch\\n    role: evidence\\n    result: d005 pred=A 55.7% vs d000 40.4%\\n  - exp_id: exp_001_sft_d005_05B_v3\\n    role: cause\\n    result: noisy SFT with QC-fail paraphrases (D010)\\n  depends_on:\\n  - D010\\n  - D017\\n- id: D020\\n  date: 2026-05-14 16:10 UTC\\n  summary: 重训 3B d000：降低 LoRA lr 到 5e-5、alpha 到 16，修复 SFT 导致的 CoT 崩塌\\n  rationale: 3B d000 GSM8K 12% 确认为 LoRA 超参过激（lr=2e-4, r=16, alpha=32, 全7模块）导致 CoT\\n    能力灾难性遗忘。d100-d000=57.7pp 是 artifact，真实 contamination signal ~9pp（raw 60.5 → d100\\n    69.7）。重训成本 ~8h GPU，但能补全 \\n\\n... [截断: 省略 26737 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 38737, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bae0d6ae-6e99-4823-8f4d-3738be5aaa04",
  "isSidechain": false,
  "promptId": "29973f98-8d7d-4a5e-ba55-2e3eddf46b62",
  "type": "user",
  "uuid": "007ae959-3cb6-45e0-a7c7-27ac69ae8b35",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml\\\", \\\"content\\\": \\\"_next_id: 51\\\\ndecisions:\\\\n- id: D001\\\\n  date: 2026-05-13 04:26 UTC\\\\n  summary: MVP 用 simulation identifiability test 验证 4PL+γ IRT 核心假设，放弃 EMNLP 2026 May\\\\n    ARR\\\\n  rationale: 核心假设是 γ 与 θ 可分离——这在合成数据上可验证，无需 GPU。12 天内完成完整论文不现实，目标改为 AAAI 2027 / ICLR\\\\n    2027。MVP 通过后再配置 GPU 进入 research 阶段。\\\\n  related_experiments: []\\\\n  depends_on: []\\\\n- id: D002\\\\n  date: 2026-05-13 04:29 UTC\\\\n  summary: 采纳 Reviewer 3 个 warning：扩展 simulation grid + 加 θ-exposure confounding +\\\\n    加 FPR/FNR 噪声模型\\\\n  rationale: Reviewer 指出原 MVP simulation 条件过于理想化。θ-exposure confounding 是 γ identifiability\\\\n    的核心威胁，必须在 MVP 阶段覆盖。参数 grid 扩展（18 conditions）和 FPR/FNR 噪声增量成本约 4-8h CPU，不影响时间线。\\\\n  related_experiments: []\\\\n  depends_on:\\\\n  - D001\\\\n- id: D003\\\\n  date: 2026-05-13 10:57 UTC\\\\n  summary: Phase A PASS：4PL+γ 在 N_items=300 下成功分离 γ 和 θ；θ_RMSE 阈值从 0.2 放宽至 0.30\\\\n  rationale: 'Variant A (N_items=300, 4PL NUTS): γ_rel_bias=6.8%, θ_corr=0.943, 收敛完美。N_items=100\\\\n    的 borderline fail 确认为信息量不足（c/d 参数估计需要更多 items），非方法论缺陷。θ_RMSE 阈值从 0.2 放宽至 0.30，Reviewer\\\\n    论证理论最优 SE≈0.18-0.26，0.2 在 N=50 models 下不可达。ADVI 在 4PL 上彻底失败（bad local mode），MVP\\\\n    阶段放弃 ADVI，仅用 NUTS。2PL+γ 在 4PL 生成数据上严重 misspecified（γ=0.16），确认 4PL 的必要性。'\\\\n  related_experiments:\\\\n  - exp_id: mvp_sim_4pl_gamma\\\\n    role: primary\\\\n    result: Phase A PASS (Variant A)\\\\n  depends_on:\\\\n  - D001\\\\n  - D002\\\\n- id: D004\\\\n  date: 2026-05-13 15:45 UTC\\\\n  summary: MVP 通过，进入 Research 阶段\\\\n  rationale: Phase A (identifiability) 和 P2 (confounding robustness) 两个 gate 全部 PASS。4PL+γ\\\\n    NUTS 在 N_items=300 条件下 γ 相对偏差 <8%，θ 相关性 >0.94，混淆分离后残差相关 0.058。ADVI 和 2PL 被排除。核心假设\\\\\\\"IRT\\\\n    模型可分离污染效应与真实能力\\\\\\\"在合成数据上得到验证。\\\\n  related_experiments:\\\\n  - exp_id: mvp_sim_4pl_gamma\\\\n    role: Phase A identifiability\\\\n    result: PASS at N_items=300\\\\n  - exp_id: mvp_sim_confounding\\\\n    role: P2 confounding robustness\\\\n    result: PASS with confound_corr=0.38\\\\n  depends_on:\\\\n  - D002\\\\n  - D003\\\\n- id: D005\\\\n  date: 2026-05-13 17:11 UTC\\\\n  summary: Dream 审稿分析：best=5/10, median=5/10, worst=4/10。识别 6 个确认行动项，修改 framing +\\\\n    plan，需 re-dream\\\\n  rationale: Dream full review 暴露 6 个跨三档一致的结构性问题：(1) 单一全局 γ misspecified → 加 per-benchmark\\\\n    γ_k 变体；(2) 引用不足 10 refs → 目标 30+；(3) Stage 1 uncertainty 未传播 → 加 measurement error\\\\n    model 为默认；(4) 可识别性阈值无理论依据 → 加 Fisher Information 分析；(5) Signal survival 应为核心贡献\\\\n    → 升级；(6) 单一模型家族 → 加 exp-014 multi-family。DCR baseline 此前已修复。RL regret ground truth\\\\n    明确为 held-out clean benchmark。Local independence 加显式讨论。方向正确但执行需加强，不降 venue。\\\\n  related_experiments:\\\\n  - exp_id: dream_20260513T155040\\\\n    role: Dream simulation\\\\n    result: best=5/10, median=5/10, worst=4/10\\\\n  depends_on:\\\\n  - D004\\\\n- id: D006\\\\n  date: 2026-05-13 17:14 UTC\\\\n  summary: 投稿目标改回 EMNLP 2026 ARR May 25（撤销 D001），12 天冲刺\\\\n  rationale: 用户明确指令：改回 EMNLP 2026 ARR May 25，承诺提供充足资源，不担心 DDL。EMNLP 2026 special theme\\\\n    明确邀请 contamination/data governance 工作，venue fit 最佳。12 天冲刺计划：4+ GPU 并行 SFT injection，AI\\\\n    团队 24/7，Day-8 contingency 保底。P2 实验和 exp-014 (multi-family) 推迟到 camera-ready 或\\\\n    rebuttal。\\\\n  related_experiments: []\\\\n  depends_on:\\\\n  - D001\\\\n  - D005\\\\n- id: D007\\\\n  date: 2026-05-13 17:23 UTC\\\\n  summary: Re-dream gate 从阻塞改为 advisory：D2 结果不再阻塞 P0 实验启动，改为 advisory 参考\\\\n  rationale: D006 确立 12 天冲刺后，re-dream 等待时间（~25min）虽短但 GPU 到位后不应因 dream 结果阻塞实验启动。Dream\\\\n    D2 结果仍会分析并据此调整 framing/plan，但不作为 P0 实验的 hard gate。准备工作（代码/数据/环境）立即并行推进。\\\\n  related_experiments: []\\\\n  depends_on:\\\\n  - D006\\\\n- id: D008\\\\n  date: 2026-05-13 18:45 UTC\\\\n  summary: Dream D2 分析：best=4/10, median=5/10, worst=4/10。Best 降分因 imagined data 质量问题（非结构性）。6\\\\n    个跨档结构性行动项已确认并持久化。Per D007 advisory gate, 继续推进实验。\\\\n  rationale: D2 三档评分：best=4(R1 因 imagined data suspicious patterns 给 3/10), median=5,\\\\n    worst=4。结构改进被审稿认可（per-benchmark γ_k, ME model, signal survival）。跨档一致的结构性问题：(1)\\\\n    Fisher Information 推导缺失 [B][M][W], (2) DIF 文献缺失 [B][M][W], (3) 零图表 [B], (4) ML\\\\n    calibration 歧义 [M][W], (5) Conformal prediction 未讨论 [M][W], (6) 因果推断类比未形式化 [B][M][W]。数据依赖问题（coverage\\\\n    gap, significance, RRF vs single signal）留待真实实验验证。Best 降分主要因 R1 对 imagined data\\\\n    的 \\\\\\\"suspicious patterns\\\\\\\" 严厉打分——真实实验数据不会有此问题。Per D007 advisory gate, 不阻塞实验。\\\\n  related_experiments:\\\\n  - exp_id: dream_20260513T171200\\\\n    role: re-dream validation\\\\n    result: best=4/10 median=5/10 worst=4/10\\\\n  depends_on:\\\\n  - D005\\\\n  - D007\\\\n- id: D009\\\\n  date: 2026-05-13 19:15 UTC\\\\n  summary: HumanEval demoted to appendix case study; main experiments use MMLU/GSM8K/ARC-Challenge\\\\n  rationale: HumanEval paraphrase QC pass rate only 16% (26/164) with Qwen2.5-7B-Instruct\\\\n    — code paraphrasing is fundamentally harder than text/math paraphrasing. N=164\\\\n    already flagged as potential 4PL estimation limitation in paper_framing.md. Dream\\\\n    median/worst reviews both identified HumanEval convergence issues (ESS=85, R̂=1.12).\\\\n    Keeping 3 strong benchmarks (MMLU 14K, GSM8K 1.3K, ARC-C) with high QC pass rates\\\\n    provides robust validation. HumanEval results reported in appendix with paraphrase\\\\n    quality caveat.\\\\n  related_experiments:\\\\n  - exp_id: exp_001_sft_injection\\\\n    role: paraphrase generation\\\\n    result: HumanEval 16% QC pass rate vs expected >80% for text benchmarks\\\\n  depends_on: []\\\\n- id: D010\\\\n  date: 2026-05-13 20:12 UTC\\\\n  summary: Use all paraphrases for SFT injection regardless of QC; QC filtering only\\\\n    for ConStat signal\\\\n  rationale: 'QC pass rate (cosine>0.85 + BLEU<0.3) is systematically low across all\\\\n    benchmarks due to 7B model producing overly lexically similar paraphrases. Two\\\\n    distinct use cases: (1) SFT contamination injection — high-BLEU paraphrases still\\\\n    contaminate the model effectively, QC irrelevant. (2) ConStat signal — needs divergent\\\\n    paraphrases, use QC-passed items only. In our controlled setup we KNOW which items\\\\n    are contaminated (ground truth labels), so n-gram decontamination evasion is motivation,\\\\n    not operational requirement. Re-running generation would cost ~2h on critical\\\\n    path — unacceptable in 12-day sprint. Report QC stats transparently in paper.'\\\\n  related_experiments:\\\\n  - exp_id: exp_001_sft_injection\\\\n    role: paraphrase generation\\\\n    result: BLEU>0.3 across benchmarks, QC pass rates expected 15-40%\\\\n  depends_on:\\\\n  - D009\\\\n- id: D011\\\\n  date: 2026-05-14 00:45 UTC\\\\n  summary: Real-data IRT pipeline 改用 CmdStanPy Bayesian 推断，弃用 PyTorch MLE\\\\n  rationale: Reviewer CRITICAL：(1) MLE SE 计算失效（Hessian 对角线接近零，49/50 items 回退到上限值）；(2)\\\\n    MLE γ 恢复退化（corr=0.629 vs Stan ~0.94）；(3) 论文 framing 为 Bayesian Calibration，方法论必须与模拟验证一致。复用\\\\n    mvp_sim 已验证的 Stan 模型文件，posterior SD 自然提供 SE。\\\\n  related_experiments:\\\\n  - exp_id: exp_006\\\\n    role: trigger\\\\n    result: PyTorch MLE gamma_corr=0.629, SE全部失效\\\\n  - exp_id: mvp_sim_4pl_gamma\\\\n    role: reference\\\\n    result: Stan NUTS theta_corr~0.94, gamma bias<8%\\\\n  depends_on: []\\\\n- id: D012\\\\n  date: 2026-05-14 00:55 UTC\\\\n  summary: d100_qc_only ablation 列为 P1：noisy vs clean contamination confound 需隔离，但不阻塞\\\\n    Phase 3 主矩阵\\\\n  rationale: Reviewer 指出 d100 使用全部 paraphrase（含 QC fail，GSM8K QC 仅 17.3%）导致 noisy\\\\n    contamination confound——若 d100 calibration error 不显著高于 d000，无法区分\\\\\\\"污染无影响\\\\\\\"vs\\\\\\\"噪声稀释信号\\\\\\\"。解决方案：(1)\\\\n    当前 d100 frame 为 conservative/realistic test（真实污染也有噪声）；(2) 补 d100_qc_only（仅 QC\\\\n    pass 样本）作为 P1 ablation，seed=0 主矩阵完成后启动。不阻塞当前 Phase 3。\\\\n  related_experiments:\\\\n  - exp_id: exp_001_sft_d100_05B\\\\n    role: trigger\\\\n    result: success, but noisy contamination confound identified\\\\n  depends_on: []\\\\n- id: D013\\\\n  date: 2026-05-14 01:19 UTC\\\\n  summary: 正式实验使用 Simple IRT model，弃用 Analytic ME model\\\\n  rationale: 诊断实验表明 Analytic ME 模型不仅未改善 γ 偏差，反而加剧（59.2% vs Simple 的 57.5%，N=30, σ_e=0.1）。ME\\\\n    模型理论上更优但在有限样本下无法胜过 simple model。exp-006 及后续正式实验统一使用 simple model。\\\\n  related_experiments:\\\\n  - exp_id: exp_005_diag_nmodels50\\\\n    role: evidence\\\\n    result: N=50 simple model γ bias +23.6%, CI covers true value\\\\n  - exp_id: exp_005_diag_analytic_me\\\\n    role: evidence\\\\n    result: ME model γ bias +59.2%, worse than simple model\\\\n  depends_on: []\\\\n- id: D014\\\\n  date: 2026-05-14 01:19 UTC\\\\n  summary: C1 claim 需加条件限定：γ recovery 依赖 N≥50 且 σ_e≥0.3；论文需含 bias characterization\\\\n    section\\\\n  rationale: 诊断实验显示 N=30/σ_e=0.1 时 γ 正偏差达 57.5%，N=50 仍有 23.6%。Phase 3 预计 N~30-45 处于\\\\n    bias 敏感区。论文必须：(1) C1 加条件限定，(2) 加 simulation calibration section 披露 bias 特性（透明度对审稿人加分），(3)\\\\n    优先报 interval estimates。最终 N vs bias 曲线待 exp-004 sweep 确认。\\\\n  related_experiments:\\\\n  - exp_id: exp_005_diag_nmodels50\\\\n    role: evidence\\\\n    result: N=50 bias +23.6%, σ_e=0.1\\\\n  - exp_id: exp_005_noise_prop_v2\\\\n    role: evidence\\\\n    result: N=30 bias +57.5%, σ_e=0.1\\\\n  - exp_id: exp_005_diag_nmodels50\\\\n    role: evidence\\\\n    result: N=30 σ_e=0.3 bias only -8.4%, well-calibrated\\\\n  depends_on: []\\\\n- id: D015\\\\n  date: 2026-05-14 04:11 UTC\\\\n  summary: C2 \\\\\\\"cliff-like\\\\\\\" claim 需条件限定：无 RL 中间 checkpoint 时降级为 \\\\\\\"significant degradation\\\\\\\"；exp-008\\\\n    代码扩展为 N-regime 支持\\\\n  rationale: Reviewer 审查 exp-008 代码发现：当前只支持 SFT vs RL 两个 regime pairwise 对比，2 个数据点无法区分\\\\n    cliff 和 gradual 退化形状。paper_framing.md Figure 2 要求 4 regime heatmap（base/SFT-clean/SFT-contaminated/RL）。决定：(1)\\\\n    代码扩展为 N-regime 矩阵输出；(2) 若提交时无 RL 中间 checkpoint 数据，claim 措辞从 \\\\\\\"cliff-like, not gradual\\\\\\\"\\\\n    降级为 \\\\\\\"significant degradation under RL\\\\\\\"。\\\\n  related_experiments:\\\\n  - exp_id: exp-008\\\\n    role: signal survival analysis\\\\n    result: code pass with warning\\\\n  depends_on: []\\\\n- id: D016\\\\n  date: 2026-05-14 06:31 UTC\\\\n  summary: Min-K++ 参考模型使用 0% dosage fine-tuned model（非裸基座），隔离污染效应\\\\n  rationale: Min-K++ delta = target - reference 的 log-likelihood 差。若 reference = 裸基座，delta\\\\n    混入 fine-tuning 效应 + 污染效应，无法隔离。用 0% dosage model 作 reference，delta 仅反映污染注入的记忆化效应，与论文\\\\n    story（精确量化污染程度）一致。代码注释 `e.g., 0% dosage` 也暗示此意图。\\\\n  related_experiments:\\\\n  - exp_id: exp_002_signal_pipeline\\\\n    role: affected\\\\n    result: 需新增 --ref-adapter-path 参数\\\\n  depends_on: []\\\\n- id: D017\\\\n  date: 2026-05-14 07:07 UTC\\\\n  summary: MC 评估改用 \\\\\\\"The answer is\\\\\\\" 前缀（方案 C），不重训模型\\\\n  rationale: SFT 训练格式 \\\\\\\"The answer is X\\\\\\\" 与评估的 \\\\\\\"Answer:\\\\\\\" 前缀不匹配，导致 logprob 退化为 token\\\\n    先验。方案 A（改训练格式）需重训全部模型，DDL 前不可行。方案 B（改生成式）失去 per-item logprob 细粒度，影响 IRT 分析。方案\\\\n    C（评估 prompt 加 \\\\\\\"The answer is\\\\\\\" 前缀）最小侵入：不需重训、保留 logprob 评估、d000 模型也有 5674 条同格式训练数据所以不会退化。需先在\\\\n    d000 上验证方案 C 不引入负面效应。\\\\n  related_experiments:\\\\n  - exp_id: exp_001_eval_05B_d005\\\\n    role: evidence\\\\n    result: MMLU=0.293 A-collapse, 证实格式冲突\\\\n  - exp_id: exp_001_eval_05B_d000_s42_v5\\\\n    role: baseline\\\\n    result: MMLU=0.418, 同格式但无污染语义相似性\\\\n  depends_on:\\\\n  - D016\\\\n- id: D018\\\\n  date: 2026-05-14 09:57 UTC\\\\n  summary: 3B GSM8K 崩塌归因为 LoRA SFT CoT 遗忘，排除出 dose-response 分析，作为发现报告\\\\n  rationale: 3B raw GSM8K=60.5%，d000 SFT 后=11.7%（-48.8pp），两个 seed 一致，排除格式/提取问题。根因是\\\\n    LoRA r=16/alpha=32 对 3B 的 CoT 推理过于激进。修复需~20h GPU 重训+eval，DDL 紧张且可能引入新问题。3B MC\\\\n    benchmarks（MMLU=0.634, ARC=0.822）不受影响，保留在 dose-response 中。论文 claim 调整为\\\\\\\"3 model\\\\n    sizes on MC, 2 sizes (0.5B/1.5B) on generative\\\\\\\"，Discussion 讨论 SFT 对 CoT 的 scale-dependent\\\\n    side effect。\\\\n  related_experiments:\\\\n  - exp_id: exp_001_eval_3B_d000_s42\\\\n    role: evidence\\\\n    result: GSM8K=0.117, 确认 SFT 后 CoT 崩塌\\\\n  - exp_id: exp_001_eval_3B_raw_gen\\\\n    role: evidence\\\\n    result: GSM8K=0.605, 确认 base model 正常\\\\n  depends_on:\\\\n  - D017\\\\n- id: D019\\\\n  date: 2026-05-14 15:21 UTC\\\\n  summary: 'd005 position bias confound: contamination SFT 将 \\\\\\\"选A\\\\\\\" 比例从 40% 推高到 55%，需\\\\n    position-debiased analysis'\\\\n  rationale: Reviewer 发现 d005 (5% dosage, noisy QC-fail paraphrases) 模型退化为\\\\\\\"大多选A\\\\\\\"。contamination\\\\n    gap (orig-para accuracy) 被 degeneracy noise 污染，不能直接作为 contamination signal 证据。需要：(1)\\\\n    在 contamination gap 计算前做 position-debiased accuracy；(2) 检查 d100 是否有同样问题；(3) 论文中标注\\\\n    d005 含 QC-fail paraphrases。不重训 d005——d005 是次要剂量点，core result 基于 d000 vs d100。\\\\n  related_experiments:\\\\n  - exp_id: exp_001_eval_05B_aligned_batch\\\\n    role: evidence\\\\n    result: d005 pred=A 55.7% vs d000 40.4%\\\\n  - exp_id: exp_001_sft_d005_05B_v3\\\\n    role: cause\\\\n    result: noisy SFT with QC-fail paraphrases (D010)\\\\n  depends_on:\\\\n  - D010\\\\n  - D017\\\\n- id: D020\\\\n  date: 2026-05-14 16:10 UTC\\\\n  summary: 重训 3B d000：降低 LoRA lr 到 5e-5、alpha 到 16，修复 SFT 导致的 CoT 崩塌\\\\n  rationale: 3B d000 GSM8K 12% 确认为 LoRA 超参过激（lr=2e-4, r=16, alpha=32, 全7模块）导致 CoT\\\\n    能力灾难性遗忘。d100-d000=57.7pp 是 artifact，真实 contamination signal ~9pp（raw 60.5 → d100\\\\n    69.7）。重训成本 ~8h GPU，但能补全 \\\\n\\\\n... [截断: 省略 26737 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 38737, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml\", \"content\": \"_next_id: 51\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:26 UTC\\n  summary: MVP 用 simulation identifiability test 验证 4PL+γ IRT 核心假设，放弃 EMNLP 2026 May\\n    ARR\\n  rationale: 核心假设是 γ 与 θ 可分离——这在合成数据上可验证，无需 GPU。12 天内完成完整论文不现实，目标改为 AAAI 2027 / ICLR\\n    2027。MVP 通过后再配置 GPU 进入 research 阶段。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:29 UTC\\n  summary: 采纳 Reviewer 3 个 warning：扩展 simulation grid + 加 θ-exposure confounding +\\n    加 FPR/FNR 噪声模型\\n  rationale: Reviewer 指出原 MVP simulation 条件过于理想化。θ-exposure confounding 是 γ identifiability\\n    的核心威胁，必须在 MVP 阶段覆盖。参数 grid 扩展（18 conditions）和 FPR/FNR 噪声增量成本约 4-8h CPU，不影响时间线。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 10:57 UTC\\n  summary: Phase A PASS：4PL+γ 在 N_items=300 下成功分离 γ 和 θ；θ_RMSE 阈值从 0.2 放宽至 0.30\\n  rationale: 'Variant A (N_items=300, 4PL NUTS): γ_rel_bias=6.8%, θ_corr=0.943, 收敛完美。N_items=100\\n    的 borderline fail 确认为信息量不足（c/d 参数估计需要更多 items），非方法论缺陷。θ_RMSE 阈值从 0.2 放宽至 0.30，Reviewer\\n    论证理论最优 SE≈0.18-0.26，0.2 在 N=50 models 下不可达。ADVI 在 4PL 上彻底失败（bad local mode），MVP\\n    阶段放弃 ADVI，仅用 NUTS。2PL+γ 在 4PL 生成数据上严重 misspecified（γ=0.16），确认 4PL 的必要性。'\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: primary\\n    result: Phase A PASS (Variant A)\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-13 15:45 UTC\\n  summary: MVP 通过，进入 Research 阶段\\n  rationale: Phase A (identifiability) 和 P2 (confounding robustness) 两个 gate 全部 PASS。4PL+γ\\n    NUTS 在 N_items=300 条件下 γ 相对偏差 <8%，θ 相关性 >0.94，混淆分离后残差相关 0.058。ADVI 和 2PL 被排除。核心假设\\\"IRT\\n    模型可分离污染效应与真实能力\\\"在合成数据上得到验证。\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: Phase A identifiability\\n    result: PASS at N_items=300\\n  - exp_id: mvp_sim_confounding\\n    role: P2 confounding robustness\\n    result: PASS with confound_corr=0.38\\n  depends_on:\\n  - D002\\n  - D003\\n- id: D005\\n  date: 2026-05-13 17:11 UTC\\n  summary: Dream 审稿分析：best=5/10, median=5/10, worst=4/10。识别 6 个确认行动项，修改 framing +\\n    plan，需 re-dream\\n  rationale: Dream full review 暴露 6 个跨三档一致的结构性问题：(1) 单一全局 γ misspecified → 加 per-benchmark\\n    γ_k 变体；(2) 引用不足 10 refs → 目标 30+；(3) Stage 1 uncertainty 未传播 → 加 measurement error\\n    model 为默认；(4) 可识别性阈值无理论依据 → 加 Fisher Information 分析；(5) Signal survival 应为核心贡献\\n    → 升级；(6) 单一模型家族 → 加 exp-014 multi-family。DCR baseline 此前已修复。RL regret ground truth\\n    明确为 held-out clean benchmark。Local independence 加显式讨论。方向正确但执行需加强，不降 venue。\\n  related_experiments:\\n  - exp_id: dream_20260513T155040\\n    role: Dream simulation\\n    result: best=5/10, median=5/10, worst=4/10\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 17:14 UTC\\n  summary: 投稿目标改回 EMNLP 2026 ARR May 25（撤销 D001），12 天冲刺\\n  rationale: 用户明确指令：改回 EMNLP 2026 ARR May 25，承诺提供充足资源，不担心 DDL。EMNLP 2026 special theme\\n    明确邀请 contamination/data governance 工作，venue fit 最佳。12 天冲刺计划：4+ GPU 并行 SFT injection，AI\\n    团队 24/7，Day-8 contingency 保底。P2 实验和 exp-014 (multi-family) 推迟到 camera-ready 或\\n    rebuttal。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n  - D005\\n- id: D007\\n  date: 2026-05-13 17:23 UTC\\n  summary: Re-dream gate 从阻塞改为 advisory：D2 结果不再阻塞 P0 实验启动，改为 advisory 参考\\n  rationale: D006 确立 12 天冲刺后，re-dream 等待时间（~25min）虽短但 GPU 到位后不应因 dream 结果阻塞实验启动。Dream\\n    D2 结果仍会分析并据此调整 framing/plan，但不作为 P0 实验的 hard gate。准备工作（代码/数据/环境）立即并行推进。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-13 18:45 UTC\\n  summary: Dream D2 分析：best=4/10, median=5/10, worst=4/10。Best 降分因 imagined data 质量问题（非结构性）。6\\n    个跨档结构性行动项已确认并持久化。Per D007 advisory gate, 继续推进实验。\\n  rationale: D2 三档评分：best=4(R1 因 imagined data suspicious patterns 给 3/10), median=5,\\n    worst=4。结构改进被审稿认可（per-benchmark γ_k, ME model, signal survival）。跨档一致的结构性问题：(1)\\n    Fisher Information 推导缺失 [B][M][W], (2) DIF 文献缺失 [B][M][W], (3) 零图表 [B], (4) ML\\n    calibration 歧义 [M][W], (5) Conformal prediction 未讨论 [M][W], (6) 因果推断类比未形式化 [B][M][W]。数据依赖问题（coverage\\n    gap, significance, RRF vs single signal）留待真实实验验证。Best 降分主要因 R1 对 imagined data\\n    的 \\\"suspicious patterns\\\" 严厉打分——真实实验数据不会有此问题。Per D007 advisory gate, 不阻塞实验。\\n  related_experiments:\\n  - exp_id: dream_20260513T171200\\n    role: re-dream validation\\n    result: best=4/10 median=5/10 worst=4/10\\n  depends_on:\\n  - D005\\n  - D007\\n- id: D009\\n  date: 2026-05-13 19:15 UTC\\n  summary: HumanEval demoted to appendix case study; main experiments use MMLU/GSM8K/ARC-Challenge\\n  rationale: HumanEval paraphrase QC pass rate only 16% (26/164) with Qwen2.5-7B-Instruct\\n    — code paraphrasing is fundamentally harder than text/math paraphrasing. N=164\\n    already flagged as potential 4PL estimation limitation in paper_framing.md. Dream\\n    median/worst reviews both identified HumanEval convergence issues (ESS=85, R̂=1.12).\\n    Keeping 3 strong benchmarks (MMLU 14K, GSM8K 1.3K, ARC-C) with high QC pass rates\\n    provides robust validation. HumanEval results reported in appendix with paraphrase\\n    quality caveat.\\n  related_experiments:\\n  - exp_id: exp_001_sft_injection\\n    role: paraphrase generation\\n    result: HumanEval 16% QC pass rate vs expected >80% for text benchmarks\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-13 20:12 UTC\\n  summary: Use all paraphrases for SFT injection regardless of QC; QC filtering only\\n    for ConStat signal\\n  rationale: 'QC pass rate (cosine>0.85 + BLEU<0.3) is systematically low across all\\n    benchmarks due to 7B model producing overly lexically similar paraphrases. Two\\n    distinct use cases: (1) SFT contamination injection — high-BLEU paraphrases still\\n    contaminate the model effectively, QC irrelevant. (2) ConStat signal — needs divergent\\n    paraphrases, use QC-passed items only. In our controlled setup we KNOW which items\\n    are contaminated (ground truth labels), so n-gram decontamination evasion is motivation,\\n    not operational requirement. Re-running generation would cost ~2h on critical\\n    path — unacceptable in 12-day sprint. Report QC stats transparently in paper.'\\n  related_experiments:\\n  - exp_id: exp_001_sft_injection\\n    role: paraphrase generation\\n    result: BLEU>0.3 across benchmarks, QC pass rates expected 15-40%\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-14 00:45 UTC\\n  summary: Real-data IRT pipeline 改用 CmdStanPy Bayesian 推断，弃用 PyTorch MLE\\n  rationale: Reviewer CRITICAL：(1) MLE SE 计算失效（Hessian 对角线接近零，49/50 items 回退到上限值）；(2)\\n    MLE γ 恢复退化（corr=0.629 vs Stan ~0.94）；(3) 论文 framing 为 Bayesian Calibration，方法论必须与模拟验证一致。复用\\n    mvp_sim 已验证的 Stan 模型文件，posterior SD 自然提供 SE。\\n  related_experiments:\\n  - exp_id: exp_006\\n    role: trigger\\n    result: PyTorch MLE gamma_corr=0.629, SE全部失效\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: reference\\n    result: Stan NUTS theta_corr~0.94, gamma bias<8%\\n  depends_on: []\\n- id: D012\\n  date: 2026-05-14 00:55 UTC\\n  summary: d100_qc_only ablation 列为 P1：noisy vs clean contamination confound 需隔离，但不阻塞\\n    Phase 3 主矩阵\\n  rationale: Reviewer 指出 d100 使用全部 paraphrase（含 QC fail，GSM8K QC 仅 17.3%）导致 noisy\\n    contamination confound——若 d100 calibration error 不显著高于 d000，无法区分\\\"污染无影响\\\"vs\\\"噪声稀释信号\\\"。解决方案：(1)\\n    当前 d100 frame 为 conservative/realistic test（真实污染也有噪声）；(2) 补 d100_qc_only（仅 QC\\n    pass 样本）作为 P1 ablation，seed=0 主矩阵完成后启动。不阻塞当前 Phase 3。\\n  related_experiments:\\n  - exp_id: exp_001_sft_d100_05B\\n    role: trigger\\n    result: success, but noisy contamination confound identified\\n  depends_on: []\\n- id: D013\\n  date: 2026-05-14 01:19 UTC\\n  summary: 正式实验使用 Simple IRT model，弃用 Analytic ME model\\n  rationale: 诊断实验表明 Analytic ME 模型不仅未改善 γ 偏差，反而加剧（59.2% vs Simple 的 57.5%，N=30, σ_e=0.1）。ME\\n    模型理论上更优但在有限样本下无法胜过 simple model。exp-006 及后续正式实验统一使用 simple model。\\n  related_experiments:\\n  - exp_id: exp_005_diag_nmodels50\\n    role: evidence\\n    result: N=50 simple model γ bias +23.6%, CI covers true value\\n  - exp_id: exp_005_diag_analytic_me\\n    role: evidence\\n    result: ME model γ bias +59.2%, worse than simple model\\n  depends_on: []\\n- id: D014\\n  date: 2026-05-14 01:19 UTC\\n  summary: C1 claim 需加条件限定：γ recovery 依赖 N≥50 且 σ_e≥0.3；论文需含 bias characterization\\n    section\\n  rationale: 诊断实验显示 N=30/σ_e=0.1 时 γ 正偏差达 57.5%，N=50 仍有 23.6%。Phase 3 预计 N~30-45 处于\\n    bias 敏感区。论文必须：(1) C1 加条件限定，(2) 加 simulation calibration section 披露 bias 特性（透明度对审稿人加分），(3)\\n    优先报 interval estimates。最终 N vs bias 曲线待 exp-004 sweep 确认。\\n  related_experiments:\\n  - exp_id: exp_005_diag_nmodels50\\n    role: evidence\\n    result: N=50 bias +23.6%, σ_e=0.1\\n  - exp_id: exp_005_noise_prop_v2\\n    role: evidence\\n    result: N=30 bias +57.5%, σ_e=0.1\\n  - exp_id: exp_005_diag_nmodels50\\n    role: evidence\\n    result: N=30 σ_e=0.3 bias only -8.4%, well-calibrated\\n  depends_on: []\\n- id: D015\\n  date: 2026-05-14 04:11 UTC\\n  summary: C2 \\\"cliff-like\\\" claim 需条件限定：无 RL 中间 checkpoint 时降级为 \\\"significant degradation\\\"；exp-008\\n    代码扩展为 N-regime 支持\\n  rationale: Reviewer 审查 exp-008 代码发现：当前只支持 SFT vs RL 两个 regime pairwise 对比，2 个数据点无法区分\\n    cliff 和 gradual 退化形状。paper_framing.md Figure 2 要求 4 regime heatmap（base/SFT-clean/SFT-contaminated/RL）。决定：(1)\\n    代码扩展为 N-regime 矩阵输出；(2) 若提交时无 RL 中间 checkpoint 数据，claim 措辞从 \\\"cliff-like, not gradual\\\"\\n    降级为 \\\"significant degradation under RL\\\"。\\n  related_experiments:\\n  - exp_id: exp-008\\n    role: signal survival analysis\\n    result: code pass with warning\\n  depends_on: []\\n- id: D016\\n  date: 2026-05-14 06:31 UTC\\n  summary: Min-K++ 参考模型使用 0% dosage fine-tuned model（非裸基座），隔离污染效应\\n  rationale: Min-K++ delta = target - reference 的 log-likelihood 差。若 reference = 裸基座，delta\\n    混入 fine-tuning 效应 + 污染效应，无法隔离。用 0% dosage model 作 reference，delta 仅反映污染注入的记忆化效应，与论文\\n    story（精确量化污染程度）一致。代码注释 `e.g., 0% dosage` 也暗示此意图。\\n  related_experiments:\\n  - exp_id: exp_002_signal_pipeline\\n    role: affected\\n    result: 需新增 --ref-adapter-path 参数\\n  depends_on: []\\n- id: D017\\n  date: 2026-05-14 07:07 UTC\\n  summary: MC 评估改用 \\\"The answer is\\\" 前缀（方案 C），不重训模型\\n  rationale: SFT 训练格式 \\\"The answer is X\\\" 与评估的 \\\"Answer:\\\" 前缀不匹配，导致 logprob 退化为 token\\n    先验。方案 A（改训练格式）需重训全部模型，DDL 前不可行。方案 B（改生成式）失去 per-item logprob 细粒度，影响 IRT 分析。方案\\n    C（评估 prompt 加 \\\"The answer is\\\" 前缀）最小侵入：不需重训、保留 logprob 评估、d000 模型也有 5674 条同格式训练数据所以不会退化。需先在\\n    d000 上验证方案 C 不引入负面效应。\\n  related_experiments:\\n  - exp_id: exp_001_eval_05B_d005\\n    role: evidence\\n    result: MMLU=0.293 A-collapse, 证实格式冲突\\n  - exp_id: exp_001_eval_05B_d000_s42_v5\\n    role: baseline\\n    result: MMLU=0.418, 同格式但无污染语义相似性\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-14 09:57 UTC\\n  summary: 3B GSM8K 崩塌归因为 LoRA SFT CoT 遗忘，排除出 dose-response 分析，作为发现报告\\n  rationale: 3B raw GSM8K=60.5%，d000 SFT 后=11.7%（-48.8pp），两个 seed 一致，排除格式/提取问题。根因是\\n    LoRA r=16/alpha=32 对 3B 的 CoT 推理过于激进。修复需~20h GPU 重训+eval，DDL 紧张且可能引入新问题。3B MC\\n    benchmarks（MMLU=0.634, ARC=0.822）不受影响，保留在 dose-response 中。论文 claim 调整为\\\"3 model\\n    sizes on MC, 2 sizes (0.5B/1.5B) on generative\\\"，Discussion 讨论 SFT 对 CoT 的 scale-dependent\\n    side effect。\\n  related_experiments:\\n  - exp_id: exp_001_eval_3B_d000_s42\\n    role: evidence\\n    result: GSM8K=0.117, 确认 SFT 后 CoT 崩塌\\n  - exp_id: exp_001_eval_3B_raw_gen\\n    role: evidence\\n    result: GSM8K=0.605, 确认 base model 正常\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-14 15:21 UTC\\n  summary: 'd005 position bias confound: contamination SFT 将 \\\"选A\\\" 比例从 40% 推高到 55%，需\\n    position-debiased analysis'\\n  rationale: Reviewer 发现 d005 (5% dosage, noisy QC-fail paraphrases) 模型退化为\\\"大多选A\\\"。contamination\\n    gap (orig-para accuracy) 被 degeneracy noise 污染，不能直接作为 contamination signal 证据。需要：(1)\\n    在 contamination gap 计算前做 position-debiased accuracy；(2) 检查 d100 是否有同样问题；(3) 论文中标注\\n    d005 含 QC-fail paraphrases。不重训 d005——d005 是次要剂量点，core result 基于 d000 vs d100。\\n  related_experiments:\\n  - exp_id: exp_001_eval_05B_aligned_batch\\n    role: evidence\\n    result: d005 pred=A 55.7% vs d000 40.4%\\n  - exp_id: exp_001_sft_d005_05B_v3\\n    role: cause\\n    result: noisy SFT with QC-fail paraphrases (D010)\\n  depends_on:\\n  - D010\\n  - D017\\n- id: D020\\n  date: 2026-05-14 16:10 UTC\\n  summary: 重训 3B d000：降低 LoRA lr 到 5e-5、alpha 到 16，修复 SFT 导致的 CoT 崩塌\\n  rationale: 3B d000 GSM8K 12% 确认为 LoRA 超参过激（lr=2e-4, r=16, alpha=32, 全7模块）导致 CoT\\n    能力灾难性遗忘。d100-d000=57.7pp 是 artifact，真实 contamination signal ~9pp（raw 60.5 → d100\\n    69.7）。重训成本 ~8h GPU，但能补全 \\n\\n... [截断: 省略 26737 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 38737, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "bae0d6ae-6e99-4823-8f4d-3738be5aaa04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/reviewer_e442a828",
  "sessionId": "0765c104-2abd-42e2-87bc-cff39e71bd8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 162_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_investigate_alpha-verify_20260515T151011]: Worker worker_investigate_alpha-verify_20260515T151011 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "007ae959-3cb6-45e0-a7c7-27ac69ae8b35",
  "sessionId": "0765c104-2abd-42e2-87bc-cff39e71bd8e"
}
```

---


### Runtime record

_source line 163_

```json
{
  "type": "ai-title",
  "aiTitle": "Review contamination calibration IRT results",
  "sessionId": "0765c104-2abd-42e2-87bc-cff39e71bd8e"
}
```

---


### Assistant

_source line 164 · 2026-05-15T15:12:26.267Z_

<details><summary>Logged reasoning block</summary>

```text
The decisions file is still getting truncated at the same point (after D020). I need to see the latest decisions. Let me read the file directly to get the end portion with recent decisions (D048-D050).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "007ae959-3cb6-45e0-a7c7-27ac69ae8b35",
  "isSidechain": false,
  "requestId": "req_011Cb4a1qT9FHyewS8otnG6H",
  "type": "assistant",
  "uuid": "b0fdb07d-6fcb-4bba-80d4-9965db1c71df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/reviewer_e442a828",
  "sessionId": "0765c104-2abd-42e2-87bc-cff39e71bd8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmzoyKVHbjLM5bLxAEasGU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6948,
      "cache_read_input_tokens": 132082,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6948,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 132082,
          "cache_creation_input_tokens": 6948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6948
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

_source line 165 · 2026-05-15T15:12:27.897Z_

<details open><summary>🔧 Tool call — Read · `toolu_015ZRRZDAyT8in5voAtaY8EF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml",
  "offset": 900,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0fdb07d-6fcb-4bba-80d4-9965db1c71df",
  "isSidechain": false,
  "requestId": "req_011Cb4a1qT9FHyewS8otnG6H",
  "type": "assistant",
  "uuid": "95eb334c-78e1-4c32-86f2-a21765209140",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/reviewer_e442a828",
  "sessionId": "0765c104-2abd-42e2-87bc-cff39e71bd8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmzoyKVHbjLM5bLxAEasGU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6948,
      "cache_read_input_tokens": 132082,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6948,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 132082,
          "cache_creation_input_tokens": 6948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6948
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

_source line 166 · 2026-05-15T15:12:27.909Z_

<details><summary>↩ Tool result · `toolu_015ZRRZDAyT8in5voAtaY8EF`</summary>

```text
900	    role: reference
901	    result: alpha=32 无需重跑
902	  depends_on: []
903	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95eb334c-78e1-4c32-86f2-a21765209140",
  "isSidechain": false,
  "promptId": "29973f98-8d7d-4a5e-ba55-2e3eddf46b62",
  "type": "user",
  "uuid": "b8aeb0fe-466b-4710-a6fd-ec66f4b591ae",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml",
      "content": "    role: reference\n    result: alpha=32 无需重跑\n  depends_on: []\n",
      "numLines": 4,
      "startLine": 900,
      "totalLines": 903
    }
  },
  "sourceToolAssistantUUID": "95eb334c-78e1-4c32-86f2-a21765209140",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/reviewer_e442a828",
  "sessionId": "0765c104-2abd-42e2-87bc-cff39e71bd8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 167 · 2026-05-15T15:12:34.835Z_

<details><summary>Logged reasoning block</summary>

```text
The file is 903 lines long and ends at line 903. Let me read from further back to find the most recent decisions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8aeb0fe-466b-4710-a6fd-ec66f4b591ae",
  "isSidechain": false,
  "requestId": "req_011Cb4a2ZcvcupbSzMk47BZj",
  "type": "assistant",
  "uuid": "2e6d02a5-a113-4d51-a4c4-0bb0bd681643",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/reviewer_e442a828",
  "sessionId": "0765c104-2abd-42e2-87bc-cff39e71bd8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bYTRtYTmyQAGLpsxwstjH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 227,
      "cache_read_input_tokens": 139030,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 139030,
          "cache_creation_input_tokens": 227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 227
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

_source line 168 · 2026-05-15T15:12:35.477Z_

<details open><summary>🔧 Tool call — Read · `toolu_016Ni6JnHGJGo8Zw1nGFcirJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml",
  "offset": 830,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e6d02a5-a113-4d51-a4c4-0bb0bd681643",
  "isSidechain": false,
  "requestId": "req_011Cb4a2ZcvcupbSzMk47BZj",
  "type": "assistant",
  "uuid": "39e1dac1-fe84-443d-af10-9101bc47b20e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/reviewer_e442a828",
  "sessionId": "0765c104-2abd-42e2-87bc-cff39e71bd8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bYTRtYTmyQAGLpsxwstjH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 227,
      "cache_read_input_tokens": 139030,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 139030,
          "cache_creation_input_tokens": 227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 227
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

_source line 169 · 2026-05-15T15:12:35.494Z_

<details><summary>↩ Tool result · `toolu_016Ni6JnHGJGo8Zw1nGFcirJ`</summary>

```text
830	  - exp_id: exp_008_base_pretrained_eval_v2
831	    role: pending
832	    result: 0.5B base eval still running, expected same pattern
833	  depends_on:
834	  - D045
835	- id: D047
836	  date: 2026-05-15 11:56 UTC
837	  summary: Drop base pretrained from regime comparison; d000 SFT as clean baseline;
838	    remove "SFT tax" framing
839	  rationale: 'Reviewer CRITICAL: 1.5B base pretrained 99.5% predicts "A" on MC (position
840	    bias, not knowledge). Combined with D045 (0.5B same pattern), base pretrained
841	    models at ≤1.5B cannot serve as MC baselines — IRT data meaningless, contamination
842	    signals trivially zero. Base→SFT gap reflects instruction following acquisition,
843	    not calibration/contamination. Core claims unaffected: Claim 1 characterization
844	    uses SFT dosage gradient (d000→d100), d000 is already the clean baseline. Exp-008
845	    regime axis: drop "base", keep {SFT-clean, SFT-contaminated, RL}. Report base
846	    pretrained failure in Discussion as "capacity threshold for reliable MC evaluation"
847	    (extends D045 from 0.5B to 1.5B).'
848	  related_experiments:
849	  - exp_id: exp-008
850	    role: triggered_by
851	    result: 1.5B base pretrained MMLU=23% ARC=23% GSM8K=0.5% — all MC answers are
852	      A
853	  - exp_id: exp_008_base_pretrained_eval_v2
854	    role: in_progress
855	    result: 0.5B base eval still running, will show same MC degradation per D045
856	  depends_on:
857	  - D045
858	- id: D048
859	  date: 2026-05-15 15:09 UTC
860	  summary: LoRA alpha=32 为全项目标准值。3B s42 的 5 个 alpha=16 实验需重跑，但 pooled IRT 可先用 alpha=32
861	    一致子集（N≥19）启动
862	  rationale: 21/26 SFT 实验用 alpha=32（默认），仅 5 个 3B s42 实验用了 alpha=16（手动提交时指定）。统一到 alpha=32
863	    成本最低（重跑 5 个 vs 21 个）。0.5B/1.5B 全系列 + 3B s123 全系列均为 alpha=32，排除 3B s42 后仍有 N≥19
864	    examinees，满足 N≥16 pooled IRT 要求，可先跑 pooled IRT 不等重跑。
865	  related_experiments:
866	  - exp_id: exp_001_sft_3B_d025_s123
867	    role: trigger
868	    result: 调查发现 alpha 不一致
869	  - exp_id: exp_001_sft_d100_15B_v2
870	    role: baseline
871	    result: alpha=32 一致
872	  depends_on: []
873	- id: D049
874	  date: 2026-05-15 15:09 UTC
875	  summary: LoRA alpha 统一为 32。5 个 3B s42 实验 (alpha=16) 需重跑，0.5B/1.5B 不受影响。重跑优先级低于当前
876	    critical path (s123 eval → pooled IRT)
877	  rationale: 21/26 SFT 实验已用 alpha=32，统一到 32 的重跑代价最小（5 个 vs 21 个）。跨种子 alpha 不一致会破坏
878	    multi-seed pooling 前提条件。受影响实验：3B d000_v2 ×2, d025_s42 ×1, d100 ×2。重跑后还需重做对应 eval
879	    和 signals。总成本约 25 GPU-hours，不阻塞当前 s123 关键路径。
880	  related_experiments:
881	  - exp_id: exp_001_sft_3B_d025_s123
882	    role: trigger
883	    result: 调查发现 alpha=32 vs 其他 3B s42 alpha=16 不一致
884	  depends_on: []
885	- id: D050
886	  date: 2026-05-15 15:09 UTC
887	  summary: 统一 LoRA alpha=32。重跑 5 个 3B s42 实验（d000_v2×2, d025×1, d100×2），0.5B/1.5B
888	    不受影响
889	  rationale: Worker 调查发现 run_exp001.sh 未显式传 --lora-alpha，21/26 SFT 用默认 alpha=32，5
890	    个 3B s42 手动指定了 alpha=16。跨种子可比性前提（同 dosage 同超参）被破坏。方案 A（统一 32）重跑代价最小（5 vs 21），且
891	    0.5B/1.5B 数据完全可用。10 天 DDL 不允许方案 B。
892	  related_experiments:
893	  - exp_id: exp_001_sft_3B_d025_s123
894	    role: trigger
895	    result: alpha=32 默认
896	  - exp_id: exp_001_sft_d025_3B
897	    role: affected
898	    result: alpha=16 需重跑
899	  - exp_id: exp_001_sft_d100_15B_v2
900	    role: reference
901	    result: alpha=32 无需重跑
902	  depends_on: []
903	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39e1dac1-fe84-443d-af10-9101bc47b20e",
  "isSidechain": false,
  "promptId": "29973f98-8d7d-4a5e-ba55-2e3eddf46b62",
  "type": "user",
  "uuid": "45a57788-0dc5-42fd-92b3-64334a54a6a0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml",
      "content": "  - exp_id: exp_008_base_pretrained_eval_v2\n    role: pending\n    result: 0.5B base eval still running, expected same pattern\n  depends_on:\n  - D045\n- id: D047\n  date: 2026-05-15 11:56 UTC\n  summary: Drop base pretrained from regime comparison; d000 SFT as clean baseline;\n    remove \"SFT tax\" framing\n  rationale: 'Reviewer CRITICAL: 1.5B base pretrained 99.5% predicts \"A\" on MC (position\n    bias, not knowledge). Combined with D045 (0.5B same pattern), base pretrained\n    models at ≤1.5B cannot serve as MC baselines — IRT data meaningless, contamination\n    signals trivially zero. Base→SFT gap reflects instruction following acquisition,\n    not calibration/contamination. Core claims unaffected: Claim 1 characterization\n    uses SFT dosage gradient (d000→d100), d000 is already the clean baseline. Exp-008\n    regime axis: drop \"base\", keep {SFT-clean, SFT-contaminated, RL}. Report base\n    pretrained failure in Discussion as \"capacity threshold for reliable MC evaluation\"\n    (extends D045 from 0.5B to 1.5B).'\n  related_experiments:\n  - exp_id: exp-008\n    role: triggered_by\n    result: 1.5B base pretrained MMLU=23% ARC=23% GSM8K=0.5% — all MC answers are\n      A\n  - exp_id: exp_008_base_pretrained_eval_v2\n    role: in_progress\n    result: 0.5B base eval still running, will show same MC degradation per D045\n  depends_on:\n  - D045\n- id: D048\n  date: 2026-05-15 15:09 UTC\n  summary: LoRA alpha=32 为全项目标准值。3B s42 的 5 个 alpha=16 实验需重跑，但 pooled IRT 可先用 alpha=32\n    一致子集（N≥19）启动\n  rationale: 21/26 SFT 实验用 alpha=32（默认），仅 5 个 3B s42 实验用了 alpha=16（手动提交时指定）。统一到 alpha=32\n    成本最低（重跑 5 个 vs 21 个）。0.5B/1.5B 全系列 + 3B s123 全系列均为 alpha=32，排除 3B s42 后仍有 N≥19\n    examinees，满足 N≥16 pooled IRT 要求，可先跑 pooled IRT 不等重跑。\n  related_experiments:\n  - exp_id: exp_001_sft_3B_d025_s123\n    role: trigger\n    result: 调查发现 alpha 不一致\n  - exp_id: exp_001_sft_d100_15B_v2\n    role: baseline\n    result: alpha=32 一致\n  depends_on: []\n- id: D049\n  date: 2026-05-15 15:09 UTC\n  summary: LoRA alpha 统一为 32。5 个 3B s42 实验 (alpha=16) 需重跑，0.5B/1.5B 不受影响。重跑优先级低于当前\n    critical path (s123 eval → pooled IRT)\n  rationale: 21/26 SFT 实验已用 alpha=32，统一到 32 的重跑代价最小（5 个 vs 21 个）。跨种子 alpha 不一致会破坏\n    multi-seed pooling 前提条件。受影响实验：3B d000_v2 ×2, d025_s42 ×1, d100 ×2。重跑后还需重做对应 eval\n    和 signals。总成本约 25 GPU-hours，不阻塞当前 s123 关键路径。\n  related_experiments:\n  - exp_id: exp_001_sft_3B_d025_s123\n    role: trigger\n    result: 调查发现 alpha=32 vs 其他 3B s42 alpha=16 不一致\n  depends_on: []\n- id: D050\n  date: 2026-05-15 15:09 UTC\n  summary: 统一 LoRA alpha=32。重跑 5 个 3B s42 实验（d000_v2×2, d025×1, d100×2），0.5B/1.5B\n    不受影响\n  rationale: Worker 调查发现 run_exp001.sh 未显式传 --lora-alpha，21/26 SFT 用默认 alpha=32，5\n    个 3B s42 手动指定了 alpha=16。跨种子可比性前提（同 dosage 同超参）被破坏。方案 A（统一 32）重跑代价最小（5 vs 21），且\n    0.5B/1.5B 数据完全可用。10 天 DDL 不允许方案 B。\n  related_experiments:\n  - exp_id: exp_001_sft_3B_d025_s123\n    role: trigger\n    result: alpha=32 默认\n  - exp_id: exp_001_sft_d025_3B\n    role: affected\n    result: alpha=16 需重跑\n  - exp_id: exp_001_sft_d100_15B_v2\n    role: reference\n    result: alpha=32 无需重跑\n  depends_on: []\n",
      "numLines": 74,
      "startLine": 830,
      "totalLines": 903
    }
  },
  "sourceToolAssistantUUID": "39e1dac1-fe84-443d-af10-9101bc47b20e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/reviewer_e442a828",
  "sessionId": "0765c104-2abd-42e2-87bc-cff39e71bd8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
