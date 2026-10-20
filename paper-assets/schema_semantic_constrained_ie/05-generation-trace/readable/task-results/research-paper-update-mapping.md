# research paper update mapping

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper_update_mapping_20260516T001755_result.json`
- **Structured JSON:** [`db1258cf814928f6fea5.json`](../../sessions/db/db1258cf814928f6fea5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册为 artifact `art_20260516_d100d9`。

**共发现 13 个需更新的位置**，按优先级：

**必须更新（6处）**：
- **U1** `section5_composability.tex` Table `tab:composability` — 加 8 行 DocRED FT 数据（最复杂，需重构表格加 Dataset 列）
- **U2–U5** 同文件 3 个段落 + 表标题 — 当前所有讨论只覆盖 SciERC FT，需补 DocRED FT 数字和分析
- **U6** `main.tex:69` Limitations — 删除 "DocRED fine-tuning is not reported" 声明

**需要更新数字（3处）**：
- **U7** `main.tex:65` — CF 上界 "≤1.18%" 可能需根据 DocRED FT CF 调整
- **U8** `main.tex:68` — Entity F1 在 FT 下的行为需扩展到 DocRED
- **U9** `section7_conclusion_compressed.tex` — "45–99% DR reduction" 范围可能需更新

**建议更新（4处）**：
- **U10** `section1_introduction_draft.tex:27` — Contribution #3 可加 "both ZS and FT"
- **U11** `abstract.tex` — 加一句 composability 结论
- **U12** `appendix_discussion.tex` — 将前瞻性声明替换为直接 FT 证据
- **U13** `paper_tables_draft.tex` Table 4 TBD — 仅参考文件，低优先级

**关键分析点**：DocRED FT 的 CF 行为和 tightness × FT 交互效应，可能产生新发现值得讨论。

---
