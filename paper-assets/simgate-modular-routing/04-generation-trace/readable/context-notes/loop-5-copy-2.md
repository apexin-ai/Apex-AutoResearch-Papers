# agent / loop_5.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`66c398ffddfc3ac18b4d.json`](../../sessions/66/66c398ffddfc3ac18b4d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-14T07:09:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格限制 `cuda:0` 和 `cuda:1`（服务器 westb-13313），不得使用其他设备号
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，服务器无 .venv
- AutoDL 网络：提交前必须 `source /etc/network_turbo` + `HF_HOME=/root/autodl-tmp/.hf_cache` + `HF_HUB_OFFLINE=1`（如果模型已下载）
- plan-002 classification head 已被 D022 定性为 **negative baseline**——v6 是最终对照，之后停止迭代，不再尝试修复分类路线
- Qwen3-1.7B LoRA 训练 batch_size 上限 4（32GB 显存，batch_size=32 OOM）

### 2. 🖥️ 基础设施快照
- **服务器**: westb-13313，2× RTX 5090 32GB（cuda:0, cuda:1）
- **工作目录**: `/root/autodl-tmp/simgate-modular-routing`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，非 venv）
- **模型**: `/root/autodl-tmp/models/Qwen/Qwen3-1.7B`（已下载，本地路径）
- **数据**: `results/plan_c/`（11 tasks × labeled_steps.jsonl，共 2040 samples）
- **HF cache**: `/root/autodl-tmp/.hf_cache`
- **W&B**: offline 模式（`WANDB_MODE=offline`）
- **活跃进程**: plan-002-formal-v6（PID 240633，cuda:0，tmux session 未确认——有 worker_diag_plan-002-v6-crash 在诊断可能的崩溃）
- **Cron**: 本 session 无活跃 cron（reconcile_crons 返回 0），**需要为 v6 重新注册监控**

### 3. 📊 当前状态
**刚做完**: plan-002 根因分析全链完成（D020→D021→D022→D023）。确认 class_weights [4.5, 0.5625] + max_grad_norm=1.0 交互导致 v3/v4/v5 全部退化（internal recall=0%）。v5 实证否定 pad_token_id 假说。

**正在进行**:
- `plan-002-formal-v6` (RUNNING, cuda:0, PID 240633): 移除 class_weights 的最终对照实验。**但有 worker_diag_plan-002-v6-crash 正在运行**，暗示 v6 可能经历过一次崩溃——下一轮 BOOT 首要任务是确认 v6 是否仍在运行
- `plan-004-v3` (ALLOCATED, 未提交): implicit router SFT 去掉 class_weights auto 的对照版本，等 GPU1 空闲提交
- 2 个 Worker 运行中: `worker_monitor_v5-early-loss`（可能过时，v5 已结束）、`worker_diag_plan-002-v6-crash`

**已完成的核心实验**:
- plan-012: ✅ 全量 11 tasks/245 eps death decomposition（Δ_full=+29.60, death_fraction=90.41%, r=0.9698）
- plan-011: ✅ keyword baseline 结构性失效（v1 always-det, v2 always-internal）
- plan-004-ablation-b: ✅ implicit router 非退化（internal recall=51.5%），证明信号可提取

**僵尸实验（PREPARING/PENDING but killed）**: plan-001b-gpu1-rebalance, mvp-p1-signal, research-cf-pilot-gpu1——来自早期阶段，registry 里 conclusion=killed 但 status 未清理

### 4. 📋 待办（条件触发式）
- **v6 Worker 回调到达** → 检查 v6 实际运行状态。若已崩溃：读 crash log → 修复 → 用 `submit_on_allocated` 重提交到 cuda:0。若正在运行：注册 cron 监控
- **v6 完成（预计 ~8h）** → 分析 loss 曲线和 internal recall。预期仍退化（D022 判断）→ 确认 classification head = negative baseline → update_registry(conclusion=negative) → 汇报 Director
- **v6 结果确认后** → 立即提交 plan-004-v3 到 cuda:0（implicit router 无 class_weights 对照）；同时 cuda:1 提交 plan-004 ablation 或 plan-003
- **plan-004-v3 + plan-002-v6 都完成** → 汇总 explicit vs implicit router 对比表 → 更新 paper_framing.md C2 段 → 启动论文写作
- **DDL 压力（May 25，11 天）** → 实验预计 May 16-17 全部完成，写作窗口 May 17-24。优先级：plan-002-v6 > plan-004-v3 > plan-003 > plan-005 > paper writing

### 5. 🎯 战略上下文
**核心结论链**:
- D013: framing pivot 到 "death avoidance dominates + counterfactual methodology"（非 router 架构贡献）
- D018/D019: C1 = "~90% death avoidance"（episode-weighted ~94.5%，per-task 10/11 death-dominated）
- D022: classification head = negative baseline，implicit router (plan-004) 是唯一成功提取信号的路线
- D023: class_weights + gradient clipping 交互是 plan-002 退化根因（非 pad_token_id）

**易错点**:
- **不要再尝试修复 plan-002 分类路线**——v6 之后停止迭代（D022 硬约束）
- **plan-004 implicit router 才是正面证据**——论文中 explicit router 是 negative baseline，implicit 是 positive
- **find-non-living-thing 是正面案例不是异常**——零死亡 task 仍有 Δ=+9.58，证明 routing 价值超越 death avoidance
- **dryrun 的 5880 samples ≠ plan_c 的 2040 samples**——数据源不同，不要混淆
- **D022 提到 dryrun 也退化（internal recall=0）**——这意味着即使去掉 class_weights，classification head 仍可能退化。v6 结果很可能是 negative，准备好按 negative 路径处理
- **keyword baseline (plan-011) 结构性失效**——这是论文正面证据（learned routing 不可被简单规则替代），不是问题


---
