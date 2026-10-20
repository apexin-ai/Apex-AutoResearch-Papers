# Training Progress Report

**Time:** 2026-05-15 13:10 UTC

## Experiment 1: vota_no_ae_seed42 (plan_001)

| Metric | Value |
|--------|-------|
| Progress | 208/444 steps (46.8%) |
| Latest Loss | 0.0603 (epoch 0.95) |
| Token Accuracy | 0.983 |
| Loss Trend | 0.8221 → 0.0603 (单调下降，正常) |
| Speed | ~13.5 s/it |
| ETA | ~14:04 UTC (约 53 min) |
| GPU | cuda:1, 52,779 / 97,887 MiB, 100% util, 69°C |
| PID | 953133 (bash) → 953138 (python) |

Loss 历史（每 ~30 steps 输出一次）：
- epoch 0.07: 0.8221 → 0.14: 0.6149 → 0.20: 0.3124 → 0.27: 0.1757
- epoch 0.34: 0.1483 → 0.41: 0.1215 → 0.47: 0.1216 → 0.54: 0.1212
- epoch 0.61: 0.1024 → 0.68: 0.0919 → 0.75: 0.0806 → 0.81: 0.0749
- epoch 0.88: 0.0662 → 0.95: 0.0603

## Experiment 2: full_trace_label_only_seed42 (plan_002)

| Metric | Value |
|--------|-------|
| Progress | 70/444 steps (15.8%) |
| Latest Loss | 尚未输出（首次 log 需到 ~step 148） |
| Speed | ~18.4 s/it |
| ETA | ~15:06 UTC (约 115 min) |
| GPU | cuda:0, 90,355 / 97,887 MiB, 100% util, 75°C |
| PID | 955296 (bash) → 955301 (python) |

使用 gradient_checkpointing，显存占用更高（90 GB vs 53 GB），单步速度更慢（18.4s vs 13.5s）。

## GPU 总览

| GPU | Model | VRAM | Util | Temp | Power |
|-----|-------|------|------|------|-------|
| 0 (full_trace) | RTX PRO 6000 Blackwell | 90,355 / 97,887 MiB (92%) | 100% | 75°C | 510W/600W |
| 1 (vota_no_ae) | RTX PRO 6000 Blackwell | 52,779 / 97,887 MiB (54%) | 100% | 69°C | 474W/600W |

## 异常检查

- ✅ 无 OOM warning
- ✅ 无 loss spike（实验 1 loss 单调下降）
- ✅ 两进程均存活
- ✅ GPU 温度正常（< 80°C）
- ⚠️ 实验 2 尚未产出 loss 值，需等到 ~step 148 才有首次 loss 输出
