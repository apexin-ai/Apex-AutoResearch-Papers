# research paper status audit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper_status_audit_20260521T225539_result.json`
- **Structured JSON:** [`fce8d4a310524008c5ab.json`](../../sessions/fc/fce8d4a310524008c5ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计报告已写入 `artifacts/paper_status_audit.md`。

核心结论：

**论文主体已基本完成**——8个 LaTeX section 全部有实质内容，12张表格已填数，5张图已生成，references.bib 301行。evidence_tax 数字修正（+7.5→+0.25, -6.2→-5.63）已应用到 .tex。dev_test_gap 段落已整合到 appendix。

**3个 CRITICAL gap：**
1. **DocRED 官方 test set 缺失**——只有 Re-DocRED test，CodaLab 未提交
2. **SFT test baselines 全部缺失**——test 表无法计算 RSFT gain
3. **4B test checkpoint 不可恢复**——test 表缺 4B 行

**需要立即验证的：**
- LaTeX 编译（figures 路径是否对齐、页数是否 ≤8 页主文）
- 全文 grep 旧数字残留（"+7.5" / "-6.2" / "non-monotonic"）
- flat-NLI Ign-F1 和 14B RSFT 详细指标在附录表中仍为 "--"

---
