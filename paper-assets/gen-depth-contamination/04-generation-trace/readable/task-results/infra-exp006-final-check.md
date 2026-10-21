# infra exp006 final check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp006-final-check_20260515T042918_result.json`
- **Structured JSON:** [`8bb63e904fa77f90fba6.json`](../../sessions/8b/8bb63e904fa77f90fba6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
STATUS: still_running
PROGRESS: 44/51
GPU_STATUS: busy (79%, 18353/24564 MiB)
TMUX: active (exp_006_graduated_filtering)

CURRENT RUN: surprisal_s789 — eval 98% complete

COMPLETED (44):
  base_model              1/1
  no-filter               5/5  (s42 s123 s456 s789 s1024)
  binary-ours             5/5  (s42 s123 s456 s789 s1024)
  binary-drayson          5/5  (s42 s123 s456 s789 s1024)
  graduated_a0.1          5/5  (s42 s123 s456 s789 s1024)
  graduated_a0.3          5/5  (s42 s123 s456 s789 s1024)
  graduated_a0.5          5/5  (s42 s123 s456 s789 s1024)
  graduated_a0.7          5/5  (s42 s123 s456 s789 s1024)
  graduated_a0.9          5/5  (s42 s123 s456 s789 s1024)
  surprisal               3/5  (s42 s123 s456 — s789 in progress)

REMAINING (7):
  surprisal_s789    ← eval ~98%, finishing soon
  surprisal_s1024
  dsir × 5 seeds    (s42 s123 s456 s789 s1024)

EST. TIME: ~25 min/run × 7 remaining ≈ 2.5-3 hours
```

---
