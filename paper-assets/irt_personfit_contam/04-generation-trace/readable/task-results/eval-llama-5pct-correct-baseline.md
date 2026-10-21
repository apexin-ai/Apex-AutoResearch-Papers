# eval llama 5pct correct baseline

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_llama-5pct-correct-baseline_20260524T043305_result.json`
- **Structured JSON:** [`f12f1c235bf5f3ee8382.json`](../../sessions/f1/f12f1c235bf5f3ee8382.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the complete summary:

---

## eval_lz.py Fix

**Bug**: Lines 170-184 hardcoded only `contam_15/25/50` seen_items paths. `contam_5` fell through to `else: seen_set = set()`, so all 702 seen items were treated as unseen.

**Fix**: Replaced with regex-based lookup `re.search(r'contam_(\d+)', args.condition)` → loads `seen_items_{pct}pct.json` dynamically. Works for any contamination percentage.

---

## Contam_5 Results (Llama-3.1-8B-Instruct)

| 指标 | Overall | Seen (702) | Unseen (13340) |
|------|---------|------------|----------------|
| Accuracy | 0.6342 | 0.7920 | 0.6259 |
| lz* (free-θ) | **-4.954** | -1.420 | -4.568 |
| lz* (fixed-θ) | **-1.892** | -0.270 | -1.880 |

## Cohen's d（Llama clean baseline: **mean=0.262, SD=1.542**）

| 类型 | Overall | Seen | Unseen |
|------|---------|------|--------|
| free-θ | **-3.38** | -1.09 | -3.13 |
| fixed-θ | **-1.65** | — | — |

Fixed-θ baseline: mean=0.597, SD=1.509 (10 clean seeds)

## theta_fixed_llama.json

已更新，新增 contam_5 条目：
- `lz_star_fixed = -1.892`
- `delta_lz_star_fixed = -2.737`（相对 clean 的 0.845）

---
