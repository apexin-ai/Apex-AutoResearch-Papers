# Evaluation Results: LIBERO Object Benchmark, Seed=44

## Experiment 1: obs_only CRM v3-norm, norm=0.1, seed=44
- **Exp ID:** eval-obs-only-object-norm01-seed44
- **Server:** bjb1-32546
- **Overall SR:** 16.0% (16/100)
- **Config:** crm_obs_only, K=10, 10 tasks x 10 rollouts, max_correction_norm=0.1
- **CRM checkpoint:** /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt (327,198 params)

### Per-task Results
| Task | SR | Successes |
|------|-----|-----------|
| alphabet_soup | 0% | 0/10 |
| cream_cheese | 10% | 1/10 |
| salad_dressing | 30% | 3/10 |
| bbq_sauce | 20% | 2/10 |
| ketchup | 0% | 0/10 |
| tomato_sauce | 10% | 1/10 |
| butter | 10% | 1/10 |
| milk | 20% | 2/10 |
| chocolate_pudding | 30% | 3/10 |
| orange_juice | 30% | 3/10 |

### Comparison
- argmin baseline seed44: 13% → obs_only norm=0.1 is +3pp above baseline
- obs_only norm=0.2 seed44: 16% → identical performance
- obs_only norm=0.1 seed42: 19% → seed44 is lower but still positive

**Conclusion: success** (above argmin baseline, consistent with norm=0.2)

---

## Experiment 2: perdof CRM v3-norm, norm=0.1, seed=44
- **Exp ID:** eval-perdof-object-seed44
- **Server:** bjb1-18228
- **Overall SR:** 8.0% (8/100)
- **Config:** crm_perdof, K=10, 10 tasks x 10 rollouts, max_correction_norm=0.1
- **CRM checkpoint:** /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt (337,438 params)

### Per-task Results
| Task | SR | Successes |
|------|-----|-----------|
| alphabet_soup | 0% | 0/10 |
| cream_cheese | 0% | 0/10 |
| salad_dressing | 20% | 2/10 |
| bbq_sauce | 10% | 1/10 |
| ketchup | 0% | 0/10 |
| tomato_sauce | 0% | 0/10 |
| butter | 0% | 0/10 |
| milk | 0% | 0/10 |
| chocolate_pudding | 20% | 2/10 |
| orange_juice | 30% | 3/10 |

### Comparison
- argmin baseline seed44: 13% → perdof is -5pp below baseline
- perdof seed42: 11%, seed43: 12% → seed44 continues negative trend

**Conclusion: negative** (consistently below argmin baseline across all seeds)
