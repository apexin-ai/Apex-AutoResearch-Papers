# prep 5090b gpu inventory

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_5090b_gpu_inventory_20260520T221308_result.json`
- **Structured JSON:** [`5865e6b20ce9256860b8.json`](../../sessions/58/5865e6b20ce9256860b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 5090-b 实验就绪度报告

### 可用模型
| 模型 | 路径 | 状态 |
|------|------|------|
| **Qwen2.5-7B-Instruct** | `/root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct/` | 完整（~14GB，4个 safetensors） |
| **Qwen3-8B** | `.hf_cache/models--Qwen--Qwen3-8B` | 可用 |
| **Qwen2.5-72B-Instruct-AWQ** | `.hf_cache/models--Qwen--Qwen2.5-72B-Instruct-AWQ` | 可用 |
| **LLaMA-3.1-8B-Instruct** | `.hf_cache/LLM-Research/` + `.hf_cache/llama3.1-8b-instruct/` | 可用 |
| **Qwen2.5-32B-Instruct** | `.hf_cache/Qwen/Qwen2___5-32B-Instruct/` | **下载中**（7.3GB/~60GB，2/17 shards 完成，当前 ~3-5MB/s） |

### 已有 LoRA checkpoints（16个）
包括 Qwen3-8B 和 LLaMA-3.1-8B 在 CoNLL/FewNERD/SciERC 上的各种 LoRA 和 merged 模型，以及 SCD 变体（scd-conll, scd-fewnerd, scd-fewnerd-fallback, scd-theta3）。

### 环境
- **GPU**: 4× RTX 5090 (32GB)，全部空闲（0% 利用率，2MB 显存占用）
- **vLLM**: v0.18.1
- **PyTorch**: 2.10.0+cu128，CUDA 可用，4 GPU
- **Python**: `/root/miniconda3/bin/python`（conda 环境）

### 代码部署
项目代码完整部署在 `/root/autodl-tmp/struct_self_consist_ie/`，包含：
- `code/` — 完整分析和推理代码（sampling.py, run_mvp_pilot.py 等）
- `scripts/` — 后处理脚本
- `data/` — 数据集
- `output/` — 已有实验输出（多 seed、72b zeroshot/fewshot、SCD eval 等）

### 32B 下载进度
正在下载中，当前完成 2/17 shards（~7.3GB），速度 3-5MB/s，预计还需数小时。

### 可立即执行的实验
1. **额外 seed 实验** — Qwen2.5-7B / Qwen3-8B / LLaMA-3.1-8B 的 LoRA 模型都已就绪，可跑更多 seed 的 NER 推理
2. **CoNLL T_ablation** — 已有 merged checkpoints，可用 vLLM 做温度消融
3. **SCD 评估** — 已有 scd-conll/scd-fewnerd 的 merged 模型和评估脚本（`eval_scd_*.py`）
4. **FewNERD SCD theta3 变体** — LoRA 训练完成（`qwen3-8b-fewnerd-scd-theta3-lora`），可 merge 后评估

4 块 5090 全部空闲，可并行跑多个实验。

---
