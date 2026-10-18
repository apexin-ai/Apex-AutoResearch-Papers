# ops scp libero to 38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scp-libero-to-38929_20260520T083600_result.json`
- **Structured JSON:** [`a52ca22e665d1feb6896.json`](../../sessions/a5/a52ca22e665d1feb6896.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**传输报告：**

| 目录 | 源 (27271) | 传输前 (38929) | 传输后 (38929) |
|------|-----------|---------------|---------------|
| `libero/libero/assets/` | 405M | 334M | 398M |
| `assets/turbosquid_objects/` | 69M | 20M | 69M |
| `assets/textures/` | 36M | 20M | 33M |
| `.cache/libero/` | 2.2M | 0 | 2.2M |

实际传输量：~54MB（rsync 增量传输）。

**验证结果：**
- `libero_object` / `libero_spatial` / `libero_goal` 三个 suite 均加载成功（各 10 tasks）
- `OffScreenRenderEnv` 创建、reset、set_init_state 均正常
- robosuite 基础环境正常

---
