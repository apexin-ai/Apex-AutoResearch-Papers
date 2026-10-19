# v73 Connector-Only Ablation Analysis

## Experiment Setup

| Parameter | Value |
|-----------|-------|
| Run name | acib_v73_connector_only_ablation |
| freeze_mode | connector_only |
| lambda_contrastive | 0.0 |
| lambda_drift | 0.0 |
| Steps | 20,000 |
| Final task_loss | 0.0397 |
| Training time | 1.9h |
| Checkpoint | /root/autodl-tmp/acib_connector_only_seed42/checkpoint-20000 |

**Purpose**: Determine if v7.2's spatial conditioning (Probe A cos < 0.8) is a product of scorer-driven contrastive learning or a natural result of connector tuning.

## Training Summary

- Completed normally (EXIT_CODE=0)
- All auxiliary losses = 0 throughout (no scorer, no contrastive, no IB): ib=0.0, div=0.0, ctr=0.0
- scorer_mean=0.000, std=0.000 (scorer never activated)
- task_loss decreased from ~0.076 (step 100) to ~0.040 (step 20000)
- No W&B logging configured

## Probe A Results

### Connector Output (Same Image, Different Instructions)

| Pair | Cosine | Bit Identical |
|------|--------|---------------|
| bbq_sauce vs black_bowl_cookie | 0.999991 | True |
| bbq_sauce vs black_bowl_drawer | 0.999991 | True |
| black_bowl_cookie vs black_bowl_drawer | 0.999991 | True |

**Verdict**: Connector output is **bit-identical** for the same image regardless of instruction. This is architecturally expected: the connector (modality_projection) receives only visual tokens from the vision encoder and has no language input pathway.

### Scorer Importance Maps (Untrained Scorer, Random Init)

| Pair | Cosine | L2 | Bit Identical |
|------|--------|----|---------------|
| bbq_sauce vs black_bowl_cookie | 0.999999 | 0.0077 | False |
| bbq_sauce vs black_bowl_drawer | 0.999999 | 0.0074 | False |
| black_bowl_cookie vs black_bowl_drawer | 0.999999 | 0.0076 | False |

**Verdict**: Untrained scorer (random init, concat conditioning mode) produces effectively identical importance maps (cos approx 1.0). Despite receiving different language embeddings via concatenation, the random weights do not amplify language differences into meaningful spatial variation.

## Comparison with v7.2

| Metric | v7.2 (scorer + contrastive) | v73 (connector only) |
|--------|----------------------------|---------------------|
| Probe A cos range | [0.593, 0.944] | [0.999999, 0.999999] |
| Language dependence | Strong | None |
| Connector drift | 0.4% | 13.7% |
| lambda_contrastive | > 0 | 0.0 |
| lambda_drift | 0.1 | 0.0 |

## Connector Weight Drift

| Parameter | L2 Drift | L2 Norm | Relative |
|-----------|----------|---------|----------|
| modality_projection.proj.weight | 9.84 | 71.77 | 13.71% |

The 34x larger drift (13.7% vs 0.4%) is expected: v73 had no drift regularization (lambda_drift=0.0) while v7.2 used lambda_drift=0.1.

## Conclusion

**Probe A cos approx 1.0 -> scorer contrastive is the NECESSARY component for spatial conditioning.**

1. Connector tuning alone does NOT produce language-dependent features (architecturally impossible: connector has no language input)
2. Without contrastive training, the scorer produces language-invariant importance maps even in concat mode
3. The spatial conditioning observed in v7.2 (cos as low as 0.593) is entirely driven by scorer-targeted contrastive learning

## Registry Entry

- **Conclusion**: success (ablation confirms hypothesis)
- **Notes**: Connector-only ablation confirms contrastive loss is necessary for spatial conditioning. Without scorer training, importance maps are language-invariant (cos approx 1.0 vs v7.2's [0.593, 0.944]). Connector drift 13.7% (no drift reg) vs v7.2 0.4% (with drift reg).
