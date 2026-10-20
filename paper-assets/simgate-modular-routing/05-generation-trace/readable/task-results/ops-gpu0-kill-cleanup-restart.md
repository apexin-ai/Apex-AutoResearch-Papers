# ops gpu0 kill cleanup restart

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu0-kill-cleanup-restart_20260514T041542_result.json`
- **Structured JSON:** [`16045d81f9c4410a24e7.json`](../../sessions/16/16045d81f9c4410a24e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| Step | 结果 |
|------|------|
| **Step 1: Kill GPU0** | 原 PID 698985/699929 已不存在；实际运行的 PID 934571/935125 已 kill，GPU0 释放 |
| **Step 2: 删除 150G 文件** | `results/plan_c/lifespan-longest-lived/` 整个目录已删除。df 未变化是因为 md0 是多容器共享设备；autodl-tmp 实际使用 19G |
| **Step 3: 重启** | 通过 `submit_training_job` 提交 tmux session `gpu0-v6-lifespan`，运行 `SLIM_EPISODES=1` + `--start_episode 0` + `--episodes 20` |
| **Step 4: 验证** | GPU0 利用率 100%，vLLM PID 37837 已加载，推理正在进行（~1000 toks/s input, ~96 toks/s output），ep0 数据收集已开始 |

GPU1 进程（PID 789051, freeze/chemistry-mix）未受影响。

---
