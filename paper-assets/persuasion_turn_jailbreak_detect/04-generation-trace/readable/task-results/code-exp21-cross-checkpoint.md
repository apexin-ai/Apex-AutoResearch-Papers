# code exp21 cross checkpoint

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp21-cross-checkpoint_20260520T140155_result.json`
- **Structured JSON:** [`ef8fb1929b4b7b5cbf33.json`](../../sessions/ef/ef8fb1929b4b7b5cbf33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp21 完成。

**结果汇总：**

| DAPT Checkpoint | IID F1 | DD OOD F1 | AA OOD F1 |
|----------------|--------|-----------|-----------|
| seed42 | 1.000 | 0.900 | 0.926 |
| seed123 | 1.000 | 0.917 | 0.926 |
| seed456 | 1.000 | 0.962 | 0.953 |
| **mean±std** | **1.000±0.000** | **0.926±0.026** | **0.935±0.013** |

**结论：** IID 和 AA OOD 的跨 checkpoint 方差都在 2pp 以内（0pp 和 1.27pp）。DD OOD 方差 2.63pp 略超阈值，主要由 seed42 的 F1 偏低（0.900 vs 0.962）造成。总体来看，下游 OOD 性能对 Stage-1 DAPT 训练变异具有较好的稳定性。

**产出文件：**
- 脚本：`/root/persuasion_turn_jailbreak_detect/scripts/exp21_cross_checkpoint.py`
- 结果：`/root/persuasion_turn_jailbreak_detect/results/exp21_cross_checkpoint.json`

---
