# code multi seed prep debate logiqa

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_multi-seed-prep-debate-logiqa_20260519T181220_result.json`
- **Structured JSON:** [`ffd82a2c68a5dcf62e25.json`](../../sessions/ff/ffd82a2c68a5dcf62e25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Summary:

**Part A** — 3 seed=123 replication scripts on westd-25068:
- `scripts/run_icg_seed123.sh` (exp-074c)
- `scripts/run_contrastive_seed123.sh` (exp-075c)
- `scripts/run_debate_seed123.sh` (exp-076c)

**Part B** — exp-078-debate-mistral-logiqa200 deployed on westd-16639:
- Patched `run_debate.py` with 10 changes for LogiQA multichoice (A/B/C/D) support
- Synced code via base64 chunked transfer (25068→16639)
- vLLM Mistral-7B running on cuda:3 port 8013 (tmux: `vllm_logiqa`), FlashInfer sampler disabled for Blackwell compat
- C001 dry-run passed: `--limit 1` on logiqa_000 completed end-to-end (75s, answer extraction functional)
- Full 200-problem run active as PID 194538, processing problem 2/200 at ~75s/problem (ETA ~4.2 hours)
- Registered in registry as RUNNING with hypothesis, parent=exp-076, artifact logged

Monitor with: `tail -f /tmp/exp078_debate_logiqa.log` or `grep -c "Processing" /tmp/exp078_debate_logiqa.log` on westd-16639.

---
