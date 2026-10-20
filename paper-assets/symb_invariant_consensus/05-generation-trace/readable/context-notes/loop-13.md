# reviewer / loop_13.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`e92b7f3b9b94860ca413.json`](../../sessions/e9/e92b7f3b9b94860ca413.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-25T05:26:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 训练任务，不涉及 GPU 设备号约束。所有实验已完成（176 条 registry 全部 DONE/killed）
- 论文 tex 源在**本地** `projects/symb_invariant_consensus/docs/paper/`，不在远程服务器。审查"是否已改"前先读本地，不要只读远程残留旧版
- Abstract 硬限 200 words（EMNLP 2026），当前恰好 200——任何编辑必须重新计数
- analysis.tex 中 73.5%/26.5% 数据已统一到 n=166 口径（之前 148 vs 166 差异已查明为 answer 归一化问题，已修复）

### 2. 🖥️ 基础设施快照
- 服务器：`westd-16639` + `westd-30973`，代码根目录 `/root/symb_invariant_consensus`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/`
- 论文 tex：`docs/paper/` 下（main.tex, abstract.tex, introduction.tex, experiments.tex, analysis.tex, solutions.tex, discussion.tex, limitations_content.tex, appendix.tex）
- 关键数据文件：
  - `artifacts/_project/data/minority_constraint_direction.json`（MF3 方向分析，n=166 统一版）
  - `artifacts/_project/data/per_problem_cv_values.json`（CV 分布，N=204）
  - `artifacts/review_issues.yaml`（跨轮 issue tracker）
  - `artifacts/review_reports/round_19.md`（= R22 fresh review，3.0→3.5 Borderline Conference）
- 活跃进程：**无**。所有实验已完成，无 RUNNING 任务

### 3. 📊 当前状态
刚完成 R22 最终报告的全面修复审查。Paper Agent 已落地 MF1-3 + 部分 SF。我审查了：
- MF1（标题/Abstract）✅ 标题改为 "Reduce to Majority Voting under Zero-Shot Extraction"
- MF2（SCB vs CoT 分离）✅ analysis.tex L31-35 重构为 3-test + "transparency property" 结论
- MF3（TOST ±2pp）✅ experiments.tex L52 四点先验论证
- 148 vs 166 差异 ✅ 已查明（answer 归一化）并统一到 166
- CV histogram ✅ 已生成（`fig_cv_distribution.pdf`），高 CV 子集 18/18=100% agreement
- Fig 1 v9 ❌ SC 分支 "Majority Vote" 重复，建议保留 v8

**等待中**：Director 对 SF2-SF8 方案的调度决策（Discussion 扩展 PRM/ORM 段、§5 密度、"Symbolic Mirage" 注释等）

### 4. 📋 待办
- SF2 Discussion PRM/ORM 段落 worker 完成 → 审查是否正确连接 DPI bound 与 learned verification，确认 Math-Shepherd/GRACE 引用准确
- CV histogram 嵌入 appendix worker 完成 → 检查 L826 附近插入位置 + caption + 高 CV 子集描述（18/18=100%）
- analysis.tex 73.6%→73.5% 更新 worker 完成 → 核对与 n=166 数据文件一致
- Fig 1 v9 重试 worker 完成 → 检查 SC 分支是否只有 2 节点
- **任何论文章节写作审查请求** → 必须先加载 `skills/global/paper-quality-lessons.skill.md`，按 §5.1 审查维度 + §7 论文写作审计逐项检查
- **全文编译后** → 用 `check_figures_and_layout` 做视觉审查，特别关注 page 30 空页问题和 Figure 3 位置

### 5. 🎯 战略上下文
- **核心结论**：SICA 在零样本自提取下退化为多数投票。SCB 是 transparency property（source-attribution 忠实传递 CoT 分布），不是新 bias。跨架构 NLI verifier 是初步逃逸路径（exploratory, n=6）
- **R22 评分 3.5 Borderline Conference**。MF1-3 已修复，主要提分点在：Discussion 扩展（太短）、§5 密度改善、visual layout 优化
- **易错点**：
  1. Abstract 恰好 200 words，改一个词就可能超限
  2. "preliminary" 在 Intro L27 出现两次同一句（"Preliminary evidence... preliminary capability-gap"），应改第二个
  3. Table 1 caption 很长但 GSM8K/AIME 已不在表中（SF3 已解决，不要重复修）
  4. Discussion 只有 1 段 ~70 words，是 R9-VL4 的老问题，SF2 PRM/ORM 段可同时解决
  5. `fig_cv_distribution` 和高 CV 分析数据就绪但未嵌入 appendix，需 worker 插入


---
