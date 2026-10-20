# code prep server a 5090

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_server_a_5090_20260519T062014_result.json`
- **Structured JSON:** [`80f61af01d11507d3ccb.json`](../../sessions/80/80f61af01d11507d3ccb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 环境检查报告

### 磁盘空间
| 指标 | 值 |
|------|------|
| 总量 | 250GB |
| 已用 | 203GB (81%) |
| 可用 | **48GB** |

主要占用：`checkpoints/` 134GB, `output/` 24GB, `.hf_cache/Qwen3-8B` 16GB

### GPU 状态
4x **RTX 5090 32GB**，全部空闲（0% utilization, 2MiB used）

### 模型可用性
- **Qwen2.5-32B：未下载**
- 已缓存：Qwen3-8B (16GB), Llama-3.1-8B-Instruct, Llama-3.2-3B-Instruct, DeBERTa-v3-large

### 训练环境
| 包 | 版本 |
|----|------|
| Python | 3.12 (miniconda3) |
| PyTorch | 2.10.0+cu128 |
| transformers | 4.57.1 |
| peft | 0.17.1 |
| trl | 0.24.0 |
| accelerate | 1.11.0 |
| bitsandbytes | 0.49.2 |
| deepspeed | 0.18.9 |
| vllm | 0.18.1 |

环境完备，无需额外安装。

### FewNERD 数据集
已就绪。train 131K 行, dev 19K 行, test 38K 行。LLaMA-Factory 格式版本也存在（llmfactory_train 1.58M 行）。

### 阻塞问题：磁盘空间不足

**Qwen2.5-32B 全精度权重约 65GB，48GB 可用空间装不下。** 即使用 4-bit 量化加载（~18GB），训练时 checkpoint 还需额外空间，非常紧张。

需要清理旧 checkpoint 释放空间。当前 `checkpoints/` 134GB，包含：
- 5 个 merged 模型（各 ~16GB）= **80GB** — 这些是 8B 模型的完整权重副本
- 多个 LoRA adapter（3-5GB 不等）= **~54GB**

**建议**：删除不再需要的 merged 模型和旧 LoRA，至少释放 ~80GB。请确认哪些 checkpoint 可以清理。

---
