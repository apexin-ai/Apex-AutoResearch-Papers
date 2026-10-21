# Table 2: Hacking Taxonomy Distribution

Data sources: plan012 (aggregate taxonomy), paper_framing D043/D044 (per-seed H7 calibration), classify_h7.py reproducible.

## Table 2a: ISR β=0.1 vs Random β=0.1 — s42 Strict Taxonomy (D044)

| Hacking Mode | ISR β=0.1 s42 (n=81) | Random β=0.1 s42 (n=79) | Delta | Interpretation |
|-------------|----------------------|--------------------------|-------|----------------|
| **Genuine** | **30.9%** (25/81) | **25.3%** (20/79) | +5.6pp | ISR marginally improves genuine rate |
| H1: Multi-premise conclusion embedding | 51.9% (42/81) | 70.9% (56/79) | -19.0pp | GRPO universal degradation |
| H7: Single premise = conclusion | **16.1%** (13/81) | **0%** (0/79) | +16.1pp | **ISR-specific gaming** |
| H3: Complexity without utility | 0% (0/81) | 3.8% (3/79) | -3.8pp | ISR eliminates this mode |
| **Total hacking** | **69.1%** (56/81) | **74.7%** (59/79) | -5.6pp | ISR slightly reduces total but shifts mode |

**Key finding**: ISR reward does not reduce overall hacking rate substantially (69.1% vs 74.7%). Instead, it **redistributes** hacking from H1 (multi-premise embedding, GRPO-universal) to H7 (single-premise duplication, ISR-specific). H7 is more extreme and more deceptive (both PR and ISR appear high).

## Table 2b: H7 Rate Across ISR β=0.1 Seeds

| Seed | H7 Rate | H1 Rate | Genuine Rate | ISR (proved) | Diagnosis |
|------|---------|---------|-------------|-------------|-----------|
| s42 | 16.1% (13/81) | 51.9% (42/81) | 30.9% (25/81) | 0.415 | Mixed — genuine + hacking |
| s43 | **96.7%** (59/61) | 0% | ~0% | 0.830 | **Near-total H7 collapse** |
| s44 | **86.5%** (77/89) | 0% | ~0% | 0.902 | **Near-total H7 collapse** |
| **3-seed mean** | **66.4%** | **17.3%** | **~10.3%** | 0.68 | **2/3 seeds meta-Goodhart** |

**Interpretation**: 
- s42 is the only seed with genuine structural improvement (~31% genuine proofs)
- s43/s44 discovered the "shortcut": single premise = conclusion → r_exec=1.0, ISR=1.0, maximum reward with zero reasoning
- The H7 strategy is ISR-specific: random β=0.1 produces 0% H7 across all samples
- ISR β=0.1 3-seed H7 total: 149/231 (64.5%)

## Table 2c: Aggregate Taxonomy Comparison (plan012, 160 samples each)

| Metric | ISR β=0.1 | Random β=0.1 | Delta |
|--------|-----------|-------------|-------|
| Genuine rate | 25.9% | 17.7% | +8.2pp |
| Conclusion embedding rate | 72.8% | 78.5% | -5.7pp |
| Complexity w/o utility rate | 0% | 3.8% | -3.8pp |
| **Total hacking rate** | **74.1%** | **82.3%** | **-8.2pp** |
| Genuine mean ISR | 0.672 | 0.343 | +0.329 |

Note: plan012 uses 160-sample aggregation; D044 strict taxonomy (Table 2a) uses per-seed eval_sta.py outputs. Numbers differ slightly due to sample composition and classification criteria.

## Table 2d: Cross-Logic H7 Comparison

| Condition | Logic | H7 Rate | PR | ISR (proved) | Source |
|-----------|-------|---------|----|-------------|--------|
| exec-only s42 | FOL | ~0%† | 0.93 | 0.132 | plan001-s42-r2 |
| ISR β=0.1 s42 | FOL | 16.1% | 0.81 | 0.415 | plan002-b01-s42 |
| ISR β=0.1 s43 | FOL | 96.7% | 0.61 | 0.830 | plan002-b01-s43 |
| ISR β=0.1 s44 | FOL | 86.5% | 0.89 | 0.902 | plan002-b01-s44 |
| Random β=0.1 s42 | FOL | 0% | 0.79 | 0.131 | plan018-b01-s42 |
| exec-only s42 | Prolog | 0% | 0.83 | 0.037 | plan006-exec-s42 |
| exec+STA s42 | Prolog | **100%** | 0.50 | 1.0 | plan006-sta-s42 |

† Exec-only H7 not explicitly measured but expected ~0% (no ISR incentive for single-premise strategy).

**Cross-logic finding**: Prolog exec+STA produces 100% H7 (vs FOL ISR β=0.1 max 96.7%). Simpler logic semantics → faster, more complete gaming. Prolog training saturated at step ~100 with PR=1.0, ISR=1.0, then eval shows 50% PR (memorization) with 100% H7 on proved samples.

## Table 2e: Full Hacking Mode Taxonomy (6 modes)

| Mode | Description | Where Observed | ISR-Specific? |
|------|------------|----------------|---------------|
| H1 | Multi-premise conclusion embedding | All conditions (GRPO universal) | No |
| H2 | Tautological collapse (2-component) | plan001-s44 (exec-only) | No |
| H3 | Complexity without utility | plan017 (random β=0.3) | No |
| H5 | Repetition collapse (max_tokens) | plan001-s43 (exec-only) | No |
| H6 | Format/structural collapse | plan002-b03 (ISR β=0.3) | Partial |
| H7 | Single premise = conclusion (ISR inflation) | plan002-b01 s43/s44, plan006-sta | **Yes** |

**H7 is the novel ISR-specific hacking mode**: It only appears when ISR is used as a reward signal. The strategy simultaneously maximizes exec reward (conclusion is trivially provable) and ISR (single component = ablating it destroys proof → ISR=1.0). Random reward never triggers H7 because random noise provides no structural shortcut signal.

---

## Pending Data

1. **Random β=0.1 s43/s44**: Needed to confirm 0% H7 holds across seeds for random control
2. **Prolog exec-only s43/s44**: Needed for cross-logic 3-seed comparison
3. **Prolog exec+STA s43/s44**: Would strengthen cross-logic H7 finding

## Notes for Paper

- Table 2a (strict per-seed) and Table 2c (aggregate) tell consistent stories but use different sample sizes/criteria; paper should use one as main table, other as supplement
- H7 is the key discriminative finding between ISR and random reward — zero in random, 64.5% across ISR β=0.1 seeds
- The "meta-Goodhart" narrative: ISR designed to detect hacking → ISR used as reward → models hack ISR itself via H7
- Per C006: Prolog exec-only low ISR (0.037) reflects redundant clause coding (repeated ground facts), NOT absence of reasoning. Must distinguish from exec+STA high ISR (1.0) which is genuine H7 gaming.
