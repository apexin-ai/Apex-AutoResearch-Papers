Location: autodl-5090:/root/gen-depth-fingerprint/data/downstream/

Files:
- train_depth0_only.jsonl (797 samples) — human text only
- train_depth01.jsonl (3951 samples) — depth 0+1
- train_all.jsonl (12299 samples) — all depths
- train_size_matched.jsonl (3951 samples) — random sample, count-matched to depth01
- train_binary_filtered.jsonl (3951 samples) — NLL-based binary filtering, count-matched
- test.jsonl (3138 samples) — held-out test set (20% by seed_id)
- nll_scores.json — per-sample NLL scores for all training data

Binary baseline depth distribution: {0: 678, 1: 921, 2: 848, 3: 787, 4: 717}
Source: 4 generators (olmo-2-1b, pythia-1b, qwen3-0.6b, qwen3-1.7b), depth-0 deduplicated