# agent / loop_9.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`3ed53d815b27ef621a9c.json`](../../sessions/3e/3ed53d815b27ef621a9c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-19T11:15:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-25068 GPU 白名单需确认（report.md 显示 cuda:0-3 曾用，但 gpu_ids 需从 `get_project_resource_usage` 实时确认）
- westd-16639 GPU 白名单同上，当前 4 卡都有实验在跑（exp-038/039/040/041）
- exp-033 的 registry key 是 `exp-033`（不是 `exp-033-qwen3-pw600-nonthinking`，后者是旧的同名失败实验）
- EMNLP 2026 ARR May 25 截止（距今 ~6 天），所有实验和论文工作按此 deadline 排优先级
- 禁止在未分配 GPU 上启动实验（2026-04-24 事故教训），即使 Director 明确指令也要 push back

### 2. 🖥️ 基础设施快照
- **westd-25068**: 工作目录 `/root/symb_invariant_consensus`，conda base 环境，Python via miniconda3
  - 模型缓存: `/root/autodl-tmp/models/` (含 Mistral-7B-Instruct-v0.3, Qwen2.5-14B-Instruct 等)
  - 结果目录: `/root/symb_invariant_consensus/results/`
  - 磁盘: 427G/879G 可用 (49% 使用)
  - 活跃进程: exp-042-premise-formalization (cuda:2, PID unknown, tmux session)
- **westd-16639**: 同结构，磁盘 502G/879G 可用 (40%)
  - 活跃进程: exp-038 (LogiQA200), exp-039 (14B PW600), exp-040 (Qwen3 PW600), exp-041 (14B FOLIO204) — 4 卡全占
- 活跃 cron: exp-042, exp-038, exp-039, exp-040, exp-041（共 5 个，reconcile 刚确认全部正常）

### 3. 📊 当前状态
**刚做的**: Session 启动初始化完成（registry 同步、cron reconcile、report.md 读取）。收到 exp-033 (Mistral-7B FOLIO-204 SICA vs SC) 完成回调，已派 Worker `worker_analysis_exp-033_20260518T190340` SSH 到 westd-25068 提取结果。

**等待中**:
- Worker 回调: `worker_analysis_exp-033_20260518T190340` — 分析 exp-033 结果（Mistral-7B 跨家族验证 capability trap）
- Cron 监控中: exp-038 (LogiQA200), exp-039 (14B PW600), exp-040 (Qwen3 PW600), exp-041 (14B FOLIO204), exp-042 (Premise Formalization)
- PREPARING: exp-033-qwen3-pw600-nonthinking (旧), exp-045-backward-verification, exp-044-icl-oracle, smoke-test-5q

**Registry 概览**: 65 实验，RUNNING 5, ANALYZING 2 (含 exp-033), PREPARING 3, QUEUED 1

### 4. 📋 待办
- Worker `worker_analysis_exp-033_20260518T190340` 回调 → 提取 SC/SICA/delta/n → update_registry(status=DONE, conclusion=success/negative, metrics) → 刷新 report.md → 向 Director 汇报（含文献联动）
- exp-033 结果如果 negative (delta ≈ 0) → 进一步证实 capability trap 跨家族持续，强化 Framework B narrative；如果 delta > 0 且显著 → 意外，需要重新评估 Mistral 家族特殊性
- exp-038/039/040/041/042 任一 cron 回调 → 按 on-experiment-done 流程处理
- exp-044-icl-oracle 和 exp-045-backward-verification 状态为 PREPARING → 需要 GPU 分配后提交
- EMNLP deadline 6 天 → 所有 constructive experiment 完成后需要立即铺论文写作 Worker

### 5. 🎯 战略上下文
- **核心结论**: SICA 的 capability trap 是结构性的——LLM 提取的符号约束质量受限于 LLM 自身推理能力。Oracle +14.22pp (p=2e-7) 证明聚合机制有效，bottleneck 在 extraction quality。三路 constructive intervention（contrastive/cross-model/generational）全部 negative。Z3 Feedback (exp-036) 也 negative（第 4 个 negative）。
- **Framework B**: 论文定位为"诊断性研究"——capability trap 的发现本身是贡献，不是方法改进论文
- **当前扩展方向**: 跨模型（Mistral/Qwen3）、跨数据集（LogiQA/ProofWriter）、constructive attempts（ICL Oracle/Backward Verification/Premise Formalization）来巩固 evidence
- **易错点**: exp-033 在 registry 中有两个条目——`exp-033-qwen3-pw600-nonthinking`（旧，已 failed）和 `exp-033`（新，当前分析的 Mistral 实验），不要混淆
- **决策链**: D046→D048→D050→D051 确认四路 negative 后进入大规模扩展验证阶段


---
