# check exp 021 cuda3 status

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_021_cuda3_status_20260516T061214_result.json`
- **Structured JSON:** [`f38393e306989672b5f3.json`](../../sessions/f3/f38393e306989672b5f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-021 状态报告

**状态：崩溃（CRASHED）**

### 崩溃原因

实验在第一个长度（128）的 **seed data 下载阶段** 就失败了。根本原因是网络问题：

```
RuntimeError: Cannot send a request, as the client has been closed.
```

具体路径：`run_pipeline.py:88 → prepare_seed_data() → load_dataset("allenai/c4", "en", split="validation", streaming=True)`

日志显示连接 HuggingFace Hub 时报 `[Errno 99] Cannot assign requested address`，重试后 HTTP client 关闭。**脚本没有 `source /etc/network_turbo`**，导致 AutoDL 网络代理未启用。

### 结果

| 长度 | 数据 | 结果 |
|------|------|------|
| 128 | 目录存在但空 | 目录存在但空 |
| 256 | 不存在 | 不存在 |
| 512 | 不存在 | 不存在 |

三个长度**全部未完成**，无任何 obd_results.json 产出。

### cuda:3 状态

**空闲可用**。0% 利用率，0 MiB 显存占用，无相关进程运行。可立即用于 exp-022。

### 修复建议

重跑 exp-021 时需要在脚本中添加 `source /etc/network_turbo` 以及 SSL 证书环境变量（`REQUESTS_CA_BUNDLE`/`SSL_CERT_FILE`），或改用离线数据集避免网络下载。

---
