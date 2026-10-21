# eval vtc m32 spatial

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_vtc_m32_spatial_20260519T200623_result.json`
- **Structured JSON:** [`52cdda8692be44bd84e7.json`](../../sessions/52/52cdda8692be44bd84e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前 GPU 状态：

| GPU | 任务 | 进度 | 预计完成 |
|-----|------|------|----------|
| 0 | train m16_seed44 | 44,150/100K | ~3.9h |
| 1 | train m128_seed43 | 69,150/100K | **~2.1h** |
| 2 | train m16_seed43 | 68,750/100K | **~2.2h** |
| 3 | eval m32_seed44 object | 14/5000 ep | ~8-10h |

所有 GPU 都忙。**GPU 1 和 GPU 2 最快释放（~2h）**。GPU 3 的 eval 不是串行 sweep，只是单个 m32_seed44 object eval，但 500ep×10tasks 预估 8-10h。

Checkpoint 确认：`smart_compress_m32/checkpoint.pt`（May 18，应为 seed42 首次训练产物）。Eval 脚本支持 `--suite libero_spatial`（max_steps=280）。

**建议**：等 GPU 1（m128_seed43）训练完成后提交 Spatial eval。要我设置轮询监控，训练完自动提交？

---
