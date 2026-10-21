# director / loop_9.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`1c31b3c9fc44c68765d9.json`](../../sessions/1c/1c31b3c9fc44c68765d9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-21T23:51:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-41718 cuda:0,1 + westd-34887 cuda:0,1（4× RTX PRO 6000）
- 论文真源在**本地** `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/`，不在远程服务器
- paper_compile_and_check 必须传 `paper_dir="/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"`，默认路径不存在
- Round 19 审稿已提交（fresh mode），等用户审批卡。**不要重复提交**
- DDL: 2026-05-25（EMNLP 2026 ARR May cycle），距今 ~3 天

### 2. 🖥️ 基础设施快照
- 服务器 westd-41718：`/root/distill_sparse_swiglu/`，aml-train 镜像，conda base (`/root/miniconda3/bin/python`)
- 服务器 westd-34887：同上路径和环境
- 模型：`/root/autodl-tmp/` 下 LLaMA-3.1-8B（base + KL checkpoints）
- Per-layer KL checkpoints：westd-41718 `/root/distill_sparse_swiglu/checkpoints/perlayer_kl_30_s{42,123,456}/`；westd-34887 仅有 s123
- HF cache：`/root/autodl-tmp/.hf_cache`（BoolQ/super_glue 在 41718 有缓存，34887 需单独下载）
- 活跃进程：无（所有实验已完成）
- Cron：无活跃 cron

### 3. 📊 当前状态
**刚做完**：
- Per-layer KL 3-seed 全部完成（PPL 9.05±0.02, downstream 6-task + BoolQ）
- 论文 2D decomposition 重写（Abstract/Intro/Experiments §4.5）
- BoolQ 3-seed 最终数据落地：per-layer KL 64.5±11.5% vs E2E KL 73.7±3.2%
- 编译通过（0 critical），一致性检查通过
- Round 19 审稿卡已发用户（fresh mode），review_issues.yaml 已更新（R18-W4 resolved）

**Agent 当前状态**：正在处理一条关于 BoolQ cache 的旧指令 + 1 个 worker_done 排队。这些是**过时任务**——BoolQ 数据已经完整了。Agent 完成后可能会报告冗余结果，直接确认无需进一步动作即可。

**registry**：0 个 RUNNING，0 个 PREPARING。357 个实验总计（234 success, 23 negative, 31 failed）。

### 4. 📋 待办
- 用户审批 Round 19 审稿卡 → 等 Review Director 出报告 → 按 `review-report-action` skill 处理（Holistic Pass → Action Matrix）
- Agent 报告 BoolQ worker done → 确认数据已在论文中，无需进一步操作
- Round 19 审稿报告到达 → Read `skills/global/review-report-action.skill.md` → 逐条处理
- 若 Round 19 分数 ≥3.5 → 准备最终投稿
- 若 Round 19 分数仍 3.0 → 评估剩余 open issues（R18-W1 novelty, R18-W2 speedup, R18-W7 mask Jaccard）是否可在 DDL 前解决
- 审稿期间 GPU 空闲 → 可考虑跑 cross-seed mask Jaccard（R18-W7，唯一低成本可补实验）

### 5. 🎯 战略上下文
- **核心叙事升级**：从 Round 18 的 "coupling alignment hierarchy"（3.0 Findings）升级为 "quantitative 2D decomposition: signal type × coupling scope"。Per-layer KL 是关键新实验，直接回应 R18-W4（两位 reviewer 共识的 critical weakness）。
- **预期 Round 19 提分路径**：R18 升档路径 4 条中已解决 2 条（per-layer KL + MSE multi-seed）。预期 R2 可能从 3.0→3.5，R1 维持 3.5 或升 4.0。
- **不可解决的 structural weakness**：R18-W1（MaskLLM novelty overlap）和 R18-W2（no speedup）是论文固有限制，无法通过补实验解决——这是 Findings vs Conference 的核心分歧点。
- **易错点**：
  - Agent 可能报告 BoolQ 相关 worker 完成——数据已经在论文中了，不要再派重复 eval
  - 不要因为 "审稿期间 GPU 空闲" 就盲目派实验——DDL 前 3 天，只有直接影响论文分数的实验才值得
  - mask Jaccard 实验（R18-W7）是唯一可能在 DDL 前低成本完成的 open warning，但需确认代码是否已就绪


---
