# code gpu download check

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpu-download-check_20260521T193646_result.json`
- **Structured JSON:** [`51962eaafd6e05d4adc5.json`](../../sessions/51/51962eaafd6e05d4adc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### GPU
- 4 块 GPU，GPU 1 利用率 100%（但显存占用 0 MiB，说明在做 I/O 密集任务而非推理），其余 3 块空闲

### 模型下载（通过 ModelScope）
| 模型 | 已下载 | 总大小(估) | 状态 |
|------|--------|-----------|------|
| **Qwen2.5-7B-Instruct** | 2.8 GB | ~15 GB | 下载中（之前的进程，日志显示已在序列下载） |
| **Llama-3.1-8B-Instruct** | 1.2 GB | ~15 GB | **正在下载**（PID 21964，4 个 shard 并行下载，速度 ~550-700 KB/s） |
| **Mistral-7B-Instruct-v0.3** | 3.2 MB | ~15 GB | 几乎未开始 |

临时下载缓存 `._____temp/` 占 28 GB，说明有大量 shard 正在写入中。

### 标注进度
- **无标注脚本在运行**，无 GPU 推理进程
- 唯一产出：`pilot_gemini_annotations.csv`（60KB，Gemini API 标注的 pilot 数据，非本地模型产出）
- 无本地模型标注结果

### Llama 标注未开始的原因
**模型下载未完成。** Llama 当前正在通过 ModelScope 下载（4 个 shard，每个 3.3-4.6 GB），下载速度约 550-700 KB/s，按当前进度：
- shard 4: 已 80%，预计 ~20 分钟完成
- shard 1-3: 30-61%，预计 **50-80 分钟**完成

三个模型（Qwen/Llama/Mistral）都还没下载完，序列下载脚本在跑但速度很慢（AutoDL 代理限速）。全部下载完预计还需 **2-3 小时**。

---
