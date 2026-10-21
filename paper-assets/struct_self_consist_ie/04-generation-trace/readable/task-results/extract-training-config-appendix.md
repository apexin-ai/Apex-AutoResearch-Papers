# extract training config appendix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_extract_training_config_appendix_20260515T071343_result.json`
- **Structured JSON:** [`65809b4a1cdccef6058f.json`](../../sessions/65/65809b4a1cdccef6058f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入并注册。

**文件**: `artifacts/training_config_appendix.md`

**内容摘要**:

| 项目 | 内容 |
|------|------|
| 超参数表 | Qwen3-8B 和 LLaMA-3.1-8B 完全对齐：LoRA r=32, α=64, all modules, lr=2e-4, cosine, warmup 0.1, eff. batch=16, 5 epochs, cutoff 2048, bf16 |
| 数据集变体 | CoNLL-2003/WNUT-17 额外开启 load_best_model_at_end, eval 间隔 200 steps |
| SciERC 数据量 | train 1861 / dev 275 / test 551 |
| Prompt template | 完整示例（含 entity types + relation types schema hint） |
| Schema constraint | vLLM + XGrammar JSON constrained decoding，完整 UIE JSON Schema 已列出 |

---
