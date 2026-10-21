# experiment exp llama70b ner bcs null

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_exp_llama70b_ner_bcs_null_20260521T171749_result.json`
- **Structured JSON:** [`fef4e654c1a7235d11f8.json`](../../sessions/fe/fef4e654c1a7235d11f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。总结：

**LLaMA-70B NER BCS-null 分析结果**

复用了已有的 `d051_llama-3.1-70b-fp8_fewnerd_n25_s42` 数据（25 random batches × 1000 test instances，count_6 和 count_12），计算了 per-batch text-match F1 与 BCS 的相关性。

| 模型 | count_6 r (p) | count_12 r (p) | Pooled r (p) |
|------|--------------|----------------|-------------|
| Qwen3-32B | — | — | 0.004 (0.94) |
| LLaMA-8B | — | — | -0.12 (0.29) |
| **LLaMA-70B** | **-0.06 (0.76)** | **-0.42 (0.034)** | **-0.13 (0.36)** |

- **count_6**: 清楚的 null (r=-0.06, p=0.76)
- **count_12**: 边界显著负相关 (r=-0.42, p=0.034)，但 Bonferroni 校正后 p=0.069，不显著
- **Pooled**: 非显著 (r=-0.13, p=0.36)，与前两个模型一致

**结论**: BCS null 在 pooled level 上跨三个模型得到支持。count_12 的边界负相关值得后续关注，但不影响主结论。

结果保存在 `cqa1-38874:/root/schema-dag-extraction/artifacts/exp_llama70b_ner_bcs_null/bcs_null_analysis.json`，包含全部 50 个 batch 的 (BCS, F1, recall) 数据。

---
