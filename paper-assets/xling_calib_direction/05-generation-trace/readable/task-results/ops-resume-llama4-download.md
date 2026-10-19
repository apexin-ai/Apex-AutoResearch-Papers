# ops resume llama4 download

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_resume-llama4-download_20260521T073949_result.json`
- **Structured JSON:** [`74f18a893ced5a3148e3.json`](../../sessions/74/74f18a893ced5a3148e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程均在运行。

**结果：**

| 任务 | PID | 状态 |
|------|-----|------|
| Llama4 Scout W4A16 恢复下载 | 67791 | 运行中，8/27 文件已存在，正在下载剩余 6 个 shard（00004, 00009, 00011-00014），每个 ~4.9GB |
| Telugu GlobalMMLU | 67841 | 运行中，数据集加载/下载中 |

**注意事项：**
- 两个下载都未认证（unauthenticated），速率受限。如果速度太慢，可设置 `HF_TOKEN` 加速。
- Llama4 剩余约 ~30GB，按 AutoDL 代理速度预计需要数小时。
- 可用 `tail -5 /tmp/llama4_download.log` 和 `tail -5 /tmp/te_download.log` 随时查看进度。

---
