# agent / loop_10.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`b9e1391a3057b0fa6c62.json`](../../sessions/b9/b9e1391a3057b0fa6c62.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-21T19:41:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-19183 的 cuda:0 和 cuda:1（gpu_ids 白名单）
- 审稿阶段，GPU 保留给审稿反馈后 targeted experiments，不要主动起新方向实验
- DDL: Abstract 2026-05-26, Paper 2026-05-29（ICML 2025 workshop 或类似）
- conda 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在
- 论文 framing 已锁定（D082-D085 决策链），不要改动 paper story 除非 Director 明确批准
- 前几轮 loop 启动了 benchmark 扩展工作（LIBERO-Object/NORA/TracVLA Spatial），**我已向 Director 确认是否授权，等回复中**——在 Director 确认前不要扩展这些工作

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183，项目目录 /root/vla-ssd（代码），/root/autodl-tmp/vla-ssd（数据+结果+checkpoints）
- Python：/root/miniconda3/bin/python（conda base env）
- 模型：OpenVLA → /root/autodl-tmp/vla-ssd/checkpoints/；TracVLA-Phi3V → /root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/
- NORA venv（独立）：/root/autodl-tmp/vla-ssd/envs/nora/（PyTorch 安装状态未知，可能卡住）
- 数据：/root/autodl-tmp/vla-ssd/data/libero/libero_goal/（10 tasks × 50 demos）
- 结果：/root/autodl-tmp/vla-ssd/results/（各实验子目录）
- 活跃进程：
  - `libero_object_full_pipeline` (PID 513523, cuda:0, tmux session, cron 监控中) — Phase 2 R² probing 进行中
  - LIBERO-Long checkpoint 下载 (PID 513449, 后台, ~12% 完成)
  - NORA 模型下载（hf-mirror PID 513278, ~53%）
- 磁盘：根分区 ~816G/879G 可用

### 3. 📊 当前状态
Session 10 刚完成 session-start 初始化。核心实验全部 DONE/success（88/16/121）。

**Registry 关键状态：**
- `libero_object_full_pipeline` — registry 显示 PREPARING 但实际 RUNNING on cuda:0（Phase 2 R² probing）。Registry 状态不一致需修复
- 7 个 behavioral 实验 — PREPARING，等审稿反馈决定是否启动
- 所有 phi3v_r2_* 实验 — DONE/success（seed_expansion CI=[0.629,0.639], untrained peak=0.583）

**等待中：**
- Worker `worker_code_tracvla_spatial_pipeline_20260521T014051`（running, turn 16, SSH 读取中）
- Worker `worker_analysis_gpu1_nora_diagnosis_20260521T014730`（刚派发，诊断 cuda:1 + NORA 安装状态）
- Director 回复：确认 benchmark 扩展工作（LIBERO-Object/NORA/TracVLA Spatial）是否经过审批
- `libero_object_full_pipeline` cron 回调（实验完成时）

### 4. 📋 待办
- Director 回复确认 benchmark 扩展工作已授权 → 继续推进；未授权 → 只维护已在跑实验，不扩展
- `worker_analysis_gpu1_nora_diagnosis` 回调 → 读诊断报告，了解 cuda:1/NORA/下载状态，决定是否需要干预
- `worker_code_tracvla_spatial_pipeline` 回调 → 读产出，如果是代码就绪则等 Director 决策是否提交
- `libero_object_full_pipeline` cron 回调（ANALYZING）→ 派 Worker 分析 R² 结果 → update_registry(conclusion, metrics) → 汇报 Director（跨 benchmark R² 对比）
- Round 15 审稿结果到达 → 根据 reviewer comments 启动 targeted experiments（PREPARING 池中已有 7 个候选）

### 5. 🎯 战略上下文
- **核心结论**：VLA 微调创造 instruction routing（attention head specialization），跨架构收敛（OpenVLA LLaMA-2 + TracVLA Phi3V 双验证）
- **D082-D085 决策链**：Framing 从单模型观察升级为跨架构收敛性质。C1 token specialization + C2 entry-exit routing + C3 R² inverted-U geometry 全部双架构复现
- **关键数据点**：Peak R² 0.637 (L9, OpenVLA) vs 0.634 (L11, Phi3V)，Δ=0.003；Counterfactual all d>0.8 across 20 tasks
- **结构性瓶颈**：Closed-loop gap (0/30 SR, wont_fix)、Scope fit (纯 representational)、LIBERO-only（Spatial counterfactual 部分缓解）
- **易错点**：
  - phi3v_r2_action_probe（5 seeds）和 phi3v_r2_seed_expansion（seeds 6-15）合在一起才是 15-seed 完整数据
  - `libero_object_full_pipeline` registry 显示 PREPARING 但实际在 GPU 上跑——不要因为看到 PREPARING 就重新提交
  - 前几轮 loop 启动的新工作（NORA/LIBERO-Object/Spatial）可能未经 Director 审批，已问 Director 确认中
  - NORA 用独立 venv（不是 conda base），加载用 `AutoModelForImageTextToText`


---
