# ops llama70b disk fix and restart

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama70b_disk_fix_and_restart_20260523T105911_result.json`
- **Structured JSON:** [`23ee239ef93149850ee1.json`](../../sessions/23/23ee239ef93149850ee1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载已正常启动，多个分片并行下载中。

---

## 产出汇报

| 项目 | 详情 |
|------|------|
| **清理前磁盘** | 350G 总 / 314G 用 / **37G 可用 (90%)** |
| **清理后磁盘** | 350G 总 / 127G 用 / **224G 可用 (37%)** |
| **释放空间** | **187G** |
| **删除路径 1** | `LLM-Research/Meta-Llama-3___1-70B-Instruct/original/` — 17G（1个 .pth 文件） |
| **删除路径 2** | `Qwen/` — 171G（含 `Qwen2.5-72B-Instruct` + `Qwen2___5-72B-Instruct` 两个副本） |
| **新下载 PID** | **318630**（Python 子进程 318664） |
| **下载速度** | ~1.5 MB/s，多分片并行 |
| **待下载量** | 29 个分片 × ~4.5G ≈ **~126G safetensors** |
| **预计完成时间** | 以当前 ~1.5 MB/s × 多线程（实测 ~5 MB/s 总速）：约 **7-8 小时** |

额外处理：清除了上次 kill 后残留的 ModelScope 锁文件，否则新下载会一直阻塞。

---
