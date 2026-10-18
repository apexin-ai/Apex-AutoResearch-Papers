# ops d168 westd27271 xvla v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d168_westd27271_xvla_v2_20260522T141008_result.json`
- **Structured JSON:** [`43e82bdb61c846e6e769.json`](../../sessions/43/43e82bdb61c846e6e769.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### GPU 实际状态

| GPU | Session | 当前任务 | 进度 |
|-----|---------|----------|------|
| 0 | `xvla_spatial` | Baseline (k=1.0), task 3/10 运行中 | 3/10 tasks done, 后面还有 3 个 pruning 配置 |
| 1 | `xvla_goal` | Baseline (k=1.0), task 4/10 刚开始 | 4/10 tasks done, 后面还有 3 个 pruning 配置 |

**每个 suite 有 10 个 task × 50 episodes = 500 episodes/config，每个 config ~30 min，4 configs 共 ~2 小时。**

### 已完成的 Spatial baseline 结果（部分）
- Task 0: 98.0%
- Task 1: 100.0%
- Task 2: 100.0%

### 已完成的 Goal baseline 结果（部分）
- Task 0: 100.0%
- Task 1: 100.0%
- Task 2: 96.0%
- Task 3: 98.0%

### 新部署的实验

| tmux session | GPU | 内容 | 状态 |
|---|---|---|---|
| `xvla_long` | 0 | Long suite (baseline + l2_norm k=0.95/0.9/0.7)，max_steps=900 | 等待 `xvla_spatial` 完成后自动启动 |
| `xvla_random` | 1 | Random pruning 对照 (Object/Spatial/Goal/Long × k=0.95/0.9/0.7 = 12 runs) | 等待 `xvla_goal` 完成后自动启动 |

两个新 session 使用 `pgrep` 轮询等待，前序实验进程退出后自动接力启动。预计 Long ~2h 后开始，Random 也类似。

---
