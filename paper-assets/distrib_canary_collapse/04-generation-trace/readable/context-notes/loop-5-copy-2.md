# agent / loop_5.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`bb768e476934a0c1e3b7.json`](../../sessions/bb/bb768e476934a0c1e3b7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-15T08:47:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 westd-19828 cuda:0 / cuda:1，禁止用其他 GPU
- AutoDL 实例已退役，所有实验只在 westd-19828 上跑
- α-sweep 训练命令必须包含 `export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com`
- conda 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要创建 venv
- α=0.50 的 Granger 结果（FDR 后不显著）已报告 Director 并写入 D025，不要在没有新证据的情况下推翻
- 非单调 dose-response（α=0.50 d1_drift < α=0.25）已记录为 D024，这是 feature 不是 bug

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828，account: root
- 工作目录：/root/autodl-tmp/distrib_canary_collapse
- Python：/root/miniconda3/bin/python（conda base 环境）
- 数据：data/wikitext103_5k（5k 样本，α-sweep 用）、data/wikitext103（完整，plan_006 用）
- HF cache：/root/autodl-tmp/.hf_cache
- 模型：EleutherAI/pythia-410m（所有实验统一）
- 活跃进程：
  - plan_006_s42: PID 68368, tmux=plan_006_s42, cuda:0, 20gen α=1.0（进度 12/20）
  - alpha_sweep_a075_s42: PID 89753, tmux=alpha_sweep_a075_s42, cuda:1, 刚启动
- 两个 cron 监控上述实验

### 3. 📊 当前状态
**刚做完**：收到 alpha_sweep_a050_s42 完成回调（ANALYZING），派了分析 Worker（worker_analysis_alpha_sweep_a050_final_20260515T054443），同时在 cuda:1 启动了 α=0.75。已向 Director 发初步汇报。

**等待中**：
- Worker 回调：a050 分析 Worker 正在提取 gen10 指标 + Granger 确认 → 回调后需更新 registry（conclusion/metrics/checkpoint_path）、刷新 report.md、发 Director 完整报告
- Cron：plan_006_s42（~还需 8 gen × ~30min/gen ≈ 4h）、alpha_sweep_a075_s42（~4.5h）

**Registry 关键状态**：
- alpha_sweep_a050_s42: ANALYZING（等 Worker 完成 → DONE）
- alpha_sweep_a075_s42: RUNNING（cuda:1, pivotal boundary）
- plan_006_s42: RUNNING（cuda:0, 12/20 gen）
- alpha_sweep_a010_s42: QUEUED（等 GPU 释放）
- alpha_sweep_a060_s42: PREPARING（等 GPU 释放）

### 4. 📋 待办
- a050 分析 Worker 回调 → 读 Worker 产出 → update_registry(conclusion, metrics, checkpoint_path) → 刷新 report.md → 向 Director 发完整分析（含 cross-alpha 对比表 + 文献联动 + 实验计划反思）
- alpha_sweep_a075_s42 cron 回调 → 这是 Claim 1 的 pivotal boundary，分析优先级最高：Granger 显著→boundary 在 0.50-0.75 之间；不显著→boundary 在 0.75-1.0 之间，Claim 1 scope 进一步收窄
- plan_006_s42 cron 回调（20gen α=1.0）→ 验证 T=20 下 diversity lead robustness + ECE 升级判定
- a075 或 plan_006 完成释放 GPU → 立即启动 alpha_sweep_a010_s42（QUEUED，最低 α 边界）
- a010 完成后 → alpha_sweep_a060_s42（finer resolution）

### 5. 🎯 战略上下文
**核心 narrative**：三个 claim 并行——(1) token_entropy Granger-leads diversity collapse（仅 α=1.0 稳固 24/24），(2) 可检测性 regime-dependent（非单调 dose-response），(3) 分析方法选择决定结论（naive 100% vs strict 0% at α=0.50）。目标 AAAI 2027。

**决策链关键**：D025 确认 Claim 1 只在 α=1.0 成立，α=0.50 strict 全归零。D024 发现非单调性。α=0.75 是 pivotal——决定 boundary 位置和 Claim 1 最终 scope。

**易错点**：
- α=0.50 的 d1_drift（-36.6%）弱于 α=0.25（-40.3%），这是非单调现象不是数据错误。不要试图"修复"
- MVP 阶段 α=1.0 的 Granger 24/24 是在 4 seed × 6 canary→diversity pair 上统计的，不是单个 p 值
- gen 编号：num_generations=10 意味着 gen0 到 gen10（11 个点），不是 gen0 到 gen9
- a050 registry 里的 metrics 是 gen9 不是 gen10——Worker 应该补上 gen10 final 数据
- cross-alpha 对比必须用相同方法（差分 permutation Granger），不要混用不同统计方法的结果


---
