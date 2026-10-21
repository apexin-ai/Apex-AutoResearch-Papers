# ops verify dosage data files

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-dosage-data-files_20260518T133303_result.json`
- **Structured JSON:** [`761f4b659f4ada61a45a.json`](../../sessions/76/761f4b659f4ada61a45a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个文件全部存在，d050 已就位。

| 文件 | Dosage | 大小 | 行数 |
|------|--------|------|------|
| `sft_dosage_000.jsonl` | 0% | 89M | 50,000 |
| `sft_dosage_005.jsonl` | 5% | 89M | 50,826 |
| `sft_dosage_025.jsonl` | 25% | 91M | 54,133 |
| `sft_dosage_050.jsonl` | 50% | 93M | 58,266 |
| `sft_dosage_100.jsonl` | 100% | 97M | 66,533 |

数据合理：baseline d000 = 50,000 行，随 dosage 增加行数和文件大小单调递增（污染样本追加到基础数据上）。d050 行数 58,266 落在 d025 (54,133) 和 d100 (66,533) 之间，符合预期。

---
