# ops investigate starcoder s44 slow exit

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate-starcoder-s44-slow-exit_20260515T165448_result.json`
- **Structured JSON:** [`11409f3a742a86d7ad22.json`](../../sessions/11/11409f3a742a86d7ad22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结论

### 1. PID 913995 状态
- **存活**，进程状态 R (running)，113 线程
- GPU 1 利用率 100%，VRAM 55087/97887 MiB
- I/O 活跃（5 秒内有 50 次 syscall），非 hang

### 2. 核心发现：早停时间被误判
**Early stopping 在 ~13 分钟前触发（00:45 CST），不是 8 小时前。** 8h29m 是进程总运行时间（含训练 1500 步 + 3 次中间 eval）。

时间线：
- 16:28 — random_s44 训练开始
- 19:15 — eval@500, 保存 best_by_val_loss (val_loss=0.5913)
- 00:45 — eval@1500, early stop 触发, 保存 best_by_recall_at_1 (R@1=0.4871)
- 00:45~now — **final eval 正在运行**（代码 `evaluate()` 在 3024 样本上跑前向推理）

### 3. 进程正常，无需干预
Final eval 完成后（预计 15-30 分钟内），代码会自动保存 `final/` checkpoint 并退出。主链脚本随后自动启动 **bm25_s42**（第 3/9 个 subrun）。

### 4. random_s44 结果
| 指标 | 值 | Step |
|------|-----|------|
| Best val_loss | 0.5913 | 500 |
| Best R@1 | 0.4871 | 1500 |
| Early stop | step 1500 | patience 2/2 |

Registry 已更新。

---
