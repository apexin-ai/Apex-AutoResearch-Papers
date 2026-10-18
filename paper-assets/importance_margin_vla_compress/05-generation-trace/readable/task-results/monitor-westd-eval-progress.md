# monitor westd eval progress

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd_eval_progress_20260516T233748_result.json`
- **Structured JSON:** [`1d3c9fec550e9938668c.json`](../../sessions/1d/1d3c9fec550e9938668c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU 状态
| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| cuda:0 | 3558MiB / 97887MiB | 1% | IMM v2 eval (PID 455965) |
| cuda:1 | 3702MiB / 97887MiB | 1% | Full FT seed0 libero_spatial eval (PID 452461) |

### TMux Sessions
只有 `imm_v2_eval` 一个 session。cuda:1 的 libero_spatial eval 是后台进程（非 tmux）。

---

### cuda:0 — IMM v2 eval (libero_object, acis_prune, 50 eps/task)

**状态: 进行中 — Task 1/10, Ep 1/50**

刚完成 Task 0（SR = 0/50 = 0.0%），正在跑 Task 1。启动时间 07:33，当前 07:38，Task 0 耗时约 4 分钟。

预计总时间: ~40 分钟（10 tasks × 4 min/task），预计 ~08:13 完成。

Task 0 全部 FAIL（都跑满 280 steps）。Task 1 第一个 ep 已 SUCCESS。

---

### cuda:1 — Full FT seed0 100K libero_spatial eval

**状态: 进行中**

命令: `eval_success_rate_libero.py --suite libero_spatial --num_episodes 50 --output eval_results/full_ft_seed0_100k_libero_spatial.json`

输出文件 `full_ft_seed0_100k_libero_spatial.json` 尚未生成（未在 ls 结果中出现），正在运行。启动时间 07:32。

---

### 已完成的新结果文件

#### `full_ft_seed0_100k_libero_object.json` (完成于 07:32)
| Task | SR |
|------|----|
| alphabet soup | 4% |
| cream cheese | 74% |
| salad dressing | 56% |
| bbq sauce | 68% |
| ketchup | 54% |
| tomato sauce | 32% |
| butter | 68% |
| milk | 14% |
| chocolate pudding | 80% |
| orange juice | 60% |
| **Overall** | **51.0%** (CI: 46.6%–55.4%) |

#### `full_ft_100k_libero_object_formal.json` (完成于 06:09)
- Overall SR: **44.8%** (CI: 40.5%–49.2%)
- 这是 `checkpoints/libero_full_ft_100k/checkpoint.pt`（非 seed0 版）

**对比**: seed0 (51.0%) vs 原版 (44.8%)，seed0 高 ~6 个百分点。

---
