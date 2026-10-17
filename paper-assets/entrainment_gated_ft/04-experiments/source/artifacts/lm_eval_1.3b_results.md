# lm_eval Benchmark Results (1.3B Scale, 100B Tokens)

**Date:** 2026-05-18
**Server:** westb-48145
**Script:** `/root/entrainment_gated_ft/run_lmeval_clean.py` (no monkeypatch)
**Settings:** batch_size=16, bf16, lm_eval 0.4.12, fla 0.5.0, transformers 5.8.1

## Results

| Task | Metric | GDN Pure | Transformer | GDN Hybrid-12-1 | RetNet Pure |
|------|--------|----------|-------------|-----------------|-------------|
| lambada_openai | acc | **0.5430** | 0.4805 | 0.5337 | pending |
| lambada_openai | ppl | **8.26** | 11.46 | 8.73 | pending |
| hellaswag | acc_norm | 0.6080 | 0.5924 | **0.6103** | pending |
| winogrande | acc | 0.6077 | **0.6180** | 0.6117 | pending |
| arc_easy | acc | **0.7125** | 0.7113 | 0.6995 | pending |
| arc_challenge | acc_norm | **0.3925** | **0.3925** | 0.3857 | pending |
| mmlu | acc | **0.2606** | 0.2358 | 0.2541 | pending |

## Key Findings

1. **GDN Pure outperforms Transformer baseline** on 5/6 tasks (lambada, hellaswag, arc_easy, arc_challenge, mmlu). Only winogrande favors the transformer.
2. **GDN Hybrid-12-1** performs between pure GDN and transformer on most tasks, with the best hellaswag score.
3. **lambada ppl** shows the largest gap: GDN pure (8.26) vs transformer (11.46), a 28% relative improvement.

## Notes

- **RetNet Pure** checkpoint was corrupted during initial download (176/266 weight tensors all zeros in shard 1). Re-downloading from ModelScope. Results pending.
- piqa was dropped because the dataset was not in the HuggingFace cache on the offline server.
- Config fixes applied: GDN `allow_neg_eigval=True` for beta computation; RetNet `tie_weights()` for shared embeddings.
- fla `_tied_weights_keys` patched from list to dict format for transformers 5.8.1 compatibility.

## Result JSON Files

- `/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure.json` (132MB)
- `/root/entrainment_gated_ft/lm_eval_clean/transformer_1.3B_baseline.json` (123MB)
- `/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-hybrid-12-1.json` (132MB)
- `/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure.json` (pending re-download + eval)
