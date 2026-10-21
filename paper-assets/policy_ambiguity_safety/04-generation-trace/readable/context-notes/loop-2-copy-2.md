# reviewer / loop_2.md

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`303f75fcdd401dcaa03c.json`](../../sessions/30/303f75fcdd401dcaa03c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-22T00:22:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU、无训练——全部是 API 实验（5+2 模型），不存在 GPU 越界风险
- Judge assignment 已修正：GPT-5.4 judges {Claude, GPT-4.1, Qwen3}; GPT-4.1 judges {GPT-5.4, DeepSeek}。如有人改回旧版（GPT-5.4 judges DeepSeek）立即 CRITICAL
- 论文主文严格 8 页，当前余量极小（Conclusion 在 page 8 底部）。任何主文增字必同时验证不超页
- tamkin_evaluating_2023 和 yin_safeagentbench_2025 是 related_work.tex 有效引用，不是 orphan——之前 ROADMAP 标错过，别再删

### 2. 🖥️ 基础设施快照
- 服务器：localhost(ubuntu)，无远程 GPU 服务器
- 工作目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/`
- 论文目录：`docs/paper/sections/*.tex`，PDF 在 `docs/paper/main.pdf`
- Artifacts：`artifacts/round10_supplementary/` 含 A1-A5 JSON 分析结果
- Checklist 草稿：`artifacts/emnlp_arr_checklist_draft.md`（已校对）
- 无活跃进程、无 tmux、无 cron、无 wandb

### 3. 📊 当前状态
Round 10 全部修复已验证通过（我发了 7 份审查报告，最终全 PASS）。论文提交就绪：
- 15 页 PDF，编译干净（3 个 hyperref bookmark 警告，无实质问题）
- A1-A5 robustness 分析已集成到 Appendix
- Method judge assignment 已修正
- Orphan bib 已清理（van_deemter, lassiter_goodman 删除）
- Checklist 草稿已校对（D2 κ归属、E2 Δ_perturb、Ethics section 引用 三处错误已修）

Registry: 16 experiments 全 DONE（12 success / 3 negative / 1 replaced）。无 RUNNING。
等待：Round 11 审稿结果（已提交 continue 模式），无 pending worker。

### 4. 📋 待办
- Round 11 审稿结果返回 → 按 severity 分级：info 级忽略，warning 级评估是否值得改，critical 级立即派 worker
- 如 Round 11 给 4.0 → 提交就绪，提醒用户填 OpenReview ARR checklist（参考 artifacts/emnlp_arr_checklist_draft.md）
- 如 Round 11 仍 3.5 且有新 critical → 评估是否在 DDL (2026-05-25) 前可修，注意页数余量
- 如有新 worker 改 tex → 必查：(1) judge assignment 未被回滚 (2) 主文未超 8 页 (3) 数值与 artifacts JSON 一致

### 5. 🎯 战略上下文
- 核心结论：policy ambiguity 对 LLM agent 是 universally nocuous (+34.0pp)，incompleteness 是 consistent upper-bound risk type (46-62% across 7 models)，type identity 解释 22× more variance than model identity
- 评分轨迹：3.5 (Round 9) → 3.5 (Round 10, 审稿人说"有 4.0 潜力")。关键瓶颈是 claims-evidence calibration
- 易错点 1：auth scope 52pp range 是 "upper bound with substantial measurement uncertainty"（κ=0.385），不要当成精确估计
- 易错点 2：C3 layer effect 是 inconclusive（p=0.017 但 Holm-Bonferroni 不过），不要说 "significant"
- 易错点 3：Kendall's W 5-model 是 non-significant (p=0.072)，7-model 才 significant (p=0.038)——不要混用
- 易错点 4：A3 judge-group ranking ρ=-0.03 反映 agent composition effect（Group 1 含 DeepSeek+GPT-5.4 高 auth scope 模型），不是 judge bias


---
