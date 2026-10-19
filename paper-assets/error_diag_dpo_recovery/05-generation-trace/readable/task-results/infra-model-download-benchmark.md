# infra model download benchmark

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_model-download-benchmark_20260512T105444_result.json`
- **Structured JSON:** [`37c5f04ca66863ebe831.json`](../../sessions/37/37c5f04ca66863ebe831.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**执行摘要：**

1. **模型下载加速**：HF 下载慢 (~1MB/s) → 杀掉 HF 下载 + 4 个重复的 Qwen2.5 下载 → 用 hf-mirror.com 并行 wget 4 个 safetensors（关键发现：不走 network_turbo 代理速度从 ~2MB/s 提升到 ~15MB/s，因为 hf-mirror.com 本身就是中国 CDN，不需要代理）
2. **模型路径**: `/root/autodl-tmp/.hf_cache/Qwen3-8B`，5 个 safetensors 全部下载完成 (16.4GB)
3. **Benchmark 结果**:
   - 训练 step time: **0.28s**（2048 tokens，排除 warmup）
   - 推理: **15.5 tokens/sec**
   - GPU 内存: **10.6GB**（4-bit 量化，单卡 4090D 轻松承载）

---
