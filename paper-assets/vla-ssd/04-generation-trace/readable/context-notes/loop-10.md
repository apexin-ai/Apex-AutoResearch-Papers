# director / loop_10.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`058daa3ad09cee223884.json`](../../sessions/05/058daa3ad09cee223884.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-25T19:15:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- experiments.tex line ~176-179 "a first cross-architecture decomposition" — **禁止删除 "first"**，Reviewer 确认事实准确，Agent 已两次误删被手动恢复（M021）
- GPU 只能用 westd-19183 分配的卡，用户指示保留 1 张，已通知 Manager 释放另 1 张（执行状态未确认）
- 用户说"不用等我回 OpenReview"——提交操作由用户自己处理，不要催促 OpenReview 账号/作者信息
- 论文正文严格 ≤8 页（CoRL 硬限），当前 Conclusion 刚好在 p8 结尾，任何正文改动都要 paper_compile_and_check 确认页数

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183，2× RTX PRO 6000（用户指示保留 1 张）
- 论文源码：`projects/vla-ssd/docs/paper/`（main.tex 入口）
- 终版 PDF：`projects/vla-ssd/artifacts/_project/paper/VLA-SSD_终版v11_20260525.pdf`
- submission_fields.md：`projects/vla-ssd/docs/paper/submission_fields.md`（Title/TL;DR/Abstract/Keywords 已完整）
- 无活跃进程，无 RUNNING 实验，Agent/Reviewer/Worker 全部空闲
- 审稿群：review_chat_id `oc_554a5023cde4d603635cf97e6ab8151a`

### 3. 📊 当前状态
论文 v11 终稿已完成并上传飞书。两轮全文精读（19 处语言优化 + 3 个 caveat 恢复 + 8 页压缩）。Reviewer 最终评估中稿率 47-62%。

- 实验：107 success / 17 negative / 7 failed / 154 total，全部 DONE
- 统计加固：seed robustness (std<0.02) + bootstrap CI (MCCV 1000 iter) + permutation test (p=0.008)
- 0 个 RUNNING/PREPARING 实验
- 无等待中的 Worker 回调或 Cron
- Abstract DDL 5/26 11:59 UTC，Paper DDL 5/29——用户自行操作 OpenReview 提交
- plain-text abstract 已发给用户（154 词，ΔR²/d 转 Unicode）
- Primary Keyword 已回复用户："Learning representations for robotic perception and control"

### 4. 📋 待办
- 用户问提交相关问题 → 立即回复，所有材料已在 submission_fields.md
- 用户要求继续改论文 → 派 Agent 执行，改完 paper_compile_and_check 确认 8 页
- 审稿报告回来（review_chat_id 群） → Read `skills/global/review-report-action.skill.md` 按协议处理
- Paper DDL 5/29 前用户要求最终 PDF → 编译并上传
- Reviewer 独立评估已确认"无 GPU 实验值得跑"（详见 Reviewer 逐项分析），如果新 Reviewer 有不同看法可重新评估
- GPU 释放状态待确认 → 可向 Manager 查询

### 5. 🎯 战略上下文
- 核心发现：R² exit collapse 在所有 VLM→VLA 转换一致出现（6/6, ΔR²=0.156-0.455），VLA→VLA 无 collapse（0/4, ΔR²=0.033-0.086），3 个 NLP controls 全部 ΔR²=0.000
- 论文定位：分析型论文（非 method paper），贡献是 cross-architecture representational characterization
- 最弱点：behavioral correlation ρ=0.583, p=0.10, n=9——underpowered 但 effect size large。闭环 eval infra 不可行（registry 证明所有尝试 SR=0），这个弱点无法在 DDL 前修复
- 竞品：Kachaev et al. 做 visual representation collapse（t-SNE），我们做 layer-wise ΔR² across architectures——Related Work 已清晰定位差异
- 易错点：Agent 倾向删除 "first" claim（已发生 2 次），必须用 [DO NOT CHANGE] 标记保护；Discussion 压缩时容易丢 caveat（confound/open-loop/ρ effect size），改 Discussion 后必须让 Reviewer 验证 caveat 完整性
- 决策链：D095-D105 记录在 decisions.yaml，关键转折点是 D101（Round 15 审稿 Weak Reject → 统计框架重构 + NLP control 扩展）和 D102（从 significance testing 转 effect size threshold）


---
