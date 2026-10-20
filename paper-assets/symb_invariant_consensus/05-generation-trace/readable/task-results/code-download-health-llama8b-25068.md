# code download health llama8b 25068

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_download-health-llama8b-25068_20260518T101818_result.json`
- **Structured JSON:** [`0666c8b32e54e80aa77d.json`](../../sessions/06/0666c8b32e54e80aa77d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个下载都在正常运行。最终状态：

| 模型 | 状态 | 已下载 | 进程 |
|------|------|--------|------|
| Qwen2.5-72B | 运行中 | 41 GB (19/37 shards) | PID 5399 |
| Qwen2.5-14B | 运行中 | 14 GB | PID 16416 |
| LLaMA-3.1-8B | 已启动 (modelscope) | 116 MB | PID 17783 |
| 磁盘 | 197 GB 可用 (22% used) | | |

备注：LLaMA-8B 的 HF 下载因 gated repo 权限被拒（Meta 未批准该 token），已自动切换到 modelscope 镜像（`LLM-Research/Meta-Llama-3.1-8B-Instruct`），当前速度约 430 kB/s，预计数小时完成。

---
