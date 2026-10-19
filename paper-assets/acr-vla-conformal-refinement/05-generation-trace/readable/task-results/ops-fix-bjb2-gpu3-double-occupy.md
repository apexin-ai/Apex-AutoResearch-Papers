# ops fix bjb2 gpu3 double occupy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-bjb2-gpu3-double-occupy_20260515T172859_result.json`
- **Structured JSON:** [`67244d14a155e8eb2fcf.json`](../../sessions/67/67244d14a155e8eb2fcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 已更新 gpu=cuda:2, pid=115384（状态留在 DEPLOYED，状态机不允许直接回 RUNNING）。

**结果汇总：**

| GPU | 之前 | 之后 |
|-----|------|------|
| GPU 2 | PID 13737 僵尸进程 (1987 MiB) | PID 115384 eval-mag-perdof-norm03-object (3132 MiB，加载中) |
| GPU 3 | PID 107658 + PID 113552 双占 | 仅 PID 107658 (v4-default) |

- 僵尸进程已清除
- GPU 3 双占已解除
- eval-mag-perdof-norm03-object 已迁移到 GPU 2 运行

---
