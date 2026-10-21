# code gpu progress check

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpu-progress-check_20260521T182323_result.json`
- **Structured JSON:** [`5a1bd0742939cf3be127.json`](../../sessions/5a/5a1bd0742939cf3be127.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## autodl-rtx6000 进度报告

### 1. GPU 利用率

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 0 / 96 GB |
| 1 | 100% | 0 / 96 GB |
| 2 | 0% | 0 / 96 GB |
| 3 | 0% | 0 / 96 GB |

GPU 1 显示 100% 利用率但 0 显存占用，可能是后台 kernel 活动或报告异常。**无模型加载推理**。

### 2. 模型下载进度

| 模型 | 预估总大小 | 已下载(final+temp) | 进度 | 状态 |
|------|-----------|-------------------|------|------|
| Gemma-2-9B-IT | ~18 GB | 11 GB (temp) | ~61% | 下载中 |
| Llama-3.1-8B-Instruct | ~14 GB | 1.2G final + ~8G temp | ~65% | 下载中 |
| Qwen2.5-7B-Instruct | ~14 GB | 1.1G final + 5G temp | ~43% | 下载中 |
| Mistral-7B-Instruct-v0.3 | ~15 GB | 3.2M final + 1.5G temp | ~10% | 下载中 |

ModelScope cache 另有 7.5G（LLM-Research 目录），可能是早期下载的备份。

### 3. 当前运行进程

有 **3 个下载进程** 并行跑：
- `sequential_download.py` (PID 8925) — 正在下载 Llama shards
- `download_models.py` (PID 11382) — 正在下载 Gemma/Mistral
- `download_and_annotate.py` (PID 12489) — 正在下载 Qwen（下完后会自动开始标注）

辅助脚本：`launch_when_ready.sh`、`auto_launch.sh`、`run_all.sh` 也在后台等待。

### 4. 标注 log

**唯一的 log 文件 `log_llama31.txt`**：Llama 标注曾经尝试但 **失败**了：
```
FileNotFoundError: .../model-00001-of-00004.safetensors
```
原因是 Llama 模型尚未下载完成（只有 shard 4 到了 final 目录，shard 1-3 还在下载）。

### 5. 预估完成时间

下载速度约 **600-1000 kB/s/stream**，多 shard 并行聚合约 2.5 MB/s：

| 模型 | 剩余 | 预估完成 |
|------|------|---------|
| Llama | ~5 GB | ~35 min → **~03:00** |
| Gemma | ~7 GB | ~47 min → **~03:10** |
| Qwen | ~8 GB | ~55 min → **~03:20** |
| Mistral | ~13 GB | ~90 min → **~03:55** |

**全部下载完成预计 ~04:00**（北京时间），之后才能开始标注推理。标注尚未真正开始，当前阶段完全是模型下载。

---
