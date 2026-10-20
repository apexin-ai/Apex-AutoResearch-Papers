# EE FT Cross-Field Consistency (CF) Violation Results

## Definition

CF violation = same entity text appears with different entity types across different event arguments within the same document. Entity text is normalized (lowercase, stripped) before comparison.

## Results

| Model | Condition | Total Args | Unique Entities | CF Entities | CF Rate per Arg (%) | CF Rate per Entity (%) | Docs with CF |
|-------|-----------|-----------|-----------------|-------------|---------------------|------------------------|--------------|
| Qwen3-8B FT | Unconstrained | 261 | 206 | 2 | 0.77 | 0.97 | 2/20 |
| Qwen3-8B FT | Constrained | 339 | 261 | 3 | 0.89 | 1.15 | 2/20 |
| Llama-3.1-8B FT | Unconstrained | 298 | 222 | 1 | 0.34 | 0.45 | 1/20 |
| Llama-3.1-8B FT | Constrained | 255 | 199 | 3 | 1.18 | 1.51 | 2/20 |

Note: Llama unconstrained had 79 malformed arguments (bare strings instead of dicts) that were skipped; 298 + 79 = 377 matches the bootstrap CI total_args count.

## CF Violation Examples

### Qwen Unconstrained (2 CF entities)
| Doc ID | Entity Text | Conflicting Types |
|--------|-------------|-------------------|
| K0C041O37 | drone | VEH, WEA |
| wiki_mass_car_bombings_0_news_9 | colombia | GPE, PER |

### Qwen Constrained (3 CF entities)
| Doc ID | Entity Text | Conflicting Types |
|--------|-------------|-------------------|
| JC002YBW0 | tsarnaev | LOC, PER |
| JC002YBW0 | silva | LOC, PER |
| wiki_ied_bombings_5_news_3 | police | ORG, PER |

### Llama Unconstrained (1 CF entity)
| Doc ID | Entity Text | Conflicting Types |
|--------|-------------|-------------------|
| K0C041O37 | drone | VEH, WEA |

### Llama Constrained (3 CF entities)
| Doc ID | Entity Text | Conflicting Types |
|--------|-------------|-------------------|
| wiki_mass_car_bombings_1_news_8 | bodies | BOD, PER |
| wiki_mass_car_bombings_1_news_8 | government | GPE, ORG, PER |
| K0C041O37 | drone | VEH, WEA |

## CF Source Analysis

Common patterns:
1. **"drone" (VEH vs WEA)**: appears across 3 of 4 conditions. Genuinely ambiguous: a drone is both a vehicle and a weapon depending on context.
2. **Person names mistyped as LOC** ("tsarnaev", "silva" as LOC): constrained decoding doesn't prevent this since both PER and LOC are valid entity types in the schema.
3. **Collective nouns** ("police" as ORG vs PER, "government" as GPE/ORG/PER): inherently ambiguous entity references.
4. **"colombia" as PER**: clear model error in unconstrained output.
5. **"bodies" as BOD vs PER**: semantic ambiguity (physical bodies vs people).

## Comparison with RE CF Rates (SciERC)

| Task | Model | Unconstrained CF (%) | Constrained CF (%) |
|------|-------|---------------------|---------------------|
| RE (SciERC) | Qwen | — | 1.18 |
| RE (SciERC) | Llama | — | 0.46 |
| EE (WikiEvents) | Qwen | 0.77 | 0.89 |
| EE (WikiEvents) | Llama | 0.34 | 1.18 |

EE CF rates are in a similar range to RE CF rates (0.3%--1.2%). The absolute counts are very small (1--3 entities per condition out of 200--260 unique entities), so differences between conditions are not statistically meaningful.

## Key Observations

1. **Constrained decoding does NOT reduce CF in EE FT**: CF rates are slightly higher under constrained decoding for both models. This is expected because the current constraint grammar enforces role-type compatibility per event but does not enforce cross-event entity type consistency.
2. **CF is rare in FT models**: all rates are below 1.2%, much lower than base model unconstrained rates. Fine-tuning itself substantially reduces CF.
3. **Most CF cases are semantically ambiguous**, not clear errors. "drone" as VEH/WEA and "police" as ORG/PER reflect genuine type ambiguity in the schema rather than model confusion.

## Data Sources

- Qwen FT r5 (westd-21461): `outputs/ee_qwen_ft_wikievents_unconstrained_r5.jsonl`, `outputs/ee_qwen_ft_wikievents_full_s1_r5.jsonl`
- Llama FT r2 (westd-16980): `outputs/ee_llama_ft_wikievents_unconstrained_r2.jsonl`, `outputs/ee_llama_ft_wikievents_full_s1_r2.jsonl`
- Script: `scripts/calc_ee_cf.py` on both servers
