# check full status 20260517

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full_status_20260517_20260517T115450_result.json`
- **Structured JSON:** [`1f00f190a96b0a5ab8b9.json`](../../sessions/1f/1f00f190a96b0a5ab8b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Status Report

### GPU
| GPU | Process | VRAM | Util | Temp |
|-----|---------|------|------|------|
| 0 | exp_001 (PID 59365) | 65.9/97.9 GB | 96% | 78°C |
| 1 | exp_003 (PID 88161) | 23.7/97.9 GB | 97% | 81°C |

Both GPUs fully loaded, running normally.

---

### exp_001: **RUNNING** — Gen 8/9 (training, Step ~1600)

Results JSON has Gen 0-7 complete. Gen 8 fine-tuning in progress. Still needs: Gen 8 eval + Gen 9 train+eval.

**Phase 0 Data Table (Gen 0-7):**

| Gen | eff_rank | log_det | ppl | distinct_4 | train_loss |
|-----|----------|---------|-----|------------|------------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.741 | — |
| 1 | 491.77 | 2464.76 | 11.38 | 0.626 | 1.623 |
| 2 | 496.44 | 2469.93 | 13.58 | 0.515 | 1.268 |
| 3 | 493.31 | 2440.57 | 16.25 | 0.490 | 1.134 |
| 4 | 485.67 | 2405.05 | 19.80 | 0.468 | 1.098 |
| 5 | 479.21 | 2370.17 | 24.59 | 0.463 | 1.047 |
| 6 | 473.00 | 2335.17 | 30.91 | 0.466 | 1.025 |
| 7 | 464.20 | 2304.19 | 38.89 | 0.447 | 1.015 |

Clear model collapse trajectory: log_det peaked at Gen 2 (2469.93) then monotonically decreasing. PPL 4x degradation (9.55 → 38.89). distinct_4 dropped from 0.741 → 0.447. Train loss converging toward 1.0 (memorization signal).

---

### exp_003: **RUNNING** — Gen 2/10 (training, Step ~3400), controller **TRIGGERED**

Results JSON has Gen 0-1 complete. Gen 2 fine-tuning in progress with mix_ratio = 0.5625.

**Phase 1 Adaptive Data (Gen 0-1):**

| Gen | eff_rank | log_det | ppl | distinct_4 | train_loss | mix_ratio |
|-----|----------|---------|-----|------------|------------|-----------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.741 | — | — |
| 1 | 479.49 | 2356.68 | 10.01 | 0.711 | 1.983 | 0.5 |

**Controller analysis:**
- Δ(0→1) = (2366.68 - 2356.68) / 2366.68 = **0.00423**
- τ = 0.005, so 0.003 ≤ Δ < 0.005 — near threshold
- Gen 1 mix_ratio = 0.5 (at boundary); Gen 2 already at 0.5625 → controller is actively increasing real data proportion
- No controller_log.json found at the expected path

**exp_003 vs exp_001 at Gen 1:**
| Metric | exp_001 (pure synth) | exp_003 (adaptive) |
|--------|---------------------|--------------------|
| log_det | 2464.76 (+4.1%) | 2356.68 (-0.4%) |
| ppl | 11.38 | 10.01 |
| distinct_4 | 0.626 | 0.711 |

The adaptive controller with real data mixing is dramatically better at preserving quality: log_det barely dropped (vs +4.1% spike in pure synthetic), diversity preserved at 0.711 vs 0.626.

---

**Summary:**
- **exp_001**: ~2 generations remaining (Gen 8 training + Gen 9). Estimated completion in a few hours.
- **exp_003**: 8 generations remaining (Gen 2 training + Gen 3-9). Controller is active, increasing real data ratio. Early results are promising.
- No action taken per instructions — exp_004 not started.

---
