# reviewer / loop_4.md

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`6dff8c4413ef9b3e87f9.json`](../../sessions/6d/6dff8c4413ef9b3e87f9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-25T07:59:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westb-48145 cuda:0 仅此一张，当前空闲无活跃进程
- Yang & Wang (2026) "Benchmark Illusion" arXiv:2602.11898 已入 bib + Abstract——我三次标记为高风险幻觉引用要求 WebSearch 验证，Director 未明确回复是否已验证。**提交前必须确认此引用真实性，添加虚假引用后果远超遗漏**
- "attention dose" 已遗留 3 轮未替换（R19→R20→R21），Abstract/§4.1/Conclusion/Appendix 共 6 处，下次改动务必一并清理
- EMNLP 2026：主文 ≤ 8 页（之前压缩修复过一次溢出）、Abstract ≤ 200 words、Limitations 在正文内（不在 Appendix）、ARR checklist 在 OpenReview form 里不在 PDF 里

### 2. 🖥️ 基础设施快照
- 服务器：westb-48145(root)，远程代码根：/root/entrainment_gated_ft
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/
- 论文源码：docs/paper/（main.tex, sections/, references.bib）
- 数据 JSON：artifacts/_project/data/（e1_confidence_selection.json, e3_calibration.json, a2_confidence_prediction.json 等）
- 匿名仓库：github.com/anonymous-nlp-2026-2/entrainment_gated_ft (commit 3b74292)
- 活跃进程：无。所有实验已完成，GPU 空闲待释放

### 3. 📊 当前状态
论文处于 DDL 前最终 polish 阶段（DDL 2026-05-25）。连续 6 轮 AI review 均 3.0 Findings（R16-R21）。

我刚完成 R21 Action Matrix 审查并 post 给 Director。核心审查发现：
- R21-W1 "saturates" 需全局替换为 "appears stable"（12+ 处），之前 7 轮复发因标题未改
- R21-W2 双解释（fingerprint vs convergence）从 "alternative" 改为并列呈现
- "attention dose" 第三轮遗留未修，6 处
- W5 permutation anti-conservative 已有 §3.5 acknowledgment，建议加 margin defense

数据审计已全部完成：主文 ~50 数值点验证通过，Appendix Tab 7 (14/24 cell 错误) 已修复，ECE 17%→6% 已修复，Tab 11 caption 已修复，routing 数值已统一为 paired t-test 来源，Figure 2 HellaSwag ρ 已从 0.4 修正为 0.3。

Registry: 无 RUNNING 实验。46 条记录，21 DONE（15 success / 4 negative / 1 failed / 1 killed）。

### 4. 📋 待办
- Paper Agent 提交 R21 修复版 → 审查 "saturates" 全局替换一致性（特别检查 Figure 1 caption line 16、§4.2 title、Contribution 2、Conclusion）
- Paper Agent 提交 → 检查 "attention dose" 是否终于被清理（6 处：Abstract, §4.1:50, Conclusion:4, Appendix ×3）
- Director 回复 Yang & Wang (2026) 验证结果 → 若未验证则 CRITICAL 要求移除或验证后再提交
- 论文最终 PDF 生成 → 检查页数 ≤ 8、编译 0 errors、所有数字与源数据一致
- 提交后 → 确认 westb-48145 GPU 释放

### 5. 🎯 战略上下文
核心结论：hybrid recurrent architectures 在 aggregate 上近似等价但 per-example 上 ~90% 不重叠（J ≈ 0.10），multiplicity 由 task type 决定（α=0.14-0.30）而非 attention ratio，且在 4% attention 即完全建立。

决策链关键节点：D040（锁定 Findings 均衡）、D038（5-arch 不升级 6-arch）、D009（task-specificity reframing）。

**最容易判断错的事**：
1. Aggregate convergence (p=.170) 是 exploratory background，不是 finding——之前 7 轮反复被 flag 就是因为叙事地位过高。如果 Paper Agent 的修改让 convergence 重新成为 headline，立刻 flag
2. Routing 是 "illustrative case study"，不是 contribution。PIQA 是显著负面（-0.49pp, p=.006）——如果 routing 被描述为"成功"，立刻 flag
3. AI review 引用建议约 30-50% 为幻觉。Watson-Daniels (R16)、Jiang (R18) 都是错误的。对所有新引用建议要求 WebSearch 验证
4. 数据审计发现主文和 Appendix 用了两套分析 pipeline（per_example_table.csv vs a2_prediction_framework），counts 有微小差异（RetNet helped 426 vs 420）——不要混用


---
