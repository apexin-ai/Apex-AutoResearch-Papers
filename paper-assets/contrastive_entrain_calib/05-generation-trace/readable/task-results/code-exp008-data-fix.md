# code exp008 data fix

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp008-data-fix_20260518T174020_result.json`
- **Structured JSON:** [`d34f31b41e2ab52f4ac0.json`](../../sessions/d3/d34f31b41e2ab52f4ac0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All four changes applied, syntax verified:

1. **`CalibrationSFTDataset.__init__`** — Now loads 3-turn data, encodes full sequence via `apply_chat_template`, locates Turn 1 (assistant) boundaries using `msgs[:1]` prefix + `<|im_end|>` scan, masks labels to only Turn 1 tokens, stores `resp_pos = len(full_ids) - 1` and `response_text = turns[1]["content"]`.

2. **`sft_collate`** — Returns `resp_positions` instead of `prompt_lens`; labels come pre-built from the dataset (no longer constructed in collate).

3. **Training loop probe extraction** — Uses `resp_positions[b]` (sequence end) instead of `plens[b] - 1`.

4. **R3 precompute** — `response_text` correctly points to Turn 1 assistant content (`turns[1]["content"]`), no change needed in `precompute_r3` itself.

---
