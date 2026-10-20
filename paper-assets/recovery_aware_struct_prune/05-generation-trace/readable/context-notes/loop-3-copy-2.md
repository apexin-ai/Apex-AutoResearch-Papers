# agent / loop_3.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`ab549d073178a5c2738b.json`](../../sessions/ab/ab549d073178a5c2738b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-14T16:53:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-23072 的 cuda:0 + cuda:1，不得用其他设备
- 环境激活必须用 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在
- 35% sparsity 下剪枝必须用 GQA group 粒度（per-Q-head 会违反 GQA 约束导致 forward crash，v1 的教训）
- GRPO 不能直接在严重退化模型（<1% accuracy）上跑——会 loss=0/grad_norm=0 死循环，必须先 SFT warmup

### 2. 🖥️ 基础设施快照
- 服务器：westb-23072，工作目录 `/root/recovery_aware_struct_prune/`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- GPU：2× RTX PRO 6000 Blackwell 94GB
- 模型：`/root/recovery_aware_struct_prune/models/` 下有 pruned_standard_35 + pruned_rasp_35（从 DeepSeek-R1-Distill-Qwen-7B 剪枝）
- 数据：GSM8K（calibration 512 samples + test 1319 samples）
- 结果目录：`/root/recovery_aware_struct_prune/results/`
- 日志：`~/runs/recovery_aware_struct_prune/mvp_rasp_pipeline_v2.log`
- 活跃进程：无（实验已结束）
- Worker 活跃：`worker_analysis_mvp_rasp_pipeline_v2_20260514T135102` 正在运行，分析日志+W&B+结果文件

### 3. 📊 当前状态
刚收到 mvp_rasp_pipeline_v2 的 CRON 完成回调（进程正常退出，W&B 数据可用）。已派 Worker 做全面分析（读日志、检查结果文件、拉 W&B 指标、写分析报告）。Registry 状态：
- `mvp_rasp_pipeline_v2`：ANALYZING — SFT warmup → GRPO 两阶段恢复，核心问题是 ρ(F(h), recoverability) 是否 ≥ 0.4
- `mvp_rasp_pipeline`：DONE(failed) — v1 因 GQA 约束违反 crash，已被 v2 取代

**等待中**：Worker `worker_analysis_mvp_rasp_pipeline_v2_20260514T135102` 回调 → 拿到分析报告后更新 registry conclusion + metrics，刷新 report.md，向 Director 汇报。

### 4. 📋 待办
- Worker 分析回调到达 → 读分析报告 → 按 on-experiment-done skill 分叉：
  - ρ ≥ 0.4（success）→ 更新 registry DONE(success) → 刷 report.md → 向 Director 汇报 → 立即铺 Phase 2 实验（GRASPrune + RLVR 等）
  - ρ ∈ [0.3, 0.4)（边缘）→ ROADMAP 说 25% sparsity 重复验证 → 向 Director 请示
  - ρ < 0.3 或 SFT/GRPO 未跑完（negative/failed）→ 产出 red-section Framing 调整提案 → 向 Director 汇报，不默默跑下一个
- 如果 Worker 报告 SFT warmup 本身也失败 → 可能需要重新审视整个两阶段方案，pivot 到 Contingency（3 methods × 3-5 sparsity × 2 recovery 交互 benchmark）

### 5. 🎯 战略上下文
- 目标会议：EMNLP 2026 ARR May 25（距今 11 天），时间极紧
- 核心 idea：CKA functional overlap 预测 RLVR recoverability → RASP scoring 选择可恢复结构
- D001：35% sparsity 下接受 MLP-only pruning（attention head 因 GQA 约束不好剪）
- D002：终止无效 GRPO，改用 SFT warmup → GRPO 两阶段恢复
- **最容易判断错的事**：v2 的 notes 记录了 post-prune accuracy 只有 0.15% 且 GRPO 直接失败。如果 SFT warmup 后 accuracy 仍很低（比如 <5%），GRPO 阶段大概率也跑不起来。此时不要硬凑 correlation——应该诚实标记 negative 并走 red-section 流程
- **易踩的坑**：v1 已经证明 per-Q-head 粒度不可行。任何新实验都必须沿用 GQA group 粒度。另外 GRPO 在严重退化模型上无法产生有效 advantage，这是根本性问题不是超参问题


---
