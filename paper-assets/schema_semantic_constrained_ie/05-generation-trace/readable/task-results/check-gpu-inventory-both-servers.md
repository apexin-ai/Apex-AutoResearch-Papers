# check gpu inventory both servers

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu-inventory-both-servers_20260523T044245_result.json`
- **Structured JSON:** [`dfa056362e8dd66da535.json`](../../sessions/df/dfa056362e8dd66da535.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部收集完毕。

---

## 服务器 1: westd-21461

### GPU 状态
| GPU | 利用率 | 显存占用 | 总显存 | 状态 |
|-----|--------|----------|--------|------|
| 0 | 0% | 0 MiB | 97,887 MiB (~96GB) | **空闲** |
| 1 | 87% | 41,607 MiB | 97,887 MiB | **占用中** |

### 可用模型
| 模型 | 路径 | 大小 |
|------|------|------|
| Llama-3.1-70B-Instruct-AWQ-INT4 | `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4/` | 38G |
| Llama-3.1-8B-Instruct | `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/` | 15G |
| Qwen3-8B | `/root/autodl-tmp/models/Qwen3-8B-ms/` | 16G |
| Mistral-7B-Instruct-v0.3 | `/root/autodl-tmp/.ms_cache/mistralai/Mistral-7B-Instruct-v0___3/` (符号链接) | 14G |

### LoRA Checkpoint / Merged 模型
| 名称 | 路径 | 大小 | 类型 |
|------|------|------|------|
| 70b_lora_docred | `/root/autodl-tmp/checkpoints/70b_lora_docred/` | 267M | LoRA adapter (checkpoint-1146) |
| 70b_lora_scierc | `/root/autodl-tmp/checkpoints/70b_lora_scierc/` | 768M | LoRA adapter (checkpoint-663) |
| qwen3_8b_lora_scierc_merged | `/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged/` | 16G | merged |
| qwen_lora_docred_merged | `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged/` | 16G | merged |
| qwen3_8b_lora_wikievents_merged | `/root/autodl-tmp/checkpoints/qwen3_8b_lora_wikievents_merged/` | 16G | merged |
| qwen_full_ft_scierc | `/root/autodl-tmp/checkpoints/qwen_full_ft_scierc/` | 16G | full fine-tune |
| llama_lora_scierc_merged | `/root/autodl-tmp/checkpoints/llama_lora_scierc_merged/` | 15G | merged |
| llama_lora_docred_merged | `/root/autodl-tmp/checkpoints/llama_lora_docred_merged/` | 15G | merged |

### 数据集
| 数据集 | 路径 |
|--------|------|
| DocRED | `/root/schema_semantic_constrained_ie/data/docred/` |
| WikiEvents | `/root/schema_semantic_constrained_ie/data/wikievents/` |
| SFT data | `/root/schema_semantic_constrained_ie/data/sft/` |
| Processed data | `/root/schema_semantic_constrained_ie/data/processed_data/` |

(SciERC 数据通过 `schema_outputs/` 的推理输出文件存在，原始数据可能在 `processed_data` 中)

### 推理/评估/训练脚本
```
/root/schema_semantic_constrained_ie/scripts/eval_d064.py
/root/schema_semantic_constrained_ie/scripts/eval_d066_scierc.py
/root/schema_semantic_constrained_ie/eval_event_extraction.py
/root/schema_semantic_constrained_ie/scripts/train_lora_scierc.py
/root/schema_semantic_constrained_ie/scripts/train_lora_llama_scierc.py
/root/schema_semantic_constrained_ie/scripts/train_lora_docred.py
/root/schema_semantic_constrained_ie/scripts/train_lora_docred_llama.py
/root/schema_semantic_constrained_ie/scripts/train_lora_wikievents.py
/root/schema_semantic_constrained_ie/scripts/train_full_ft_scierc.py
```

### 磁盘空间
**250G 总量，已用 177G，剩余 74G (71%)**

---

## 服务器 2: westd-16980

### GPU 状态
| GPU | 利用率 | 显存占用 | 总显存 | 状态 |
|-----|--------|----------|--------|------|
| 0 | 0% | 0 MiB | 97,887 MiB (~96GB) | **空闲** |
| 1 | 0% | 0 MiB | 97,887 MiB | **空闲** |

### 可用模型
| 模型 | 路径 | 大小 |
|------|------|------|
| Llama-3.1-70B-Instruct-AWQ-INT4 | `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4/` | 38G |
| Llama-3.1-8B-Instruct | `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/` | 15G |
| Qwen3-8B | `/root/autodl-tmp/models/Qwen3-8B-ms/` (符号链接 `Qwen3-8B-link`) | 16G |
| Mistral-7B-Instruct-v0.3 | `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3-ms/` | 14G |
| GoLLIE model | `/root/autodl-tmp/gollie_model/` | 13G |

### LoRA Checkpoint / Merged 模型
| 名称 | 路径 | 大小 | 类型 |
|------|------|------|------|
| 70b_lora_docred | `/root/autodl-tmp/checkpoints/70b_lora_docred/` | 1.1G | LoRA adapter (checkpoint-1146 + final) |
| 70b_lora_scierc | `/root/autodl-tmp/checkpoints/70b_lora_scierc/` | 1.1G | LoRA adapter (checkpoint-663 + final) |
| llama_8b_lora_wikievents | `/root/autodl-tmp/checkpoints/llama_8b_lora_wikievents/` | 1.2G | LoRA adapter (checkpoint-26/39 + final) |
| llama_8b_lora_wikievents_merged | `/root/autodl-tmp/checkpoints/llama_8b_lora_wikievents_merged/` | 15G | merged |
| llama_lora_scierc_merged | `/root/autodl-tmp/checkpoints/llama_lora_scierc_merged/` | 15G | merged |
| llama_lora_docred_merged | `/root/autodl-tmp/checkpoints/llama_lora_docred_merged/` | 15G | merged |
| qwen3_8b_lora_scierc_merged | `/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged/` | 16G | merged |
| qwen_lora_docred_merged | `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged/` | 16G | merged |

### 数据集
| 数据集 | 路径 |
|--------|------|
| ACE05 | `/root/schema_semantic_constrained_ie/data/ace05/` |
| DocRED | `/root/schema_semantic_constrained_ie/data/docred/` |
| WikiEvents | `/root/schema_semantic_constrained_ie/data/wikievents/` |
| RAMS | `/root/schema_semantic_constrained_ie/data/rams/` |
| Synthetic | `/root/schema_semantic_constrained_ie/data/synthetic/` |
| SFT data | `/root/schema_semantic_constrained_ie/data/sft/` |
| Processed data | `/root/schema_semantic_constrained_ie/data/processed_data/` |

### 推理/评估/训练脚本
```
/root/schema_semantic_constrained_ie/scripts/eval_d064.py
/root/schema_semantic_constrained_ie/scripts/eval_d066_unified.py
/root/schema_semantic_constrained_ie/scripts/eval_gollie_scierc.py
/root/schema_semantic_constrained_ie/scripts/eval_gollie_comparison.py
/root/schema_semantic_constrained_ie/eval_event_extraction.py
/root/schema_semantic_constrained_ie/scripts/train_lora_scierc.py
/root/schema_semantic_constrained_ie/scripts/train_lora_llama_scierc.py
/root/schema_semantic_constrained_ie/scripts/train_lora_docred.py
/root/schema_semantic_constrained_ie/scripts/train_lora_docred_llama.py
/root/schema_semantic_constrained_ie/scripts/train_lora_wikievents.py
/root/schema_semantic_constrained_ie/scripts/train_lora_wikievents_llama.py
/root/schema_semantic_constrained_ie/scripts/train_lora_70b_scierc.py
/root/schema_semantic_constrained_ie/scripts/train_lora_70b_docred.py
/root/GoLLIE/src/trainer.py
/root/GoLLIE/src/evaluate.py
```

### 磁盘空间
**250G 总量，已用 173G，剩余 78G (69%)**

---

## 总结

| | westd-21461 | westd-16980 |
|--|------------|------------|
| 空闲 GPU | 1 × 96GB (GPU 0) | **2 × 96GB (全空闲)** |
| 占用 GPU | GPU 1 (87%, 42GB占用) | 无 |
| 基座模型 | 70B-AWQ, 8B-Llama, Qwen3-8B, Mistral-7B | 70B-AWQ, 8B-Llama, Qwen3-8B, Mistral-7B, **GoLLIE** |
| 独有资源 | qwen_full_ft_scierc, qwen3_8b_lora_wikievents_merged | llama_8b_lora_wikievents (未merge adapter), GoLLIE, ACE05/RAMS/Synthetic 数据 |
| 磁盘剩余 | 74G | 78G |

---
