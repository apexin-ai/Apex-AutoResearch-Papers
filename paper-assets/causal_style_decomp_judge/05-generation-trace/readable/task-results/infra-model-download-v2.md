# infra model download v2

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_model_download_v2_20260520T084430_result.json`
- **Structured JSON:** [`661802f9bff4d5ca8c7d.json`](../../sessions/66/661802f9bff4d5ca8c7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

速度提升到 ~1MB/s。Qwen3 下载 2.3GB/~64GB，多文件并行。NLI wget 进行中。

当前状态汇报：

**Qwen3-32B（ModelScope 下载，PID 2964）**
- 已下载：2.3GB / ~64GB
- 速度：~1MB/s per shard，多个 shard 并行下载
- 路径：`/root/autodl-tmp/models/Qwen3-32B/`
- 预计：3-5 小时完成

**NLI 模型（wget 下载，PID 4220）**
- 已下载：~18MB / ~1.5GB
- 速度：~300-400 kB/s
- 路径：`/root/autodl-tmp/models/nli-deberta-v3-large/`
- 配置文件（config.json, tokenizer 等）已就绪
- 预计：~1 小时完成 model.safetensors

**问题说明**
- 服务器带宽有限，HuggingFace xet CDN 完全不通
- ModelScope CDN 和 hf-mirror.com 的直接文件下载可用但较慢
- 两个下载都在后台 nohup 运行，不会因 SSH 断开而中断

**磁盘空间**
- `/root/autodl-tmp/` 数据盘 250GB，当前几乎空，足够容纳两个模型

需要我定期轮询进度吗？还是等你下次回来再检查？

---
