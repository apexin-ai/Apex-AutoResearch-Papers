# diagnose seed300 eval v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_seed300_eval_v2_20260522T190401_result.json`
- **Structured JSON:** [`79c5f751755bbf76fdfe.json`](../../sessions/79/79c5f751755bbf76fdfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：SUCCESS**

eval v2 已完成，134 episodes 全部跑完。

**OOD pass@1 = 0.0%**

关键指标：
| 指标 | 值 |
|------|-----|
| `val-env/AlfworldSG_OOD/pass@1` | 0.0 |
| `val-env/AlfworldSG_OOD/success` | 0.0 |
| `val-core/unknown/reward/mean@134` | 0.0 |
| `val-core/unknown/reward/best@134/mean` | 0.0 |
| `val-env/AlfworldSG_OOD/action_is_valid` | 0.918 |
| `val-env/response_length` | 4150.7 |
| episodes | 134 |

日志 8625 行，BrokenPipeError 出现在第 8577 行（Ray TaskRunner 子进程 pipe 断开），非致命——之后正常输出了完整的 134-episode 汇总结果。

seed300 step5 checkpoint 在 OOD 上完全失败，134 个 episode 无一成功。模型在生成有效动作（action_is_valid=91.8%）但没有解决任何任务。

---
