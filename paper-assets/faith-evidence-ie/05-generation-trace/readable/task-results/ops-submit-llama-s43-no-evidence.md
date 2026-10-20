# ops submit llama s43 no evidence

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_llama_s43_no_evidence_20260520T021036_result.json`
- **Structured JSON:** [`b11d3316a612b756ca31.json`](../../sessions/b1/b11d3316a612b756ca31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交并启动成功。

**提交结果：**
- **exp_id**: `eval_llama_rsft_s43_no_evidence`
- **PID**: 745299
- **GPU**: cuda:1（显存空闲，0 MiB）
- **日志**: `/tmp/eval_llama_rsft_s43_no_evidence.log`
- **关键参数**: `--no_evidence`（C005）、`CUDA_VISIBLE_DEVICES=1`（C002）
- **命令**: `CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s43 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/eval_llama_rsft_s43_no_evidence`

模型正在加载 checkpoint shards，进程运行正常。

---
