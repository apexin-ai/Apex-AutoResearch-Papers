# eval_pi05_random_k085_object_seed42_postfix Results

## Experiment Config
- Model: pi0.5
- Pruning: random, keep_ratio=0.85 (217/256 tokens/image, 651 total)
- Suite: libero_object (10 tasks x 50 episodes = 500 total)
- Seed: 42
- Version: post CPU-RNG-fix

## Summary

```
total_episodes: 500
total_successes: 28
success_rate: 5.6%
```

## Per-Task Results

| Task | Description | Successes | Episodes | SR |
|------|-------------|-----------|----------|----|
| T0 | pick up the alphabet soup and place it in... | 3 | 50 | 6% |
| T1 | pick up the cream cheese and place it in... | 1 | 50 | 2% |
| T2 | pick up the salad dressing and place it in... | 1 | 50 | 2% |
| T3 | pick up the bbq sauce and place it in... | 1 | 50 | 2% |
| T4 | pick up the ketchup and place it in... | 6 | 50 | 12% |
| T5 | pick up the tomato sauce and place it in... | 4 | 50 | 8% |
| T6 | pick up the butter and place it in... | 2 | 50 | 4% |
| T7 | pick up the milk and place it in... | 4 | 50 | 8% |
| T8 | pick up the chocolate pudding and place it in... | 2 | 50 | 4% |
| T9 | pick up the orange juice and place it in... | 4 | 50 | 8% |

## Key Comparisons

| Condition | Object SR |
|-----------|-----------|
| pi0.5 baseline (no pruning) | ~96% |
| Random k=0.85 pre-fix | 5.0% |
| **Random k=0.85 post-fix** | **5.6%** |
| L2-norm k=0.85 | 99.0% |

## Conclusion

**conclusion: negative (disruption peak confirmed as real)**

Post-fix (5.6%) is essentially identical to pre-fix (5.0%) — the +0.6pp difference is within noise (binomial SE ~1pp at n=500). The CPU RNG fix did NOT resolve the extreme degradation at k=0.85.

This confirms that the **disruption peak at k=0.85 for random pruning on libero_object is a real phenomenon**, not an artifact of the RNG bug. Random removal of even 15% of vision tokens causes catastrophic failure on object manipulation tasks (~94pp drop from baseline), while L2-norm importance-based pruning at the same ratio preserves near-perfect performance (99.0%).

### Cross-suite comparison (Random k=0.85, post-fix)
- Goal: 52.4%
- Spatial: 56.6%
- **Object: 5.6%**

Object suite is uniquely sensitive to random token removal at this ratio.

## Runtime
- Total: 113.4 minutes
- Exit code: 0
