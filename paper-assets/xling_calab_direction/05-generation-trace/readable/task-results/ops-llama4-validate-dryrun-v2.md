# ops llama4 validate dryrun v2

**xling calab direction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama4-validate-dryrun-v2_20260521T110134_result.json`
- **Structured JSON:** [`bf2b70bd5c6da03e3588.json`](../../sessions/bf/bf2b70bd5c6da03e3588.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

### 下载
- **状态**: 成功，14/14 shard 全部就位，轮询约 21 分钟完成
- **模型路径**: `/root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/`
- **文件**: 14 safetensors (12×4.7G + 2.9G + 2.0G) + config.json + tokenizer.json + tokenizer_config.json + model.safetensors.index.json

### Dry-run
- **状态**: 成功
- **模型**: 48 层, hidden_dim=5120, bfloat16
- **提取层数**: 13 层 `[0,4,8,12,16,20,24,28,32,36,40,44,47]`
- **耗时**: 66s（含模型加载+解压+推理）
- **输出**: 13 个 `L*/` 目录各含 `en_{train,eval}.npy` + `en_{train,eval}_labels.npy`，metadata.json 含 train/eval indices

### 修复项（3 个）
1. `AutoModelForVision2Seq` → `AutoModelForImageTextToText`（transformers 5.x 不兼容）
2. `get_layer_modules` 新增 `model.language_model.model.layers` 路径（ConditionalGeneration 架构）
3. `get_final_norm` 新增 `model.language_model.model.norm` 路径

### GPU 需求
- **单卡 OOM**：compressed_tensors 解压时显存不足（W4A16 压缩权重 ~62GB 占满单卡 95GB，解压需额外缓冲）
- **最低 4 卡**（`CUDA_VISIBLE_DEVICES=0,1,2,3`）才能通过

### 磁盘估算
- Dry-run: 1 sample ≈ 10KB/层/语言（5120 dims × 2 bytes）
- MMLU 全量 ~14,042 samples/语言 → 每层每语言 ~137MB（train 96MB + eval 41MB）
- **全量: 20 langs × 13 layers × 137MB ≈ 35.6 GB**
- **当前剩余: 99 GB** → 充足，无需额外清理

### 环境注意
- 需设置 `HF_HOME=/root/autodl-tmp/.hf_cache` 和 `HF_DATASETS_OFFLINE=1`（HF Hub 网络不通）
- 需 `export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`
- 需安装 `compressed-tensors`（已装）

---
