# ssh phase1 check and phase2 3 launch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_phase1-check-and-phase2-3-launch_20260513T191733_result.json`
- **Structured JSON:** [`e31c8726b5155369d352.json`](../../sessions/e3/e31c8726b5155369d352.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态已清晰。

```
=== exp-001 Status Report ===

GPU Health:
  GPU 0: RTX 4090D, 100%, 22195/24564 MiB  [MMLU vLLM generation]
  GPU 1: RTX 4090D,  95%, 15049/24564 MiB  [GSM8K attempt 2 retry]
  GPU 2: RTX 4090D,  94%, 15119/24564 MiB  [ARC attempt 1 finishing]
  GPU 3: RTX 4090D,   0%,     0/24564 MiB  [idle]
  GPU 4: RTX 4090D,   0%,     0/24564 MiB  [idle]
  GPU 5: RTX 4090D,   0%,     0/24564 MiB  [idle]

Phase 1 Paraphrase:
  MMLU:          IN_PROGRESS — vLLM gen 31/878 batches (3.5%), ETA ~1h50m
  GSM8K:         IN_PROGRESS — attempt 1 done (42/42), QC retry attempt 2 starting (0/38 batches), ETA ~27min
  ARC-Challenge: IN_PROGRESS — attempt 1 at 34/37 batches (92%), ETA ~2.5min + QC/retry
  HumanEval:     DONE (164 items, 26/164 QC pass = 15.9%) — 降级为 appendix per D009

Phase 2 Data Prep:
  Status: BLOCKED — waiting for MMLU (critical bottleneck)

Phase 3 SFT Training:
  Status: BLOCKED — waiting for Phase 2

Bottleneck: MMLU vLLM generation at 3.5% (878 batches total, ~8s/batch).
预计最早可启动 Phase 2 时间: ~2 hours from now.
```

**注意事项：**
- GSM8K 和 ARC 的 vLLM 初始化均失败（Qwen2.5-7B-Instruct 的模板冲突），回退到 transformers，速度慢很多（~43-50s/batch vs vLLM 的 ~5-8s/batch）
- MMLU 使用 vLLM 成功，速度快但数据量大（14K items vs GSM8K 1.3K / ARC 1.2K）
- GSM8K 第一轮生成完成后大量 QC 失败，正在第二轮重试（38 batches ≈ 大部分items需要重新生成）
- GPU 3-5 空闲，如果 paraphrase_gen 支持多 GPU 分布式生成，可以加速 MMLU

---
