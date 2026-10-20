# code wikievents llama unconstrained full

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_llama_unconstrained_full_20260517T174529_result.json`
- **Structured JSON:** [`3f4285591a5f55ec864b.json`](../../sessions/3f/3f4285591a5f55ec864b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行确认完毕。

**状态总结：**

1. **tmux session `llama_wikievents_full` 正常运行**
   - GPU 0 (16610 MiB)，Llama-3.1-8B-Instruct
   - 已完成 8/246 docs，进度正常

2. **命令**：
   ```
   CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py \
     --dataset wikievents --mode unconstrained \
     --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct \
     --data_path data/wikievents/all.jsonl \
     --output_path outputs/wikievents_llama_unconstrained_full.jsonl \
     --max_new_tokens 4096
   ```

3. **预估完成时间**：基于 pilot run 平均 ~17s/doc（短文档 4-10s，长文档 40-50s），246 docs 预计 **1-1.5 小时**，约在 UTC 03:00-03:30 完成。

4. **输出文件**：`outputs/wikievents_llama_unconstrained_full.jsonl`

---
