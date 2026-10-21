# director / loop_19.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_19.md`
- **Structured JSON:** [`d167114ef2acdb7ad8d3.json`](../../sessions/d1/d167114ef2acdb7ad8d3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_messages
updated: '2026-05-22T22:14:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-32935 cuda:0-3, westb-23072 cuda:0-1。不可用其他服务器/卡
- westb:0 当前 GPU 异常（100% util / 0 MiB / 无进程），AutoDL 不支持在线 gpu-reset，需重启实例才能恢复，但 westb:1 有 MF3 在跑，暂不能重启
- α=1.0 GSM8K SFT 数据：ROADMAP 记录 61.49%，Agent 曾报 63.31%，以 ROADMAP 为准（有 registry 溯源）
- D111/D112 约束：C1 max |Δ|=1.34pp（含 MBPP），GSM8K-specific 用 1.14pp；scope 限定 "fine-grained structured pruning"；Self-Healing caveat 必须保留
- 论文真源在本地 `docs/paper/`，`paper/` 已重命名为 `paper_deprecated/`

### 2. 🖥️ 基础设施快照
- westd-32935：4× RTX PRO 6000，工作目录 `/root/recovery_aware_struct_prune`，磁盘 ~89%
  - 模型目录：`/root/autodl-tmp/recovery_aware_struct_prune/` 下各 SFT checkpoint
  - α=1.0 模型：`/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd`
- westb-23072：2× RTX PRO 6000，工作目录 `/root/recovery_aware_struct_prune`，磁盘 ~89%
- 论文本地路径：`projects/recovery_aware_struct_prune/docs/paper/`
- 活跃进程（截至 handoff 前）：
  - westd:0 — 空闲（α=3.0 完成），已指示 Agent 启动 Standard SFT MATH-500 eval
  - westd:1 — CKA-only MATH-500 eval PID 75284 (~6-8h)
  - westd:2 — α=0.5 MATH-500 eval PID 58276 (74%, ~1h 内完成)
  - westd:3 — α=1.0 MATH-500 eval PID 79030 (刚启动, ~6-8h)
  - westb:0 — GPU 异常，空闲
  - westb:1 — MF3 v3 Qwen-Math cross-arch PID 220343 (~45%, ~4-5h)

### 3. 📊 当前状态
MATH-500 dose-response 数据收集中，3/5 完成：
- α=2.0 = 24.0% ✅ (registry updated)
- α=3.0 = 23.2% ✅ (刚指示 Agent 更新 registry)
- α=4.0 = 26.6% ✅
- α=0.5 = 运行中 (~1h)
- α=1.0 = 运行中 (~6-8h)

关键发现：MATH-500 三个已完成点全在 stderr (~2pp) 范围内，本质 flat。GSM8K inverted-U 不跨 benchmark 成立。已通知用户 dose-response 叙事限定为 GSM8K-validated，MATH-500 作 supplementary discussion。

Agent 刚 RESET，pending 指令：更新 α=3.0 registry + westd:0 启动 Standard SFT MATH-500 + α=0.5 完成后汇报。

### 4. 📋 待办
- α=0.5 MATH-500 完成（~1h）→ 收集 accuracy，更新 registry，4/5 dose-response 完成
- α=1.0 MATH-500 完成（~6-8h）→ 5/5 dose-response 完成，汇总完整 MATH-500 表，确认 flat pattern
- CKA-only MATH-500 完成（~6-8h）→ 上界参照点，对比 dose-response 各 α 值
- MF3 v3 Qwen-Math 完成（~4-5h）→ cross-arch 验证 C2 recovery gradient
- 全部 MATH-500 数据齐 → Paper Agent Patch MATH-500 表进论文 → submit_paper_to_review
- westb MF3 完成 → 可重启 westb 实例修复 GPU:0 异常

### 5. 🎯 战略上下文
- 核心 claims：C1 universal decoupling (GRPO≈SFT, max |Δ|=1.34pp across 10+ conditions) + C2 recovery capacity gradient (CKA-only >> Random >> Standard)
- Dose-response (α inverted-U) 是 C2 的因果证据，但仅在 GSM8K 上成立。MATH-500 accuracy ~24% 接近 floor，信噪比不足区分——这不是 negative result，是 task-difficulty dependency
- 论文已完成 D111 合规修复（Self-Healing caveat, fine-grained scope, 1.34pp），编译通过 14页主文≤8页
- 投稿目标 EMNLP 2026 ARR May 25，~2.5 天
- 易错点：(1) truncation rate 高（31-38%），讨论 MATH-500 时必须提及 max_new_tokens 限制 (2) 不要把 MATH-500 flat 解读为 negative——是 floor effect，在论文中定位为 supplementary observation (3) Agent 报的 α=1.0 GSM8K=63.31% 与 ROADMAP 的 61.49% 不一致，以 ROADMAP/registry 为准


---
