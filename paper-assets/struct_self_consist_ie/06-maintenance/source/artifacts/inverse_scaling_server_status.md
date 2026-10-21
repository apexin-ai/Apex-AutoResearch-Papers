# Multiseed Inverse Scaling — Server Status

## Status: COMPLETE

Computation finished on autodl-5090. All 9 configs ran successfully.

**Server files** (`/root/autodl-tmp/struct_self_consist_ie/artifacts/multiseed_inverse_scaling/`):
- `all_results.json` (106KB) — full per-instance results
- `consistency_report.json` (21KB) — cross-seed direction consistency
- `output.log` (20KB) — complete run log
- `run.py` (18KB) — computation script

**No active processes** — computation is fully done.

## Results Summary (9 configs)

| Config | Seed | N_max | Transitions | Sig Inverse | Sig Positive |
|--------|------|-------|-------------|-------------|--------------|
| Qwen_FewNERD | 42 | 8 | 21 | 4 (19%) | 15 |
| Qwen_FewNERD | 123 | 8 | 21 | 6 (29%) | 13 |
| Qwen_FewNERD | 456 | 8 | 21 | 6 (29%) | 13 |
| Qwen_FewNERD | 789 | 8 | 21 | 5 (24%) | 14 |
| Qwen_FewNERD | 42 | 16 | 28 | 8 (29%) | 18 |
| Qwen_FewNERD | 456 | 16 | 28 | 10 (36%) | 15 |
| LLaMA_FewNERD | 42 | 8 | 21 | 8 (38%) | 13 |
| LLaMA_FewNERD | 123 | 8 | 21 | 6 (29%) | 14 |
| LLaMA_FewNERD | 456 | 8 | 21 | 6 (29%) | 14 |

## Cross-seed Consistency (Qwen N=8, 4 seeds)

**4/21 transitions** show sig inverse across ALL 4 seeds:
- `lp_weighted` N=6→8
- `theta2n` N=6→8
- `uniform` N=2→4
- `uniform` N=6→8

**Method stratification**:
- Never inverse: `majority_vote`, `lp_best` (consistent across all seeds/models)
- Always inverse at high N: `lp_weighted`, `theta2n`, `uniform`
- Borderline: `vc_weighted`, `sj_weighted`

LLaMA shows even higher cross-seed agreement: 19/21 same direction (90%).

## "40 of 58 transitions" Claim

The multi-seed data **supports** the original claim's validity — inverse scaling is not a seed artifact. The per-seed sig positive counts (13–15 out of 21 for N=8) are stable. The specific "40 of 58" number refers to the original single-seed experiment scope and does not need updating based on this analysis, but the paper can now additionally claim **cross-seed reproducibility** of inverse scaling patterns.

## Local Report

Full analysis already written to `artifacts/multiseed_inverse_scaling_report.md` with detailed per-method breakdowns, direction consistency tables, and conclusions.
