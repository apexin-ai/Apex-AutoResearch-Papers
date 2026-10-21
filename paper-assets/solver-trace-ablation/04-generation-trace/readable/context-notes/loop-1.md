# director / loop_1.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`7214b4b6df7282821aad.json`](../../sessions/72/7214b4b6df7282821aad.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-13T22:03:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-39279 的 cuda:0 和 cuda:1，必须用 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1` 隔离，否则 accelerate 自动分布到两卡导致 OOM (r3 教训)
- 根分区 30GB 已满，所有 checkpoint/log/模型必须写 `/root/autodl-tmp/`
- exec-sta-r5 registry conclusion 应为 negative（当前可能标为 success，需修正）
- MVP 状态是"部分通过"——Pass #4/#5 未满足，Kill criteria 未触发。不要引用"MVP 通过"

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279 (connect.westd.seetacloud.com:39279)，account: root
- 工作目录：`/root/solver-trace-ablation/`（代码/脚本），输出写 `/root/autodl-tmp/outputs/`
- Python：conda base `/root/miniconda3/bin/python`（aml-train 镜像）
- 模型：`/root/solver-trace-ablation/models/Qwen3-4B/`（7.6GB, ModelScope 下载）
- 数据：`/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl`（实际是 FOLIO）、`proofwriter_fol_500.jsonl`
- Solvers：Prover9 `/usr/local/bin/prover9`、SWI-Prolog 8.4.2、Z3 4.16.0
- W&B：未配置，训练用 `no_wandb: true` + 本地 JSONL logging
- 活跃进程：GPU 当前空闲（0% util）。已排队的紧急实验（低权重STA + ISR-as-bonus）可能正在启动

### 3. 📊 当前状态
刚完成 MVP 阶段，项目已转 research phase。核心发现：full STA 连续 ISR 作为度量指标有区分力（GT=0.56 vs model=0.064），但 50/50 权重作为训练 reward 导致 prove_rate 退化（0.10 < baseline 0.12）。O(1) fast_isr 完全无效（r4 阴性）。

Registry 关键实验：
- sta-phase0-baseline: DONE(success) — base model ISR=0.064
- sta-gt-isr-baseline: DONE(success) — ground-truth ISR=0.559
- sta-phase1-exec-only-r4/r5: DONE — prove_rate=0.15, 完美复现
- sta-phase1-exec-sta-r5: DONE — prove_rate=0.10, STA 50/50 导致退化
- r1/r2/r3: 全 DONE(failed)，分别因 argparse/wandb/OOM

等待中：
- Dream dream_20260513T215750 (full review mode) — pending，10-25min 异步
- Agent 队列：紧急实验指令（低权重STA cuda:0 + ISR-as-bonus cuda:1）+ research 前置任务（数据准备/Prolog STA/训练脚本升级）

### 4. 📋 待办
- 紧急实验完成 → 如果低权重或 bonus 模式 prove_rate ≥ exec-only(0.15) 且 ISR 有信号 → "STA as reward" 叙事成立，按 experiment_plan P0 推进
- 紧急实验完成 → 如果两者都仍 < exec-only → plan_005 全面 weight ablation 是最后机会；全失败 → 与用户讨论退化为 "STA as monitoring metric" 论文
- Dream 回调 → Read dream-report-action skill → 按三档对比评估 framing/plan 是否需要调整
- Dream 无阻塞 → 立即批准 P0 实验（plan_001-005），plan_005 与 plan_001 并行（pivotal）
- 不等 Dream 可启动：plan_004（O(1)vsO(N) 500步）、plan_009（SFT baseline）、FOLIO train/test split

### 5. 🎯 战略上下文
- 决策链：D001(MVP方案) → D002(100步+baseline) → D003(full STA+K=8) → D004(50/50退化，补低权重实验)
- paper_framing.md 和 experiment_plan.yaml 已写好，但 framing Claim 1 的 "ISR/PR 64%→33% 检测 hacking" 论述被 Reviewer 质疑——ISR/PR 下降可能只是分母（prove_rate）上升，不一定是 hacking。需要 plan_003（统一 eval）+ plan_012（人工标注）验证
- **最易判断错的事**：exec-only 的 ISR 是 binary（≡prove_rate），exec-sta 的 ISR 是 continuous（0-1）。直接比两者的 isr_mean 是比较不同指标。论文中必须用相同 full STA 评估两个 checkpoint
- **最易踩的坑**：train_grpo.py 的 config merge 用 `parser.set_defaults()` + 二次 parse，不是直接 setattr。改超参时改 YAML config 即可，不需要 CLI 传参
- DDL：EMNLP 2026 ARR 5月25日，剩 12 天。GPU 充足（30h 总量 / 2卡），时间瓶颈是实验方向对不对而非算力
- plan_005（weight ablation）是 pivotal：决定论文是 "STA improves training"（强 claim）还是 "STA monitors training"（弱 claim）


---
