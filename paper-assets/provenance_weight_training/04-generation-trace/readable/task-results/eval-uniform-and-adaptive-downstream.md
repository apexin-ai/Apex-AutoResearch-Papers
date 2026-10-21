# eval uniform and adaptive downstream

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_uniform_and_adaptive_downstream_20260517T171858_result.json`
- **Structured JSON:** [`9c4855c7aa07cf76f976.json`](../../sessions/9c/9c4855c7aa07cf76f976.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Status update:

**uniform_seed42 training is NOT near completion.** It's at step ~623/6103 (10%), with ~23 hours remaining. The 8477/8477 bar was one epoch's forward passes, not total training. `final` checkpoint does not exist yet.

**adaptive_fix_seed42 already has complete fewshot results** from a previous run with the exact settings requested:

```
adaptive_fix_seed42:
  HellaSwag (10-shot)  acc_norm = 0.4863
  ARC-Easy (25-shot)   acc/acc_norm = 0.7100/0.7121
  PIQA (5-shot)        acc/acc_norm = 0.6866/0.6839
  WinoGrande (5-shot)  acc = 0.5635
```

I also ran a new 0-shot eval for adaptive_fix (saved to `qwen_adaptive_fix_downstream/`):
```
adaptive_fix_seed42 (0-shot):
  HellaSwag  acc_norm = 0.4785
  ARC-Easy   acc/acc_norm = 0.6503/0.6157
  PIQA       acc/acc_norm = 0.6872/0.6866
  WinoGrande acc = 0.5777
```

**Options for uniform:**
1. Wait for training to finish (~23 hours), then eval the final checkpoint
2. Eval the latest available checkpoint (checkpoint-600 at step 600/6103) now for a preliminary comparison
3. Something else

What would you like to do?

---
