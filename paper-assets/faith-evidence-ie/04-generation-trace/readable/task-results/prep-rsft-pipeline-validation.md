# prep rsft pipeline validation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_rsft_pipeline_validation_20260515T040419_result.json`
- **Structured JSON:** [`ed7ffae9deb2b3dbf657.json`](../../sessions/ed/ed7ffae9deb2b3dbf657.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

预验证完成。产出已写入 `artifacts/rsft_pipeline_commands.md`。

核心结论：
- 4 个脚本全部就位（在 `freige/training/` 和 `freige/eval/` 下，不在 `freige/freige/`）
- 输入输出格式全链路对齐，无需格式转换
- `rsft_score_filter` 内置 shard 合并，可跳过 merge_shards 直接喂 `--input_dir`
- NLI 模型、SFT adapter、base model、DocRED 数据均已就位
- rsft_trainer 默认 lora_rank=64, lora_alpha=128, bf16=True, quantize=False，满足硬约束
- inference.py 的 quantize 默认 True，**必须传 `--no-quantize`**
- shard_3 行数偏少（4,104 vs ~4,700），执行前需确认 generation 已全部结束

---
