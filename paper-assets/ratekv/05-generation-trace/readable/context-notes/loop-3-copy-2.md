# agent / loop_3.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`1191758771e9f2708879.json`](../../sessions/11/1191758771e9f2708879.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-14T11:39:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 westd-37397 的 cuda:0 和 cuda:1，其他卡号必须 push back Director
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，服务器无 .venv
- Mistral 是 genuine negative（profiler zero-signal），不要再尝试优化 Mistral 的 non-uniform allocation
- Δ=0.0000（greedy vs MCKP solver equivalence）已是定论（D028/D030），不要重跑验证
- 投稿目标 EMNLP 2026 ARR May 25（距今 11 天），所有实验必须服务于此 deadline

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397，2× RTX PRO 6000 96GB
- 工作目录：/root/ratekv
- Python：/root/miniconda3/bin/python（conda base 环境）
- 日志位置：/root/ratekv/*.log
- 结果文件：/root/ratekv/*_results.json
- 活跃进程：multi_seed_error_bars（PID 199409，tmux session，cuda 未明确记录）
- W&B：配置在项目 config 中，entity/project 用 load_project_config 获取

### 3. 📊 当前状态
**刚做完**：session-start 初始化 + 派 Worker（worker_analysis_kv_separation_20260514T083637）分析 kv_separation 实验结果。Worker 正在 SSH 读日志、提取指标、更新 registry。

**Registry 状态**：
- `kv_separation`（ANALYZING）— K/V 独立 bit-width 分配 vs joint optimization，plan_014，cuda:1，进程已正常退出，Worker 正在分析
- `multi_seed_error_bars`（RUNNING）— 3 seeds 统计误差条，plan_017，PID 199409，reconcile 确认仍在跑
- `greedy_constrained_ablation`（PREPARING）— 尚未提交

**等待中**：
- Worker `worker_analysis_kv_separation_20260514T083637` 回调 → 需根据 conclusion 走 on-experiment-done 流程（success→更新 report+通知 Director / negative→产 Framing 提案）
- Worker `worker_file_transfer_figures` 和 `worker_util_copy_figures` 仍在运行（figures 传输）
- `multi_seed_error_bars` cron 回调 → 完成后同样需分析

### 4. 📋 待办
- kv_separation Worker 回调到达 → 读 conclusion：success 则更新 report.md + 通知 Director + 铺下一格实验；negative 则产 Framing 提案 + 禁止默跑下一个
- multi_seed_error_bars cron 回调 → spawn Worker 分析 3 seeds 的 mean±std，更新 registry，汇报 Director
- kv_separation 分析完 + multi_seed 完成后 → cuda:0 和 cuda:1 均空闲，立即从 P1 队列铺 plan_018（runtime/latency benchmark）或 greedy_constrained_ablation
- figures Worker 回调 → 确认图表文件就位
- 所有 P1 实验完成 → 评估 Paper Agent 激活时机，向 Director 建议启动论文写作

### 5. 🎯 战略上下文
- 核心 story：cardinality constraint 是方法贡献（Δ=0.0000 证明 greedy=MCKP），heterogeneity 决定 non-uniform 是否值得
- 三模型格局：Qwen（GQA 7:1）strong positive +29.3%，Llama（GQA 4:1）marginal +0.2%，Mistral（GQA 4:1 + SWA）genuine negative -2.7%
- Claim 1/2/3 全部 CONFIRMED（D030），writing_plan.yaml 已审批（D031）
- **易错点**：kv_separation 如果是 negative，不要慌——它是 plan_014 的探索性实验，核心 claims 不依赖它。但仍需走 red-section Framing 提案流程
- **易错点**：multi_seed_error_bars 的 GPU 分配在 registry 里没明确记录，分析时需 SSH 确认实际用了哪张卡
- P1 剩余：plan_018 runtime benchmark 是 reviewer 关心的实用性证据，优先级高于 P2


---
