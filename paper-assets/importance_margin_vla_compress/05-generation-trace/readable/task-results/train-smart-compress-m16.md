# train smart compress m16

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_smart_compress_m16_20260517T210644_result.json`
- **Structured JSON:** [`5f364e7bb54228303a8a.json`](../../sessions/5f/5f364e7bb54228303a8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

M=16 训练已稳定运行。

**汇总：**
- **PID**: 352025
- **GPU**: 3（已占用 2815 MiB）
- **Loss 趋势**: step 0 → 1.03, step 50 → 2.30 (warmup spike), step 100 → 1.03, step 150 → 0.43, step 200 → 0.46, step 250 → 0.60
- **速度**: ~4.2 steps/s
- **Registry**: `smart_compress_m16` 已注册为 RUNNING

当前 4 张 GPU 全部在跑 smart compress 实验：
| GPU | 实验 | Config |
|-----|-------|--------|
| 0 | M=32 | `smart_compress.yaml` |
| 1 | M=64 | `smart_compress_m64.yaml` |
| 2 | M=96 | `smart_compress_m96.yaml` |
| 3 | M=16 | `smart_compress_m16.yaml` |

---
