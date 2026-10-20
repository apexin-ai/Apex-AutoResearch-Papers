# ops start final ar eval

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_start_final_ar_eval_20260523T002736_result.json`
- **Structured JSON:** [`6d7160ba06083d72b964.json`](../../sessions/6d/6d7160ba06083d72b964.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 不空闲，不启动新任务。**

`queue_runner` tmux session 仍在运行（并非已退出）。当前状态：

- **任务**: `[2/8] AR N=50 existing s42 checkpoints`
- **当前子任务**: pcgrad_s42 AR eval, conv 20/50 (beta=0), PID 54414, 已运行 21 分钟
- **GPU**: 56% util, 22336 MiB

queue_runner 还有 pcgrad 剩余 30 convs（beta=0）+ beta=3 和 beta=5 的 50 convs 各一轮，加上后续 conditions 和 items [3-8]，预计还需要较长时间。

**建议**：等 queue_runner 自然完成或确认其 items 列表是否已包含 d048_final_ar_eval 的内容（可能有重叠）。需要你确认：
1. 让 queue_runner 继续跑完？
2. 还是 kill 掉 queue_runner，改用 d048_final_ar_eval.sh？

---
