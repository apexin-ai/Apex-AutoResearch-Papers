# check math500 eval progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_math500_eval_progress_20260518T021852_result.json`
- **Structured JSON:** [`0197c552b86f9d5596e7.json`](../../sessions/01/0197c552b86f9d5596e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Key finding: **grpo_unpruned** (pid 64467's child) is NOT on GPU despite being assigned cuda:2, while **sft_cka_only_20** (pid 65395) occupies cuda:2 with 30GB. They're competing for the same GPU.

| exp_id | pid alive | progress | avg rate | est_completion (UTC) |
|--------|-----------|----------|----------|---------------------|
| eval_math500_grpo_standard_20 | yes (14556, GPU 34.5GB) | **383/500** | ~20/hr | ~16:00 May 18 |
| eval_math500_grpo_rasp_20_v3 | yes (31706, GPU 32.5GB) | **340/500** | ~21/hr | ~18:00 May 18 |
| eval_math500_grpo_unpruned | yes (64467→child, **no GPU**) | **166/500** | ~52/hr | ~16:45 May 18 |
| eval_math500_sft_cka_only_20 | yes (65395, GPU 30GB) | **43/500** | ~15/hr | ~May 19 17:00 |

**Issues:**
- `grpo_unpruned` 和 `sft_cka_only_20` 都被分配到 cuda:2，但 nvidia-smi 只显示 sft_cka_only_20 占用 GPU。grpo_unpruned 可能在 CPU 上跑（速度看起来还行 52/hr，但不确定是否有隐患）。
- `sft_cka_only_20` 极慢（单题平均 ~4min），按当前速度还需 ~30 小时才能完成。

---
