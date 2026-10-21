# code regenerate dosage data

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_regenerate-dosage-data_20260513T235208_result.json`
- **Structured JSON:** [`cf6a0ede978392752800.json`](../../sessions/cf/cf6a0ede978392752800.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**任务已完成——文件已经是最新的。**

`prepare_sft_data.py` 已在 May 14 07:16 重新运行过，生成了包含 MMLU+ARC+GSM8K 的完整 dosage 文件。

### 验证报告

| 文件 | 行数 | 构成 |
|------|------|------|
| sft_dosage_000.jsonl | 50,000 | 纯 SlimOrca |
| sft_dosage_005.jsonl | 50,826 | 50000 + 826 contam (5%) |
| sft_dosage_025.jsonl | 54,133 | 50000 + 4133 contam (25%) |
| sft_dosage_050.jsonl | 58,266 | 50000 + 8266 contam (50%) |
| sft_dosage_100.jsonl | 66,533 | 50000 + 16533 contam (100%) |

Benchmark 分布（总 contam pool）：
- MMLU: 14,042 条
- GSM8K: 1,319 条
- ARC Challenge: 1,172 条

contamination_labels 文件也已为三个 benchmark 的四个 dosage 生成完毕（共 12 个 label JSON）。无需再次运行。

---
