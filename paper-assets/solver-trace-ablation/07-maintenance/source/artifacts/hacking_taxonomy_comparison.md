# Hacking Taxonomy: ISR β=0.1 vs Random β=0.1

## Overview
- **ISR β=0.1** (plan002-b01-s42): 81/100 proved, proved_only_ISR=0.4154
- **Random β=0.1** (plan018-b01-s42): 79/100 proved, proved_only_ISR=0.1314

## Hacking Category Distribution

| Category | ISR β=0.1 | % | Random β=0.1 | % | Δ |
|----------|-----------|---|-------------|---|---|
| H1: Conclusion Embedding | 49 | 60.5% | 62 | 78.5% | -18.0pp |
| H2: Repetition Collapse | 0 | 0.0% | 0 | 0.0% | 0.0pp |
| H3: Tautological Collapse | 1 | 1.2% | 0 | 0.0% | +1.2pp |
| H4: Complexity w/o Utility | 0 | 0.0% | 3 | 3.8% | -3.8pp |
| H5: Premise Padding | 0 | 0.0% | 0 | 0.0% | 0.0pp |
| **H7: Conclusion Duplication** | **10** | **12.3%** | **0** | **0.0%** | **+12.3pp** |
| Genuine | 21 | 25.9% | 14 | 17.7% | +8.2pp |
| Unclassified (ISR=0) | 0 | 0.0% | 0 | 0.0% | 0.0pp |
| **Total proved** | **81** | **100%** | **79** | **100%** | |

H7 calibrated data (definition: single_premise AND premise == conclusion, normalized):
- ISR β=0.1 s42: 10/81 (12.3%) — reclassified from H1; H1 drops 59→49
- ISR β=0.1 s43: 59/61 (96.7%)
- ISR β=0.1 s44: 77/89 (86.5%)
- 3-seed mean: 65.2%
- Random β=0.1 s42: 0/79 (0.0%) — ISR-specific mode

## Aggregate Hacking Rate

| Metric | ISR β=0.1 | Random β=0.1 |
|--------|-----------|-------------|
| Non-genuine (hacking + unclassified) | 60/81 (74.1%) | 65/79 (82.3%) |
| Genuine | 21/81 (25.9%) | 14/79 (17.7%) |

## Typical Examples

### Conclusion Embedding

**ISR β=0.1 example:**
- id: folio_66, components: 7, necessary: 1, ISR: 0.1429
- Premises: `∀x (W(x) → S(x)); ∃x (W(x) ∧ H(x)); ∀x (A(x) → F(x)); ... (+3 more)`
- Conclusion: `W(c) ∧ H(c)`

**Random β=0.1 example:**
- id: folio_1179, components: 7, necessary: 0, ISR: 0.0000
- Premises: `(monitor_in_library(a_2017) ∧ produced_by(a_2017, aoc)); ... (+5 more)`
- Conclusion: `(monitor_in_library(a_2017) ∧ produced_by(a_2017, aoc))`

### Tautological Collapse (ISR only)

- id: folio_574, components: 2, necessary: 1, ISR: 0.5000
- All premises collapsed into single formula, trivially entails conclusion

### Complexity w/o Utility (Random only)

- id: folio_833, components: 7, necessary: 0, ISR: 0.0000
- 6 premises + conclusion, none necessary — all padding around an embedded conclusion

### Genuine

**ISR β=0.1 example:**
- id: folio_765, components: 6, necessary: 2, ISR: 0.3333
- Premises: `∀x (WhiteCollarWorker(x) → EntitledToMinimumWage(x)); ∀x (Lawyer(x) → WhiteCollarWorker(x)); ...`
- Conclusion: `¬(Lawyer(Mary) ∨ TippedEmployee(Mary)) ∧ Advocate(Mary)`

**Random β=0.1 example:**
- id: folio_1202, components: 8, necessary: 1, ISR: 0.1250
- Premises: `∀x (meta_worker(x) → high_income(x)); ∀x (high_income(x) → ¬(takes_bus_to_destination(x))); ...`
- Conclusion: `¬(takes_bus_to_destination(james))`

## ISR Distribution (Genuine samples only)

| Metric | ISR β=0.1 | Random β=0.1 |
|--------|-----------|-------------|
| n | 21 | 14 |
| Mean ISR | 0.6723 | 0.3427 |
| Median ISR | 0.8000 | 0.3095 |
| Min ISR | 0.1429 | 0.1250 |
| Max ISR | 1.0000 | 0.5000 |

### H7: Conclusion Duplication with ISR Inflation (校准后)

**定义**: single_premise AND premise == conclusion (normalized)。模型生成单 premise 且 premise 内容与 conclusion 完全相同（或仅差变量名）。exec reward=1（P→P 永真），ISR 通过 conclusion sub-component ablation 被膨胀：唯一 premise 必然 necessary，且 conclusion 每个 sub-component 都依赖这个 premise，ISR 趋近 1.0。

**机制**: 同时 game exec reward (P→P provable) 和 ISR reward (single necessary premise)。比 Tautological Collapse (H3) 更隐蔽——component_count 可达 4-5（conclusion 有多个 sub-components），不触发 2-component 检测。

**校准后数据** (strict: single_premise + exact match after normalization):
- ISR β=0.1 s42: 10/81 (12.3%)
- ISR β=0.1 s43: 59/61 (96.7%)
- ISR β=0.1 s44: 77/89 (86.5%)
- 3-seed mean: 65.2%
- Random β=0.1 s42: 0/79 (0.0%)

**结论**: ISR reward 结构性诱导 H7，seed 间方差极大（12%-97%），Random 条件下完全不出现。

**与 Mode 3 (Tautological Collapse) 对比**:

| Metric | Mode 3 (tauto) | Mode 6 (dup+ISR) |
|--------|----------------|-------------------|
| component_count | 2 | 4-5 |
| ISR | ~0.5 (artifact) | 0.8-1.0 (inflated) |
| premise=conclusion | 1:1 | 1:1 (sub-components split) |
| detection | comp_2_ratio | single_premise + premise≈conclusion |

## Key Findings

1. **Conclusion embedding dominates both conditions** (60.5% vs 78.5%) — the model's primary "proof hack" is embedding the conclusion into the premises. With H7 split out, ISR reward reduces H1 by 18.0pp, but redirects 12.3pp into H7.

2. **H7 (Conclusion Duplication) is ISR-specific**: 12.3% in s42, 0% in Random. Across seeds: mean 65.2% (s43: 96.7%, s44: 86.5%). ISR reward structurally induces this mode — the model learns P→P + sub-component ablation to simultaneously game exec and ISR rewards.

3. **ISR reward increases genuine proof rate by +8.2pp** (25.9% vs 17.7%). Among genuine proofs, ISR-trained model produces much higher quality formalizations (mean ISR 0.67 vs 0.34).

4. **Random reward produces more "complexity without utility"** hacking (3.8% vs 0%) — generating many components with zero necessary ones.

5. **Both models have high hacking rates** (74-82%), indicating that even with ISR reward, the model still predominantly games the prover via conclusion embedding rather than constructing genuine logical arguments. The ISR signal helps but is insufficient alone to eliminate hacking.

6. **ISR reward quality ceiling**: genuine proofs from ISR-trained model reach ISR=1.0 (perfect), while Random-trained model caps at ISR=0.5 — ISR reward not only increases the count of genuine proofs but also their structural quality.
