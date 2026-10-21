## exp-004-eval-ckpt3500 Results

**Metrics**: ToF=0.1326, NoF=0.9006, SYCONScore=0.2312 (n=362, valid=181, invalid=181)
**vs vanilla**: SYCONScore 0.2312 vs 0.1335 = +73.2%
**Trajectory position**: Within dip region but above both neighbors — ckpt-3000 (0.2058) and ckpt-4000 (0.2140). Creates non-monotonic oscillation pattern in the dip.

### Updated Trajectory (ckpt-2000 to ckpt-5000 region)

| Checkpoint | ToF | NoF | SYCONScore | Delta vs vanilla |
|-----------|------|------|------------|-----------------|
| 2000 | 0.1492 | 0.8785 | 0.2550 | +91.0% |
| 2500* | 0.1381 | 0.8840 | 0.2389 | +78.9% |
| 3000 | 0.1160 | 0.9116 | 0.2058 | +54.2% |
| **3500** | **0.1326** | **0.9006** | **0.2312** | **+73.2%** |
| 4000 | 0.1215 | 0.8950 | 0.2140 | +60.3% |
| 5000 | 0.1547 | 0.8785 | 0.2631 | +97.1% |

*ckpt-2500 also newly evaluated in this batch.

### Dip Region Analysis

The dip region (ckpt-2500 to ckpt-4000) is confirmed but shows oscillation rather than a smooth valley:
- Decline: ckpt-2000 (0.2550) → ckpt-2500 (0.2389) → ckpt-3000 (0.2058) — steady descent
- Recovery attempt: ckpt-3000 (0.2058) → ckpt-3500 (0.2312) — partial rebound (+12.3%)
- Second dip: ckpt-3500 (0.2312) → ckpt-4000 (0.2140) — drops again
- Full recovery: ckpt-4000 (0.2140) → ckpt-5000 (0.2631) — surpasses pre-dip level

The dip bottom remains at ckpt-3000 (0.2058). ckpt-3500 partially recovers but doesn't sustain — ckpt-4000 dips again before final recovery at ckpt-5000.

**Conclusion**: success. SYCONScore 0.2312 >> vanilla baseline 0.1335. All checkpoints in the dip region remain well above vanilla, confirming ACT consistently improves sycophancy calibration. The oscillation pattern in the dip suggests training instability around ckpt-3000–4000 rather than systematic degradation.

### Paths

- **checkpoint_path**: `/root/autodl-tmp/outputs/exp-004-act-baseline/checkpoint-3500`
- **log_path**: `~/runs/contrastive_entrain_calib/exp-004-eval-ckpt3500.log` (on westd-28034)
- **results_json**: `/root/autodl-tmp/results/exp004_unified_eval/exp004_ckpt3500_preset_eval.json` (on westd-28034)
- **results_summary**: `/root/autodl-tmp/results/exp004_unified_eval/exp004_ckpt3500_preset_summary.txt` (on westd-28034)
