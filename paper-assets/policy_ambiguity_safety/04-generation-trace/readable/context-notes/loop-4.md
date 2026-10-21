# director / loop_4.md

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`7d5c854e129ba7f2922c.json`](../../sessions/7d/7d5c854e129ba7f2922c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-25T03:21:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 分配（纯 API 实验 + 论文写作阶段），不要尝试分配或使用 GPU
- Fig 8b Jaccard 矩阵的权威数据源是 `artifacts/bootstrap_jaccard_ci.json`（从原始 judgments.jsonl 计算），**不是**之前对话中所谓的"Reviewer-verified originals"——那些值是错的，已在本轮修正
- Permissive attractor 数据源是 `artifacts/convergence_analysis/attractor_pattern.md`
- 图表生成脚本 `/tmp/upgrade_all_figures_v4.py` 是临时路径，重启后会丢失，需要持久化到 artifacts 或 docs 目录
- EMNLP 2026：主文本严格 8 页，abstract ≤ 200 words，limitations 一小段即可

### 2. 🖥️ 基础设施快照
- 本地 workspace：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/`
- 论文目录：`docs/paper/`（main.tex + sections/*.tex + figures/*.pdf）
- 实验数据：`artifacts/full_study/`（judgments、analysis、statistics）
- PaperBanana venv：`/tmp/pb_venv/`（paperbanana 0.1.2，Google API Key 额度已耗尽）
- 图表脚本：`/tmp/upgrade_all_figures_v4.py`（v4 最终版，包含 PB-harmonized style_config）
- 无远程服务器、无活跃进程、无 cron 任务

### 3. 📊 当前状态
刚完成 PaperBanana 引导的全部 6 张统计图美学升级 + 数据准确性审计修正：
- 6 步工作流：PB 折线图参考 → matplotlib 复刻 → 提取设计语言 → 统一应用 → 编译验证
- 数据审计发现 Fig 8b Jaccard 矩阵 9/10 值错误 + Fig 8a attractor 3 处四舍五入偏差，已全部修正
- 论文编译通过：26 页（8 页主文本 + appendix/references），无 critical warnings
- Registry 无 RUNNING/PREPARING 实验
- 项目处于审稿阶段（review_chat_id 已配置，Group C 独立审稿团队运作中）

### 4. 📋 待办
- 用户要求新的图表修改 → 用 `/tmp/upgrade_all_figures_v4.py` 修改后重生成（注意 v4 在 /tmp，考虑持久化）
- 收到 Group C 审稿报告 → Read `skills/global/review-report-action.skill.md`，按 Holistic Pass + Action Matrix 处理
- 用户说"提交审稿"/"重新审稿" → 调 `submit_paper_to_review`
- Google API Key 补充 → 可继续 PaperBanana 3 图型参考方案（当前因额度耗尽只完成了 2 张 PB 参考 + 手动补充第 3 种）

### 5. 🎯 战略上下文
- 论文核心贡献：(1) 首个 matched-pair 因果研究证明 policy ambiguity 导致 LLM agent 安全违规 (+34.0pp)；(2) convergent nocuity——模型收敛到同一错误解读，agreement-based 监控失效
- 当前阶段是论文 visual polish，实验已全部完成，数据已冻结
- 最容易判断错的事：Jaccard 值的"正确性"——之前有过多轮混乱（Reviewer 验证了错误值、Agent 多次用错数据），**唯一权威来源是 `bootstrap_jaccard_ci.json`**，其汇总统计与论文正文完全匹配
- 图表风格：v4 使用 PB-harmonized 配色（#C0392B spec red, #2C3E50 ling navy），serif 字体，暖红 colormap，仅左/底 spine


---
