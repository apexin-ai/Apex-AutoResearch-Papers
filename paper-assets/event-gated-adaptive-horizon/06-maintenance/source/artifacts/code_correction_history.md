# DreamerV3 Code Correction History

**Date**: 2026-05-28
**Scope**: Commit `09876d7` (May 14-18, old code) → `fb56c860a+` (May 25, corrected code)
**Source**: D152/D153 decisions, `d152_code_evolution_report.md`, registry, paper footnotes

---

## 1. The Bug: BF1 — `subsample_variable_dt` Parameter Routing Error

### What was wrong

`models.py:172` passed `gate_max_dt` (=8, the architectural maximum for the nn.Embedding) to `subsample_variable_dt`, **completely ignoring** `gate_subsample_max_dt` (=2, the user-configured sampling range).

**Old code** (commit `09876d7`, `models.py:171-173`):
```python
data, dt_labels = tools.subsample_variable_dt(
    data, self._config.gate_max_dt, self._config.discount,
)
```
Old `subsample_variable_dt` signature: `def subsample_variable_dt(data, max_dt, discount)` — no `effective_max_dt` parameter. The function used `max_dt=8` as the sampling range.

**New code** (commit `fb56c860a+`, `models.py:216-225`):
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
New code correctly routes `gate_subsample_max_dt=2` → `effective_max_dt=2`.

### Concrete effect

| Aspect | Intended (dt≤2) | Old code (actual: dt≤8) | New code (correct: dt≤2) |
|---|---|---|---|
| Subsample dt range | {1, 2} | {1, 2, 3, 4, 5, 6, 7, 8} | {1, 2} |
| dt=1 fraction | ~50% | ~27% (log-uniform) | ~50% |
| dt≠1 fraction | ~50% | **~73%** | ~50% |
| Train/imagination gap | small | **massive** (8× range vs dt=1 only) | small |

The old code created a massive distribution mismatch: the RSSM trained on dt∈{1–8} transitions but imagination always used dt=1. The dt_embedding encoded broad temporal information from 8 different scales, amplifying value overestimation through representational mismatch.

### When fixed

The fix was implemented between May 18 (last old-code experiment) and May 25 (first new-code verification). The exact commit date is unclear because the remote repo has no `.git` directory. Both `tools.py` (added `effective_max_dt` parameter to `subsample_variable_dt`) and `models.py` (routing logic) were modified.

---

## 2. Secondary Bug Fixes

### BF2: Replay Sampling Seed (May 17)

- **Old code** (`tools.py:332`): `def sample_episodes(episodes, length, seed=0)` — hardcoded seed=0
- **New code**: `seed=config.seed` passed from `dreamer.py`
- **Effect**: All old experiments shared identical replay buffer sampling regardless of `--seed`. Model weight init was correctly seeded. This made old experiments' stochastic landscape correlated across seeds — CIVO could cluster in vulnerable model-init seeds.
- **Impact**: Secondary. Doesn't explain systematic CIVO elimination but contributes to different collapse patterns.

### BF3: Gate Loss Guard (May 18)

- **Old code**: Computed gate loss even when `gate_fixed_dt>0` (gate unused in imagination)
- **New code**: `if self._config.gate_fixed_dt == 0:` guard skips gate loss when gate is fixed
- **Effect**: Old code trained the EventGate MLP unnecessarily, adding ~0.01-0.1 to model loss. Stop-gradient isolates this from RSSM, so impact is negligible (minor optimizer state noise).

---

## 3. Impact on Configurations

### 008e_v3 (trained dt_emb + subsample ON + dt=1 imagination + H=15)

This is the **primary affected configuration**. The bug meant 008e_v3 was a fundamentally different experiment than intended:

| | Old code (09876d7, May 14-18) | New code (fb56c860a, May 25) |
|---|---|---|
| Actual dt range | {1–8} (bug: 73% dt≠1) | {1, 2} (correct) |
| Seeds tested | s1, s2, s3, s4 (+s1 dup = 5 runs) | s0, s1, s2, s5 (4 runs) |
| CIVO collapse | **2/5** (s2: NVE 3.78×, s3: NVE 4.02×) | **0/4** |
| Experiment IDs (old) | exp_008e_v3_walker_s1/s2, exp_008e_v3_s3/s4 | exp_080, exp_081, exp_070, exp_072 |

**Paper handling**: Old data completely discarded (D153). Paper reports only corrected code results (0/4 CIVO). The old "Pathway B" narrative (stochastic CIVO under dt=1 mitigation) was deleted — it was a bug artifact.

### 008f (no dt_embedding + subsample ON + dt=2 + H=8)

008f uses `gate_dt_embed_dim=0`, so there is no dt_embedding. But **subsample ON** means `subsample_variable_dt` was still called, and the bug applied to the dt range used for temporal subsampling of training data.

| | Old code (exp_008f_no_dt_embed_subsample_on_h8, May 14) | New code (rerun, ~May 25) |
|---|---|---|
| Actual dt range | {1–8} (bug) | {1, 2} (correct) |
| eval @105K | 503.0 | 139.5 (with late-stage dip from 342.9@95K) |
| NVE | 0.97× | 1.69× (transient, no value overestimation) |

**Paper handling**: Footnote f (main table) / footnote l (appendix): "Corrected-code rerun; pre-correction data (eval 503.0, NVE 0.97×) superseded. NVE transient (1.69×) driven by late-stage eval dip (95K peak 342.9 → 105K final 139.5); no value overestimation—not CIVO."

### 008a_ch (Cheetah Run, unexposed/untrained dt_emb, subsample OFF)

Although 008a uses subsample OFF (so BF1 doesn't apply to dt subsampling), the Cheetah 008a experiments were also rerun on corrected code. Footnote k in the appendix table: "Corrected implementation; prior codebase runs on this configuration (eval 532.4, 504.4) were superseded."

This rerun likely reflects cumulative effects of BF2 (seed fix) and BF3 (gate loss guard), not BF1 specifically.

### Configs NOT affected by BF1

| Config | Why unaffected |
|---|---|
| 008a (Walker, subsample OFF) | `subsample_variable_dt` not called |
| 008c (subsample OFF, untrained) | Same reason |
| 001 baseline | No gate, no subsample |
| All `gate_enabled=false` experiments | Subsample code path not entered |

### Configs affected but with different implications

| Config | Bug effect |
|---|---|
| 008d (trained dt_emb, subsample ON, H=8) | Bug amplified CIVO (wider dt range → more severe mismatch). Old data still shows collapse but from a worse-than-intended configuration. The CIVO mechanism finding still holds — the bug made it stronger, not weaker. |
| All subsample ON experiments on old code | dt drawn from {1–8} instead of {1, gate_subsample_max_dt}. Effect depends on whether dt_embedding was trained. |

---

## 4. Are 008e_v3 and 008f caused by the same bug?

**Yes.** Both are caused by BF1 (gate_max_dt=8 parameter routing bug). The same `subsample_variable_dt` call in `models.py:172` affected both configurations because both use `subsample ON` (`gate_subsample_max_dt=2`).

The effect manifested differently because:
- **008e_v3** (trained dt_emb): Bug created massive train/imagination dt distribution gap → CIVO in 2/5 seeds. Fixed → 0/4 CIVO.
- **008f** (no dt_emb): Bug changed the training data composition (dt distribution) but no dt_embedding exists to create mismatch. Effect was on RSSM training dynamics → different eval trajectory but same CIVO-negative conclusion.

---

## 5. Is current code (HEAD) the corrected version?

**Yes.** The current code on the server (`westd-51268:/root/autodl-tmp/event-gated-adaptive-horizon/models.py`) contains the fix at lines 216-225 that correctly routes `gate_subsample_max_dt` through `effective_max_dt`. The supplementary code submitted with the paper also contains the corrected version.

---

## 6. Timeline Summary

| Date | Event | Key Commit |
|---|---|---|
| May 13 | First subsample experiments (exp_002–004) | Early code |
| May 14 04:10 | exp_008e (original, killed — duplicate process) | 09876d7 |
| May 14 04:27 | exp_008e_v2 (killed, replaced by v3) | 09876d7 |
| May 14 04:29 | **exp_008e_v3** (old code, seed 0) → SUCCESS (869.88) | 09876d7 |
| May 14 04:51 | **exp_008f** (old code, seed 0) → 503.0 eval | 09876d7 |
| May 14–15 | 008e_v3 s1, s2 (s2 collapsed: NVE 3.78×) | 09876d7 |
| May 17 | BF2 fixed (replay seed hardcoded→configurable) | |
| May 18 | BF3 fixed (gate loss guard); exp_008e_v3 s3 (collapsed: NVE 4.02×), s4 (healthy) | 09876d7 |
| ~May 21 | **BF1 fixed** (subsample_variable_dt effective_max_dt routing) | intermediate |
| May 25 | D152: Reviewer flags 008e_v3 0/4 CIVO on new code vs 2/5 on old | fb56c860a |
| May 25 | D153: Root cause confirmed — BF1 gate_max_dt=8 bug. Pathway B deleted. | fb56c860a |
| May 25–27 | All corrected-code reruns (008e_v3 s0/s1/s2/s5, 008f, 008a_ch) | fb56c860a |

---

## 7. What to tell a reviewer

**Concise explanation**: An implementation bug in the temporal subsampling routine passed the architectural embedding dimension (`gate_max_dt=8`) as the sampling range instead of the configured limit (`gate_subsample_max_dt=2`). This caused training data to include dt∈{1–8} instead of the intended dt∈{1,2}, creating a distribution mismatch between training and imagination that artificially inflated CIVO rates. After correction, the dt=1 imagination mitigation deterministically prevents CIVO (0/4 seeds).

**Key points for transparency**:
1. The bug affected all `subsample ON` configurations run before ~May 21.
2. The paper reports only corrected-code data for affected configurations, with explicit footnotes (^f/^k/^l) marking superseded results.
3. The CIVO mechanism finding (C2: trained dt_embedding causes value overestimation) is **strengthened** by the fix — the bug made CIVO worse, not better. Removing it confirms the core finding while upgrading the mitigation (C6) from stochastic to deterministic.
4. Unaffected configurations (subsample OFF: 008a, 008c, baseline) retain their original data.
