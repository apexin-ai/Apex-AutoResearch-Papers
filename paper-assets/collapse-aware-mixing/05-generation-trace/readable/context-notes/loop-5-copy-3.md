# reviewer / loop_5.md

**collapse aware mixing** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`c64a0fab57f6147eb033.json`](../../sessions/c6/c64a0fab57f6147eb033.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-14T03:52:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:0**（cqa1-38874 单卡 RTX PRO 6000 96GB，`execution.gpu_ids=[0]`）
- mvp_seed0_replication_r2 正在 cuda:0 上运行（PID 122208），**不要 kill 它**——它是 seed robustness 验证的关键前置实验
- 远程代码根目录是 `/root/collapse-aware-mixing/`，本地 workspace 是 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/`——论文/设计文档在本地，训练代码/checkpoint/日志在远程，**不要混淆源**
- controller.py 已从旧的 `CollapseAwareController`（velocity-form, spectral eff_rank）重写为 `PIController`（position-form, n-gram entropy）——**不要回退到旧版本**

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-38874`，工作目录 `/root/collapse-aware-mixing/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型缓存：`/root/autodl-tmp/.hf_cache/`（HF_HOME）
- 实验输出：`/root/autodl-tmp/output_seed0/`（seed0 实验），`/root/autodl-tmp/output_v7/`（v7 原始数据）
- 活跃进程：mvp_seed0_replication_r2（PID 122208，tmux session，cuda:0），预计完成 ~2026-05-14 17:00-18:00 UTC
- 无 wandb（项目未配置 W&B，不检查）
- 无 cron 任务

### 3. 📊 当前状态
**刚完成**：Plan A 实现代码审查（controller.py + controlled_pipeline.py），发现 seed 未设置的 bug → bugfix worker 已修复（四路 seed + num_workers=0），代码可投入实验。

**Registry 活跃实验**：
- `mvp_seed0_replication_r2` — **RUNNING**，seed=0 复现 v7（3 代 × 20M tokens），审查时在 G0 评估阶段 (checkpoint 6/6)，还需 ~13-15h 完成 G1+G2

**等待中**：
- seed0 实验完成后需要审查其结论（eff_rank 是否在 seed=0 下仍然上升——Plan A §3 "Why Spectral Rank Fails" 的前提）
- Director 尚未就 Plan A 实验矩阵做出 GO/NO-GO 决策（我已提交技术可行性评估 + 设计文档审查 + 实现审查）

### 4. 📋 待办（条件触发式）
- **seed0 实验完成** → 审查 metrics：若 holdout eff_rank 仍上升 → Plan A §3 前提成立；若 eff_rank 下降 → [severity: critical]，Plan A narrative 需要重大调整
- **Director 批准 Plan A 实验** → 审查首次 PI controller 实验的 registry spec（确认用 controlled_pipeline.py 而非旧的 main_experiment.py，确认 --mode pi_controller + n-gram entropy 信号）
- **Plan A Phase 1 实验开始** → 核实 GPU 利用率 + 确认没有跑在 spectral eff_rank 旧代码上
- **收到章节写作审查** → 先检查 paper_framing.md 是否已更新（当前完全过时，仍基于 C1 positive hypothesis）

### 5. 🎯 战略上下文
**决策链**：D014（C1 falsified: holdout eff_rank 上升+0.96%）→ D016（Pivot B "GO" 但被 D018 推翻）→ D018（MVP FAIL，三条路全封：C1/Pivot B/Direction C）→ 当前在 Plan A（n-gram entropy + PI controller 闭环控制）和 Q2（negative result paper）之间选择。

**核心发现**：spectral eff_rank 作为 collapse 检测信号彻底失败（holdout 上升、generated 噪声 573x 高于 n-gram）。N-gram entropy 是 superior 信号（-86% drop at G1 step 152, var=0.77）。文献调研确认**没有人做过 collapse-signal-driven adaptive real/synthetic mixing**——这是 Plan A 的核心 novelty gap。

**最容易判断错的事**：
1. **不要把 main_experiment.py 当作 Plan A 入口**——它仍用 spectral eff_rank 旧控制器。正确入口是 `controlled_pipeline.py --mode pi_controller`
2. **GPU 时间估算**：每次 5-gen 运行约 26h（不是 6h），因为 synthetic generation 占 74% 时间。Phase 1 (5 条件 × 1 seed) ≈ 130h
3. **paper_framing.md 完全过时**——仍基于 C1 positive hypothesis，不要引用其中的 claims/contributions
4. **D013 "why not threshold"** 是在 eff_rank 信号下的判断，换到 n-gram entropy 后不再适用——但 threshold 仍作为 ablation baseline 保留在实验矩阵中


---
