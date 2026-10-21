# ops kill llama8b download

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-llama8b-download_20260518T125512_result.json`
- **Structured JSON:** [`42762356c3483578d2e0.json`](../../sessions/42/42762356c3483578d2e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**1. LLaMA-8B 下载进程 PID 17783** — 已终止。第一次 `kill` 后进程变为僵尸态（0 内存），`kill -9` 时已不存在，确认已结束。

**2. Qwen3-14B 下载** — 进行中
- PID 29779 运行中，modelscope `snapshot_download`
- 已下载 **12G**
- 已落盘文件：`config.json`, `generation_config.json`, `merges.txt`, `LICENSE` 等配置文件 + `._____temp` 临时目录（权重文件还在下载中）

**3. 磁盘空间**
- `/root` 所在分区：30G 总量，已用 12G，剩余 **19G (38%)**
- Qwen3-14B 完整约 28G，当前分区空间不足。注意下载目标是 `/root/autodl-tmp/models/`，需确认 autodl-tmp 是否挂载在独立分区。

**4. exp-026 (folio_regen_v3)**
- PID 27245 运行中，`run_full_mvp.py --mode vllm` FOLIO 数据集实验
- 日志最后时间 **20:12:26**，持续产生 HTTP 200 请求，运行正常

---
