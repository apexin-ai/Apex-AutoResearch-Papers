# director / loop_6.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`6df93f52f17a65960f22.json`](../../sessions/6d/6df93f52f17a65960f22.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-15T10:33:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0, cuda:1（bjb1-17606 项目分配）
- AutoDL 容器 cgroup pids.max=20480，verl-agent Ray 架构在此服务器上无法运行（D028 已终止该路线）
- RAGEN 框架下必须用线程压缩 env vars（OMP/MKL/OPENBLAS_NUM_THREADS=1 等）+ ray_init.num_cpus=8 + enforce_eager=True，否则可能触碰 PID 限制
- exp026 正式训练刚提交（10:28 UTC），是 12+ 小时 GPU 空转后首次实质训练——不要 kill 除非有明确崩溃证据
- success 指标有两种口径：step-level（0.04）vs episode-level（25%）。论文和决策必须用 episode-level

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606 (connect.bjb1.seetacloud.com)，root 用户
- 代码路径：/root/cost-verify-agent-rl（RAGEN 框架）
- verl-agent 参考代码：/root/autodl-tmp/verl-agent/（仅分析用，不能直接运行训练）
- Conda env（verl-agent 专用，不用于 RAGEN）：/root/autodl-tmp/conda-envs/verl-agent/
- RAGEN 用 base conda 环境：source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
- 模型：/root/autodl-tmp/models/Qwen/Qwen3-1___7B/（Qwen3-1.7B，等同 Instruct）
- SFT checkpoint：/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final/
- 磁盘：root 26% / data 54%
- 活跃进程：exp026 刚提交（PID 待确认，tmux=exp026），预计 ~26.5h wall clock
- W&B：应已启用（正式训练脚本含 logger=wandb）

### 3. 📊 当前状态
exp026_step_independent_grpo 刚提交正式训练（150 steps），状态 ALLOCATED→应很快变 RUNNING。这是 Track B cherry-pick 的核心实验：step-independent rollout + step-level discounted returns GRPO，整合到 RAGEN 框架。

dry run step 0 验证通过：step-level advantage 生效（advantages max=11.93/min=-0.47），无 fallback 警告，RAGEN 下 PID=3573 安全。step 1 在 dry run 中异常退出（无 traceback），正式训练是否能稳定过 step 1 待确认。

等待中：
- exp026 启动确认（GPU 加载 + val_before_train）
- step 0-2 稳定性验证
- Reviewer 独立核验 GPU 合规 + W&B 连接 + step-level advantage 生效

### 4. 📋 待办
- exp026 启动后 5 分钟 → 确认 GPU 在用（nvidia-smi）+ 日志有输出 + 无 CRITICAL fallback 警告
- val_before_train 完成 → 检查 episode-level success rate（对比 exp021 的 6.25%）
- step 0-2 完成 → 让 Reviewer 审查 pg_loss/entropy/success 趋势，对比 exp022-24 的退化 pattern
- step 1 崩溃 → 带完整 traceback 诊断，可能是 rollout_filter 或 step-level batch 维度问题
- exp026 success ≥20% → complete_mvp()，进入 research 阶段
- exp026 退化/失败 → 评估是否需要 GiGPO Phase 2（step-level advantage grouping）或调参

### 5. 🎯 战略上下文
- 项目处于 MVP 阶段，目标：ALFWorld success ≥20%（GRPO 训练后）
- SFT baseline：6.25% success（16ep，exp021/exp023c）
- RAGEN GRPO 路线 3/3 退化失败（exp020b/022/023c），根因是 full-history context 爆炸（D025/D026）
- D026 pivot 到 verl-agent，D028 因 cgroup 限制放弃直接运行 verl-agent，转为 cherry-pick step-independent rollout 到 RAGEN
- exp026 vs exp022-24 关键变更：context O(1) vs O(steps)、KL 0.01 vs 0.5、LR 1e-6 vs 5e-7、step-level reward vs episode-only
- 易错点：(1) 不要再尝试在 bjb1-17606 上跑 verl-agent（Ray 会撞 pids.max）(2) 不要把 step-level success metric（0.04）当成 episode-level success rate（25%）(3) anchor_obs 日志污染问题未修——大量 "Skipping non-numeric metric" 警告是正常的，不影响训练 (4) is_action_valid 路径已修复但要确认正式训练中 invalid_action_penalty 是否实际触发
- cherry-pick Phase 2（GiGPO）方案已就绪（gigpo_cherry_pick_plan.md），等 Phase 1 结果决定是否需要


---
