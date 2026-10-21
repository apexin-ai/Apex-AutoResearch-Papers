# ops westd gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-gpu-status-check_20260520T001123_result.json`
- **Structured JSON:** [`7a6d7b3623c8f71a9f33.json`](../../sessions/7a/7a6d7b3623c8f71a9f33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
westd GPU 状态:
cuda:0 — Phi-4 s123 training     2576/4159 (62%)  剩余 ~1h
cuda:1 — Qwen-14B s123 training  2433/3642 (67%)  剩余 ~1h04m
cuda:2 — OLMo-2 GSM8K s123 eval  d000_s123 43/165 (26%)  剩余 ~39min (含 d100)
cuda:3 — Gemma-2 s123 training   3128/3642 (86%)  剩余 ~26min

GSM8K eval 状态:
  s42:  ✅ 全部完成 (d000~d100, 07:51:42 结束)
  s123: 🔄 d000_s123 进行中 (43/165), 之后还有 d100_s123
        脚本只跑 d000 和 d100 两个 dosage，每个 ~22min

s123 训练预计完成时间:
  Gemma-2:  ~08:37 (最先完成)
  Phi-4:    ~09:12
  Qwen-14B: ~09:15
```

---
