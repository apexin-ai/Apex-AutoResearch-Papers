# infra P0 kill cleanup restart random s0

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_P0-kill-cleanup-restart-random-s0_20260521T105415_result.json`
- **Structured JSON:** [`f2e404a58f2025d938d7.json`](../../sessions/f2/f2e404a58f2025d938d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

### 汇报

| 项目 | 状态 |
|------|------|
| safe_cleanup.sh | **已杀死** |
| 3 个训练进程 | **全部存活** (515223/517869/519025) |
| 磁盘清理 | 释放 ~30GB（删除 vanilla_s0/s1 各 15G + incomplete random_s0 chkpt 819M），当前 **169GB 可用 (33%)** |
| random_s0 重启 | **从头开始**（无可用 checkpoint），PID 521936, cuda:1，已开始训练 (step 7/50005, ~1.13s/it)，save_freq=10000 |
| 4 GPU 状态 | cuda:0 99% 62G, cuda:1 66% 63G, cuda:2 85% 63G, cuda:3 99% 62G — **4卡全部在跑** |
| vanilla_s2 | 保留（后续 50r eval） |
| protected_checkpoints.txt | safe_cleanup 已死，该文件不再被读取，无需更新 |

---
