# infra registry sync audit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_registry_sync_audit_20260513T230318_result.json`
- **Structured JSON:** [`5f1f8756d77574c15af4.json`](../../sessions/5f/5f1f8756d77574c15af4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
PROCESS_STATUS:
  grammar_only:    running, PID=126473, GPU=cuda:1 (GPU-342cbca6), progress=315/551
  unconstrained:   running, PID=126948, GPU=cuda:1 (GPU-342cbca6), progress=276/551
  s2_pilot50:      completed (no process), progress=50/50, output=118KB
  docred_schema:   running, PID=116365, GPU=cuda:0 (GPU-0ce19412), progress=684/998

GPU_ALLOCATION:
  GPU 0: docred_schema (PID 116365), 24442 MiB used / 97887 MiB, util 87%
  GPU 1: grammar_only (PID 126473) + unconstrained (PID 126948), 16502+16502=33004 MiB used / 97887 MiB, util 92%

CRASH_ROOT_CAUSE:
  dmesg: [无法读取 — read_only 不允许 dmesg]
  journalctl: [无法读取 — read_only 不允许]
  实际状态: 4 个实验均无异常，3 个在跑，s2_pilot50 已正常完成
```

注意：grammar_only 和 unconstrained 共享 GPU 1（各占 ~16.5GB），两者都设了 `--device cuda:0` 但通过 `CUDA_VISIBLE_DEVICES` 隔离——grammar_only 未设 CUDA_VISIBLE_DEVICES（实际映射到物理 GPU 1），unconstrained 设了 `CUDA_VISIBLE_DEVICES=1`。两个进程在同一张卡上并行跑，GPU 利用率 92%。

---
