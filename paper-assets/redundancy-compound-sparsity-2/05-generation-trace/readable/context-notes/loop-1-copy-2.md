# agent / loop_1.md

**redundancy compound sparsity 2** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`96b0973efb2700536f42.json`](../../sessions/96/96b0973efb2700536f42.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-12T14:18:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-16980 的 cuda:0 和 cuda:1（gpu_ids 白名单）
- mvp_001 是占位实验（无 pid/gpu），不要尝试查它的进程状态或分析它的结果
- TEAL thresholds 是预校准的（thresholds.json），CARC coordination 免校准但底层 thresholds 不是——写论文时必须区分
- DDL: EMNLP 2026 ARR 2026-05-25（剩 13 天），MVP 判定直接决定后续路径（PASS/DISCORDANT/FAIL 三条路线）

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980，工作目录 /root/carc
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（aml-train 镜像，不要创建 venv）
- 模型：/root/carc/models/DeepSeek-R1-Distill-Qwen-14B
- 数据集：EleutherAI/hendrycks_math (precalculus, cached)
- 结果文件：/root/carc/results_seed42.json, /root/carc/results_seed1337.json
- 活跃进程：carc_mvp_seed42 (PID 12699, cuda:0, tmux 管理)
- Cron：carc_mvp_seed42 仍在监控中（reconcile 确认 still running）

### 3. 📊 当前状态
- **刚做完**：收到 carc_mvp_seed1337 的 CRON 完成回调，已 spawn Worker (`worker_analysis_carc_mvp_seed1337_20260512T111612`) 去服务器读取结果 + 提取指标 + 对照 2×2 矩阵判定 + 更新 registry
- **等待中的回调**：
  1. Worker `analysis:carc_mvp_seed1337` — 正在分析 seed1337 结果，完成后会更新 registry（conclusion + metrics）
  2. Cron `carc_mvp_seed42` — 仍在 RUNNING (cuda:0)，完成后也需要同样的分析流程
- **未向 Director 汇报**：等 Worker 回来拿到实际指标后再汇报（不报未确认的数字）

### 4. 📋 待办
- Worker analysis:carc_mvp_seed1337 回调 → 读取 conclusion + metrics → 执行 on-experiment-done 分叉（success/negative）→ 更新 report.md → 向 Director 汇报（带 [资源] 行）
- carc_mvp_seed42 cron 回调 → spawn 同样的分析 Worker → 同上流程
- 两个 seed 都分析完 → 聚合两组结果做最终 MVP 判定（2×2 矩阵），汇报 Director 走哪条 post-MVP 路径（Path A/B/C）
- MVP 判定为 PASS → 立即准备 τ/γ/sparsity sweep 实验代码
- MVP 判定为 FAIL/DISCORDANT → 按 red-section 产出 Framing 调整提案

### 5. 🎯 战略上下文
- 核心假设：KV similarity (EMA centroid) 同时驱动 MLP 稀疏化 + KV cache 驱逐，单一 O(1) 信号协调两个正交瓶颈轴
- MVP 用 2×2 矩阵判定：perturbation diff (≥10%) × correlation |r| (≥0.4)。PASS 需要两者同时满足
- 两个 seed (42, 1337) 各 30 samples，总共 60 samples 覆盖 precalculus
- **易错点**：seed1337 的 Worker 分析报告会写入 artifacts/carc_mvp_seed1337_analysis.md 并更新 registry——下一个"你"拿到 Worker 回调后直接从 registry 读 metrics，不要重新 SSH
- **易错点**：mvp_001 是旧的占位实验，真正跑的是 carc_mvp_seed42 和 carc_mvp_seed1337，不要混淆
- 决策链：D001 (2026-05-12) MVP 定义 → 当前等两组 seed 结果 → 判定后进入 Path A/B/C


---
