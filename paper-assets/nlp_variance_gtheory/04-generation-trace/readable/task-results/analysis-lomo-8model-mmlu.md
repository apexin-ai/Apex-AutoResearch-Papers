# analysis lomo 8model mmlu

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lomo_8model_mmlu_20260522T012249_result.json`
- **Structured JSON:** [`ea092d13ccd347d4ddae.json`](../../sessions/ea/ea092d13ccd347d4ddae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `results/exp004_8model_analysis/lomo_8model_mmlu.json`。

| Dropped Model | item_id% | model×item% | G_item | N |
|---|---|---|---|---|
| DeepSeek-7B | 39.14% | 29.59% | 0.8888 | 403,200 |
| Gemma-2-9B | 37.29% | 29.73% | 0.8830 | 403,200 |
| InternLM2.5-7B | 36.62% | 30.35% | 0.8769 | 403,200 |
| Llama-3.1-8B | 36.37% | 31.36% | 0.8773 | 403,200 |
| Mistral-7B-v0.3 | 37.05% | 30.30% | 0.8822 | 403,200 |
| OLMo-2-7B | 36.98% | 29.85% | 0.8817 | 403,200 |
| Qwen3-8B | 38.23% | 28.78% | 0.8877 | 403,200 |
| Yi-1.5-9B | 40.94% | 31.74% | 0.8876 | 403,200 |

**Full 8-model**: item_id=37.88%, G_item=0.8962

**LOMO range**: G_item [0.8769, 0.8888], item_id% [36.37%, 40.94%]

G_item 在所有 7-model subsets 中稳定在 0.877–0.889，与 8-model baseline (0.896) 相差不大。Dropping InternLM2.5 或 Llama 导致最低 G_item；dropping DeepSeek 导致最高。结论对 model composition 不敏感。

---
