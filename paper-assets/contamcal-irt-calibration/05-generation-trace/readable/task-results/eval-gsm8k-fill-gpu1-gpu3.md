# eval gsm8k fill gpu1 gpu3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_gsm8k-fill-gpu1-gpu3_20260521T085524_result.json`
- **Structured JSON:** [`99738c19a368977bb493.json`](../../sessions/99/99738c19a368977bb493.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 正常推进，无报错：

- **GPU 1** OLMo-2 d000_s0: 12/660 batches, ~5.5s/it → 预计 ~60 min 完成
- **GPU 3** Phi-4 d100_s0: 4/660 batches, ~6.5s/it → 预计 ~72 min 完成

**GPU 0 和 GPU 2 空闲**。如果要最大化利用率，可以立即在这两个 GPU 上启动：
- GPU 0: OLMo-2-7B d100_s0 GSM8K（优先级 #4）
- GPU 2: Gemma-2 d100_s0 GSM8K（优先级 #5）

需要我填满 GPU 0 和 2 吗？

---
