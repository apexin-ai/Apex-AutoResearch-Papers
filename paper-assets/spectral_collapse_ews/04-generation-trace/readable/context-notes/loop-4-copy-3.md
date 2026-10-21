# reviewer / loop_4.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`2facd289e3445d4e87e6.json`](../../sessions/2f/2facd289e3445d4e87e6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-17T17:03:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（rtx6000-diagprobe 的两张 RTX PRO 6000, 98GB）。项目无其他 GPU 分配。
- exp_005 (PID 116947) 在 cuda:1 上通过 nohup 启动（非 tmux/sentinel），监控系统会误报 "process dead"。已发生一次 false positive failure（cron:on_failed 触发）。**不要因为监控告警就重启 cuda:1 上的进程——先 /proc/{PID}/status 确认存活。**
- D015 确定论文主参数 k=10（不是 k=20）。exp_005 (k=20) 是 sensitivity data，不是主结果。新的 exp_006 (k=10) 才是论文主表的 adaptive 条件。
- D004：collapse 从 Gen 1 开始度量（不是 Gen 0）。Gen 0→1 的 eff_rank 上升是 pretrained decompression，不是 collapse 反转。

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe (root)，代码 `/root/spectral_collapse_ews`
- Python：`/root/miniconda3/bin/python`（conda base env）
- Checkpoints：`/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/`（数据盘 250G，49% used）
- Root 分区：30G，83% used（5.2G free）——exp_002 曾因此崩溃，需持续监控
- 数据：`/root/spectral_collapse_ews/data/`（train_real_50k.pt, eval_5k.pt, spectral_1k.pt）
- 活跃进程：
  - exp_001: PID 59365, tmux=exp_001_gen4, cuda:0, Phase 0 Gen 10 生成中（30720/50000 samples as of ~16:10 UTC）
  - exp_005: PID 116947, **nohup**（无 tmux/sentinel）, cuda:1, Phase 1 adaptive k=20 s42, Gen 2 完成 → Gen 3 训练中
- Log: exp_005 未设 PYTHONUNBUFFERED，stdout 全缓冲，只能看 stderr（padding warnings）。通过 checkpoint 目录和 results JSON 判断进度。
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/`

### 3. 📊 当前状态
**我刚完成**：ROADMAP 大更新审查 + exp_005 Gen 2 数据独立核实 + D014 dry-run 战略评估（已提交 3 份报告给 Director）。

**Registry**：
- exp_001 RUNNING — Phase 0 410M Gen 10/10 生成中，即将完成（~1-2h）
- exp_005 RUNNING — Phase 1 adaptive k=20 s42, Gen 2 完成, Gen 3 训练中。Gen 2 log_det=2395.23（延迟 decompression 确认）
- exp_004 PREPARING — fixed_mix s42，等 cuda:0 释放
- exp_006 未创建 — adaptive k=10 s42（D015 论文主版本），等 cuda:1 释放

**等待中**：
- exp_001 完成 → worker 回调
- exp_005 Gen 3 结果 → D014 decision gate（但已降为 sensitivity，实际影响有限）
- Director 对我三份报告的响应

### 4. 📋 待办（条件触发式）
- exp_001 完成通知 → 审查 Gen 10 完整数据，验证 Phase 0 10 代趋势一致性 + HellaSwag 全程
- exp_005 Gen 3 结果出现（看 results JSON 或 checkpoint） → 核查 controller ratio（预测=0.50，因 Gen 2 decompression 使 delta 为负）
- exp_004 启动通知 → 核查 GPU 设备号 + 命令参数（seed=42, ratio=0.50, 10 gens）
- exp_006 启动通知 → 核查 k=10（非 k=20）, tau=0.002, signal=log_det, signal_mode=per_gen
- 任何实验 Gen 5+ 数据 → 重新评估信号衰减悖论的实际影响，与 Phase 0 dry-run 预测对比
- 论文章节审查请求 → 合规检查（是否读了 red-section skill）+ claim-evidence 对齐

### 5. 🎯 战略上下文
**决策链**：D001(MVP) → D004(Gen 1 baseline) → D009(Phase 0 PASS) → D010(log_det signal) → D011(3-layer bug) → D012(k=20) → D013(claim pivot: EWS detection 为主, controller 为 PoC) → D015(k=10 for paper)

**核心结论**：Phase 0 数据极强（8 代单调 collapse，5 指标一致）。Controller 是弱项——信号衰减悖论（混入 real data → collapse 信号减弱 → controller 不响应）是 fundamental limitation。论文主线已 pivot 到 spectral characterization + EWS detection。

**最容易判断错的事**：
1. **D014 cumulative 校准数字是错的**（Gen 5 delta=0.042 实际应为 0，用了错误的 Gen 1 baseline 而非代码实际的 Gen 0 baseline）。如果有人引用这些数字做决策，需要纠正。
2. **exp_005 不是论文主结果**（是 sensitivity）。论文主 adaptive 是 exp_006 (k=10)，尚未创建。不要把 exp_005 数据当主表数据。
3. **Phase 1 有延迟 decompression**：Gen 1→2 log_det 上升 +28.77（Phase 0 同期 Gen 0→1 上升 +98）。这意味着 per-gen controller 在 Phase 1 中触发时间比 Phase 0 dry-run 晚 1-2 代。不要用 Phase 0 dry-run 的 "Gen 5 首次触发" 预测 Phase 1 的行为。
4. **Root 分区 83%**——两个实验同时生成数据可能触发磁盘满。exp_002 就是这样死的。


---
