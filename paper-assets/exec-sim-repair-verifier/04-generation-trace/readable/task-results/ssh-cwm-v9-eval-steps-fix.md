# ssh cwm v9 eval steps fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cwm-v9-eval-steps-fix_20260512T223907_result.json`
- **Structured JSON:** [`bec91dd20176056c8b3d.json`](../../sessions/be/bec91dd20176056c8b3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中。

## 汇报

| 项目 | 值 |
|------|-----|
| 旧 PID | 95806（已 kill） |
| 新 PID (bash wrapper) | 100512 |
| 新 PID (python) | **100517** |
| GPU | cuda:2, 21067 MiB, 89% 利用率 |
| Resume checkpoint | checkpoint-200 |
| 当前 step | 206/6633 |
| 训练速度 | ~8s/step |
| eval_steps | **500**（已生效） |
| save_steps | **500**（也改了 — 见下） |

### 变更说明

1. **脚本修改**：`train_repo_cwm.py` 新增 `--eval_steps` CLI 参数（默认为 None，回退到 save_steps）
2. **save_steps 也改为 500**：原计划只改 eval_steps=500 保留 save_steps=100，但 Transformers 的 `load_best_model_at_end=True` 要求 save_steps 是 eval_steps 的倍数。100 不是 500 的倍数，第一次尝试直接报 ValueError 崩溃。因此 save_steps 也调为 500
3. **checkpoint-100 和 checkpoint-200 均存在**：位于 `/root/autodl-tmp/checkpoints_repo_cwm_v9/`

### 注意
- 进程用 `CUDA_VISIBLE_DEVICES=2` 启动（脚本默认 device 是 cuda:3，但原进程实际运行在 GPU 2，保持一致）
- 原进程在 step ~202 被 kill（eval@step 200 已完成）
- 有 warning 说 eval_steps/save_steps 与 checkpoint 的 trainer_state.json 不匹配，属正常行为

---
