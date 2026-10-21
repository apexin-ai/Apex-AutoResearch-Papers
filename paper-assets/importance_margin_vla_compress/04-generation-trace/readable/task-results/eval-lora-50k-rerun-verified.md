# eval lora 50k rerun verified

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_lora_50k_rerun_verified_20260516T195446_result.json`
- **Structured JSON:** [`dae8c3968bb7a84beb45.json`](../../sessions/da/dae8c3968bb7a84beb45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

```
=== LORA 50K EVAL RE-RUN (VERIFIED) ===

[KEY LOADING]
- State dict total keys: 574
- State dict LoRA keys: 74
- Model LoRA keys: 74
- Successfully loaded LoRA keys: 74 (all matched)
- Missing keys: 0 (LoRA: 0)
- Unexpected keys: 0 (LoRA: 0)
- VERDICT: CORRECT_LOAD ✓

[EVAL RESULTS]
- Suite: libero_object
- Episodes per task: 5
- Overall SR: 0/50 (0.0%)
- Per-task: [0%, 0%, 0%, 0%, 0%, 0%, 0%, 0%, 0%, 0%]
- All 50 episodes hit max 280 steps (timeout)

=== CONCLUSION ===
■ LORA GENUINELY 0% SR — keys correctly loaded, model doesn't work at 50K steps

排除了 eval bug 可能性。LoRA 74 个权重全部正确加载（0 missing, 0 unexpected），
模型就是在 50K steps 时完全不工作。这是训练本身的问题，不是 eval 流程的问题。

→ Plan B
```

---
