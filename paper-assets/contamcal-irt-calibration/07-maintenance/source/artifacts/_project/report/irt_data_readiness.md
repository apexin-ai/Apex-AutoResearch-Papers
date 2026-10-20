# IRT Data Readiness Report
**Date**: 2026-05-15
**Goal**: Compile N≥16 pooled IRT input data for per-benchmark independent fits (D053)

## Summary

| Benchmark | N (alpha=32) | Target | Status | Gap |
|-----------|-------------|--------|--------|-----|
| MMLU | 12 | 16 | **BLOCKED** | -4 |
| GSM8K | 15 | 16 | **BLOCKED** | -1 |
| ARC-Challenge | 12 | 16 | **BLOCKED** | -4 |
| HumanEval | 20 | 16 | READY (appendix only, D009) | — |

**Verdict**: Cannot start pooled IRT fitting yet. 3B alpha=32 reruns + 1 missing eval block all main benchmarks.

---

## 1. Available IRT-Eligible Models (alpha=32, aligned, non-deprecated)

### 0.5B — 8 models (all alpha=32) ✓
| Dosage | s42 | s123 |
|--------|-----|------|
| d000 | ✓ | ✓ |
| d005 | ✓ | ✓ |
| d025 | ✓ | ✓ |
| d100 | ✓ | ✓ |

### 1.5B — 8 models (all alpha=32) ✓
| Dosage | s42 | s123 |
|--------|-----|------|
| d000 | ✓ | ✓ |
| d005 | ✓ | ✓ |
| d025 | ✓ | ✓ |
| d100 | ✓ | ✓ |

### 3B — 4 models available (alpha=32 with aligned eval)
| Dosage | s42 | s123 |
|--------|-----|------|
| d000 | **MISSING eval** | ✓ (v1) |
| d005 | ✓ | ✓ |
| d025 | **RERUN pending** | ✓ |
| d100 | **RERUN pending** | **RERUN pending** |

**Total available**: 20 models

---

## 2. Per-Benchmark N After Exclusions

Exclusion rules applied:
- D044: GSM8K excludes d000 (format confound)
- D045: 0.5B excluded from MMLU/ARC (position bias)
- D046/D047: base_pretrained excluded
- D018: 3B d000_s42_v3 excluded (LoRA damage, dirname doesn't match regex → auto-excluded)

| Benchmark | 0.5B | 1.5B | 3B | Total | Target |
|-----------|------|------|----|-------|--------|
| MMLU | 0 (D045) | 8 | 4 | **12** | 16 |
| GSM8K | 6 (no d000) | 6 (no d000) | 3 (no d000) | **15** | 16 |
| ARC-Challenge | 0 (D045) | 8 | 4 | **12** | 16 |
| HumanEval | 8 | 8 | 4 | **20** ✓ | 16 |

---

## 3. Blocking Items

### 3.1 3B Alpha=32 SFT Reruns (3 checkpoints)
Per D055/D066/D067: d025_s42, d100_s42, d100_s123 trained with alpha=16, must be retrained with alpha=32.

| Checkpoint | Training Status | Eval Status |
|-----------|----------------|-------------|
| `Qwen2.5-3B_d025_a32_s42` | **~2% (68/3384 steps)**, ~4h remaining | Not started |
| `Qwen2.5-3B_d100_a32_s42` | lora_adapter empty, **not started or failed** | Not started |
| `Qwen2.5-3B_d100_a32_s123` | lora_adapter empty, **not started or failed** | Not started |

### 3.2 Missing Aligned Eval (1 checkpoint)
| Checkpoint | Alpha | Checkpoint Status | Eval Status |
|-----------|-------|------------------|-------------|
| `Qwen2.5-3B_d000_s42` | 32 ✓ | Complete | **Aligned eval not run** |

Note: Non-aligned eval exists (MMLU=0.634, GSM8K=0.117, ARC=0.822). GSM8K=0.117 is the known CoT collapse (D018) — irrelevant since D044 excludes d000 from GSM8K anyway.

### 3.3 Resolution Path
When all 4 blocking items resolved, 3B goes from 4→8 alpha=32 models:

| Benchmark | Current N | After fix | Target |
|-----------|----------|-----------|--------|
| MMLU | 12 | **16** ✓ | 16 |
| GSM8K | 15 | **18** ✓ | 16 |
| ARC-Challenge | 12 | **16** ✓ | 16 |
| HumanEval | 20 | **24** ✓ | 16 |

---

## 4. Alpha Consistency (D055)

Verified via `adapter_config.json` on all 3B checkpoints:

| Checkpoint | lora_alpha | Status |
|-----------|-----------|--------|
| d000_s42 | 32 | ✓ use original |
| d000_s123 | 32 | ✓ use original |
| d000_v2_s42 | 16 | DEPRECATED (D055) |
| d000_v2_s123 | 16 | DEPRECATED (D055) |
| d005_s42 | 32 | ✓ |
| d005_s123 | 32 | ✓ |
| d025_s123 | 32 | ✓ |
| d025_s42 | **16** | RERUN → d025_a32_s42 |
| d100_s42 | **16** | RERUN → d100_a32_s42 |
| d100_s123 | **16** | RERUN → d100_a32_s123 |

**Warning**: The existing `run_irt_calibration.py` and `run_pooled_4bench_irt.py` do NOT filter by alpha. Without modification, they will load alpha=16 3B v2 evals (d000_v2_s42, d000_v2_s123) alongside alpha=32 models, violating D055. The IRT script needs either:
1. An explicit alpha filter/exclusion list, or
2. Renaming/removing alpha=16 eval dirs before running

---

## 5. Para_Aligned Coverage (Non-blocking for IRT)

Para_aligned evals are needed for contamination gap signal (exp002), NOT for IRT correctness matrix. Missing items listed for completeness:

| Scale | Missing para_aligned |
|-------|---------------------|
| 0.5B | d000_s123, d025_s123, d100_s42, d100_s123 |
| 1.5B | d000_s123, d005_s123, d025_s123, d100_s123 |
| 3B | d000_s123, d025_s42, d100_s42, d100_s123 |

Total: 12 missing para_aligned evals across scales (all s123 seeds underrepresented).

---

## 6. Data Format Validation

All eval results use consistent format:
- Path: `/root/autodl-tmp/exp001/eval_results/{dirname}/eval_results.json`
- Structure: `{"benchmarks": {"mmlu": {"accuracy": float, "per_item": [{"correct": bool, ...}]}}}`
- Item counts: MMLU=14042, GSM8K=1319, ARC-C=1172, HumanEval=164 (consistent across all models)
- Para_aligned item counts: MMLU=6596, GSM8K=228, ARC-C=697, HumanEval=26

---

## 7. Existing IRT Scripts

| Script | Purpose | Status |
|--------|---------|--------|
| `exp006/run_irt_calibration.py` | Core IRT fitting (Stan MCMC) | Ready, needs alpha filter |
| `exp006/run_pooled_4bench_irt.py` | Pooled multi-scale IRT with exclusions | Ready, needs alpha filter |
| `exp006/run_stratified_irt.py` | Stratified IRT (abandoned per D053) | Not needed |
| `scripts/gen_eval_matrix.py` | Eval summary CSV generation | Ready |

---

## 8. Recommended Next Steps

1. **Immediate**: Run aligned eval on `Qwen2.5-3B_d000_s42` checkpoint (alpha=32, already trained) → +1 model
2. **Check**: Verify d100_a32_s42 and d100_a32_s123 training status — lora_adapter dirs empty, may need restart
3. **Wait**: d025_a32_s42 training at ~2%, ~4h remaining
4. **Before IRT fitting**: Add alpha=16 exclusion to IRT scripts OR rename/archive alpha=16 eval dirs
5. **After all blocking items resolved**: Run per-benchmark IRT with N=16-24 models
