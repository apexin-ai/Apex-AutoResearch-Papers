# Cliff Curve Data Summary
> Generated: 2026-05-27T10:00 UTC
> Status: 58/72 data points have values (12 RUNNING, 9 no data)
> π0.5 strict note: 5/18 confirmed strict, 13 approximate (postfix/non-tag), 6 strict re-runs RUNNING

---

## OpenVLA Object (baseline = 74.0%)

| k | L2norm | Attn | Random |
|---|--------|------|--------|
| 0.95 | 70.6% | 71.2% | 67.4% |
| 0.90 | 70.6% | 61.4% | 62.8% |
| 0.85 | **RUNNING** | 55.0% | **MISSING** |
| 0.75 | **MISSING** | 53.2% | 50.4% |
| 0.70 | 49.8% | 43.8% | 44.4% |
| 0.50 | 39.2% | **MISSING** | **MISSING** |

**Collected: 13/18** | Running: 1 | Missing: 4

Running:
- L2norm k=0.85 → `eval_openvla_l2norm_k085_object_seed42` on westd-27271

Missing (no experiment registered):
- L2norm k=0.75
- Attn k=0.50
- Random k=0.85
- Random k=0.50

---

## OpenVLA Goal (baseline = 74.8%)

| k | L2norm | Attn | Random |
|---|--------|------|--------|
| 0.95 | 75.2% | 75.6% | **MISSING** |
| 0.90 | 74.8% | 73.2% | 79.6% |
| 0.85 | 75.4% | 74.6% | 78.6% |
| 0.75 | 70.2% | 67.4% | 72.0% |
| 0.70 | 68.4% | **MISSING** | 68.4% |
| 0.50 | 43.4% | 44.2% | 52.2% |

**Collected: 16/18** | Running: 0 | Missing: 2

Note: Attn k=0.95 uses v2 (75.6%); v1 was 76.8%.

Missing (no experiment registered):
- Attn k=0.70
- Random k=0.95

---

## OpenVLA Long (baseline = 52.8%)

| k | L2norm | Attn | Random |
|---|--------|------|--------|
| 0.95 | **RUNNING** | **RUNNING** | **RUNNING** |
| 0.90 | 43.6% | 44.0% | 46.8% |
| 0.85 | 38.8% | 45.8% | 45.0% |
| 0.75 | **RUNNING** | 37.4% | **MISSING**¹ |
| 0.70 | 31.2% | 24.0% | 38.8% |
| 0.50 | **MISSING** | 14.6% | **MISSING** |

**Collected: 11/18** | Running: 4 | Missing: 3

¹ `eval_openvla_random_k075_long_seed42` is DONE/success but metrics=null (data lost).

Running:
- L2norm k=0.95 → `eval_openvla_l2norm_k095_long_seed42` on westd-38929
- Attn k=0.95 → `eval_openvla_attn_k095_long_seed42` on westd-38929
- Random k=0.95 → `eval_openvla_random_k095_long_seed42_backup` on westd-38929
- L2norm k=0.75 → `eval_openvla_l2norm_k075_long_seed42_v2` on westd-38929

Missing (no experiment registered):
- L2norm k=0.50
- Random k=0.75 (metrics lost from previous run, needs re-run)
- Random k=0.50

---

## π0.5 Long — strict (baseline = 92.8%)

Values marked ✓ are from explicitly strict-tagged experiments.
Values marked ~ are from postfix/non-tag runs (approximate, typically ~1-3pp higher than strict).

| k | L2norm | Attn | Random |
|---|--------|------|--------|
| 0.95 | 86.2% ✓ | ~77.0% → **RE-RUN** | 60.6% ✓ |
| 0.90 | ~80.0% → **RE-RUN** | 64.0% ✓ | ~32.0% → **RE-RUN** |
| 0.85 | ~78.4% → **RE-RUN** | 50.0% ✓ | ~45.2% |
| 0.75 | ~73.4% | ~51.8% | 63.0% ✓ |
| 0.70 | ~62.6% | ~50.8% | ~65.8% → **RE-RUN** |
| 0.50 | ~50.2% | ~49.8% | ~46.8% → **RE-RUN** |

**Confirmed strict: 5/18** | Approximate: 13 | Strict re-runs RUNNING: 6

Strict vs lenient calibration (where both available):
- L2norm k=0.95: strict=86.2%, lenient=87.0% (Δ=−0.8pp)
- Random k=0.95: strict=60.6%, lenient=63.2% (Δ=−2.6pp)
- Attn k=0.90: strict=64.0%, postfix=63.8% (Δ=+0.2pp)
- Attn k=0.85: strict=50.0%, lenient=51.6% (Δ=−1.6pp)

Running strict re-runs:
- L2norm k=0.90 → `eval_pi05_l2norm_k09_long_seed42_strict_cqa1` on cqa1-33015
- L2norm k=0.85 → `eval_pi05_l2norm_k085_long_seed42_strict` on cqa1-33015 + westd-41074
- Attn k=0.95 → `eval_pi05_attn_k095_long_seed42_strict_w41` on westd-41074
- Random k=0.90 → `eval_pi05_random_k09_long_seed42_strict_v2` on westd-41074
- Random k=0.70 → `eval_pi05_random_k07_long_seed42_strict_v2` on cqa1-33015
- Random k=0.50 → `eval_pi05_random_k05_long_seed42_strict_w41_v2` on westd-41074

---

## Summary: All RUNNING Experiments (12 total)

| exp_id | Model | Method | k | Suite | Server |
|--------|-------|--------|---|-------|--------|
| eval_openvla_l2norm_k085_object_seed42 | OV | L2norm | 0.85 | Object | westd-27271 |
| eval_openvla_l2norm_k095_long_seed42 | OV | L2norm | 0.95 | Long | westd-38929 |
| eval_openvla_attn_k095_long_seed42 | OV | Attn | 0.95 | Long | westd-38929 |
| eval_openvla_random_k095_long_seed42_backup | OV | Random | 0.95 | Long | westd-38929 |
| eval_openvla_l2norm_k075_long_seed42_v2 | OV | L2norm | 0.75 | Long | westd-38929 |
| eval_pi05_l2norm_k09_long_seed42_strict_cqa1 | π0.5 | L2norm | 0.90 | Long | cqa1-33015 |
| eval_pi05_l2norm_k085_long_seed42_strict | π0.5 | L2norm | 0.85 | Long | cqa1-33015 |
| eval_pi05_l2norm_k085_long_seed42_strict_w41 | π0.5 | L2norm | 0.85 | Long | westd-41074 |
| eval_pi05_attn_k095_long_seed42_strict_w41 | π0.5 | Attn | 0.95 | Long | westd-41074 |
| eval_pi05_random_k09_long_seed42_strict_v2 | π0.5 | Random | 0.90 | Long | westd-41074 |
| eval_pi05_random_k07_long_seed42_strict_v2 | π0.5 | Random | 0.70 | Long | cqa1-33015 |
| eval_pi05_random_k05_long_seed42_strict_w41_v2 | π0.5 | Random | 0.50 | Long | westd-41074 |

## Truly Missing (need new experiments, 9 cells)

### OpenVLA Object (4)
- L2norm k=0.75
- Attn k=0.50
- Random k=0.85
- Random k=0.50

### OpenVLA Goal (2)
- Attn k=0.70
- Random k=0.95

### OpenVLA Long (3)
- L2norm k=0.50
- Random k=0.75 (metrics lost from previous run)
- Random k=0.50

### π0.5 Long strict (0 truly missing, 7 cells using approximate values without strict re-run planned)
- L2norm k=0.75 (~73.4%)
- L2norm k=0.70 (~62.6%)
- L2norm k=0.50 (~50.2%)
- Attn k=0.75 (~51.8%)
- Attn k=0.70 (~50.8%)
- Attn k=0.50 (~49.8%)
- Random k=0.85 (~45.2%)
