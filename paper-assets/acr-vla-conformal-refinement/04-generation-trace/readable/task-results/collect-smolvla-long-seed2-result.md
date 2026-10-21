# collect smolvla long seed2 result

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_smolvla-long-seed2-result_20260522T153905_result.json`
- **Structured JSON:** [`ddee8d06de64b7364f46.json`](../../sessions/dd/ddee8d06de64b7364f46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清楚了。原始 eval 进程已被 kill，但有新的 lerobot eval 正在运行。

## 结论

### seed2 (及 seed0/seed1) vla_only eval — **失败，被 kill**

三个 seed 都在完成第 2 个 task 后、第 3 个 task (KITCHEN_SCENE3) rollout 5/10 处中断。无 JSON 输出文件。日志无错误信息，推测被手动 kill 或 OOM killer。

已完成的 per-task SR（vla_only, 不完整）:

| Task | seed0 | seed1 | seed2 |
|------|-------|-------|-------|
| put_alphabet_soup_and_tomato_sauce | 0% (0/10) | 10% (1/10) | 10% (1/10) |
| put_cream_cheese_and_butter | 80% (8/10) | 90% (9/10) | 70% (7/10) |
| turn_on_stove_moka_pot | 5/5 进行中 | 5/5 进行中 | 5/5 进行中 |
| Task 4-10 | 未执行 | 未执行 | 未执行 |

### seed0/seed1/seed2 lerobot eval — 也被 kill

seed2 lerobot 日志显示跑到 batch 18/20 (90%), running SR=55.6% 时中断。

### 当前运行中的进程

GPU 0-2 上有**新的 lerobot eval** 进程（PID 249181/249256/249393），已跑 ~36 分钟，使用 `lerobot.scripts.lerobot_eval`，参数 `libero_10`, `n_episodes=20`:
- seed=0 (GPU 0)
- seed=1 (GPU 1)  
- seed=2 (GPU 2)

GPU 3-5 上有 **CRM precompute** 进程（pi05/goal/K=10），已跑 ~7.5 小时。

---
