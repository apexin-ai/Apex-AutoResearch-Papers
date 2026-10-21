# ops d143 cleanup disk

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d143-cleanup-disk_20260519T125514_result.json`
- **Structured JSON:** [`10806e7a10fc3be9b62b.json`](../../sessions/10/10806e7a10fc3be9b62b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 删除的文件和释放空间

| 文件/目录 | 大小 |
|-----------|------|
| `/root/autodl-tmp/d143_pw_exec_s42/` | **15 GB** |
| `/root/autodl-tmp/d143_proofwriter_pipeline.sh` | 8 KB |
| `/root/autodl-tmp/d143_pipeline.log` | 96 KB |
| `/root/solver-trace-ablation/data/proofwriter_real_train_500.jsonl` | 328 KB |
| `/root/solver-trace-ablation/data/proofwriter_real_eval_100.jsonl` | 68 KB |

**总计释放：~15 GB**（数据盘从 60G used → 45G used）

### 2. 当前磁盘使用

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/root/autodl-tmp` (数据盘) | 250G | **45G** | **206G** | 18% |
| `/root` (系统盘) | 30G | 11G | 20G | 34% |

### 3. LLaMA 下载状态

两个并行下载正在进行中：
- **HF 下载** (`hf download`): 正在下载 `model-00001-of-00002.safetensors`，刚开始
- **ModelScope 下载** (nohup): 两个 shard 同时下载中，速度约 400 KB/s，预计还需数小时
  - `model-00001-of-00002.safetensors`: 39M/4.62G (1%)
  - `model-00002-of-00002.safetensors`: 37M/1.36G (3%)

当前 Llama-3.2-3B 目录已有 4.1G（部分文件已下载完成），ModelScope cache 196M。

### 4. 前 10 大目录

| 目录 | 大小 |
|------|------|
| `models/` | **40 GB** (Qwen3-8B 16G, Qwen3-4B×2 15G, Qwen3-1.7B 5G, Llama 4G) |
| `outputs/` | 501 MB |
| `d142_gated_isr_s52~s57` (6个) | 各 16-17 MB |
| 其余为日志文件 | < 5 MB |

---
