# monitor westd 21461 gpu status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd-21461-gpu-status_20260522T052009_result.json`
- **Structured JSON:** [`75652ca4035248cb9919.json`](../../sessions/75/75652ca4035248cb9919.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。汇总如下：

---

## westd-21461 服务器状态

### GPU
| GPU | 型号 | 显存 | 利用率 | 显存占用 |
|-----|------|------|--------|----------|
| 0 | NVIDIA RTX PRO 6000 Black | 96 GB | 0% | 0 MiB |
| 1 | NVIDIA RTX PRO 6000 Black | 96 GB | 0% | 0 MiB |

**两块 GPU 完全空闲，无运行进程。**

### 磁盘
| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (root) | 30G | 21G | 9.5G | 69% |
| /root/autodl-tmp | 250G | 176G | 75G | 71% |

根分区偏紧（9.5G 剩余），数据盘 75G 可用。

### 项目代码
`/root/schema_semantic_constrained_ie/` — 存在，包含完整代码（脚本、编译器、数据、论文目录等）。

### 已下载模型 (`/root/autodl-tmp/models/`)
- `LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4` — 完整（9 个 safetensors 分片 + tokenizer）
- `Mistral-7B-Instruct-v0.3`
- `Qwen3-8B-ms`
- `hugging-quants`
- `mistralai`

### Checkpoints（LoRA / 微调）
**`/root/autodl-tmp/checkpoints/`:**
- `llama_lora_docred_merged`
- `llama_lora_scierc_merged`
- `qwen3_8b_lora_scierc_merged`
- `qwen3_8b_lora_wikievents_merged`
- `qwen_full_ft_scierc`
- `qwen_lora_docred_merged`

**`/root/schema_semantic_constrained_ie/checkpoints/`:**
- `llama_lora_docred`
- `qwen3_8b_lora_wikievents`

SciERC 和 DocRED 的 LoRA checkpoint 均存在（Llama + Qwen 两个模型）。

### 已有输出 (`/root/autodl-tmp/schema_outputs/`)
大量历史推理结果（70b_scierc、docred beam sweep、seed variance、trie baseline、latency 等）。

### Python 环境
- Python 3.10.12（系统），conda 环境在 `/root/miniconda3/`（Python 3.12）
- **PyTorch** 2.8.0+cu128
- **Transformers** 5.8.1
- **PEFT** 0.19.1
- **xgrammar** 0.1.33
- **vLLM** — 未安装

### 结论
**可以直接启动新推理任务。** GPU 空闲、模型和 checkpoint 齐全、核心依赖（torch/transformers/peft/xgrammar）已装好。唯一缺失是 vLLM（如需 vLLM 推理需额外安装）。根分区空间偏紧，新输出建议写到 `/root/autodl-tmp/`。

---
