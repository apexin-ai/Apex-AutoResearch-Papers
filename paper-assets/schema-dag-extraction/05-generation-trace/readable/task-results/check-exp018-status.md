# check exp018 status

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp018_status_20260516T073310_result.json`
- **Structured JSON:** [`c7d5e3f2a533357a1e25.json`](../../sessions/c7/c7d5e3f2a533357a1e25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-018 已完成

重启后跳过了 vLLM extract 阶段（数据已在首次运行中提取完毕），直接汇总结果并正常退出。

### 最终结果

| 条件 | Accuracy | Macro-F1 | BCS |
|------|----------|----------|-----|
| **confusability_aware** | **0.8021** | 0.8021 | 0.5524 |
| random_batch (15 seeds) | 0.7877 ± 0.0178 | 0.7877 ± 0.0178 | 0.5585 |
| single_pass | 0.5042 | 0.5042 | 0.5572 |

- Confusability-aware (0.8021) > random batch 95% CI 上界 (0.7967)，**提升显著**
- Per-type：51 types improved, 28 degraded, mean Δ=+0.0144
- 结果已保存至 `/root/schema-dag-extraction/artifacts/exp_confusability_batch_composition/results.json`

---
