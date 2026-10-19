# scan all servers gpu status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_scan_all-servers-gpu-status_20260523T143657_result.json`
- **Structured JSON:** [`37998ac2a38c6fe0ebb9.json`](../../sessions/37/37998ac2a38c6fe0ebb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 扫描结果

### GPU 状态

| 服务器 | GPU 使用 | 空闲 GPU |
|--------|---------|----------|
| bjb2-28827 | 6/6 busy (16-28% util) | 无 |
| bjb2-40593 | 1/1 busy (11% util) | 无 |
| cqa1-32758 | 4/6 busy (27-32% util) | **GPU 1, GPU 5** |

### 仍在运行的实验

| 服务器 | GPU | 实验 | 备注 |
|--------|-----|------|------|
| bjb2-28827 | 0/1/2 | τ-sweep τ=0.10/0.15/0.40 goal-s42 | ~9h in |
| bjb2-28827 | 3/4/5 | Long s42: reconvla/adapt/crm | ~6.7h in, 未完成 |
| bjb2-40593 | 0 | spatial-vla-only-s44 | running |
| cqa1-32758 | 0 | obj-reconvla-s44 | running |
| cqa1-32758 | 2 | long-vla-only-s43 | running |
| cqa1-32758 | 3 | k2mean-object-s44 | running |
| cqa1-32758 | 4 | long-k2mean-s42 | running |

### 已完成 & 收割（registry 已更新为 DONE）

| exp_id | SR | 服务器 | 状态 |
|--------|-----|--------|------|
| eval-supp-spatial-vla-only-s43 | **79.0%** | cqa1-32758 GPU5 | ✓ DONE |
| eval-supp-k2mean-spatial-s44 | **81.0%** | cqa1-32758 GPU1 | ✓ DONE |

### 额外发现（未在 registry 中）

| 实验 | SR | 服务器 | 说明 |
|------|-----|--------|------|
| eval-object-vla-only-wrapper-s42-r2 | 79.0% | bjb2-28827 GPU3 | 今天 06:56Z 完成，不在 registry |
| k2mean-spatial-s43 | 78.0% | cqa1-32758 | 旧 tmux session，不在 registry |

**cqa1-32758 GPU 1 和 GPU 5 空闲可用。** bjb2-28827 的 Long s42 三个实验仍在跑，未到 ETA。

---
