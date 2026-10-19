# analysis v4 status and results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4_status_and_results_20260524T004406_result.json`
- **Structured JSON:** [`5b6c0c098f918f550c7a.json`](../../sessions/5b/5b6c0c098f918f550c7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验状态：running**

- **tmux session**: `qwen14b_kl30_s123_gsm8k_v4` 活跃
- **进程**: PID 169182，CPU 101%，启动于 08:42 UTC
- **GPU 0**: 72% 利用率，63263 MiB 显存
- **当前阶段**: GSM8K generate_until，进度 25/1319 (~2%)，速度 ~1.79s/it，预计还需 **~38 分钟**完成
- **已完成**: 层级稀疏率分析（Model-level: 0.296），loglikelihood 阶段（1319/1319）

层级稀疏率范围 0.285–0.301，model-level 0.296，与 0.3 target 一致。

---
