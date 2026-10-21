# analysis t20 a050 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_t20_a050_s42_fp32_20260520T163556_result.json`
- **Structured JSON:** [`a037e2a2f21c757e6dfa.json`](../../sessions/a0/a037e2a2f21c757e6dfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## T=20 α=0.50 实验结果 — Power Theory 预测验证

### 1. Verification JSON

```json
{
  "alpha": 0.5,
  "seed": 42,
  "T": 20,
  "n_generations": 21,
  "observed_permg_count": 6,
  "observed_rate": 0.75,
  "predicted_permg_count": 7,
  "predicted_rate": 0.8257,
  "predicted_rate_95ci": [0.01502, 0.829926],
  "within_ci": true,
  "robust_pairs_K3": 6
}
```

### 2. 5-Method Forward Significance Counts

| Method | Sig Count (/8) |
|--------|:---------:|
| **Perm Granger FDR (fwd)** | **6** |
| **Diff XCorr FDR (fwd)** | **6** |
| **Threshold Onset (fwd)** | **6** |
| **TY Granger (fwd)** | **4** |
| Perm Granger FDR (rev) | 0 |

### 3. Robust Pairs (K≥3)

**6/8** robust pairs:

| Pair | Votes | Methods |
|------|:-----:|---------|
| ece→distinct_1 | 5/5 | naive, diff, threshold, perm, ty |
| ece→distinct_2 | 4/5 | diff, threshold, perm, ty |
| ece→distinct_3 | 4/5 | diff, threshold, perm, ty |
| token_entropy→distinct_1 | 3/5 | diff, threshold, perm |
| token_entropy→distinct_2 | 3/5 | diff, threshold, perm |
| token_entropy→distinct_3 | 3/5 | diff, threshold, perm |
| token_entropy→mauve | 0/5 | — |
| ece→mauve | 2/5 | naive, ty |

### 4. 训练日志尾部

训练正常完成：
- 最终 metrics: `ppl=34.70, entropy=2.7257, eff_rank=61.5, mauve=0.0259`
- `all_metrics.json` 已保存
- **EXIT_CODE=0**

### 5. Checkpoint 路径

```
results/t20/a050_s42_fp32/gen_19/checkpoint
results/t20/a050_s42_fp32/gen_20/checkpoint
```

### 6. Conclusion: **SUCCESS — Power Theory 预测验证通过**

- Observed PermG = **6/8** (rate=0.750)
- Predicted PermG = 7/8 (rate=0.826)
- T=10 baseline PermG = 6/8 (rate=0.746)
- Observed rate 0.750 **在 95% CI [0.015, 0.830] 内** → **PASS**
- PermG 从 T=10 的 6/8 到 T=20 的 6/8 保持稳定（未显著增长也未 regression）
- Reverse PermG = 0/8，方向性完好——forward causation 清晰，无反向信号
- ECE 通道 lead-lag 信号最强（3 个 downstream 均 4-5/5 consensus），TY 在 ECE pairs 上首次有效（dmax=0 适配 T=20 序列长度）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "alpha": 0.5,
    "seed": 42,
    "T": 20,
    "n_generations": 21,
    "observed_permg_count": 6,
    "observed_rate": 0.75,
    "predicted_permg_count": 7,
    "predicted_rate": 0.8257,
    "predicted_rate_95ci": [
      0.01502,
      0.829926
    ],
    "within_ci": true,
    "robust_pairs_K3": 6
  }
}
```

</details>

---
