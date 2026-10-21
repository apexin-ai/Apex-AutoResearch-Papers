# Claim 3: Avoidance Source Diagnosis — Data Summary

## 1A. Main Summary Table

| Condition | Seeds | CAR (per-seed) | CAR mean±std | TSR mean±std | dfCAR | frozen | EE Disp (m) |
|-----------|-------|----------------|--------------|--------------|-------|--------|-------------|
| Pi0.5 baseline | 3 | — | 26.8±1.6% | 74.7±1.5% | — | 0% | 0.367 |
| LoRA-only | 2 | s0=56.5, s1=52.5 | 54.5±2.83% | 51.5% | 54.5% | 0% | 0.392 |
| SDF λ=0.005 | 3 | s0=57.0, s1=54.0, s2=52.5 | 54.5±2.29% | 54.0±3.0% | 54.5% | 0% | 0.387 |
| SDF λ=0.01 | 3 | s0=57.0, s1=57.5, s2=54.5 | 56.3±1.61% | 53.8±1.5% | 56.3% | 0% | 0.389 |
| SDF λ=0.1 (20K) | 2 | s0=55, s1=56 | 55.5±0.71% | 52.5% | — | 0% | — |
| SDF λ=0.1 (30K) | — | pending | pending | pending | — | — | — |

### Null Distribution

Pooled from LoRA-only (2 seeds) + λ=0.005 (3 seeds) = 5 values: 56.5, 52.5, 57.0, 54.0, 52.5

- **mean = 54.5%**, **σ = 2.15%**

### Key Comparisons

| Comparison | Δ vs null | σ units | p-value | Verdict |
|------------|-----------|---------|---------|---------|
| λ=0.01 mean (56.3%) vs null | +1.8pp | +0.84σ | >0.1 | not significant |
| λ=0.1 20K mean (55.5%) vs null | +1.0pp | +0.47σ | >0.1 | within null |
| Phase 2 ablation (λ=0 after 5K): 57.5% vs null | +3.0pp | +1.40σ | ~0.08 | within null |

All SDF conditions fall within the null distribution range.

---

## 1B. Per-Task Breakdown

### TSR per-task (from appendix.tex Table tab:per_task_tsr)

| Task | Pi0.5 base | LoRA-only (2s mean) | SDF 0.005 (3s mean) | SDF 0.01 (3s mean) |
|------|-----------|---------------------|----------------------|---------------------|
| Orange Juice | 70.7 | 33.0 | 33.3 | 24.7 |
| Choco Pudding | 86.0 | 68.0 | 78.0 | 76.7 |
| Milk | 66.0 | 46.0 | 35.3 | 48.7 |
| BBQ Sauce | 76.0 | 59.0 | 69.3 | 65.3 |

> **Note**: These are **TSR** values, not CAR. Source: appendix.tex Table tab:per_task_tsr.

### CAR per-task for λ=0.1 (20K) (from eval JSON results)

| Task | seed 0 | seed 1 |
|------|--------|--------|
| Orange Juice | 50 | 62 |
| Choco Pudding | 72 | 76 |
| Milk | 72 | 66 |
| BBQ Sauce | 26 | 20 |

> **Note**: These are **CAR** values. Source: eval result JSONs.

---

## 1C. Scenario B Narrative Points

1. **λ∈[0.005, 0.1] all within null range** — no SDF weight produces statistically significant CAR improvement over LoRA-only baseline.
2. **20× increase in SDF loss weight ineffective** — going from λ=0.005 to λ=0.1 does not change CAR.
3. **Level A signal masking is not a binding constraint** — even when SDF signal strength is amplified by 20×, collision avoidance rate does not improve.
4. **Level B (EE-only structural mismatch) is the sole binding constraint** — the SDF auxiliary loss acts on end-effector position only, but collision avoidance requires full-body awareness (links, joints, swept volumes).
5. **Paper conclusion: purely negative finding** — Claim 3 establishes that the SDF-based approach fundamentally cannot improve collision avoidance due to the structural gap between EE-level SDF supervision and the full-body collision geometry.

---

## Data Provenance

- All 30K eval data: seed=7, rotation-fixed `eval_safelibero.py`
- λ=0.1 training uses suffix `_l1` (not `_l01`)
- Scenario B confirmed at 20K with dual seeds (55%, 56%)
- Phase 2 ablation (λ=0 after 5K): CAR=57.5%
- Null distribution: 5-sample pooled from LoRA-only + λ=0.005
