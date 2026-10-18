# reviewer / loop_14.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`e668331846a76fc45a3f.json`](../../sessions/e6/e668331846a76fc45a3f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-23T19:49:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文主体 ≤8 页（EMNLP 2026 ARR），Limitations 豁免但不能塞额外内容
- Abstract ≤200 words（当前 ~183 words）
- ARR Checklist 在 OpenReview form 填写，不放 PDF 里（main.tex:50 已正确注释）
- 一篇文章只能有一个 Limitations section，放正文，appendix 不能有
- "73% multi-match rate"（非 "none-rate"）——已全文修正，不要回退
- Appendix Table 17 caption 残留 "format-independent" → 应改为 "no detected format dependence"（上轮审查标 warning，可能尚未修复，需确认）

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874 (root) + westd-24295 (root)
- 代码根目录（远程）：/root/schema-dag-extraction
- 论文源文件（本地）：/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/
- 模型：Qwen3-32B-FP8（cqa1 上 vLLM serving）
- 数据：FewRel /root/schema-dag-extraction/data/fewrel_parquet/
- 无活跃进程：exp_fewshot_bcs_count16 已 DONE，无 RUNNING 实验
- 无 W&B（本项目不用 wandb）

### 3. 📊 当前状态
**Loop #14 完成了全部提交前审查工作。** 论文 submission-ready。

本轮完成的审查：
- 对抗性审稿模拟：Q2 (3/5), Q7 (3.5/5), Q11 (3/5), Q13 (3/5) + 10 个 TP 批量评估
- 叙事一致性检查（多轮，覆盖所有 framing 修改）
- Negative results 叙事审计（9 个 NR，无 omit）
- 两张新图质量审查（Fig 1 framework, Fig 4 SDGD pipeline）— PASS
- Submission-readiness 整篇通读 — READY WITH CAVEATS（仅 Appendix Table 17 一处残留）
- Related work 近期工作检查 — 无重要遗漏
- exp_fewshot_bcs_count16 结果核实 — success，1-shot widening 复现
- 最终 claim 强度评估 — 无 over/under-claiming，无值得跑的新实验

Registry: 全部 DONE，0 RUNNING，0 PREPARING。

### 4. 📋 待办
- Appendix Table 17 "format-independent" 若尚未修复 → 确认是否已改，未改则标 warning 提醒 Director
- 论文提交后（DDL 5/25）→ 切换到 rebuttal 准备模式
- 如果 Director 要求补实验 → 参考本轮结论：没有值得跑的低成本实验，所有核心 claim 已有充分证据
- 如果收到审稿意见 → 加载 rebuttal skill，重点准备 Q7 additivity（kill 3.5/5，论文最薄弱点）

### 5. 🎯 战略上下文
**论文核心结论**：Schema complexity 沿两个维度降解 LLM IE——count (Dim1, 跨任务) 和 confusability (Dim2, RE batch-level, semipartial R²=0.273)。SDGD decomposition 失败（merge amplification + routing failure），但 oracle routing 证明 separability。

**最容易判断错的事**：
- 0.218 出现在 main.tex 里是 Spearman ρ（SCS-confusion, 3160 pairs），**不是** semipartial R² 的旧 bug。Loop #13 handoff 误报了这个，我已在 Loop #14 开头纠正
- DocRED R²=0.578 是 total R²（VIF=50.9 inflate），semipartial R²_BCS 只有 0.056——论文正确地用 FewRel 0.273 作为 primary evidence
- NER BCS null 是 boundary condition 而非 negative result——有机制解释（error mode dispersion + BCS range compression SD ratio 19%）
- TOST additivity 只在 FewRel linear scale 通过（p=0.003），logit scale inconclusive（p=0.209）——Introduction L18 已收窄为 "directionally consistent on DocRED after controlling for BCS range restriction"

**审稿人最可能追问的 Top-3**：
1. Q7 Additivity 只在 FewRel 成立（kill 3.5/5）——range matching post-hoc + MDE=5.5pp underpowered
2. Q13 No solution（kill 3/5）——建议用 "representational challenge" framing 翻转
3. Q2 Effect size 小（kill 3/5）——ecological aggregation + IntraSub 单调性是防线


---
