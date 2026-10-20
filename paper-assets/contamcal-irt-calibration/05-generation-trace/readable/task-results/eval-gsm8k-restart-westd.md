# eval gsm8k restart westd

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_gsm8k-restart-westd_20260521T071122_result.json`
- **Structured JSON:** [`55f3c611c6234c5cc121.json`](../../sessions/55/55f3c611c6234c5cc121.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 eval 全部正常推理中，C009/C006 检查通过（否则脚本会 exit 1）。

```
GPU 分配:
  cuda:0 → Gemma-2 d000 s0 GSM8K   PID 492703  (~1h30m ETA)
  cuda:1 → Qwen-14B d100 s0 GSM8K  PID 481803  (未动)
  cuda:2 → Qwen-14B d050 s0 GSM8K  PID 492186  (~1h43m ETA)
  cuda:3 → Phi-4 d000 s0 GSM8K     PID 493644  (~1h13m ETA)

日志:
  /tmp/eval_qwen14b_d050_gsm8k.log
  /tmp/eval_gemma2_d000_gsm8k.log
  /tmp/eval_phi4_d000_gsm8k.log
```

---
