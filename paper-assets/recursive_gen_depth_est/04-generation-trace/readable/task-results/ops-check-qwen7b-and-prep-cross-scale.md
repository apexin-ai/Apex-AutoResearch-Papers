# ops check qwen7b and prep cross scale

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_qwen7b_and_prep_cross_scale_20260516T024608_result.json`
- **Structured JSON:** [`52715e58cce7b1b294cb.json`](../../sessions/52/52715e58cce7b1b294cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## 模型状态

| 模型 | 状态 | 路径 | 大小 |
|------|------|------|------|
| Qwen2.5-7B-Instruct | **已下载完成** | `/root/autodl-tmp/.ms_cache/Qwen/Qwen2___5-7B-Instruct/` (symlink at `Qwen2.5-7B-Instruct`) | 15GB, 4/4 safetensors 分片完整 |
| Qwen2.5-7B (base) | **不存在** | — | — |

任务要求下载的是 **Qwen2.5-7B base model**（非 Instruct）。Instruct 版已有，base 版需要下载。

## GPU 状态

- 2× NVIDIA RTX PRO 6000 Blackwell, 各 96GB VRAM
- 两卡均 **空闲**（0 MiB used, 0% utilization）

## 磁盘

- `/root/autodl-tmp/` 总 250GB，已用 117GB，**剩余 134GB**，下载 Qwen2.5-7B base (~15GB) 无压力

## 代码结构摘要

- **Pipeline 脚本** (`scripts/run_pipeline.sh`): Pythia-1.4B 的完整递归生成链（LoRA finetune → generate → finetune → generate ...），生成 depth_0~3 数据
- **特征提取** (`scripts/extract_features.py`): 用 frozen Pythia-1.4B 提取统计特征（PPL, entropy 等）
- **多模型 pipeline**: 已有 `run_pipeline_gpt2xl.sh`, `run_pipeline_olmo.sh` 等变体
- **LoRA 微调** (`scripts/lora_finetune.py`): 支持任意 depth，`--model_name` 和 `--target_modules` 参数化
- **Zeroshot baseline** (`src/zeroshot_qwen7b_500.py`): 已有 Qwen2.5-7B-Instruct 的 zero-shot 分类脚本
- **cross_scale 相关代码**: **不存在**，需要新建

## 下一步

需要下载 Qwen2.5-7B base model。用 ModelScope 下载到 ms_cache。是否启动下载？

---
