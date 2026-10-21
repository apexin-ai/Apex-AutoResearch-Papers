# code olmo retrain v3 setup

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_olmo-retrain-v3-setup_20260520T095025_result.json`
- **Structured JSON:** [`5892aa45a83145954032.json`](../../sessions/58/5892aa45a83145954032.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇报如下：

---

## OLMo-1B Retrain Chain 实验准备完成

### 环境状态
| 项目 | 状态 |
|------|------|
| Python | 3.12.3 (conda base) |
| PyTorch | 2.8.0+cu128 |
| transformers | 5.8.1 |
| peft | 0.19.1 |
| lightgbm / sklearn | 4.6.0 / 1.8.0 |
| GPU | 4x RTX 4090D (24GB), cuda:2 空闲 (0 MiB used) |

### 模型和数据
| 资源 | 路径 | 状态 |
|------|------|------|
| OLMo-1B-hf | `/root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf/` | 完整 (4.4GB, model load + generate + LoRA 验证通过) |
| Qwen2.5-1.5B scorer | `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B/` | 存在 |
| Seed data (depth_0) | `data/olmo_retrain_chain/depth_0.jsonl` | 5000 docs (前次 run 已 copy) |

### 脚本
- **路径**: `/root/autodl-tmp/gen-depth-contamination/scripts/exp_olmo_retrain_v3.py`
- 基于 `exp_olmo_retrain_chain.py`，修复了 `torch_dtype` → `dtype` 弃用警告
- `--help` dry-run 通过

### 运行命令
```bash
CUDA_VISIBLE_DEVICES=2 python scripts/exp_olmo_retrain_v3.py --device cuda:0 --max_depth 4
```
注意：`CUDA_VISIBLE_DEVICES=2` 使物理 GPU2 映射为 `cuda:0`。

### 关键参数
- LoRA: rank=16, alpha=32, targets=q/k/v_proj, trainable 3.1M/1180M (0.27%)
- Training: lr=2e-4, batch=4, grad_accum=4, 1 epoch/generation
- Decoding: nucleus p=0.95, T=1.0, max_new_tokens=256
- Depth: 0→4 (4 generations)

### 预计运行时间
每代包含 LoRA fine-tune (5000 docs, ~15min) + generation (5000 docs, ~20min)，加上 feature extraction (~10min) 和 analysis。总计约 **2.5~3 小时**。

### 阻塞问题
无。全部验证通过，可以提交训练任务。

---
