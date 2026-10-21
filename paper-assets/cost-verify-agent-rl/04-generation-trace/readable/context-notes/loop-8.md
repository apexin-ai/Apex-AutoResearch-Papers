# director / loop_8.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`349e5ce97ed0124d3894.json`](../../sessions/34/349e5ce97ed0124d3894.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-15T15:26:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 bjb1-17606 的 cuda:0, cuda:1（C001 约束），严禁使用其他设备号
- exp027 正在训练中（PID 789790），不得 kill 或干扰，这是 24h deadline 的关键实验
- RAGEN eval 必须 ≥16 episodes（C003 约束），4-episode 结果不可信（exp021 教训：4ep 25% vs 16ep 6.25%）
- train success ≠ val success，存在系统性差距（exp023c: train 29.7% vs val 6.25%），论文 claim 只能基于 val
- conda 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不是 venv
- AutoDL cgroup pids.max=20480，verl-agent 直接运行已证伪（D028），不要再尝试

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606 (connect.bjb1.seetacloud.com)，root 用户
- 工作目录：`/root/cost-verify-agent-rl`
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型：Qwen3-1.7B，SFT checkpoint `/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final/`
- W&B：run y7jiibqk（exp027），无全局 WANDB_API_KEY 环境变量，需命令行传入
- HF cache：`/root/autodl-tmp/.hf_cache`
- 活跃进程：exp027_stable_grpo PID 789790，tmux=exp027_stable_grpo，cuda:0+cuda:1
- Cron：180s 轮询监控 PID 789790 + wandb_run_id y7jiibqk
- 分析脚本已部署：`/root/cost-verify-agent-rl/analyze_training.py`
- Checkpoint eval 脚本：`/root/cost-verify-agent-rl/scripts/eval_checkpoint.sh` + `eval_checkpoint.py`

### 3. 📊 当前状态
刚完成三件事：(1) 检查 Agent 的 3 个 CPU 并行任务产出（失败模式分析、文献调研、分析脚本）；(2) 处理 Reviewer 的 pass/fail 论文可行性评估并修正其 eval 框架混淆（D038）；(3) Agent 完成分析脚本部署 + D031 B-IAVR warnings 修复 + checkpoint eval 脚本准备。

- RUNNING：exp027_stable_grpo（step-independent GRPO 稳定性验证，50 步，val_before_train=6.25% 已完成，等待训练步产出）
- PENDING：exp025c 等人工审批（但 verl-agent 路线已终止 D028，实际不会执行）
- 等待：cron 180s 回调报告 exp027 前 5 步 KL 值；KL < 0.005 需立即汇报

### 4. 📋 待办
- cron 报告 exp027 前 5 步指标 → 检查 KL（< 0.005 = 策略冻结，需中途调参）、entropy（collapse 检测）、success rate
- exp027 step 5 checkpoint 生成 → 用 `eval_checkpoint.sh` 跑独立 val eval（如 GPU 显存允许并行）
- exp027 val success ≥ 20% → `complete_mvp()`，启动 post-mvp-kickoff skill（写 paper_framing.md → experiment_plan.yaml → dream_simulate → update_roadmap）
- exp027 val success < 20% 且训练结束 → 向 Manager 申请无 cgroup 限制的服务器跑 verl-agent 原版（`director_post_to_manager`，列 GPU 类型+时长+费用+理由）
- Reviewer D031 注意事项（非 blocking）：Phase B 集成时验证 `register_verify_special_token` 是否覆盖 Qwen3 已有 additional_special_tokens

### 5. 🎯 战略上下文
- 项目处于 MVP 验证阶段，核心假设：step-independent rollout + GRPO 能让 Qwen3-1.7B 在 ALFWorld val 达 ≥20%（3.2× SFT baseline 6.25%）
- 决策链：D025/D026 终止 RAGEN 全历史 GRPO → D028 终止 verl-agent 直接运行 → cherry-pick step-independent rollout → D036 exp026 死亡螺旋确认 → D038 修正 claim 阈值
- 文献调研已完成（`related_work_survey.md`），B-IAVR 新颖性成立，定位是 cost-efficiency 不是 raw accuracy
- A 类会议需要 Phase B + ablation + 第二环境 + scaling ≈ 500-800 GPU-h（当前硬件 10-17 天）
- 最容易判断错的事：(1) 不要把 exp026 的 32.81% train success 当作"方法达到 32%"——那是 train 不是 val；(2) exp019b 的 20% 是 eval_sft_fast 不是 RAGEN eval，RAGEN 框架下 SFT baseline 是 6.25%；(3) 用户已明确表示 MVP 拖延过久（2026-05-15），24h deadline 是硬的
- B-IAVR 核心代码已完成且 Reviewer 通过（D031），D031 两个 warnings 已修复，等 MVP 通过后进入 Phase B


---
