# diagnose gpu utilization

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_utilization_20260528T033252_result.json`
- **Structured JSON:** [`a5439b210bfd9e0fc4e4.json`](../../sessions/a5/a5439b210bfd9e0fc4e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### westd-38929

| GPU | Util | 显存占用 | 状态 |
|-----|------|---------|------|
| 0 | 45% | 10486 MiB / 97887 MiB | 正常运行 |
| **1** | **0%** | **1 MiB / 97887 MiB** | **实验已完成，GPU 空闲** |
| 2 | 35% | 10686 MiB / 97887 MiB | 正常运行 |
| 3 | 13% | 11050 MiB / 97887 MiB | 正常运行（可能在 task 加载阶段） |

**GPU 1 问题确认**：`pi05_attention_k0.90_seed45` 已跑完，结果已保存到 `eval_results/pi05_attention_k0.90_libero_10_seed45.json`。GPU 1 现在完全空闲，可以部署新实验。

### westd-41074

| GPU | Util | 显存占用 | 状态 |
|-----|------|---------|------|
| 0 | 18% | 10692 MiB / 97887 MiB | 正常（random_k09_long_seed45） |
| 1 | 0% | 9961 MiB / 97887 MiB | 显存占用正常，瞬时 0% = eval task 加载阶段 |
| 2 | 50% | 10464 MiB / 97887 MiB | 正常（l2norm_k07_long_seed45） |
| 3 | 31% | 10638 MiB / 97887 MiB | 正常（attn_k075_long_seed45） |

**w41 无异常**。4 张卡均有进程在跑，GPU 1 利用率为 0% 是 eval 间歇行为（显存 ~10GB 仍被占用，进程存活）。

### 结论
- **w38 GPU 1 空闲**，实验已完成，可部署新任务
- **w41 全部正常**，无需干预

---
