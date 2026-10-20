# Eval Data Inventory for Pooled IRT Redesign
**Date**: 2026-05-15 | **Target**: N≥16 models, balanced dosage, d000 included

---

## 1. Currently Running Evals (6 GPUs active)

| GPU | PID | Eval | Checkpoint α |
|-----|---------|------|------|
| 0 | 566224 | 1.5B_d005_s123_aligned | 32 ✅ |
| 1 | 566311 | 1.5B_d025_s123_aligned | 32 ✅ |
| 2 | 580698 | 3B_d005_s123_aligned | 32 ✅ |
| 3 | 576735 | 3B_d025_s123_aligned | 32 ✅ |
| 4 | 584233 | 3B_d005_s123_para_aligned | 32 ✅ |
| 5 | 584315 | 3B_d025_s123_para_aligned | 32 ✅ |

All 6 use alpha=32 checkpoints. 4 are aligned evals (contribute to IRT), 2 are para_aligned.

---

## 2. Aligned Eval Coverage Matrix (Canonical, alpha=32 only)

### Full Grid: 3 sizes × 4 dosages × 2 seeds = 24 cells

| Size | d000 s42 | d000 s123 | d005 s42 | d005 s123 | d025 s42 | d025 s123 | d100 s42 | d100 s123 |
|------|----------|-----------|----------|-----------|----------|-----------|----------|-----------|
| 0.5B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 1.5B | ✅ | ✅ | ✅ | 🔄 GPU0 | ✅ | 🔄 GPU1 | ✅ | ✅ |
| 3B | ✅ | ✅ | ✅ | 🔄 GPU2 | ❌ retrain | 🔄 GPU3 | ❌ retrain | ❌ retrain |

**Legend**: ✅ = eval complete (4 benchmarks) | 🔄 = running | ❌ = needs SFT retrain (alpha=16→32, per D055)

### Summary
- **Now**: 18/24 complete
- **After running evals finish**: 22/24 complete
- **Blocked (need 3B retrain)**: d025_s42, d100_s42, d100_s123

---

## 3. Accuracy Table — All Usable Aligned Evals

| Model | MMLU | GSM8K | ARC | HumanEval |
|-------|------|-------|-----|-----------|
| **0.5B_d000_s42** | .398 | .369 | .469 | .110 |
| **0.5B_d000_s123** | .422 | .341 | .497 | .104 |
| **0.5B_d005_s42** | .325 | .362 | .328 | .079 |
| **0.5B_d005_s123** | .300 | .368 | .298 | .098 |
| **0.5B_d025_s42** | .280 | .366 | .325 | .122 |
| **0.5B_d025_s123** | .347 | .353 | .406 | .085 |
| **0.5B_d100_s42** | .233 | .365 | .294 | .000 |
| **0.5B_d100_s123** | .306 | .380 | .367 | .104 |
| **1.5B_d000_s42** | .585 | .654 | .772 | .128 |
| **1.5B_d000_s123** | .585 | .654 | .758 | .171 |
| **1.5B_d005_s42** | .585 | .648 | .769 | .128 |
| **1.5B_d025_s42** | .590 | .654 | .769 | .128 |
| **1.5B_d100_s42** | .593 | .650 | .769 | .128 |
| **1.5B_d100_s123** | .596 | .644 | .782 | .171 |
| **3B_d000_s42** (v3) | .634 | .120 | .828 | .146 |
| **3B_d000_s123** | .633 | .181 | .833 | .128 |
| **3B_d005_s42** | .634 | .208 | .829 | .146 |
| **3B_d100_v2_s123** ⚠️α16 | .632 | .732 | .831 | .183 |
| **3B_d100_v2_s42** ⚠️α16 | .632 | .741 | .824 | .195 |
| **3B_d025_v2** ⚠️α16 | .600 | .679 | .828 | .134 |

⚠️ Last 3 rows use alpha=16 checkpoints — usable as-is if alpha consistency is relaxed, otherwise wait for retrain.

---

## 4. D045 Exclusion Rule

**Decision**: 0.5B MMLU/ARC excluded from IRT pooling (position bias: d000 A=46% → d100 A=98%).
- 0.5B GSM8K/HumanEval: **included** (free-form, unaffected)
- 1.5B/3B all benchmarks: **included**

---

## 5. Per-Benchmark N Counts

### Scenario A: Right now (only complete alpha=32 evals)

| Benchmark | 0.5B | 1.5B | 3B | **Total N** |
|-----------|------|------|----|-------------|
| MMLU | ~~8~~ D045 | 6 | 3 | **9** |
| ARC | ~~8~~ D045 | 6 | 3 | **9** |
| GSM8K | 8 | 6 | 3 | **17** |
| HumanEval | 8 | 6 | 3 | **17** |

### Scenario B: After running evals complete (+4 aligned)

| Benchmark | 0.5B | 1.5B | 3B | **Total N** |
|-----------|------|------|----|-------------|
| MMLU | ~~8~~ | 8 | 5 | **13** |
| ARC | ~~8~~ | 8 | 5 | **13** |
| GSM8K | 8 | 8 | 5 | **21** |
| HumanEval | 8 | 8 | 5 | **21** |

### Scenario C: After 3B retrain + eval (full 24-model grid)

| Benchmark | 0.5B | 1.5B | 3B | **Total N** |
|-----------|------|------|----|-------------|
| MMLU | ~~8~~ | 8 | 8 | **16** |
| ARC | ~~8~~ | 8 | 8 | **16** |
| GSM8K | 8 | 8 | 8 | **24** |
| HumanEval | 8 | 8 | 8 | **24** |

### Scenario B': If we include alpha=16 3B evals as-is

| Benchmark | 0.5B | 1.5B | 3B | **Total N** |
|-----------|------|------|----|-------------|
| MMLU | ~~8~~ | 8 | 8 | **16** |
| ARC | ~~8~~ | 8 | 8 | **16** |
| GSM8K | 8 | 8 | 8 | **24** |
| HumanEval | 8 | 8 | 8 | **24** |

---

## 6. Para_Aligned Eval Coverage (for ConStat control)

| Size | d000 s42 | d000 s123 | d005 s42 | d005 s123 | d025 s42 | d025 s123 | d100 s42 | d100 s123 |
|------|----------|-----------|----------|-----------|----------|-----------|----------|-----------|
| 0.5B | ✅ | — | ✅ | ✅ | ✅ | — | — | — |
| 1.5B | ✅ | — | ✅ | — | ✅ | — | ✅ | — |
| 3B | ✅ | ❌α16 | ✅ | 🔄 GPU4 | ❌α16 | 🔄 GPU5 | ❌α16 | — |

Para coverage is sparser: s123 variants mostly missing for 0.5B/1.5B.

---

## 7. Design Recommendation for Pooled IRT

### Option 1: Proceed now with Scenario B (after running evals, ~hours)
**N=13 for MMLU/ARC, N=21 for GSM8K/HumanEval**

Models included:
- 0.5B: 8 models (d000×2, d005×2, d025×2, d100×2) — GSM8K/HumanEval only
- 1.5B: 8 models (full grid)
- 3B: 5 models (d000×2, d005×2, d025_s123)

**Pros**: Can start immediately after running evals finish. d000 included. N=13 is borderline acceptable for per-benchmark fit.
**Cons**: 3B missing d025_s42 and all d100 (dosage imbalance). MMLU/ARC N=13 is marginal.

### Option 2: Include alpha=16 evals as-is (Scenario B')
**N=16 for MMLU/ARC, N=24 for GSM8K/HumanEval**

Same as above + add 3B alpha=16 evals: d025_v2(s42), d100_v2_s42, d100_v2_s123

**Pros**: Hits N≥16 target. Balanced dosage. Full design.
**Cons**: Alpha inconsistency (3 out of 8 3B models at alpha=16 vs 32). May introduce systematic confound: alpha=16 LoRA has different capacity → different contamination absorption → biased gamma estimates.

### Option 3: Wait for 3B retrain (Scenario C, needs ~2-3 days)
**N=16 for MMLU/ARC, N=24 for GSM8K/HumanEval**

**Pros**: Clean, consistent alpha=32 across all models. Best for publication.
**Cons**: Blocks IRT work for days.

### Recommended: Option 2 now, Option 3 for final results
1. **Immediately**: run pooled IRT with alpha=16 evals included → fast iteration on model convergence
2. **In parallel**: retrain 3B d025_s42, d100_s42, d100_s123 at alpha=32
3. **Final paper**: re-fit with clean alpha=32 data

### Per-Benchmark Model Lists (Option 2, after running evals)

**MMLU** (N=16): 1.5B_d000_s42, 1.5B_d000_s123, 1.5B_d005_s42, 1.5B_d005_s123, 1.5B_d025_s42, 1.5B_d025_s123, 1.5B_d100_s42, 1.5B_d100_s123, 3B_d000_s42, 3B_d000_s123, 3B_d005_s42, 3B_d005_s123, 3B_d025_s42*, 3B_d025_s123, 3B_d100_s42*, 3B_d100_s123*

**ARC** (N=16): same as MMLU

**GSM8K** (N=24): all 8 × 0.5B + all 8 × 1.5B + all 8 × 3B (same list as MMLU + 8 × 0.5B)

**HumanEval** (N=24): same as GSM8K

*asterisk = alpha=16 checkpoint

### Models to exclude
- **0.5B MMLU/ARC**: D045 position bias
- **3B d000_v2 evals**: deprecated (alpha=16, redundant with alpha=32 originals)
- **All DEPRECATED dirs**: already excluded
- **All _raw and _base_pretrained evals**: not part of experimental grid
- **Instruct eval**: different model class
