# code phase3 data prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase3_data_prep_20260513T235409_result.json`
- **Structured JSON:** [`2bd2d9ec68090182b4ce.json`](../../sessions/2b/2bd2d9ec68090182b4ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**任务已完成，数据已是最新状态。** 总结：

`prepare_sft_data.py` 已于 May 14 07:16 运行过，生成了包含全部 3 个 benchmark 的 dosage 文件。

### 数据完整性确认

| 文件 | 行数 | 构成 |
|------|------|------|
| `sft_dosage_000.jsonl` | 50,000 | 纯 SlimOrca base（未修改） |
| `sft_dosage_005.jsonl` | 50,826 | 50,000 base + 826 contam (5%) |
| `sft_dosage_025.jsonl` | 54,133 | 50,000 base + 4,133 contam (25%) |
| `sft_dosage_050.jsonl` | 58,266 | 50,000 base + 8,266 contam (50%) |
| `sft_dosage_100.jsonl` | 66,533 | 50,000 base + 16,533 contam (100%) |

### Benchmark 覆盖

- arc_challenge: 1,172 items
- gsm8k: 1,319 items  
- mmlu: 14,042 items
- **contam total: 16,533** = 1,172 + 1,319 + 14,042 ✓

### d100_05B 训练状态

`Qwen2.5-0.5B_d100_s42` checkpoint 目录存在但为空（`lora_adapter/` 无内容），训练尚未开始。数据在训练启动前已更新为完整版本，不存在使用旧数据的问题。

---
