# research auroc calculation

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_auroc-calculation_20260525T045219_result.json`
- **Structured JSON:** [`297c492e9a9117c7a839.json`](../../sessions/29/297c492e9a9117c7a839.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

| Model | Direction | AUROC | Balanced Acc |
|---|---|---|---|
| Llama-3.1-8B | EN→EN | 0.9808±0.0012 | 92.7%±0.1% |
| Gemma-2-9B | EN→EN | 0.9313±0.0065 | 88.1%±1.3% |
| Gemma-2-9B | ZH→ZH | 0.8997±0.0084 | 85.7%±0.6% |
| Gemma-2-9B | EN→ZH | 0.8522±0.0155 | 75.1%±1.2% |
| Gemma-2-9B | ZH→EN | 0.9213±0.0134 | 77.8%±3.5% |
| Qwen3-8B | EN→EN | 0.7705±0.0210 | 71.4%±1.9% |

**关键发现：**
- AUROC 普遍高于 balanced accuracy（因为 AUROC 利用了连续概率值，不受阈值选择影响）
- Gemma ZH→EN 的 AUROC (0.9213) 远高于其 balanced accuracy (77.8%)，说明 probe 的排序能力很强，但阈值不理想
- Llama31 和 Qwen3 只有 EN activations（无 `zh_activations.pt`），所以只能计算 EN→EN

脚本保存在服务器 `src/compute_auroc.py`，结果在 `results/auroc_all_models.json`，本地副本在 `artifacts/auroc_all_models.json`。

---
