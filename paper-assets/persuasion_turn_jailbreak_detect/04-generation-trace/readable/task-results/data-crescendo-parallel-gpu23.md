# data crescendo parallel gpu23

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_crescendo-parallel-gpu23_20260517T100414_result.json`
- **Structured JSON:** [`c79e01461049e6869ddf.json`](../../sessions/c7/c79e01461049e6869ddf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both processes running and utilizing all 4 GPUs. Summary:

**Status: Both processes running**

| Process | Screen | GPUs | Playbooks | Conversations | First conv time |
|---------|--------|------|-----------|---------------|-----------------|
| Part 1 | `crescendo1` | cuda:0+1 | A,B,C,D | 128 total | 88.9s (10 turns) |
| Part 2 | `crescendo2` | cuda:2+3 | E,F,G,H | 122 total | 51.9s (6 turns) |

**GPU Memory**: ~19GB (attacker/Qwen3-8B) + ~17.6GB (target/Qwen2.5-7B-Instruct) per pair

**Conv ID scheme**: Part 1 = `crescendo_0000`-`crescendo_0127`, Part 2 = `crescendo_0128`-`crescendo_0249`

**Output files**: `data/generated/crescendo_part1.jsonl`, `data/generated/crescendo_part2.jsonl`

**ETA**: Initial estimates are ~105-190min but these are based on only 1 sample each. Average should improve as shorter conversations (5-7 turns) dominate. Realistic estimate: ~2-2.5 hours for all 250 conversations across both processes.

**Auto-restart**: Both wrapped with retry logic (up to 10 retries with 10s delay).

---
