# First-seen Type Locking Cascade Error Analysis (SF4 Evidence)

## Data Source
- **ZS**: `phase2_scierc_full_s1_v2.jsonl` (Qwen ZS SciERC S1) — 245 CF entities, 248 violations
- **FT**: `w5_lora_scierc_full_s1_eval.jsonl` (Qwen FT SciERC S1) — 21 CF entities, 22 violations

## Methodology
Simulates OntoCoDec's entity registry: walks entity list then relations in generation order.
First occurrence of each span locks its type. Any subsequent occurrence with a different type = CF violation.
Each violation classified by comparing first-seen vs attempted type against gold annotations.

## Key Findings

### ZS (248 violations, 245 unique entities, 167/551 docs)
| Classification | Count | Pct | Description |
|---|---|---|---|
| no_gold_match | 144 | 58.1% | Entity not in gold (hallucinated) |
| correct_lock | 45 | 18.1% | First-seen correct, blocked wrong type |
| both_wrong | 41 | 16.5% | Neither type matches gold |
| cascade_error | 18 | 7.3% | First-seen WRONG, blocked correct type |
| legitimate_ambiguity | 0 | 0.0% | Both types valid in gold |

### FT (22 violations, 21 unique entities, 20/551 docs)
| Classification | Count | Pct |
|---|---|---|
| correct_lock | 14 | 63.6% |
| no_gold_match | 5 | 22.7% |
| both_wrong | 3 | 13.6% |
| cascade_error | 0 | 0.0% |

### Generic Involvement (ZS)
- Specific→Generic: 127 (51.2%) — dominant pattern
- Specific→Specific: 91 (36.7%)
- Generic→Specific: 30 (12.1%)

## Narrative for Paper
1. Only 7.3% of ZS CF violations are true cascade errors (first-seen wrong, correct type blocked)
2. 18.1% are *beneficial* constraints (correct_lock) — ratio 2.5:1 in favor of locking
3. 58.1% involve hallucinated entities — root cause is model weakness, not constraint mechanism
4. FT **completely eliminates** cascade errors (0/22), confirming fine-tuning resolves the issue
5. Dominant pattern is Specific→Generic (51.2%), reflecting ZS model's Generic overuse

## Output Files
- `/root/schema_semantic_constrained_ie/outputs/cf_cascade_analysis_qwen_zs_scierc_s1.json`
- `/root/schema_semantic_constrained_ie/outputs/cf_cascade_analysis_qwen_ft_scierc_s1.json`
