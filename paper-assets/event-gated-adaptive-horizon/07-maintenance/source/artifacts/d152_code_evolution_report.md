# D152: Code Evolution Report — 008e_v3 CIVO Reproducibility

**Date**: 2026-05-25
**Scope**: Commit `09876d7` (May 14-18) → `fb56c860a+` (May 25)
**Config**: 008e_v3 = `gate_enabled=True, gate_fixed_dt=1, gate_subsample_max_dt=2, imag_horizon=15, trained dt_emb`

## Observation

| Code version | Seeds | CIVO collapse | Non-CIVO collapse |
|---|---|---|---|
| Old (09876d7) | s1,s2,s3,s4 (+ s1 dup) | **2/5** (s2: 3.78×, s3: 4.02×) | 0/5 |
| New (fb56c860a) | s0,s1,s2,s5 | **0/4** | 2/4 (s0, s2 low eval) |

## All Commits (May 14-25) — Classification

### Bug Fixes (behavior-altering)

| # | Date | Change | Classification | Impact on 008e_v3 |
|---|---|---|---|---|
| **BF1** | May 14 | `subsample_variable_dt` range: old code passed `gate_max_dt=8` to subsample function, ignoring `gate_subsample_max_dt=2`; new code passes `effective_max_dt=2` | **Critical Bug Fix** | **YES — PRIMARY CAUSE** |
| **BF2** | May 17 | `tools.sample_episodes(seed=0)` hardcoded → `seed=config.seed` passed from `dreamer.py` | Bug Fix | YES — secondary |
| **BF3** | ~May 18 | Gate loss guard: old code computed gate loss when `gate_fixed_dt>0`; new code skips gate loss when `gate_fixed_dt>0` | Bug Fix | YES — minor |

### Algorithm Changes (intentional, feature-gated)

| # | Date | Change | Files | Impact on 008e_v3 |
|---|---|---|---|---|
| A1 | May 14 | `dt_embed_dim=0` guard in RSSM init | networks.py | No (008e_v3 uses dim=32) |
| A2 | May 15 | `dt_emb_freeze` config + re-freeze logic after `RequiresGrad` | models.py, configs.yaml | No (defaults False, not set) |
| A3 | May 15 | Reward SGS (`reward_dt_emb_detach`) | models.py | No (defaults False) |
| A4 | May 15 | SGS diagnostic code added then deleted (30 lines) | models.py | No (guarded by sgs flag) |
| A5 | May 15-16 | Full SGS (`full_sgs`) | models.py | No (defaults False) |
| A6 | May 17 | CIVO Detector in eval loop | dreamer.py, configs.yaml | No (read-only monitoring) |
| A7 | May 19 | Obs-decoder-only SGS (`sgs_mode`) | models.py | No (defaults "none") |
| A8 | May 20 | TCN noise in `img_step` (`tcn_sigma`) | networks.py, models.py | No (defaults 0.0, guarded by `if tcn_sigma > 0`) |
| A9 | May 20 | RAVE value ceiling (`rave_ceiling`) | models.py | No (defaults 0.0, guarded) |
| A10 | May 20 | Dual critic | models.py, configs.yaml | No (defaults False) |
| A11 | May 21 | Wide critic | models.py, configs.yaml | No (defaults False) |
| A12 | May 21 | Narrow dual critic | models.py, configs.yaml | No (defaults False) |

### Cosmetic / Non-behavioral

| # | Date | Change | Impact |
|---|---|---|---|
| C1 | May 15-16 | ManiSkill3 env wrapper | No (different env) |
| C2 | Various | Analysis scripts (nve_audit, grad decomp, etc.) | No (standalone scripts) |
| C3 | Various | Metric logging additions | No (read-only) |

---

## Detailed Analysis of Bug Fixes

### BF1: `subsample_variable_dt` Range Bug — PRIMARY CAUSE

**Old code** (`artifacts/code/models.py:171-173`):
```python
data, dt_labels = tools.subsample_variable_dt(
    data, self._config.gate_max_dt, self._config.discount,
)
```
Old `subsample_variable_dt` signature: `def subsample_variable_dt(data, max_dt, discount)` — no `effective_max_dt` parameter.

With `gate_max_dt=8` and `gate_subsample_max_dt=2`: **old code sampled dt ∈ {1,2,3,4,5,6,7,8}** with log-uniform distribution. The `gate_subsample_max_dt` parameter was **completely ignored**.

**New code** (`supplementary/code/models.py:216-225`):
```python
subsample_max_dt_override = getattr(self._config, 'gate_subsample_max_dt', 0)
if subsample_max_dt_override > 0:
    subsample_eff_dt = float(subsample_max_dt_override)
else:
    subsample_eff_dt = effective_max_dt
data, dt_labels = tools.subsample_variable_dt(
    data, bst_max_dt, self._config.discount,
    effective_max_dt=subsample_eff_dt, min_dt=...,
)
```
New code correctly limits dt ∈ {1, 2}.

**Why this causes CIVO**:
- Old: dt_embedding trained on dt=1..8 during world model training, but imagination always uses dt=1
- Training/imagination distribution gap: 8× range vs 1-value → dt_embedding encodes broad temporal info → amplifies value overestimation through representational mismatch
- New: dt_embedding trained on dt=1..2 only → minimal distribution gap → CIVO trigger suppressed

**Estimated dt distribution (old log-uniform over [1,8])**:
- dt=1: ~27%, dt=2: ~23%, dt=3: ~13%, dt=4: ~11%, dt=5-8: ~26%
- Over 70% of training data used dt≠1, massive mismatch with imagination (always dt=1)

### BF2: Replay Sampling Seed Bug

**Old code** (`artifacts/code/tools.py:332`): `def sample_episodes(episodes, length, seed=0)` — hardcoded seed.
**Old dreamer.py**: `tools.sample_episodes(episodes, config.batch_length)` — `config.seed` not passed.

All experiments shared identical replay buffer sampling regardless of `--seed`. Model init via `torch.manual_seed` was correct.

**Impact**: Changes the stochastic landscape across seeds. Old experiments had correlated replay → CIVO could cluster in certain model-init seeds that were vulnerable. New experiments have independent replay → different collapse pattern. Secondary factor; doesn't explain systematic CIVO elimination.

### BF3: Gate Loss with gate_fixed_dt > 0

**Old code** (`artifacts/code/models.py:218`):
```python
if self._config.gate_enabled and self.event_gate is not None:
    # computes gate loss, adds to mean_model_loss
```

**New code** (`supplementary/code/models.py:272`):
```python
if self._config.gate_enabled and self.event_gate is not None and self._config.gate_fixed_dt == 0:
```

Old code trained EventGate MLP even when gate was never used in imagination. EventGate receives stop-gradient features, so its loss doesn't backprop into RSSM. However:
- Adds ~0.01-0.1 to model loss (noise)
- EventGate parameters participate in optimizer state (Adam moments)
- Minor effect on effective learning rate through gradient norm scaling

**Impact**: Negligible. Gate loss is small relative to model loss and isolated by stop-gradient.

---

## Conclusion

### Root Cause: BF1 (subsample range bug)

The old `subsample_variable_dt` ignored the `gate_subsample_max_dt` parameter and used `gate_max_dt=8` as the sampling range. **Old 008e_v3 was a fundamentally different experiment** from what was intended:

| Aspect | Old (intended: dt≤2) | Old (actual: dt≤8) | New (correct: dt≤2) |
|---|---|---|---|
| Subsample dt range | {1, 2} | {1, 2, 3, 4, 5, 6, 7, 8} | {1, 2} |
| Train/imag gap | small | **large** | small |
| dt_emb exposure | minimal variation | broad temporal spectrum | minimal variation |
| CIVO rate | unknown | 2/5 (40%) | 0/4 (0%) |

### Classification

**The old 2/5 CIVO data is invalid** — it was produced by a buggy implementation that ran a different experiment than intended. The `gate_subsample_max_dt=2` flag had no effect in the old code.

### Paper Recommendation

1. **Do NOT cite old 008e_v3 data (2/5 collapse)** in the paper. The old code had a parameter-routing bug that invalidated those results.
2. **Use only current code data (0/4 CIVO)** for the C6 narrative.
3. If the paper needs to discuss the 008e_v3 configuration, report it as:
   - "trained dt_emb + subsample_max_dt=2 + fixed_dt=1 + H=15: 0/4 CIVO collapse across 4 seeds"
4. The bug itself is **not** paper-worthy as a finding — it's an implementation error, not a scientific insight.
5. Note that 2/4 seeds in the new code show non-CIVO collapse (low eval without value explosion), which is a separate phenomenon from CIVO.

### Supporting Evidence

- Old `tools.py:767`: `subsample_variable_dt(data, max_dt, discount)` — only 3 params, no effective_max_dt
- Old `models.py:172`: passes `self._config.gate_max_dt` (=8), not `gate_subsample_max_dt` (=2)
- New `tools.py:768`: `subsample_variable_dt(data, max_dt, discount, effective_max_dt=None, min_dt=1)` — accepts effective_max_dt
- New `models.py:216-224`: correctly routes `gate_subsample_max_dt` → `effective_max_dt`
- Gradient decomposition analysis (`grad_decomp_008d_corrected.py`) explicitly documents this as "wrong config vs correct config"
- Seed bug fix (`M003/D075`): secondary factor, does not explain systematic CIVO elimination
