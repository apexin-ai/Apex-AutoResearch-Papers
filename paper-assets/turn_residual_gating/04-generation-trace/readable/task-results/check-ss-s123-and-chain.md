# check ss s123 and chain

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_ss_s123_and_chain_20260523T133353_result.json`
- **Structured JSON:** [`968fa30ec97d410ee733.json`](../../sessions/96/968fa30ec97d410ee733.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### SS s123 训练状态：进行中（Epoch 1/3）

| 项目 | 状态 |
|------|------|
| PID 84793 | **运行中**，已运行 5h40m |
| 当前进度 | Epoch 1（epoch_0 在 18:33 保存，耗时 ~2h38m） |
| epoch_1 目录 | 尚未创建 → epoch 1 仍在训练（SS 比例递增导致后期 epoch 更慢） |
| 预计完成 | epoch 1 ~22:00，epoch 2 ~00:30（粗估） |
| GPU 占用 | 32612 MiB / 97887 MiB，RTX PRO 6000，GPU-Util 55% |

### GPU 链状态

| 项目 | 状态 |
|------|------|
| wait_and_launch.sh (v1) | **已超时退出**（10min 超时，19:29 退出） |
| wait_and_chain_v2.sh (PID 94251) | **存活**，已运行 1h47m，6h 超时兜底 |
| gpu_chain_next.sh | 尚未触发（等待 PID 84793 退出后自动启动） |

### 风险

v2 等待脚本 6h 超时 = 19:46 + 6h = 次日 01:46。如果训练在 00:30 前完成，链可以正常接续。如果训练超过 01:46 还没结束（不太可能），v2 会超时退出导致链断裂。

当前无需干预，链路完整。

---
