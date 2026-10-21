# ssh minihack day2 pilot

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_minihack-day2-pilot_20260519T113749_result.json`
- **Structured JSON:** [`42dbc713d2458229b6e2.json`](../../sessions/42/42dbc713d2458229b6e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Pilot Results

### Deterministic (10 eps, MiniHack-Room-5x5-v0)

| Ep | Seed | Steps | Score | Status |
|----|------|-------|-------|--------|
| 0-9 | 42-51 | 4 | +1.0 | GOAL |

- **Win rate: 100% (10/10)**
- **Death rate: 0%**
- **Avg steps: 4.0**

### Internal / LLM (10 eps, MiniHack-Room-5x5-v0, Qwen2.5-7B-Instruct)

| Ep | Seed | Steps | Score | Wall Time | Parse Failures |
|----|------|-------|-------|-----------|----------------|
| 0-9 | 42-51 | 4 | +1.0 | ~0.26s | 0/4 |

- **Win rate: 100% (10/10)**
- **Death rate: 0%**
- **Avg steps: 4.0**
- **Parse failure rate: 0%**

### Delta (Internal - Deterministic)
- **DR: 0% - 0% = 0%**
- **Win rate delta: 0%**
- **Avg steps delta: 0.0**

### Infrastructure Status
- **vLLM server**: stable, running in tmux `vllm-minihack`, model ID = `/root/autodl-tmp/models/Qwen2.5-7B-Instruct/`
- **LLM latency**: ~65ms per call (4 calls/ep, ~0.26s total)
- **Zero parse failures** across all 40 LLM calls

### Notes
- Room-5x5-v0 is a trivial navigation task: both agents solve it perfectly in 4 steps. The staircase is always reachable via a direct diagonal path from spawn.
- Initial prompt had a bug where the LLM confused "stairs up" and "stairs down", causing oscillation. Fixed by adding explicit distance cues and "IGNORE stairs up" instruction.
- NLELanguageWrapper requires string actions (not int indices) and needs extra obs keys (`tty_chars`, `tty_cursor`, `inv_letters`, `inv_strs`).
- Files deployed: `minihack_det_agent.py` (476 lines), `minihack_episode_runner.py` (264 lines) at `/root/autodl-tmp/simgate-modular-routing/scripts/minihack/`.
- Results saved to `results/pilot_det.jsonl` and `results/pilot_internal.jsonl`.

---
