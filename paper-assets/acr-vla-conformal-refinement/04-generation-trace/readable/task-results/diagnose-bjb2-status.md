# diagnose bjb2 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb2-status_20260514T181415_result.json`
- **Structured JSON:** [`00ac6ebf248662eaa025.json`](../../sessions/00/00ac6ebf248662eaa025.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 进程存活状态
| 任务 | PID | 状态 | 运行时间 | GPU 显存 |
|------|-----|------|----------|----------|
| eval-vla-mean-spatial | 143106 → 143112 | **RUNNING** | 15h 05m | 2444 MiB |
| crm-train-v3-perdof | 181668 → 181673 | **RUNNING** | 9m 51s | 508 MiB |
| crm-train-v3-scalar-unc | 181896 → 181901 | **RUNNING** | 9m 44s | 512 MiB |
| crm-train-v3-obs-only | 181973 → 181978 | **RUNNING** | 9m 43s | 512 MiB |

### GPU 总览
- **显存**: 4011 / 24564 MiB (16.3%)，远未饱和，**无 OOM 风险**
- **利用率**: 96%，GPU 算力被充分使用

### crm-train-v3 系列训练进度
三个任务都在正常训练，当前均在 **Epoch 24/50**，val_loss 持续下降：

| 变体 | 当前 val_loss | 趋势 |
|------|-------------|------|
| perdof (full) | 1.2011 | 每 epoch 持续刷新 best |
| scalar-unc | 1.2012 | 每 epoch 持续刷新 best |
| obs-only | 1.2020 | Epoch 24 略微反弹 (1.2020 vs 1.2020)，基本持平 |

三个变体 val_loss 非常接近（~1.201），obs-only 略高但差距很小。

### eval-vla-mean-spatial 进度
正在逐 task 评估，当前在 `pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate`（rollout 5/10）。已完成的 task 成功率差异很大：部分 0%，有一个 80%。已跑了 15 小时，仍在继续。

### 结论
- **4 个任务全部正常运行**，无 OOM、无挂起、无等待
- 4 个进程共用 1 张 4090 D 只占 16% 显存，因为 3 个 CRM 训练是小模型（各 ~512 MiB）
- CRM 训练约 10 分钟跑了 24/50 epoch，预计再 ~10 分钟内全部完成
- eval 是长任务（15h+），仍在正常推进

---
