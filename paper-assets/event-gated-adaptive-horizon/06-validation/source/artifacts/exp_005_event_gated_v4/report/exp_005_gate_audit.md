# exp_005 Gate Audit Report — effective_max_dt Single Source Architecture

## Bug Root Cause
`compute_gate_targets(feat_time, gate_max_dt)` placed probability mass across all 8 bins,
while `EventGate.forward(effective_max_dt=...)` masked logits to only `effective_max_dt` bins.
Cross-entropy between mismatched distributions caused enormous gate_loss (3e8).

## Architecture Fix: Single Source for effective_max_dt
- `WorldModel._update_gate_schedule()`: centralized computation (was duplicated 3x)
- `WorldModel._effective_max_dt` / `._gate_scale`: stored as attributes
- All consumers read from these attributes instead of recomputing

## Full Audit Table

| File:Line | Variable Used | Should Use | Modified? | Status |
|-----------|--------------|------------|-----------|--------|
| models.py:93 | gate_max_dt (RSSM init) | gate_max_dt | No — init param | OK |
| models.py:132 | gate_max_dt (EventGate init) | gate_max_dt | No — init param | OK |
| models.py:170-178 | NEW: _update_gate_schedule | effective_max_dt single source | Yes — new method | FIXED |
| models.py:189-191 | _update_gate_schedule() | — | Yes — replaces inline | FIXED |
| models.py:193 | gate_max_dt (subsample upper bound) | gate_max_dt | No — upper clamp OK | OK |
| models.py:246 | gate_max_dt → effective_max_dt | effective_max_dt | Yes — **critical fix** | FIXED |
| models.py:249 | gate_max_dt (reshape) | gate_max_dt | No — network output dim | OK |
| models.py:254-255 | NEW: effective_max_dt param | effective_max_dt | Yes — target masking | FIXED |
| models.py:262 | gate_max_dt (entropy reshape) | gate_max_dt | No — network output dim | OK |
| models.py:266-277 | gate_scale duplicate removed | _gate_scale | Yes — dedup | FIXED |
| models.py:502 | gate_max_dt (bincount minlength) | gate_max_dt | No — array size OK | OK |
| models.py:505 | gate_max_dt (metrics loop) | gate_max_dt | No — reports all bins | OK |
| models.py:509 | gate_max_dt → effective_max_dt | effective_max_dt | Yes — entropy ratio | FIXED |
| models.py:528-531 | gate_scale/eff_dt dupl → world_model attrs | effective_max_dt | Yes — dedup | FIXED |
| models.py:542-543 | effective_max_dt (gate clamp) | effective_max_dt | No — already correct | OK |
| networks.py:57 | max_dt (Embedding init) | max_dt | No — init param | OK |
| networks.py:369 | max_dt (Linear layer) | max_dt | No — init param | OK |
| networks.py:391-393 | effective_max_dt (masking) | effective_max_dt | No — already correct | OK |
| tools.py:763-789 | effective_max_dt (subsample) | effective_max_dt | No — already correct | OK |

## EventGate.entropy() Audit
- Input logits contain -1e9 for masked bins
- `F.softmax(-1e9)` → 0.0 (float32 underflow, exact zero)
- `0.0 * F.log_softmax(-1e9)` → `0.0 * (-1e9)` → `0.0` or `-0.0` (IEEE 754 safe)
- Entropy correctly computed only over unmasked bins
- **No fix needed** — numerically safe

## Unit Test Results
- compute_gate_targets: valid_mass=1.0, invalid_mass=0.0 for all eff values ✓
- gate_loss: [0.0, 2.08] range (was 3e8 before fix) ✓
- entropy: no NaN, bounded by log(eff_dt) ✓
- schedule: identical to original 3-phase curriculum ✓

## Changes Summary (8 edits)
1. compute_gate_targets: +effective_max_dt param, mask invalid bins
2. WorldModel.__init__: +_effective_max_dt, +_gate_scale attrs
3. WorldModel._update_gate_schedule: new centralized method
4. WorldModel._train: use _update_gate_schedule()
5. compute_gate_targets call: pass effective_max_dt
6. Gate loss section: remove duplicate gate_scale computation
7. ImagBehavior._imagine: use world_model attributes
8. ImagBehavior._train metrics: use effective_max_dt for entropy normalization
