# agent / loop_9.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`3cf1cb7c2a5533ea3779.json`](../../sessions/3c/3cf1cb7c2a5533ea3779.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-15T01:11:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 bjb1-45299 只有 2 张 GPU（cuda:0 + cuda:1），gpu_ids=[0,1]。不要用其他 GPU 编号
- submit_training_job 的 command 必须用 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py ..."`，不能省略环境变量
- 训练命令中 `--device cuda:0` 始终固定（框架通过 CUDA_VISIBLE_DEVICES 映射物理 GPU），不要写 `--device cuda:1`
- 008e_v3 的 dt_embedding 实际是 **trained** 的（D033 确认），不要假设是 untrained。关键变量是 `--gate_fixed_dt 1`（imagination dt=1），不是 embedding 训练状态
- nve>1.5x 诊断仅在 **35K+ steps** 有效，25K 处 baseline v/e 太低会产生 false positive
- CoRL DDL 2026-05-29，距今 **14 天**

### 2. 🖥️ 基础设施快照
- **服务器**：bjb1-45299（本地机器，非 AutoDL）
- **工作目录**：`/root/autodl-tmp/event-gated-adaptive-horizon`
- **Python**：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- **代码 commit**：`09876d7080affdb0fb329e24753a46d998da9d8e`
- **logdir 根目录**：`/root/autodl-tmp/event-gated-adaptive-horizon/logdir/`
- **GPU**：RTX PRO 6000 × 2（cuda:0 + cuda:1）
- **活跃进程**：
  - exp_009a_baseline_walker_s2: PID 142508, cuda:0, ~336K/500K steps, tmux log `~/runs/event-gated-adaptive-horizon/exp_009a_baseline_walker_s2.log`
  - exp_008e_v3_walker_s2: PID 43437, cuda:1, 0-105K steps（刚启动 ~2026-05-15T00:46），tmux log `~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s2.log`
- **Cron 监控**：两个 RUNNING 实验都有 cron 监控（需 `reconcile_crons` 确认）
- **监控要点**：读 `logdir/*/metrics.jsonl` 获取真实进度，不依赖 tmux log（有 buffering 延迟）

### 3. 📊 当前状态
**刚完成**：008e_v3_walker_s1（C6 crown jewel seed 1，success: eval=869.9@105K, nve=0.527x，与 seed 0 几乎完全一致）。提交了 008e_v3_walker_s2（seed 2）到 cuda:1。

**RUNNING**：
- `exp_009a_baseline_walker_s2` — cuda:0, ~336K/500K, baseline seed 2, eval stable ~920, v/e 0.699（healthy）。预计还需 ~22h
- `exp_008e_v3_walker_s2` — cuda:1, 0→105K, C6 crown jewel seed 2。预计 ~10-12h

**QUEUED**（按排期顺序）：
- cuda:0: 009a → **009d**（baseline s1）→ **010a**（cheetah baseline s1）
- cuda:1: 008e_v3_s2 → **009e**（008d s1）→ **009f**（008f s1）→ 009c extension(200K) → plan_060

**等待中**：
- 无 pending Worker 回调
- Dream 审稿结果（dream_20260514T062606）未见明确完成/反馈记录，需确认
- Cheetah Run / Cartpole Swingup 实验尚未启动，只有 Walker Walk 数据

### 4. 📋 待办（条件触发式）
- **009a cron 回调（进程结束）** → spawn Worker 提取 500K 全程 metrics + v/e 曲线 → 更新 registry（conclusion）→ 立即提交 009d（baseline s1）到 cuda:0
- **008e_v3_s2 cron 回调（进程结束）** → spawn Worker 提取 metrics → 若 eval≥800 且 nve<1.0x → success，C6 三 seed 全部通过 → 立即提交 009e（008d s1）到 cuda:1 → 汇报 Director C6 closure
- **008e_v3_s2 eval<800 或 nve>1.5x** → negative，C6 需要重新评估 → Framing 调整提案
- **009d 完成** → 提交 010a（cheetah baseline s1）到 cuda:0（首个跨环境实验）
- **009e 完成** → 提交 009f（008f s1）到 cuda:1
- **所有 Walker Walk P0 完成** → 汇报 Director，请求是否扩 GPU 加速 Cheetah/Cartpole 验证（剩余 ~130 GPU·h P0 实验 vs ~12 天 DDL，2 张卡勉强但紧张）

### 5. 🎯 战略上下文
**核心叙事**（Narrative B+）：Diagnostic Analysis — trained dt_embedding → delusional critic → collapse。因果链已闭合（D028），nve>1.5x 是 4/4 完美分类的诊断标记（D032）。C6 mitigation（dt=1 imagination）是 crown jewel（95% baseline，零成本策略改变）。

**决策链关键节点**：
- D028: C2 因果归因确认
- D029: Dream 审稿后调整——3 seeds 不扩 5, 008e_v3 定位为 mitigation
- D031: Option A narrative（机制+陷阱+正确修复），C6 升为 crown jewel
- D032: Collapse is stochastic, nve>1.5x is reliable diagnostic marker
- D033: 008e_v3 的 dt_emb 是 trained 的，关键变量是 imagination dt=1

**易错点**：
1. **不要把 008f 当推荐方案**——008f 去掉 dt_emb 破坏 reward prediction（75x baseline MAE），009c seed 2 已 negative。推荐方案是 008e_v3（C6）
2. **不要混淆 seed 编号和配置编号**——008d seed 0 = exp_008d, seed 1 = exp_009e, seed 2 = exp_009b。008f seed 0 = exp_008f, seed 1 = exp_009f, seed 2 = exp_009c
3. **GPU 瓶颈是 wall time**——P0 还剩 ~130 GPU·h（Cheetah + Cartpole + Walker seeds），2 张卡 = ~65h wall = ~2.7 天，加上 Walker 排队实验 ~3.5 天。DDL 前应该能完成 P0 但没余量，任何失败重跑都吃紧
4. **Collapse 是 stochastic 的**——不能 claim "trained dt_emb 必然导致 collapse"，只能说 "reliably triggers pathological nve>1.5x, creating high collapse risk"
5. **report.md 的趋势统计**：成功 6 / 负向 9 / 失败 1 / 共 23——负向多是因为早期 event-gated 迭代（exp_002-005）和 pivot 过程。当前 diagnostic analysis framing 下的实验成功率高


---
