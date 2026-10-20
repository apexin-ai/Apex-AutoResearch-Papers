# ops gsm8k results collect olmo phi

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gsm8k-results-collect-olmo-phi_20260521T101303_result.json`
- **Structured JSON:** [`2ca11c0be8893261c413.json`](../../sessions/2c/2ca11c0be8893261c413.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 11 个 GSM8K eval 结果已收集完毕。GPU 2 空闲，OLMo-2 d005_s0 已完成。

## GSM8K 结果汇总（westd, seed=0, N=1319）

| Model | Dosage | Correct | Accuracy |
|-------|--------|---------|----------|
| **Qwen2.5-14B** | d000 | 989 | 74.98% |
| | d005 | 939 | 71.19% |
| | d025 | 1046 | 79.30% |
| | d050 | 1069 | 81.05% |
| | d100 | 1087 | 82.41% |
| **Gemma-2** | d000 | 235 | 17.82% |
| **Phi-4** | d000 | 1114 | 84.46% |
| | d100 | 1129 | 85.60% |
| **OLMo-2** | d000 | 799 | 60.58% |
| | d005 | 873 | 66.19% |
| | d100 | 920 | 69.75% |

**GPU 状态**: GPU 0/1/3 跑 LLaMA-3 SFT（82-98% util），GPU 2 空闲。

**注意**: Qwen14b d005 (71.19%) 低于 d000 (74.98%)，出现性能下降；Gemma-2 d000 只有 17.82%，大量 pred=null，可能有 eval 格式问题需排查。

---
