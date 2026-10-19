# infra p2b final status check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_p2b_final_status_check_20260512T161937_result.json`
- **Structured JSON:** [`2e38814ba65480679d10.json`](../../sessions/2e/2e38814ba65480679d10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**情况 B：5/9 runs 失败，不自行重启。**

## 状态汇总

### 成功完成（4 runs）

| Run | val_loss | recall@1 | Checkpoints |
|-----|----------|----------|-------------|
| random_s42 | 0.0347 | 0.984 | 200/400/600/final ✓ |
| random_s123 | 0.0446 | 0.984 | 200/400/600/final ✓ |
| random_s456 | 0.0189 | 0.992 | 200/400/600/final ✓ |
| embedding_distance_s42 | 0.1876 | 0.874 | 200/400/600/final ✓ |

### 失败（5 runs）

| Run | 失败点 | 已有 checkpoint |
|-----|--------|----------------|
| embedding_distance_s123 | torch.save @ step 400 | checkpoint-200 (6.2GB, 可能有效) + checkpoint-400 (1.3GB, **截断**) |
| embedding_distance_s456 | torch.save @ step 200 | checkpoint-200 (**197KB, 损坏**) |
| dataflow_aware_s42 | torch.save @ step 200 | checkpoint-200 (197KB, 损坏) |
| dataflow_aware_s123 | torch.save @ step 200 | checkpoint-200 (197KB, 损坏) |
| dataflow_aware_s456 | torch.save @ step 200 | checkpoint-200 (197KB, 损坏) |

### 错误原因

统一报错 `RuntimeError: [enforce fail at inline_container.cc:668] . unexpected pos` — PyTorch `torch.save()` 写入 zip 文件时位置校验失败。正常 model.pt 应为 ~5.8GB，但失败 run 的 checkpoint 只有 197KB（损坏）或 1.3GB（截断）。

从 embedding_distance_s123 开始级联失败。首个失败 run 还能完整保存 checkpoint-200（6.2GB），之后的 run 连 checkpoint-200 都无法正常保存。

### 环境状态

- **磁盘**: `/root/autodl-tmp` 93% (156G/169G, 剩余 14G) — 单个完整 checkpoint 5.8GB，空间不足以支持多 run 同时保存
- **GPU**: 0/1/2/4 空闲，3 和 5 被其他进程占用（各 23GB 和 9GB）
- **无训练进程运行中**

### 等待 Director 指令

需要决定：
1. 是否清理磁盘空间后重跑 5 个失败 run
2. embedding_distance_s123 的 checkpoint-200 是否可作为 fallback 评估
3. 4 个成功 run 是否先启动评估，不等失败 run

---
