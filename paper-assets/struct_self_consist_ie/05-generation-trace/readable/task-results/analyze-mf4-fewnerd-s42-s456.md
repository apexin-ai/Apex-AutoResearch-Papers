# analyze mf4 fewnerd s42 s456

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_mf4_fewnerd_s42_s456_20260522T124524_result.json`
- **Structured JSON:** [`916634ad6fc89e54828e.json`](../../sessions/91/916634ad6fc89e54828e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均正常完成（EXIT_CODE=0）。注意：当前 `run_mvp_pilot.py` 输出中**没有** `mv_strict_f1`、`lp_best_f1`、`degeneracy_rate` 这三个指标，report.json 里也没有。以下是所有可用指标。

```
============================================================
exp_fewnerd_mf4_s42 (seed=42)
============================================================
  greedy_f1:           0.7885
  oracle_f1:           0.8787
  oracle_headroom:     +0.0902
  verdict:             FAIL

  Agreement:
    fleiss_kappa_mean:   0.3537
    soft_jaccard_mean:   0.6751

  Sample quality:
    sample_f1_mean:      0.6130
    sample_f1_std:       0.3910
    sample_f1_pct_zero:  23.0%

  Filtering:
    gold_empty_filtered:       5083
    all_samples_f1_zero:       3874

  Correlation (full, n=32565):
    ρ(κ, F1):   +0.0510   p=3.30e-20
    ρ(SJ, F1):  +0.1648   p=5.23e-197
  Correlation (cond, n=28691):
    ρ(κ, F1):   -0.0301   p=3.49e-07
    ρ(SJ, F1):  +0.1989   p=8.73e-254
  Structural > Surface: YES  (Δ=+0.1138)

  Logprob (full, n=32565):
    ρ=+0.1561  τ=+0.1163  AUROC=0.5776
  Logprob (cond, n=28691):
    ρ=+0.1638  τ=+0.1228  AUROC=0.5766

  checkpoint: checkpoints/qwen3-8b-fewnerd-exp021-merged
  log: ~/runs/struct_self_consist_ie/exp_fewnerd_mf4_s42.log
  output: /root/autodl-tmp/struct_self_consist_ie/output/fewnerd_mf4_seed42/

============================================================
exp_fewnerd_mf4_s456 (seed=456)
============================================================
  greedy_f1:           0.7883
  oracle_f1:           0.8810
  oracle_headroom:     +0.0927
  verdict:             MARGINAL

  Agreement:
    fleiss_kappa_mean:   0.3555
    soft_jaccard_mean:   0.6845

  Sample quality:
    sample_f1_mean:      0.6430
    sample_f1_std:       0.3771
    sample_f1_pct_zero:  19.4%

  Filtering:
    gold_empty_filtered:       5083
    all_samples_f1_zero:       3883

  Correlation (full, n=32565):
    ρ(κ, F1):   +0.1643   p=6.54e-196
    ρ(SJ, F1):  +0.3122   p=0.0
  Correlation (cond, n=28682):
    ρ(κ, F1):   +0.0143   p=1.53e-02
    ρ(SJ, F1):  +0.2559   p=0.0
  Structural > Surface: YES  (Δ=+0.1479)

  Logprob (full, n=32565):
    ρ=+0.2439  τ=+0.1812  AUROC=0.6280
  Logprob (cond, n=28682):
    ρ=+0.2366  τ=+0.1773  AUROC=0.6215

  checkpoint: checkpoints/qwen3-8b-fewnerd-exp021-merged
  log: ~/runs/struct_self_consist_ie/exp_fewnerd_mf4_s456.log
  output: /root/autodl-tmp/struct_self_consist_ie/output/fewnerd_mf4_seed456/
```

**跨 seed 对比：**

| 指标 | seed=42 | seed=456 | Δ |
|------|---------|----------|---|
| greedy_f1 | 0.7885 | 0.7883 | -0.0002 |
| oracle_f1 | 0.8787 | 0.8810 | +0.0023 |
| oracle_headroom | +0.0902 | +0.0927 | +0.0025 |
| soft_jaccard_mean | 0.6751 | 0.6845 | +0.0094 |
| ρ(SJ, F1) full | +0.1648 | +0.3122 | **+0.1474** |
| ρ(SJ, F1) cond | +0.1989 | +0.2559 | +0.0570 |
| logprob AUROC (full) | 0.5776 | 0.6280 | **+0.0504** |
| sample_f1_pct_zero | 23.0% | 19.4% | -3.6pp |
| verdict | FAIL | MARGINAL | — |

**关键发现：**
1. Greedy F1 跨 seed 非常稳定（~0.788），符合预期
2. seed=456 在所有信号质量指标上显著优于 seed=42：ρ(SJ,F1) 高出 0.15，logprob AUROC 高出 0.05，sample 退化率低 3.6pp
3. `mv_strict_f1`、`lp_best_f1`、`degeneracy_rate` 当前 pipeline 未输出——如果需要这些指标，需要在 `run_mvp_pilot.py` 中增加 MV/LP selection 的 aggregation 逻辑
4. 无 W&B run ID（未使用 wandb logging）

---
