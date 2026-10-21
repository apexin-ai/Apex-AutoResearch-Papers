# ops inspect 16980 processes

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_inspect-16980-processes_20260520T082455_result.json`
- **Structured JSON:** [`317b5d3d8d3a36c4a9f3.json`](../../sessions/31/317b5d3d8d3a36c4a9f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息如下：

---

## PID 728348 完整命令行

```
python run_constrained_extraction.py \
  --mode full_s1 \
  --dataset docred \
  --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged \
  --data_path data/docred/dev.json \
  --constraints_path data/docred/ontology_constraints_docred.json \
  --output_path /root/autodl-tmp/schema_outputs/d065_qwen_docred_greedy_con_4096.jsonl \
  --device cuda:0 \
  --max_new_tokens 4096 \
  --seed 42 \
  --decoding_strategy greedy \
  --skip_on_error
```

## PID 732035 完整命令行

```
python run_constrained_extraction.py \
  --mode full_s1 \
  --dataset docred \
  --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged \
  --data_path data/docred/dev.json \
  --constraints_path data/docred/ontology_constraints_docred.json \
  --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/qwen_docred_200_beam2_full_s1.jsonl \
  --device cuda:0 \
  --max_new_tokens 4096 \
  --max_docs 200 \
  --seed 42 \
  --decoding_strategy beam \
  --num_beams 2 \
  --skip_on_error
```

## nvidia-smi

```
2× NVIDIA RTX PRO 6000 Blackwell (98GB each)
GPU 0: 51°C, 280W/600W, 37836MiB/97887MiB, 92% util
GPU 1: idle, 0MiB

PID 728348 → GPU 0, 18910MiB
PID 732035 → GPU 0, 18912MiB
```

## 环境变量

两个进程均为 `CUDA_VISIBLE_DEVICES=0`

---

## 确认项

| 项目 | PID 728348 | PID 732035 |
|------|-----------|-----------|
| 模型 | **Qwen** (`qwen_lora_docred_merged`) | **Qwen** (同) |
| max_new_tokens | **4096** ✓ | **4096** ✓ |
| decoding_strategy | **greedy** | **beam** (`num_beams=2`) |
| 数据集 | `data/docred/dev.json` (全量) | `data/docred/dev.json` (`max_docs=200`) |
| GPU | **GPU 0** | **GPU 0** |

注意：两个进程都挤在 GPU 0 上（共占 ~37.8GB/98GB），GPU 1 完全空闲。

---
