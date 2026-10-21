# research check cross inst trained

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check_cross_inst_trained_20260516T234759_result.json`
- **Structured JSON:** [`377a3e283bbf26522966.json`](../../sessions/37/377a3e283bbf26522966.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Results

**Trained extraction (PID 751661): COMPLETED SUCCESSFULLY**
- File: `trained_cross_inst.h5` (399 MB)
- Log confirms: "Done. 5000 forward passes in 4.2 min"
- Process no longer running (finished)
- Structure: `task_{0-9}/frame_{0-49}/instruction_{0-9}/{image_mean, last_preaction}` each with shape `(5, 4096)` float16
- 10 tasks x 50 frames x 10 instructions = 5000 forwards, as expected

**Untrained extraction (PID 751972): STILL RUNNING**
- Currently on task_7 (~72% of task_7, which means ~7.4/10 tasks done, roughly 74% overall)
- File already 294 MB and growing
- GPU 1 at 72% utilization, 15.4 GB memory used
- Rate: ~2.09 it/s per frame, ~20 fwd/s overall
- ETA: ~2 more tasks remaining, ~50s each = ~100s to finish

Both extractions have matching structure. Untrained should complete within ~2 minutes.

---
