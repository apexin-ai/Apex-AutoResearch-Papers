# monitor baseline eval progress

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_baseline_eval_progress_20260516T013116_result.json`
- **Structured JSON:** [`213b95511f3d36935be8.json`](../../sessions/21/213b95511f3d36935be8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. PID 状态

| 实验 | PID | 状态 |
|------|-----|------|
| baseline_plus_v2 (cuda:0) | 471056 | **已退出** — 日志无 error/traceback，疑似被 OOM killer 杀死 |
| baseline_std_v3 (cuda:1) | 508625 | **存活** — 已运行 ~1h56m，正在跑 libero_goal |

### 2. GPU 利用率

| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 62% | 39016 / 97887 MiB |
| 1 | RTX PRO 6000 Blackwell | 0% | 2142 / 97887 MiB |

GPU 0 有大量显存占用但 PID 471056 已死，可能是显存未释放。GPU 1 利用率 0% 但 PID 508625 在跑，可能处于 episode 间隙或实际在 GPU 0 上运行。

### 3. Suite 完成状态

**baseline_plus_v2:**

| Suite | 状态 | Success Rate |
|-------|------|-------------|
| libero_spatial | **完成** | **81.6%** |
| libero_object | **完成** | **88.8%** |
| libero_goal | **完成** | **87.8%** |
| libero_10 | **崩溃** — 跑到 episode 4/50，rollout step 395/520 时进程死亡 | — |

**baseline_std_v3:**

| Suite | 状态 | Success Rate |
|-------|------|-------------|
| libero_spatial | **完成** | **66.0%** |
| libero_object | **完成** | **67.8%** |
| libero_goal | **进行中** — 15/50 episodes，running_success_rate=60.0% | — |
| libero_10 | 未开始 | — |

### 4. 预估剩余时间（baseline_std_v3）

- **libero_goal**: 35 episodes 剩余，~30s/episode → **~17 min**
- **libero_10**: 50 episodes × 520 steps，每 episode ~1-3 min → **~50-150 min**
- 总计约 **1-3 小时**

### 5. 需要处理

**baseline_plus_v2 的 libero_10 需要重跑。** 进程在 libero_10 第 4 个 episode 期间无错误退出，需要单独重启 libero_10 评测。

---
