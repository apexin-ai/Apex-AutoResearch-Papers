# ssh fix exp3 eval metric

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_exp3_eval_metric_20260517T125735_result.json`
- **Structured JSON:** [`6b23410eeb804e9251d3.json`](../../sessions/6b/6b23410eeb804e9251d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

## LLaMA 70B Few-NERD: text-only vs type+text recall

| count_key | text-only (旧) | type+text (修正) | delta |
|-----------|---------------|-----------------|-------|
| count_2   | 0.9623 | 0.9618 | -0.0004 |
| count_6   | 0.9024 | 0.9003 | -0.0022 |
| count_12  | 0.8293 | 0.8218 | -0.0075 |
| count_22  | 0.6840 | 0.6663 | -0.0176 |
| count_44  | 0.5309 | 0.4803 | -0.0506 |
| count_66  | 0.4072 | 0.3388 | -0.0684 |

## 关键结论

1. **Bug 影响随 count 增大而加剧**：count_2 仅差 0.04pp，count_66 差 6.84pp。type 越多，错误类型匹配的概率越高，符合预期。

2. **Qwen3 无需重新评估**：Qwen3 的评估走 `src/evaluate.py` 的 `_text_match` 函数，该函数第一行就检查 `pred.get("type") != gold["type"]`，已经是 type+text 匹配。

3. **count_66 的 type+text recall = 0.3388**，非零且合理。

4. **Sanity check 通过**：所有 count level 的 type+text recall <= text-only recall。

5. 修正后的 summary 已保存至 `/root/schema-dag-extraction/artifacts/d051_llama-3.1-70b-fp8_fewnerd_n25_s42/summary_type_text.json`。

---
