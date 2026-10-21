# agent / loop_11.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`59b4979d946bc7cb4d3e.json`](../../sessions/59/59b4979d946bc7cb4d3e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: idle_timeout
updated: '2026-05-17T21:48:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-34887 cuda:0 + cuda:1。westd-41718 的 GPU 目前被 Qwen-14B eval 临时占用（Director 批准），但不在常规白名单内，新实验不要往那提交
- Qwen-14B 实验跑在 westd-41718 是因为模型太大 westd-34887 单卡放不下，这是特批例外
- 论文数字必须有代码来源（C003），不能手动编造
- EMNLP 2026 ARR May DDL = 2026-05-25，剩 8 天

### 2. 🖥️ 基础设施快照
- **westd-34887**: 工作目录 `/root/distill_sparse_swiglu/`，Python `/root/miniconda3/bin/python`，RTX PRO 6000 Blackwell 95GB×2
- **westd-41718**: 同上路径结构，同型号 GPU
- 模型路径: `/root/autodl-tmp/models/llama-3.1-8b`（LLaMA），`/root/autodl-tmp/models/Qwen2.5-14B`（Qwen）
- HF cache: `/root/autodl-tmp/.hf_cache/datasets`
- W&B: 大部分 eval 实验 WANDB_MODE=disabled（离线评估）
- 活跃进程:
  - qwen14b_kl30_s42_eval: PID 52224, westd-34887:cuda:1
  - qwen14b_bce30_s42_eval: PID 59122, westd-34887:cuda:0
  - qwen14b_teal30_eval: PID 6896, westd-41718:cuda:1
- 活跃 Worker: `worker_analysis_lambda_sparsity_curve_20260517T173720`（CPU，生成 λ/sparsity 时序曲线图，R1-W5）

### 3. 📊 当前状态
刚完成 `downstream_teal30_baseline` 分析并推至 DONE(success)。TEAL 30% 在 HellaSwag/PIQA/BoolQ 全面弱于 KL（平均 -5.6pp），已汇报 Director。

Registry 摘要：
- **RUNNING (3)**: qwen14b_kl30_s42_eval / qwen14b_teal30_eval / qwen14b_bce30_s42_eval — 全是 Qwen-14B 跨规模下游验证（MMLU/ARC/WinoGrande/GSM8K）
- **PREPARING (16)**: 包括 bce_isocompute_v3_s456/s123（多 seed）、kl50_global_s123_reeval（数据一致性修复）、wallclock_speedup_30_50、longbench_dense_v5 等
- **DONE**: 117 个（75 success, 17 negative, 15 failed, 10 killed）

等待中：
- 3 个 Qwen-14B eval 的 cron 回调（预计各 ~30-60min）
- λ/sparsity curve Worker 回调
- Director 对 downstream_teal30_baseline 汇报的回复

### 4. 📋 待办
- qwen14b_kl30_s42_eval cron 回调 → 读日志提取 MMLU/ARC/WinoGrande/GSM8K → 更新 registry → 与 8B 对应指标对比退化比
- qwen14b_teal30_eval cron 回调 → 同上，这是 14B TEAL baseline
- qwen14b_bce30_s42_eval cron 回调 → 同上，14B BCE baseline；三个都完成后汇总 14B cross-scale table 汇报 Director
- λ/sparsity curve Worker 回调 → 注册 artifact → 更新 ROADMAP（R1-W5 resolved）
- 三个 14B eval 全完成 + λ curve 完成 → 提交 Round 2 review（submit_paper_to_review）
- westd-34887 双卡空出后 → 从 PREPARING 队列中优先提交 wallclock_speedup_30_50（论文需要 latency 数据）或 kl50_global_s123_reeval（Table 2 数据一致性修复）

### 5. 🎯 战略上下文
- 论文核心叙事（D047）：KL distillation 使 SwiGLU 的 contextual sparsity prediction 不再需要 error compensation，实现最简推理管线。三个 claim：KL>>baselines / SPON orthogonal / three-regime phase transition
- Allocation narrative 已定稿（D050）：variance reduction only，不再 claim uniform > global mean
- Round 1 审稿 3.0/5，4 critical 已全部 resolved，剩 2 warning in_progress（R1-W4 SNR patch 已 dispatched，R1-W5 λ curve 正在生成）
- qwen14b_bce30_s42_v2 是 **negative**（BCE 10x stronger Lagrangian 仍然失败），这是 publishable finding：BCE gradient signal 在 14B scale fundamentally insufficient
- 易错点：14B TEAL PPL 此前有 misattribution（8.76 已移除，保留 KL 7.62），不要把旧数字写回论文
- 易错点：50% global KL MMLU 数据已升级为 3-seed mean±std（28.1±0.2），不要用单 seed 数字


---
