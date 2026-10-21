# ops cqa1 xvla k05 seed43 check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-xvla-k05-seed43-check_20260521T075354_result.json`
- **Structured JSON:** [`3af2eb057067879a3dd6.json`](../../sessions/3a/3af2eb057067879a3dd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

L2norm k=0.5/k=0.7 seed42 结果文件不存在，确认 GPU 1/2 上的实验仍在运行。

## 汇总

### 已完成（registry 已更新为 DONE）

| 实验 | GPU | Mode | k | Seed | SR | 对照 |
|------|-----|------|---|------|----|------|
| eval_xvla_random_k05_object_seed43 | 3 | random | 0.5 | 43 | **71.0%** | seed42=70.6% |
| eval_xvla_random_k07_object_seed43_v2 | 0 | random | 0.7 | 43 | **65.0%** | seed42=65.2% |

**非单调性再次确认**：两个 seed 都显示 k=0.5 > k=0.7 (seed43: 71.0% > 65.0%, seed42: 70.6% > 65.2%)

### 仍在运行

| 实验 | GPU | Mode | k | Seed |
|------|-----|------|---|------|
| eval_xvla_l2norm_k05_object_seed42 | 1 | L2norm | 0.5 | 42 |
| eval_xvla_l2norm_k07_object_seed42_v2 | 2 | L2norm | 0.7 | 42 |

### GPU 状态
- GPU 0/1/2: 有进程（~4.5GB），GPU 0 可能已启动新实验
- **GPU 3: 空闲**

### 额外发现（batch sweep 结果，非 registry）
- random k=0.3 seed42 = 62.8%
- random k=0.85 seed42 = 63.6%
- random k=0.5 spatial seed42 = 71.4%
- random k=0.85 spatial seed42 = 67.6%

---
