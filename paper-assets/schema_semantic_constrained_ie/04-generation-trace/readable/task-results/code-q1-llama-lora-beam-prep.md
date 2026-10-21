# code q1 llama lora beam prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_q1_llama_lora_beam_prep_20260518T133005_result.json`
- **Structured JSON:** [`da0d49a909e0d5542de0.json`](../../sessions/da/da0d49a909e0d5542de0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Q1 实验准备汇报

### Checkpoint
**就绪。** westd-21461 上 `/root/autodl-tmp/checkpoints/llama_lora_scierc_merged/` 已有完整 checkpoint（16GB，4 个 safetensors 分片 + tokenizer），与 westd-16980 一致。

### Beam search
**支持。** 原任务命令中的 `--beam_size 4` 不存在，正确参数是：
- `--decoding_strategy beam --num_beams 4`
- 实现了专用的 `BeamAwareTypeConstraintProcessor`（per-beam 重放语义约束）和 `BeamSearchGrammarProcessor`

### 数据
- SciERC test: `data/processed_data/test.json`，**100 docs**（非 551）
- Ontology: `ontology_constraints.json`（项目根目录）

### GPU
2x NVIDIA RTX PRO 6000 Blackwell（98GB），**完全空闲**（0 MiB used）。

### Dry-run
2 docs 成功，输出格式正确，每 sample 约 1.7-5.3s。

### 修正后的启动命令

```bash
cd /root/schema_semantic_constrained_ie && /root/miniconda3/bin/python3.12 run_constrained_extraction.py \
  --mode full_s1 \
  --dataset scierc \
  --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged \
  --data_path data/processed_data/test.json \
  --constraints_path ontology_constraints.json \
  --decoding_strategy beam \
  --num_beams 4 \
  --output_path /root/autodl-tmp/schema_outputs/q1_llama_lora_scierc_beam4.jsonl \
  --max_new_tokens 4096 \
  --skip_on_error
```

预估 100 docs × ~3.5s/doc ≈ 6 分钟完成。可以启动。

---
