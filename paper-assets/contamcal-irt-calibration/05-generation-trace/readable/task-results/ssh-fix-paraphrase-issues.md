# ssh fix paraphrase issues

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-paraphrase-issues_20260513T190626_result.json`
- **Structured JSON:** [`4f0fcb637a7f1153cf1c.json`](../../sessions/4f/4f0fcb637a7f1153cf1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务运行正常。HumanEval 正在进行第二轮 vLLM 生成（可能是 rejection resampling）。

```
=== Phase 1 Fix Summary ===
GPU 0: MMLU - PID 196968 - vLLM - 16/220 batches (~8s/batch)
GPU 1: GSM8K - PID 189375 - transformers - 27/42 batches (64%)
GPU 2: ARC - PID 190717 - transformers - 22/37 batches (59%)
GPU 3: (freed) — killed old HumanEval PIDs 191459, 196320
GPU 4: HumanEval - PID 201102 - vLLM - 2nd round starting (EngineCore 203311)
GPU 5: idle

Estimated completion:
  GSM8K   ~10 min (15 batches × 43s)
  ARC     ~12 min (15 batches × 49s)
  MMLU    ~27 min (204 batches × 8s)
  HumanEval ~5 min (new round 0/5, plus similarity)
```

与预期不同的关键发现：
- MMLU 实际上在用 **vLLM 正常跑**（PID 196968，GPU 0），不需要 kill 重启
- HumanEval 已有人在 GPU 4 上用 vLLM 重启（PID 201102），正在多轮生成中
- 只需清理 GPU 3 上的两个旧 HumanEval 进程，已完成

---
