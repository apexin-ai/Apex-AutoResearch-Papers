# reviewer / loop_5.md

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`be95c9c8e27ba16bfed9.json`](../../sessions/be/be95c9c8e27ba16bfed9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-24T19:37:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 DDL 是 **2026-05-25**（明天），所有修改必须以不破坏现有论文为前提
- 服务器账号是 **sonny**（不是 root），home-1x5090 上 `/root/miniconda3` 无权限
- 工作树有 **25 个文件未 commit**（table overflow fixes、fig2/3/4/7 更新、italic cleanup 等），提交前必须 commit 否则不进 PDF
- EMNLP 2026：正文 ≤8 页（Limitations 不计入但 Conclusion 计入），abstract ≤200 words，单一 Limitations section（appendix 不能有）
- 论文中 "sign_flips: 0" 指 **primary coefficient** sign flip（plan006 定义）；HumAID K=10 的 7/8 exposure sign flips 是 **secondary coefficient**，两者定义不同，引用时必须区分

### 2. 🖥️ 基础设施快照
- 服务器：**home-1x5090 (sonny)**，代码根目录 `/home/sonny/causal_annot_error_attrib`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/`
- 论文源文件：`docs/paper/`（main.tex 入口），artifacts 目录存实验结果 JSON
- GPU：1× RTX 5090，**已通知 Manager 释放**（D021），本项目不再需要 GPU
- 活跃进程：无（所有实验已完成）
- 标注数据：`/home/sonny/causal_annot_error_attrib/results/{humaid,vast,civil_comments}/` — 36/36 JSONL + 36/36 NPZ 齐全

### 3. 📊 当前状态
**所有实验已完成**，registry 16 个实验（15 success + 1 failed/plan003 API 402 搁置）。无 RUNNING/PREPARING。

本轮审查已完成：
- 终稿数据审计 4 项全部 PASS（adversarial numbers、DGP table、cross-refs、MAPE 1.6%）
- HumAID K=10 分析审查 PASS（数据一致，与 plan006 兼容）
- 标注补跑 36/36 审查 PASS
- Fig2 resize / fig fix / italic cleanup / formula dedup / table overflow fix 全部审查 PASS
- ROADMAP 审查 PASS
- 3.5→4.0 评估已提交：MF-1/2/3 + SF-3 四项已在 commits bb8c468/c9b3b2b 完成，差距是结构性的（Conjecture 1 未证明 + 无完全真实案例研究）

等待中：无 worker、无 cron、无 pending Director 决策。

### 4. 📋 待办
- **Agent commit 未提交修改** → 验证 `git diff --stat HEAD`，确认 25 个文件变更已 commit
- **最终编译后** → 确认正文 ≤8 页（之前缺 fig3/fig4 时 Conclusion 在 page 9，图补全后应恢复）
- **Director 发来 PDF 视觉审查请求** → 用 `pdf_to_images` + `paper-visual-review` skill 检查排版
- **收到新 worker_done 通知** → 按标准流程审查（读 result JSON → 交叉验证数据 → post_to_director）
- **收到 paper_agent_request_review** → 使用 §5.3 评分模板（维度评分 + Overall + 具体问题）

### 5. 🎯 战略上下文
- 项目核心结论：K≥3 多分类标注误差 × 7 DAG 拓扑 = 质变（exposure/IV 可翻转符号，5 个拓扑保符号）；FWL 使 4 个 covariate 拓扑的矩阵校正证明无效；ASV 给出拓扑依赖的脆弱性排序
- Round 23 评分 3.5 (Borderline Conference)，稳固但无 quick win 推至 4.0
- **易错判断**：不要因为 DDL 紧而建议"降级 venue"——这不在 Reviewer 职责范围；也不要套人类工时直觉判断"做不完"
- **Conjecture 1 状态**：K=2 已证（Theorem 1）、K=3 symmetric 已证（Theorem 2）、general K≥3 有 545K+ 数值证据（ε<0.017）但未证明。standalone proof (`artifacts/conjecture1_diagonal_dominant_proof.tex`) 有 K=2 tightness 数学错误（DD condition ≠ a+b≥1），但该文档不在论文中，不影响提交
- **plan003 qwen3_few-shot-5 "402 错误"**：是真实 API 402（非 sample index），数据后来 May 22 被重新标注。Worker 的解释有误但数据已修复


---
