# code mistral constrained v2 launch

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral_constrained_v2_launch_20260517T213706_result.json`
- **Structured JSON:** [`906aab7b7b3cef59f265.json`](../../sessions/90/906aab7b7b3cef59f265.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程都在正常运行。

## 启动结果

- **type_mask_processor.py**: 812 行 (验证通过)
- **--skip_on_error**: 新增（argparse + 主循环 try/except）
- **tmux session**: `mistral_constrained_v2`
- **GPU**: cuda:0
- **PID**: 40830
- **完整命令行**: `cd /root/schema_semantic_constrained_ie && HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python run_constrained_extraction.py --mode full_s1 --dataset wikievents --model_path /root/autodl-tmp/.ms_cache/mistralai/Mistral-7B-Instruct-v0___3/ --constraints_path data/wikievents/ontology_constraints_wikievents.json --data_path data/wikievents/all.jsonl --output_path outputs/ee_mistral_wikievents_constrained_v2_full.jsonl --skip_on_error --resume 2>&1 | tee logs/mistral_constrained_v2_full.log`
- **初始进度**: 3/246（约2分钟内）
- **nvidia-smi 确认**: cuda:0 显存占用 15293 MiB，GPU-Util 81%
- **cuda:1 未受影响**: yes（PID 37038 仍在运行，96/246 已处理，16665 MiB 显存，GPU-Util 84%）

---
