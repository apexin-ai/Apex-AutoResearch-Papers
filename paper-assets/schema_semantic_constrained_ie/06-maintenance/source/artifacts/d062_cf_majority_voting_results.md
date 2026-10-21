# d062: CF Majority Voting Post-hoc Correction Results

## Method
Per-document majority voting: for each unique entity text (case-insensitive), count type occurrences across entities list and all relation head/tail positions. If one type has strict majority, unify all occurrences to that type. Ties preserve original types.

## Results: Before vs After Majority Voting

### CF Violations (cross-field consistency)

| Condition | CF Before | CF After | Reduction |
|---|---|---|---|
| Qwen SciERC ZS | 245 | 201 | -18.0% |
| Llama SciERC ZS | 162 | 123 | -24.1% |
| Qwen DocRED ZS | 518 | 21 | -95.9% |
| Llama DocRED ZS | 1358 | 107 | -92.1% |
| Qwen SciERC FT | 21 | 12 | -42.9% |
| Llama SciERC FT | 8 | 4 | -50.0% |
| Qwen DocRED FT | 48 | 3 | -93.8% |
| Llama DocRED FT | 41 | 2 | -95.1% |

### DR Violations (domain-range)

| Condition | DR Before | DR Rate Before | DR After | DR Rate After | Delta |
|---|---|---|---|---|---|
| Qwen SciERC ZS | 16 | 0.93% | 56 | 3.24% | +250% |
| Llama SciERC ZS | 1 | 0.08% | 31 | 2.36% | +3000% |
| Qwen DocRED ZS | 1770 | 10.21% | 2543 | 14.66% | +43.7% |
| Llama DocRED ZS | 418 | 2.55% | 2725 | 16.65% | +551.7% |
| Qwen SciERC FT | 0 | 0.00% | 8 | 0.71% | +inf |
| Llama SciERC FT | 1 | 0.09% | 4 | 0.37% | +300% |
| Qwen DocRED FT | 2 | 0.01% | 68 | 0.44% | +3300% |
| Llama DocRED FT | 33 | 0.21% | 81 | 0.50% | +145.5% |

### Corrections Made

| Condition | Corrections | CF Entities Before | CF Entities After |
|---|---|---|---|
| Qwen SciERC ZS | 44 | 245 | 201 |
| Llama SciERC ZS | 40 | 162 | 123 |
| Qwen DocRED ZS | 955 | 2670 | 2131 |
| Llama DocRED ZS | 2862 | 3824 | 2348 |
| Qwen SciERC FT | 9 | 21 | 12 |
| Llama SciERC FT | 5 | 8 | 4 |
| Qwen DocRED FT | 86 | 74 | 21 |
| Llama DocRED FT | 73 | 69 | 17 |

## Key Findings

1. **CF reduction is effective**: Majority voting reduces CF violations across all conditions, with DocRED seeing the largest absolute and relative reductions (92-96%).

2. **DR increases substantially in every condition**: Majority voting blindly unifies entity types without checking domain/range constraints, so the "winning" type often violates the allowed (head_type, tail_type) pairs for specific relations. The DR increase is severe: up to 551% relative increase (Llama DocRED ZS).

3. **SciERC CF reduction is modest** (18-24% for ZS): SciERC is sentence-level, so many CF cases involve tied counts (2 types each appearing once), which the conservative tie-breaking rule skips.

4. **FT models have very low baseline CF**: FT already learns consistent typing, so majority voting has little room to improve (8-48 CF violations before correction).

5. **Conclusion: Naive majority voting is not viable as a post-hoc CF fix** because it trades CF for DR. A constraint-aware approach (e.g., the w1_cf_fallback method that checks domain/range before overriding) is necessary to avoid this trade-off.

## Files

- Script: `/root/schema_semantic_constrained_ie/scripts/cf_majority_voting.py`
- Corrected outputs: `outputs/*_cf_corrected.jsonl` (8 files)
- Correction reports: `outputs/cf_correction_report_*.json` (8 files)
- Violation reports: `outputs/violation_report_*_cf_corrected.json` (8 files)
