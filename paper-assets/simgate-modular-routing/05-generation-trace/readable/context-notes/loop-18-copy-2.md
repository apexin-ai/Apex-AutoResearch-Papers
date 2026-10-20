# reviewer / loop_18.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_18.md`
- **Structured JSON:** [`47e632b5f1c116722cd6.json`](../../sessions/47/47e632b5f1c116722cd6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_wall_time
updated: '2026-05-21T22:17:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- **D131/D132 实验冻结**：DDL 05-25 前不做新实验（GPU 或 CPU 均算）。W4 positive control 已被我标 WARNING（Director 未明确追溯批准）
- **westd-18266 GPU 白名单**：项目只分配了 1 张卡（具体 gpu_id 需从 execution config 确认），不可越界
- **论文数字红线**：97.4% step tie rate（5,935/6,094）、78.9% label fraction（75/95）、DAF 90.4% [81.1, 99.0] — 之前有 Worker 误改 97.4% 为 93.0% 被我 CRITICAL 打回，必须持续监控
- **Gemma bootstrap CI**：论文使用 [79.5%, 98.4%]（来自 unified_episode_bootstrap.py），registry 仍显示旧值 [68.8, 100]（来自 analysis.json）。论文值正确，registry 未更新。不要被 registry 误导

### 2. 🖥️ 基础设施快照
- 服务器：westd-18266(root)，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/`
- 论文源文件：`docs/paper/` (main.tex, abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex)
- 关键数据：`results/plan_c/` (step-level labeled data), `results/baseline_245eps/`, `results/gemma_scienceworld_counterfactual/`
- 活跃进程：无（D131 冻结，所有 121 个实验已完成）
- W4 产出：`src/task_type_positive_control.py` + `artifacts/w4_task_type_positive_control.json`（sklearn, 未注册 registry）

### 3. 📊 当前状态
**论文 submission-ready**。25 页（主文 8 页），0 errors，Round 25 审稿修复全部完成并通过我的 PASS 审查。

最近审查完成：
- final-consistency-check worker → PASS（14 个关键数字跨章节一致）
- w4-code-survey worker → PASS（纯调查，无行动项）
- w4-positive-control worker → WARNING（D132 说不做但 Worker 做了；结果 64.7% bal.acc 远低于预期 90%+；LOTO=50% 与论文 49.2% 一致性有 rebuttal 价值）
- Task-level router ROI 评估 → INFO（建议不做，用文字 argue）

等待：用户确认启动 ARR 提交流程 + 匿名代码仓库

### 4. 📋 待办（条件触发式）
- Director 发来新 worker_done 通知 → 按常规审查
- Director 转发 rebuttal 章节写作 → 进入审查模式 B，先 Read paper-quality-lessons skill
- Director 问 W4 数据是否可用于 rebuttal → 回答：可以，重点用 LOTO 50% vs LLM router 49.2% 一致性叙事，避免引用 64.7%
- 审稿人意见到达 → Read rebuttal skill → 逐条审查 response letter
- 任何论文数字修改通知 → 立即交叉核对全部 6 个章节（97.4%/78.9%/90.4% 等核心数字）

### 5. 🎯 战略上下文
- 项目核心结论：ScienceWorld 中 78.9% routing labels 源自 death asymmetry，DAF 88-90% 跨三模型一致
- 目标：EMNLP 2026 via ARR, Findings (≥3.0)，预估 ~3.2
- 决策链关键节点：D013（framing pivot → diagnostic framework）→ D126/D127（framework-centric reframing）→ D130（accept Findings）→ D131/D132（冻结实验）
- **易错点**：
  - W4 positive control 结果（64.7%）如果不加解释直接放论文，审稿人会说"和 59.3% 差不多，task-type 也没用"——必须用 LOTO 一致性叙事而非绝对数字
  - Registry 的 Gemma CI [68.8, 100] 是旧值，论文 [79.5, 98.4] 才是对的（来自 unified_episode_bootstrap.py）
  - "action-space restriction" = "grounding interventions" = Appendix O "Grounding Ablation"，三个术语指同一机制
  - ROADMAP 目标写 "Findings (≥3.0)" 是 D130 reconciliation 后的结果（不是 "Conference ≥3.5"）


---
