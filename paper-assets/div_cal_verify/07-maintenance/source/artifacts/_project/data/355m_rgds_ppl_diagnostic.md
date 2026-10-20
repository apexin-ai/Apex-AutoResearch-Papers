## 355M RGDS Selected vs Rejected PPL (Gen-0 model, seed=42)

Gen 4:
  Selected  (N=488): mean PPL=1.85, median=1.51, P90=2.61
  Rejected  (N=489): mean PPL=1.74, median=1.70, P90=2.11
  差异: +0.11, t=1.45, p=0.1474, Cohen's d=0.09

Gen 7:
  Selected  (N=488): mean PPL=1.80, median=1.58, P90=2.77
  Rejected  (N=489): mean PPL=1.80, median=1.73, P90=2.27
  差异: +0.01, t=0.16, p=0.8747, Cohen's d=0.01

## 跨 Scale 对比
| Scale | Gen 4 d | Gen 7 d | 效应 |
|-------|---------|---------|------|
| 125M | -1.11 | -0.94 | RGDS 强烈选择低 PPL（模板化）样本 |
| 355M | +0.09 | +0.01 | 无系统性差异 |