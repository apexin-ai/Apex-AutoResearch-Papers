# Eval Progress Report — 2026-05-16 ~11:30 UTC

## Summary

| Eval | PID | GPU | Progress | Avg Speed | ETA (UTC) | Status |
|------|-----|-----|----------|-----------|-----------|--------|
| eval_rsft_ced_s45 | 283838 | cuda:2 | **173/247 (70%)** | ~42s/it | ~12:22 | ✅ Running |
| eval_rsft_ced_s43 | 286587 | cuda:1 | **105/247 (43%)** | ~44s/it | ~13:14 | ✅ Running |
| eval_plan_014_no_evidence_r2 | 288109 | cuda:0 | **143/247 (58%)** | ~27s/it | ~12:17 | ✅ Running |
| reeval_flat_nli_s43_r2 | 291003 | cuda:3 | **35/247 (14%)** | ~43s/it | ~14:02 | ✅ Running |

## GPU Utilization

| GPU | Util | VRAM Used | VRAM Total |
|-----|------|-----------|------------|
| 0 | 57% | 10,355 MiB | 32,607 MiB |
| 1 | 51% | 10,859 MiB | 32,607 MiB |
| 2 | 48% | 11,091 MiB | 32,607 MiB |
| 3 | 49% | 10,855 MiB | 32,607 MiB |

## Notes

- All 4 processes alive, no OOM or errors.
- `eval_plan_014_no_evidence_r2` runs ~1.6x faster (no evidence → shorter generation).
- Predicted completion order: plan_014_no_evidence_r2 → rsft_ced_s45 → rsft_ced_s43 → reeval_flat_nli_s43_r2.
- VRAM usage ~10-11GB per process on 32GB cards — comfortable headroom.
