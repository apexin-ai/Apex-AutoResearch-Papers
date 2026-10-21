# agent / loop_21.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_21.md`
- **Structured JSON:** [`c6742487588f52201a81.json`](../../sessions/c6/c6742487588f52201a81.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: idle_timeout
updated: '2026-05-17T23:40:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 bjb1-45299 的 cuda:0 和 cuda:1（gpu_ids 白名单）
- submit_training_job 命令必须自带环境激活：`source /root/miniconda3/bin/activate && ...`（不能假设 .venv 存在）
- GPU 编号脚本内始终从 0 开始（框架自动映射物理 GPU）
- DMC 实验必须用 `--configs dmc_proprio`（不是 dmc_vision），且 `--compile False`（torch.compile inductor crash，D082 教训）
- Negative 结果禁止默默跑下一个实验——必须先产出 Framing 提案给 Director 审批

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299，工作目录 `/root/autodl-tmp/event-gated-adaptive-horizon`
- Python：`/root/miniconda3/bin/python`，预置镜像 `aml-train`
- 运行日志目录：`~/runs/event-gated-adaptive-horizon/`
- W&B 数据可用（项目名待 Worker 确认，可能含 "dreamerv3" 或 "event-gated"）
- 磁盘：`/usr/bin/nvidia-smi` 分区 399G/439G 可用（5%），`/autodl-pub/data` 5.7T/10T
- 活跃进程：exp_023a_cheetah_baseline_s0 (PID 683708, cuda:0, RUNNING)
- Cron 监控：exp_023a 有活跃 cron（reconcile 确认 still running）

### 3. 📊 当前状态
**刚发生的事**：exp_023b_cheetah_baseline_s1 完成（ANALYZING），我已派 Worker `worker_analysis_exp_023b_cheetah_baseline_s1_20260517T192705` 分析结果（SSH 读日志 + W&B 指标），Worker 尚未回调。

**Registry 状态**：
- exp_023a_cheetah_baseline_s0：RUNNING (cuda:0, PID 683708)——Cheetah baseline seed=0，ETA ~3h（ROADMAP 说 @85K）
- exp_023b_cheetah_baseline_s1：ANALYZING——等 Worker 回调完成分析
- exp_021_full_sgs_cheetah_s1：QUEUED——等 GPU 释放后提交
- 总计：56 实验，success 17 / negative 14 / failed 6 / killed 16

**等待中**：
- Worker 回调：exp_023b 分析 Worker
- Cron 回调：exp_023a 完成
- Director 决策：用户跨架构方案（待回复）

### 4. 📋 待办
- exp_023b Worker 回调到达 → 读分析结果 → update_registry(status=DONE, conclusion, metrics, checkpoint_path, log_path) → 刷新 report.md → 汇报 Director
- exp_023a cron 回调到达 → 派 Worker 分析 → 同上流程
- 023a + 023b 都 DONE 后 → cuda:1 空出 → 提交 exp_021_full_sgs_cheetah_s1（已 QUEUED）
- 023a + 023b baseline 指标就绪 → 计算 Cheetah NVE 归一化基准（两个 seed 取均值）→ 后续 Cheetah CIVO trigger 实验的 NVE 基准
- 所有 Cheetah 数据就绪 → 同步到论文 Table 1 / detector validation → submit_paper_to_review

### 5. 🎯 战略上下文
- **目标**：CoRL 2026，DDL 2026-05-29（剩 12 天）
- **论文定位**：CIVO 诊断论文 + 在线检测工具。核心因果链：Trained dt_emb → obs decoder gradient → RSSM fidelity gap → reward bias → critic overestimation → collapse
- **关键 Claims**：C2（Trained dt_emb → CIVO）最强，AUROC=0.926；C7 Detector TPR=100% FPR=25%；C5 SGS intervention 50% prevention rate 是弱点
- **Cheetah baseline 的意义**：第三个环境（Walker + PickCube 已有），用于 cross-environment validation。023a/023b 建立归一化基准后，需要跑 Cheetah CIVO trigger 实验来验证 CIVO 跨环境一致性
- **易错点**：
  - 梯度分解数据已修正（D086）：Reward=49%, Obs=16.3%, KL=34.7%，不要引用旧数据（93% obs/0% reward）
  - Detector FPR 已统一为 2/8=25%（不是 2/7），n=11（D083 撤回了 PickCube 019b 的 TP 结论，是 TN）
  - NVE 口径统一为 12-exp 全集 AUROC=0.926（不是 0.933，D084）
  - exp_022 curriculum 未激活 gate（D081 撤回 D080），022b 才是有效实验
  - Reviewer 预期评分 5-6/10 borderline，提升路径：叙事精简 + TAWM hook + detector 实用性包装


---
