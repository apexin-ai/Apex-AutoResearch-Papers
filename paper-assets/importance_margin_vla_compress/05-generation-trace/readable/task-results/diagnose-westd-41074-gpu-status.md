# diagnose westd 41074 gpu status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd-41074-gpu-status_20260525T193225_result.json`
- **Structured JSON:** [`306f25e5f9aa2e892433.json`](../../sessions/30/306f25e5f9aa2e892433.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 experiments are progressing well. Here's the summary:

## westd-41074 状态报告

### GPU 状态：全部占用（非空闲）
所有 4 张 RTX PRO 6000 Blackwell (~16GB used, ~70% utilization) 都在运行实验。

### 实验进度

| GPU | 实验 | 进度 | 当前成绩 |
|-----|------|------|----------|
| 0 | `random_k05_object_v2` (stale) | Task 3/10, Ep 20/50 | Task SR ~40% |
| 1 | `l2norm_k05_object_v2` (stale) | Task 3/10, Ep 20/50 | Task SR ~45% |
| 2 | `zeromask_random_k09_object` | Task 3/10, Ep 40/50 | Task SR ~77.5% |
| 3 | `zeromask_l2norm_k09_object` | Task 3/10, Ep 40/50 | Task SR ~87.5% |

### 已完成操作
- **Registry 更新**：2 个 stale v2 实验标记为 `conclusion: killed`
- **Registry 更新**：2 个 zeromask 实验状态从 PREPARING → RUNNING

### 需要决策
**GPU 0 和 GPU 1** 仍在运行 stale v2 实验（v4/v5 已 success）。进程仍在消耗 GPU 资源。要杀掉这两个进程释放 GPU 吗？如果是，这两张卡可以部署新实验。

### Zeromask 初步信号
- zeromask_l2norm k=0.9 当前 task 3 SR=87.5% vs hard-prune l2norm k=0.9=70.6% → zero_mask 显著优于 hard-prune
- zeromask_random k=0.9 当前 task 3 SR=77.5% vs hard-prune random k=0.9=62.8% → 同样 zero_mask 更好

这暗示**位置扰动（而非信息丢失）可能是 hard-prune 性能下降的主因**，与假设一致。不过才 task 3/10，最终结果需要等全部完成。

---
