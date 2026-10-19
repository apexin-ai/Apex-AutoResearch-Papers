# agent / loop_15.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_15.md`
- **Structured JSON:** [`f1f9571cef89207fc883.json`](../../sessions/f1/f1f9571cef89207fc883.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_wall_time
updated: '2026-05-17T11:21:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 bjb1-17606 的 cuda:0 + cuda:1（gpu_ids 白名单，其他 GPU 未分配）
- hsweep_h2_seed1 正在 PID 920380 上跑，**禁止 kill 或干扰该进程**
- tmux session `hsweep_watchdog` 是安全网监控，不要删除
- h-sweep auto_next 序列已优化（2:1→2:2→5:1→10:1→20:1→full:1→补剩余），不要改回原序列
- val 对比必须统一 env_groups=32 + full context mode（不同 context mode 下 val 不可直接比较）
- 论文 baseline 数字：episode-level = 12.5%（4/32, exp029），不是 6.25%

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606，工作目录 `/root/cost-verify-agent-rl/`
- Python：`/root/miniconda3/bin/python`（conda base env）
- RAGEN 框架：`/root/cost-verify-agent-rl/RAGEN/`，Hydra config 在 `RAGEN/config/`
- SFT checkpoint：`/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4`
- Runs 目录：`~/runs/cost-verify-agent-rl/`（日志），`/root/autodl-tmp/checkpoints/`（权重）
- W&B project：wandb 启用（不要设 WANDB_MODE=disabled，会导致 cron auto-fail）
- 活跃进程：hsweep_h2_seed1 PID 920380 (cuda:0,1), tmux=hsweep_watchdog
- Cron：hsweep_h2_seed1 监控中（reconcile 确认 still running）

### 3. 📊 当前状态
**刚完成**：
- auto_next 序列优化（先跑每个 h 各 1 seed 出 cliff figure）
- plan_003b GAE + REINFORCE++ baseline config 创建并验证（待 GPU 启动）
- post-hoc full-context eval 脚本（D059）
- cliff figure 可视化脚本（plot_hsweep_cliff.py，含 demo 模式）
- 论文全部章节初稿：introduction, method, theoretical_analysis, experiments(骨架), related_work, discussion+limitations, conclusion, references.bib（29 entries verified）

**Registry RUNNING**：hsweep_h2_seed1（step 2/15，~48min/step，预计 ~17:30 UTC 完成）

**等待中**：
- hsweep_h2_seed1 cron 完成回调 → 触发 hsweep_complete_handler.sh → auto_next 启动 h=2 seed 2（含 advantage logging）
- h=2 seed 2 完成后 → 运行 analyze_advantage_log.py 产出 plan_004 sign misattribution 证据
- Director 决策：何时/是否启动 GAE baseline（plan_003b）

### 4. 📋 待办（条件触发式）
- cron 回调 hsweep_h2_seed1 完成 → spawn worker 跑 `hsweep_complete_handler.sh 2 1`，确认 auto_next 正常启动 h=2 seed 2
- h=2 seed 2 完成 → 运行 `analyze_advantage_log.py` on advantage_log.jsonl → 汇报 sign misattribution 证据
- 每个 h 的 seed 1 全部完成（5:1, 10:1, 20:1, full:1）→ 运行 `eval_checkpoint_full_context.py` 批量 eval → 运行 `plot_hsweep_cliff.py` 生成 preliminary cliff figure → 汇报 Director
- Director 分配额外 GPU 或 h-sweep 完成释放 GPU → 启动 GAE baseline：`python train.py --config-name _alfworld_gae_baseline`
- 论文 experiments.tex 有 6 个 placeholder → h-sweep 数据到手后填入真实数字

### 5. 🎯 战略上下文
- **核心论点**：step-independent GRPO 在多轮 agent 任务中因 advantage sign misattribution（M1）+ γ-attenuated credit decay（M2）导致训练崩溃；episode-level GRPO 是简单有效的解决方案
- **论文结构已完整**，等数据填入 placeholder 即可组装 LaTeX 提交
- **Cliff figure 是关键 evidence**：展示 performance 随 h 减小骤降。新序列优化后 2-3 天可出 preliminary 版本
- **val 比较陷阱**：h-sweep 训练时的 val 也受 context 截断（h=2 step0 val=0%），必须用 `eval_checkpoint_full_context.py` 做 post-hoc full-context eval 才能公平比较
- **GAE baseline 几乎零代码**：verl 原生支持，config 已就绪，只缺 GPU 时间
- **62pp gap 已解释**（见 memory: project_recipe_gap_findings.md）：SFT 和 penalty 已排除，recipe 参数组合是根因
- **易错点**：不要用训练时的 val metrics（受 context mode 影响）作为 cliff figure 数据源，必须用 post-hoc full-context eval 结果


---
