# verify lora 50k checkpoint integrity

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_lora_50k_checkpoint_integrity_20260516T192803_result.json`
- **Structured JSON:** [`82e6079fa5f37caec6bd.json`](../../sessions/82/82e6079fa5f37caec6bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report saved to `artifacts/checkpoint_integrity_report.md`. Here's the summary:

---

**=== VERDICT: No loading/transfer bug. Checkpoint is intact. ===**

**Step 1 — Weight Check: PASS**
- 74 LoRA params, all non-zero, reasonable mean/std
- Key alignment **perfect**: 0 missing, 0 unexpected keys when loaded with `libero_baseline.yaml`

**Step 2 — MD5: PASS (MATCH)**
- westd = cqa1 = `445418230f9642acc1932d7a3098cab3`

**Step 3 — Inference: PASS (REASONABLE)**
- Actions in [-1.03, 1.00], non-zero, non-NaN, vary across inputs
- Model is actively producing different policies for different observations

---

**⚠️ Critical side-finding**: Full FT and LoRA checkpoints have **ZERO overlapping keys** (different key namespaces due to PEFT wrapping). The eval uses `strict=False` which silently drops all keys on mismatch. The only saved eval result file (`libero_libero_object.json`) shows Full FT checkpoint was evaluated with LoRA config — a guaranteed 0% SR bug.

**Cannot confirm** how the LoRA 50K eval was actually run (no bash_history or eval log found). If it was run with the correct config, the 0% SR is genuine. If there was a config mismatch, it's a bug. **Recommend re-running the eval with explicit missing/unexpected key logging.**

---
