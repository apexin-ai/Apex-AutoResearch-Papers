# director / loop_2.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`8f67e46d4a64fcdebce9.json`](../../sessions/8f/8f67e46d4a64fcdebce9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-15T17:07:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 仅限 cuda:0, cuda:1（Constraint C001，westd-34887 上的 2× RTX PRO 6000 Blackwell 98GB）
- post-MVP kickoff 流程：Dream dream_20260515T164925 结果回来之前**禁止批准新 GPU 实验**（已写 framing + plan，gate on Dream）
- Vanilla TEAL baseline PPL=66036 已被 Reviewer 判 CRITICAL invalidated——registry 中 6 个实验的 vanilla_teal_sparse_ppl 字段不可引用，需修复实现后重测
- BCE std 是 0.89 不是 0.72（已在 ROADMAP 修正）

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887 (connect.westd.seetacloud.com)，账号 root
- 远程代码路径：**未配置**（get_project_status 显示 ❌），需要确认后 update_project_config
- Python/conda/venv：未探测（Agent 之前 session 搭建过环境但 handoff 未记录路径）
- 模型：Llama 3.1 8B（远程路径未记录）
- 已有代码：`src/compensation.py`（ErrorCompensation 模块，12 单元测试通过）
- 活跃进程：无（Agent idle 180min 后被 reset，两张 GPU 空闲）
- W&B / HF cache：未配置

### 3. 📊 当前状态
**刚做完**：post-MVP kickoff 全流程——complete_mvp → paper_framing.md → experiment_plan.yaml → dream_simulate(full) → update_roadmap。Reviewer 两轮 warning 已处理（claim 字段类型 fix、Claim 3 降级、SPON 预算提升、BCE std 修正）。

**Dream**：dream_20260515T164925 启动于 ~3h 前（预期 10-25 min），**回调尚未收到**。可能已完成但 callback 丢失——新 session 启动后立即 `get_dream_status` 检查。

**Registry**：16 实验，7 success / 2 negative / 3 failed / 4 killed。无 RUNNING / PREPARING。
- 成功的 MVP 实验：mvp_kl_norm_v2_s42/s123/s456（KL，PPL 12.08/11.91/13.58）+ mvp_bce_s42/s123/s456（BCE，PPL 44.54/44.59/43.03）

**Agent 上一轮未处理的指令**：代码准备任务（SPON 实现、proper TEAL greedy allocation、BCE+comp 训练配置、KL s0/s1 seed 配置）—— Agent idle 超时没收到，需重发。

### 4. 📋 待办
- Dream 状态 = done → Read dream-report-action.skill.md，按三档审稿行动指令处理，通过后批准 P0 实验
- Dream 状态 = pending/failed → 重新 `dream_simulate(review_mode="full")`
- Dream 通过 → 并行启动：plan_001 BCE+comp (cuda:0) + plan_004 SPON (cuda:1)，同时派 Agent 做 proper TEAL 实现 + KL s0/s1 补 seed
- Reviewer CRITICAL vanilla TEAL → Agent 必须修复 `vanilla_teal_global_masks()`（加 per-layer z-score normalization 或 Wanda-style scoring），修复前 plan_006 数据无效
- SPON 复现失败 → Claim 2 死亡，需 pivot framing 到 2-claim paper

### 5. 🎯 战略上下文
- **核心结论链**：D001(MVP 设计) → D003(sparsity 坍塌) → D004(KL 归一化+Lagrangian) → D006(Reviewer 抓 bug 纠正) → D007(MVP PASS, 进入 research)
- **MVP 效果量巨大**：KL 12.52 vs BCE 44.05（差 31.53 PPL）。但 Claim 1 headline 取决于 BCE+comp 结果——如果 BCE+comp 缩到 15-18 PPL，"eliminates compensation" 变成 "marginally better"
- **最容易判断错的事**：(1) 不要引用 vanilla_teal_sparse_ppl=66036 作为 evidence——这是实现 bug 不是方法差 (2) s456 是 outlier（PPL 13.58 vs 12.08/11.91），加 2 seeds 后 5-seed mean 可能上移 (3) Claim 3（s² 二次缩放）是 testable prediction 不是已验证结论，abstract/intro 不能写成断言
- **DDL**：EMNLP 2026 ARR 5/25，剩 10 天，时间线激进但 AI 团队 24/7 可行


---
