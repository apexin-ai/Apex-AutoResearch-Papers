# ops check server models and qwen progress

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_server_models_and_qwen_progress_20260516T044842_result.json`
- **Structured JSON:** [`28c6663389513ffdb6d1.json`](../../sessions/28/28c6663389513ffdb6d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### QWEN PIPELINE PROGRESS
正在执行 **depth-4 生成**阶段——depth-3 的 QLoRA 训练已完成（final loss: 1.2019），LoRA adapter 已保存到 `checkpoints/qwen7b_nucleus/lora_depth_3`。当前正在加载模型准备生成 depth-4 数据。

### GPU STATUS
| GPU | 利用率 | 显存使用 | 总显存 |
|-----|--------|----------|--------|
| 0 | 54% | 8321 MiB | 97887 MiB |
| 1 | 0% | 0 MiB | 97887 MiB |

### QWEN DATA (`data/qwen7b_nucleus/`)
```
depth_0.jsonl  1.1MB  May 16 11:01
depth_1.jsonl  1.1MB  May 16 11:28
depth_2.jsonl  1.1MB  May 16 11:58
depth_3.jsonl  1.2MB  May 16 12:25
depth_4.jsonl  954KB  May 16 12:49  ← 正在生成中(可能未完成)
```

### ALL MODELS

**HF cache:**
- EleutherAI/pythia-1.4b, pythia-410m
- FacebookAI/roberta-base
- Qwen/Qwen2.5-1.5B, Qwen3-8B
- allenai/OLMo-1B, OLMo-1B-hf
- microsoft/deberta-v3-base, deberta-v3-large
- openai-community/gpt2-xl
- roberta-base, roberta-large

**ModelScope cache:**
- allenai/OLMo-1B-hf
- iic/nlp_deberta-v3-base_backbone
- **Qwen/Qwen2.5-7B-Instruct**

**models/ 目录:**
EleutherAI, Qwen, Qwen2.5-1.5B, Qwen3-8B, deberta-v3-base, deberta-v3-base-ms, deberta-v3-large, gpt2-xl, olmo-1b, olmo-1b-hf, pythia-1.4b, pythia-410m, roberta-base, roberta-base-ms, roberta-large, roberta-large-ms

### LLAMA CHECK
```
/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct
/root/autodl-tmp/.hf_cache/._____temp/LLM-Research/Meta-Llama-3.1-8B-Instruct
```
Llama-3.1-8B-Instruct 存在（在 HF cache 中）。

### DISK
```
/dev/md0  250G  117G used  134G avail  47%
```

---
