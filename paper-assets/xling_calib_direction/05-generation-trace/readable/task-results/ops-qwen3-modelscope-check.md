# ops qwen3 modelscope check

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen3-modelscope-check_20260521T074110_result.json`
- **Structured JSON:** [`fd083861d2ad119a4d8a.json`](../../sessions/fd/fd083861d2ad119a4d8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据够了，汇总报告：

## 结果

### 1. ModelScope 可用性
**有。** Model ID: `Qwen/Qwen3-235B-A22B-GPTQ-Int4`，116GB，6万+ 下载量。

### 2. 下载已切换
- 已 kill HF 下载进程 (PID 53359)
- ModelScope 下载已启动 (PID 68080)
- **8 路并行下载**，单流 1.7-2.7 MB/s，聚合带宽 ~16 MB/s
- ModelScope 没有复用 HF 已下载的 6 个 shard，从头下载全部 32 个
- **预计总耗时 ~2 小时**（vs. HF 的 ~27h 剩余），加速约 13x

### 3. 磁盘空间
- 数据盘 350GB，已用 175GB，剩余 176GB
- Qwen3 还需 ~75GB，Llama4 还需 ~34GB，总计 ~109GB — 够用

### 4. Llama4 下载状态
- PID 67796 在跑，8/27 files (46GB)
- 也是 HF 源（同样偏慢），但文件较小，暂不切换

日志文件：`/tmp/qwen3_modelscope.log`，可随时 `tail` 查看进度。

---
