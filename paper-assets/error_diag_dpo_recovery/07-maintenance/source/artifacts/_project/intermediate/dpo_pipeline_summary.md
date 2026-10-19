## DPO Pipeline Scripts (on cqa1-21977)

### src/measure_correction_span.py (P1 gate)
CLI: python src/measure_correction_span.py --classified data/classified/classified_errors.jsonl --expert eto_repo/data/alfworld_sft.json --output data/correction_span_results.jsonl

### src/build_dpo_pairs.py
CLI: python src/build_dpo_pairs.py --classified data/classified/classified_errors.jsonl --expert eto_repo/data/alfworld_sft.json --output data/dpo_pairs_v2.jsonl

### Dry-run Results (88 classified, potentially tainted by episode boundary bug)
- action: N=5, mean=1.20
- verification: N=4, mean=1.00
- planning: N=73, mean=5.32
- Kruskal-Wallis: H=16.839, p=0.0002

### DPO Pairs: 67/88 success, 15 build_failed, 6 no_expert_match