# director / loop_10.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`bcda62d8e74ee0c83de0.json`](../../sessions/bc/bcda62d8e74ee0c83de0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-25T08:08:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- EMNLP 2026 ARR 正文严格 8 页限制，当前恰好 8 页——任何正文内容增加都必须同时压缩等量文本
- Abstract ≤ 200 words，当前 ~140 words，单段不分段
- 论文 PDF 真源在本地 `artifacts/_project/paper/`，不在远程服务器
- 今天 2026-05-25 是 ARR May cycle 的 hard deadline

### 2. 🖥️ 基础设施快照
- 论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/`
- 编译产物：`docs/paper/main.pdf`（由 `paper_compile_and_check` 自动 symlink）
- 最新 PDF：`OntoCoDec_EMNLP2026_v0525.pdf` 已上传飞书 A 群
- 无活跃 GPU 实验——本 session 全程在做论文排版优化
- 无远程服务器活跃进程

### 3. 📊 当前状态
刚完成用户要求的四项修改并上传 PDF：
1. ✅ Related Work 移至 §2（main.tex input 顺序调整）
2. ✅ 摘要合并为单段（abstract.tex 删除空行）
3. ✅ 缩写首次使用规范审计（全文 acronym audit 完成）
4. ✅ 正文图表密度优化（新增 3 张图：scale_dependency/per_relation_dr/framework；因 8 页限制移除了 ablation_waterfall、composability_bar、deployment_tiers、beam_pareto）

当前图表分布：P2 Figure 1, P4 Figure 2, P6 Figure 3, P7 Table 1+2。P1/3/5/8 无视觉元素。

等待：用户对 PDF 的反馈。无 RUNNING 实验，无待处理 cron/worker 回调。

### 4. 📋 待办
- 用户反馈 PDF 有修改意见 → 按意见改 → 重新编译上传
- 用户说"提交" → `submit_paper_to_review` 提交给 Review Director 做最终审查
- 用户要求增加正文图 → 必须同时压缩等量文本保持 8 页（之前已试过加 4 图全部超页）
- Figure 1 (framework) PaperBanana Morandi 色系重做的 agent 状态未知 → 如果用户问起需要重新派

### 5. 🎯 战略上下文
- 论文核心 claim：grammar + semantic 层非加性交互（3% + 24% → 94% DR reduction）
- 主要章节顺序已改：Intro → Related Work → Background → Method → Composition → Experiments → Conclusion
- 易错点：`paper_compile_and_check` 的 max_pages 检查是全文页数（含附录），不是主正文页数。39 页 ≠ 超页，需要视觉检查 page 8/9 边界确认主正文在第 8 页结束
- 易错点：正文加图和 8 页限制存在张力——用户想"每页有图"但实测加到 4+ 张新图就超页。当前 3 张新图 + 2 张表是平衡点
- decisions.yaml 和 paper_framing.md 有完整决策链和 claim 结构


---
