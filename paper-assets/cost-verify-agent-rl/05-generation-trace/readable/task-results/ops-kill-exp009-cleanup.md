# ops kill exp009 cleanup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_exp009_cleanup_20260514T040827_result.json`
- **Structured JSON:** [`517849ea3e76110bf301.json`](../../sessions/51/517849ea3e76110bf301.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 结果

| 项目 | 状态 |
|------|------|
| **exp009 进程** | 全部清理（9 个进程 + 2 个孤儿 ray agent） |
| **exp010 进程** | 正常运行，PID 199399，step 2/30（7%），每步 ~481s |
| **GPU 占用** | 仅 exp010 的两个 ray::WorkerDict（PID 202873/202874），GPU 0: 48325 MiB, GPU 1: 48305 MiB，显存占用从 ~97GB 降到 ~48GB/卡 |
| **checkpoint 目录** | `/root/autodl-tmp/checkpoints/exp008_grpo/` 不存在，无残留 |
| **日志** | 无 error/traceback/OOM，训练正常推进中 |

exp010 训练指标：train success 4.7%, pass@8 37.5%, val success 0.0%，正在第 2 步。

---
