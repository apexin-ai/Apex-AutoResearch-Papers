# status downstream and seed42 check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_downstream_and_seed42_check_20260519T193035_result.json`
- **Structured JSON:** [`ebe7e5470d114ac8aec1.json`](../../sessions/eb/ebe7e5470d114ac8aec1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. Downstream Eval 状态

| 模型 | 状态 | ARC-Easy (acc) | ARC-Chall (acc_norm) | HellaSwag (acc_norm) | PIQA (acc) | WinoGrande (acc) |
|------|------|-------|-------|-------|-------|-------|
| adaptive_ood_seed123 | ✅ 完成 | 0.6671 | 0.3481 | 0.4791 | 0.6850 | 0.5706 |
| adaptive_ood_seed456 | ✅ 完成 | 0.6519 | 0.3541 | 0.4800 | 0.6877 | 0.5714 |
| uniform_ood_seed123 | ✅ 完成 | 0.6637 | 0.3507 | 0.4797 | 0.6844 | 0.5762 |
| uniform_ood_seed456 | 🔄 运行中 | — | — | — | — | — |

**uniform_ood_seed456** (PID 340636) 仍在运行，当前阶段：模型已加载完成，正在从缓存加载数据集（网络不可达，用 cached 版本）。尚未开始实际 eval 推理，预计还需 ~2 分钟完成全部 5 个 benchmark。

### 2. adaptive_fromscratch_seed42 训练进度

| 指标 | 值 |
|------|-----|
| 当前 step | **1037 / 6103** (17%) |
| 速度 | ~2.24 s/step |
| 预计剩余 | **~3h 09min** |
| weighted_loss (近期) | 2.5 ~ 3.1 |
| unweighted_loss (近期) | 1.5 ~ 2.5 |

PID 337777 正常运行中。

### 3. GPU 状态

| GPU | 型号 | 利用率 | 显存 | 用途 |
|-----|------|--------|------|------|
| 0 | RTX PRO 6000 Black (98GB) | **100%** | 45.6 / 97.9 GB | adaptive_fromscratch_seed42 训练 |
| 1 | RTX PRO 6000 Black (98GB) | **0%** | 3.7 / 97.9 GB | uniform_ood_seed456 eval（加载中） |
| 2 | RTX PRO 6000 Black (98GB) | 0% | 空闲 | — |
| 3 | RTX PRO 6000 Black (98GB) | 0% | 空闲 | — |

GPU 2、3 空闲可用。

---
