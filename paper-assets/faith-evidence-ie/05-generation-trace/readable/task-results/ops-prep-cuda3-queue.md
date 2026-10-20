# ops prep cuda3 queue

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep-cuda3-queue_20260515T230659_result.json`
- **Structured JSON:** [`d2176d497bf50e526fc2.json`](../../sessions/d2/d2176d497bf50e526fc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All info gathered. Here's the summary:

## Checkpoint 路径确认

| 模型 | 路径 | 最终 checkpoint |
|------|------|----------------|
| rsft_output_s44 (CED RSFT s44) | `/root/autodl-tmp/rsft_output_s44` | checkpoint-510 (root 有 adapter files) |
| rsft_output_flat_nli_s44 | `/root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507` | checkpoint-507 (root 无 adapter，需用 checkpoint 路径) |
| rsft_output_flat_nli_s45 | `/root/autodl-tmp/rsft_output_flat_nli_s45` | checkpoint-507 (root 有 adapter files) |

## 建议 eval 命令

**1) CED RSFT s44**
```bash
cd /root/autodl-tmp && python -m freige.eval.inference \
    --model_path /root/autodl-tmp/rsft_output_s44 \
    --sft_adapter /root/autodl-tmp/sft_output \
    --base_model /root/autodl-tmp/models/Qwen3-4B \
    --data_path /root/autodl-tmp/data/docred \
    --split dev \
    --batch_size 16 \
    --max_new_tokens 1024 \
    --seed 42 \
    --output_dir /root/autodl-tmp/eval_results/mvp2_rsft_s44 \
    --no-quantize
```

**2) Flat-NLI RSFT s44**
```bash
cd /root/autodl-tmp && python -m freige.eval.inference \
    --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 \
    --sft_adapter /root/autodl-tmp/sft_output \
    --base_model /root/autodl-tmp/models/Qwen3-4B \
    --data_path /root/autodl-tmp/data/docred \
    --split dev \
    --batch_size 16 \
    --max_new_tokens 1024 \
    --seed 42 \
    --output_dir /root/autodl-tmp/eval_results/mvp2_rsft_flat_nli_s44 \
    --no-quantize
```

**3) Flat-NLI RSFT s45**
```bash
cd /root/autodl-tmp && python -m freige.eval.inference \
    --model_path /root/autodl-tmp/rsft_output_flat_nli_s45 \
    --sft_adapter /root/autodl-tmp/sft_output \
    --base_model /root/autodl-tmp/models/Qwen3-4B \
    --data_path /root/autodl-tmp/data/docred \
    --split dev \
    --batch_size 16 \
    --max_new_tokens 1024 \
    --seed 42 \
    --output_dir /root/autodl-tmp/eval_results/mvp2_rsft_flat_nli_s45 \
    --no-quantize
```

注意 `rsft_output_flat_nli_s44` 的 root 目录没有 adapter files（只有 README + checkpoint 子目录），所以 model_path 必须指向 `checkpoint-507`。另外两个 root 有完整 adapter，直接用 root 路径。

提交前记得按 C001 约束：`nvidia-smi` 确认 cuda:3 显存占用 < 2GB。

---
