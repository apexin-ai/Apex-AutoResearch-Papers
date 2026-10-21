# 3B RRF Aggregation Readiness Check

**Date**: 2026-05-16
**Script**: `/root/contamcal-irt-calibration/exp003/rrf_aggregation.py`

## Status: PARTIALLY READY — needs minor filter + signal completion

## 1. Script Functionality

**Dry-run result: PASS** — script processes 3B signal directories without errors.

- Regex `_DIR_RE` correctly parses all 3B dir names (including `_v3`, `_a32` suffixes)
- `detect_available_signals()` dynamically uses only available signals (s3 absence handled gracefully)
- `SKIP_PATTERNS = ["DEPRECATED"]` filters `d025_s42_DEPRECATED_alpha16`
- `--generate-exposure` mode produces correct output structure

## 2. Required Modification

**Problem**: Script includes blacklisted alpha=16 directories (C006 violation).

The dry-run showed these alpha=16 dirs being processed:
- `Qwen2.5-3B_d000_v2_s42` (uses s1+s2+s3, wrong signal set)
- `Qwen2.5-3B_d005_s42` (alpha=16)
- `Qwen2.5-3B_d025_s42` (alpha=16, only has s4_mmlu)
- `Qwen2.5-3B_d100_s42` (alpha=16)

**Fix options**:
1. **Recommended**: Add alpha=16 blacklist to SKIP_PATTERNS:
   ```python
   SKIP_PATTERNS = ["DEPRECATED", "Qwen2.5-3B_d000_v2_s42", "Qwen2.5-3B_d005_s42",
                    "Qwen2.5-3B_d025_s42", "Qwen2.5-3B_d100_s42"]
   ```
2. Or add `--model-size` CLI filter (more work, less urgent)

## 3. 3B Signal File Status (alpha=32 valid directories only)

| Directory | s1 (m/g/a) | s2 (m/g/a) | s4 (m/g/a) | RRF-ready? |
|-----------|:----------:|:----------:|:----------:|:----------:|
| **d000_s123** (NO signal dir) | ✗/✗/✗ | ✗/✗/✗ | ✗/✗/✗ | ✗ BLOCKED |
| **d005_s123** | ✓/✓/✓ | ✓/✓/✓ | ✓/✓/✓ | ✓ COMPLETE |
| **d025_s123** | ✓/✓/✓ | ✓/✓/✓ | ✓/✓/✗ | ~90% (s4_mmlu chunking in progress) |
| **d025_v3_s42** | ✓/✓/✓ | ✓/✓/✓ | ✗/✗/✗ | ✗ s4 missing entirely |
| **d100_a32_s123** | ✓/✗/✗ | ✓/✗/✗ | ✗/✗/✗ | ✗ only mmlu s1/s2 |
| **d100_a32_s42** (NO signal dir) | ✗/✗/✗ | ✗/✗/✗ | ✗/✗/✗ | ✗ BLOCKED |

Legend: m=mmlu, g=gsm8k, a=arc_challenge

## 4. Blocking Conditions for Full 3B RRF

**Minimum viable** (1 seed per dosage, s1+s2 only):
- Need d000_s123 signals (s1+s2 for 3 benchmarks)
- Need d100_a32_s123 signals (s1+s2 for gsm8k, arc_challenge)

**Full target** (s1+s2+s4, all dosages, all benchmarks):
- d000_s123: all 9 signal files needed
- d025_s123: s4_selfcritique_mmlu.json (in progress via chunking)
- d025_v3_s42: all 3 s4 files needed
- d100_a32_s123: s1/s2 for gsm8k+arc, all 3 s4 files
- d100_a32_s42: all 9 signal files

## 5. Dry-Run Output (d005_s123, --limit 10)

```
Saved 10 items to rrf_scores_Qwen2.5-3B_d005_s123_mmlu.json
Saved 10 items to rrf_scores_Qwen2.5-3B_d005_s123_gsm8k.json
Saved 10 items to rrf_scores_Qwen2.5-3B_d005_s123_arc_challenge.json
```

Output correctly uses s1+s2+s4 (no s3), produces normalized exposure in [0,1].

## 6. Recommended Execution Command (once signals complete)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/contamcal-irt-calibration/exp003
python rrf_aggregation.py \
  --signal-root /root/autodl-tmp/exp002/signals \
  --benchmarks mmlu gsm8k arc_challenge \
  --output-dir /root/autodl-tmp/exp003/rrf_3B \
  --generate-exposure \
  --csv
```

Note: Must apply SKIP_PATTERNS fix first to exclude alpha=16 dirs.
