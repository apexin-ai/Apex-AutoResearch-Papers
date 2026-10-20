# code fix instruct eval chat template

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_instruct_eval_chat_template_20260516T103220_result.json`
- **Structured JSON:** [`ab65f451329a4429312c.json`](../../sessions/ab/ab65f451329a4429312c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval is running well — processing ~25 items/sec on MMLU (14042 items). At this speed, MMLU alone will take ~9 minutes. The full run (mmlu + gsm8k + arc_challenge + humaneval x2 modes) should take roughly 30-40 minutes.

Here's a summary of everything completed:

## Part 1: Diagnosis

**Root cause** (two distinct issues):
1. **MCQ (MMLU/ARC)**: Logprob-based eval assigns highest probability to verbose tokens ("The", "Let") for RLHF'd Instruct models, not answer letters. Additionally, chat template was applied but with no system message, causing the model to generate verbose explanations instead of answer letters.
2. **HumanEval**: Instruct model wraps code in markdown blocks (` ```python...``` `) with explanations, but the code extraction only truncated at `def`/`class` boundaries without stripping markdown.

## Part 2: Fix Applied to `evaluate.py`

All changes are backward-compatible (base/SFT models unaffected):

1. **`--instruct` CLI flag** + auto-detection from model name
2. **`format_as_chat()`** — added optional `system_prompt` parameter
3. **`extract_mcq_answer()`** — new function for generation-based answer extraction
4. **`extract_code_from_markdown()`** — new function for markdown code block extraction
5. **MCQ generation mode** (instruct only): system prompt constraining output to answer letter only, `max_new_tokens=5`
6. **HumanEval instruct mode**: markdown code extraction + skip re-stated function signature
7. **Regex fix**: corrected double-escaped backslashes in all 3 regex patterns
8. Applied to both `evaluate_mcq` and `evaluate_paraphrased` blocks

## Part 3: Re-run Launched

- **tmux session**: `instruct_eval_v2`
- **PID**: 764449 / 764451
- **Script**: `/root/contamcal-irt-calibration/scripts/run_instruct_3b_eval_v2.sh`
- **GPU**: cuda:3
- **Output dirs**: `Qwen2.5-3B-Instruct_v2_aligned`, `Qwen2.5-3B-Instruct_v2_para_aligned`
- **Log**: `/root/autodl-tmp/exp001/instruct_eval_v2.log`
- **Registry**: `exp_001_eval_3B_instruct_v2` (RUNNING), old `exp_001_eval_3B_instruct_aligned_para` already marked failed

---
