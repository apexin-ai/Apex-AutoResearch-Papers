# data folio and sc baseline

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_folio_and_sc_baseline_20260514T070419_result.json`
- **Structured JSON:** [`802869e40d20fbb5af09.json`](../../sessions/80/802869e40d20fbb5af09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

**FOLIO 数据集**
- 来源：GitHub `Yale-LILY/FOLIO`，保存至 `/root/autodl-tmp/data/folio/`
- 格式：jsonl，每条含 `premises`(list), `premises-FOL`, `conclusion`, `conclusion-FOL`, `label`
- **Train**: 1004 样本 — True: 388, False: 286, Unknown: 330
- **Validation**: 204 样本 — True: 72, False: 63, Uncertain: 69
- 注意：train 用 "Unknown"，validation 用 "Uncertain"，后续加载时需统一标签映射

**SC Baseline 代码**
- 服务器：`/root/svs_pipeline/svs_pipeline/evaluation/sc_baseline.py` ✓
- 本地：`artifacts/svs_pipeline/evaluation/sc_baseline.py` ✓
- `evaluation/__init__.py` 已更新，导出 `sc_majority_vote` 和 `evaluate_sc_baseline`
- 验证通过：`from svs_pipeline.evaluation.sc_baseline import sc_majority_vote, evaluate_sc_baseline` → OK

---
