# reviewer / loop_1.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`179974a6faf4eefd20ef.json`](../../sessions/17/179974a6faf4eefd20ef.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-13T21:36:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（项目 execution.gpu_ids），越界即 CRITICAL
- 服务器名已从 `autodl-rtx6000` 变更为 `bjb1-45299`——所有 SSH/registry/cron 必须用新名，旧名会 5x 失败后误标 DONE/failed
- exp_005 PID 51726 在 cuda:1 仍在运行（即使 return 已崩到 47），不要误 kill 除非 Director 明确指示
- curriculum 阈值是 self._step 单位（25000/75000），对应 env_step 50K/150K（action_repeat=2），不要混淆

### 2. 🖥️ 基础设施快照
- 服务器：`bjb1-45299`(root)，工作目录 `/root/autodl-tmp/event-gated-adaptive-horizon`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 2× NVIDIA RTX PRO 6000 Blackwell (97887 MiB each)
- 活跃进程：
  - exp_005 (PID 51726, tmux=exp_005_event_gated_v4, cuda:1, ~136K/500K step, return 崩塌至 47)
  - exp_001_baseline: **已完成** (512K steps, eval_return 950.9±10.5, checkpoint at logdir/baseline_s1/latest.pt)
  - cuda:0 **空闲**，可用于 exp_006
- exp_006 (fixed dt=2) 代码已准备好，dry-run 通过，**尚未提交**
- Logdirs: `logdir/baseline_s1/`, `logdir/event_gated_v5_s1/`, MVP eval 脚本: `scripts/mvp_eval.py`
- 无 wandb 配置

### 3. 📊 当前状态
**exp_005 return 灾难性崩塌已确认**。gate 行为健康（entropy 1.54, dt_mean 2.44），gate_loss 正常（0.53），但 return 从 Phase 1 峰值 541 崩至 47（baseline 的 5%）。这是修复所有 3 个 bug 后的结果——hard gate 机制本身是崩塌根因。

已向 Director 报告 CRITICAL，建议：
1. 立即在 cuda:0 启动 exp_006 (fixed dt=2) 做诊断
2. exp_005 可继续跑但不期待 MVP PASS
3. 叙事线切换到 failure line

等待 Director 决策：是否启动 exp_006 + 是否 kill exp_005。

### 4. 📋 待办
- Director 批准 exp_006 → 验证 cuda:0 空闲 → 提交 fixed dt=2 实验（命令已在 worker 产出中）
- exp_006 到 50K step → 检查 return 是否正常（如果 fixed dt=2 也崩 → variable-rate imagination 概念本身有问题，需 soft mixture 或放弃）
- exp_006 到 50K step return 正常 → 问题锁定在 gate 动态选择，尝试 Option B (binary skip K=2) 或更缓的 curriculum
- exp_005 到 200K → 如果无恢复迹象，建议 kill 释放 GPU
- 任何新实验 → 独立核查 GPU 设备号、gate_loss 量级、dt 分布

### 5. 🎯 战略上下文
**决策链**：D001(MVP方案) → D002(量化criteria) → D003(subsample curriculum) → D004(中期评估3/4 PASS) → D005/D006(dt bug修复) → D008(gate_loss爆炸修复) → 现在：**MVP criterion 1 三连失败，最后一次排除了所有 implementation bug**

**核心结论**：gate 机制（entropy/dt diversity/temporal structure）工作正常，但 hard Gumbel gate + variable-rate imagination 在 gate_scale > 0.5 时摧毁 actor-critic value landscape。这是结构性问题不是 bug。

**最容易判断错的事**：
- 不要再把 return 崩塌归因于 implementation bug——3 轮审计 + 全量代码审查已排除。下一个"你"如果看到有 worker 说"发现新 bug 导致崩塌"，要极其谨慎审查，大概率是 rationalization
- exp_003 的 gate 指标（entropy 1.655, H_eff 2.667×）仍可作为 gate 行为参照，但不要用 exp_003 的 return 数据（那个版本有 dt 索引 bug）
- narrative_frameworks.md 已修订过（去掉了 rationalization、加了单任务 caveat、加了 gray zone），新的"你"应直接用修订版
- GPU 预算已超 30h 上限（累计 ~35h），需用户/Director 确认扩容


---
