# code references merge

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_references-merge_20260521T065224_result.json`
- **Structured JSON:** [`a078e6a27223a52adce3.json`](../../sessions/a0/a078e6a27223a52adce3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`paper/references.bib` 已合并，共 58 条条目。

**变更摘要：**

| 操作 | 数量 |
|------|------|
| 保留 paper 原有条目 | 37 |
| 从 artifacts 合并（去重后） | 18 |
| 新增 HT 统计量相关 | 3 |
| 删除 UNVERIFIED | 1（未进入 paper） |

**新增的 3 条 Reviewer 要求引用：**
- `harnisch1983` — Harnisch (1983), *J. Educational Measurement* 20(2), 191–206
- `tatsuoka1982` — Tatsuoka & Tatsuoka (1982), *J. Educational Statistics* 7(3), 215–231 (aberrant response detection)
- `tatsuoka1984` — Tatsuoka (1984), *Psychometrika* 49(1), 95–110 (caution indices, DOI verified)

**确认：**
- `wang2025fragility`（MIA fails after RL）已在 paper bib 中
- `polo2024tinybenchmarks`（tinyBenchmarks/PSN-IRT）已在 paper bib 中
- `zhuang2023`（adaptive testing for LLMs）从 artifacts 补入

---
