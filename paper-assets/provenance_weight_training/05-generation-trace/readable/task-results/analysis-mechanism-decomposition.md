# analysis mechanism decomposition

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mechanism-decomposition_20260516T191250_result.json`
- **Structured JSON:** [`7c53d82170558c6c9bfe.json`](../../sessions/7c/7c53d82170558c6c9bfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个产出已注册。以下是完整结果：

---

### 统计量汇总

| 指标 | 值 |
|------|-----|
| Paired PPL gap (adaptive better) | 0.0722 |
| Bootstrap 95% CI | [0.0624, 0.0773] |
| Paired t-test | t=14.772, p=0.0046 |
| ESS binding (ρ=0.4 → 0.6) | 61.0% → 66.0% (+5pp) |
| α_eff binding (ρ=0.4 → 0.6) | 38.2% → 33.4% (−4.8pp) |
| Intervention ratio (ESS-only / adaptive b*) | 4.9× |

N=3 的 p=0.0046 不常见地显著，bootstrap CI 不跨零（全正区间），两者一致指向 adaptive 优于 ESS-only。

---

### 论文叙事段落

> The dual-constraint architecture yields a consistent PPL advantage over ESS-only across three seeds (gap = 0.072, bootstrap 95% CI [0.062, 0.077]; paired *t*-test *p* = 0.005, *N* = 3). Constraint regime decomposition reveals the mechanism: at ρ = 0.4, 38.2% of batches are α_eff-binding and 61.0% are ESS-binding, with < 1% unconstrained. As contamination rises to ρ = 0.6, the ESS constraint absorbs more batches (66.0%), while α_eff binding recedes to 33.4%. This structural shift means the dual system *automatically* throttles intervention under heavier contamination—the ESS floor prevents over-downweighting that would otherwise degrade language modeling. In α_eff-binding batches, the adaptive method applies a mean b\* ≈ 1.19, whereas ESS-only permits b\* up to ≈ 5.88—a 4.9× over-correction that explains its PPL penalty. Proportion-robustness thus emerges as a structural consequence of dual constraints, not a tuned coincidence: higher ρ triggers more ESS binding, which caps the damage floor, making the method inherently adaptive to unknown contamination levels.

---
