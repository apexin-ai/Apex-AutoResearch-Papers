# ops rrf 15b instruct

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rrf-15b-instruct_20260516T185730_result.json`
- **Structured JSON:** [`befeb4e7a5d74187f8df.json`](../../sessions/be/befeb4e7a5d74187f8df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出文件：

| 文件 | 路径 | 行数 |
|------|------|------|
| exposure_aggregated.json | `/root/autodl-tmp/exp002/signals/rrf/exposure_aggregated.json` | 16,540 |
| exposure_scores.json | `/root/autodl-tmp/exp002/signals/rrf/exposure_scores.json` | 509,676 |

注意：脚本实际以 `--signal-root` 模式处理了所有模型目录（不仅限于 1.5B-Instruct），因为 `--generate-exposure` 会扫描整个 signals root 生成聚合分数。`exposure_aggregated.json` 包含 3 个 benchmark（mmlu/gsm8k/arc_challenge）× 所有 respondent 的聚合 RRF 输出。

---
