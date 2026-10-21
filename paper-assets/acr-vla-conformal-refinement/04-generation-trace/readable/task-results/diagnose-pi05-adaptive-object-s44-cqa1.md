# diagnose pi05 adaptive object s44 cqa1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-adaptive-object-s44-cqa1_20260526T094050_result.json`
- **Structured JSON:** [`9195f34c83bd99fd471f.json`](../../sessions/91/9195f34c83bd99fd471f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验都在运行中，尚未产出 JSON。汇总如下：

---

```
exp_id: pi05-adaptive-object-s44-cqa1
tmux_session: 存在 (pi05-obj-s44, created 13:54)
process_status: 运行中
output_json: 不存在
当前进度: object 任务，正在跑 pick_up_the_chocolate_pudding rollout 5/20
  已完成任务样例: tomato_sauce 85%, butter 95%, milk 100%
```

```
exp_id: pi05-adaptive-long-s43-cqa1
tmux_session: 存在 (pi05-long-s43, created 13:55)
process_status: 运行中
output_json: 不存在
当前进度: long-horizon 任务，正在跑 LIVING_ROOM_SCENE5 rollout (已出 20/20, 90%)
  已完成任务样例: KITCHEN_SCENE3 95%, KITCHEN_SCENE4 95%
```

```
exp_id: pi05-adaptive-long-s44-cqa1
tmux_session: 存在 (pi05-long-s44, created 13:55)
process_status: 运行中
output_json: 不存在
当前进度: long-horizon 任务，正在跑 LIVING_ROOM_SCENE5 rollout 15/15
  已完成任务样例: KITCHEN_SCENE3 100%, KITCHEN_SCENE4 85%
```

---

**GPU 状态** — 6× RTX 4090D 全部在用：

| GPU | 显存占用 | GPU-Util | PID |
|-----|---------|----------|-----|
| 0 | 13110/24564 MiB | 32% | 216649 |
| 1 | 11720/24564 MiB | 47% | 219043 |
| 2 | 10759/24564 MiB | 34% | 219679 |
| 3 | 10319/24564 MiB | 22% | 197917 |
| 4 | 11860/24564 MiB | 49% | 198442 |
| 5 | 12711/24564 MiB | 21% | 199049 |

另外还有 3 个额外 tmux session 也在跑：`pi05-adaptive-goal-s42-cqa1`、`pi05-adaptive-object-s42-cqa1`、`pi05-crm-k2-long-s44-cqa1`。6 个 session 对应 6 张卡，全满载。

**结论**：三个实验重启成功，均在正常推进中，还未跑完。无空闲 GPU。

---
