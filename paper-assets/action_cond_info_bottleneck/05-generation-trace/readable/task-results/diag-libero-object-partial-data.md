# diag libero object partial data

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_libero_object_partial_data_20260515T213244_result.json`
- **Structured JSON:** [`b6c12099df7a09773c2f.json`](../../sessions/b6/b6c12099df7a09773c2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 新进程状态：正常运行

- **PID 294229** 存活，已运行 ~11 分 36 秒
- **当前位置**：`libero_object` suite，task 1，episode 4/5 正在跑 rollout（step ~167/280）
- **已完成**：`libero_object_0` 全部 10 episodes，`libero_object_1` 已完成 4 episodes
- 日志显示之前 `libero_spatial` 已完成（10 tasks 全部跑完），现在进入 `libero_object`
- 后续还有 `libero_goal` 和 `libero_10` 两个 suites

### 2. libero_object 旧数据：无冲突风险

- 输出目录 `baseline_plus_v2/libero_object/` 下**没有 `eval_info.json`**（只在所有 tasks 跑完后才生成）
- 当前只有 `videos/` 目录，包含 `libero_object_0`（10 episodes）和 `libero_object_1`（4 episodes in progress）
- 这些都是当前新进程产生的，不是旧残留数据——新进程从 task 0 开始重跑了整个 suite

### 3. GPU 使用

| PID | 显存 | 用途 |
|-----|------|------|
| 294229 | 5480 MiB | baseline_plus remaining suites (cuda:0) |
| 308788 | 5476 MiB | baseline_std (cuda:1) |

两个进程各占 ~5.5GB，RTX PRO 6000 96GB 资源充裕。

---
