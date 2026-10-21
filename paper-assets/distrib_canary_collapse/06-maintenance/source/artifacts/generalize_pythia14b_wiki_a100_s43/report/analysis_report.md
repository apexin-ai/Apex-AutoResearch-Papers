# Analysis Report: generalize_pythia14b_wiki_a100_s43

**Model**: Pythia-1.4B | **Dataset**: WikiText-103 | **Alpha**: 1.0 | **Seed**: 43
**Date**: 2026-05-18

## 1. Training Completion

- 11 generations (gen_0 to gen_10) completed successfully
- EXIT_CODE = 0, no errors
- Final metrics: ppl=801.50, entropy=1.2795, eff_rank=96.3, mauve=0.0273

## 2. Five-Method Causal Analysis (16 pairs, 5 methods)

Total sig: s42=45/80, s43=46/80. K>=4: s42=8/16, s43=6/16. K>=3: both 9/16.
Per-method nearly identical across seeds. Scale effect confirmed systematic.

## 3. Conclusion: SUCCESS - scale effect is systematic, not seed noise.