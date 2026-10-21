# A3: Cascade Length & Position Analysis

## 1. Cascade Length vs Pruning Outcome

**Question:** Does ack chain length predict pruning safety?

### Qwen×GSM8K (N=1,999 task-seed pairs; 200 tasks × 10 seeds)

| Chain Len | N     | Safe (%) | Improved (%) | Degraded (%) |
|-----------|-------|----------|--------------|--------------|
| 0         | 9     | 100.0    | 0.0          | 0.0          |
| 1         | 507   | 98.4     | 1.0          | 0.6          |
| 2         | 1,188 | 98.9     | 0.9          | 0.2          |
| 3         | 23    | 100.0    | 0.0          | 0.0          |
| 4+        | 272   | 98.2     | 0.4          | 1.5          |

- Point-biserial r = −0.007, p = 0.753
- Mann-Whitney U = 25,791, p = 0.956
- Cochran-Armitage z = 1.767, p = 0.077
- Mean chain: safe = 2.02, changed = 2.08

**Verdict:** No significant relationship. Pruning safety is uniformly high (~98–100%) regardless of chain length.

### Llama×GSM8K (N=1,939 task-seed pairs; 200 tasks × 10 seeds)

| Chain Len | N     | Safe (%) | Improved (%) | Degraded (%) |
|-----------|-------|----------|--------------|--------------|
| 0         | 90    | 86.7     | 1.1          | 12.2         |
| 1         | 1,167 | 92.1     | 5.6          | 2.3          |
| 2         | 463   | 96.5     | 1.7          | 1.7          |
| 3         | 50    | 84.0     | 16.0         | 0.0          |
| 4+        | 169   | 96.4     | 3.0          | 0.6          |

- Point-biserial r = 0.063, p = 0.005
- Mann-Whitney U = 139,443, p < 0.001
- Cochran-Armitage z = −3.662, p < 0.001
- Mean chain: safe = 1.52, changed = 1.28

**Verdict:** Statistically significant but tiny effect (r = 0.063). Longer chains marginally associated with safer pruning, but the degraded rate at chain=0 (12.2%) is the primary driver—tasks with zero acks have fewer redundant messages to prune safely.

---

## 2. Position Control: Cascade as Sequential Dependency vs Position Artifact

**Question:** Are ack cascades genuine sequential dependencies, or artifacts of conversation position?

**Method:** Logistic regression P(ack_t | ack_{t−1}, position_t). If cascades are position artifacts, prev_ack should lose significance after controlling for position.

### Qwen×GSM8K (N=1,200 message pairs; 300 tasks)

| Predictor | OR    | 95% CI          | p-value   |
|-----------|-------|-----------------|-----------|
| prev_ack  | 6.425 | [4.377, 9.432]  | 2.14e-21  |
| position  | 1.950 | —               | 1.22e-19  |

- AIC (full) = 1,212.6 vs AIC (position-only) = 1,315.5 → ΔAIC = −102.8
- BIC (full) = 1,227.9 vs BIC (position-only) = 1,325.6

### Llama×GSM8K (N=1,176 message pairs; 294 tasks)

| Predictor | OR    | 95% CI          | p-value   |
|-----------|-------|-----------------|-----------|
| prev_ack  | 2.022 | [1.489, 2.747]  | 6.49e-06  |
| position  | 0.734 | —               | 8.28e-06  |

- AIC (full) = 1,574.8 vs AIC (position-only) = 1,593.6 → ΔAIC = −18.9
- BIC (full) = 1,590.0 vs BIC (position-only) = 1,603.8

**Verdict:** prev_ack remains highly significant (p < 1e-5) after controlling for position in both backbones. Cascades are genuine sequential dependencies—a message is 2–6× more likely to be an ack if the preceding message was also an ack.

---

## 3. Rebuttal One-Liner

> **Pruning effectiveness is robust to cascade structure:** chain length does not predict pruning outcome (Qwen: r = −0.007, p = 0.753; Llama: r = 0.063, p = 0.005 with negligible effect size), and acknowledgment cascades reflect genuine sequential dependencies rather than position artifacts (prev_ack OR = 2.0–6.4, p < 1e-5 after position control, ΔAIC = −18.9 to −102.8).
