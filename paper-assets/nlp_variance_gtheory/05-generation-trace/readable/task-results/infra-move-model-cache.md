# infra move model cache

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_move_model_cache_20260520T195623_result.json`
- **Structured JSON:** [`e6cda8fa11a9bcd2bed9.json`](../../sessions/e6/e6cda8fa11a9bcd2bed9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

迁移完成。

- **根分区**: 91% → **41%** (18G free，释放了 15G)
- **数据盘**: 10% (318G free)
- Symlink: `/root/nlp_variance_gtheory/models/.hf_cache` → `/root/autodl-tmp/.hf_cache`

数据盘已有的 `LLM-Research/Meta-Llama-3___1-8B-Instruct` 和 `models--meta-llama--Llama-3.1-8B-Instruct` 两份模型均保留，项目代码通过 symlink 透明访问。

---
