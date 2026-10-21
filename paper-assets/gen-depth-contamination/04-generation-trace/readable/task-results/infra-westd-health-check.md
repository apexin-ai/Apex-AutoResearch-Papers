# infra westd health check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-health-check_20260519T202556_result.json`
- **Structured JSON:** [`7d9274e7dc3fdb35ca4d.json`](../../sessions/7d/7d9274e7dc3fdb35ca4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 1. exp_deberta_c4 (PID 130789) — **已完成**

| 项目 | 状态 |
|------|------|
| 进程 | 存活，运行 49m42s（bash wrapper 尚未退出） |
| 进度 | **5/5 fold 全部完成**，每 fold 3 epoch，loss 从 ~1.44 降至 ~1.10 |
| 配置 | Config=exp_14b_c4, 30000 samples, 6 classes (depth 0-5), 5000 docs |
| 结果文件 | `exp_14b_c4_oof.npz` (1.88MB) 已生成 |
| GPU 0 | **0% 利用率**，787 MiB / 97887 MiB — 训练实际已结束 |

训练数据完整，每 fold ~188s/epoch，总计 ~47 min 符合预期。

---

### 2. exp_32b_c4 (PID 44715) — **运行中，接近尾声**

| 项目 | 状态 |
|------|------|
| 进程 | 存活，运行 **1天13小时22分** |
| 进度 | **depth 5**: 2290/2500 batches (**92%**) |
| 速度 | ~14.5-14.9 s/it |
| 剩余时间 | ~210 batches × 14.7s ≈ **51 min** |
| GPU 1 | **90% 利用率**，64775 MiB / 97887 MiB |

Depth 5 是最后一个 depth (0-5)，完成后整个 pipeline 结束。预计约 **50 分钟后**完成。

---
