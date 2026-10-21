# ssh check gpu state

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-gpu-state_20260515T144052_result.json`
- **Structured JSON:** [`daebd6a1e8b6b0f9aead.json`](../../sessions/da/daebd6a1e8b6b0f9aead.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### GPU 状态
| GPU | 型号 | 显存占用 | 利用率 | 进程 |
|-----|------|---------|--------|------|
| 0 | RTX PRO 6000 Black (96GB) | 1297MiB / 97887MiB | 0% | python3 (PID 617024) — PCA action_prediction |
| 1 | RTX PRO 6000 Black (96GB) | 1297MiB / 97887MiB | 0% | python3 (PID 617376) — PCA action_delta |

两块 GPU 都在跑 PCA 实验，显存占用极低（~1.3GB），利用率 0%（当前可能在做 PCA/CPU 计算阶段）。

### 实验状态

| 实验 | 模型 | 状态 | 详情 |
|------|------|------|------|
| **action_prediction** | trained | 完成 | 33 层全部完成 + summary |
| **action_prediction** | untrained | 完成 | 33 层全部完成 + summary |
| **action_delta** | trained | 仅 layer_4 | dry-run 结果，只有 1 层 |
| **action_delta** | untrained | 不存在 | 目录不存在 |
| **DINO action_prediction** | dinov2 | 仅 layer_0 | 只有 1 层结果，未完整 |
| **DINO action_delta** | dinov2 | 不存在 | 目录不存在 |
| **PCA action_prediction** | trained, pca=1024 | **运行中** | GPU0, 已完成 2/33 层 (正在跑 Layer 2)，运行 3h16m |
| **PCA action_delta** | trained, pca=1024 | **运行中** | GPU1, 已完成 1/33 层 (正在跑 Layer 1)，运行 2h22m |

### 关键发现
- 两个 PCA 实验正在跑，每层约 90-120 秒，预计各需约 1 小时完成剩余层
- DINO 的 action_prediction 只跑了 layer_0 就停了，action_delta 完全没跑
- 原始 action_prediction (trained/untrained) 已全部完成
- action_delta 之前只做了 trained layer_4 的 dry-run

---
