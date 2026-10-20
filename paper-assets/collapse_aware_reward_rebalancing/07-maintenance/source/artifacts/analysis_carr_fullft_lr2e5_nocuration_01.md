# Experiment: carr_fullft_lr2e5_nocuration_01

Full-FT, LR=2e-5, No-Curation (random 1-of-4), 3 generations, 2000 prompts/gen, 3 epochs training.

## Metrics Per Generation

| Gen | mean_quality | vendi_score | self_bleu | perplexity | mean_nn_distance | complexity_mean |
|-----|-------------|-------------|-----------|------------|-----------------|-----------------|
| 0   | 0.1112      | 108.08      | 0.0046    | 10.97      | 0.7064          | 2.826           |
| 1   | 0.1100      | 107.85      | 0.0049    | 10.83      | 0.7095          | 2.871           |
| 2   | 0.1097      | 108.13      | 0.0068    | 11.15      | 0.7094          | 2.855           |

## Vendi Decline

vendi_decline_pct = (108.13 - 108.08) / 108.08 * 100 = **+0.05%** (essentially flat)

## Training Loss Trend

| Gen | train_loss |
|-----|-----------|
| 0   | 0.3765    |
| 1   | 0.1992    |
| 2   | 0.1320    |

Loss decreases across generations as the model fits increasingly to its own outputs.

## Checkpoint

Confirmed: `/root/autodl-tmp/carr/outputs_fullft_lr2e5_nocuration/gen_2/condition_0/merged` exists with full model files.

## Comparison: LR=2e-5 vs LR=5e-6 (No-Curation)

| Metric | LR=5e-6 (gen0 to gen2) | LR=2e-5 (gen0 to gen2) |
|--------|---------------------|---------------------|
| quality | 0.1126 to 0.1117 (-0.8%) | 0.1112 to 0.1097 (-1.3%) |
| vendi_score | 107.17 to 108.64 (+1.4%) | 108.08 to 108.13 (+0.05%) |
| self_bleu | 0.0045 to 0.0065 (+44%) | 0.0046 to 0.0068 (+48%) |
| perplexity | 8.77 to 8.82 (+0.6%) | 10.97 to 11.15 (+1.6%) |
| nn_distance | 0.7061 to 0.7114 (+0.8%) | 0.7064 to 0.7094 (+0.4%) |
| complexity | 2.847 to 2.82 (-0.9%) | 2.826 to 2.855 (+1.0%) |
| vendi_decline_pct | +1.38% | +0.05% |

Key observations:
- Both LR settings show minimal collapse under no-curation (vendi stable or slightly up)
- LR=2e-5 has higher perplexity (~11 vs ~8.8), suggesting more aggressive fitting diverges from base model distribution
- LR=2e-5 shows slightly more self_bleu increase (+48% vs +44%), indicating marginally more repetition
- Quality degradation is slightly larger with LR=2e-5 (-1.3% vs -0.8%)
- Neither condition shows meaningful collapse in 3 generations without curation
