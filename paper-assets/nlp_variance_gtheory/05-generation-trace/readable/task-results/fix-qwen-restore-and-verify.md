# fix qwen restore and verify

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_qwen_restore_and_verify_20260521T072039_result.json`
- **Structured JSON:** [`e68d36420a8b089e2608.json`](../../sessions/e6/e68d36420a8b089e2608.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

1. **补跑进程**：无运行中的补跑进程，无需 kill
2. **每个 shard 行数**：均为 64,800
3. **总计**：259,200 ✓
4. **统计**：
   - **精度分布**：bfloat16=100,200 / float16=79,600 / float32=79,400
   - **温度分布**：0.0=87,000 / 0.3=84,800 / 0.7=87,400
   - **Accuracy**：0.0000（`binary_correct` 字段全为 0，可能该字段名或计算逻辑不同）
   - **Unique conditions**：1,227（少于预期的 1,296，差 69 个——shard_3 中部分 condition 有 400 条重复记录，说明 `_merged_with_dup` 文件确实含重复）

注意点：accuracy 为 0 异常，建议检查正确性字段的实际 key 名。条件数 1,227 < 1,296 也值得确认是否符合预期。

---
