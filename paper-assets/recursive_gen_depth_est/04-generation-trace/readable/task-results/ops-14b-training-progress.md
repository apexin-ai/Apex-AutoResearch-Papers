# ops 14b training progress

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_14b_training_progress_20260519T053429_result.json`
- **Structured JSON:** [`3804061a1864f7e3f20c.json`](../../sessions/38/3804061a1864f7e3f20c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程都活着，正在 d0 generation 阶段。汇报如下：

---

## 14B 实验进度报告（~13:36 CST）

### 进程状态
| PID | GPU | VRAM | 状态 |
|-----|-----|------|------|
| 776616 | GPU-0 | 32,304 MiB | **alive** (temp09) |
| 787051 | GPU-1 | 32,302 MiB | **alive** (topk50) |

### temp09（τ=0.9）
- **当前阶段**: d0 generation — **1,766 / 5,000** samples (35.3%)
- **已运行**: ~2h36m（11:00 CST 启动）
- **d0 生成速率**: ~11.3 samples/min
- **d0 剩余**: ~4.8h
- **全流程预估**: d0 generation 单阶段约 7.4h；4 个 depth 的 generation 约 28-30h，加上 4 轮 training + feature extraction + RF eval，总计预估 **~35-40h**，剩余 **~32-37h**

### topk50（k=50）
- **当前阶段**: d0 generation — **674 / 5,000** samples (13.5%)
- **已运行**: ~37min（12:59 CST 启动）
- **d0 生成速率**: ~18.2 samples/min
- **d0 剩余**: ~4.0h
- **全流程预估**: d0 generation 单阶段约 4.6h；4 depth generation 约 18-20h，加上 training + eval，总计预估 **~24-28h**，剩余 **~23-27h**

### 备注
- topk50 速率（18.2 samples/min）比 temp09（11.3 samples/min）快约 60%，可能因为 top-k 截断使采样更高效
- 日志文件未增长（log 只记录到 model loading），实际进度需通过 `wc -l depth_*.jsonl` 查看
- 两个实验均为单 GPU 运行，互不干扰

---
