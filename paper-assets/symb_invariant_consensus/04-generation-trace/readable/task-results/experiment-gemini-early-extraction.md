# experiment gemini early extraction

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_gemini-early-extraction_20260521T193216_result.json`
- **Structured JSON:** [`bc207f1bf4cbbd06b37c.json`](../../sessions/bc/bc207f1bf4cbbd06b37c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

| 项目 | 状态 |
|------|------|
| **数据同步** | ✓ 通过 HF Hub 中转 95 题 (westd-25068 → westd-16639)，已转为 intermediates 格式 |
| **Extraction 脚本** | `scripts/cross_model_extract.py` (复用已有 pipeline) |
| **PID** | 480272 (westd-16639) |
| **初始进度** | 4/95 完成，**4/4 全部正确** |
| **增量模式** | ✓ `--resume`，checkpoint 在 output JSON，Gemini SC 后续完成新题后补充 intermediates 即可重跑 |

初始 constraint 统计：
- folio_0: 106→63 unique, Unknown ✓
- folio_1: 120→95 unique, True ✓
- folio_10: 79→30 unique, False ✓
- folio_11: 69→42 unique, Unknown ✓

ETA ~35 min (剩余 91 题，~24s/题)。输出路径：`results/exp_d135_frontier_scb/google_gemini-2.5-pro/cross_model/cross_model_mistral.json`

---
