# reviewer / loop_2.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`a9a4e258192cc03b8009.json`](../../sessions/a9/a9a4e258192cc03b8009.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-17T07:35:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- exp_001 只能用 cuda:0（PID 59365），exp_003 只能用 cuda:1（PID 88161）。exp_004 等 cuda:0 空出后启动。
- exp_003 的 registry command 缺少 `CUDA_VISIBLE_DEVICES=1`，实际通过 tmux 环境变量设置。代码里 `--gpu` 默认 0，靠 CUDA_VISIBLE_DEVICES=1 映射到物理 GPU 1。复现时必须加这个环境变量。
- 远程代码在 `/root/spectral_collapse_ews`，checkpoint 在 `/root/autodl-tmp/spectral_collapse_ews/`（数据盘）。根分区只有 30GB（~84% 满），之前 1B 实验因根分区满而崩溃（exp_002）。不要往根分区写大文件。
- Phase 0 results JSON 路径：`/root/spectral_collapse_ews/results/phase0_results.json`（非 autodl-tmp）

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe（ssh account: root），2× NVIDIA RTX PRO 6000 Blackwell 98GB
- 工作目录：`/root/spectral_collapse_ews`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 数据：`/root/spectral_collapse_ews/data/`（50K train + 5K eval + 1K spectral probe）
- Checkpoint 盘：`/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/`
- 活跃进程：
  - exp_001: PID 59365, tmux=exp_001_gen4, cuda:0, 65.9GB — Phase 0 Gen 7/10 生成中
  - exp_003: PID 88161 (tmux PID 88156), tmux=exp_003, cuda:1, 19GB — Phase 1 adaptive Gen 1 生成中（~21K/50K）
- 无 W&B 配置，无 cron 任务

### 3. 📊 当前状态
**刚完成**：D010 术语改名全文跨章一致性审查。abstract/intro/conclusion/method/experiments 均已审查。intro 已大幅重写（controller 信号从 eff_rank 改为 spectral log-volume，contributions 重写为 3 条含 EWS claim）。conclusion 的 contributions 仍未与 intro 同步（warning 已报 Director）。

**Registry 状态**：
- exp_001 RUNNING — Phase 0 pure collapse 410M, Gen 7/10 生成中（Gen 6 完成：eff_rank=473.00, log_det=2335.17, ppl=30.91）
- exp_002 DONE — 1B pilot Gen 0-3, log_det 领先 eff_rank 已验证
- exp_003 RUNNING — Phase 1 adaptive seed42, D010 版 log_det+τ=0.005, Gen 1 生成中（21K/50K）
- exp_004 PREPARING — Phase 1 fixed_mix seed42, 等 cuda:0

**等待中**：conclusion contribution 同步修正的 worker 回调

### 4. 📋 待办
- exp_001 Gen 7-10 完成 → 核实全量指标，计算 go/no-go condition 2 加速比（Gen 6-10 vs Gen 1-5），更新 Table 1 到 Gen 10
- exp_003 Gen 1 结果出来 → 确认 controller 第一次 update 返回的 mix_ratio（应为 ~0.56 based on budget spread，delta=0）
- exp_003 Gen 3+ 结果出来 → 验证 controller 是否实际触发（delta > τ=0.005），如果 mix_ratio 仍为 base rate → CRITICAL
- exp_004 启动 → L1 GPU 边界检查（必须在 cuda:0），核实 PID 和 CUDA_VISIBLE_DEVICES
- conclusion contributions 修正 worker 回来 → 核对是否与 intro 的 3 条 contribution 一致
- distinct-4 在 Gen 7+ 如果继续上升 → flag paper claim "monotonic decline" 需改措辞

### 5. 🎯 战略上下文
- **决策链**：D001(MVP方案) → D003(用户坚持May25 DDL) → D004(baseline改Gen1) → D009(go/no-go PASS) → D010(eff_rank→log_det, τ 0.02→0.005，因为旧参数控制器永远不触发)
- **核心风险**：Phase 1 adaptive vs fixed_mix 的对比是论文中心 claim，目前零数据。exp_003 刚开始 Gen 1。如果 adaptive 没有显著优于 fixed_mix，整篇论文需要 pivot。
- **最容易判断错的事**：
  1. Controller 触发时机——我的 Phase 0 模拟预测 Gen 3 data 输入时首次触发（delta=0.0054>0.005），但 Phase 1 adaptive 有真实数据注入，spectral 轨迹不同于 Phase 0 纯合成。不要用 Phase 0 数据直接预判 Phase 1 触发行为，等实际 results JSON 的 mix_ratio 字段。
  2. Pipeline 不打印 controller 内部状态（delta, r_raw）——只能从 results JSON 的 per-gen mix_ratio 间接验证。需要从 spectral metrics 反推 delta 来审计。
  3. exp_001 的 65.9GB 显存看似异常但运行正常——是 PyTorch CUDA 缓存累积，不是内存泄漏。
  4. "spectral log-volume" 是新统一术语（替代旧的 "log-determinant"）。全文 grep "log-determinant" 应为零。experiments.tex 的 `$\tfrac{1}{2}\log\det(Z^T Z)$` 是数学注释不是旧术语。


---
