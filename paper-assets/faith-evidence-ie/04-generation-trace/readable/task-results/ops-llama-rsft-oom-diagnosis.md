# ops llama rsft oom diagnosis

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama_rsft_oom_diagnosis_20260516T154223_result.json`
- **Structured JSON:** [`97c6b5d2294e8c9aba96.json`](../../sessions/97/97c6b5d2294e8c9aba96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have all the data needed. Here's the diagnosis and retry plan:

---

## OOM 根因分析

**核心原因：GPU 共享导致显存不足，非模型本身过大。**

证据对比：
| | Qwen3-8B (成功) | LLaMA-3.1-8B (失败) |
|---|---|---|
| 模型参数 | ~8.2B (36层, FFN=12288) | ~8.0B (32层, FFN=14336) |
| bf16 权重 | ~16.4GB | ~16.0GB |
| KV cache peak (batch=8×5120 tokens) | ~5.8GB (36层) | ~5.1GB (32层) |
| 观测显存占用 | 28067 MiB | 被 kill |
| `CUDA_VISIBLE_DEVICES` | **=3 (已设)** | **未设或 GPU 被占** |

Qwen3-8B 更大、KV cache 更多，却稳定运行，说明 LLaMA OOM 是因为 cuda:1 当时被其他进程占用（与现在 cuda:1 被 eval 占 10.3GB 的情形一致）。没有设 `CUDA_VISIBLE_DEVICES` 或目标 GPU 不干净，`device_map="auto"` 加载到已有 10+GB 占用的 GPU 上，16GB 模型 + 5GB KV cache + 10GB 已有 > 32GB → OOM killed。

SFT adapter 额外开销：merge_and_unload 过程中临时多占 ~670MB（adapter_model.safetensors）。

---

## 推荐重试方案

### 方案 A（首选）：bf16 全精度，等 GPU 空闲

**前提**：等 cuda:1 上的 eval (PID 353322) 完成后，GPU 显存 < 2GB。

```bash
# 先确认 GPU 空闲
nvidia-smi -i 1 --query-gpu=memory.used --format=csv,noheader
# 确认 < 2GB 后执行：

CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 \
nohup python -m freige.training.rsft_generate \
    --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B \
    --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b \
    --num_generations 8 \
    --temperature 0.7 \
    --batch_size 1 \
    --max_new_tokens 1024 \
    --data_path /root/autodl-tmp/data/docred \
    --split train \
    --seed 42 \
    --output_dir /root/autodl-tmp/freige/outputs/rsft_candidates_llama_8b \
    > /root/autodl-tmp/logs/plan_016_llama_rsft_candidates_r3.log 2>&1 &
```

**预估显存**：16GB(模型) + 5GB(KV cache peak) + 2GB(activations/overhead) ≈ **23-28GB / 32GB**（与 Qwen3-8B 表现一致）

**优势**：断点续传自动跳过已完成的 64 docs，从第 65 个继续。

---

### 方案 B（立即可用）：4-bit 量化

如果不想等 GPU 空闲：

```bash
CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 \
nohup python -m freige.training.rsft_generate \
    --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B \
    --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b \
    --num_generations 8 \
    --temperature 0.7 \
    --batch_size 1 \
    --max_new_tokens 1024 \
    --quantize \
    --data_path /root/autodl-tmp/data/docred \
    --split train \
    --seed 42 \
    --output_dir /root/autodl-tmp/freige/outputs/rsft_candidates_llama_8b \
    > /root/autodl-tmp/logs/plan_016_llama_rsft_candidates_r3.log 2>&1 &
```

**预估显存**：5GB(4bit模型) + 5GB(KV cache, bf16) + 2GB(overhead) ≈ **12-14GB / 32GB**

**代价**：4-bit 量化可能略降生成质量。由于 RSFT 依赖 candidate diversity 和质量，bf16 优先。但量化可立即运行无需等待。

---

### 关键注意事项

1. **必须设 `CUDA_VISIBLE_DEVICES`**（C002/C003），禁止依赖 `device_map="auto"` 自动分配
2. 方案 A 须遵守 C001：launch 前 `nvidia-smi -i 1` 确认 < 2GB
3. 断点续传已内置（progress.json 记录 64 已完成 doc_ids），无需清空 output_dir
4. 输出文件 generations.jsonl 以 append 模式写入，已有的 512 行保持不变

---
