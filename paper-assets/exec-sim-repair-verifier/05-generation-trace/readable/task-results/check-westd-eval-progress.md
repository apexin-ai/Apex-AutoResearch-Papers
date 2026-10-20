# check westd eval progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-eval-progress_20260514T200451_result.json`
- **Structured JSON:** [`e4737a973364895bd08a.json`](../../sessions/e4/e4737a973364895bd08a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Westd 4×5090 状态汇报

### GPU 状态

| GPU | 利用率 | 显存 | 任务 | PID |
|-----|--------|------|------|-----|
| cuda:0 | 99% | 19.8/32.6 GB | CLS 8B val@5120 sweep | 276775 |
| cuda:1 | 100% | 13.6/32.6 GB | CLS v5 4B val@5120 sweep | 277670 |
| cuda:2 | 97% | 30.7/32.6 GB | CWM 8B 训练 | 266816 |
| cuda:3 | 90% | 30.9/32.6 GB | CLS 8B seed123 训练 | 266449 |

---

### cuda:0 — CLS 8B val@5120 sweep (PID 276775)
- 当前: **ckpt-200**, 6000/9335 (64.3%), running_acc=**64.5%**
- 速度: ~1.7s/10样本
- 预计 ckpt-200 还剩 ~10min，之后串行跑 ckpt-400 和 ckpt-600（各 ~17min）
- **ETA 整个 CLS 8B sweep 完成: ~44min**

### cuda:1 — CLS v5 4B val@5120 sweep (PID 277670)
- 当前: **ckpt-200**, 4640/9335 (49.7%), running_acc=**61.4%**
- 速度: ~3.7s/20样本
- 预计 ckpt-200 还剩 ~14min，之后串行跑 ckpt-400 和 ckpt-600
- **ETA 整个 CLS v5 sweep 完成: ~60min**

### cuda:2 — CWM 8B 训练 (PID 266816)
- Step: **1984/6633 (29.9%)**, ~12.1s/it
- 最新 eval (step 1900): **eval_loss=0.3866**, epoch=0.81
- 最新 train: **loss=0.2261**, lr=3.76e-5, epoch=0.86
- **ETA: ~15.7hr**

### cuda:3 — CLS 8B seed123 训练 (PID 266449)
- Step: **3702/6633 (55.8%)**, ~8.0s/it
- 最新 eval (step 3600): **eval_loss=0.3874**, epoch=1.63, checkpoint已保存
- 训练指标趋势:
  - step 3050: loss=0.5255, grad_norm=205.4
  - step 3650: loss=0.3716, grad_norm=9.59
  - step 3700: loss=0.3805, grad_norm=0.14
- loss 明显下降，grad_norm 已稳定
- **ETA: ~6.5hr**

---

### 训练指标趋势
- **CWM 8B**: train_loss 0.2261 vs eval_loss 0.3866 — gap 较大，可能有过拟合迹象
- **CLS 8B seed123**: train_loss ~0.37 vs eval_loss 0.3874 — 很接近，泛化良好

---

### val@5120 sweep 完整计划（val5120_sweep_commands.txt）

**4B 模型 sweep（sweep文件中的 13 个 runs）：**
1. CLS v5 (4B): 3 ckpts (200/400/600) — **cuda:1 正在跑 ckpt-200**
2. CWM v12 (4B): 5 ckpts (300/400/500/600/700)
3. CWM seed123 (4B): 5 ckpts (200/300/400/500/600)

执行策略: 6 phases，cuda:0 + cuda:1 并行，预计 6-12hr

**8B 模型 sweep（单独启动）：**
- CLS 8B: 3 ckpts (200/400/600) — **cuda:0 正在跑 ckpt-200**

**当前进度**: CLS 8B 和 CLS v5 各自的 ckpt-200 都在跑，ckpt-200 完成后各自还有 ckpt-400 和 ckpt-600。CLS 8B sweep 约 44min 完成，CLS v5 约 60min 完成。之后 cuda:0/1 可以开始跑 CWM v12 和 CWM seed123 的 val@5120 sweep（10 个 CWM runs，预计 5-10hr）。

---
