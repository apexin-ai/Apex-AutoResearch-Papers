# paper round3 edits

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_round3_edits_20260521T072827_result.json`
- **Structured JSON:** [`e6c310691bd70aec9f36.json`](../../sessions/e6/e6c310691bd70aec9f36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All modifications complete. Summary:

## 修改报告

### 完成的修改项

| 项目 | 变更 |
|------|------|
| **B1(a)** | 标题改为 "Type-Specific Safety Risks for LLM Agents" |
| **B1(b)** | Introduction 中 "jointly determine" → "type primarily determines severity, with...2.9% of variance" (原文在 intro 而非 abstract) |
| **B1(c)** | Contribution 2 中 C4 降级为 `[Exploratory]`，改写措辞 |
| **B1(d)** | §5.4 subsection 标题加 `[Exploratory]` 标记 |
| **B2(a)** | §5.2 incompleteness 段替换为含 logistic regression、confound-free lower bound、two-tier pattern 的完整讨论 |
| **B2(b)** | §3 Taxonomy incompleteness 定义处加 confound 标注 |
| **B2(c)** | Limitations 中 incompleteness confound 段精简为 2 句，用 "As discussed in §5" 开头 |
| **B4** | §4 Statistical Analysis 加 SESOI ±15pp 论证 + perturbation bound 关系 + sensitivity 引用 |
| **B5** | §4 perturbation control 处加 worst-case 39% / residual ≥20.7pp 分析 |
| **B6** | §6 开头加 GPT-5.4/GPT-4.1 选择原因（跨 judge boundary） |
| **B8** | §6 开头加 failure mode taxonomy 与 input taxonomy 区分说明 |
| **B9** | 新增 cohen_1960、gwet_2014、hu_ambiguity_2025 (arXiv:2505.11679) bib 条目；在 §6 ICR 处加 `\citep{cohen_1960}` 和 `\citep{gwet_2014}`；§6.3 加 `\citet{hu_ambiguity_2025}` |
| **B10/M2** | Appendix B caption: coreferential 排除原因改为 "zero information delta" |
| **B10/M4** | Introduction 首次 "nocuous" 后加 "(i.e., harmful)" |
| **B10/M6** | Figure 3 改为 `figure*` 全宽 |

### B3 压缩

| 位置 | 操作 |
|------|------|
| Discussion "Practical implications" | 12→5 行，保留 -8.5pp、auth scope vs incompleteness、Claude 0pp、externalized 结论 |
| §6.1 + §6.2 | 合并为单一 "Type-Specific Failure Mechanisms" subsection，删除冗余 per-model 百分比 |
| §5.2 TOST sensitivity | 3→1 行 + Appendix 引用 |
| §5.1 variance decomposition | 压缩为 1 句 |
| §5.3 C3 layer effect | 2 段→1 段，保留关键数字 |
| §5.4 C4 within-judge + Fleiss κ | 压缩为 2 句 |
| §5.4 C4 interaction patterns | 压缩为列表式 1 句 |
| Discussion "Differential Nocuity" | 5→4 行 |
| Discussion "Safety training" | 删除冗余解释 |
| Systematic Nocuity | 压缩为 3 句 |
| Conclusion | 微调合并 |

### 最终结果
- **总页数**: 12 (8 主文本 + Limitations + References + Appendix)
- **主文本**: Conclusion 在第 8 页结束，符合 EMNLP 2026 8-page 限制
- **编译**: 无 citation/reference warning，仅 hyperref 标题 token warning（无害）

---
