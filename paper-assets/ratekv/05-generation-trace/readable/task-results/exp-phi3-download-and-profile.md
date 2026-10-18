# exp phi3 download and profile

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_phi3_download_and_profile_20260515T163926_result.json`
- **Structured JSON:** [`45af03034ea3d403c1b2.json`](../../sessions/45/45af03034ea3d403c1b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

总 incomplete: 294+724+388+231+839+220 = 2.70GB / ~26GB (10.4%)。进程运行约 30 分钟。

下载在持续进行。链式脚本会在下载完成后自动验证并启动 profiling。

当前状态汇总：
- **下载进程**：PID 351291，正在通过 AutoDL 代理从 HuggingFace 下载 Phi-3-medium-128k-instruct
- **已下载**：约 2.7GB/26GB（6 个 shard 并行下载中）
- **自动链式脚本**：PID 352691，等待下载完成后自动验证 + 启动 profiling
- **Registry**：phi3_medium_hires_profiling 已注册为 RUNNING
- **预计完成时间**：下载还需 1-2 小时，profiling 约 30-60 分钟

所有组件已就绪，cron 可自动监控后续状态。

---
