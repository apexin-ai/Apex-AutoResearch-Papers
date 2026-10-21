# diagnose cuda1 next readiness

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cuda1_next_readiness_20260521T071019_result.json`
- **Structured JSON:** [`3afb1779dd48432c9b41.json`](../../sessions/3a/3afb1779dd48432c9b41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 就绪状态汇总

### NORA Spatial 实验 — **READY** ✅

| 组件 | 状态 |
|------|------|
| **Checkpoint** (`nora-libero-spatial/`) | 7.1G, 2/2 shards 齐全 (index 引用的文件全部存在) |
| **Phi3V Base** (`phi3v-base/`) | 7.8G, 2/2 shards 齐全 |
| **Script** (`nora_spatial_full_pipeline.py`) | 存在, 23KB |
| **Data** (`libero_spatial/`) | 10 个 hdf5 文件齐全 |

**NORA Spatial 可以立即在 cuda:1 上跑。** Checkpoint、base model、脚本、数据全部就位。

### Object Pipeline — **FAILED**

日志显示连接 HuggingFace 失败，无法加载 `openvla/openvla-7b` 的 `processing_prismatic.py`，EXIT_CODE=1。需要 `source /etc/network_turbo` 或离线加载才能修复。

---
