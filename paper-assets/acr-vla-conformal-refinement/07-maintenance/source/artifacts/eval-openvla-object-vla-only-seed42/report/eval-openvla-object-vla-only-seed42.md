# OpenVLA VLA-only Baseline: LIBERO-Object (seed 42)

## Experiment Summary
- **Model**: OpenVLA-7B (fine-tuned on LIBERO-Object)
- **Benchmark**: LIBERO-Object (10 tasks x 10 rollouts = 100 episodes)
- **Mode**: VLA-only (K=1, no CRM)
- **Server**: bjb1-18228
- **Wall clock**: ~2.1 GPU-hours
- **Avg inference**: 178 ms/step

## Results

**Overall success rate: 0.0% (0/100)**

| Task | Success Rate |
|------|-------------|
| pick_up_the_alphabet_soup_and_place_it_in_the_basket | 0% (0/10) |
| pick_up_the_cream_cheese_and_place_it_in_the_basket | 0% (0/10) |
| pick_up_the_salad_dressing_and_place_it_in_the_basket | 0% (0/10) |
| pick_up_the_bbq_sauce_and_place_it_in_the_basket | 0% (0/10) |
| pick_up_the_ketchup_and_place_it_in_the_basket | 0% (0/10) |
| pick_up_the_tomato_sauce_and_place_it_in_the_basket | 0% (0/10) |
| pick_up_the_butter_and_place_it_in_the_basket | 0% (0/10) |
| pick_up_the_milk_and_place_it_in_the_basket | 0% (0/10) |
| pick_up_the_chocolate_pudding_and_place_it_in_the_basket | 0% (0/10) |
| pick_up_the_orange_juice_and_place_it_in_the_basket | 0% (0/10) |

## Comparison with SmolVLA Baseline

| Method | LIBERO-Object Mean SR |
|--------|----------------------|
| SmolVLA VLA-only (K=1) | 10.8% |
| **OpenVLA VLA-only (K=1)** | **0.0%** |
| SmolVLA + obs_only CRM (K=10, eps=0.2) | 17.5% |

OpenVLA performs significantly worse than SmolVLA on this benchmark in VLA-only mode. This is surprising given OpenVLA's larger model size (7B vs 0.4B).

## Analysis

The 0% result across all tasks is notable. Possible explanations:

1. **Checkpoint quality**: The fine-tuned checkpoint at `/root/autodl-tmp/models/openvla-libero-object` may not have converged well on LIBERO-Object. Need to verify training logs.
2. **Action space mismatch**: OpenVLA's action tokenization/detokenization may not align with the LIBERO action space as configured. The `unnorm_key=libero_object` should handle this, but worth verifying.
3. **Evaluation protocol**: The eval ran cleanly (EXIT_CODE=0, no errors), consistent 175-181ms inference time, suggesting the model is producing actions but they are ineffective.

## Implications for CRM

- If the OpenVLA backbone produces 0% success alone, CRM correction would need to be extremely strong to rescue performance.
- This may actually be a stronger test of CRM's value: can conformal refinement improve a completely failing VLA backbone?
- However, 0% baseline may indicate a broken checkpoint rather than genuine model weakness. Recommend verifying before building CRM on top.

## Next Steps

1. **Verify checkpoint**: Check if this OpenVLA checkpoint was properly fine-tuned (training loss, validation metrics)
2. **Sanity check**: Run a few manual rollouts or check if the model produces meaningful action distributions
3. **Compare with published results**: OpenVLA paper reports higher success on LIBERO; discrepancy needs investigation
4. **If checkpoint is valid**: Proceed with CRM experiments on OpenVLA to test correction capability on a weaker backbone
