# audit bjb1 32546 gpu status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bjb1-32546-gpu-status_20260520T143149_result.json`
- **Structured JSON:** [`7cf65c0c145667b4fc83.json`](../../sessions/7c/7cf65c0c145667b4fc83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-32546 GPU 审计报告

| GPU | PID | 显存 | 利用率 | 实验 | 进度 | 推荐 |
|-----|-----|------|--------|------|------|------|
| **0** | 423286 | 1989 MiB | 15% | `crm_obs_only` / object / seed50 / K10 / norm0.2 → `eval_obs_only_object_norm02_seed50.json` | **8/10 tasks** | **continue** |
| **1** | 444147 | 2780 MiB | 19% | `vla_only` / goal / seed51 / K1 → `eval_vla_only_goal_seed51.json` | **6/10 tasks** | **continue** |
| **2** | 450388 | 4781 MiB | 32% | `crm_perdof` / object / seed49 / K10 / norm0.2 → `eval_perdof_object_norm02_seed49.json` | **3/10 tasks** | **continue** |
| **3** | 423622 | 2420 MiB | 19% | `reconvla` / object / seed50 / K10 → `eval_argmin_object_seed50.json` | **7/10 tasks** | **continue** |
| **4** | 423899 | 2358 MiB | 7% | `vla_only` / object / seed48 / K1 → `eval_vla_only_object_seed48.json` | **7/10 tasks** (r2) | **continue** |
| **5** | — | 2 MiB | 0% | **空闲** | — | **deploy** |

### 补充说明

- tmux session `eval-crm-long-seed51` (CUDA_VISIBLE_DEVICES=1) 的 python 进程已完成，输出文件 `eval_long_obs_only_norm02_seed51.json` 已生成 (15:10)。GPU 1 之后被 vla_only goal seed51 占用。
- GPU 0/3/4 预计 1-2 小时内完成（剩余 2-3 tasks）。
- GPU 2 (perdof) 只完成 3/10，预计还需 3-4 小时。
- GPU 1 (goal) 完成 6/10，预计 2 小时内完成。
- **GPU 5 空闲可立即部署新实验。**

---
