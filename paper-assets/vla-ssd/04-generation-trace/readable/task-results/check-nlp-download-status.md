# check nlp download status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_nlp_download_status_20260522T082510_result.json`
- **Structured JSON:** [`98de8b6d76f71e49370d.json`](../../sessions/98/98de8b6d76f71e49370d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 下载状态汇总

| 项目 | 状态 |
|------|------|
| **shard2** (model-00002-of-00002.safetensors) | **已完成** — 3.3G/3.26G (100%) |
| **shard1** (model-00001-of-00002.safetensors) | **下载中** — 3.94G/9.29G (**42%**) |
| **下载速度** | ~407-450 KB/s (ModelScope CDN，偏慢) |
| **已运行时间** | 2h53m |
| **预计剩余** | ~3h50m（日志显示 ETA 约 3:50-4:00） |
| **预计完成时间** | 约 **20:15** (北京时间) |

**进程状态**：
- PID 612753 (download_llama.py) — 存活，RSS 557MB
- PID 613202 (wait_and_run.sh) — 存活，等待下载完成后启动 NLP control 实验

**GPU**：两卡均空闲 (0% util, 0 MiB)，等待下载完成后启动训练。

shard1 正在临时目录 `._____temp/` 中下载（当前 4.0G），完成后会移到上级目录。速度约 400-450 KB/s，还需约 3.5-4 小时。

---
