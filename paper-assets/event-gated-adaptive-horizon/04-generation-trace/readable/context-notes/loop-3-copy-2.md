# agent / loop_3.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`0001acfe0e7883ffb2b8.json`](../../sessions/00/0001acfe0e7883ffb2b8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-14T00:43:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**仅 bjb1-45299 的 cuda:0 + cuda:1**（config gpu_ids）。Director 指定白名单外 GPU 必须 push back
- **禁止 hard categorical gate**（含 K=2 Gumbel-Softmax）——三轮实验确认结构性失败，memory.md 明确记录。Pivot 用 Bernoulli ST 或 continuous sigmoid
- submit 命令必须 `bash -c "..."` 包装 + `--compile False` + 环境三件套（`LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6`, `MUJOCO_GL=osmesa`, `PYOPENGL_PLATFORM=osmesa`）
- exp_007 (dt=4) 已由 D013 定性为 actor-critic credit assignment 崩塌，**不要再给 dt=4 机会**——model_loss 正常但 actor_loss→0、entropy→random，根因是动作时间分辨率不足
- Metrics 录入必须核实 metrics.jsonl 原始数据（exp_005 误录事故教训）
- Worker 声称"已更新 registry"不可信，Main Agent 必须回调后重新 read_registry 验证

### 2. 🖥️ 基础设施快照
- **服务器**：bjb1-45299（AutoDL RTX PRO 6000 × 2, 98GB each）
- **工作目录**：`/root/autodl-tmp/event-gated-adaptive-horizon`
- **Python**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（conda 环境，非 venv）
- **代码 commit**：`6ef8646d807cd10ce0c88e10a7e943211e7fc44c`
- **Baseline checkpoint**：`/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1`（exp_001, 512K steps, eval_return ~950.9）
- **活跃进程**：
  - exp_006_fixed_dt2: PID 85029, cuda:0, logdir `fixed_dt2_v1_s1`, cron 监控中（reconcile 确认 running）
  - exp_007_fixed_dt4: PID 90354, cuda:1, logdir `fixed_dt4_v2_s1`, cron 监控中（第 2 次重试）
- **活跃 Worker**：`worker_monitor_exp_006_check_20260514T004155`（monitor 任务，running）
- **GPU 内存**：单进程仅占 ~4GB/98GB，单 GPU 可跑 8-10 并发（D012 确认）
- **累计 GPU·h**：~44h（已超 MVP 30h 预算，用户已确认扩容）

### 3. 📊 当前状态
**刚完成**：exp_005 negative 分析 + exp_007 dt=4 诊断（D013 根因定位：credit assignment 崩塌，非模型能力问题）+ 三档 claim 结构确立（D012）

**Registry 状态**：
| exp_id | status | 摘要 |
|--------|--------|------|
| exp_006_fixed_dt2 | RUNNING | cuda:0, step 45K/150K, eval_return 477 (~93% baseline)，跟踪基线 ±10%，关键诊断实验 |
| exp_007_fixed_dt4 | RUNNING | cuda:1, step 35K, eval_return 127 (33% baseline)，已由 D013 定性失败，可 kill 释放 GPU |
| exp_005 | DONE/negative | hard Gumbel gate 结构性失败 |
| exp_001 | DONE/success | baseline ~950.9 |
| exp_002-004 | DONE/negative or failed | 各类 bug + gate 失败 |

**等待中**：
- exp_006 cron 回调（预计还需 ~3-4h 跑到 150K）
- Worker `worker_monitor_exp_006_check` 正在 running
- 未派 Worker 预备 Bernoulli ST 代码（ROADMAP 提到"预备中"但本 session 未实际执行）

### 4. 📋 待办（条件触发式）
- **exp_007 已可 kill** → kill_job 释放 cuda:1 → 立即用于 Bernoulli ST 实验或 multi-seed dt=2
- **exp_006 到 150K（cron 回调）** → 若 return ≥80% baseline 且正趋势 → D009 分支确认"问题在 learned gate 动态选择"→ 立即启动 Bernoulli ST gate 实验（D011 方案 a）
- **exp_006 到 150K 且 return <80%** → variable-rate imagination 本身有害 → 需根本架构改变（multi-scale WM / options），向 Director 汇报 pivot
- **Bernoulli ST 代码就绪** → 在 cuda:1 上 dry-run → 提交审批 → seed=1 先跑，同时铺 seed=2,3（CoRL 最低 3 seeds）
- **Bernoulli ST 成功（B 档 claim）** → 铺 4-6 个 DMC 环境（Walker Walk / Cheetah Run / Hopper / Cartpole / Reacher / Finger）× 3 seeds → 单 GPU 8-10 并发可大幅加速
- **Bernoulli ST > fixed dt=2（C 档 claim）** → 最强 CoRL 投稿，加 ablation（gate scale schedule / entropy bonus / max_dt）

### 5. 🎯 战略上下文
- **CoRL DDL 2026-05-29（剩 15 天）**，当前仍在诊断阶段，时间极紧
- **三档 claim 结构（D012）**：A 档=仅诊断发现（workshop 级）/ B 档=Bernoulli ST 成功（CoRL 可投）/ C 档=learned gate > fixed dt（最强 CoRL）。当前距 B 档差 Bernoulli ST 一步
- **dt=2 sweet spot 已确立**：dt=2 跟踪 baseline ±10%（exp_006），dt=4 credit assignment 崩塌（D013），dt=1 是 baseline。这是论文 discussion 的重要论点
- **最易判断错的事**：(1) exp_006@35K 的 485 vs baseline 389 看起来"超越基线"，实际是 baseline 临时回调的假象，正确表述是"跟踪基线 ±10%"（D012 修正）；(2) K=2 Gumbel-Softmax 看起来是"最简单的 binary gate"但本质仍是 hard categorical，必须用 Bernoulli ST 替代（D011）
- **最大加速杠杆**：单 GPU 8-10 并发能力尚未利用，一旦 Bernoulli ST 代码就绪，可同时铺 multi-env × multi-seed，从串行变并行
- **决策链**：D009(hard gate 失败) → D010(K=2 pivot) → D011(修正为 Bernoulli ST) → D012(三档 claim + 并行策略) → D013(dt=4 根因)


---
