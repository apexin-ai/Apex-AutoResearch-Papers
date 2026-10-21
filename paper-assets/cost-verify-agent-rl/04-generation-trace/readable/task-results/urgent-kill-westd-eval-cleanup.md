# urgent kill westd eval cleanup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_kill_westd_eval_cleanup_20260521T121502_result.json`
- **Structured JSON:** [`96b2b7d149fd89406999.json`](../../sessions/96/96b2b7d149fd89406999.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 结果汇总

| 项目 | 状态 |
|------|------|
| **eval 进程 kill** | 已杀（PID 195885 + 相关子进程） |
| **GPU 0/1 内存** | 已释放：0 MiB / 0 MiB |
| **GPU 2/3 内存** | 96007 MiB — 这是 Seed 6 训练占用，正常 |
| **Seed 6 训练** | 正常运行（主进程 920749 + Worker 927990, 927997） |
| **临时文件清理** | /tmp 从 25MB → 16MB（清理了旧日志、wandb 临时目录、b64 分片、图表文件等） |
| **磁盘** | 根分区 14G/30G (46%)，数据盘 148G/250G (60%) |

注意：/tmp 实际只有 25MB 而非 27GB，磁盘占用大头不在 /tmp。如需进一步清理磁盘空间，需要排查数据盘上的 checkpoint 或模型缓存。

---
