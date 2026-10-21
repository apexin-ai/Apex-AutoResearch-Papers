# ops gpu5 verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu5-verify_20260513T235945_result.json`
- **Structured JSON:** [`3cf311cd8e7cd1b953f6.json`](../../sessions/3c/3cf311cd8e7cd1b953f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

| 检查项 | 结果 |
|--------|------|
| GPU 5 有 d005 训练进程 | **是** — 但是 **v3** (PID 239734)，不是 r3 |
| GPU 0 有新增进程 | **否** — 仅有原 PID 235248 (d100 SFT) |
| r3 训练正常启动 | **否 — r3 已 OOM 崩溃 (EXIT_CODE=1)** |

### 根因

**v3 仍在 GPU 5 上运行**（PID 239734，当前进度 209/3177，~1 it/s），占用 21.5 GiB 显存。r3 (PID 240163) 也指向 GPU 5，启动时发现仅剩 459 MiB 可用，尝试分配 578 MiB 失败 → OOM 崩溃。

**好消息**：r3 的 GPU 指向正确（`CUDA_VISIBLE_DEVICES=5`），`--gpu 5` 参数生效了，没有跑到 GPU 0。

**问题**：v3 还活着占着 GPU 5，r3 和 v3 冲突了。需要先 kill v3 或等 v3 完成后再重新提交 r3。

---
