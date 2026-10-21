# code prep server c 5090c

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_server_c_5090c_20260519T062043_result.json`
- **Structured JSON:** [`b07dfee62e4ab0bc202a.json`](../../sessions/b0/b07dfee62e4ab0bc202a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## autodl-5090-c 环境检查报告

### 磁盘空间
- 总量 350GB，已用 86GB，**可用 265GB** — 充足（需 ~30GB）
- `/root/autodl-tmp/struct_self_consist_ie` 占 48GB

### GPU 状态
- **4× RTX 5090，32GB VRAM 每卡，全部空闲（0% 利用率，0MB 占用）**

### 训练环境
需先 `source env.sh` 激活 conda base 环境：
| 组件 | 版本 |
|---|---|
| Python | 3.12.3 |
| PyTorch | 2.10.0+cu128 |
| Transformers | 4.57.1 |
| PEFT | 0.17.1 |
| TRL | 0.24.0 |
| bitsandbytes | 0.49.2 |
| vLLM | 0.18.1 |

### 模型可用性
- **Qwen3-8B**: 已缓存（24GB），路径 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`
- **Llama-3.1-8B-Instruct**: 已缓存
- **Qwen2.5-14B: 未缓存，需要下载（~10GB）**

### FewNERD 数据集
已就绪，含 train/dev/test JSON + LLaMA-Factory 格式数据

### WNUT-17 数据集
**已就绪**，含完整 pipeline：
- 原始数据: train.json (3394行), dev.json (1009行), test.json (1287行)
- LLaMA-Factory 格式: `llmfactory_train.json`, `llmfactory_dev.json`
- 下采样版本: `train_downsampled.json`, `llmfactory_train_downsampled.json`
- 训练配置: `train_config_wnut17.yaml`, `wnut17_lora.yaml`, `export_config_wnut17.yaml`
- Entity types: location, group, corporation 等

### 阻塞问题
**1个阻塞项**: Qwen2.5-14B 模型未缓存，需要下载后才能开始 14B QLoRA 训练。是否现在下载？

---
