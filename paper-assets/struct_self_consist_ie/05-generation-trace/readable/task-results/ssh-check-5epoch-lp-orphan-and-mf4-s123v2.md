# ssh check 5epoch lp orphan and mf4 s123v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_5epoch_lp_orphan_and_mf4_s123v2_20260522T131708_result.json`
- **Structured JSON:** [`c59871b4c3e0da3778fa.json`](../../sessions/c5/c59871b4c3e0da3778fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full status:

---

### Task 1: 5-epoch LP (cuda:3)
- PID 137895 is dead (killed). But **PID 137900 + child 138176 are alive** on cuda:3 (30224 MiB).
- Progress: **96% (288,096 / 301,184 prompts)**, elapsed 1h44m, ETA ~5 min.
- Log: `/tmp/exp_fewnerd_5epoch_lp_s42.log` (no log in `~/runs/`).
- Let it finish.

### Task 2: MF4 s123v2 (cuda:2)
- PID 136358 alive, running 1h50m. VLLM engine PID 136811 on cuda:2 (30914 MiB).
- **VLLM inference: 100% complete** (301,184/301,184 prompts, took 1h47m).
- Now in **"Rendering prompts" post-processing: ~24% (9,172/37,648)**. Output dir still empty — results not written yet.
- Estimate: rendering at ~500 it/s → ~58s remaining for rendering, then save to disk.

### Task 3: Freeform experiments
- **FewNERD freeform (cuda:0)**: PID 144468 (`--use_grammar false --seed 42`), started ~15 min ago, VLLM engine PID 145028 (30268 MiB). Just finished CUDA graph capture, entering inference. No log in `~/runs/` — appears to have been started outside the job runner.
- **CoNLL freeform (cuda:1): CRASHED** — `RuntimeError: Engine core initialization failed` in VLLM. cuda:1 is now free.

### GPU Summary
| GPU | Process | Status |
|-----|---------|--------|
| cuda:0 | FewNERD freeform s42 | Just started (~15min) |
| cuda:1 | — | **Free** (CoNLL freeform crashed) |
| cuda:2 | MF4 s123v2 | Rendering 24%, almost done |
| cuda:3 | 5epoch LP s42 | Inference 96%, ~5min left |

---
