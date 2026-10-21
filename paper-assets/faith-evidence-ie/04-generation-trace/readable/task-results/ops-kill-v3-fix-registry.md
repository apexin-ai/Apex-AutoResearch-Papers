# ops kill v3 fix registry

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-v3-fix-registry_20260522T013227_result.json`
- **Structured JSON:** [`51f31e220a356a816c6c.json`](../../sessions/51/51f31e220a356a816c6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
v3 kill: ✅ (PID 151217, kill -9 confirmed dead)
cuda:2 状态: 基本空闲 (9593/97887 MiB, ~10%)
registry 修复: ✅
  - evi_f1 = 0.1838 (joint, corrected)
  - evi_f1_tp = 0.6237 (TP-only, corrected)
```

注：registry 中无 v3 条目，无需更新。cuda:2 残余 ~9.6GB 可能是其他小进程或 CUDA context 残留。

---
