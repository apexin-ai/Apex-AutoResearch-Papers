# research data pipeline audit 069

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_data-pipeline-audit-069_20260519T131154_result.json`
- **Structured JSON:** [`e0e5f488f5c4df710bfe.json`](../../sessions/e0/e0e5f488f5c4df710bfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：数据通道 VALID，无需重跑。**

核心机制：`logiqa_200.json` 每条数据已自带 `"dataset": "logiqa"` 字段，`load_all_problems()` 中的 `setdefault("dataset", "strategyqa")` 不会覆盖已存在的 key。主循环根据 `dataset == "logiqa"` 分支正确设置了 `generator.domain = "multichoice"` + `extractor.domain = "logic"`，与专用的 `run_logiqa.py` 行为一致。prompt 模板（多选题格式）、答案抽取（A/B/C/D）、答案比对（`is_equiv` 字符串匹配）均无问题。

报告已保存至 `artifacts/exp069_data_pipeline_audit.md`。

---
