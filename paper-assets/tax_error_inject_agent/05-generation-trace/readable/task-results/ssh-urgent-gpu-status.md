# ssh urgent gpu status

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-gpu-status_20260514T131827_result.json`
- **Structured JSON:** [`b5bc268ca2eaa4f2e805.json`](../../sessions/b5/b5bc268ca2eaa4f2e805.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态
| GPU | 状态 | 显存占用 | 温度 |
|-----|------|----------|------|
| cuda:0 | **空闲** | 0MiB / 32607MiB | 28°C |
| cuda:1 | **空闲** | 0MiB / 32607MiB | 28°C |
| cuda:2 | **空闲** | 0MiB / 32607MiB | 28°C |
| cuda:3 | **空闲** | 0MiB / 32607MiB | 27°C |

无 GPU 进程运行。PID 51848（v3-vanilla eval）和 PID 50537（v4-vanilla 训练）均已退出。

## 训练/Eval 完成状态

| 任务 | 状态 | Checkpoints | 耗时 | 最终 loss |
|------|------|-------------|------|-----------|
| v3-vanilla 训练 | **完成** | checkpoint-1566 | — | — |
| v3-taxei 训练 | **完成** | 944 / 1888 / 2832 | 1h34m | 0.374 |
| v3-random 训练 | **完成** | 1135 / 2270 / 3405 | 1h50m | 0.350 |
| v4-vanilla 训练 | **完成** | 545 / 1090 / 1635 | 59m | 0.417 |
| v3-vanilla eval | **完成** | — | — | — |

### v3-vanilla eval 结果
- **success_rate = 74.5%**（35/47 episodes）
- 按任务类型：

| task_type | success/total | rate |
|-----------|--------------|------|
| look_at_obj_in_light | 4/6 | 66.7% |
| pick_and_place_simple | 6/8 | 75.0% |
| pick_clean_then_place | 8/11 | 72.7% |
| pick_cool_then_place | 5/7 | 71.4% |
| pick_heat_then_place | 7/8 | **87.5%** |
| pick_two_obj_and_place | 5/7 | 71.4% |

## 空闲 GPU
**cuda:0, cuda:1, cuda:2, cuda:3 — 全部空闲**，可立即调度新任务。

---
