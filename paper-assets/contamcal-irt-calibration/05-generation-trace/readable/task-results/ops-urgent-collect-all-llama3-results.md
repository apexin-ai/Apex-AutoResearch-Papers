# ops urgent collect all llama3 results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-collect-all-llama3-results_20260521T131152_result.json`
- **Structured JSON:** [`a3f73e5fd83c33017595.json`](../../sessions/a3/a3f73e5fd83c33017595.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
d000: MMLU=53.50%, ARC=72.61%
d025: MMLU=52.75%, ARC=72.01%
d100: MMLU=pending, ARC=pending
d100 SFT: 进行中 3924/4159 steps (94%), epoch 0.92, ETA ~11min
GPU: [0] idle | [1] idle | [2] idle | [3] 77% 37.9/97.9GB (d100 SFT)
活跃进程:
  - PID 510203: train_sft.py Meta-Llama-3.1-8B d100_s0 (CUDA:3)
  - PID 521160: monitor_llama3_eval.sh d100 (等训练完自动启 eval)
```

d100 SFT 还有约 235 步（~11分钟）就完成。d025 monitor 已不在运行（只剩 d100 monitor）。

---
