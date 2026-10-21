# code 8b cell c episode v5

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8b_cell_c_episode_v5_20260519T131227_result.json`
- **Structured JSON:** [`fe7f60d64c3ff12a22e7.json`](../../sessions/fe/fe7f60d64c3ff12a22e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Experiment crashed again (EXIT_CODE=1)**, this time with a different error:

```
VLLMValidationError: This model's maximum context length is 8192 tokens. 
However, your prompt contains 8450 input tokens (exceeds max_model_len: 8192).
```

A validation prompt accumulated 8450 tokens during multi-turn ALFWorld, exceeding the `max_model_len: 8192` limit.

---

## Summary

### 1. GPU 清空状态
All 4× RTX PRO 6000 96GB were at 0 MiB before launch.

### 2. ScienceWorld PID 状态
- **PID 51279**: RUNNING — `python3 /root/autodl-tmp/extract_scienceworld_sft_optimized.py`, elapsed ~43 min
- **PID 755742**: NOT RUNNING (not found)
- Additional related processes: PID 19201 (`extract_scienceworld_sft_partial.py`) and two Java gateway servers

### 3. Config 修改 diff
| Field | Before | After |
|-------|--------|-------|
| `use_ref` | `True` | `False` |
| `use_kl_loss` | `True` | `False` |
| `gpu_memory_utilization` | `0.15` | `0.20` |
| `max_model_len` | `8192` | `8192` (unchanged) |
| `ppo_mini_batch_size` | `4` | `4` (unchanged) |
| `ppo_max_token_len_per_gpu` | `16384` | `16384` (unchanged) |

### 4. 实验提交状态
Submitted twice:
- **1st attempt**: Crashed immediately — `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` incompatible with vLLM CuMemAllocator (`AssertionError`)
- **2nd attempt** (without expandable_segments): Crashed during val_before_train — prompt exceeded `max_model_len: 8192` (a validation prompt had 8450 tokens)

### 5. Step 1 backward pass
**Not reached.** Crashed during val_before_train. Two issues discovered:
1. `expandable_segments:True` is incompatible with this vLLM version (fixed by removing it from the command)
2. `max_model_len: 8192` is too small for some multi-turn ALFWorld prompts — need to increase it (e.g. to 16384 or 32768) or reduce `max_prompt_length` below 8192

---
