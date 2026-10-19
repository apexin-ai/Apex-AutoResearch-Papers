# eval-acr-object-v4-scalar — Final Report

## Config
- Mode: crm_scalar (scalar_unc CRM v3-norm)
- Benchmark: LIBERO object (10 tasks × 10 rollouts)
- max_correction_norm: 0.1
- Checkpoint: /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt
- GPU hours: 13.27h

## Per-Task Results

| Task | SR | Success/Total |
|------|-----|---------------|
| alphabet_soup | 0% | 0/10 |
| cream_cheese | 0% | 0/10 |
| salad_dressing | 10% | 1/10 |
| bbq_sauce | 10% | 1/10 |
| ketchup | 0% | 0/10 |
| tomato_sauce | 0% | 0/10 |
| butter | 10% | 1/10 |
| milk | 10% | 1/10 |
| chocolate_pudding | 30% | 3/10 |
| orange_juice | 20% | 2/10 |

## Overall: **9.0%** (9/100)

## Comparison (LIBERO Object, max_correction_norm=0.1)

| Method | SR |
|--------|-----|
| argmin K=10 | 6.7% |
| **scalar_unc** | **9.0%** |
| perdof | 8.3% |
| vla_mean | 10.0% |
| obs_only 0.1 | 13.3% |
| obs_only 0.2 | 18.0% (5t) |

## Conclusion: **NEGATIVE**

scalar_unc (9.0%) marginally beats argmin baseline (6.7%) and perdof (8.3%), but underperforms obs_only (13.3%) and vla_mean (10.0%). 4/10 tasks have 0% success rate. The scalar uncertainty signal does not provide sufficient information for effective correction compared to obs_only which uses the full observation embedding.
