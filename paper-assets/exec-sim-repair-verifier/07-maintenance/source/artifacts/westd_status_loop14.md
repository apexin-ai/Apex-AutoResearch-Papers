# Westd Status — Loop 14 (2026-05-15 10:15 UTC)

## GPU 状态

| GPU | 利用率 | 显存 Used/Total | 任务 |
|-----|--------|----------------|------|
| 0 | 86% | 17.6/32 GB | eval 已完成，GPU 即将空闲 |
| 1 | 97% | 27.3/32 GB | cls-8b s42 resume 训练 |
| 2 | 98% | 30.7/32 GB | cwm-8b 训练 |
| 3 | 91% | 30.9/32 GB | cls-8b seed123 训练 |

磁盘：/root/autodl-tmp 139G/250G (56%)

---

## ★ ckpt-1000 Test Eval — 已完成

**checkpoint**: cls-8b s42 ckpt-1000
**测试集**: 9784 instances (pass=7138, fail=2646)
**Majority baseline**: 73.0%

| 指标 | 值 |
|------|----|
| **Accuracy** | **83.52%** (+10.6pp vs majority) |
| **F1 macro** | **77.50%** |

**Per-class 指标**:

| Class | Precision | Recall | F1 |
|-------|-----------|--------|----|
| fail | 74.9% | 58.7% | 65.8% |
| pass | 85.8% | 92.7% | 89.1% |

**Confusion Matrix**:
```
              Predicted
              fail    pass
Actual fail   1554    1092
Actual pass    520    6618
```

结果文件：`eval_repo_cls.json`, `eval_repo_cls_predictions.jsonl`

---

## 训练进度

### 1. cls-8b s42 resume (cuda:1)

| 项目 | 值 |
|------|----|
| Step | ~1811/6633 (27%) |
| Epoch | 0.81 |
| 速度 | ~8-15 s/step (波动) |
| 预估剩余 | ~16h → 约 May 16 02:00 |

**eval_loss 趋势**:
| Step | Epoch | eval_loss |
|------|-------|-----------|
| 800 | 0.36 | 0.1717 ★ best |
| 1000 | 0.45 | 0.1820 |
| 1200 | 0.54 | 0.2046 |
| 1400 | 0.63 | 0.3226 |
| 1600 | 0.72 | 0.2758 |
| 1800 | 0.81 | 0.2764 |

**Checkpoints**: 800, 1000, 1200, 1400, 1600, 1800

### 2. cwm-8b s42 (cuda:2)

| 项目 | 值 |
|------|----|
| Step | ~2900/6633 (44%) |
| Epoch | 1.27 |
| 速度 | ~12.2 s/step |
| 预估剩余 | ~12.7h → 约 May 15 23:00 |

**eval_loss 趋势**:
| Step | Epoch | eval_loss |
|------|-------|-----------|
| 2800 | 1.22 | 0.4466 |
| 2900 | 1.27 | 0.4478 |

**Checkpoints**: 400, 2500, 2600, 2700, 2800

### 3. cls-8b seed123 (cuda:3) — 最接近完成

| 项目 | 值 |
|------|----|
| Step | ~5400/6633 (81%) |
| Epoch | 2.44 |
| Latest loss | 0.2755 |
| 速度 | ~8.5 s/step |
| 预估剩余 | ~2.9h → 约 May 15 13:00 |

**eval_loss 趋势**:
| Step | Epoch | eval_loss |
|------|-------|-----------|
| 5000 | 2.17 | 0.3731 |
| 5200 | 2.26 | 0.3649 ★ recent best |
| 5400 | 2.35 | 0.3899 |

**Checkpoints**: 200, 4600, 4800, 5000, 5200

---

## 异常

无。所有进程存活，无 OOM，无报错。eval 进程正常退出，tmux session 已自动清理。
