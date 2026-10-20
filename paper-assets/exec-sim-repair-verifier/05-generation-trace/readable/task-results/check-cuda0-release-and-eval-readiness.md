# check cuda0 release and eval readiness

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cuda0-release-and-eval-readiness_20260515T140904_result.json`
- **Structured JSON:** [`bbed4610deecb923eb37.json`](../../sessions/bb/bbed4610deecb923eb37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### cuda:0 状态
已释放。PID 377100 已 kill，显存 0 MiB / 32607 MiB，完全空闲。

### 可用 Checkpoints

| Checkpoint | 路径 | 状态 |
|---|---|---|
| seed123 8B ckpt-3000 | `checkpoints_backup_cls_8b_seed123/checkpoint-3000/` | 完整（adapter 61MB） |
| s42 8B ckpt-200 (conda) | `checkpoints_repo_cls_8b_conda/checkpoint-200/` | 完整（含 eval_test_full 子目录） |
| **s42 resume 系列** | `checkpoints_repo_cls_8b_s42_resume/` | **23 个 ckpt: 800-5200（步长200）** |

### 已有 Eval 结果

**已完成（不需重跑）：**
- seed123 ckpt-3000 test → `cls8b_seed123_ckpt3000_test8192`
- s42 val sweep (200-1600) → `cls8b_ckpt{200,400,600}_val` 等
- s42 test sweep (400-1600) → `cls8b_s42_ckpt{800,1000,1200,1400,1600}_test8192`
- seed123 val 额外点: ckpt-6200, 6400, 6600, 6633

### 建议优先 Eval

s42 resume 系列有 **ckpt 1800-5200 未做 test eval**（共 18 个点）。如果目标是补全 s42 test learning curve，建议先跑这些点，从 ckpt-1800 开始往后推进。如果只需关键点，可以先跑 2000, 3000, 4000, 5000 四个代表性节点。

---
