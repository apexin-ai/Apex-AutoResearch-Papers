# code 14b rsft withevi 2048 launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_14b-rsft-withevi-2048-launch_20260521T024530_result.json`
- **Structured JSON:** [`96d124322660e0dfed60.json`](../../sessions/96/96d124322660e0dfed60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动，推理进行中。

| 项目 | 值 |
|------|-----|
| **exp_id** | plan017_14b_rsft_eval_2048 |
| **PID** | 70388 |
| **GPU** | cuda:1, 32.5GB / 97.9GB |
| **进度** | 5/985 docs, ~13.6s/it |
| **预计耗时** | ~3.7h |
| **日志** | `/root/logs/plan017_14b_rsft_eval_2048.log` |
| **输出** | `/root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048/` |

**命令**:
```
CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference \
  --model_path /root/autodl-tmp/rsft_output_14b \
  --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B \
  --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 \
  --data_path /root/autodl-tmp/data/docred \
  --split dev \
  --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval_2048 \
  --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42
```

---
