# check w38 w27 status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_w38-w27-status_20260527T185655_result.json`
- **Structured JSON:** [`2770324d4be8104ebc37.json`](../../sessions/27/2770324d4be8104ebc37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已修复为 RUNNING。汇总：

### 实验状态

| 实验 | 服务器 | 进度 | 当前数据 |
|------|--------|------|----------|
| **Attn k=0.5 s43** (w38) | westd-38929 GPU:3 | T0 ep=40/50 | 27/40=68% |
| **Attn k=0.85 s43 v2** (w27) | westd-27271 GPU:0 | T1 完成，进入 T2 | T0: 26%, T1: 56%, 累计 41/100=41% |
| **Attn k=0.75 s43 v2** (w27) | westd-27271 GPU:1 | T2 ep=20/50 | T0: 58%, T1: 68%, T2 当前 70%, 累计 63/100=63% |

- w38 实验刚启动约 17 分钟，registry 已从 PREPARING 修复到 RUNNING
- w27 两个实验都正常推进，k=0.75 比 k=0.85 快（GPU 共享影响不同）且成功率明显更高
- k=0.85 的 T0 只有 26% 异常低，值得关注

---
