# probe v7 new ckpt5000 probe a

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_probe_v7-new-ckpt5000-probe-a_20260516T135000_result.json`
- **Structured JSON:** [`570a1efb91eb18388023.json`](../../sessions/57/570a1efb91eb18388023.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**无法在 GPU 1 执行 Probe A** — GPU 1 被 v7 seed2 训练占满：

| GPU | PID | 进程 | 显存 |
|-----|-----|------|------|
| 0 | 21363 | v7 contrastive 训练 (step 6800/20000) | 16220 MiB |
| 1 | 27427 | v7 seed2 训练 (seed=1337) | 16216 MiB |

两块 GPU 都被训练占满，无法在 GPU 1 启动 Probe A。

**选项：**
1. Kill seed2（PID 27427）后跑 Probe A（probe 只需几分钟，跑完可重启 seed2）
2. 在 CPU 上跑 Probe A（慢但不影响任何训练）
3. 等某个训练结束后再跑

要怎么处理？

---
