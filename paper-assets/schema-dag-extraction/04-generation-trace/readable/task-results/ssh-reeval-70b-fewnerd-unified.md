# ssh reeval 70b fewnerd unified

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_reeval_70b_fewnerd_unified_20260517T132526_result.json`
- **Structured JSON:** [`c92c153a5603c15bc2cb.json`](../../sessions/c9/c92c153a5603c15bc2cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。以下是统一协议后的结果：

## LLaMA 70B d051 重新评估结果（text_match protocol）

| Count | 70B Recall | Qwen3 Recall | Delta | 70B Precision | Qwen3 Precision |
|-------|-----------|-------------|-------|--------------|----------------|
| count_2 | **0.323** | 0.515 | -19pp | 0.446 | 0.320 |
| count_6 | **0.300** | 0.399 | -10pp | 0.323 | 0.248 |
| count_12 | **0.278** | 0.318 | -4pp | 0.311 | 0.269 |
| count_22 | **0.252** | 0.279 | -3pp | 0.376 | 0.365 |
| count_44 | **0.297** | 0.309 | -1pp | 0.468 | 0.504 |
| count_66 | **0.273** | 0.407 | -13pp | 0.609 | 0.633 |

## 关键发现

1. **旧值完全失效**：70B count_2 从 0.962 降至 0.323（-64pp），证实旧评估协议严重失真
2. **70B recall 在所有 count level 都低于 Qwen3**，差距 1-19pp
3. **70B 更保守**：pred/gold ratio 0.45-0.93 vs Qwen3 在低 count 大量过度预测（count_2 ratio 3.11）。70B 高 precision / 低 recall，Qwen3 反之
4. **中间段（count_12-44）两模型接近**，差距仅 1-4pp
5. **count_66 差距大**（13pp）：Qwen3 在全类型场景下 recall 反弹至 0.407，70B 仍停留在 0.273

结果已保存至 westd: `/root/schema-dag-extraction/artifacts/d051_llama-3.1-70b-fp8_fewnerd_n25_s42/summary_unified_protocol.json`

---
