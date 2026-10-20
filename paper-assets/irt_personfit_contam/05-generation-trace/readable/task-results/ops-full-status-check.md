# ops full status check

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-status-check_20260523T123735_result.json`
- **Structured JSON:** [`8c4efdda2a761a3845c4.json`](../../sessions/8c/8c4efdda2a761a3845c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Comprehensive Status Report — westd-35694

### GPU State

| GPU | Memory Used | Memory Total | Utilization |
|-----|------------|--------------|-------------|
| 0 | 32,687 MiB | 97,887 MiB | 96% |
| 1 | 0 MiB | 97,887 MiB | 0% (eval loading) |
| 2 | 0 MiB | 97,887 MiB | 0% (eval loading) |
| 3 | 0 MiB | 97,887 MiB | 0% (free) |

**Disk:** 92G/250G used, **159G free** (37%)

---

### Active Processes

1. **Training:** `mistral contam_25 s1` — step **863/1596 (54%)**, ~37 min elapsed, ETA ~55 min. Loss ~1.35, token accuracy ~0.67. (GPU 0, tmux `exp-mistral-25pct-s1`)

2. **Eval batch pipeline (GPU 0, pts/4):** sequential chain:
   - `llama contam_5` — **DONE** (result saved)
   - `llama contam_25` — **RUNNING** (~3000/14042, 21%)
   - `mistral contam_5` — **PENDING**

3. **Nohup eval (GPU 1):** `llama contam_25` — still loading weights (duplicate of batch pipeline #2)

4. **Nohup eval (GPU 2):** `mistral contam_5` — still loading weights

---

### Checkpoints Inventory

| Model | contam_5 | contam_5_s2 | contam_15_s2 | contam_15_s3 | contam_25 | contam_25_s2 | contam_50_s2 | contam_50_s3 |
|-------|----------|-------------|--------------|--------------|-----------|--------------|--------------|--------------|
| Llama | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Mistral | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ (training) | ✅ | ✅ |
| Legacy (Qwen) | ✅ | — | ✅ | ✅ | ✅ (+ s2, s3) | — | ✅ | ✅ (+s1) |

---

### Eval Results (Llama & Mistral, new eval_lz)

| Model | Condition | acc_overall | acc_seen | acc_unseen | lz\*_seen | lz\*_unseen | theta_mle | lz\* | Status |
|-------|-----------|------------|----------|------------|-----------|-------------|-----------|------|--------|
| **Llama** | contam_5 | 0.638 | 0.801 | 0.629 | -0.610 | -4.398 | -0.407 | -4.695 | ✅ Done |
| **Llama** | contam_15_s2 | 0.658 | 0.774 | 0.638 | -2.093 | -3.673 | -0.319 | -4.680 | ✅ Done |
| **Llama** | contam_50_s2 | 0.708 | 0.765 | 0.650 | -1.560 | -2.473 | -0.086 | -3.735 | ✅ Done |
| **Llama** | contam_25 | — | — | — | — | — | — | — | 🔄 Running (21%) |
| **Llama** | contam_5_s2 | — | — | — | — | — | — | — | ⏳ Not started |
| **Llama** | contam_15_s3 | — | — | — | — | — | — | — | ⏳ Not started |
| **Llama** | contam_25_s2 | — | — | — | — | — | — | — | ⏳ Not started |
| **Llama** | contam_50_s3 | — | — | — | — | — | — | — | ⏳ Not started |
| **Mistral** | contam_15_s2 | 0.605 | 0.768 | 0.576 | -2.363 | -2.571 | -0.611 | -4.141 | ✅ Done |
| **Mistral** | contam_50_s2 | 0.677 | 0.750 | 0.603 | -1.638 | -2.883 | -0.272 | -4.695 | ✅ Done |
| **Mistral** | contam_5 | — | — | — | — | — | — | — | 🔄 Loading weights |
| **Mistral** | contam_25 | — | — | — | — | — | — | — | ⏳ Training (54%) |
| **Mistral** | contam_5_s2 | — | — | — | — | — | — | — | ⏳ Not started |
| **Mistral** | contam_15_s3 | — | — | — | — | — | — | — | ⏳ Not started |
| **Mistral** | contam_25_s2 | — | — | — | — | — | — | — | ❌ No checkpoint yet |
| **Mistral** | contam_50_s3 | — | — | — | — | — | — | — | ⏳ Not started |

---

### Key Observations

- **Duplicate eval:** `llama contam_25` is running in both the batch pipeline (GPU 0) and a nohup process (GPU 1) — one is redundant.
- **GPU contention on GPU 0:** training (mistral contam_25) and eval (llama contam_25 batch) are sharing GPU 0 — likely slowing both down.
- **5 completed evals** across both models, **~11 remaining** (assuming all checkpoint×model combos need eval).
- Mistral `contam_25` training is 54% done — checkpoint expected in ~55 min, after which its evals can begin.

---
