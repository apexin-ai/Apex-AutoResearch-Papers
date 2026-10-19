# ops westd 34887 fix hf cache resubmit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-34887-fix-hf-cache-resubmit_20260518T090523_result.json`
- **Structured JSON:** [`df268076a45e91f70a8e.json`](../../sessions/df/df268076a45e91f70a8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部正常：

- **cuda:0** (PID 15057): kl_comp_30pct_s42_eval — 49GB 显存，98% GPU 利用率，正在跑 arc_challenge
- **cuda:1** (PID 15367): kl50_s42_uniform_eval — 42GB 显存，正在跑 arc_challenge
- 两个日志都显示 "Using the latest cached version"，HF 离线缓存命中，无 ConnectionError
- Registry 两个实验均已更新为 RUNNING

---
