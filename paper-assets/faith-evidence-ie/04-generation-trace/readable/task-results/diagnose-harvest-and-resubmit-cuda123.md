# diagnose harvest and resubmit cuda123

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_harvest-and-resubmit-cuda123_20260520T153701_result.json`
- **Structured JSON:** [`4f44f3cbf6c617678636.json`](../../sessions/4f/4f44f3cbf6c617678636.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报：3 个实验全部仍在运行

| 实验 | GPU | PID | 运行时间 | 进度 | 预估剩余 |
|------|-----|-----|---------|------|---------|
| eval_llama_sft_s43_no_evidence | cuda:1 | 27322 | 1h29m | **183/247** (74%) | ~30min |
| eval_llama_sft_s44_no_evidence | cuda:2 | 29983 | 46min | **92/247** (37%) | ~70min |
| eval_llama_rsft_s44_no_evidence | cuda:3 | 30188 | 46min | **105/247** (43%) | ~55min |

GPU 利用率 85-91%，每张卡占用 ~18.9GB，推理正常无报错。

- **s43** 最先完成，约 30 分钟后
- **rsft_s44** 其次，约 55 分钟
- **s44** 最后，约 70 分钟

无需干预，等完成后 harvest 结果即可。

---
