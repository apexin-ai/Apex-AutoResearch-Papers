# code dense l1 l8 extraction script

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dense_l1_l8_extraction_script_20260517T000052_result.json`
- **Structured JSON:** [`14b71b53c83f195836f3.json`](../../sessions/14/14b71b53c83f195836f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All validated. Here's the summary:

**Script:** `/root/vla-ssd/scripts/cross_instruction_extract_dense.py`

**Dry-run result:** Passed. 1 task × 1 frame × 2 instructions = 2 forward passes completed in <1s. Output shape confirmed `(9, 4096)` for both `image_mean` and `last_preaction`. `f.attrs['layers'] = [0,1,2,3,4,5,6,7,8]` correctly stored.

**Run commands (when ready):**
```bash
# trained (~4-5 min)
/root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/cross_instruction_extract_dense.py --condition trained --gpu 0

# untrained (~4-5 min)
/root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/cross_instruction_extract_dense.py --condition untrained --gpu 0
```

**Estimated runtime:** ~4-5 min per condition. The forward pass computes all 32 layers regardless; hooking 9 vs 5 adds negligible overhead. Total ~8-10 min for both conditions.

**Key differences from original:**
- `LAYER_INDICES = [0,1,2,3,4,5,6,7,8]` (9 layers) vs `[0,8,16,24,31]` (5 layers)
- Output shape `(9, 4096)` vs `(5, 4096)`
- Output dir: `/root/autodl-tmp/vla-ssd/results/cross_instruction_dense/`
- Filenames: `{trained,untrained}_cross_inst_dense.h5`
- Default model path corrected to `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b`

---
