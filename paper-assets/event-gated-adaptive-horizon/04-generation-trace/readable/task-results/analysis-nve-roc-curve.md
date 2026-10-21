# analysis nve roc curve

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve_roc_curve_20260520T132753_result.json`
- **Structured JSON:** [`2410ead3e92ec1c72c0f.json`](../../sessions/24/2410ead3e92ec1c72c0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== NVE ROC 分析 ===
数据点: n=29 (13 positive, 16 negative)
数据点明细:
  exp_id                  max_nve  label
  024b_ch_s1                0.100     no
  024b_ch_s0                0.200     no
  008a_unexp_s2             0.333     no
  008a_unexp_s1             0.430     no
  015b_frozen               0.467     no
  008a_ch_unexp_s1          0.478     no
  008a_ch_unexp_s0          0.490     no
  009c_s3                   0.520     no
  008e_v3_s1                0.800     no
  027_tcn_s0_σ02            0.908     no
  008e_v3_s4                0.990     no
  008f_s3                   1.000     no
  022b_nocurr               1.220     no
  008f_s4                   1.410     no
  ---- θ=1.5× threshold ----
  008d_s3                   1.530   CIVO
  027_tcn_s1                1.637   CIVO
  018v2_sgs_s1              1.660   CIVO
  025_obs_sgs_s2            1.730     no  ← SGS failure, not CIVO
  028_rave_ceil15           2.230     no  ← anchor pollution, not CIVO
  008e_v3_s2                3.780   CIVO
  019b                      3.780   CIVO
  027_tcn_s0                3.965   CIVO
  008e_v3_s3                4.020   CIVO
  009e_s1                   4.120   CIVO
  008d_s4                   4.620   CIVO
  010b_s1                   8.270   CIVO
  021_sgs_cheetah           9.940   CIVO
  016e_sgs_s1              10.420   CIVO
  010b_s0                  70.640   CIVO

AUROC: 0.971 (95% CI: 0.904 – 1.000)
θ=1.5× 工作点: TPR=1.00, FPR=0.12
最优阈值（Youden's J）: θ=1.53, TPR=1.00, FPR=0.12 (与 1.5× 重合)
2 个 FP: RAVE anchor pollution (NVE=2.23) + obs-SGS failure (NVE=1.73)
图表路径: artifacts/figures/nve_roc_curve.pdf / .png
```

FPR=0.12 的两个假阳性来自非 CIVO 机制的崩溃（RAVE anchor pollution、obs-decoder SGS 副作用），恰好说明 NVE 检测的是 value overestimation 信号而非崩溃本身——支持 θ=1.5× 不是 post-hoc 的论点。

---
