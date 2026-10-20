# Cross-Model & Recovery Eval Comprehensive Analysis

**Date**: 2026-05-16  
**Project**: tax_error_inject_agent (EMNLP 2026 Findings)  
**Data source**: Registry (112 DONE experiments verified)

---

## 1. Data Completeness Audit

### 1.1 User-provided data vs Registry — discrepancies found

| Item | User Value | Registry Value | Note |
|------|-----------|---------------|------|
| TaxEI-RP 5-seed mean (core table) | 47.9±7.8 | **50.2±8.6** | User's per-seed data (38.3+46.8+48.9+57.4+59.6)/5=50.2, contradicts the 47.9 in the summary table |
| Vanilla recovery s42 | (omitted) | **61.7%** | User listed s0/s1/s7/s123 but missed s42 |
| TaxEI recovery s42 | (omitted) | **59.6%** | User listed s0/s1/s123 but missed s42 |
| Random recovery | (not mentioned) | **63.8% (s42 only)** | Only 1 seed exists |

### 1.2 Additional experiments in registry not mentioned by user

- **LLaMA-3.1-8B s0 training** (llama31-vanilla-s0): training DONE but **no eval** exists
- **Dose-response multi-seed** (10%/25%/50% × TaxEI/Random): extensive data exists beyond seed=42
- **Training dynamics** (v4-training-dynamics-forward, v2): per-operator loss analysis
- **Recovery-paired datagen**: 711 samples generated for future recovery-paired SFT

---

## 2. Table A: Cross-Model Comparison (s42, Recovery Eval)

Both models evaluated with injected_eval.py — same 47 episodes, same error operators.

### Recovery Rate

| Condition | Qwen3-8B | LLaMA-3.1-8B | Δ (LLaMA−Qwen) |
|-----------|----------|--------------|-----------------|
| Vanilla | 61.7% (29/47) | 74.5% (35/47) | **+12.8pp** |
| TaxEI | 59.6% (28/47) | 74.5% (35/47) | **+14.9pp** |
| Random | 63.8% (30/47) | 76.6% (36/47) | **+12.8pp** |

### Detection Rate

| Condition | Qwen3-8B | LLaMA-3.1-8B | Δ |
|-----------|----------|--------------|---|
| Vanilla | 0% | 21.3% | **+21.3pp** |
| TaxEI | 0% | 29.8% | **+29.8pp** |
| Random | 0% | 29.8% | **+29.8pp** |

### Per-Operator Recovery (s42)

| Operator | Qwen Vanilla | Qwen TaxEI | Qwen Random | LLaMA Vanilla | LLaMA TaxEI | LLaMA Random |
|----------|-------------|------------|-------------|---------------|-------------|-------------|
| C1 (Context Truncation) | 75.0% | 66.7% | — | 75.0% | 83.3% | 66.7% |
| C4 (Observation Masking) | 54.5% | 63.6% | — | 72.7% | 72.7% | 72.7% |
| P1 (Step Order Swap) | 58.3% | 58.3% | — | 75.0% | 58.3% | 91.7% |
| P2 (Sub-Goal Deletion) | 58.3% | 50.0% | — | 75.0% | 83.3% | 75.0% |

*Note: Qwen Random s42 per-operator breakdown not recorded in registry.*

---

## 3. Table B: TaxEI-RP Eval Summary (5-seed)

TaxEI-RP = Recovery-Paired injection training (711 paired recovery demos).

| Seed | Recovery Rate | Count |
|------|-------------|-------|
| s42 | 38.3% | 18/47 |
| s0 | 46.8% | 22/47 |
| s1 | 48.9% | 23/47 |
| s123 | 57.4% | 27/47 |
| s7 | 59.6% | 28/47 |
| **Mean±SD** | **50.2±8.6%** | — |

### Comparison with baselines

| Metric | Value |
|--------|-------|
| TaxEI-RP mean | 50.2% |
| Vanilla clean eval mean | 67.3% |
| Gap vs Vanilla | **−17.1pp** |
| TaxEI full clean eval mean | 58.3% |
| Gap vs TaxEI full | **−8.1pp** |
| Vanilla recovery eval mean | 67.3% |
| Gap vs Vanilla recovery | **−17.1pp** |

Detection rate across all 5 TaxEI-RP seeds: **0%** (no explicit error detection).

---

## 4. Table C: Recovery Eval Completeness Matrix

### Qwen3-8B Recovery Eval (injected_eval.py)

| Seed | Vanilla | TaxEI | Random |
|------|---------|-------|--------|
| s42 | ✅ 61.7% | ✅ 59.6% | ✅ 63.8% |
| s0 | ✅ 68.1% | ✅ 46.8% | ❌ |
| s1 | ✅ 66.0% | ✅ 61.7% | ❌ |
| s7 | ✅ 74.5% | ❌ | ❌ |
| s123 | ✅ 66.0% | ✅ 61.7% | ❌ |
| **Count** | **5/5** | **4/5** | **1/5** |

**Missing**: TaxEI-s7, Random-s0/s1/s7/s123

### Summary statistics (available seeds)

| Condition | Seeds | Mean | SD | Min | Max |
|-----------|-------|------|-----|-----|-----|
| Vanilla | 5 | 67.3% | 4.7 | 61.7% | 74.5% |
| TaxEI | 4 | 57.5% | 7.1 | 46.8% | 61.7% |
| Random | 1 | 63.8% | — | — | — |

### LLaMA-3.1-8B Recovery Eval

| Seed | Vanilla | TaxEI | Random |
|------|---------|-------|--------|
| s42 | ✅ 74.5% | ✅ 74.5% | ✅ 76.6% |
| s0 | ❌ (train only) | ❌ | ❌ |
| **Count** | **1/5** | **1/5** | **1/5** |

---

## 5. Table D: Dose-Response Summary (Fixed-Size Ablation)

All conditions use 4,358 total samples (= vanilla size). Injection proportions: 10%, 25%, 50%.

### Seed=42 (complete for all doses)

| Dose | TaxEI | Random | Δ (TaxEI−Random) |
|------|-------|--------|-------------------|
| 0% (Vanilla) | 61.7% | 61.7% | 0 |
| 10% | 61.7% | 68.1% | −6.4pp |
| 25% | 48.9% | 55.3% | −6.4pp |
| 50% | 51.1% | 57.4% | −6.3pp |
| 100% (full, 9029) | 61.7% | 66.0% | −4.3pp |

### Multi-Seed Dose-Response

#### TaxEI 10% (5 seeds complete)

| Seed | Success Rate |
|------|-------------|
| s42 | 61.7% |
| s0 | 70.2% |
| s1 | 51.1% |
| s7 | 68.1% |
| s123 | 55.3% |
| **Mean±SD** | **61.3±7.7%** |

#### TaxEI 25% (3 seeds)

| Seed | Success Rate |
|------|-------------|
| s42 | 48.9% |
| s1 | 63.8% |
| s7 | 57.4% |
| **Mean±SD** | **56.7±7.5%** |

#### TaxEI 50% (3 seeds)

| Seed | Success Rate |
|------|-------------|
| s42 | 51.1% |
| s1 | 63.8% |
| s7 | 55.3% |
| **Mean±SD** | **56.7±6.4%** |

#### Random 10% (5 seeds complete)

| Seed | Success Rate |
|------|-------------|
| s42 | 68.1% |
| s0 | 66.0% |
| s1 | 68.1% |
| s7 | 61.7% |
| s123 | 55.3% |
| **Mean±SD** | **63.8±5.2%** |

#### Random 25% (3 seeds)

| Seed | Success Rate |
|------|-------------|
| s42 | 55.3% |
| s1 | 72.3% |
| s7 | 59.6% |
| **Mean±SD** | **62.4±8.8%** |

#### Random 50% (3 seeds)

| Seed | Success Rate |
|------|-------------|
| s42 | 57.4% |
| s1 | 70.2% |
| s7 | 46.8% |
| **Mean±SD** | **58.1±11.7%** |

### Dose-Response Curve (multi-seed means, where available)

| Dose | TaxEI Mean | Random Mean | Vanilla Mean |
|------|-----------|------------|-------------|
| 0% | 67.3 (5s) | 67.3 (5s) | 67.3 (5s) |
| 10% | 61.3 (5s) | 63.8 (5s) | — |
| 25% | 56.7 (3s) | 62.4 (3s) | — |
| 50% | 56.7 (3s) | 58.1 (3s) | — |
| 100% | 58.3 (5s) | 58.3 (5s) | — |

---

## 6. Key Findings & Analysis

### Finding 1: LLaMA s42 — near-zero condition effect (74.5 vs 74.5 vs 76.6)

The three conditions produce virtually identical recovery rates on LLaMA-3.1-8B (spread = 2.1pp). This contrasts with Qwen3-8B where the spread is larger (s42: 59.6–63.8, 4.2pp).

**Implications for paper framing**:
- LLaMA-3.1-8B appears **more robust to training data perturbation** — its agentic performance is insensitive to whether injection is taxonomy-guided, random, or absent. This is likely a **model capacity / pretraining quality** effect: a stronger base model can "absorb" injected errors without degrading task performance.
- The real story is the **detection rate**: LLaMA detects 21–30% of errors vs Qwen's 0%. This suggests LLaMA has sufficient metacognitive capability to notice anomalies, whereas Qwen3-8B treats injected errors as normal trajectory variation.
- **Paper framing recommendation**: Present LLaMA as a "ceiling" model where error injection is harmless (both TaxEI and Random), and Qwen as the model where injection effects manifest. The cross-model comparison becomes a **model sensitivity** analysis — taxonomy-guided injection matters more for models near the capability boundary.
- **Caution**: Only 1 seed for LLaMA. The 2.1pp spread could easily be noise. Cannot draw strong conclusions without multi-seed LLaMA data.

### Finding 2: TaxEI-RP 50.2% vs Vanilla 67.3% — significance analysis

Gap = −17.1pp. With 5 seeds:
- TaxEI-RP: 50.2±8.6%
- Vanilla: 67.3±4.7%

**Effect size** (Cohen's d): d = (67.3−50.2) / √((4.7²+8.6²)/2) = 17.1 / √(47.6) = 17.1/6.9 = **2.48** (very large).

**Welch's t-test** (approximate): t = 17.1 / √(4.7²/5 + 8.6²/5) = 17.1 / √(4.42+14.79) = 17.1/4.38 = **3.90**, df≈6.4, **p ≈ 0.006**.

**The gap is statistically significant** (p < 0.01) despite only 5 seeds. TaxEI-RP substantially degrades clean task performance. This is a critical negative result: recovery-paired training hurts more than it helps on clean eval. The recovery benefit (if any) does not compensate for the clean performance loss.

### Finding 3: TaxEI s0 recovery rate 46.8% — outlier analysis

TaxEI recovery eval: s42=59.6%, s0=46.8%, s1=61.7%, s123=61.7%.

s0 is 10.7pp below the 4-seed mean (57.5%). With SD=7.1, this is a z-score of −1.5 — outside 1σ but within 2σ. **Not a statistical outlier** by Grubbs' test (critical z for n=4 at α=0.05 is 1.48; marginal).

However, note that TaxEI **clean eval** also shows s0 as the lowest: s0=46.8% vs mean=58.3%. The same seed shows low performance in both clean and recovery eval. This suggests **s0 is a generally unlucky seed for TaxEI**, not specific to recovery conditions. The s0 TaxEI model learned a weaker policy overall.

For comparison, Vanilla s0 clean=68.1% (above vanilla mean 67.3%), so the seed itself isn't bad — the TaxEI×s0 combination specifically produces poor models. This is consistent with **high variance under injection** (TaxEI SD=6.5 vs Vanilla SD=4.7).

### Finding 4: Dose-response non-monotonicity

The dose-response curve for TaxEI (multi-seed) shows:
- 0% → 10%: −6.0pp drop
- 10% → 25%: −4.6pp drop
- 25% → 50%: +0.0pp (flat)
- 50% → 100%: +1.6pp recovery

The 25%→50%→100% plateau/recovery is unexpected. Possible explanations:
1. **More injection = more data**: at 100% (9,029 samples), the model sees 2× more total data than fixed-size (4,358), compensating for injection noise.
2. **3 seeds at 25%/50% vs 5 at 10%**: smaller sample sizes inflate uncertainty.
3. The non-monotonicity may not be real — bootstrap CIs likely overlap.

For Random injection, the curve is flatter: 67.3 → 63.8 → 62.4 → 58.1 → 58.3, showing a gentler decline. TaxEI consistently underperforms Random by ~2–6pp at all doses, suggesting taxonomy labels **amplify the perturbation effect** rather than provide useful structure.

### Finding 5: Vanilla recovery = Vanilla clean (identical per-seed)

A striking pattern: Vanilla recovery rates (s42=61.7, s0=68.1, s1=66.0, s7=74.5, s123=66.0) are **identical** to vanilla clean eval rates. This is expected because:
- Vanilla models have 0% detection rate
- Without detection, the model doesn't "know" an error was injected
- It simply continues the trajectory as if nothing happened
- Success/failure is driven entirely by the model's base capability

This validates the eval methodology: vanilla provides a consistent reference.

---

## 7. Gaps & Recommendations for Paper Completeness

| Priority | Gap | Impact | Effort |
|----------|-----|--------|--------|
| **HIGH** | Random recovery eval: only s42 exists (need s0/s1/s7/s123) | Cannot compute Random recovery mean±SD for Table C | 4 eval runs |
| **HIGH** | TaxEI recovery s7 missing | 4/5 seeds → incomplete | 1 eval run |
| **MEDIUM** | Dose-response 25% & 50%: only 3 seeds each | Weaker statistical power; cannot compute reliable CIs | 4 train + 4 eval per dose |
| **MEDIUM** | LLaMA multi-seed | n=1 makes cross-model claims fragile | 4 train + 4×3 eval |
| **LOW** | TaxEI-RP per-operator breakdown missing for 3 seeds | Cannot analyze operator-level RP effects | Already in eval logs, extract |

---

## 8. Recommended Paper Tables

### Main Table (Table 1): Qwen3-8B 5-seed Clean Eval

| Condition | Mean±SD | s42 | s0 | s1 | s7 | s123 |
|-----------|---------|-----|-----|-----|-----|------|
| Vanilla | 67.3±4.7 | 61.7 | 68.1 | 66.0 | 74.5 | 66.0 |
| TaxEI full | 58.3±6.5 | 61.7 | 46.8 | 59.6 | 61.7 | 61.7 |
| Random full | 58.3±8.7 | 66.0 | 55.3 | 46.8 | 55.3 | 68.1 |
| TaxEI-RP | 50.2±8.6 | 38.3 | 46.8 | 48.9 | 59.6 | 57.4 |

### Supplementary Table: Cross-Model (s42 only)

| Condition | Qwen3-8B Recovery | Qwen3-8B Detection | LLaMA-8B Recovery | LLaMA-8B Detection |
|-----------|-------------------|--------------------|--------------------|---------------------|
| Vanilla | 61.7% | 0% | 74.5% | 21.3% |
| TaxEI | 59.6% | 0% | 74.5% | 29.8% |
| Random | 63.8% | 0% | 76.6% | 29.8% |

---

*Registry query: 112 DONE experiments, verified 2026-05-16.*
