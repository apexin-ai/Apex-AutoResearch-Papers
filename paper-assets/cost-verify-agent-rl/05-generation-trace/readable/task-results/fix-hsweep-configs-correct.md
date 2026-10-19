# fix hsweep configs correct

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_hsweep_configs_correct_20260517T010857_result.json`
- **Structured JSON:** [`bfe3f269d15bc026151e.json`](../../sessions/bf/bfe3f269d15bc026151e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果汇总

**源码确认的参数名：**
- `agent_proxy.context_window_mode` — 支持值：`"full"`, `"step_independent"`, `"single_turn"`, `"limited_multi_turn"`
- `agent_proxy.step_independent_history_length` — 整数，默认 5

**YAML 验证：** 5/5 OK

**关键参数对比表：**

| 文件 | context_window_mode | step_independent_history_length | total_training_steps | experiment_name |
|------|--------------------|----|----|----|
| `_alfworld_hsweep_h2.yaml` | step_independent | 2 | 15 | hsweep-h2 |
| `_alfworld_hsweep_h5.yaml` | step_independent | 5 | 15 | hsweep-h5 |
| `_alfworld_hsweep_h10.yaml` | step_independent | 10 | 15 | hsweep-h10 |
| `_alfworld_hsweep_h20.yaml` | step_independent | 20 | 15 | hsweep-h20 |
| `_alfworld_hsweep_full.yaml` | full | 2 | 15 | hsweep-full |

---
