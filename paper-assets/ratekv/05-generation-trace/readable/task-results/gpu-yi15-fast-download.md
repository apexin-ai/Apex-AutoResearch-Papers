# gpu yi15 fast download

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_yi15_fast_download_20260514T152841_result.json`
- **Structured JSON:** [`06b1920691d490d3fc31.json`](../../sessions/06/06b1920691d490d3fc31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现状总结：

- **下载方式已经是 ModelScope**（PID 228878），不是 HF，但速度同样只有 ~390KB/s — 瓶颈在网络，不在下载源
- **进度**：4 个 shard 中已完成 2 个（shard 2: 4.7G, shard 4: 2.6G），剩余 shard 1 (70%, 还需 ~1.35G) 和 shard 3 (78%, 还需 ~1.03G)
- **wait_and_run_yi15_v2.sh**（PID 233159）正在轮询，下载完成后会自动启动 pipeline（`CUDA_VISIBLE_DEVICES=1`）
- 无 aria2c，无 hf_transfer

**判断**：剩余 2 shards 已下载 70-78%，kill 后重启任何方式都要重下这 ~2.4G（ModelScope 不支持断点续传到新进程），而网络本身就慢，切换下载源不会提速。预计 50-60 分钟内完成，wait 脚本会自动启动 pipeline。

kill 会浪费已下载的 70-78% 进度，净效果是更慢。建议让当前下载跑完 — 自动化已就绪，无需人工干预。

是否仍要 kill？

---
