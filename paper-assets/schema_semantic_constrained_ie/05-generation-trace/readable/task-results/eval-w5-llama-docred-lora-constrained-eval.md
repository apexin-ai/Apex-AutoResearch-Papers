# eval w5 llama docred lora constrained eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_w5_llama_docred_lora_constrained_eval_20260516T002156_result.json`
- **Structured JSON:** [`93b2236068e99c2b44cf.json`](../../sessions/93/93b2236068e99c2b44cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验已在运行中，无需重新提交。**

状态：
- **exp_id**: `w5_llama_docred_lora_constrained_eval`
- **状态**: RUNNING（PID 316883 存活）
- **提交时间**: 2026-05-16T00:22
- **进度**: 4/998 samples（输出文件最后更新 May 16 08:23，215KB）
- **GPU**: cuda:0, 32GB/97GB 占用, 94% 利用率
- **命令**: `python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_llama_docred_lora_constrained_eval.jsonl --batch_size 1 --max_new_tokens 4096`

注意：进度较慢（~8h 处理 4 个文档），DocRED full_s1 的双层约束解码在长文档上开销较大。按当前速率估计总耗时约 2000h，可能需要排查是否有性能瓶颈。

---
