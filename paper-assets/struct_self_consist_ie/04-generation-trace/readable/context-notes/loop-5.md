# director / loop_5.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`740bca170ba14ff842a6.json`](../../sessions/74/740bca170ba14ff842a6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-15T15:25:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 autodl-5090 的 cuda:0~3（4× RTX 5090 32GB），不可跨服务器抢卡
- 论文数字必须来自 D080 统一管道（旧管道有 gold-empty + FK 空集两个 bug），任何新分析必须走统一管道
- SciERC NER AUROC 正确值：VC .663, SJ .650, FK .602, EM .614, LP .578（D084/D085 确认）
- CoNLL FK ρ 已从 0.81 修正为 0.48（D080），不可回退
- report.md AUTO-FACTS 区禁止手写，只能通过 auto_build_report_facts 刷新

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (connect.bjb1.seetacloud.com)，root 用户
- 工作目录：/root/autodl-tmp/struct_self_consist_ie
- Python：aml-train 镜像，conda base 环境，/root/miniconda3/bin/python
- HF cache：/root/autodl-tmp/.hf_cache
- 活跃进程：无（全部实验已完成，4 GPU 空闲待命）
- W&B：未配置

### 3. 📊 当前状态
- 刚确认 Paper Agent D085 修改全部到位（与 D084 相同，无增量改动）
- Round 8 fresh review 已提交，等待审稿结果返回
- Registry: 83 实验全部 DONE（46 success / 20 negative / 1 failed），无 RUNNING/PREPARING
- 无待处理 Worker 回调，无 pending cron，Agent 空闲（idle 280s+）
- Research Reviewer 刚触发 RESET（5h3m 硬限）

### 4. 📋 待办
- Round 8 审稿报告返回 → 按 review-report-action.skill.md 走 Holistic Pass + Per-Comment Action Matrix，读 review_issues.yaml 对照历史
- 审稿发现新问题需补实验 → 4 GPU 待命可立即派 Agent
- 审稿通过 / 收敛 → final polish → 提交（DDL 2026-05-25，剩 10 天）
- 审稿期间 GPU 空闲 → 考虑铺 supplementary 实验或 reviewer 可能追问的 ablation

### 5. 🎯 战略上下文
- 核心发现：universal correlation-selection gap——5 类置信信号在 IE test-time scaling 中存在 score compression（controlled ablation 证明是 model/task intrinsic，非 constrained decoding artifact）
- 已过 7 轮审稿。Round 7 暴露两个系统性问题均已修复：(1) Claim-Evidence Scope Mismatch → definitional vs empirical 拆分 + scope 降级 (2) Statistical Foundation Gaps → ρ 统一管道 + 多项统计补充
- 投稿目标：EMNLP 2026 Findings，DDL 2026-05-25
- 易错点：experiment_plan.yaml 的 read_experiment_plan_with_status 工具当前有 bug（unhashable list），需直接读文件
- 易错点：不要因"审稿阶段无实验"就建议归还 GPU——归还只在 archive_project 时自动触发
- D080 是关键转折决策：统一管道修正了所有 ρ 值，后续所有数字以此为准


---
