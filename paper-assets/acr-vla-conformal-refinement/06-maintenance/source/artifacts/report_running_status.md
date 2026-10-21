# 实验运行状态报告
> 检查时间: 2026-05-15 05:28 UTC

---

## bjb1-18228 (4× RTX 4090)

### GPU 状态
| GPU | 显存占用 | 利用率 | 运行的实验 |
|-----|---------|--------|-----------|
| 0 | 17441/24564 MiB | 70% | eval-acr-spatial-v4-default + crm-train-v3-norm-obs-only |
| 1 | 1423/24564 MiB | 20% | eval-argmin-only-spatial |
| 2 | 1459/24564 MiB | 21% | eval-tiny-correction-spatial |
| 3 | 2022/24564 MiB | 70% | eval-acr-spatial-v4-small + crm-train-v3-norm-scalar-unc |

### 实验详情

#### 1. eval-acr-spatial-v4-default — ALIVE
- **PID**: 252489（python 进程），父进程 252483（tmux bash wrapper）
- **GPU**: cuda:0, 6221 MiB
- **运行时间**: ~57 分钟
- **命令**: `python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint .../crm_v3_norm/perdof/crm_best.pt`（无 max_correction_norm，使用默认值）
- **进度**: 无日志文件（stdout 输出到 tmux pipe），无法读取进度

#### 2. eval-acr-spatial-v4-small — ALIVE
- **PID**: 253085
- **GPU**: cuda:3, 1450 MiB
- **运行时间**: ~56 分钟
- **进度**: task 1/10 已完成
  - Task 1 (pick_up_bowl_between_plate_and_ramekin): 60.0% (6/10)
- **参数**: `--max_correction_norm 0.1`, CRM: crm_v3_norm/perdof/crm_best.pt

#### 3. eval-argmin-only-spatial — ALIVE
- **PID**: 231421 (bash) → 231426 (python)
- **GPU**: cuda:1, 1414 MiB
- **运行时间**: 3h38m
- **进度**: task 4/10 进行中
  - Task 1: 60.0% (6/10) | Task 2: 100.0% (10/10) | Task 3: 0.0% (0/10)
  - Task 4: rollout 5/10, 暂 1/5
- **模式**: reconvla（argmin baseline）

#### 4. eval-tiny-correction-spatial — ALIVE
- **PID**: 232815 (bash) → 232820 (python)
- **GPU**: cuda:2, 1450 MiB
- **运行时间**: 3h37m
- **进度**: task 4/10 进行中
  - Task 1: 70.0% (7/10) | Task 2: 90.0% (9/10) | Task 3: 0.0% (0/10)
  - Task 4: rollout 5/10, 暂 1/5
- **参数**: `--max_correction_norm 0.05`, CRM: crm_v2/perdof/crm_best.pt

#### 5. crm-train-v3-norm-obs-only — ALIVE
- **PID**: 256771 (bash) → 256776 (python)
- **GPU**: cuda:0, 558 MiB
- **运行时间**: ~36 分钟
- **进度**: epoch 24/50
  - Best val_loss: 0.016689 (epoch 23)
  - train_loss: ~0.0265, val_loss: ~0.0167, lr: 8.50e-03

#### 6. crm-train-v3-norm-scalar-unc — ALIVE
- **PID**: 257086 (bash) → 257091 (python)
- **GPU**: cuda:3, 558 MiB
- **运行时间**: ~36 分钟
- **进度**: epoch 24/50
  - Best val_loss: 0.040552 (epoch 24, 仍在下降)
  - train_loss: ~0.0592, val_loss: ~0.0406, lr: 8.50e-03

---

## bjb2-40593 (1× RTX 4090D)

### GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 1933/24564 MiB | 11% |

#### 7. eval-vla-mean-spatial — ALIVE
- **PID**: 143106 (bash) → 143112 (python)
- **GPU**: cuda:0, 1914 MiB
- **运行时间**: 18h16m
- **进度**: task 9/10 进行中
  - Task 1: 70% | Task 2: 100% | Task 3: 0% | Task 4: 30% | Task 5: 0% | Task 6: 0% | Task 7: 80% | Task 8: 0%
  - Task 9: rollout 5/10, 暂 1/5
- **预计**: ~2h 完成

---

## 异常与备注

1. **eval-acr-spatial-v4-default 无日志文件** — stdout 通过 pipe 输出到 tmux，无法用 ssh_read_only 读取。建议后续重定向输出到文件。
2. **GPU 0 显存偏高** — nvidia-smi 报 17.4 GB，进程合计仅 ~6.8 GB。可能是 PyTorch CUDA 预分配/框架缓存。
3. **GPU 1/2 利用率仅 20%** — MuJoCo 仿真 CPU-bound，GPU 仅在 VLA 推理时短暂使用，正常。
4. **所有 7 个实验均存活，无 OOM、无崩溃。**
5. **CRM 训练** — obs_only val_loss (0.017) 显著低于 scalar_unc (0.041)，两者均在稳定下降中。
