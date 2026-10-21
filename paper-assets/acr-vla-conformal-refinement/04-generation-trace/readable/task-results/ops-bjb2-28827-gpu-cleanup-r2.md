# ops bjb2 28827 gpu cleanup r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb2-28827-gpu-cleanup-r2_20260515T192243_result.json`
- **Structured JSON:** [`693d5dc06507861d64ce.json`](../../sessions/69/693d5dc06507861d64ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。bjb2-28827 GPU 状态：

| GPU | PID | 实验 | 状态 |
|-----|-----|------|------|
| cuda:0 | 105947 | perdof norm=0.03 object | 保留 |
| cuda:1 | 109655 | perdof norm=0.05 object | 保留 |
| cuda:2 | 140759 | **perdof norm=0.3 object r3** (新部署) | 5645MiB, 19% |
| cuda:3 | 141024 | **obs_only norm=0.2 object** (新部署) | 5645MiB, 18% |
| cuda:4 | 101616 | obs_only norm=0.05 object | 保留 |
| cuda:5 | 103034 | obs_only norm=0.3 object | 保留 |

**执行摘要：**
- 杀掉 3 个进程：PID 127581 (perdof norm=0.3 r2), 138867 (perdof norm=0.2 seed=43), 130113 (spatial obs_only norm=0.3)
- Registry 标记 killed：`eval-mag-perdof-norm03-object-r2`, `eval-mag-perdof-norm02-seed43-object`, `eval-mag-obsonly-norm03-b3`, `eval-mag-obsonly-norm03-b4`
- 新部署：`eval-mag-perdof-norm03-object-r3` (cuda:2), `eval-mag-obsonly-norm02-object` (cuda:3)
- 6 块 GPU 各一个进程，利用率正常，无资源竞争

---
