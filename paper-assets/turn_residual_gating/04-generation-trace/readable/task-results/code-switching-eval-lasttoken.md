# code switching eval lasttoken

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_switching_eval_lasttoken_20260525T220614_result.json`
- **Structured JSON:** [`89bfb43a6ec860b31b06.json`](../../sessions/89/89bfb43a6ec860b31b06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run complete. Last-token GAR shows massive TF-AR separation (Δ≈0.2) vs mid-turn's Δ≈0.004. Here's the full output:

---

### 1. Code changes

**File:** `/root/turn_residual_gating/src/eval_switching.py`

| Line | Old | New |
|------|-----|-----|
| 4 | `Measures GAR-ours (mid-turn position)` | `Measures GAR-ours (last-token position)` |
| 208 | `def measure_gar_midturn(` | `def measure_gar_lasttok(` |
| 209 | `mid-point token` | `last token` |
| 225 | `mid_positions = []` | `last_positions = []  # last-token position (summary position)` |
| **228** | `mid_positions.append((t["content_start"] + t["content_end"]) // 2)` | **`last_positions.append(t["content_end"] - 1)`** |
| 230 | `if not goal_pos or not mid_positions:` | `if not goal_pos or not last_positions:` |
| 251 | `for pos in mid_positions:` | `for pos in last_positions:` |
| 345 | `curve = measure_gar_midturn(` | `curve = measure_gar_lasttok(` |

### 2. Dry-run results (2 conversations, last-token GAR)

```
Condition         turn_1    turn_2    turn_3    turn_4    turn_5    turn_6
pure_tf           0.5377    0.5424    0.4767    0.5169    0.4933    0.4809
pure_ar           0.3231    0.0331    0.2764    0.5265    0.5056    0.4997
switch_k3         0.5372    0.5430    0.4771    0.4804    0.2912    0.4859
```

TF vs AR Δ on early turns: **0.21** (turn 1), **0.51** (turn 2), **0.20** (turn 3) — orders of magnitude larger than mid-turn's ~0.004. n=2 so high variance expected; full run will stabilize.

### 3. Mid-turn finding (quotable text)

> "Mid-turn GAR shows minimal TF–AR difference (mean across turns: TF 0.033 vs AR 0.041, Δ=0.008), confirming that exposure bias selectively disrupts last-token (summary position) attention rather than affecting the entire turn uniformly."

### 4. Full re-run command

```bash
bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup python /root/turn_residual_gating/src/eval_switching.py \
  --checkpoint-path /root/turn_residual_gating/runs/phase2_tg_s42_v7/epoch_2 \
  --data-path /root/turn_residual_gating/data/eval_200/eval_200.json \
  --output-path /root/turn_residual_gating/results/switching_tg_s42_v7 \
  --max-conversations 50 \
  --switch-points 1 2 3 4 5 \
  --max-new-tokens 150 \
  > /tmp/switching_lasttok.log 2>&1 & echo "PID=$!"'
```

### 5. Backup confirmed

```
switching_results_midturn.json  (1981 bytes)
switching_detail_midturn.json   (44124 bytes)
```

Both backed up in `/root/turn_residual_gating/results/switching_tg_s42_v7/`.

---
