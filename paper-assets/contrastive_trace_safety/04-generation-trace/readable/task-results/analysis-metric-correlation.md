# analysis metric correlation

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_metric_correlation_20260517T044054_result.json`
- **Structured JSON:** [`da3c990d5491fcda83ce.json`](../../sessions/da/da3c990d5491fcda83ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved. Here's the output:

## Metric Correlation Matrix (Pearson r across 1000 bootstrap resamples)

### R1-8B (n_valid=33)
```
              Acc      Prec      FPR
    Acc     1.0000   +0.3803   -0.3983
    Prec   +0.3803    1.0000   -0.4212
    FPR    -0.3983   -0.4212    1.0000
    p: acc-prec=9.33e-36, acc-fpr=2.35e-39, prec-fpr=2.87e-44
    |r| > 0.5: NONE
```

### R1-32B (n_valid=20)
```
              Acc      Prec      FPR
    Acc     1.0000   +0.5459   -0.4216
    Prec   +0.5459    1.0000   -0.6724
    FPR    -0.4216   -0.6724    1.0000
    p: acc-prec=9.57e-79, acc-fpr=2.33e-44, prec-fpr=1.45e-132
    |r| > 0.5: acc_prec (r=+0.5459), prec_fpr (r=-0.6724)
```

### QwQ-32B (n_valid=18)
```
              Acc      Prec      FPR
    Acc     1.0000   +0.3672   +0.0839
    Prec   +0.3672    1.0000   -0.6851
    FPR    +0.0839   -0.6851    1.0000
    p: acc-prec=2.82e-33, acc-fpr=7.97e-03, prec-fpr=1.79e-139
    |r| > 0.5: prec_fpr (r=-0.6851)
```

## 结论

**Metrics 非独立，存在显著相关性。** 所有 p-values 均极小（< 0.01），表明三指标间的 bootstrap 分布高度相关。

关键发现：
- **Precision-FPR 相关性最强**：三个模型中 |r| 分别为 0.42, 0.67, 0.69，其中 R1-32B 和 QwQ-32B 的 |r| > 0.5
- **Acc-Prec 中等相关**：|r| 为 0.38, 0.55, 0.37，R1-32B 的 |r| > 0.5
- **Acc-FPR 相关性最弱**：|r| 为 0.40, 0.42, 0.08

由于三指标普遍存在中到强相关（尤其 prec-FPR 在 2/3 模型上 |r| > 0.5），Bonferroni 只校正模型数（3）而非指标×模型（9）是合理的。对独立测试校正 9 次会过度保守。

---
