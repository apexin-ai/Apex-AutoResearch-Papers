# ops openvla pruning result check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_openvla_pruning_result_check_20260517T193654_result.json`
- **Structured JSON:** [`deee38e5a57c16b6e8cd.json`](../../sessions/de/deee38e5a57c16b6e8cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

**PID 697608 仍在运行**，正在执行 random prune k=0.5 eval：

```
python -u eval_openvla_libero.py --mode random_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 7
```

### Baseline 结果（已完成）
- **Overall SR: 74.0% (370/500)**
- 文件: `openvla_baseline_object.json`
- 耗时: 226.1 min

Per-task SR:
| Task | SR |
|---|---|
| alphabet soup | 78% |
| cream cheese | 80% |
| salad dressing | 82% |
| bbq sauce | 46% |
| ketchup | 96% |
| tomato sauce | 78% |
| butter | 58% |
| milk | 72% |
| chocolate pudding | 68% |
| orange juice | 82% |

### Random Prune k=0.5 状态
- **仍在运行**，刚开始 ~7 分钟
- Log 只到 Task 1/10, Ep 10/50 (task_sr=7/10)
- 按 baseline 耗时推算，预计还需 **~3.5 小时**（约 07:00-07:30 服务器时间完成）
- 输出可能被缓冲，最终结果会写入 `openvla_random_prune_k05_object.json`（目前尚未生成）

### 结论
pruning eval 未退出，进程正常运行中。需要等待约 3.5 小时才能拿到最终结果。

---
