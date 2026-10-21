## α_crit Entity Selection Bound (v4 — Unified Strict MV)

> **v3→v4 change**: MV threshold unified from inclusive `≥ N/2 = 4` to strict `> N/2` (N=8: need ≥5/8 votes).
> Entity match: 4-tuple (text, type, start, end). Data source: MF4v2 pipeline samples.jsonl.
> Evaluation: gold-non-empty instances only, micro-F1 (aggregate TP/FP/FN).

### Main Table (T=1.0, MF4v2 micro-F1, strict MV > N/2)

| Dataset | Seeds | greedy_f1 | mv_f1 | oracle_f1 | Δ_SC (pp) | α_crit | δ (degen) | α_crit_eff | δ > 1−α_crit? |
|---------|-------|-----------|-------|-----------|-----------|--------|-----------|------------|---------------|
| FewNERD | 3 (42/123/456) | 0.7912 | 0.7638 | 0.8852 | **−2.74±0.54** | 0.3956 | 8.8% | 0.4338 | No (8.8% < 60.4%) |
| CoNLL   | 1 (42 only) | 0.9123 | 0.9101 | 0.9538 | **−0.22** | 0.4562 | 60.1% | 1.143 | **Yes** (60.1% > 54.4%) |
| SciERC  | 3 (42/123/456) | 0.6670 | 0.6596 | 0.7808 | **−0.74±0.57** | 0.3335 | 12.2% | 0.3799 | No (12.2% < 66.7%) |

- **Δ_SC** = mv_f1 − greedy_f1. All three datasets: MV **loses** to greedy under strict threshold.
- **α_crit** = F₁^gr / 2 (Proposition 1: marginal-entity precision threshold for Δ F₁ > 0)
- **α_crit_eff** = α_crit / (1 − δ). CoNLL α_crit_eff > 1.0 means MV gain structurally impossible given degeneracy.
- **δ**: fraction of gold-non-empty instances where all N=8 samples produce identical entity sets.
- ⚠️ **v4 公式修正**: 旧版脚本用 `π_MV/(2−π_MV)` 计算 α_crit（错误），已改为 Proposition 1 的 `F₁^gr/2`。

### Per-Seed Detail

#### FewNERD (n=32,565 gold-non-empty instances per seed)

| Seed | greedy_f1 | mv_f1 | oracle_f1 | degen | α_crit | Δ_SC (pp) |
|------|-----------|-------|-----------|-------|--------|-----------|
| 42   | 0.7913 | 0.7580 | 0.8803 | 9.1% | 0.3957 | −3.33 |
| 123  | 0.7908 | 0.7645 | 0.8899 | 9.2% | 0.3954 | −2.63 |
| 456  | 0.7915 | 0.7689 | 0.8855 | 8.1% | 0.3958 | −2.27 |

#### CoNLL (n=2,756 gold-non-empty instances; seed 123/456 pending — data missing)

| Seed | greedy_f1 | mv_f1 | oracle_f1 | degen | α_crit | Δ_SC (pp) |
|------|-----------|-------|-----------|-------|--------|-----------|
| 42   | 0.9123 | 0.9101 | 0.9538 | 60.1% | 0.4562 | −0.22 |
| 123  | — | — | — | — | — | pending |
| 456  | — | — | — | — | — | pending |

#### SciERC (n=529 gold-non-empty instances per seed)

| Seed | greedy_f1 | mv_f1 | oracle_f1 | degen | α_crit | Δ_SC (pp) |
|------|-----------|-------|-----------|-------|--------|-----------|
| 42   | 0.6683 | 0.6558 | 0.7840 | 13.4% | 0.3342 | −1.24 |
| 123  | 0.6663 | 0.6652 | 0.7789 | 11.0% | 0.3332 | −0.11 |
| 456  | 0.6663 | 0.6577 | 0.7795 | 12.1% | 0.3332 | −0.86 |

### v3 → v4 Delta (threshold change: ≥4/8 → ≥5/8)

Impact on mv_f1 (greedy/oracle/δ unchanged since they don't depend on MV threshold):

| Dataset | Seed | mv_f1 (v3 incl) | mv_f1 (v4 strict) | Δ mv_f1 (pp) |
|---------|------|------------------|--------------------|--------------|
| FewNERD | 42   | 0.7777 | 0.7580 | −1.97 |
| FewNERD | 123  | 0.7845 | 0.7645 | −2.00 |
| FewNERD | 456  | 0.7857 | 0.7689 | −1.68 |
| CoNLL   | 42   | 0.9128 | 0.9101 | −0.27 |
| SciERC  | 42   | 0.6640 | 0.6558 | −0.82 |
| SciERC  | 123  | 0.6689 | 0.6652 | −0.37 |
| SciERC  | 456  | 0.6687 | 0.6577 | −1.10 |

Note: α_crit = F₁^gr/2 不随 MV 阈值变化（仅取决于 greedy_f1），故不再列对比。

**Strict threshold consistently lowers mv_f1** by 0.3–2.0pp (largest on FewNERD).

### v3 → v4 Comparison (vs old published v3 values)

| Dataset | Seed | Metric | Old v3 | New v4 | Delta | Flag (>0.5pp) |
|---------|------|--------|--------|--------|-------|---------------|
| FewNERD | 42 | greedy_f1 | 0.7909 | 0.7913 | +0.04pp | |
| FewNERD | 42 | mv_f1 | 0.7781 | 0.7580 | −2.01pp | ⚠️ threshold |
| FewNERD | 42 | oracle_f1 | 0.8802 | 0.8803 | +0.01pp | |
| FewNERD | 123 | greedy_f1 | 0.7909 | 0.7908 | −0.01pp | |
| FewNERD | 123 | mv_f1 | 0.7844 | 0.7645 | −1.99pp | ⚠️ threshold |
| FewNERD | 456 | greedy_f1 | 0.7916 | 0.7915 | −0.01pp | |
| FewNERD | 456 | mv_f1 | 0.7857 | 0.7689 | −1.68pp | ⚠️ threshold |
| CoNLL | 42 | greedy_f1 | 0.9075 | 0.9123 | +0.48pp | data regen |
| CoNLL | 42 | mv_f1 | 0.9090 | 0.9101 | +0.11pp | data+threshold |
| CoNLL | 42 | δ | 65.7% | 60.1% | −5.6pp | ⚠️ data regen |
| SciERC | 42 | greedy_f1 | 0.6663 | 0.6683 | +0.20pp | data regen |
| SciERC | 42 | mv_f1 | 0.6657 | 0.6558 | −0.99pp | ⚠️ threshold+data |
| SciERC | 123 | mv_f1 | 0.6689 | 0.6652 | −0.37pp | threshold |
| SciERC | 456 | mv_f1 | 0.6687 | 0.6577 | −1.10pp | ⚠️ threshold |

**Notes**:
- FewNERD: greedy/oracle/δ match v3 to rounding → data identical. All mv changes from threshold.
- CoNLL s42: greedy/oracle/δ all shifted → conll_mf4v2_seed42 data was regenerated since v3.
- SciERC s42: small greedy shift (+0.20pp) → data may have been regenerated. s123/s456 data unchanged.
- CoNLL s123/s456: data missing on both servers. Marked "pending".

### Key Finding

**Strict MV (>N/2) uniformly hurts**: all 7 available (dataset, seed) combinations show Δ_SC < 0. Under inclusive (≥N/2), 3 of 7 showed marginal gains (+0.05 to +0.26pp); switching to strict eliminates even these.

The ~2pp FewNERD degradation is the largest. Entities at exactly 4/8 votes were net-positive on average under inclusive voting — removing them costs precision without reducing noise.

### Data Sources

- FewNERD: MF4v2 pipeline, Qwen3-8B-FT, N=8, T=1.0
  - seed 42: `fewnerd_mf4v2_seed42/samples.jsonl` (autodl-5090)
  - seed 123: `fewnerd_mf4v2_seed123/samples.jsonl` (autodl-5090)
  - seed 456: `fewnerd_mf4v2_seed456/samples.jsonl` (autodl-5090)
- CoNLL: MF4v2 pipeline, Qwen3-8B-FT, N=8, T=1.0
  - seed 42: `conll_mf4v2_seed42/samples.jsonl` (autodl-5090-c)
  - seed 123: **MISSING** (not on autodl-5090 or autodl-5090-c)
  - seed 456: **MISSING** (not on autodl-5090 or autodl-5090-c)
- SciERC: MF4v2 pipeline, Qwen3-8B-FT, N=8, T=1.0
  - seed 42: `scierc_mf4v2_seed42/samples.jsonl` (autodl-5090)
  - seed 123: `scierc_mf4v2_seed123/samples.jsonl` (autodl-5090)
  - seed 456: `scierc_mf4v2_seed456/samples.jsonl` (autodl-5090)
- Computed 2026-05-21 via `code/recompute_alpha_crit_unified.py`
- Entity match: exact 4-tuple (text, type, start, end)
- MV threshold: strict > N/2 (entity included if count > 4 of 8 samples, i.e., ≥5)
- Oracle: per-instance best-sample by instance F1, then aggregate micro-F1
- Evaluation scope: gold-non-empty instances only

### Version History

| Version | MV Threshold | Metric | FewNERD Δ | CoNLL Δ | SciERC Δ | Status |
|---------|-------------|--------|-----------|---------|----------|--------|
| v1 | — | macro_f1 | +0.89 | −1.09 | +0.76 | ❌ Wrong Δ def |
| v2 | ≥ N/2 | macro_f1 | −9.21 | −1.37 | −3.03 | ❌ Macro bug |
| v3 | **≥ N/2** | micro_f1 | −0.83 | +0.16 | +0.15 | ⚠️ Inclusive threshold |
| **v4** | **> N/2** | **micro_f1** | **−2.74** | **−0.22** | **−0.74** | **✓ Unified strict** |
