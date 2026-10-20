# eval probe 001 mvp

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_probe_001_mvp_20260514T081126_result.json`
- **Structured JSON:** [`efab2c07a629eef99280.json`](../../sessions/ef/efab2c07a629eef99280.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## evaluate.py 完整原始输出

```
Applying confidence filter (min_confidence=2): 15401/54809 windows
Test set: 1824 windows
Loading trajectory data for baselines ...

| Method | Macro-F1 | Accuracy | Precision | Recall | F1(stag) | F1(prog) |
|---|---|---|---|---|---|---|
| GRU Probe            | 0.9055   | 0.9282   | 0.9176    | 0.8952 | 0.8593   | 0.9518   |
| Random               | 0.4955   | 0.5598   | 0.5024    | 0.5029 | 0.3154   | 0.6756   |
| Majority             | 0.4233   | 0.7341   | 0.3671    | 0.5000 | 0.0000   | 0.8467   |
| CosineSim            | 0.3129   | 0.3591   | 0.3469    | 0.3044 | 0.1347   | 0.4911   |
| Repeat-3             | 0.8432   | 0.8947   | 0.9373    | 0.8021 | 0.7532   | 0.9331   |

Best baseline: Repeat-3 (Macro-F1: 0.8432)
GRU Probe improvement: +0.0624 (+7.4%)
```

## MVP 判定

```
MVP 判定：
- Probe test macro-F1: 0.9055
- Baseline 对比:
  - Random:      0.4955
  - Majority:    0.4233
  - CosineSim:   0.3129
  - Repeat-3:    0.8432
- Best baseline: 0.8432 (Repeat-3)
- Gap: 6.24pp
- MVP 条件 1 (F1 ≥ 0.70): PASS ✓
- MVP 条件 2 (gap ≥ 5pp): PASS ✓
```

## 训练曲线摘要

```
训练曲线摘要：
- Best epoch: 3
- Best val macro-F1: 0.9511
- Final train loss: 0.0215 (epoch 8)

逐 epoch 明细：
  Epoch 1: train_loss=0.2040, val_macro_f1=0.9184
  Epoch 2: train_loss=0.1178, val_macro_f1=0.9456
  Epoch 3: train_loss=0.0822, val_macro_f1=0.9511 ← best
  Epoch 4: train_loss=0.0616, val_macro_f1=0.9388
  Epoch 5: train_loss=0.0429, val_macro_f1=0.9426
  Epoch 6: train_loss=0.0360, val_macro_f1=0.9460
  Epoch 7: train_loss=0.0239, val_macro_f1=0.9419
  Epoch 8: train_loss=0.0215, val_macro_f1=0.9425
```

**两项 MVP 条件均通过。** GRU Probe (0.9055) 在 test set 上大幅超过 0.70 阈值，且比最强 baseline Repeat-3 (0.8432) 高出 6.24pp (>5pp)。训练在 epoch 3 达到最佳 val F1 (0.9511)，之后略有波动但未显著退化。

---
