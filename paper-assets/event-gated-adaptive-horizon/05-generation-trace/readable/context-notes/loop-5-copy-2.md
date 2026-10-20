# agent / loop_5.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`efe8d9fdf5e95173245b.json`](../../sessions/ef/efe8d9fdf5e95173245b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-14T07:27:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 `cuda:0` 和 `cuda:1`（服务器 bjb1-45299）。**不得使用其他 GPU 编号**
- 提交命令必须用绝对路径激活 conda：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，**不要假设 .venv 存在**
- 环境变量三件套必带：`LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6`、`MUJOCO_GL=osmesa`、`PYOPENGL_PLATFORM=osmesa`
- exp_009a 已 ALLOCATED 到 cuda:0，exp_009c 已 ALLOCATED 到 cuda:1——**必须等 008f/008e_v3 完成释放 GPU 后才能提交**，不要强占
- Worker 计算 normalized v/e 经常出错（用固定值做分母）——汇报时必须自己用 baseline 同 step 的 v/e 重算

### 2. 🖥️ 基础设施快照
- **服务器**：bjb1-45299（AutoDL RTX PRO 6000 ×2）
- **工作目录**：`/root/autodl-tmp/event-gated-adaptive-horizon`
- **Python**：`/root/miniconda3/bin/python`（conda base 环境）
- **模型/数据**：DMC Walker Walk（dm_control built-in），无需额外数据集下载
- **脚本已就绪**：`scripts/multi_seed_runs.sh`（Walker 6 configs）、`scripts/cheetah_run_experiments.sh`（Cheetah 9 configs）
- **活跃进程**：
  - exp_008f_no_dt_embed_subsample_on_h8：PID 127761，tmux session，cuda:0，~56K/105K
  - exp_008e_v3_subsample_on_dt1_h15：PID 126110，tmux session，cuda:1，~68K/105K
- **Cron 监控**：2 个活跃 cron 分别监控上述两个实验
- **无活跃 Worker**

### 3. 📊 当前状态
**刚完成**：session-start 初始化，registry 同步完成，两个 RUNNING 实验 cron 确认存活。

**RUNNING（2 个）**：
- `exp_008f_no_dt_embed_subsample_on_h8`（cuda:0，~56K/105K）——C2 因果控制实验，dt_embed_dim=0。55K 时 normalized v/e=0.97x，仍正常。预计还需 ~2h
- `exp_008e_v3_subsample_on_dt1_h15`（cuda:1，~68K/105K）——B+ confound 控制。65K eval=580.7（94% baseline），normalized v/e=0.72x，非常健康。预计还需 ~1.5h

**ALLOCATED 待提交（2 个，等 GPU 释放）**：
- `exp_009a_baseline_walker_s2`（cuda:0）——Walker baseline seed 2
- `exp_009c_008f_walker_s2`（cuda:1）——008f 复现 seed 2

**QUEUED（2 个，未分配 GPU）**：
- `exp_009b_008d_walker_s2`——008d 崩塌复现 seed 2
- `exp_010a_cheetah_baseline_s1`——Cheetah Run baseline seed 1

**等待中**：
- 2 个 cron 回调（008f/008e_v3 完成时触发）
- Dream review（dream_20260514T062606）尚未回调——Director 启动的 full review，通过后批准 P0 实验

### 4. 📋 待办（条件触发式）
- **008f cron 回调到达** → 分析 105K 最终 metrics，更新 registry（conclusion 取决于 v/e 是否 <1.2x），汇报 Director。释放 cuda:0 后立即用 `submit_on_allocated` 提交 exp_009a（已 ALLOCATED）
- **008e_v3 cron 回调到达** → 分析 105K，验证 subsample ON + untrained dt_emb 长期稳定性。释放 cuda:1 后立即用 `submit_on_allocated` 提交 exp_009c（已 ALLOCATED）
- **009a + 009c 提交后** → cuda:0/1 各还能共存 1 个实验（VRAM<9%），可同时提交 009b 和 010a（需先向 Director 确认 GPU 共存方案）
- **Dream review 回调到达** → 按反馈调整 paper_framing / experiment_plan，然后批准 P0 后续实验
- **所有 Walker seed 2 完成** → spawn Worker 做统计显著性分析（paired t-test / bootstrap CI），更新 report.md

### 5. 🎯 战略上下文
**核心结论**：Narrative B+（Diagnostic Analysis of Temporal Abstraction）。因果链已闭合：trained dt_embedding → delusional critic → value overestimation → collapse。Untrained dt_embedding 提供结构性 value growth suppression（008a@105K=778，82% baseline，normalized v/e=0.59x）。

**决策链关键节点**：
- D028：C2 因果归因确认（008f vs 008d）
- D027：C3 措辞决定（"preventing optimistic drift"）
- D020：因果机制修正（精确 imagination → delusional critic）
- D019：compounding error 假说被 008c 反驳

**目标**：CoRL 2026，DDL 2026-05-29（剩 15 天）。P0+P1 实验预算 ~121 GPU·h（~2.5 天 wall time），时间充裕。

**易错点**：
- **不要把 H=8 实验（008c/008d/008f）的 eval_return 和 H=15 实验（008a/baseline）直接比较**——H=8 learning signal 不足导致系统性偏低，只能比 v/e ratio
- **008e_v3 gate 完全锁定 dt=1（entropy=0）**——这是 untrained dt_emb 的预期行为，不是 bug
- **exp_008a/008c/008d/006/008e_v2 等 PREPARING 状态条目**是历史残留（与对应的 `_xxx` 全名实验重复），不要当作待执行实验
- **GPU 共存方案（每 GPU 2 实验）已验证可行**，但尚未获 Director 批准——不要自行启动共存


---
