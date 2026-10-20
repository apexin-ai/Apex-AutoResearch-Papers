# research bib full audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bib-full-audit_20260515T183544_result.json`
- **Structured JSON:** [`9fda7a6dc04c62499274.json`](../../sessions/9f/9fda7a6dc04c62499274.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量审计完成。

## 汇总

| 指标 | 数值 |
|------|------|
| 总条目 | 48 |
| 已审计 | 48 (100%) |
| 发现错误 | **3** |
| 已修正 | **3** |
| 元数据补充 | 5 条 |

### 修正的 3 个错误

1. **`curse_of_recursion`** — 作者顺序错误：Gal 应为末位作者，非第4位。已按 Nature 原文修正为 `Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal`
2. **`reliable_detection`** — 标题不完整：TMLR 正式版标题为 `"...Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks"`，已补全
3. **`model_collapse_avoidable`** — 还标注为 arXiv preprint，实际已在 ICML 2024 发表。已改为 `@inproceedings`

### 先前标记条目确认

- `wu_survey_2025` ✅ 当前6位作者正确（之前虚构的已修复）
- `munir_looking_glass` ✅ 当前5位作者正确（之前错误的已修复）
- `diveye` ✅ 年份 2026 正确（TMLR '26）
- `strong_model_collapse` ✅ 年份 2025 正确（ICLR 2025 Spotlight）
- `aaronson_watermark` ✅ URL 正确

审计报告已写入 `artifacts/bib_audit_report.md`。

---
