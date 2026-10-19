# code fisher test script object

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fisher-test-script-object_20260515T204705_result.json`
- **Structured JSON:** [`73d39e9226f6468b6cd5.json`](../../sessions/73/73d39e9226f6468b6cd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

dry-run 完成，输出如下：

```
============================================================
  LIBERO-Object 6-Method Statistical Analysis
============================================================
Mode: seed=42 only
Seeds available per method:
  obs_only    : 1 seed(s)
  argmin      : 1 seed(s)
  perdof      : 1 seed(s)
  vla_only    : 1 seed(s)
  vla_mean    : 1 seed(s)
  scalar      : 1 seed(s)

============================================================
  1. Pooled Fisher Exact Test: obs_only vs argmin
============================================================

  obs_only: 19/100 = 19.0%
  argmin:   12/100 = 12.0%

  2x2 contingency table:
              success  failure
  obs_only         19       81
  argmin           12       88

  Fisher exact p-value (two-sided): 0.2408
  Odds ratio: 1.720
  Cohen's h: 0.195

  Interpretation: Not significant (p>=0.05)

============================================================
  2. Per-Seed Fisher Exact Test: obs_only vs argmin
============================================================

  seed42:
    obs_only: 19/100 = 19.0%
    argmin:   12/100 = 12.0%
    Fisher p = 0.2408, OR = 1.720, h = 0.195

============================================================
  3. Bootstrap CI for SR Difference (obs_only - argmin)
============================================================

  Task-level resampling, 10 tasks, 10000 bootstrap iterations
  Mean difference: +0.0702 (+7.0%)
  95% CI: [+0.0300, +0.1100] ([+3.0%, +11.0%])
  CI includes 0: No → significant

============================================================
  4. Six-Way Comparison Table
============================================================

  Method       |  Pooled SR |  seed42 SR |  seed43 SR | Seeds
  -------------+------------+------------+------------+------
  obs_only     |     19.0% |     19.0% |        N/A |     1
  argmin       |     12.0% |     12.0% |        N/A |     1
  perdof       |     11.0% |     11.0% |        N/A |     1
  vla_only     |     12.0% |     12.0% |        N/A |     1
  vla_mean     |     12.0% |     12.0% |        N/A |     1
  scalar       |      9.0% |      9.0% |        N/A |     1

============================================================
  5. Pairwise Fisher Tests: obs_only vs Each Baseline
============================================================

  Bonferroni correction: 5 comparisons, α_adj = 0.0100

  Comparison                     |  p-value |    p_adj |     OR |      h |   Sig?
  -------------------------------+----------+----------+--------+--------+-------
  obs_only vs argmin             |   0.2408 |   1.0000 |  1.720 | +0.195 |     No
  obs_only vs perdof             |   0.1649 |   0.8247 |  1.898 | +0.226 |     No
  obs_only vs vla_only           |   0.2408 |   1.0000 |  1.720 | +0.195 |     No
  obs_only vs vla_mean           |   0.2408 |   1.0000 |  1.720 | +0.195 |     No
  obs_only vs scalar             |   0.0652 |   0.3261 |  2.372 | +0.293 |     No
```

**验证结果**:
- 5 个 section 全部正常输出
- Pooled Fisher p=0.2408，符合预期范围（19% vs 12%, n=100, 预期 p≈0.17-0.25）
- Bootstrap CI [+3.0%, +11.0%] 不含 0 — task-level resampling 比 Fisher 更敏感，因为它保留了 task 间方差结构
- Six-way table 数值正确（obs_only 19%, scalar 最低 9%）
- Bonferroni 校正后所有比较均不显著（单 seed 100 trials power 不够）

seed=43 数据到齐后填入 `SEED43` dict 即可，不需改代码逻辑。

---
