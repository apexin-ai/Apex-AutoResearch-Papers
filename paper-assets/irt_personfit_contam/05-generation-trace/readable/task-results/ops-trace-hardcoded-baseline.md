# ops trace hardcoded baseline

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_trace-hardcoded-baseline_20260523T141650_result.json`
- **Structured JSON:** [`aec631592a58fa049b84.json`](../../sessions/ae/aec631592a58fa049b84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete analysis:

---

## 1. Hardcoded baseline code segment

**File**: `ctrl_contam_llama/compute_cohens_d.py` (created May 22, 13:17)
```python
clean_lz_stars = np.array([
    -0.4891, -0.7793, 0.4109, 0.6498, -0.3043,
    -1.1483, 0.1419, 0.7175, -0.3718, -1.9506
])
clean_mean = clean_lz_stars.mean()   # -0.31233
clean_std = clean_lz_stars.std(ddof=1)  # 0.840
```

Same values also appear in:
- `/root/autodl-tmp/bca_bootstrap.py` (created May 22, 05:39) — labeled `# Llama MMLU free-theta`
- `/root/autodl-tmp/anon_repo/llama/compute_cohens_d.py` (git commit May 23, 20:57)
- `contam_25_cohens_d.json` (output, May 22, 14:02)

## 2. Git history

**No git repo** in `ctrl_contam_llama/` or `ctrl_contam_pilot/`. The only git history is `anon_repo/` with a single commit:
```
5fe69c3 "Anonymous submission for review" (2026-05-23 20:56:51)
```
This commit includes the hardcoded values as-is. No revision history.

## 3. Hardcoded vs current result files

| Seed | Hardcoded | Current file | File date | Match? |
|------|-----------|-------------|-----------|--------|
| s1 | -0.4891 | 0.8446 | May 21 07:17 | **NO** |
| s2 | -0.7793 | -0.1823 | May 21 09:26 | **NO** |
| s3 | 0.4109 | 0.3452 | May 23 21:57 | **NO** |
| s4 | 0.6498 | 0.0206 | May 21 20:40 | **NO** |
| s5 | -0.3043 | 1.7323 | May 21 20:41 | **NO** |
| s6 | -1.1483 | 2.8466 | May 23 22:02 | **NO** |
| s7 | 0.1419 | -0.4007 | May 21 20:42 | **NO** |
| s8 | 0.7175 | 1.1656 | May 21 22:30 | **NO** |
| s9 | -0.3718 | 0.1897 | May 23 22:10 | **NO** |
| s10 | -1.9506 | -2.2497 | May 21 22:32 | **NO** |

**None of the 10 values match** — not even the files from May 21 (pre-modification).

## 4. Re-eval progress

4 GPUs running. Status from `/tmp/eval_clean_status.log`:
- **Completed**: clean_s3, clean_s6, clean_s9, contam_15_s1
- **In progress**:
  - GPU 0: clean_s7 (~10500/14042, ~75%)
  - GPU 1: clean (s1) (~12500/14042, ~89%)
  - GPU 2: clean_s4 (~13000/14042, ~93%)
  - GPU 3: clean_s10 (~7000/14042, ~50%)
- **Not yet started**: clean_s2, clean_s5, clean_s8

## 5. Source analysis

**Timeline**:
1. **May 21, 04:26** — `eval_lz.py` created (V0)
2. **May 21, 07:08–22:32** — All clean seed evaluations run (s1 through s10), results saved
3. **May 22, 05:39** — `bca_bootstrap.py` created with hardcoded values (first appearance of these numbers)
4. **May 22, 13:13** — `eval_lz.py` **modified** (V1 → the eval logic changed)
5. **May 22, 13:17** — `compute_cohens_d.py` created (copies values from bca_bootstrap.py)
6. **May 23, 21:35** — V2 re-evaluation started on 4 GPUs

**Conclusion**: The hardcoded values were produced by the **original V0 version of `eval_lz.py`** (born May 21 04:26, modified May 22 13:13). The result files from May 21 currently on disk already reflect a different run from the one that produced the hardcoded values — the original V0 results were **overwritten** by intermediate re-evaluations. The values were manually transcribed into `bca_bootstrap.py` on May 22 (likely from terminal output or notes, since no JSON preserves them). No backup files or version control exists to recover the original outputs. The eval_lz.py modification on May 22 likely changed the lz* computation logic, making all subsequent evaluations produce different results.

---
