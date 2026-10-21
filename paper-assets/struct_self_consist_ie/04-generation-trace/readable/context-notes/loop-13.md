# director / loop_13.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_13.md`
- **Structured JSON:** [`41959086178236b9c155.json`](../../sessions/41/41959086178236b9c155.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_messages
updated: '2026-05-24T23:25:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 实验（纯论文写作阶段），不涉及 GPU 分配/服务器
- EMNLP 2026 主文 8 页硬限制（Limitations + References 不计入）。当前刚好 8 页，任何正文增加都需要同步缩减其他部分
- Abstract 不超过 200 词（当前 ~172 词，余量约 28 词）
- 论文 `\enlargethispage{3\baselineskip}` 在 Section 8 前，删除可能导致超页
- Fig 1 已缩到 0.92\textwidth，不可再缩（再小细节看不清）

### 2. 🖥️ 基础设施快照
- 工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/`
- 论文源码：`docs/paper/main.tex`，PDF：`docs/paper/main.pdf`
- 图表脚本：`docs/paper/figures/_gen_*.py` + `gen_fig_overview.py`
- 配色已统一到 overview 色系：Blue=#3B7DD8 (FewNERD), Amber=#E8930C (SciERC), Green=#43A047 (CoNLL)
- review_issues.yaml：`artifacts/review_issues.yaml`
- 审稿报告：`artifacts/review_reports/round_45.md`（由系统自动存档）
- 无活跃进程/GPU/tmux/cron

### 3. 📊 当前状态
**刚完成**：曹晓玉三项修复（超页、Fig 3/4 图例白底、Fig 1 缩小）+ 段落间距收紧（titlesec）+ Limitations 分页到 p9 + 全部统计图配色统一到主图色系。已编译验证。

**正在处理**：Round 45 审稿报告（Overall 3.0 Findings）。已完成：
1. ✅ 逐条分析 + 复发标注
2. ✅ 逐条 Action Matrix 初稿
3. ✅ 已 `post_to_reviewer` 发给 Research Reviewer 独立审视
4. ⏳ 等待 Reviewer 反馈 → 综合定稿 → 派 Agent 执行

**审稿提交**：Round 45 审稿已由运维指令直接提交（`submit_paper_to_review`，approval_id: apr_20260524T224818_ac2t，continue 模式）。

### 4. 📋 待办
- Reviewer 反馈到达 → 综合定稿 Action Matrix → 派 Paper Agent 执行论文修改（全部为写作修改，无需补实验）
- 修改完成后 → 要求 Agent 将修后段落 + 原始审稿意见发给 Reviewer 验证 → PASS 后标 resolved
- 全部 resolved → `update_review_issues` 更新状态 → 重新编译 → 考虑是否再提交一轮审稿

### 5. 🎯 战略上下文
**论文定位**：negative result paper（SC 对 NER 无效），建设性部分（entity construction）统计边际。审稿人评 Findings 合理。

**核心修复优先级**：
1. R45-N1 (Must-Fix, 复发×2)：收窄 abstract/intro scope 至 "7-14B fine-tuned"。**不补实验**（审稿人同意 claim 收窄路线）
2. R45-W1 (复发×3)：entity construction 在 abstract/Figure 1 降低展示权重
3. R45-W2 (复发×2)：Introduction 增段分离 discovering vs diagnosing the gap
4. R45-W6 (新)：Section 8 加 practical implications（2-3 句）

**易踩的坑**：
- 页面空间极紧张（8 页满），任何正文增加（W2 增段、W6 加 practical implications）必须同步找到等量可缩减内容
- R45-N1 是复发问题，上轮只在 Limitations 声明被审稿人升级——这次必须在 abstract/intro **正面** 限定，不能再只放 Limitations
- R45-W1 的 entity construction 已复发 3 轮——只改措辞不够，需要降低其在论文叙事结构中的地位（如从三大贡献之一降为附带探索）
- Table 1 novelty comparison（R45-W5）也是复发——上轮精简维度不够，这次需要主动暴露本文弱项维度


---
