# infra env setup mvp001

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_env-setup-mvp001_20260511T221147_result.json`
- **Structured JSON:** [`77efb5d604cfb3e24cd5.json`](../../sessions/77/77efb5d604cfb3e24cd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型加载和推理验证通过。最终环境报告：

---

## MVP 环境报告 — seetacloud-bjb2-structtts

| 项目 | 值 |
|------|-----|
| **GPU** | NVIDIA GeForce RTX 5090, 31GB VRAM |
| **CUDA** | 12.8 |
| **Python 环境** | conda base (`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`) |
| **Python 版本** | 3.12.3 |
| **torch** | 2.10.0+cu128, CUDA 可用, 1 GPU |
| **transformers** | 4.57.6 |
| **模型路径** | `/root/autodl-tmp/models/deepseek-r1-distill-qwen-7b/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B` |
| **模型大小** | 7.62B params, 15GB 磁盘占用, bf16 加载到 cuda:0 |
| **数据盘剩余** | 221GB / 250GB (12% used) |
| **项目目录** | `/home/sonny/redundancy-compound-sparsity/results/mvp/` |

推理验证通过——tokenizer 加载、模型加载到 GPU、生成 token 均正常。

---
