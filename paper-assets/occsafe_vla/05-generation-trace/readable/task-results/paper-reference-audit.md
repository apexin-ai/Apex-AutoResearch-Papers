# paper reference audit

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reference-audit_20260526T194657_result.json`
- **Structured JSON:** [`09e8c5d5543e1e41ef44.json`](../../sessions/09/09e8c5d5543e1e41ef44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。

**46 条引用全部验证为真实论文，无幻觉引用。** 修正了 12 处问题：

- 1 处作者名错误（`chen2026gstvla`: "Md Sarowar Morshed" → "Md Selim Sarowar"）
- 10 处作者名不完整（缺少 given name，已补全）
- 1 处发表场所不准确（`li2017adabn`: ICLR 主会 → ICLR Workshop）

无缺失引用、无孤立条目、无重复条目。2 处 bib key 命名不一致（`wu2025spatialvla` 和 `chen2026gstvla`）未修改以避免破坏 tex 引用。

报告已写入 `artifacts/reference_audit_report.md`。

---
