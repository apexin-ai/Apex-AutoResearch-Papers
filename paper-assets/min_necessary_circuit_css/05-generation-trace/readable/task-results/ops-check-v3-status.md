# ops check v3 status

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_v3_status_20260512T205252_result.json`
- **Structured JSON:** [`e7c851d4b5049efdfeb5.json`](../../sessions/e7/e7c851d4b5049efdfeb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态：仍在运行

**进程**：PID 279210 / 279220 存活，日志持续更新（最近写入 2026-05-13 04:53:49 CST）

**进度总览**：
| 阶段 | 方法 | 状态 |
|------|------|------|
| Phase A | EAP-IG | ✅ 完成（cache 1.37MB） |
| Phase B | edge_pruning | ✅ 完成（cache 1.34MB） |
| Phase B | ACDC | 🔄 运行中 **96.9%** (31471/32491) |
| Phase C | CSS 交叉分析 | ⏳ 未开始 |

**ACDC 当前状态**：
- 已移除 31384 条边，保留 87 条边
- 正在扫描 Layer 2 attention heads (A0→A2, A1→A2 连接)
- 速度 ~3.00 it/s，进度条显示剩余 ~5:40
- 已运行 1h17m

**预估剩余**：ACDC 约 **5-6 分钟**完成，之后 Phase C (CSS) 通常很快（< 1 分钟）。整体实验预计 **~10 分钟内**结束。

---
