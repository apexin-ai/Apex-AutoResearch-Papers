# code l1 head ablation v3

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_l1_head_ablation_v3_20260517T124429_result.json`
- **Structured JSON:** [`5f6696f3b2aac961b8e9.json`](../../sessions/5f/5f6696f3b2aac961b8e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job submitted successfully.

- **Script**: `/root/vla-ssd/scripts/l1_head_ablation.py`
- **Job**: `l1_head_ablation` (tmux session, log at `~/runs/vla-ssd/l1_head_ablation.log`)
- **Output**: `/root/autodl-tmp/vla-ssd/results/l1_head_ablation/results.json`

实验设计：
- 3 conditions: `baseline` (no ablation), `ablate_all24` (24 instruction-attending heads zeroed), `ablate_control8` (8 non-instruction heads zeroed)
- 50 images (10 tasks × 5 demos × frame 0) × 10 instructions = 500 forward passes/condition
- Features extracted at layers [1, 8, 16, 31], 10-way task classification (train on demos 0-2, test on demos 3-4)
- 预计运行 25-30 分钟

---
