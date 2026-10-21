# code q1 llama lora beam launch

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_q1_llama_lora_beam_launch_20260518T133727_result.json`
- **Structured JSON:** [`cb32807664d21793df1d.json`](../../sessions/cb/cb32807664d21793df1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型加载成功，已开始推理。实验配置确认：

- **exp_id**: `q1_llama_lora_scierc_beam4`
- **服务器**: westd-21461, cuda:0
- **模型**: Llama-3.1-8B-Instruct LoRA merged
- **模式**: full_s1 (grammar + semantic constraints)
- **解码**: beam search, num_beams=4
- **数据**: SciERC test.json, 551 samples
- **输出**: `/root/autodl-tmp/schema_outputs/q1_llama_lora_scierc_beam4.jsonl`
- **状态**: RUNNING, 模型已加载并开始生成

Cron 会自动监控进度。首次提交缺少 `--data_path` 和 `--constraints_path` 导致报错，已修复重新提交。

---
