# Project Memory

## Experiment Registry

### acib_v73_connector_only_ablation (2026-05-18)
- **Status**: Completed, analyzed
- **Purpose**: Ablation to determine if v7.2's spatial conditioning (Probe A cos < 0.8) requires scorer contrastive learning or emerges from connector tuning alone
- **Config**: freeze_mode=connector_only, lambda_contrastive=0.0, lambda_drift=0.0, 20k steps, seed=42
- **Checkpoint**: /root/autodl-tmp/acib_connector_only_seed42/checkpoint-20000
- **Results**:
  - Training: 20k steps, 1.9h, final task_loss ~0.04
  - Probe A (connector output): cos=0.999991, bit_identical=True (connector has no language input)
  - Probe A (untrained scorer): cos=0.999999 (no language dependence without contrastive training)
  - Connector drift: 13.7% (vs v7.2's 0.4% with drift reg)
- **Conclusion**: Contrastive loss is NECESSARY for spatial conditioning. Pass criterion met (cos ≈ 1.0).
- **Comparison**: v7.2 trained scorer had cos in [0.593, 0.944]; v73 untrained scorer has cos ≈ 1.0

### acib_v72_connector_scorer_seed1 (parent)
- Probe A cos: [0.593, 0.944] (strong language-dependent spatial conditioning)
- Had scorer + contrastive loss + drift regularization
- Connector drift: 0.4%
