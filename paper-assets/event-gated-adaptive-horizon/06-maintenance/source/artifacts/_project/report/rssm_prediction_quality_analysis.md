# RSSM Prediction Quality: dt=1 vs dt=2 Analysis

## Results

| Model | dt1 obs_mse | dt2 obs_mse | obs gap | dt1 reward_mae | dt2 reward_mae | reward gap |
|-------|------------|------------|---------|---------------|---------------|------------|
| baseline_s1 | 13.49 | 27.50 | 2.04x | 0.0102 | 0.0159 | 1.56x |
| exp_008d (dt_emb, collapsed) | 41.31 | 53.67 | 1.30x | 0.0568 | 0.1579 | 2.78x |
| exp_008f (no_dt_emb, stable) | 8.01 | 22.04 | 2.75x | 0.7469 | 0.7526 | 1.01x |

## Key Findings

1. All models show degraded prediction at dt>1, supporting C2 delusional critic hypothesis
2. exp_008d dt_emb REDUCES relative obs gap (1.30x vs baseline 2.04x) but has WORST absolute quality (dt1=41.31 vs baseline 13.49)
3. exp_008d dt_emb causes HUGE reward prediction gap (2.78x) — reward predictions collapse at dt=2
4. exp_008f without dt_emb has best absolute dt=1 quality (8.01) but largest obs gap (2.75x) and broken reward model (~0.75 MAE)
5. The collapse in exp_008d is likely reward-driven: dt_emb helps obs prediction gap but massively worsens reward gap

## Server Path
/root/autodl-tmp/event-gated-adaptive-horizon/logdir/analysis_rssm_prediction_quality.json