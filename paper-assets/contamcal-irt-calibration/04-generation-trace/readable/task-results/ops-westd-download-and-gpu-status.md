# ops westd download and gpu status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-download-and-gpu-status_20260518T101722_result.json`
- **Structured JSON:** [`986af93d3e2b2233026b.json`](../../sessions/98/986af93d3e2b2233026b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 逐项结果

### 1. 模型下载进度

| 模型 | safetensors 文件数 | 总大小 | incomplete 文件 | 状态 |
|------|-------------------|--------|----------------|------|
| **Qwen2.5-14B** | 5/8 | 26G | 无 | **下载中**，缺 shard 2, 3, 5 |
| **gemma-2-9b** | 4/8 | 23G | 无 | **下载中**，缺 shard 2, 3, 4, 6 |
| **phi-4** | 0 | 1.6G | 无 | **仅下载了配置文件**，safetensors 尚未开始 |
| **OLMo-2-1124-7B** | 1/6 | 13G | 无 | **下载中**，只有 shard 6 |

### 2. 下载进程

两个活跃下载进程：
- **Qwen2.5-14B**: PID 5066，由 `download_all.sh` 触发
- **gemma-2-9b**: PID 6380，由 screen session `dl_gemma` 触发

phi-4 和 OLMo-2 **无活跃下载进程**（可能在 download_all.sh 中排队等前面的完成）。

### 3. GPU 状态

4 × NVIDIA RTX PRO 6000 Blackwell (98GB each)

| GPU | 显存占用 | GPU-Util | 进程 |
|-----|---------|----------|------|
| 0 | 63281/97887 MiB | 99% | PID 17819 (7B pilot 训练) |
| 1 | 0 MiB | 0% | **空闲** |
| 2 | 0 MiB | 0% | **空闲** |
| 3 | 0 MiB | 100% util, 0 MiB mem | **异常**：GPU-Util=100% 但无显存占用，无进程 |

GPU 3 状态异常，可能是驱动残留状态，不影响使用但值得留意。

### 4. 7B pilot 确认

**PID 17819 运行正常。** 启动命令：
```
python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B \
  --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl \
  --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42 \
  --seed 42 --gpu 0 --lr 5e-5 --lora-r 16 --lora-alpha 32 \
  --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048
```

进度：**317/3125 steps (10%)**，速度 ~1.7-2.1 s/it，预计剩余 ~1.3-1.5 小时。

### 5. train_sft.py 参数

脚本路径：`exp001/train_sft.py`（不是根目录的 `train_sft.py`）

全部可用参数（注意都用 **kebab-case**）：

| 参数 | 必需 | 说明 |
|------|------|------|
| `--model-name` | **是** | 模型路径 |
| `--data-path` | **是** | JSONL 训练数据路径 |
| `--output-dir` | **是** | checkpoint 输出目录 |
| `--seed` | 否 | 随机种子 |
| `--max-seq-length` | 否 | 最大序列长度 |
| `--lora-r` | 否 | LoRA rank |
| `--lora-alpha` | 否 | LoRA alpha |
| `--epochs` | 否 | 训练轮数 |
| `--batch-size` | 否 | 单设备 batch size |
| `--grad-accum` | 否 | 梯度累积步数 |
| `--lr` | 否 | 学习率 |
| `--merge` | 否 | 合并 LoRA 到完整模型（默认仅保存 adapter） |
| `--cache-dir` | 否 | HF 缓存目录 |
| `--gpu` | 否 | GPU 设备索引 |
| `--gradient-checkpointing` | 否 | 梯度检查点（7B 必需，省显存） |
| `--load-in-4bit` | 否 | 4-bit 量化加载（QLoRA） |
| `--bnb-4bit-quant-type` | 否 | nf4 或 fp4 |
| `--bnb-4bit-compute-dtype` | 否 | bfloat16 或 float16 |

注意：没有 `--dosage` 参数，dosage 通过 `--data-path` 选择不同的 JSONL 文件实现。

---
