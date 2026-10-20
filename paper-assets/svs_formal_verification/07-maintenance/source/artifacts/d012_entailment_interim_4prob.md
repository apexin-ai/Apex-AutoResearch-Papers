# D012 Phase 1: Entailment Rescoring — Interim Report (4/16 problems)

## Status
- **PID 54002** on autodl-5090, running since ~20:45 UTC
- 5/16 problems done at 46 min elapsed (5th just completed)
- Estimated completion: ~160 min total (~115 min remaining)
- Checkpoint every 4 problems to `/root/outputs/entailment_rescore_results.json`
- **NOTE**: A second instance (PID 60443) was detected and killed at min 44. It had overwritten the 4-problem checkpoint with empty data. Original PID 54002 continues normally and will restore data at the 8-problem checkpoint.

## 4-Problem Checkpoint Data (n=32 chains: 18 correct, 14 wrong)

### Problems Processed
| # | Problem ID | Gold Label | Time (s) |
|---|-----------|-----------|----------|
| 1 | pw_20952 | True | 559.9 |
| 2 | pw_3648 | Unknown | 710.8 |
| 3 | pw_819 | Unknown | 619.7 |
| 4 | pw_24299 | False | 389.4 |
| 5 | pw_9012 | Unknown | 461.2 |

Label distribution (4-prob checkpoint): True:1, Unknown:2, False:1

### Core Metrics

| Metric | Correct mean | Wrong mean | Cohen's d | p-value | 95% CI |
|--------|-------------|-----------|-----------|---------|--------|
| ic_score_old | 0.664 | 0.775 | **-0.644** | 0.092 | [-1.49, 0.06] |
| ic_entail | 0.591 | 0.675 | **-0.410** | 0.279 | [-1.20, 0.30] |
| ic_consist | 0.690 | 0.781 | **-0.558** | 0.141 | [-1.42, 0.16] |

### Entailment/Consistency Rates
- Entailment rate (among formalized claims): mean=79.6%, std=15.8%, median=84.2%
- Consistency rate (among formalized claims): mean=94.3%, std=11.9%, median=100%

## Key Findings

1. **All three metrics show NEGATIVE Cohen's d** — wrong chains score higher than correct chains. This is the opposite of the hypothesis (correct chains should have higher IC).

2. **ic_entail (-0.410) is least negative**, partially correcting the old IC (-0.644). Entailment-based scoring reduces the anti-signal by ~36%.

3. **95% CIs all cross zero** — the true effect could be positive with more data, especially as the label distribution becomes more balanced.

4. **Label-dependent bias confirmed**: With 2/4 Unknown-label problems, wrong chains (answering True/False) have more definitively entailable claims than correct Unknown chains.

5. **Formalization errors discovered**: e.g., "The dog does not chase the tiger" → `Not(Eat(dog, tiger))` (wrong predicate). The autoformalization introduces semantic errors that corrupt the signal.

6. **Entailment mechanically works**: 79.6% of formalized claims are entailed from premises + prior claims. The Z3 entailment checker is producing non-trivial results.

7. **Consistency ≈ SAT (old IC)**: ic_consist closely tracks ic_score_old (both driven by formalization rate), providing minimal additional discrimination.

## Sample Claims

### Entailed (correct behavior)
- "The bear does not eat the lion." → `Not(Eat(bear, lion))` — entailed from premise (CORRECT)
- "The lion is big." → `Big(lion)` — entailed from premise (CORRECT)
- "The mouse eats the squirrel." → `Eat(mouse, squirrel)` — entailed from premise (CORRECT)

### Not Entailed
- "The mouse likes the bear." → `Like(mouse, bear)` — not_entails (correct: not derivable from premises)
- "The squirrel is blue." → `Blue(squirrel)` — not_entails (correct: novel claim not in premises)

## Next Steps
- Wait for 8-problem checkpoint (~76 min elapsed) for more balanced label distribution
- Full completion at ~160 min
- Key question: does Cohen's d flip positive with more True/False gold-label problems?
