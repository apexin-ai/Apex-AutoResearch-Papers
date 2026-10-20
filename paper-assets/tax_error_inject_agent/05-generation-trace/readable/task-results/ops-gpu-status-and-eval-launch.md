# ops gpu status and eval launch

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-and-eval-launch_20260514T193101_result.json`
- **Structured JSON:** [`061ccd1dd972a6eff8dc.json`](../../sessions/06/061ccd1dd972a6eff8dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 张 GPU 满载确认完成。

## 最终状态

| GPU | 显存 | 利用率 | 任务 | Registry |
|-----|------|--------|------|----------|
| cuda:0 | 17091 MiB | 65% | vanilla recovery eval (injected_eval.py, seed=42) | `v4-vanilla-recovery-eval` RUNNING |
| cuda:1 | 17091 MiB | 78% | taxei-seed0 clean eval (47 tasks) | `v4-taxei-seed0-eval` RUNNING |
| cuda:2 | 17091 MiB | 84% | random-seed0 clean eval (47 tasks) | `v4-random-seed0-eval` RUNNING |
| cuda:3 | 17091 MiB | 90% | vanilla seed123 clean eval (47 tasks) | `v4-vanilla-seed123-eval` RUNNING |

**训练完成：**
- `v4-taxei-seed0`: loss=0.355, token_acc=0.917, 3387 steps, 1h50m → DONE
- `v4-random-seed0`: loss=0.355, token_acc=0.912, 3387 steps, 1h50m → DONE

cuda:1 和 cuda:2 的 eval 由之前部署的 wait-then-eval 脚本自动衔接启动，无空闲间隔。

---
