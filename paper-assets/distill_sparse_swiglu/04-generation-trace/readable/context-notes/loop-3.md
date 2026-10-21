# director / loop_3.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`b968051c0a31cc751042.json`](../../sessions/b9/b968051c0a31cc751042.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-16T11:39:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-34887 的 cuda:0 和 cuda:1（项目白名单，不得越界）
- 论文 sparsity sweep 主表必须用同推理协议对比：predictor-TEAL vs vanilla-TEAL，禁止混用 hard_mask_ppl（D035）
- 70% KL 数字用 predictor_teal_sparse_ppl=17.91，不是 hard_mask=13.84
- D032 "数据污染"已撤回（D033）——kl_sparsity30_s42_v3 的 teal_sparse_ppl=8.98 是正确值，不是 13.63
- bench_eval 用 WANDB_MODE=offline，否则 wandb API key 缺失会立即崩溃

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887 (connect.westd.seetacloud.com)，账号 root
- 工作目录：/root/distill_sparse_swiglu/
- Python：conda base 环境（/root/miniconda3/bin/python），aml-train 镜像
- 模型：Llama-3.1-8B + Mistral-7B-v0.3，HF_HOME=/root/autodl-tmp/.hf_cache
- Checkpoints：/root/distill_sparse_swiglu/checkpoints/（KL/BCE/sparsity variants）
- 日志：/root/runs/ 下各实验 log
- 活跃进程：bench_kl30_global (PID 222736, cuda:0) 和 bench_kl50_global (PID 222658, cuda:1) — 可能已完成，需 SSH 确认
- Cron：两个 bench 实验有 120s 间隔监控

### 3. 📊 当前状态
刚批准 RESET_BOTH 并绕过 handoff 等待，给 Agent 发了紧急指令检查 GPU + 收结果 + 提交 bench_teal30/teal50。Agent 空闲 ~97min 后收到指令，应正在处理。

Registry RUNNING：bench_kl30_global, bench_kl50_global（实际可能已完成，registry 状态需 SSH 确认后更新）
Registry QUEUED：bench_kl50_uniform, bench_teal50, bench_teal30
Paper Agent：Step 3/5 文献补充中，图表 3/3 完成，数据 patch 已整合
Review 团队（C 群）：已启动并行审稿

### 4. 📋 待办
- bench_kl30_global/bench_kl50_global 完成 → 收结果 update_registry，立即上 bench_teal30 (cuda:0) + bench_teal50 (cuda:1)
- bench_teal30 完成 → Claim 3 "surpassing TEAL at 30%" 有同协议 downstream 证据，通知 Paper Agent patch 主表
- bench_teal50 完成 → 论文主表 TEAL 50% downstream 数据完整
- 两个 teal bench 完成后 → bench_kl50_uniform（填满 allocation matrix）→ LongBench (P1, EMNLP venue fit)
- Paper Agent Step 3 完成 → 审批进入 Step 4 (Section Writing)
- 收到 Review 团队（C 群）审稿报告 → Read review-report-action skill，逐条处理

### 5. 🎯 战略上下文
- 投稿目标：EMNLP 2026 ARR May，DDL 5/25（剩 9 天）
- 论文 narrative：KL output-distribution distillation 使 error compensation 不必要 + PPL-downstream disconnect + allocation vs capacity phase transition
- 三个 Core Claim：Claim 1 (KL >> baselines) Strong, Claim 2 (SPON orthogonal) Adequate, Claim 3 (Phase transition) 数据到位但缺 bench_teal30 同协议对比
- 关键决策链：D034 Claim 3 reframe → D035 表格协议约束 → D036 threshold 30-40% → D037 LongBench P1/MT-Bench P3
- 易错点：(1) 不要把 0-shot 旧数据和 few-shot bench 数据混在同一张表 (2) PPL 非单调（40%=8.36 < 30%=8.82）是 feature 不是 bug——支撑 "PPL is poor proxy" 叙事 (3) Reviewer Concern #5 措辞已降级，不再承诺 MT-Bench
- paper_framing.md 和 decisions.yaml 是最新的，ROADMAP 可能略滞后需要更新


---
