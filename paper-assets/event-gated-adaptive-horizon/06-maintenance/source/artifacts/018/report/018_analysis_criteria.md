# Exp-018 Full-SGS: Hypothesis & Decision Criteria

## Experiment Design

**Config**: Walker Walk, trained dt_emb, `full_sgs=True` (detach ALL non-KL head gradients from dt_emb), subsample ON, H=8, seed 1

**What Full-SGS does**: Removes ~93% of gradients flowing into dt_emb. Only the 7% from KL dynamics (dyn_loss + rep_loss) remain. All observation decoder, reward, and continuation head gradients are detached.

**Core question**: Is CIVO a gradient-level or representation-level phenomenon?

## Decision Table

| 018 Outcome | NVE Pattern | Interpretation | Paper Impact |
|---|---|---|---|
| **NVE < 1.5x, eval stable** | No sustained collapse | CIVO is **gradient-level** → Full-SGS eliminates it | **C2 strengthened**: obs decoder gradients are a *necessary condition* for CIVO. Removing 93% of gradients suffices to prevent value overestimation collapse. |
| **NVE > 1.5x, collapse** | Sustained NVE > 1.5x for 2+ consecutive checkpoints | CIVO is **representation-level** → KL training alone maintains harmful dt_emb representation | **Direction pivot**: intervention must target dt_emb *representation* (e.g., orthogonalization, information bottleneck), not just gradient pathways. |
| **NVE transiently > 1.5x then recovers** | Spike above threshold but returns below | **Partial gradient effect** → obs decoder contributes but is not the sole cause | **Need finer ablation**: gradient stopping helps but insufficient alone. Suggests hybrid intervention (gradient + representation). |

## Quantitative Criteria

- **CIVO threshold**: NVE > 1.5x (baseline-normalized value estimation ratio)
- **Sustained**: 2+ consecutive eval checkpoints (eval every 10K steps → 20K+ sustained)
- **Peak comparison**: 018 peak_eval vs 008d peak_eval (167@25K) and baseline

## Reference Experiments

| Exp | Config | NVE | Status | Role in comparison |
|---|---|---|---|---|
| **008d** | trained dt_emb, subsample ON, H=8 | 4.12x@55K | CIVO collapse | Positive control (CIVO present, same base config as 018 minus SGS) |
| **008f** | no dt_embed (dim=0) | ≤ 1.02x | Stable | Negative control (no dt_emb → no CIVO possible) |
| **016e** | reward-only SGS (no-op, 0% detach) | 10.42x | Collapsed | Sanity check (removing 0% gradients doesn't help) |
| **baseline** | no dt_emb features | ~1.0x | Stable | NVE normalization reference |

## Key Comparisons

### 018 vs 008d (same config ± Full-SGS)
- If 018 stable & 008d collapsed → Full-SGS is the difference → gradient-level mechanism
- If both collapse → gradient stopping insufficient → representation-level

### 018 vs 016e (93% vs 0% gradient removal)
- 016e removes 0% of gradients (reward-only SGS is no-op since reward head was already stopped)
- 018 removes 93% of gradients
- If 016e collapses but 018 doesn't → the 93% gradient difference is causal

### 018 vs 008f (Full-SGS vs no dt_emb)
- 008f eliminates dt_emb entirely (dim=0) → no CIVO
- 018 keeps dt_emb but removes most gradients
- If 018 also stable → gradient removal achieves similar effect to removing the feature entirely

## Analysis Script

```bash
python scripts/analyze_018_full_sgs.py \
  --logdir-018 logdir/exp_018_full_sgs_walker_s1 \
  --logdir-008d logdir/exp_008d_subsample_on_h8 \
  --logdir-008f logdir/exp_008f_no_dt_embed_subsample_on_h8 \
  --logdir-016e logdir/exp_016e_sgs_walker_s1 \
  --baseline-logdir logdir/baseline_s1 \
  --output-dir artifacts/018_analysis
```

Outputs: `018_eval_comparison.{pdf,png}`, `018_nve_comparison.{pdf,png}`, `018_summary.json`
