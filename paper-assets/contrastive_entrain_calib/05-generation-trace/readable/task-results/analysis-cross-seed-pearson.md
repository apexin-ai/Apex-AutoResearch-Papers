# analysis cross seed pearson

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross-seed-pearson_20260522T090310_result.json`
- **Structured JSON:** [`d41de7d4631a7a6ada1e.json`](../../sessions/d4/d41de7d4631a7a6ada1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
Pearson r = 0.5245  (p = 0.182)
Spearman rho = 0.8583  (p = 0.006)
Bootstrap 95% CI for r: [0.080, 0.957]
n = 8
```

- **Pearson r=0.525**，moderate correlation，但 p=0.182 不显著（n=8 太小）
- **Spearman rho=0.858**，p=0.006 显著——说明两个 seed 的 rank order 高度一致，只是幅度不同
- Bootstrap 95% CI 很宽 [0.08, 0.96]，反映样本量不足的不确定性

---
