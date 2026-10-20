---
loop: 22
reason: max_wall_time
updated: '2026-05-25T03:15:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-41312 有 4 张 GPU（cuda:0/1/2/3），项目未配置 `constraints.yaml` 的 gpu_ids 白名单，但实际只用这 4 张卡
- Cron 监控连续两次误判（permuted_score_control_seed42、random_subset_epoch_seed42）：进程正常退出被判 failed。收到 cron:on_failed 时**必须先 SSH 查 checkpoint 是否完整**再信 conclusion
- contamination_20_tau07_seed42 的正确 baseline 是 ρ=0.2 uniform (holdout_ppl=17.336)，**不是** ρ=0.4 uniform (17.694)。Agent 曾用错 baseline 标 success，已被我 CRITICAL 打回改为 negative
- D&R 阈值方向：q>0.3 最激进（保留最少 116935），q>0.7 最温和（保留最多 184908）。detect_remove_q07_seed42_r2 的 hypothesis 文本把方向写反了

### 2. 🖥️ 基础设施快照
- 服务器：westd-41312 (root)，4× NVIDIA RTX PRO 6000 Blackwell (98GB each)
- 工作目录：`/root/provenance_weight_training`（代码）、`/root/autodl-tmp/provenance_weight_training`（模型/数据/输出）
- 模型：`models/Qwen/Qwen3-0.6B`
- 数据：`data/scored_data.jsonl`（ρ=0.4 全量）、`data/scored_data_filtered_q0{3,5,7}.jsonl`（D&R 过滤）、`data/scored_data_rho02.jsonl`
- Eval 数据：`data/human/eval_holdout.jsonl`；eval 脚本 `eval_perplexity.py`
- 输出：`/root/autodl-tmp/provenance_weight_training/output/models/`（100+ 模型目录）
- 本地 artifacts：`/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/figures/`
- 活跃进程（截至 handoff 时）：
  - cuda:1: detect_remove_q07_seed42_r2 (PID 987903, step ~527/6103, ~3h 剩余)
  - cuda:2: detect_remove_q05_seed42 (PID 962199, step ~7942/8477, 即将完成)
  - cuda:3: detect_remove_q03_seed42 (PID 984298, step ~6860/8477, ~8min 剩余)
  - cuda:0: **空闲**（已多次提醒 Director）

### 3. 📊 当前状态
刚完成一轮图表审查（apply_calibrated_rc worker 用 PaperBanana 校准参数重新生成全套 matplotlib 图，PASS）。

**RUNNING 实验**：
- detect_remove_q05_seed42 — D&R q>0.5 训练，cuda:2，94%，马上完成
- detect_remove_q03_seed42 — D&R q>0.3 训练，cuda:3，81%，~8min
- detect_remove_q07_seed42_r2 — D&R q>0.7 训练，cuda:1，9%，~3h

**PREPARING**：16 个（大部分是旧的 1.7B 实验和 env_probe 残留）

**待决**：
- contamination_20_tau07_seed42 仍 ANALYZING / conclusion=negative，等 Director 确认
- PaperBanana 概念图未产出最终渲染（仅 planning 阶段）
- eval commands 已由 prep worker 准备好，q05/q03 完成后应立即触发

### 4. 📋 待办（条件触发式）
- detect_remove_q05_seed42 完成通知到达 → 核实 registry 更新 + eval metrics（holdout/owt/wiki PPL），与 random_subset (17.694) 和 adaptive (~17.668) 对比
- detect_remove_q03_seed42 完成通知到达 → 核实同上，**这是 D&R vs random_subset 对比的关键实验**：若 q03 PPL < 17.694 则 filtering quality load-bearing 成立
- detect_remove_q07_seed42_r2 完成 → 核实 + 完成 D&R 三阈值扫描数据集
- 三个 D&R 都完成 → 审查 D&R threshold sweep 完整性，检查论文 dr_dual_curve 图是否需更新
- 收到章节写作审查请求 → 先 Read paper-quality-lessons.skill.md，走模式 B 全维度审查
- cron:on_failed 任何实验 → **先查 checkpoint 再信结论**（连续两次误判前科）

### 5. 🎯 战略上下文
- 项目核心论点：adaptive provenance weighting 在 ρ≥0.3 时有效（Δ=-0.023 at ρ=0.4），通过 soft q-score reweighting 优于 hard D&R filtering
- 关键已证实结论：(1) batch size amplification 线性（1×→2.3×→3×）；(2) permuted score Δ=+0.225 确认 detector signal load-bearing；(3) ρ=0.2 below effective range；(4) random_subset ≈ uniform（multi-epoch 效应不存在）
- **最容易判断错的事**：D&R 阈值方向——q>0.3 是最激进的（移除最多），q>0.7 是最温和的（保留最多）。hypothesis 文本写反了，不要被误导
- **容易踩的坑**：ρ=0.2 实验的 baseline 是 17.336（ρ=0.2 uniform），不是 17.694（ρ=0.4 uniform）。不同 ρ 的 uniform baseline 不同
- 265 个 registry 实验，168 success / 12 negative / 43 failed。项目处于 research 后期，D&R baseline sweep 是论文最后一批关键实验
