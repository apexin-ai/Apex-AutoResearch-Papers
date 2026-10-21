# ssh disk cleanup llama download

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_disk-cleanup-llama-download_20260515T063826_result.json`
- **Structured JSON:** [`2a48d36990b8c1c1f161.json`](../../sessions/2a/2a48d36990b8c1c1f161.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

从 5.6GB 增长到 6.8GB，约 30 秒增加 1.2GB，下载速度约 **40MB/s**。

### 结果

**清理**: 4 个目标目录已在上次 worker 中全部删除完毕，磁盘 115GB 可用。

**LLaMA-3.3-70B-Instruct-FP8 下载**:
- PID: **229978**（后台 nohup）
- 模式: 常规 HF 下载（非 hf_transfer），8 分片并行，支持断点续传
- 速度: **~40MB/s**
- 模型总大小: ~75GB（15 个分片 × ~5GB）
- 已下载: 6.8GB（含上次部分数据断点续传）
- 预计完成: **约 30 分钟**
- 日志: `/tmp/llama_download.log`
- 目标路径: `/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/`

另外注意：服务器上有一个实验 exp004（Qwen3-32B, MAVEN dataset）正在 GPU 0 上运行，与下载互不干扰。

---
