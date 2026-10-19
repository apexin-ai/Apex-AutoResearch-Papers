# ops collect and fill 34887 cuda0

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-and-fill-34887-cuda0_20260518T054951_result.json`
- **Structured JSON:** [`80be5e52cbf5b1fd6a77.json`](../../sessions/80/80be5e52cbf5b1fd6a77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已在运行。

**Part 1 — kl50_s123_eval 结果（DONE）：**

| 指标 | 值 |
|------|-----|
| wikitext2_ppl | 11.745 |
| arc_challenge | 0.3814 (acc_norm) |
| winogrande | 0.6125 |
| mmlu | 0.2752 |
| gsm8k | 0.0281 |

**Part 2 — kl50_s123_uniform_eval 已提交：**
- cuda:0 上运行中（PID 3143, 41.7GB VRAM）
- 正在跑 arc_challenge（~42% 进度）
- WikiText-2 PPL 已出：11.8917（略高于 global_topk 的 11.745，符合预期）
- Registry 已标记 RUNNING

---
