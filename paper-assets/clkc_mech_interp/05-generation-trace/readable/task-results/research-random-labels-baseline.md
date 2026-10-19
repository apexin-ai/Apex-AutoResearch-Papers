# research random labels baseline

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_random-labels-baseline_20260525T045235_result.json`
- **Structured JSON:** [`0c0ee48183e00fcb9f10.json`](../../sessions/0c/0c0ee48183e00fcb9f10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

```
Model           | Real BA | Permuted BA (mean±std) | Selectivity
----------------------------------------------------------------
Llama-3.1-8B    |  90.0%  | 51.0% ± 3.0%          | 38.9 pp
Gemma-2-9B-IT   |  88.9%  | 49.2% ± 2.7%          | 39.6 pp
Qwen3-8B        |  71.0%  | 49.7% ± 1.8%          | 21.3 pp
```

所有模型的 permuted labels probe 都在 ~50% chance level 附近，说明 probe 学到的是真实的 conflict/non-conflict 表征差异，不是 activations 中的 trivial 统计特征。

结果已保存到 `results/random_labels_selectivity.json`，脚本在 `src/random_labels_control.py`。

---
