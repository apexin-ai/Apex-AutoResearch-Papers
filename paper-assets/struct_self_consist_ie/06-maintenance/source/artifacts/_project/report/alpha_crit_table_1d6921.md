## α_crit Entity Selection Bound (v3 — MF4v2 micro_f1)

> ⚠️ v1/v2 基于 macro_f1 数据，已作废。本版使用 MF4v2 pipeline 的 micro_f1（aggregate TP/FP/FN）。

### Main Table (T=1.0, MF4v2 micro-F1, multi-seed mean±σ)

| Dataset | Seeds | greedy_f1 | mv_f1 | oracle_f1 | Δ_SC (pp) | π_MV | α_crit | δ (degen) | α_crit_eff | Bound Predicts | Empirical |
|---------|-------|-----------|-------|-----------|-----------|------|--------|-----------|------------|----------------|-----------|
| FewNERD | 3 (42/123/456) | 0.7911 | 0.7828 | 0.8851 | **−0.83±0.38** | 0.7828 | 0.6430 | 8.8% | 0.7049 | — | **No** |
| CoNLL   | 2 (123/456) | 0.9124 | 0.9140 | 0.9522 | **+0.16±0.17** | 0.9140 | 0.8416 | 60.3% | 2.121 | — | **Marginal** |
| SciERC  | 3 (42/123/456) | 0.6663 | 0.6678 | 0.7808 | **+0.15±0.18** | 0.6678 | 0.5013 | 12.2% | 0.5707 | — | **Marginal** |

- **Δ_SC** = mv_f1 − greedy_f1 (positive = MV wins). All |Δ| < 1pp.
- **α_crit** = π_MV / (2 − π_MV)
- **α_crit_eff** = α_crit / (1 − δ). CoNLL α_crit_eff > 1.0 means MV gain is structurally impossible given degeneracy.
- **δ**: fraction of instances where all N=8 samples produce identical entity sets.

### Per-Seed Detail

#### FewNERD (n=32,565 gold-non-empty instances per seed)

| Seed | greedy_f1 | mv_f1 | oracle_f1 | degen | α_crit | Δ_SC (pp) |
|------|-----------|-------|-----------|-------|--------|-----------|
| 42   | 0.7909 | 0.7781 | 0.8802 | 9.1% | 0.6368 | −1.28 |
| 123  | 0.7909 | 0.7844 | 0.8897 | 9.2% | 0.6453 | −0.64 |
| 456  | 0.7916 | 0.7857 | 0.8855 | 8.1% | 0.6471 | −0.58 |

#### CoNLL (n=2,756 gold-non-empty instances per seed)

| Seed | greedy_f1 | mv_f1 | oracle_f1 | degen | α_crit | Δ_SC (pp) |
|------|-----------|-------|-----------|-------|--------|-----------|
| 123  | 0.9129 | 0.9157 | 0.9543 | 60.4% | 0.8445 | +0.28 |
| 456  | 0.9118 | 0.9122 | 0.9500 | 60.2% | 0.8386 | +0.04 |

> CoNLL seed 42 MF4v2 未执行（仅 2-seed）。

#### SciERC (n=529 gold-non-empty instances per seed)

| Seed | greedy_f1 | mv_f1 | oracle_f1 | degen | α_crit | Δ_SC (pp) |
|------|-----------|-------|-----------|-------|--------|-----------|
| 42   | 0.6663 | 0.6657 | 0.7839 | 13.4% | 0.4989 | −0.06 |
| 123  | 0.6663 | 0.6689 | 0.7789 | 11.0% | 0.5025 | +0.26 |
| 456  | 0.6663 | 0.6687 | 0.7795 | 12.1% | 0.5023 | +0.24 |

### Key Finding

**MV ≈ greedy (|Δ| < 1pp)**. SC captures negligible fraction of oracle headroom (4–11pp available).

- FewNERD: MV loses 0.83pp on average. Despite ~9% degeneracy and ~9pp oracle headroom, MV slightly *hurts*.
- CoNLL: MV gains 0.16pp on average. High degeneracy (60%) means most instances are trivially correct; MV barely moves the needle.
- SciERC: MV gains 0.15pp on average. Despite ~11pp oracle headroom, MV improvement is negligible.

Agreement signals predict quality (soft_jaccard ρ=0.31–0.46) but MV fails to translate correlation into selection improvement. The bottleneck is structural: entity-level MV aggregates across misaligned span boundaries, introducing errors absent from any individual sample.

### Old vs New Comparison (version history)

| Version | Δ Definition | Metric | FewNERD Δ | CoNLL Δ | SciERC Δ | Status |
|---------|-------------|--------|-----------|---------|----------|--------|
| v1 | θ2n − greedy | macro_f1 | +0.89 | −1.09 | +0.76 | ❌ Wrong Δ |
| v2 | MV − greedy | macro_f1 | −9.21 | −1.37 | −3.03 | ❌ Macro bug |
| **v3** | **MV − greedy** | **micro_f1** | **−0.83** | **+0.16** | **+0.15** | **✓ Correct** |

v2 → v3 correction: macro-F1 dramatically over-weights instances with few entities where MV tends to produce empty outputs. micro-F1 (aggregate TP/FP/FN) shows MV is approximately neutral, not catastrophically bad.

### Data Sources

- FewNERD: MF4v2 pipeline, Qwen3-8B-FT, N=8, T=1.0
  - seed 42: `fewnerd_mf4v2_seed42/samples.jsonl` (bjb2-11496)
  - seed 123: `fewnerd_mf4v2_seed123/samples.jsonl` (bjb2-11496)
  - seed 456: `fewnerd_mf4v2_seed456/samples.jsonl` (autodl-5090)
- CoNLL: MF4v2 pipeline, Qwen3-8B-FT, N=8, T=1.0
  - seed 123: `conll_mf4v2_seed123/samples.jsonl` (bjb2-11496)
  - seed 456: `conll_mf4v2_seed456/samples.jsonl` (bjb2-11496)
- SciERC: MF4v2 pipeline, Qwen3-8B-FT, N=8, T=1.0
  - seed 42: `scierc_mf4v2_seed42/samples.jsonl` (bjb2-11496)
  - seed 123: `scierc_mf4v2_seed123/samples.jsonl` (autodl-5090)
  - seed 456: `scierc_mf4v2_seed456/samples.jsonl` (autodl-5090)
- Computed 2026-05-21 via entity-level exact match (text, type, start, end) with micro-F1 (aggregate TP/FP/FN)
- MV threshold: entity included if it appears in ≥ N/2 = 4 of 8 samples
- Oracle: per-instance best-sample by instance F1
