## Plan-003 E2E Eval: Ablation-B (Trained Router)

### Overall Results
| Metric | Value |
|--------|-------|
| Mean Score | -11.11 |
| 90% CI | [-15.93, -6.70] |
| Success Rate | 23.67% |
| Death Rate | 17.96% |
| Sim Ratio | 96.07% |
| Fallback Rate | 70.6% (173/245) |

### Baseline Comparison
| Condition | Score | Delta vs Router |
|-----------|-------|-----------------|
| always-det | -9.47 | +1.64 (better) |
| oracle | -6.58 | +4.53 (better) |
| random | -22.38 | -11.27 (worse) |
| always-internal | -39.07 | -27.96 (worse) |

### Per-Task Breakdown
| Task | Score | Death% | Success% | SimRatio |
|------|-------|--------|----------|----------|
| chemistry-mix | -11.75 | 15% | 25% | 90% |
| find-animal | -22.55 | 25% | 20% | 100% |
| find-non-living-thing | +28.68 | 0% | 62.5% | 97.5% |
| freeze | -29.25 | 30% | 10% | 95% |
| grow-fruit | -13.55 | 15% | 30% | 95% |
| identify-life-stages-1 | -12.50 | 15% | 10% | 95% |
| identify-life-stages-2 | -23.40 | 25% | 10% | 95% |
| inclined-plane | -24.50 | 25% | 5% | 95% |
| lifespan-longest | -14.00 | 20% | 16% | 96% |
| lifespan-longest-then-shortest | -14.20 | 20% | 20% | 90% |
| measure-melting | -24.25 | 25% | 15% | 100% |

### Conclusion
**NEGATIVE**: C1 "selective > unconditional" not supported. Router rarely routes to internal (sim_ratio=96%), and the few internal routes hurt (extra deaths).

### Output Files (server)
- results/eval_ablation_b_e2e/overall_results.json
- results/eval_ablation_b_e2e/per_task_results.csv
- results/eval_ablation_b_e2e/episode_details.jsonl