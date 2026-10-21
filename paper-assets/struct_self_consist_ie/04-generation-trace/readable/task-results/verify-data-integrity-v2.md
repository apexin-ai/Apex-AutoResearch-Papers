# verify data integrity v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_data-integrity-v2_20260516T024719_result.json`
- **Structured JSON:** [`e300a2cd24250da54192.json`](../../sessions/e3/e300a2cd24250da54192.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计报告已写入 `artifacts/review_reports/data_integrity_audit_v2.md`。

核心发现：

**需立即修复（2处）：**
- **Table 5** 4B CoNLL：SJ .422→.432，FK .418→.424（源数据 0.4324/0.4244 被错误截断）
- **Table 3** FK NER N=16：.280→.281（0.2809 标准四舍五入应为 .281）

**需追溯来源（2处）：**
- Table 3 RE N=16 SJ=.281 和 FK=.279 在三条不同 pipeline 中均找不到精确匹配，三条 pipeline 对同一 seed42 配置给出不同值（SJ: 0.244/0.277/0.292），说明存在 instance filtering 或信号实现差异
  
**全部通过（其余）：**
- Table 1 全部 40 个值 ✅
- Table 2 选择 F1 及 +2.3pp 声明 ✅
- Table 3 T=0.7 行 ✅
- Discussion n=81 子集（Voting ρ=0.630, SJ ρ=0.502）✅
- 28 个行内数字与表格交叉验证 ✅
- Freeform 消融附录表 ✅

---
