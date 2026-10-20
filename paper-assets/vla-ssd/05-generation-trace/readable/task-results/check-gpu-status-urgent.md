# check gpu status urgent

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_status_urgent_20260522T071706_result.json`
- **Structured JSON:** [`2df0f21da843de8aa64c.json`](../../sessions/2d/2df0f21da843de8aa64c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### cuda:0 — openvla_spatial pipeline

| 项目 | 状态 |
|------|------|
| PID 594575 | **存活** (bash wrapper, 从 09:37 运行至今约 5.5h) |
| PID 594580 | **存活** (run_spatial_pipeline.sh) |
| GPU 占用 | **0MiB / 0%** — 当前无 GPU 进程 |
| 日志最新行 | `[15:17:14] Still waiting... (15G downloaded)` — 每 30s 重复，卡在等待模型下载完成（openvla-7b-finetuned-libero-spatial，已下 15G） |
| 结果目录 | `libero_spatial/` **不存在**，`libero_spatial_untrained/` **不存在** — 尚未产出结果 |

### cuda:1 — nlp_control (Llama-2 下载 + wait_and_run)

| 项目 | 状态 |
|------|------|
| PID 612748 | **存活** (download wrapper, 从 13:32 起) |
| PID 612753 | **存活** (python3 download_llama.py, 实际下载进程) |
| PID 613202/613207 | **存活** (wait_and_run.sh, 从 13:34 起等待下载完成) |
| 下载进度 | ModelScope → `/root/autodl-tmp/models/Llama-2-7b-chat-hf/`，速度 ~400kB/s |
| — shard 1/2 | **26%** (2.40G / 9.29G)，ETA ~4.5h |
| — shard 2/2 | **71%** (2.31G / 3.26G)，ETA ~40min |
| wait_and_run 日志 | 仍在等待：`Waiting for model download to complete...` |
| nlp_control run.log | 同上，尚未开始运行 |

### 磁盘

```
/root/autodl-tmp: 194G / 250G (78%)
```

### 总结

- **两张 GPU 均空闲**，无任何 GPU 进程。
- cuda:0 spatial pipeline 卡在等模型下载（HF spatial 模型 15G 已下载，可能在校验或解压阶段循环等待）。
- cuda:1 Llama-2 通过 ModelScope 下载中，速度极慢（~400KB/s），shard2 约 40min 完成，shard1 还需 ~4.5h。下载完成前 wait_and_run 不会启动 nlp_control 实验。

---
