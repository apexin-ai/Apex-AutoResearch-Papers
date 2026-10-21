# code prep server b 5090b

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_server_b_5090b_20260519T062027_result.json`
- **Structured JSON:** [`8ad80ac1748a43b387a9.json`](../../sessions/8a/8ad80ac1748a43b387a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Here's the summary:

---

## autodl-5090-b 环境检查报告

### 1. 磁盘空间
- **总量** 350GB，**已用** 66GB，**可用** 285GB
- 当前占用：`struct_self_consist_ie` 50GB
- **充足**，Qwen2.5-72B 4-bit (~40GB) + 推理输出 (~5GB) 无问题

### 2. GPU 状态
- **4x RTX 5090**，每卡 32GB VRAM，当前全部空闲 (0% utilization, 2MiB used)
- 72B 4-bit tensor parallel 4卡 ~10GB/卡，**完全可行**

### 3. Qwen2.5-72B 模型
- **未下载**。当前只有 Qwen3-8B（及其 LoRA/merged checkpoints）
- 需要下载 `Qwen/Qwen2.5-72B-Instruct-AWQ` 或 `GPTQ-Int4` 量化版（~40GB）
- 预计下载时间：取决于网络，autodl 内网有加速，通常 20-40 分钟

### 4. 推理环境（需 `source env.sh`）
| 组件 | 版本 |
|------|------|
| Python | 3.12.3 |
| PyTorch | 2.10.0+cu128 |
| transformers | 4.57.1 |
| vLLM | 0.18.1 |
| bitsandbytes | 0.49.2 |

vLLM 0.18.1 支持 AWQ/GPTQ 4-bit + tensor parallel，**环境就绪**。

### 5. 数据集
三个数据集均已存在：
- `scierc/` — processed_data 目录
- `conll2003/` — train/dev/test JSON + llmfactory 格式
- `fewnerd/` — train/dev/test JSON + llmfactory 格式

### 6. 推理代码
- `run_mvp_pilot.py` 已存在，支持 `--dataset`, `--tensor_parallel`, `--temperature`, `--n_samples` 等参数
- `sampling.py` 含完整 prompt 模板（NER/RE/Full/Train-aligned）和 vLLM sampler
- 现有 prompt 是面向 fine-tuned 模型的 UIE 格式，**72B zero-shot 推理可能需要调整 prompt**（Qwen2.5-72B-Instruct 没有经过 UIE 格式微调）

### 7. 可行性评估

| 项目 | 状态 |
|------|------|
| 磁盘 | OK (285GB free) |
| GPU | OK (4x 5090, 128GB total VRAM) |
| 软件栈 | OK (vLLM 0.18.1 + transformers 4.57.1) |
| 数据 | OK (3/3 datasets present) |
| 代码 | OK (pipeline ready) |
| 模型 | **需下载** (~40GB) |
| Prompt | **可能需调整** (现有 prompt 为 fine-tuned UIE 格式，zero-shot 72B 可能需要更详细的 instruction 或 few-shot examples) |

### 待执行
1. 下载 Qwen2.5-72B 4-bit 量化模型（AWQ 推荐，vLLM 原生支持）
2. 评估是否需要为 zero-shot 场景调整 prompt template

---
