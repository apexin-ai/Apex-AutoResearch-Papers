# infra exp001 llama status check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp001_llama_status_check_20260521T005910_result.json`
- **Structured JSON:** [`67f3aa7285570464cae0.json`](../../sessions/67/67f3aa7285570464cae0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### exp001_llama: **运行中** — 208,200 / 259,200 records (80.3%), accuracy ≈ 0.695

| Shard | Records | 进度 | Correct | Accuracy |
|-------|---------|------|---------|----------|
| shard_0 | 51,800 / 64,800 | 79.9% | 35,957 | 0.6942 |
| shard_1 | 51,600 / 64,800 | 79.6% | 35,765 | 0.6932 |
| shard_2 | 51,200 / 64,800 | 79.0% | 35,624 | 0.6958 |
| shard_3 | 53,600 / 64,800 | 82.7% | 37,303 | 0.6961 |
| **总计** | **208,200 / 259,200** | **80.3%** | **144,649** | **0.6949** |

- GPU 0-3 全部满载 (83-100% utilization, ~90GB VRAM each)
- 文件总大小: 199M
- 字段完整性 OK: condition_id, item_id, subject, model, precision, temperature, top_p, prompt_template, seed, ordering, generated_text, predicted_answer, gold_answer, correct, latency_ms, answer_logprob, top_logprobs

### Qwen3-8B download: **运行中** — 7.3GB + 553MB downloading

- 已完成: 2/5 safetensors (model-00003, model-00004) + config/tokenizer
- 下载中: 3 个 .incomplete 文件 (553MB in cache)
- 预计完整大小约 16GB，当前约 50% 完成

---
