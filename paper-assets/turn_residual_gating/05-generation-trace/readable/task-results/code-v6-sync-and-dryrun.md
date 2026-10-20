# code v6 sync and dryrun

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v6_sync_and_dryrun_20260518T173544_result.json`
- **Structured JSON:** [`c7608882ee4cda300d6a.json`](../../sessions/c7/c7608882ee4cda300d6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 代码同步 ===
gar.py: 已同步 (188行)
train_phase2.py: 已同步 (341行)
config.py: 已同步 (16行)
语法检查: 通过

=== v6 Dry-run ===
状态: 失败 (显存不足，非 OOM crash)
原因: v5 占用 85.4GB / 97.9GB，剩余 11.8GB 不足以加载 7B 模型
      device_map="auto" 将参数 offload 到 meta device，turn_embedding.to() 在 meta tensor 上失败
GPU 显存: 85.4 GB / 97.9 GB (v5 占用中，仅剩 11.8GB)
结论: 代码同步有效，等 v5 完成后再 dry-run v6
```

---
