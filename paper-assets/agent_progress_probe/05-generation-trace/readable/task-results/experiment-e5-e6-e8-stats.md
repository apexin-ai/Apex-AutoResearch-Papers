# experiment e5 e6 e8 stats

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_e5-e6-e8-stats_20260515T141424_result.json`
- **Structured JSON:** [`ee78ae20b306d36350da.json`](../../sessions/ee/ee78ae20b306d36350da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部完成。汇总如下：

---

## E5: 11 vs 30 Features 显著性检验

| Scope | N | F1(11-feat) | F1(30-feat) | Δ | 95% CI | p |
|---|---|---|---|---|---|---|
| All OH windows | 150,652 | 0.977 | 0.967 | **+0.96pp** | [+0.85, +1.07] | **<0.001** |
| Conf≥2 only | 43,376 | 0.985 | 0.992 | −0.71pp | [−0.88, −0.54] | 1.0 (NS) |

**结论**: All-windows 上 11 LF-overlap 特征显著优于 30 全特征 (p<0.001)。但在 conf≥2 高置信窗口上方向反转——额外 19 特征有帮助。Residual 19 特征单独使用 cross-agent F1 仅 0.566（崩溃）。

---

## E6: κ Bootstrap CI (N=52, B=10,000)

| Metric | Point | 95% CI |
|---|---|---|
| Fleiss κ | 0.390 | [0.165, 0.589] |
| Cohen κ (b1-b2) | 0.485 | [0.235, 0.733] |
| Cohen κ (b1-b3) | 0.406 | [0.132, 0.650] |
| Cohen κ (b2-b3) | 0.330 | [0.089, 0.575] |

所有 κ 的 CI 下界 >0，一致性显著高于 chance。Fleiss κ=0.39 属 "fair agreement"，但 CI 宽（小样本）。Unanimous 33/52 (63.5%)。

---

## E8: GB on Set A (N=52, conf≥3)

| Model | N | macro-F1 | F1(stag) | F1(prog) | Prec(stag) | Rec(stag) | Acc |
|---|---|---|---|---|---|---|---|
| **GB** | 50 | 0.721 | 0.593 | 0.849 | 0.533 | 0.667 | 0.78 |
| RF | 50 | 0.740 | 0.615 | 0.865 | 0.571 | 0.667 | 0.80 |
| MV | 50 | 0.721 | 0.593 | 0.849 | 0.533 | 0.667 | 0.78 |
| GRU Probe | 35 | 0.762 | 0.714 | 0.810 | 0.588 | 0.909 | 0.77 |
| TWV Probe | 35 | 0.746 | 0.667 | 0.826 | 0.615 | 0.727 | 0.77 |

- GB = MV（完全相同预测，p=1.0）
- 所有模型差异均不显著（p>0.25），Set A 太小
- Gold 分布：40 prog / 12 stag（unanimous 33: 27 prog + 6 stag）
- MV-Gold agreement: 78% (39/50)
- 对比 Set B (conf≥2, N=491): GB macro-F1 升至 **0.839**, F1(stag) 升至 **0.770**

结果已保存至 `artifacts/e5_e6_e8_results.json`。

---
