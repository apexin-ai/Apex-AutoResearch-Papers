# agent / loop_4.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`190346a23d2056cd416d.json`](../../sessions/19/190346a23d2056cd416d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-15T04:22:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-19828 cuda:0 和 cuda:1，**只有这两张**，禁止用其他设备号
- submit_on_allocated 的 command 必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不能假设 .venv 存在
- α-sweep 实验的 output_dir 必须严格为 `results/alpha_sweep/a{NNN}_s{seed}`，分析脚本依赖此路径模式
- Perplexity 通道已确认为伪回归（D017/D018），**不要**把 perplexity drift 作为 canary 有效性的证据
- TY Granger 已降级为辅助指标（D015），核心分析框架是 cross-corr + permutation Granger（差分版）+ BH FDR

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828，工作目录 `/root/autodl-tmp/distrib_canary_collapse/`
- Python：`/root/miniconda3/bin/python`（conda base 环境），激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：EleutherAI/pythia-410m，HF cache `/root/autodl-tmp/.hf_cache`
- 数据：`/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k`（5000 条）
- 活跃进程：
  - `plan_006_s42`：PID 68368，tmux=plan_006_s42，cuda:0，20-gen extended run（预估 ~8.7h）
  - `alpha_sweep_a050_s42`：PID 73737，tmux=alpha_sweep_a050_s42，cuda:1，刚提交
- Cron 监控：plan_006_s42 和 alpha_sweep_a050_s42 均已注册

### 3. 📊 当前状态
**刚做完**：收到 alpha_sweep_a025_s42_v3 (α=0.25) 完成回调，已派 Worker `worker_analysis_alpha_sweep_a025_v3_20260515T012002` 分析结果（读日志+指标+对比 baseline）。同时提交了 alpha_sweep_a050_s42 到 cuda:1。

**Registry 关键状态**：
- `alpha_sweep_a025_s42_v3` — ANALYZING，等 Worker 分析完成后转 DONE
- `alpha_sweep_a050_s42` — RUNNING，cuda:1，PID 73737
- `plan_006_s42` — RUNNING，cuda:0，PID 68368（20-gen extended）
- PREPARING 队列：a010, a060, a075, plan_006_s43（等 GPU 空出）

**等待中**：
- Worker `worker_analysis_alpha_sweep_a025_v3_20260515T012002` 回调 → 需更新 registry + 汇报 Director
- plan_006_s42 cron 回调（预计还需数小时）
- alpha_sweep_a050_s42 cron 回调

### 4. 📋 待办
- a025_v3 Worker 分析回调到达 → 读 conclusion/metrics → update_registry(status=DONE) → 更新 report.md → 汇报 Director（带 [资源] 行 + 与 α=0.00 对比 + α-sweep 进度）
- a050_s42 cron 回调（完成）→ 派 Worker 分析 → 对比 a000/a025 → 更新 registry → 汇报 Director
- plan_006_s42 cron 回调（完成）→ 派 Worker 分析 20-gen extended 结果（重点：ECE 是否确认升级为 co-primary canary）
- 每次 cuda:1 空出 → 从 PREPARING 队列中按优先级提交下一个 α 点（优先序：a075 > a060 > a010）
- α-sweep 首批 6 点全完成 → 启动 plan_002 Phase 2（pooled panel + permutation Granger）

### 5. 🎯 战略上下文
**项目核心**：映射迭代合成数据训练中 canary 指标的可预测性边界。三个 claim：(1) token_entropy 领先 diversity collapse 1-2 代（Granger-causal），ECE 为 conditional secondary canary；(2) 可预测性 regime-dependent（α-sweep）；(3) 方法论陷阱——分析方法选择决定结论（5-method ablation 已完成）。

**关键决策链**：D013 推翻 TY gold standard → D015 TY 降级 → D017/D018 perplexity 确认伪回归 → D019 ECE 升级为 co-primary → D020 Claim 1 措辞升级为 Granger-causal precedence。

**最容易判断错的事**：
- α=0.00（纯真实数据）也有 drift——这不是 bug，是 fine-tuning 本身的 distributional shift。α-sweep 的 claim 是 drift 幅度随 α 单调递增，不是 α=0 无 drift
- 5-method ablation 的 spurious rate 排序（naive 100% > diff 88% > threshold 56% > permG 38% > TY 25%）是 Claim 3 的核心证据，但 TY 25% 不代表 TY 最好——TY 在 T=10 时 power 只有 5-20%，低 spurious rate 是因为 underpowered
- plan_006 是 20-gen extended run（α=1.0），目标已从 "验证 perplexity lead" 改为 "ECE 在长序列下是否稳定升级为 co-primary"（D018/D019 后调整）


---
