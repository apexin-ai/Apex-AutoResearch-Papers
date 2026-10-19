# Eval 进度检查 — 2026-05-14 02:17 UTC

## 各实验状态

| exp_id | server | GPU | PID alive? | tasks done/total | 当前成功率 | 最新 log 摘要 | 预计剩余时间 |
|--------|--------|-----|-----------|-----------------|-----------|--------------|-------------|
| eval-vla-mean-spatial | bjb2 | cuda:0 (4090D) | ✅ 143106, 15.1h | 7.5/10 | 28/70 = 40.0% | task 8 rollout 5/10, 0/5 | ~5h |
| eval-acr-spatial-v3 | bjb1 | cuda:0 (4090) | ✅ 197062, 6h | 4/10 | 1/40 = 2.5% | 完成 task 4, 正跑 task 5 | ~9h |
| eval-acr-object-v3 | bjb1 | cuda:3 (4090) | ✅ 197803, 6h | 4/10 | 0/40 = 0.0% | 完成 task 4, 正跑 task 5 | ~9h |
| eval-argmin-only-spatial | bjb1 | cuda:1 (4090) | ✅ 231426, 29min | 0/10 | — | task 1 运行中, 无 rollout 输出 | ~14h |
| eval-tiny-correction-spatial | bjb1 | cuda:2 (4090) | ✅ 232820, 28min | 0.5/10 | task1: 4/5 | task 1 rollout 5/10 | ~9h |

### 各 task 成功率明细

**eval-vla-mean-spatial** (vla_only, baseline_mode=mean, spatial):
| task | success |
|------|---------|
| bowl_between_plate_ramekin → plate | 7/10 (70%) |
| bowl_next_to_ramekin → plate | 10/10 (100%) |
| bowl_from_table_center → plate | 0/10 (0%) |
| bowl_on_cookie_box → plate | 3/10 (30%) |
| bowl_in_top_drawer → plate | 0/10 (0%) |
| bowl_on_ramekin → plate | 0/10 (0%) |
| bowl_next_to_cookie_box → plate | 8/10 (80%) |
| bowl_on_stove → plate | running (0/5 so far) |

**eval-acr-spatial-v3** (acr_vla, crm_v2/perdof, spatial):
| task | success |
|------|---------|
| bowl_between_plate_ramekin → plate | 1/10 (10%) |
| bowl_next_to_ramekin → plate | 0/10 (0%) |
| bowl_from_table_center → plate | 0/10 (0%) |
| bowl_on_cookie_box → plate | 0/10 (0%) |

**eval-acr-object-v3** (acr_vla, crm_v2/perdof, object):
| task | success |
|------|---------|
| alphabet_soup → basket | 0/10 (0%) |
| cream_cheese → basket | 0/10 (0%) |
| salad_dressing → basket | 0/10 (0%) |
| bbq_sauce → basket | 0/10 (0%) |

**eval-tiny-correction-spatial** (acr_vla, max_correction_norm=0.05, spatial):
- task 1 (bowl_between_plate_ramekin → plate): rollout 5/10, 4/5 success so far

## CRM v3 训练状态

| exp_id | PID alive? | 进度 | val_loss (best) | 状态 |
|--------|-----------|------|-----------------|------|
| crm-train-v3-perdof | ✅ 181668 | epoch 29/50 | 1.1975 | 训练中, 持续下降 |
| crm-train-v3-scalar-unc | ✅ 181896 | epoch 29/50 | 1.1989 | 训练中, 持续下降 |
| crm-train-v3-obs-only | ✅ 181973 | epoch 29/50 | 1.1997 | 训练中, 持续下降 |

三个 CRM v3 训练跑了约 12 分钟，epoch 29/50。每 epoch ~24s，预计再 ~8 分钟完成。全部在 bjb2 cuda:0 上，与 eval-vla-mean-spatial 共享。

## GPU 使用情况

**bjb2:**
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX 4090 D | 99% | 4011/24564 MiB |

**bjb1:**
| GPU | 型号 | 利用率 | 显存 | 运行实验 |
|-----|------|--------|------|---------|
| 0 | RTX 4090 | 18% | 21888/24564 MiB | eval-acr-spatial-v3 + 其他 |
| 1 | RTX 4090 | 99% | 2878/24564 MiB | eval-argmin-only-spatial |
| 2 | RTX 4090 | 98% | 2914/24564 MiB | eval-tiny-correction-spatial |
| 3 | RTX 4090 | 21% | 1459/24564 MiB | eval-acr-object-v3 |

## 异常与建议

### 🔴 acr-spatial-v3 和 acr-object-v3 成功率极低
- **acr-spatial-v3**: 4 个 task 仅 1/40 成功 (2.5%)，远低于 vla_only baseline (40%)
- **acr-object-v3**: 4 个 task 全部 0/40 (0.0%)
- CRM correction (v2/perdof) 不仅没提升，反而大幅降低了性能。这两个用的是 crm_v2 checkpoint，v3 正在训练中。

### 🟡 eval-vla-mean-spatial 运行时间长但正常
- 15h 完成 7.5/10 tasks，每 task ~2h。K=10 次 VLA forward pass/step + 单 GPU 共享 CRM 训练。
- 预计再 ~5h 完成（~07:00 UTC）。

### 🟡 bjb1 GPU 0 显存接近满载
- 21888/24564 MiB (89%)，但 GPU 利用率仅 18%。可能是 eval-acr-spatial-v3 加载了完整模型但 CPU-bound（环境渲染）。不紧急但需留意 OOM。

### 🟢 CRM v3 训练即将完成
- 三个变体 (perdof/scalar_unc/obs_only) 都在 epoch 29/50，约 8 分钟后完成。完成后可用新 checkpoint 重跑 eval。

### 💡 tiny-correction 初步结果积极
- task 1 的 5 个 rollout 中 4 个成功 (80%)，比 acr-spatial-v3 的 10% 好得多。max_correction_norm=0.05 的约束可能有效防止了 CRM 过度修正。
