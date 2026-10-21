# Signal Coverage Audit — 2026-05-16 ~19:00 UTC

## Coverage Matrix

Legend: ✅ = complete, ❌ = missing, 🔄 = in progress

### 0.5B Models (seed=s42, older naming)

| Model Dir | mmlu s1 | mmlu s2 | mmlu s4 | gsm8k s1 | gsm8k s2 | gsm8k s4 | arc s1 | arc s2 | arc s4 | Status |
|-----------|---------|---------|---------|----------|----------|----------|--------|--------|--------|--------|
| 0.5B_d000_s42 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |
| 0.5B_d005_s42 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |
| 0.5B_d025_s42 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |
| 0.5B_d100_s42 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |

### 0.5B Models (seed=s123)

| Model Dir | mmlu s1 | mmlu s2 | mmlu s4 | gsm8k s1 | gsm8k s2 | gsm8k s4 | arc s1 | arc s2 | arc s4 | Status |
|-----------|---------|---------|---------|----------|----------|----------|--------|--------|--------|--------|
| 0.5B_d000_s123 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | 8/9 |
| 0.5B_d005_s123 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |
| 0.5B_d025_s123 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |
| 0.5B_d100_s123 | ✅ | ✅ | 🔄 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 2/9 |

### 1.5B Models (seed=s42, older naming)

| Model Dir | mmlu s1 | mmlu s2 | mmlu s4 | gsm8k s1 | gsm8k s2 | gsm8k s4 | arc s1 | arc s2 | arc s4 | Status |
|-----------|---------|---------|---------|----------|----------|----------|--------|--------|--------|--------|
| 1.5B_d000_s42 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |
| 1.5B_d005_s42 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |
| 1.5B_d025_s42 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |
| 1.5B_d100_s42 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |

### 1.5B Models (seed=s123)

| Model Dir | mmlu s1 | mmlu s2 | mmlu s4 | gsm8k s1 | gsm8k s2 | gsm8k s4 | arc s1 | arc s2 | arc s4 | Status |
|-----------|---------|---------|---------|----------|----------|----------|--------|--------|--------|--------|
| 1.5B_d000_s123 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |
| 1.5B_d005_s123 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |
| 1.5B_d025_s123 | ✅ | ✅ | 🔄 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 2/9 |
| 1.5B_d100_s123 | ✅ | ✅ | 🔄 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 2/9 |

### 3B Models (alpha=32, valid)

| Model Dir | mmlu s1 | mmlu s2 | mmlu s4 | gsm8k s1 | gsm8k s2 | gsm8k s4 | arc s1 | arc s2 | arc s4 | Status |
|-----------|---------|---------|---------|----------|----------|----------|--------|--------|--------|--------|
| 3B_d000_a32_s42 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |
| 3B_d005_a32_s42 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |
| 3B_d025_v3_s42 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |
| 3B_d100_a32_s42 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |
| 3B_d005_s123 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |
| 3B_d025_s123 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |
| 3B_d100_a32_s123 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | COMPLETE |

### 3B Models (alpha=16, BLOCKLISTED per C006 — excluded from RRF)

| Model Dir | Notes |
|-----------|-------|
| 3B_d000_v2_s42 | Has s1, s2 + s3_constat only (no s4). EXCLUDED. |
| 3B_d005_s42 | Partial (s1, s2 all; s4 arc only). EXCLUDED. |
| 3B_d025_s42 | Only s4_mmlu + merged_mmlu. EXCLUDED. |
| 3B_d025_s42_DEPRECATED_alpha16 | Partial. EXCLUDED. |
| 3B_d100_s42 | Missing s4_mmlu. EXCLUDED. |
| 3B_d000_s42 | Directory does NOT exist. |

## Summary Statistics

| Category | Complete | In-Progress | Total |
|----------|----------|-------------|-------|
| 0.5B s42 | 4/4 | 0 | 4 |
| 0.5B s123 | 2/4 | 2 | 4 |
| 1.5B s42 | 4/4 | 0 | 4 |
| 1.5B s123 | 2/4 | 2 | 4 |
| 3B alpha=32 | 7/7 | 0 | 7 |
| **Total (valid)** | **19/23** | **4** | **23** |

## Currently Running Processes

| GPU | PID | Model | Task | Progress |
|-----|-----|-------|------|----------|
| 0 | 739125 | 1.5B_d025_s123 | s4_selfcritique mmlu (signal=all) | chunk [10000:11000], 45% (~67% overall s4_mmlu) |
| 2 | 750036 | 1.5B_d100_s123 | s4_selfcritique mmlu | chunks 0-4000 done (~27% overall s4_mmlu) |
| 4 | 752961 | Llama-3.2-3B_d000_s42 | SFT training (not signals) | — |
| 5 | 745695 | 0.5B_d100_s123 | s4_selfcritique mmlu (signal=all) | chunk [5000:6000], 60% (~37% overall s4_mmlu) |

GPU 1, 3 idle.

## Missing Signals (Next Batch)

### Priority 0 — gap in otherwise-complete model:
1. **0.5B_d000_s123** needs `gsm8k s4_selfcritique` (only 1 signal missing; not currently running)

### Priority 1 — in-progress models (after current s4_mmlu finishes):
2. **0.5B_d100_s123** needs: gsm8k (s1, s2, s4) + arc (s1, s2, s4) — 6 signals remaining after s4_mmlu
3. **1.5B_d025_s123** needs: gsm8k (s1, s2, s4) + arc (s1, s2, s4) — 6 signals remaining after s4_mmlu
4. **1.5B_d100_s123** needs: gsm8k (s1, s2, s4) + arc (s1, s2, s4) — 6 signals remaining after s4_mmlu

### Notes:
- The 0.5B v2 batch (GPU 5) uses `--signal all` per model×benchmark. After d100_mmlu finishes, it should cycle to gsm8k/arc for remaining models (including d000_gsm8k which fills the Priority 0 gap).
- 1.5B_d025 (GPU 0) uses `--signal all --benchmark mmlu`; 1.5B_d100 (GPU 2) uses `--signal s4 --benchmark mmlu`. Both only target mmlu — gsm8k/arc will need separate submissions.
- Per C007: 0.5B/1.5B s123 signals have highest priority. Idle GPUs (1, 3) should be used for these, not lower-priority tasks.

## ETA Estimates

Based on observed throughput (~1 it/s for s4 on 0.5B, ~0.9 it/s for 1.5B; 500 iterations per chunk, 15 chunks for mmlu):

| Model | Current GPU | Remaining wall-time (approx) |
|-------|-------------|------------------------------|
| 0.5B_d000_s123 | NONE | ~25 min (just gsm8k s4) |
| 0.5B_d100_s123 | GPU 5 | ~1.5h (finish mmlu s4 + gsm8k all + arc all) |
| 1.5B_d025_s123 | GPU 0 | ~1h (finish mmlu s4) + needs gsm8k/arc submitted separately |
| 1.5B_d100_s123 | GPU 2 | ~2h (finish mmlu s4) + needs gsm8k/arc submitted separately |
