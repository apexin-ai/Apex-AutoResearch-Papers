# code mvp final check

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-final-check_20260512T150630_result.json`
- **Structured JSON:** [`b535de87e91035279bfb.json`](../../sessions/b5/b535de87e91035279bfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## ACDC MVP 状态报告

**进程状态：RUNNING**

| 指标 | 值 |
|------|-----|
| 进程 | PID 98300 + 98594，均运行 `python3 run_mvp.py` |
| GPU-5 | 100% 利用率，18736MiB / 24564MiB |
| 已运行 | 2h 08m 42s |
| 总进度 | **29487 / 32491**（**90.8%**） |
| 当前速度 | ~1.51 it/s |
| 剩余 edges | 3004 |
| 预计剩余 | **~33 分钟**（ETA ≈ 23:42 服务器时间） |
| 当前阶段 | ACDC τ=0.01，第 1/5 个 threshold |
| 已剪除/保留 | Removed 29302, Left 185 |

**已完成的阶段：**
- Phase A: EAP-IG — 32491 edges scored，已缓存
- Phase B: Edge Pruning — 32491 edges scored，已缓存
- Phase B: ACDC — 正在进行（首个 τ 的边遍历接近完成，还有 4 个 τ 要跑）

**注意：** ACDC 有 5 个 threshold 要依次跑。当前是第 1 个（τ=0.01），剩余 ~33 min 完成本轮。之后还有 4 轮，但后续轮复用已有结构，通常更快。**总预估完成时间：再 1-2 小时。**

无错误、无崩溃。日志中有 HuggingFace 连接超时但已用本地模型绕过，未影响运行。

---
