# ops dose response data prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_dose-response-data-prep_20260515T044245_result.json`
- **Structured JSON:** [`529721d366b8719c1d50.json`](../../sessions/52/529721d366b8719c1d50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CSV 已保存到 `results/dose_response_drift.csv`。完整内容：

```
alpha  metric          gen_0       gen_last    idx  drift_pct     n_gens
0.00   token_entropy   3.234195    3.042682     9   -5.92%         11
0.00   ece             0.010805    0.016972     9   +57.08%        11
0.00   perplexity      26.948959   21.015006    9   -22.02%        11
0.00   distinct_1      0.098216    0.084648     9   -13.81%        11
0.00   distinct_2      0.517803    0.469160     9   -9.39%         11
0.00   distinct_3      0.812728    0.777645     9   -4.32%         11
0.25   token_entropy   3.234195    3.119721     9   -3.54%         11
0.25   ece             0.010805    0.019151     9   +77.25%        11
0.25   perplexity      26.948959   22.512720    9   -16.46%        11
0.25   distinct_1      0.098216    0.059023     9   -39.90%        11
0.25   distinct_2      0.517803    0.229041     9   -55.77%        11
0.25   distinct_3      0.812728    0.343841     9   -57.69%        11
0.50   token_entropy   3.234195    2.608395     7   -19.35%         8
0.50   ece             0.010805    0.096342     7   +791.68%        8
0.50   perplexity      26.948959   30.768688    7   +14.17%         8
0.50   distinct_1      0.098216    0.063937     7   -34.90%         8
0.50   distinct_2      0.517803    0.272713     7   -47.33%         8
0.50   distinct_3      0.812728    0.430483     7   -47.03%         8
1.00   token_entropy   3.234195    1.263724     9   -60.93%        11
1.00   ece             0.010805    0.415585     9   +3746.38%      11
1.00   perplexity      26.948959   917.554517   9   +3304.79%      11
1.00   distinct_1      0.098216    0.070578     9   -28.14%        11
1.00   distinct_2      0.517803    0.336823     9   -34.95%        11
1.00   distinct_3      0.812728    0.557548     9   -31.40%        11
```

### distinct_1 drift 单调性分析

| α    | distinct_1 drift | gen 范围 |
|------|-----------------|----------|
| 0.00 | **-13.81%**     | 0→9      |
| 0.25 | **-39.90%**     | 0→9      |
| 0.50 | **-34.90%**     | 0→7      |
| 1.00 | **-28.14%**     | 0→9      |

**非单调性确认：** distinct_1 的退化并非随 α 单调递增。α=0.25 的退化（-39.90%）反而最严重，α=0.50（-34.90%）和 α=1.00（-28.14%）都弱于它。distinct_2/distinct_3 也有类似模式——α=0.25 的 diversity collapse 最剧烈（-55.77%/-57.69%），远超 α=0.50 和 α=1.00。

不过 α=1.00 在 token_entropy（-60.93%）、ece（+3746%）、perplexity（+3305%）上呈现灾难性崩溃，说明高 α 的退化集中在 calibration/perplexity 维度而非 diversity 维度。α=0.25 则主要表现为 diversity collapse。

**备注：** 实际目录与任务描述略有差异——α=0.25 用的是 `a025_s42`（非 `a025_s42_v3`），α=1.0 在 `results/mvp/rep_42/`（非 `mvp_v4/rep42`）。

---
