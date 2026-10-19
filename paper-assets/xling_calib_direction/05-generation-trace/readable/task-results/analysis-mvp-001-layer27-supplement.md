# analysis mvp 001 layer27 supplement

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_001_layer27_supplement_20260520T184655_result.json`
- **Structured JSON:** [`1a174509718c9ff4b899.json`](../../sessions/1a/1a174509718c9ff4b899.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是完整结果：

```
=== Layer 27 Results ===

英语 Probe:
  Layer 27: AUROC=0.7541  ECE=0.1951  Brier=0.2227
  Temperature scaling: T=6.21 → ECE=0.0744 (PASS P1)

Zero-shot Transfer (layer 27):
  zh: AUROC=0.6607  ECE=0.2673  p=0.0010
  ar: AUROC=0.6346  ECE=0.3202  p=0.0010
  hi: AUROC=0.6257  ECE=0.4363  p=0.0010
  sw: AUROC=0.5603  ECE=0.3270  p=0.0010
  ko: AUROC=0.6069  ECE=0.3423  p=0.0010

Mean-shift (layer 27):
  zh: AUROC=0.6607  ECE=0.2598  ΔECE=-0.75pp
  ar: AUROC=0.6346  ECE=0.3440  ΔECE=+2.38pp
  hi: AUROC=0.6256  ECE=0.3797  ΔECE=-5.66pp
  sw: AUROC=0.5603  ECE=0.5103  ΔECE=+18.33pp
  ko: AUROC=0.6069  ECE=0.3707  ΔECE=+2.84pp

对比 Layer 24 vs Layer 27:
  EN AUROC: L24=0.7486 vs L27=0.7541 (Δ=+0.55pp)
  EN ECE:   L24=0.1982 vs L27=0.1951 (Δ=-0.31pp)
  EN Brier: L24=0.2249 vs L27=0.2227 (Δ=-0.22pp)
```

Layer 27 是所有层中 AUROC 最高的（0.7541 > L24 的 0.7486），且原始 ECE 略低于 L24。经 temperature scaling 后 ECE=0.0744，远低于 0.15 阈值，**P1 判定 PASS**。两个 CSV 文件已合并完毕，layer 27 数据已追加到完整结果中。

---
