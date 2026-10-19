# paper reference audit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reference_audit_20260524T211234_result.json`
- **Structured JSON:** [`34fd3718fb43a79d76b5.json`](../../sessions/34/34fd3718fb43a79d76b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成。以下是审计结果摘要：

---

**CRITICAL（必须修复）：**
- **21 个 cite key 无对应 bib 条目**，编译会报 `undefined citation`。其中 `placeholder_goodhart_rl` 和 `placeholder_metric_reliability` 是占位符，需替换或移除。其余 19 个（如 `3dcavla2025`, `augvla3d2026`, `spatialvla2025` 等）主要出现在 related_work 章节。
- **2 个作者姓名错误**：`yang2025cape` 的第一作者应为 "Rui Heng Yang" 而非 "Xinyu"；`spalter2024ikinqp` 应为 "Ariana Spalter" 而非 "Ariel"。

**WARNING（应该修复）：**
- `zhi2021diffco`：IEEE TRO 正式发表于 2022 年，缺 volume/pages 字段
- `brohan2023rt2`：已发表于 CoRL 2023，建议更新为 @inproceedings
- 5 个条目作者列表仅 1 人 + "and others"，建议至少补全前 3 位

**INFO：**
- 无 fake citation，18 个现有条目全部验证为真实论文
- 无孤立 bib 条目
- `related_work_v2.tex` 中有 2 处 `%[CITE-CHECK]` 标记待清理

报告位于 `artifacts/reference_audit_report.md`。

---
