# reviewer / loop_8.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`2215a7e62a3d89da1236.json`](../../sessions/22/2215a7e62a3d89da1236.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-15T11:29:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westb-13313，GPU 白名单需查 `execution.gpu_ids`（当前无活跃训练，但 fresh review 后若补实验必须核对）
- 论文工作目录是 `docs/paper/`（本地），**不是** `artifacts/_project/paper/latex/`（旧短版残留）也不是远程 `/root/autodl-tmp/simgate-modular-routing/paper/`（旧版）。三处同名文件容易混淆
- MATH 数据以 `clean_n300_rerun` 为准（registry `math-negative-contrast` 的该字段），不要用 raw N=300 数据（diff=0.05, significant=true 是脏数据）也不要用 `long_paper_results_summary.md`（残留 +5.0%）
- ALFWorld 未承诺纳入论文主体（D044），仅在 Limitations 和 Discussion table 中作为补充

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313(root)，远程代码 `/root/autodl-tmp/simgate-modular-routing`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/`
- 论文 .tex：`{workspace}/docs/paper/`（main.tex + 7 个 \input + figures/ + references.bib）
- 远程数据：`/root/autodl-tmp/simgate-modular-routing/results/` 下有 plan_c/, multi_model_pilot/, math/ 等
- Llama 模型：`/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/`（4 shards, ~15GB）
- GPU：2× RTX 5090，当前无活跃进程/tmux/cron
- 无 wandb 配置（本项目不检查 W&B）

### 3. 📊 当前状态
论文扩写全部完成，figures/tables 全部集成。我已审查完所有章节：
- ✅ experiments.tex, discussion.tex, method.tex, related_work.tex, introduction.tex, abstract.tex, conclusion.tex, figures integration
- Registry：60 个实验全部 DONE，0 个 RUNNING/PREPARING
- 等待中：fresh long paper review（`apr_20260515T104409_t4pu` pending 用户确认）→ 审稿报告出来后进入迭代修复

**未修复的已知问题（已报告给 Director，等 fresh review 后迭代修复）**：
1. Introduction 写 57.6% / Experiments 写 58.1±0.8%（router balanced accuracy 不一致）
2. Conclusion "logit-generation gap" 术语未在 experiments.tex 定义
3. Limitations 与 Discussion/Conclusion 有轻度内容重复（graded failure costs / step-level labeling）

### 4. 📋 待办
- Fresh review 报告返回 → 逐条核实审稿意见中的数据 claim，交叉验证 registry
- Worker 提交修复 patch → 验证 57.6/58.1 是否统一、logit-generation gap 是否解释或删除
- 若 Director 要求补实验 → 核对 GPU 白名单 + CUDA_VISIBLE_DEVICES
- 论文终稿前 → paper_provenance.yaml 覆盖率检查 + reference audit（2025-2026 arXiv ID 验证）
- 注意 bib 中 cite-key 年份不一致：`toolformer-2024` 实际 year=2023，`chameleon-2024` 实际 year=2023

### 5. 🎯 战略上下文
- 核心结论：ScienceWorld 上 ~90% routing signal 来自 death avoidance（DAF=90.41%），78.9% non-tie labels 由 death asymmetry 驱动，与 penalty 无关
- MATH 是 negative contrast：无 death → signal 消失/反转（+4.3pp favoring internal, p=0.079 borderline）
- Llama pilot 是 preliminary directional evidence only（N=10 pairs, 2 tasks）——direction consistent with Qwen，不是 reversal
- **最容易判断错的事**：Llama 的 death pattern 方向。我自己在本 session 犯过这个错——误以为 Llama 方向反转，实际上 Qwen 和 Llama 都是 internal 更容易死（same direction）。D055 修正了 D054。看到 D054 描述"方向模型依赖"不要信，以 D055 为准
- **第二个坑**：论文存在三个位置（docs/paper/ vs artifacts/_project/paper/latex/ vs 远程 paper/），只有 docs/paper/ 是当前工作版本
- DDL 2026-05-25，距今 10 天，pure review-iterate 阶段，无新实验需求


---
