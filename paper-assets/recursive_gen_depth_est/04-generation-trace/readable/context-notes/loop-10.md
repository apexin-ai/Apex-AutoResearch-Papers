# director / loop_10.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`48419403a55ad9a49b84.json`](../../sessions/48/48419403a55ad9a49b84.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-22T18:16:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文禁止使用 em dash (—)，用逗号或括号替代
- EMNLP 2026 主文严格 8 页限制，Limitations/Ethics 不计入
- discussion.tex 中有 7B scale templates（注释块），等 qwen25_7b_selfref_001 实验结果到达后才能 swap in，不要提前取消注释
- 用户已连续取消多轮 paper audit，除非用户主动要求，不要触发新的 audit

### 2. 🖥️ 基础设施快照
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/`
- 主 tex：`main.tex`，编译引擎 pdflatex
- 实验服务器：通过 Agent 操作远程服务器，具体 SSH host 见 `list_ssh_hosts`
- 实验 qwen25_7b_selfref_001 在 cuda:0 上运行（session 开始时约 15-20% 进度，预计已接近完成或完成）
- 项目 GPU 分配需通过 `get_project_status` 确认

### 3. 📊 当前状态
本轮主要工作是论文一致性修复和页数调整：
- 修复了多处数字不一致（Table 20/21 AUC 值、Table 7 CPI 数据、180K/140K 计数澄清、curation PoC 选择性报告）
- 修复了多处交叉引用错误（`sec:gen:crossstrategy` → `app:prompted_gen`、`sec:gen:accumulation` → `app:accumulation_auc`）
- Limitations 去掉了所有具体数字，改为定性描述
- Discussion 新增 "Outlook" 段落，主文恰好填满 8 页
- Table 1 改为 `tabular*` 全宽、atlas Table 3 特征缩写统一、intro/method/theory 多处精简
- 源码 critical 从 3 降到 0
- qwen25_7b_selfref_001 实验状态需检查（可能已完成）

### 4. 📋 待办
- qwen25_7b_selfref_001 完成 → 检查结果 → 根据准确率选择 discussion.tex 中 VERSION A (≥60%) 或 VERSION B (40-60%) 模板 swap in → 更新 abstract/appendix 中 scale 相关叙述
- 用户可能继续发现一致性问题 → 逐条验证后修复
- 如用户要求重新 audit → 跑 `paper_compile_and_check` + `submit_paper_to_review`（注意 content agent 容易超时）

### 5. 🎯 战略上下文
- 论文定位：benchmark-driven empirical study，非方法创新。核心贡献是任务形式化 (ordinal depth estimation) + EDD 度量 + Depth Degradation Atlas
- Round 18 审稿评分 3.0 (Findings)，4 个 critical：方法无创新、full-replacement 假设、14B EDD=0、跨策略迁移弱。用户已取消该轮审稿，未做后续处理
- DDL：2026-05-25 (ARR May cycle)，今天 05-22，还有 3 天
- 易错点：grep LaTeX 文件时注意转义下划线（`\_` vs `_`），之前因此漏掉了 page 23 的未定义特征名
- 页数极其敏感：主文恰好 8 页，任何增删都需重新编译确认不超/不缺


---
