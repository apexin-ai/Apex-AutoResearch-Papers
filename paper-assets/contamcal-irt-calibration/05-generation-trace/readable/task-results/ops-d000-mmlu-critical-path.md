# ops d000 mmlu critical path

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d000-mmlu-critical-path_20260516T204631_result.json`
- **Structured JSON:** [`9d341ddaefefebdeea82.json`](../../sessions/9d/9d341ddaefefebdeea82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

1. **merged 文件**：`/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42/signals_merged_mmlu.json` 存在，98,295 行
2. **RRF 成功**：exit code 0，输出到 `/root/autodl-tmp/exp002/signals/rrf/`
   - `exposure_scores.json` — 15.2 MB（per-respondent 详细分数）
   - `exposure_aggregated.json` — 408 KB, 16,540 行（3 benchmarks 聚合分数）
   - 覆盖模型：Llama-3.2-3B d000/s42, Qwen2.5-3B 多个 dosage×seed 组合（d000/d005/d025/d100, s42/s123, alpha32）
3. **注意**：输出文件名是 `exposure_scores.json` 和 `exposure_aggregated.json`（非用户预期的 `exposure_scores_v2.json`），因为脚本 `--output-dir` 参数控制目录而非文件名

---
