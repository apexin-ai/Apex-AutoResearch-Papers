# ssh spread candidate model check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_spread_candidate_model_check_20260515T220524_result.json`
- **Structured JSON:** [`dcdd89663b8e820762ed.json`](../../sessions/dc/dcdd89663b8e820762ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## 磁盘状态：**满了** (250G/250G, 仅剩 1.6M)

### 空间使用明细

| 路径 | 内容 | 大小 |
|------|------|------|
| .hf_cache/AI-ModelScope/CodeLlama-7b-hf | CodeLlama-7B | 51G |
| .hf_cache/google/gemma-2-9b | Gemma-2-9B | 35G |
| models/LLM-Research/Meta-Llama-3.1-8B | Llama-3.1-8B | 30G |
| .hf_cache/microsoft/Phi-3-medium | Phi-3-medium | 18G |
| .hf_cache/01ai/Yi-1.5-9B | Yi-1.5-9B | 17G |
| .hf_cache/Qwen/Qwen2.5-7B | Qwen2.5-7B | 15G |
| models/Mistral-7B-v0.3 | Mistral-7B | 14G |
| .hf_cache/EleutherAI/pythia-1.4b | Pythia-1.4B | 5.5G |
| **prov_grounded_uie/** | **其他项目（DPO/GRPO训练）** | **68G** |
| 其他 (datasets, hub, codellama空壳等) | — | ~1G |

### 4 个候选模型状态

| 模型 | 在服务器? | 大小 | KV Heads (已知) | Spread 可能性 |
|------|-----------|------|----------------|--------------|
| Falcon-7B | **否** | ~14G | **1** (Multi-Query, 71层×1=71 total) | **最高** — 32:1 GQA |
| DeepSeek-V2-Lite | **否** | ~16G | MLA 架构，非传统 KV heads | 未知，需实测 |
| StableLM-3B-4E1T | **否** | ~6G | 32 (MHA，无 GQA) | 低 |
| MPT-7B | **否** | ~13G | 32 (MHA+ALiBi，无 GQA) | 低 |

### 阻塞问题

**磁盘已满，无法下载任何模型。** 需要先清理空间。可选方案：

1. **删除 `prov_grounded_uie/`**（68G）— 看起来是另一个项目（grounded UIE），与 ratekv 无关
2. **删除已完成 profiling 的模型**（如不再需要的 CodeLlama 51G、Phi-3-medium 18G 等）
3. **删除 Qwen2.5-14B 空壳和其他 0 字节别名目录**（释放微量空间）

下载 Falcon-7B（最高优先级）需要 ~14G，下载所有 4 个候选需要 ~49G。

**请确认可以删除哪些内容**，我立刻清理并开始下载。同时我先在本地查一下 Falcon-7B 的准确配置（32层不是71层，我需要确认）。

---
