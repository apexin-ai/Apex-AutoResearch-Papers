# diagnose gpu and process check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_and_process_check_20260521T205401_result.json`
- **Structured JSON:** [`10c41d1fc6be8cd04fd1.json`](../../sessions/10/10c41d1fc6be8cd04fd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/gpu_diagnosis_loop18.md`。

**结果汇总:**

- **存活 3/6**，全在 autodl-5090-c（5epoch_s456, mf4v2_s123_v3, mf4v2_s456_v3），GPU 利用率 80-92%
- **死亡 3/6**，全在 autodl-5090（mf4v2_s42_v3, 5epoch_s42, 5epoch_s123），PID 不存在，4 张 GPU 全空闲
- autodl-5090-c cuda:3 额外跑着 e2_pretrained_fewnerd_s42
- 磁盘：5090 **88% (31GB剩余，需关注)**，5090-c 72% (101GB剩余)

---
