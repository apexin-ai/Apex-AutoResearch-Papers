# 14B RSFT s43 Test Eval — Evidence Tax Analysis

## 1. 完整指标表

| Metric | with_evi (s43) | no_evi (s43) |
|--------|---------------|-------------|
| **ign_f1** | **0.3767** | **0.3775** |
| f1 | 0.3767 | 0.3775 |
| precision | 0.4252 | 0.4138 |
| recall | 0.3382 | 0.3470 |
| format_ok_rate | 0.996 (498/500) | 0.998 (499/500) |
| n_truncated | 271/500 | 292/500 |
| n_predictions | 22,861 | 31,216 |
| tp / gold | 5,867 / 17,350 | 6,020 / 17,350 |
| inference_time | 6,583.2s (1h49m) | 6,554.6s (1h49m) |
| Evi-F1 (DREEAM) | 0.2468 | N/A |
| Evi-F1 (TP) | 0.5836 | N/A |
| EDCR | 0.8340 | N/A |

**Note:** `ign_f1 == f1` because `train_annotated.json` not found (test split, no train overlap filtering).

## 2. Evidence Tax 计算

```
evidence_tax = no_evi_ign_f1 - with_evi_ign_f1
             = 0.3775 - 0.3767
             = +0.0008
             = +0.08 pp  (正值 = no-evi 更好)
```

## 3. 与 s42 对比

| Metric | s42 | s43 |
|--------|-----|-----|
| with_evi ign_f1 | 0.3849 | 0.3767 |
| no_evi ign_f1 | 0.3926 | 0.3775 |
| evidence_tax (pp) | **+0.77** | **+0.08** |

s43 两个变体的 ign_f1 均低于 s42（约 -0.8pp ~ -1.5pp），seed 间存在方差。

## 4. 14B 2-Seed Evidence Tax 汇总

| Seed | with_evi | no_evi | Tax (pp) |
|------|----------|--------|----------|
| s42 | 0.3849 | 0.3926 | +0.77 |
| s43 | 0.3767 | 0.3775 | +0.08 |
| **Mean** | **0.3808** | **0.3851** | **+0.43** |
| **Std** | **0.0058** | **0.0107** | **±0.49** |

Evidence tax mean = **+0.43 ± 0.49 pp** (sample std, n=2).

方向一致（两个 seed 均为正，即 no-evi ≥ with-evi），但幅度小且 seed 间方差大，税值在统计意义上不显著。

## 5. 结论判定

| Experiment | Conclusion | 理由 |
|-----------|-----------|------|
| test_eval_14b_rsft_s43_with_evi | **success** | 完成推理，format_ok 99.6%，ign_f1=0.3767 合理 |
| test_eval_14b_rsft_s43_no_evi | **success** | 完成推理，format_ok 99.8%，ign_f1=0.3775 合理 |

**Evidence tax 整体判定：** 14B 模型的 evidence tax 为 +0.43±0.49pp，方向一致但幅度极小，evidence 输出对 RE 性能的负面影响可忽略。
