# harvest eval xvla random k05 spatial seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_xvla_random_k05_spatial_seed43_20260524T012028_result.json`
- **Structured JSON:** [`6fe7598fcb17048cecef.json`](../../sessions/6f/6fe7598fcb17048cecef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Results summary:

| Metric | Value |
|--------|-------|
| **Overall SR** | **72.6%** (363/500) |
| **95% Wilson CI** | [68.5%, 76.3%] |
| **Elapsed** | 64.3 min |
| **Conclusion** | success (hypothesis confirmed: random pruning degrades spatial performance) |

**Per-task SR**: T0=100%, T1=38%, T2=88%, T3=92%, T4=88%, T5=0%, T6=94%, T7=68%, T8=92%, T9=66%

**Consistency with seed42** (71.4%): seed43=72.6%, within CI — highly consistent.

**westd-38929 GPU status** (4× RTX PRO 6000 Blackwell, 96GB each):

| GPU | Util | VRAM Used | Status |
|-----|------|-----------|--------|
| 0 | 82% | 4.9/96 GB | active |
| 1 | 0% | 0/96 GB | **free** |
| 2 | 47% | 4.9/96 GB | active |
| 3 | 1% | 4.9/96 GB | mostly idle |

GPU 1 is completely free. GPUs 0/2/3 have ~5GB residual memory — likely leftover from eval (no child process running per task description), could be freed by killing the tmux session.

---
