# analysis post training pipeline

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_post_training_pipeline_20260525T085449_result.json`
- **Structured JSON:** [`dda26559d2fc896ba212.json`](../../sessions/dd/dda26559d2fc896ba212.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs verified. Script works end-to-end:

**Created**: `/root/autodl-tmp/analysis/post_eval_analysis.py`

**Features**:
- 28 prior results embedded from both westd-10894 and westd-34685 evaluations
- `--dry-run` uses prior data only (tested, passes)
- `--eval-dir &lt;path>` merges new eval JSONs (from 4 upcoming experiments)
- `--no-prior` to start fresh from JSONs only
- `--metric TSR|CAR` for plot selection

**Outputs (verified)**:
- `comprehensive_results.csv` — 28 rows, 12 conditions, all TSR/CAR/collisions/episodes
- `seed_stats_summary.csv` — per-condition mean±SE
- `dose_response_car_3seed.pdf/png` — dose-response curve with error bands, filled/hollow markers
- `factorial_diagnostics.txt` — 2×2 table, main effects, narrative impact

**After training+eval on 34685 completes**, usage:
```bash
# Copy eval JSONs from 34685 to 10894
scp westd-34685:/root/occsafe_vla/artifacts/safelibero_*_2026052*.json /tmp/new_evals/

# Run analysis
python post_eval_analysis.py --eval-dir /tmp/new_evals/
```

Current state: Cutoff_15K/25K at 2 seeds, Cutoff_45K at 1, Reverse_Cutoff at 2. After the 4 new experiments, 15K/25K/Reverse will reach 3 seeds, 45K will reach 2.

---
