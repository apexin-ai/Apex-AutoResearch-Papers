# check seed100 westd status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_seed100_westd_status_20260522T181843_result.json`
- **Structured JSON:** [`c9ea44a580b0534bf027.json`](../../sessions/c9/c9ea44a580b0534bf027.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### seed100 (PID 72007) — 存活，初始化中

- 进程运行 ~26 分钟，状态正常
- GPU 0,1 已分配显存 ~44.5 GB/卡，但 **计算利用率 0%** — 仍在初始化阶段
- 日志最后输出：TaskRunner 正在初始化 AlfredTWEnv（3553 train / 140 eval games），尚未开始训练 step
- **无 checkpoint**：`/root/autodl-tmp/checkpoints/exp029-seed100/` 不存在（符合预期，还没跑到保存点）

### seed200 (PID 999987) — 主进程已死，Ray worker 残留

- PID 999987 **不存在**
- 但其 Ray raylet (PID 64789) 和 GPU workers (PIDs 66567/66568) **仍在运行**，占用 GPU 2,3，利用率 100%，各 ~45 GB 显存
- 这是**孤儿进程**，需要手动清理（`ray stop` 或 kill 对应进程树）

### GPU 总览

| GPU | 利用率 | 显存占用 | 归属 |
|-----|--------|---------|------|
| 0 | 0% | 44.5/97.9 GB | seed100 (初始化中) |
| 1 | 0% | 44.5/97.9 GB | seed100 (初始化中) |
| 2 | 100% | 45.0/97.9 GB | seed200 孤儿 worker |
| 3 | 100% | 45.0/97.9 GB | seed200 孤儿 worker |

**建议**：清理 seed200 残留的 Ray 进程（PPID 64789 的整棵进程树），释放 GPU 2,3。seed100 本身正常，等它完成初始化即可开始训练。

---
