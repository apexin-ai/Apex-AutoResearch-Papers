# diagnose dcol deberta 002 oom

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_dcol_deberta_002_oom_20260514T224140_result.json`
- **Structured JSON:** [`043cab10443f8406aab5.json`](../../sessions/04/043cab10443f8406aab5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。总结：

- **OOM 根因**: dcol_deberta_002 (57GB) 与 gpt2xl_temp09 extract_features (9GB) 同时占用 GPU 0，显存竞争导致 OOM。**不是代码 bug，不是残留进程**——PID 193689 就是 dcol_deberta_002 本身。
- **GPU 0 已清空**: 所有进程已自行退出，当前 0MiB / 97887MiB，完全空闲。GPU 1 上 olmo_temp09_001 未受影响。
- **代码和数据完好**: `dcol_trainer.py` 和 `features_all.jsonl` 均正常。
- **可以安全重试 dcol_deberta_002**，建议确保 GPU 0 独占或适当降低 batch_size。

---
