# cleanup goal s47 stale running

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_goal-s47-stale-running_20260524T125531_result.json`
- **Structured JSON:** [`bafc8fb6774e1bb578ed.json`](../../sessions/ba/bafc8fb6774e1bb578ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报：bjb2-28827 清理已无需操作

### Registry 状态（已全部为 DONE，无需更新）

实际查询 registry 发现 5 个实验**早已**标为 DONE，状态与 JSON 文件一致：

| 实验 | 状态 | SR | successes/total |
|------|------|----|--------|
| eval-supp-goal-reconvla-s47 | DONE | 0.835 | 167/200 |
| eval-supp-goal-crm-norm005-s47 | DONE | 0.820 | 164/200 |
| eval-supp-goal-adapt-tau025-s47 | DONE | 0.820 | 164/200 |
| eval-supp-goal-k2mean-s47 | DONE | 0.825 | 165/200 |
| eval-supp-obj-reconvla-s47 | DONE | 0.765 | 153/200 |

JSON 实测值与 registry 记录、上轮 harvest 全部吻合。**没有 RUNNING 残留**，任务前提条件已不存在。

### GPU 占用

```
GPU 0: 1 MiB  (空闲)
GPU 1: 1 MiB  (空闲)
GPU 2: 1 MiB  (空闲)
GPU 3: 1 MiB  (空闲)
GPU 4: 1 MiB  (空闲)
GPU 5: 3024 MiB  (PID 205647 = eval-supp-long-k2mean-s47-r2)
```

cuda:0-4 已全部释放，仅 cuda:5 的 Long k2mean s47 r2 仍在运行（符合预期）。

### 备注
发现一个孤儿 tmux session `goal-adapt-s47`（PID 199611，仅 tmux 父进程未死，python 子进程已退出，未占 GPU）。未清理，因任务未要求且无影响。如需清理可执行 `tmux kill-session -t goal-adapt-s47`。

---
