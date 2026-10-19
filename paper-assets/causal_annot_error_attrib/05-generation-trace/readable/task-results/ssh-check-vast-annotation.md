# ssh check vast annotation

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_vast_annotation_20260521T175849_result.json`
- **Structured JSON:** [`799ccb571418a3f25b99.json`](../../sessions/79/799ccb571418a3f25b99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Results

**1. Process PID 712156:** Still running. Elapsed **6h 04min**, started May 21 ~04:55. Command:
```
python3 annotate.py --dataset civil_comments --model all --prompt all --delay 0.3
```
**Important correction:** This process is annotating `civil_comments`, **not VAST**. The VAST annotations are already complete from yesterday.

**2. plan011_frontier_annotations directory: does NOT exist** on the remote server. Annotation outputs actually go to `/home/sonny/causal_annot_error_attrib/results/&lt;dataset>/`.

VAST (`results/vast/`) — **15 jsonl files, all complete** (5 models × 3 prompts, finished May 20):
- deepseek / llama4 / qwen2.5-7b / qwen3 / + deepseek prior set — all of zero-shot, few-shot-3, few-shot-5

Civil_comments (`results/civil_comments/`) — current target, **11 complete + 1 in progress**:
| Model | zero-shot | few-shot-3 | few-shot-5 |
|---|---|---|---|
| deepseek | ✓ 822KB | ✓ 822KB | **MISSING** |
| llama4 | ✓ 830KB | ✓ 831KB | ✓ 831KB |
| qwen2.5-7b | ✓ 723KB | ✓ 723KB | ✓ 724KB |
| qwen3 | ✓ 754KB | ✓ 731KB | **⏳ 17KB (in progress, mtime 10:59)** |

12 expected (4 models × 3 prompts); 11 done, 1 actively being written, 1 (`deepseek_few-shot-5`) not yet started.

**3. Log file:** `/tmp/annotate_civil_comments.log` (process fd 1+2 both point here). Size = **0 bytes**, empty — stdout is unflushed (Python default block-buffering with no `-u` flag). **No errors visible** because nothing has been written. Progress can only be tracked via jsonl file growth in `results/civil_comments/`.

---
