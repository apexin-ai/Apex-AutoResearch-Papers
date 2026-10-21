# paper reference audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reference-audit_20260515T182132_result.json`
- **Structured JSON:** [`b730bb195276ee830ca7.json`](../../sessions/b7/b730bb195276ee830ca7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/reference_audit_report.md` 并注册。

**核心发现：**

| 严重性 | 数量 | 关键问题 |
|--------|------|----------|
| CRITICAL | 2 | `fig:scaling_gap` 和 `fig:oracle_stratified` 有 label 无 `\ref`；`tab:repo_level` CWM 8B 行数据缺失 |
| WARNING | 4 | 3 个 bib key-year 不匹配（`dettmers2024qlora`→2023, `snell2024scaling`→2025, `xia2024agentless`→2025）；2 篇论文会议接收待确认 |
| INFO | 2 | 未使用的 `tabularx` 包；残留旧图片文件 |

**引用完整性**：26 条 bib 条目全部被引用，无缺失引用，无重复，无孤立条目。5 篇抽查引用全部真实存在且信息正确。

**提交前必须修复**：C1（添加图表 `\ref`）和 C2（补充 CWM 8B 数据或移除该行）。

---
