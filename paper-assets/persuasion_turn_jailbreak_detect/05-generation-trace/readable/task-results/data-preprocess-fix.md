# data preprocess fix

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_preprocess-fix_20260517T060832_result.json`
- **Structured JSON:** [`d6c9a604f72d4ac0c20c.json`](../../sessions/d6/d6c9a604f72d4ac0c20c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 preprocessing tasks completed successfully:

1. **SafeMTData placeholder removal**: Assistant `[Model response]` turns removed (avg turns: 10 → 5)
2. **attack_type field added**: cipher-based (115), persuasion-based (135), benign (250)
3. **Stratified split**: Train 350 / Val 75 / Test 75, max stratification deviation 1.0%

Output files:
- `artifacts/data/processed/conversations.jsonl` (updated with attack_type, placeholders removed)
- `artifacts/data/processed/train.jsonl`
- `artifacts/data/processed/val.jsonl`
- `artifacts/data/processed/test.jsonl`

---
