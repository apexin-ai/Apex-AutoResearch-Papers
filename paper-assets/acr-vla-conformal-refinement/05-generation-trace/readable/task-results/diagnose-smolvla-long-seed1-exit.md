# diagnose smolvla long seed1 exit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_smolvla-long-seed1-exit_20260522T153740_result.json`
- **Structured JSON:** [`23cf57bb4b174572345a.json`](../../sessions/23/23cf57bb4b174572345a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论清晰了。

## 结论

### seed1 (PID 232884): 异常退出

**原始 eval-vla-only 进程全部异常退出**（seed0/1/2 三个都死了，不只是 seed1）：
- 三个 PID（232609/232884/233564）均已不存在
- 各 seed 只跑完了 **2/10 tasks**，日志截断在 task 3 进行中
- **无结果 JSON 文件**生成
- 日志中**无 error/exception/traceback**
- 三个进程几乎同时死亡（seed1 最后写入 22:59，seed0/seed2 约 23:01）
- 无法确认 OOM（dmesg 无权限，journalctl 无记录），但同时死亡 + 无错误日志 + 无 swap 的容器环境高度怀疑 **cgroup OOM kill**

已完成的部分结果（seed1）：
| Task | SR |
|------|-----|
| put_alphabet_soup_and_tomato_sauce_in_basket | 10% (1/10) |
| put_cream_cheese_box_and_butter_in_basket | 90% (9/10) |

### 已有替代进程在运行

原始 eval-vla-only tmux session 已不存在，但在 **23:05** 已有人启动了新的 `eval-lerobot-long-seed{0,1,2}` tmux sessions，使用的是 **lerobot.scripts.lerobot_eval**（不是原来的自定义 evaluate.py），跑的是 `libero_10`，已运行 ~34 分钟，GPU 0-2 各占 1.8GB。

### seed0 / seed2 状态
与 seed1 一样——**都异常退出了**，同样只完成 2/10 tasks，无结果文件。新的 lerobot_eval 替代进程正在运行中。

---
