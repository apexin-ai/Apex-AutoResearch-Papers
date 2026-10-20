# analysis provenance audit d105

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_provenance_audit_d105_20260516T045309_result.json`
- **Structured JSON:** [`d6ab0f13a52f29f2f3c9.json`](../../sessions/d6/d6ab0f13a52f29f2f3c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。结果：

**1/3 有真正差异需修复**：
- **c023** (`appendix.tex:150`)：论文写 Q1=0.110→Q4=0.473，实际数据 Q1=0.447→Q4=0.540，且非单调递增。需要修正。
- **c032**：论文当前写 0.011，与 registry 0.0112 一致。"0.002"未在论文中找到。
- **c021**：docs/ 版已修正为 0.089，artifacts/ 旧版残留 0.062 不参与编译。

无 TACRED 进程运行。报告已写入 `artifacts/provenance_audit_d105/audit_report.md` 并注册。

---
