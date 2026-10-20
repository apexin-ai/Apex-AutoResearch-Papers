# eval exp 034 strategyqa200 s2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp-034-strategyqa200-s2_20260518T155648_result.json`
- **Structured JSON:** [`883b605453fc25b9f78b.json`](../../sessions/88/883b605453fc25b9f78b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment running successfully. First problem completed:
- **SICA**: No (correct) | **SC**: No (correct, 12/12 unanimous)
- Constraint extraction: 0 extracted (math prompt not yielding useful constraints for factual questions, as expected)
- ETA: ~45 min for 200 problems
- Problem 2/200 already processing

Summary:

| Item | Status |
|------|--------|
| **Server** | westd-16639, 4x RTX PRO 6000 Blackwell 98GB |
| **Environment** | vLLM 0.21.0, miniconda3, z3-solver 4.15.4 |
| **Model** | Qwen2.5-14B-Instruct (8 safetensors), cuda:2 |
| **vLLM** | Port 8002, started in 29s |
| **Data** | strategyqa_200.json (200 questions, 97 Yes / 103 No) |
| **Pipeline patches** | `--strategyqa-data` arg, Yes/No normalization in pipeline.py |
| **tmux session** | `exp034` on westd-16639 |
| **Registry** | exp-034 set to RUNNING |
| **Output** | `results/qwen25_14b_strategyqa200/exp034_results.json` |

Note: Constraint extraction yields 0 constraints for factual Yes/No questions (math extraction prompt expects equations/inequalities). SICA effectively falls back to frequency-based scoring, making it functionally equivalent to SC@K for this dataset type. This is a valid data point showing SICA behavior on out-of-domain (non-mathematical, non-logical) reasoning tasks.

---
