# submit pipeline alpha4 0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_pipeline_alpha4_0_20260521T173102_result.json`
- **Structured JSON:** [`7d82ee57808756991256.json`](../../sessions/7d/7d82ee57808756991256.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动，正在运行 Step 1 (Pruning)。

**总结：**

| 项目 | 详情 |
|------|------|
| **exp_id** | `pipeline_alpha4_0` |
| **服务器/GPU** | westd-29022 cuda:2 |
| **PID** | 396205 |
| **tmux session** | `pipeline_alpha4_0` |
| **日志** | `~/runs/recovery_aware_struct_prune/pipeline_alpha4_0.log` |
| **Pipeline 阶段** | Prune(α=4.0, 20%) → SFT(2ep) → GRPO(100steps, DAPO) → GSM8K eval(N=1319) |
| **当前状态** | Step 1/4 Pruning 进行中，模型加载完成 |
| **预计总时长** | ~3.5-4.5h，timeout=6h |

脚本已修改：移除了 3 处 `CUDA_VISIBLE_DEVICES=$GPU` 赋值，由框架注入 `CUDA_VISIBLE_DEVICES=2`。

---
