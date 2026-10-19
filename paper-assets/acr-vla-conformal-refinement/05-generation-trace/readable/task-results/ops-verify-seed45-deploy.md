# ops verify seed45 deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-seed45-deploy_20260516T111658_result.json`
- **Structured JSON:** [`a4de90f539335e241d50.json`](../../sessions/a4/a4de90f539335e241d50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 新实验（2个）— 全部健康

| 实验 | PID | GPU | 状态 | Log 摘要 |
|------|-----|-----|------|----------|
| eval-vla-mean-object-seed45 | 248652 | cuda:2 (5609MiB) | **ALIVE** | 模型加载完成，10 tasks loaded，正在 rollout |
| eval-obs-only-object-norm03-seed45 | 248860 | cuda:3 (5645MiB) | **ALIVE** | CRM loaded (327,198 params)，norm=0.3，10 tasks loaded，正在 rollout |

两个新实验均已通过模型加载阶段，没有 EXIT_CODE=127 或其他报错。

### 旧实验（4个）— 全部存活

| 实验 | PID | GPU | 状态 |
|------|-----|-----|------|
| eval-scalar-object-seed45 | 224623 | cuda:0 (5645MiB) | **ALIVE** |
| eval-perdof-object-norm02-seed45 | 222824 | cuda:1 (5645MiB) | **ALIVE** |
| eval-vla-only-object-seed45 | 221407 | cuda:4 (2820MiB) | **ALIVE** |
| eval-argmin-object-seed45 | 215932 | cuda:5 (4681MiB) | **ALIVE**，正在评估 cream_cheese task (rollout 10/10) |

### 注意事项

GPU 2 和 GPU 3 上各有一个**额外 python 进程**占用显存：

- **GPU 2**: PID 246301 (5422MiB) — 是一个旧的 `crm_obs_only --max_correction_norm 0.3` 实验，**输出文件与新实验相同** (`eval_object_obs_only_norm03_seed45.json`)，可能是上一次失败残留
- **GPU 3**: PID 242264 (5645MiB) — 一个 `crm_obs_only` 实验（无 norm 约束，输出到 `eval_object_obs_only_default_seed45.json`）

PID 246301 与新的 eval-obs-only-object-norm03-seed45 写同一个输出文件，可能产生冲突。建议 kill 掉 246301。

---
