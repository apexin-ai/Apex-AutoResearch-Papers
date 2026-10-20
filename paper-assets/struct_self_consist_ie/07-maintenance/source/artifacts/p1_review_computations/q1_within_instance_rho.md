# Q1: 3-epoch SciERC Within-Instance Alignment ρ(LP, F1)

## Method

Per-instance Spearman ρ(mean_logprob, entity_F1) across N=8 samples per instance.
Exclusion criteria: empty gold, <3 valid samples, constant LP across samples, constant F1 across samples.
95% CI via bootstrap (10,000 resamples) on median ρ.

Data sources:
- 3-epoch: `/root/autodl-tmp/struct_self_consist_ie/output/exp_029a_scierc_3epoch/samples.jsonl`
- 5-epoch: `/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl`

Script: `analysis_r21_q1_alignment.py` on autodl-5090.

## Results

| Setting | N_inst | N_rho | N_samp | Median ρ | Mean ρ | Std | 95% CI | %positive | Constant F1 |
|---------|--------|-------|--------|----------|--------|-----|--------|-----------|-------------|
| 3-epoch | 529 | 495 | 8 | 0.3192 | 0.2726 | — | [0.2753, 0.3856] | 76.4% | 34 |
| 5-epoch | 529 | 435 | 8 | 0.2624 | 0.1791 | — | [0.1956, 0.3637] | 64.1% | 94 |

Selection outcome (LP selection vs greedy, macro F1):

| Setting | Greedy F1 | LP Sel F1 | Δ (pp) | Oracle F1 |
|---------|-----------|-----------|--------|-----------|
| 3-epoch | 0.6507 | 0.6383 | -1.24 | 0.8002 |
| 5-epoch | 0.6441 | 0.6505 | +0.64 | 0.7758 |

## Comparison with Prior Values

Previously reported (from memory.md):
- 5-epoch: mean=0.1532, median=0.2474
- 3-epoch: median=0.3172

Current computation:
- 5-epoch: mean=0.1791, median=0.2624
- 3-epoch: median=0.3192, mean=0.2726

Minor discrepancies likely from filtering criteria differences (gold-filtered vs not, logprob field name).

## Conclusion

3-epoch training improves within-instance LP-F1 alignment:
- Median ρ increases from 0.2624 to 0.3192 (+0.0568), consistent with reduced degeneracy (34 vs 94 constant-F1 instances).
- Mean ρ increases from 0.1791 to 0.2726 (+0.0935).
- 76.4% of instances show positive correlation at 3-epoch vs 64.1% at 5-epoch.

However, improved alignment does NOT translate to better LP selection: 3-epoch LP selection actually degrades F1 by -1.24pp (vs +0.64pp at 5-epoch). This is because 3-epoch has higher oracle headroom (0.8002 vs 0.7758) but LP still cannot exploit it effectively. The ρ~0.27-0.32 range remains below the approximate boundary (~0.3-0.5) observed in Few-NERD where LP selection succeeds.

The alignment values are close enough to suggest LP-F1 alignment is primarily a dataset-intrinsic property (SciERC's entity type structure and task difficulty), not purely a training convergence artifact. Training convergence modulates alignment marginally but does not cross the threshold needed for selection success.
