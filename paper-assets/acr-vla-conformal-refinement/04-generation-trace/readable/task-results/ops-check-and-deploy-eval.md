# ops check and deploy eval

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-and-deploy-eval_20260521T191743_result.json`
- **Structured JSON:** [`e18672f7bfff8cc7f492.json`](../../sessions/e1/e18672f7bfff8cc7f492.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 6 个 Python 进程存活且活跃。bjb2-28827 两个进程正在将模型加载到 GPU（RSS 分别 11.7GB 和 18.3GB）。

---

## 汇总

### 1. Checkpoint 信息

| Checkpoint | 路径 | 大小 | 来源 |
|-----------|------|------|------|
| **Object** | `crm_pi05_full/object/crm_best.pt` | 2.4M (2,484,379 bytes) | 当前训练 epoch 7, val_loss=0.005363 (训练仍在继续 epoch 8/50) |
| **Spatial** | `crm_pi05_full/spatial/crm_best.pt` | 2.4M (2,484,379 bytes) | 从 `crm_pi05/spatial/` 复制（⚠️ crm_pi05_full spatial 训练失败：缺少 merged spatial cache） |

### 2. 训练最终 loss
- **Object**: Epoch 7 best val_loss=**0.005363**, train_loss=0.009826（训练仍在继续）
- **Spatial (crm_pi05_full)**: 训练未启动（`FileNotFoundError: No precomputed cache at .../spatial`）
- **Spatial (crm_pi05 旧版)**: 训练到 epoch 6，checkpoint 已可用

### 3. rsync 完成确认
4 个 scp-3 传输全部成功（exit code 0），两台 eval 服务器均已验证文件存在 (2.4M)。

### 4. Eval PID 和服务器分配

| # | Benchmark | Seed | Server | GPU | PID | 状态 |
|---|-----------|------|--------|-----|-----|------|
| 1 | object | 42 | bjb1-18228 | cuda:0 | 804191 | 14.7 GB, 74% util, rollout 中 |
| 2 | object | 43 | bjb1-18228 | cuda:1 | 804563 | 14.5 GB, 25% util |
| 3 | object | 44 | bjb1-32546 | cuda:0 | 196419 | 14.1 GB, 27% util |
| 4 | spatial | 42 | bjb1-32546 | cuda:1 | 196777 | 9.5 GB, 加载中 |
| 5 | spatial | 43 | bjb2-28827 | cuda:0 | 123807 | 加载中 (11.7GB RSS) |
| 6 | spatial | 44 | bjb2-28827 | cuda:1 | 124161 | 加载中 (18.3GB RSS) |

### 5. GPU 占用确认
- **bjb1-18228**: GPU 0 = 14,677 MiB ✓, GPU 1 = 14,537 MiB ✓
- **bjb1-32546**: GPU 0 = 14,125 MiB ✓, GPU 1 = 9,546 MiB (加载中)
- **bjb2-28827**: GPU 0/1 正在将模型从 CPU → GPU（进程活跃，CPU 利用率 300%+）

### ⚠️ 注意事项
1. **Object CRM 训练仍在 bjb1-18228 GPU 0 上运行**（与 eval 共用同一 GPU，暂未冲突）
2. **Spatial checkpoint 来自旧训练 (crm_pi05)**，非 crm_pi05_full 重训版。crm_pi05_full spatial 训练因缺少 merged cache 失败。如需重训 spatial，需先运行 `--precompute` 或 `--auto`。

---
