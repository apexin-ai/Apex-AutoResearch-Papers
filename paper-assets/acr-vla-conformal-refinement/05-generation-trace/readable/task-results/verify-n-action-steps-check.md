# verify n action steps check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_n-action-steps-check_20260523T041258_result.json`
- **Structured JSON:** [`52a3cbcdca99cab5979b.json`](../../sessions/52/52a3cbcdca99cab5979b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### n_action_steps 验证结果

**两台服务器均未发现任何 evaluate.py 进程使用 `--n_action_steps` 参数，全部使用默认值 10。** ✅

---

### BJB1-32546

#### evaluate.py 进程（5 个）

| PID | GPU | Session | 命令 |
|-----|-----|---------|------|
| 664412 | 0 | eval-supp-crm-norm02-spatial-s42-r2 | `evaluate.py --mode crm_obs_only --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2` |
| — | 1 | eval-supp-adapt-tau015-spatial-s42-r2 | `evaluate.py --mode adaptive_conformal --benchmark spatial --seed 42 --n_rollouts 20 --tau 0.15`（截断区） |
| — | 2 | eval-supp-adapt-tau025-spatial-s42-r2 | `evaluate.py --mode adaptive_conformal --benchmark spatial --seed 42 --n_rollouts 20 --tau 0.25`（截断区） |
| — | 4 | eval-supp-adapt-tau035-spatial-s42-r2 | `evaluate.py --mode adaptive_conformal --benchmark spatial --seed 42 --n_rollouts 20 --tau 0.35`（截断区） |
| 669429 | 5 | eval-supp-obj-crm005-s42-r2 | `evaluate.py --mode crm_obs_only --benchmark object --seed 42 --n_rollouts 20 --max_correction_norm 0.05` |

#### train_crm.py 进程（1 个）

| PID | GPU | Session | 命令 |
|-----|-----|---------|------|
| 668382 | 3 | train-crm-unified-4suite-r6 | `train_crm.py --benchmark object spatial goal long --obs_dim 960 --epochs 50 --batch_size 32 --lr 1e-3 --input_mode obs_only --resume_from checkpoint_epoch0038.pt` |

#### GPU 占用

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 6306/24564 MiB | 39% | 占用（eval crm_obs_only spatial） |
| 1 | 6212/24564 MiB | 18% | 占用（eval adaptive tau015） |
| 2 | 6212/24564 MiB | 12% | 占用（eval adaptive tau025） |
| 3 | 544/24564 MiB | 10% | 占用（train_crm，显存较低） |
| 4 | 6212/24564 MiB | 12% | 占用（eval adaptive tau035） |
| 5 | 5731/24564 MiB | 29% | 占用（eval crm_obs_only object） |

#### tmux sessions（6 个）
- eval-supp-crm-norm02-spatial-s42-r2
- eval-supp-adapt-tau015-spatial-s42-r2
- eval-supp-adapt-tau025-spatial-s42-r2
- eval-supp-adapt-tau035-spatial-s42-r2
- eval-supp-obj-crm005-s42-r2
- train-crm-unified-4suite-r6

---

### BJB2-28827

#### evaluate.py 进程（6 个）

| PID | GPU | Session | 命令 |
|-----|-----|---------|------|
| 519759 | 3 | eval-object-vla-only-wrapper-s42-r2 | `evaluate.py --mode vla_only --benchmark object --seed 42 --n_rollouts 20` |
| — | 4 | eval-object-vla-only-wrapper-s43-r2 | `evaluate.py --mode vla_only --benchmark object --seed 43 --n_rollouts 20` |
| — | 5 | eval-object-vla-only-wrapper-s44-r2 | `evaluate.py --mode vla_only --benchmark object --seed 44 --n_rollouts 20`（截断区） |
| — | 0/1 | eval-supp-obj-adapt-s42-r2 | `evaluate.py --mode adaptive_conformal --benchmark object --seed 42 --n_rollouts 20`（截断区） |
| 523250 | 1 | eval-supp-obj-reconvla-s42 | `evaluate.py --mode reconvla --crm_checkpoint crm_best.pt --benchmark object --seed 42 --n_rollouts 20` |
| 524332 | 2 | eval-supp-goal-crm005-s42 | `evaluate.py --mode crm_obs_only --crm_checkpoint crm_best.pt --benchmark goal --seed 42 --n_rollouts 20 --max_correction_norm 0.05` |

#### train_crm.py：**无进程**

#### GPU 占用

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 5636/24564 MiB | 19% | 占用 |
| 1 | 5692/24564 MiB | 30% | 占用 |
| 2 | 5608/24564 MiB | 25% | 占用 |
| 3 | 5630/24564 MiB | 18% | 占用 |
| 4 | 5630/24564 MiB | 17% | 占用 |
| 5 | 5630/24564 MiB | 18% | 占用 |

#### tmux sessions（6 个）
- eval-object-vla-only-wrapper-s42-r2
- eval-object-vla-only-wrapper-s43-r2
- eval-object-vla-only-wrapper-s44-r2
- eval-supp-obj-adapt-s42-r2
- eval-supp-obj-reconvla-s42
- eval-supp-goal-crm005-s42

---

### 总结

- **n_action_steps**: ✅ 两台服务器 11 个 evaluate.py 进程均未指定 `--n_action_steps`，全部使用默认值 10
- **BJB1**: 6 GPU 全占用（5 eval + 1 train），GPU 3 上 train_crm 显存仅 544 MiB，可能刚启动或模型较小
- **BJB2**: 6 GPU 全占用（6 eval），无训练进程
- 部分中间进程的 GPU 分配因输出截断无法100%确认，但 n_action_steps 检查覆盖了所有进程（grep 全量扫描），结论可靠

---
