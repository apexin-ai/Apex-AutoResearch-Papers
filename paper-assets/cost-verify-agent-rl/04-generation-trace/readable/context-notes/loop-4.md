# director / loop_4.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`99a56e6b3fccfb37a6e2.json`](../../sessions/99/99a56e6b3fccfb37a6e2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-15T03:19:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 bjb1-17606 的 cuda:0 和 cuda:1（C001 白名单）
- SFT 模型验证必须用 RAGEN val_before_train，**绝不用 eval_sft_fast**（eval_sft_fast 格式与 RAGEN 不匹配，exp020 系列全部因此失败）
- GRPO checkpoint 路径必须含 "qwen" 字符串（train.py:137 断言），用 symlink 解决
- Cron 对 SFT 实验（report_to="none"）会误报 failed——收到 cron on_failed 先检查 GPU 进程和日志再判断，已发生 4 次误报
- kill_job 只杀 tmux 主进程，Ray worker 子进程可能残留占 GPU 显存，kill 后必须 `ray stop --force` + 确认 nvidia-smi

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606 (connect.bjb1.seetacloud.com)，root 账号
- 工作目录：/root/cost-verify-agent-rl
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base）
- 模型 checkpoints：/root/autodl-tmp/checkpoints/
  - exp008_sft/final/（格式 SFT baseline）
  - exp019b_expert_sft_v3/final/（Expert SFT，eval_sft_fast 20% 但 RAGEN 0%）
  - exp021_ragen_sft_v4/final/（RAGEN 格式 SFT，RAGEN val 25%）★当前最佳
  - symlink: qwen3_exp021_ragen_sft_v4 → exp021 checkpoint
- SFT 数据：/root/autodl-tmp/expert_sft_v3/（eval_sft_fast 格式）、/root/autodl-tmp/expert_sft_v4/（RAGEN 格式）
- 活跃进程：exp022_grpo_from_sft_v4 (PID 434853, tmux=exp022_grpo_from_sft_v4, cuda:0+1, cron 120s)
- GRPO config：_alfworld_exp022_grpo_from_sft_v4.yaml（kl_loss_coef=0.5, val env_groups=8）

### 3. 📊 当前状态
exp022_grpo_from_sft_v4 正在训练（PID 434853, cuda:0+1, 30 steps, 预计 2.5-3h）。这是 MVP gate 最终验证——从 exp021 RAGEN SFT checkpoint (25% success) 出发做 sparse GRPO。

关键改进 vs exp020b（失败）：RAGEN 格式对齐 ✓、kl_loss_coef 0.1→0.5 ✓、val env_groups 4→8 ✓。

Registry RUNNING：exp022_grpo_from_sft_v4
Registry PREPARING（废弃不推进）：exp021_sft_ragen_format

### 4. 📋 待办
- exp022 cron 回调"完成" → 检查日志确认真完成（防 cron 误报）→ 如 success ≥ 25% 则 MVP 通过（complete_mvp），如 < 25% 则分析失败原因（entropy 坍缩？reward 稀疏？）
- exp022 如果 entropy 再次坍缩（entropy < 0.05）→ 考虑加 entropy bonus、用 DAPO/Clip-Higher、或增大 kl_loss_coef 到 1.0
- exp022 成功 → 进入 research 阶段：写 paper_framing.md → experiment_plan.yaml → dream_simulate → 完整研究规划
- exp022 失败 → 评估 sparse GRPO 是否根本不适合 ALFWorld（success rate 变化趋势），考虑 dense reward（step-level shaping）或换 RL 算法

### 5. 🎯 战略上下文
- **核心发现**：SFT 数据格式必须与 RL 框架精确匹配（D021/D022）。这是本项目最大教训——exp019b 在 eval_sft_fast 中 20% success，在 RAGEN 中 0%，根因是 Turn/State/Reward 多轮格式不一致
- **决策链**：D015-D019（LR 搜索穷尽→Expert SFT pivot→数据格式修复）→ D020（exp019b 通过）→ D021/D022（格式不匹配确认→RAGEN 格式重训）→ D023（exp021 通过，启动 exp022 GRPO）
- **易错点**：(1) 不要相信 eval_sft_fast 的结果来判断 RAGEN 中的表现 (2) cron on_failed 对 SFT 实验大概率是误报 (3) kill Ray 进程需要额外清理 (4) val 4 episodes 统计无意义，至少 8+
- **MVP gate**：ALFWorld success ≥ 20%（sparse GRPO）。当前 SFT baseline 已达 25%，GRPO 需维持或提升。exp020b 用错误格式的 SFT 导致 GRPO 从 18.75% 降到 4.69%，exp022 用正确格式能否避免退化是关键


---
