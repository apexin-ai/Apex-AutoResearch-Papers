# agent / loop_12.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`d2844bbac1861e19be9c.json`](../../sessions/d2/d2844bbac1861e19be9c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: idle_timeout
updated: '2026-05-18T01:54:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-34887 cuda:0,1 + westd-41718 cuda:0,1（westd-41718 是 14B 模型特批，新实验默认用 34887）
- EMNLP 2026 ARR May DDL = 2026-05-25（剩 8 天）
- 论文数字必须有代码来源（C003），不能手动编造
- KL PPL 引用: 4-seed mean 12.00±0.07（禁用单 seed 最佳 11.91）
- 14B TEAL PPL 此前有 misattribution（8.76 已移除，保留 KL 7.62），不要把旧数字写回论文
- 50% global KL MMLU 已升级为 3-seed mean±std（28.1±0.2），不要用单 seed 数字

### 2. 🖥️ 基础设施快照
- **westd-34887**: `/root/distill_sparse_swiglu/`, Python `/root/miniconda3/bin/python`, 2×RTX PRO 6000 Blackwell 95GB
- **westd-41718**: 同上路径结构，同型号 GPU
- 模型: `/root/autodl-tmp/models/llama-3.1-8b`(LLaMA), `/root/autodl-tmp/models/qwen2.5-14b`(Qwen)
- HF cache: `/root/autodl-tmp/.hf_cache/datasets`
- WANDB_MODE=disabled（离线评估）
- 活跃进程:
  - qwen14b_bce30_s42_eval: PID 59122, westd-34887:cuda:0
  - bce_isocompute_v3_s123_eval: PID 74858, westd-34887:cuda:1
  - qwen14b_dense_baseline: PID 18845, westd-41718:cuda:0
  - qwen14b_teal30_eval: PID 6896, westd-41718:cuda:1
- 活跃 Worker: `worker_infra_urgent_collect_all_14b_results_20260517T214835`（CPU，读 4 个 eval 日志）

### 3. 📊 当前状态
Loop #12 完成 session-start 初始化：reconcile crons（4 活跃）、注册 λ/sparsity curve artifact (art_20260517_adc7fe, R1-W5 resolved)、向 Director 汇报状态。

**已完成（本轮确认）：**
- qwen14b_kl30_s42_eval: DONE(success) — PPL 7.62, MMLU 63.7%, ARC 57.2%, WG 72.1%, GSM8K 48.8%
- λ/sparsity curve Worker: DONE — PDF/PNG 生成完毕，artifact 已注册

**RUNNING (4):** qwen14b_bce30_s42_eval / bce_isocompute_v3_s123_eval / qwen14b_dense_baseline / qwen14b_teal30_eval — 全是下游 eval，预计各 30-60min

**等待中：** 4 个 eval 的 cron 回调 + urgent Worker 回调 + Director 对状态汇报的回复

### 4. 📋 待办
- qwen14b_bce30_s42_eval 回调 → 读 metrics → 与 KL 对比（预期 BCE 弱）→ 更新 registry
- qwen14b_teal30_eval 回调 → 读 metrics → 与 KL 对比（预期 TEAL 弱）→ 更新 registry
- qwen14b_dense_baseline 回调 → 读 metrics → 计算 KL/BCE/TEAL 相对 dense 的退化比
- bce_isocompute_v3_s123_eval 回调 → 与 s42/s456 对比 → 完成 Table 2 BCE 3-seed mean±std
- 上述 4 个全完成 → 汇总 14B cross-scale table → 写入论文 → 提交 Round 2 review
- GPU 空出后优先提交: wallclock_speedup_30_50（论文需 latency 数据）或 kl50_global_s123_reeval（Table 2 一致性修复）

### 5. 🎯 战略上下文
- 论文核心叙事（D047）：KL distillation 使 SwiGLU contextual sparsity prediction 不需要 error compensation，最简推理管线。三个 claim：KL>>baselines / SPON orthogonal / three-regime phase transition
- Round 1 审稿 3.0/5，4 critical 全 resolved，R1-W4 SNR + R1-W5 λ curve 均已完成
- 14B cross-scale 验证是提交 Round 2 review 的最后阻塞——KL 30% 已证明强劲（MMLU 63.7%），等 BCE/TEAL/dense baseline 凑齐对比表
- qwen14b_bce30_s42_v2 是 negative（BCE 10x Lagrangian 仍失败）→ publishable finding
- Allocation narrative 已定稿（D050）：只 claim variance reduction，不 claim uniform > global mean
- 易错点：registry API 的 `filters={"exp_id": "xxx"}` 不生效——用 `grep registry.yaml` 或按 status 过滤
- 易错点：report.md 不可通过 save_project_file 写入（auto-generated）


---
