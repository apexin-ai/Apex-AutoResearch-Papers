# diagnose w38 attn k09 s45

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w38_attn_k09_s45_20260528T035234_result.json`
- **Structured JSON:** [`20af474d73823949928b.json`](../../sessions/20/20af474d73823949928b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 汇总

| 项目 | 状态 |
|------|------|
| **进程** | PID 893108 已退出，EXIT_CODE=0（正常完成） |
| **GPU 利用率** | GPU 0: 47%, GPU 1: **0% (空闲)**, GPU 2: 39%, GPU 3: 0% (有显存占用) |
| **实验结果** | **SR = 65.0%** (attn k=0.9, libero_10, seed45, 50 episodes) |
| **耗时** | ~155 min (~2.6h) |
| **Per-task SR** | 48, 92, 46, 84, 64, 98, 52, 58, 18, 90 |
| **Registry** | → DONE/success, metrics 已写入 |

Attn k=0.9 四个 seed 汇总：s42=64.0%, s43=62.8%, s44=64.0%, **s45=65.0%** → **mean ≈ 64.0%±0.8pp**

**w38:cuda:1 现已空闲，可部署新实验。**

---
