# verify gpu allocation fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_gpu-allocation-fix_20260520T043241_result.json`
- **Structured JSON:** [`3ebebbdfa98be2262c67.json`](../../sessions/3e/3ebebbdfa98be2262c67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切正常，两个训练任务都已成功启动并在正确 GPU 上运行。

**GPU 分布：**

| GPU | PID | 进程 | 显存占用 | GPU 利用率 |
|-----|-----|------|---------|-----------|
| 0 | 712690 | plan017_14b_rsft_generate | 17,350 MiB / 32,607 MiB | 32% |
| 1 | 754427 | llama_sft_s43_train_eval_r2 | 29,212 MiB / 32,607 MiB | 78% |
| 2 | 712690 | plan017_14b_rsft_generate | 19,548 MiB / 32,607 MiB | 39% |
| 3 | 754511 | llama_sft_s44_train_eval_r2 | 24,226 MiB / 32,607 MiB | 94% |

**训练状态：**
- **s43** (GPU 1): 已完成 9/570 steps，~5.5s/it，tokenization 完毕，训练正常推进
- **s44** (GPU 3): 已完成 9/570 steps，~5.6s/it，tokenization 完毕，训练正常推进

注意 PID 与预期略有偏差（s43 实际 PID 754427 vs 预期 754413，s44 实际 PID 754511 vs 预期 754497），这是 tmux 内 python 子进程的正常 PID 差异，不影响运行。GPU 0 和 GPU 2 仍由 plan017_14b_rsft_generate (PID 712690) 占用，符合预期。

---
