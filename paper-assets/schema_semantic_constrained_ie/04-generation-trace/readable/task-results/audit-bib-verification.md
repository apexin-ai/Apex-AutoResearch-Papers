# audit bib verification

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bib-verification_20260522T125257_result.json`
- **Structured JSON:** [`f0e8b4fbe0d304f14a52.json`](../../sessions/f0/f0e8b4fbe0d304f14a52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**Part 1 — arXiv:2510.01409 (`ontologx_2025`)**：条目已正确，无需修改。标题 "OntoLogX"、作者 Cotti 等人、年份 2025 均与真实论文一致。正文中也未出现 "OntologyCL" 错误名称。

**Part 2 — 全 bib 核查结果**（60 条逐条验证）：

修正了 4 个错误：

| 条目 | 问题 | 严重性 |
|------|------|--------|
| `paolini2021tanl` | 作者完全伪造：Akyürek/Oğuz 不是该论文作者，真实作者为 Paolini+Athiwaratkun+Krone 等 9 人 (AWS) | ❌ 严重 |
| `boostcd2025` | 多出 2 个伪造作者 Geng/Josifoski（被混淆为另一篇 geng2023gcd），真实作者仅 Sakota+West | ❌ 严重 |
| `ugare2024syncode` | 会议错误：标注为 ICML 2024，实际发表在 TMLR | ⚠️ 中等 |
| `ugare2025itergen` | 作者错误：Banerjee→应为 Gumaste | ⚠️ 中等 |

其余 56 条均验证通过。详细报告见 `artifacts/bib_audit_report.md`。

---
