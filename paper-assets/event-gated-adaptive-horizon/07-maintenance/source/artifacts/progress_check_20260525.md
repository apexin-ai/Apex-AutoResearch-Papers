# Training Progress Check — 2026-05-25

## Summary

| Exp | Task | Step | Target | Progress | eval_return | ETA (from now) |
|-----|------|------|--------|----------|-------------|----------------|
| exp_080_008e_v3_walker_s1 | Walker Walk | 84K | 105K | 80% | 846.5 @75K | ~46 min |
| exp_081_008e_v3_walker_s2 | Walker Walk | 80K | 105K | 76% | 404.5 @75K | ~45 min |
| exp_082_cheetah_no_dt_emb_s0 | Cheetah Run | 25K | 105K | 24% | 108.4 @25K | ~77 min |
| exp_083_cheetah_baseline_s1 | Cheetah Run | 8K | 105K | 8% | 11.6 @5K | ~95 min |

## Server: bjb1-45299

### GPU Utilization
| GPU | Util | VRAM |
|-----|------|------|
| 0 (exp_081) | 42% | 5742 / 97887 MiB |
| 1 (exp_080) | 98% | 6916 / 97887 MiB |

### exp_080_008e_v3_walker_s1 (PID 283925)
- **Step**: 84K / 105K (80%)
- **Elapsed**: 11023s (3.06h), rate ~7.6 steps/s
- **Latest eval**: 846.5 @75K (731.3 → 846.5)
- **Train return**: ~844-852 @84K
- **Gate**: dt_mean=1.0, gate_dt_1_frac=1.0 (all dt=1)
- **ETA**: ~46 min

### exp_081_008e_v3_walker_s2 (PID 285949)
- **Step**: 80K / 105K (76%)
- **Elapsed**: 8636s (2.40h), rate ~9.3 steps/s
- **Latest eval**: 404.5 @75K (311.9 → 404.5)
- **Train return**: ~341-417 @80K
- **Gate**: dt_mean=1.0, gate_dt_1_frac=1.0 (all dt=1)
- **ETA**: ~45 min

> exp_081 eval_return (404.5) significantly lower than exp_080 (846.5). Different seeds, s2 converging slower but still rising.

## Server: westd-19154

### GPU Utilization
| GPU | Util | VRAM |
|-----|------|------|
| 0 (exp_082) | 28% | 3242 / 97887 MiB |
| 1 (exp_083) | 54% | 4656 / 97887 MiB |

### exp_082_cheetah_no_dt_emb_s0 (PID 29479)
- **Step**: 25K / 105K (24%)
- **Elapsed**: 1436s (24min), rate ~17.4 steps/s
- **Latest eval**: 108.4 @25K (32.2 → 108.4)
- **Train return**: ~31-64 @24K
- **Gate**: dt_mean=2.0, gate_dt_2_frac=1.0 (all dt=2, no_dt_emb variant)
- **ETA**: ~77 min

### exp_083_cheetah_baseline_s1 (PID 30581)
- **Step**: 8K / 105K (8%)
- **Elapsed**: 375s (6min), rate ~21 steps/s (early, may slow)
- **Latest eval**: 11.6 @5K
- **Train return**: ~12-17 @8K
- **Gate**: N/A (baseline, no gate)
- **ETA**: ~95 min (high uncertainty, just started)

## Observations

1. **Walker (exp_080/081)**: Near completion. exp_080 performing well (eval 846.5), exp_081 slower (eval 404.5). Both gates locked at dt=1.
2. **Cheetah (exp_082/083)**: Early stage. exp_082 (no_dt_emb) gate locked at dt=2; exp_083 (baseline) just started training.
3. **GPU util**: bjb1 GPU1 near full (98%); westd GPUs underutilized (28%/54%), Cheetah tasks lighter.
4. All 4 processes running normally, no anomalies.
