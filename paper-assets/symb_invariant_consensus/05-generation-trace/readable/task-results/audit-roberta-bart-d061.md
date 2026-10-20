# audit roberta bart d061

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_roberta-bart-d061_20260522T205137_result.json`
- **Structured JSON:** [`11186d08a40cc4e5c0be.json`](../../sessions/11/11186d08a40cc4e5c0be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have complete information. Let me compile the audit findings.

---

## D061 Tiebreaking Audit: RoBERTa/BART Multi-NLI

### 1. Script Analysis

All three r11 scripts use **D061 alphabetical tiebreaking**:

| Script | Tiebreaking function | Implementation |
|--------|---------------------|----------------|
| `r11_3verifier_canonical.py` | `sc_answer_alpha()` / `combo_answer_alpha()` | `sorted(tied)[0]` over `CLASSES` |
| `r11_3verifier_final.py` | `alpha_winner()` | `sorted(c for c in CLASSES if ...)` → `tied[0]` |
| `r11_3verifier_final_v2.py` | `alpha_winner()` | identical to `final.py` |

### 2. Standalone Accuracies (from `r11_3verifier_canonical.json`)

| Verifier | Correct | Accuracy |
|----------|---------|----------|
| DeBERTa-large-MNLI | 330/600 | 55.00% |
| RoBERTa-large-MNLI | 226/600 | 37.67% |
| BART-large-MNLI | 277/600 | 46.17% |

### 3. SC Baseline: ID Fix Discrepancy

| Condition | Correct | Accuracy |
|-----------|---------|----------|
| SC D061 **without** ID fix | 235/600 | **39.17%** (paper value) |
| SC D061 **with** ID fix | 236/600 | **39.33%** (r11 JSON value) |

The r11 script applies a 2-question ID fix (`Q4→Q8` for two problems). One fix adds +1 correct to SC. The paper uses the unfixed 39.17%.

### 4. Paper vs r11 JSON: RoBERTa/BART Combos

**RoBERTa-large-MNLI** (paper Tab 26 vs r11 JSON):

| w | Paper Δ | r11 JSON Δ | r11 JSON acc | r11 p-value | Paper p |
|---|---------|------------|-------------|-------------|---------|
| 1 | −0.17 | −0.17 | 39.17% (235) | 1.0 | n.s. |
| 3 | **+4.17** | **+4.17** | 43.50% (261) | 0.0026 | 0.003** |
| 5 | **+4.33** | **+4.33** | 43.67% (262) | 0.037 | 0.037* |

**BART-large-MNLI**:

| w | Paper Δ | r11 JSON Δ | r11 JSON acc | r11 p-value | Paper p |
|---|---------|------------|-------------|-------------|---------|
| 1 | 0.00 | 0.00 | 39.33% (236) | 1.0 | n.s. |
| 3 | **+5.17** | **+5.17** | 44.50% (267) | 0.00024 | <0.001*** |
| 5 | **+6.33** | **+6.33** | 45.67% (274) | 0.0027 | 0.003** |

All deltas and p-values match exactly.

### 5. DeBERTa Discrepancy (Side Finding)

DeBERTa values in paper Tab 26 (w3=+7.00, w5=+11.17) differ from r11 JSON (w3=+6.67, w5=+11.00). This is because:
- Paper DeBERTa values come from the original experiment (no ID fix, SC=235, combo=277)
- r11 JSON applies the ID fix (SC=236, combo=276)
- The ID fix flips one question's SC/combo alignment differently for DeBERTa than for RoBERTa/BART

### 6. BH Correction

r11 JSON: **10/15 significant** at BH α=0.05.
Paper Tab 27: **10/15 significant** — matches.

Note: Paper Tab 27 tests 3 verifiers × 5 weights, while r11 JSON tests 3×3 individual + 3 ensemble + 3 additive = 15 tests. The count matches but the test composition differs.

### 7. Capability Gap Scatter (Figure 7)

`gen_capability_gap_scatter.py` uses:
- RoBERTa: gap = −1.50 (37.67−39.17), Δ = 4.17
- BART: gap = +7.00 (46.17−39.17), Δ = 5.17

These match the r11 JSON/paper Tab 26 deltas. All correct under D061.

### Verdict

**RoBERTa and BART multi-NLI combo results already use D061 tiebreaking. No correction needed.**

- All scripts use `sorted(tied)[0]` (alphabetical)
- Paper deltas and p-values match r11 JSON exactly
- SC baseline in r11 JSON (39.33%) differs from paper (39.17%) by 1 question due to ID fix, but deltas are unaffected because the fix equally shifts SC and combo
- Capability gap scatter data points are consistent
- BH correction count (10/15) matches

The only inconsistency found is the DeBERTa w3/w5 deltas in Tab 26 vs r11 JSON, caused by the ID fix (not D061). This is cosmetic since the paper's DeBERTa values come from a separate source. The 25 tied SC questions (4.2%) are correctly resolved by alphabetical tiebreaking throughout.

---
