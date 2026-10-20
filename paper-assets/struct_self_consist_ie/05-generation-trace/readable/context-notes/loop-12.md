# director / loop_12.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_12.md`
- **Structured JSON:** [`44a2d63543026b1cfd8e.json`](../../sessions/44/44a2d63543026b1cfd8e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_messages
updated: '2026-05-24T01:31:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 autodl-5090 的 cuda:0-3（4张5090），不可用其他服务器的卡
- SciERC construction 数字在论文中保持 +0.32pp n.s.（单种子 seed42），不要更新为 5-seed +1.11pp——原因是三张表的 SciERC greedy baseline 不一致（.667/.663/.647），贸然改一个会引发 cross-table 矛盾
- tab:scale_comparison（appendix L1606）使用 entity-type-averaged macro-F1（Greedy=.667），tab:selection（主表）使用 instance-averaged macro-F1（Greedy=.645）——两个都是对的，不要统一
- 匿名 repo 用 HTTPS+token 认证推送，路径 /tmp/anon_repo/，最新 commit 70ed395

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090，4×RTX 5090，当前全部空闲
- 本地论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/
- 编译：pdflatex，main.tex → main.pdf（46页，8页正文+38页appendix）
- 产出目录：projects/struct_self_consist_ie/artifacts/（含 scierc_5seed_construction_report.md, inverse_scaling_summary.json, multiseed_flip_overlap_analysis.md 等）
- 无活跃进程/tmux/cron 任务，所有实验已完成

### 3. 📊 当前状态
- R41 审稿已提交（apr_20260523T210143_2pos），待用户在飞书卡片确认审稿模式（推荐 continue）——已催用户 3 次，未回复
- Paper Agent 已派单做 DDL 前 writing polish（camera-ready 检查、caption 精炼、tab:scale_comparison 脚注），等待回调
- Registry: 0 RUNNING, 0 PREPARING，205 成功 / 55 负向 / 16 失败 / 共 311
- 本轮完成的关键修复：SciERC EM AUROC .749→.631（copy-paste bug）、headroom 11.4→13.0pp（4处）、MV +0.61→+0.6pp、bib 清理（3修正+12孤立删除）、ARR checklist 15/15、匿名检查通过

### 4. 📋 待办
- 用户确认 R41 审稿卡片 → 审稿团队启动新一轮审查，重点验证本轮 3 个数据修复
- Paper Agent writing polish 完成 → 检查修改、重新编译、推送匿名 repo
- 审稿报告返回 → 按 review-report-action skill 处理（Holistic Pass + Per-Comment Action Matrix）
- 如果用户要求补实验 → 4张5090可用，可立即安排 ablation/robustness check
- DDL 5/25 到了用户仍未确认审稿 → 直接编译最终版提交（contingency）

### 5. 🎯 战略上下文
- 论文核心发现：test-time scaling 对 NER 存在 correlation-selection gap（QE 信号有预测力但 selection 无增益）；degeneracy + signal alignment collapse 是联合失败条件；entity construction 在低 degeneracy 下有条件增益但 Holm 校正后仅 suggestive（p_adj=0.055）
- 最大风险：SciERC 跨表 greedy baseline 不一致（.667/.663/.647）——这是已知问题，决策是保守不改。如果审稿人追问，camera-ready 时统一 F1 计算方法是正确解法
- 易错点：不要把 tab:scale_comparison 的 .667 改成 .645，那会破坏该表的内部一致性（72B ZS 行也用 entity-type-averaged）
- Figure 1 最终版仍等用户确认
- 关键决策链：D001-D069 在 decisions.yaml，错题本 M069（EM AUROC copy-paste）在 mistakes.yaml


---
