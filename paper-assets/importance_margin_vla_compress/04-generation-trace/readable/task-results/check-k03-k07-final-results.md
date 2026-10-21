# check k03 k07 final results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_k03_k07_final_results_20260517T125457_result.json`
- **Structured JSON:** [`78c42b7290c6998afc1b.json`](../../sessions/78/78c42b7290c6998afc1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**确认 2 个 cameras**（agentview + wrist）。这证实了 bug：mask 的 seq_len = 2×N_per_camera，而 connector 单次输出 seq_len = N_per_camera，永远不匹配。

---

## 总结

### 结果状态（两个 eval 仍在运行）

**k=0.3 trained ACIS** (Task 8 in progress, ~ep 42/50):
| Task | SR |
|------|----|
| 0 | 0/50 (0.0%) |
| 1 | 27/50 (54.0%) |
| 2 | 31/50 (62.0%) |
| 3 | 37/50 (74.0%) |
| 4 | 21/50 (42.0%) |
| 5 | 13/50 (26.0%) |
| 6 | 16/50 (32.0%) |
| 7 | 25/50 (50.0%) |
| 8-9 | (running) |
| **累计 (Tasks 0-7)** | **170/400 (42.5%)** |

**k=0.7 trained ACIS** (Task 9 in progress, ~ep 3/50):
| Task | SR |
|------|----|
| 0-7 | **完全相同** |
| 8 | 29/50 (58.0%) |
| 9 | (running) |
| **累计 (Tasks 0-8)** | **199/450 (44.2%)** |

### 关键发现：Pruning Hook 从未生效

**根因**：`register_acis_hook` 注册在 `connector` 模块上，该模块 per-camera 调用（输出 shape `(B, N_per_cam, D)`）。但 `compute_acis_mask` 返回的 mask 是所有 cameras 拼接后的（shape `(B, 2*N_per_cam)`）。

Hook 中的守护检查 `tokens.shape[1] != mask.shape[1]` 永远为 True → 直接 `return output` → **零 pruning**。

**结果**：两个 eval 实际上都在跑未 pruned 的模型（backbone 相同，因为 ACIS 训练时 backbone frozen），所以 per-task SR 完全一致。

### 对比 baseline

fullft_100k_object baseline (10 eps/task): overall 36%。当前结果 ~42-44%，差异来自 episode 数量不同导致的统计波动（baseline 只跑了 10 eps），整体 pattern 一致。

### 需要修复

`eval_success_rate_libero.py` 中的 pruning hook 逻辑需要修改，要么：
1. 将 mask 按 per-camera 拆分，每次 hook 调用使用对应 camera 的 sub-mask
2. 或将 hook 注册到更上层的模块（在所有 cameras 拼接后的位置）

---
