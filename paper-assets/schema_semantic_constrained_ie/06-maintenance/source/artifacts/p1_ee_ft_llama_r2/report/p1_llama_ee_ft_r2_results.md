# P1 EE FT R2 Results: Llama-8B LoRA WikiEvents (Schema Fix + RepPenalty)

## Changes from R1
- **Schema fix**: `ontology_compiler.py` line 294: `required: ["entities", "events"]` → `required: ["events"]`
- **repetition_penalty=1.2** added to all generate() calls via new `--repetition_penalty` CLI arg
- Model: same merged checkpoint (`llama_8b_lora_wikievents_merged`), no retraining

## Parse Rate

| Mode | Parsed | Total | Rate |
|------|--------|-------|------|
| Unconstrained | 20 | 20 | 100% |
| Constrained (full_s1) | 20 | 20 | 100% |

## Extraction F1

| Metric | Unconstrained | Constrained (full_s1) |
|--------|--------------|----------------------|
| Entity F1 | 0.0000 | 0.0000 |
| Trigger P | 0.2563 | 0.2899 |
| Trigger R | 0.2971 | 0.2510 |
| Trigger F1 | 0.2752 | 0.2691 |
| Argument P | 0.1375 | 0.1349 |
| Argument R | 0.0783 | 0.0665 |
| Argument F1 | 0.0998 | 0.0891 |

Entity F1 = 0 because FT data only has events (no entity annotations), so model does not generate entities.

## Violation Rates

| Violation Type | Unconstrained | Constrained (full_s1) |
|---------------|--------------|----------------------|
| ET (Entity Type) | 0.0% | 0.0% |
| EV (Event Vocab) | 4.5% (14/308) | 0.0% (0/217) |
| RoV (Role Vocab) | 8.8% (33/377) | 0.0% (0/255) |
| AC (Arg Constraint) | 3.5% (13/377) | 0.8% (2/255) |
| CF (Cross-Field) | ~0% (1) | ~0% (3) |
| **Go/No-go (RoV+AC)** | **12.2%** | **0.78%** |

## Key Findings
1. **Schema fix resolved 100% parse failure** from R1 (was 0% due to grammar requiring `entities` field)
2. **Constrained decoding eliminates EV and RoV violations** (4.5%→0%, 8.8%→0%)
3. **AC violations reduced 4.4x** (3.5%→0.8%)
4. **Go/No-go metric: 15.6x improvement** (12.2%→0.78%)
5. Trigger/Argument F1 comparable between modes (constrained slightly lower, expected from vocabulary restriction)
6. repetition_penalty=1.2 successfully prevents repetitive generation (no truncation observed)

## Output Files
- `outputs/ee_llama_ft_wikievents_unconstrained_r2.jsonl`
- `outputs/ee_llama_ft_wikievents_full_s1_r2.jsonl`
- `outputs/eval_report_llama_unconstrained_r2.json`
- `outputs/eval_report_llama_full_s1_r2.json`
- `outputs/violation_report_llama_ft_unconstrained_r2.json`
- `outputs/violation_report_llama_ft_full_s1_r2.json`
