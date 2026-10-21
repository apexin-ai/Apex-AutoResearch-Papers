# ssh qwen72b download autodl

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_qwen72b_download_autodl_20260524T005414_result.json`
- **Structured JSON:** [`a833fba00f582b88152b.json`](../../sessions/a8/a833fba00f582b88152b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载正常运行中。

**报告：**

| 项目 | 状态 |
|------|------|
| 下载方式 | ModelScope（国内 CDN） |
| PID | 496190 |
| 磁盘空间 | /root/autodl-tmp 剩余 80GB，充足 |
| 当前进度 | 并行下载 11 个 safetensors 分片中，每个 ~3.6-3.7GB，速度 ~2-4 MB/s |
| 预估时间 | 模型总量 ~40GB，当前速度约 2-4 MB/s 并行，预计 **30-50 分钟**完成 |

下载在后台运行，可随时用 `tail -20 /tmp/download_qwen72b_awq.log` 检查进度。完成后模型路径为 `/root/autodl-tmp/models/Qwen/Qwen2.5-72B-Instruct-AWQ/`。

---
