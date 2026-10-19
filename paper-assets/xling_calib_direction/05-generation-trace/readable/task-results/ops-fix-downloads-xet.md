# ops fix downloads xet

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_downloads_xet_20260521T024744_result.json`
- **Structured JSON:** [`a716853a8cef047e0032.json`](../../sessions/a7/a716853a8cef047e0032.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

| 模型 | 旧PID | 操作 | 新PID | 已有数据 |
|------|-------|------|-------|---------|
| Llama4 | 51303 | kill + 删错误目录 + 重启续传 | **53308** | 7/14 shards, 43GB |
| Qwen3 | 51304 | kill (xet超时) + 重启续传 | **53359** | 5.4GB |

两个下载均已用 `HF_HUB_DISABLE_XET=1` + `hf-mirror.com` 重启。磁盘 215G 可用，空间充足。报告已写入 `artifacts/download_fix_result.md`。

---
