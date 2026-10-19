# check eval vla mean spatial

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-vla-mean-spatial_20260514T221331_result.json`
- **Structured JSON:** [`d37d67160504c578cc4f.json`](../../sessions/d3/d37d67160504c578cc4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论明确了。日志中没有 `Overall success rate` 这行输出，说明进程在完成第 9 个 task 后、开始第 10 个 task 之前被杀掉了。

## eval-vla-mean-spatial 实验结果

**状态：崩溃/被杀（incomplete）**

进程 PID 143106 已消失，tmux 会话 `eval-vla-mean-spatial` 不存在。日志在 9/10 tasks 后截断，无 `Overall success rate` 汇总行，无 sentinel。

**已完成的 9 个 task per-task 成功率：**

| # | Task | Success Rate |
|---|------|-------------|
| 1 | bowl_between_plate_and_ramekin → plate | 70% (7/10) |
| 2 | bowl_next_to_ramekin → plate | **100%** (10/10) |
| 3 | bowl_from_table_center → plate | 0% (0/10) |
| 4 | bowl_on_cookie_box → plate | 30% (3/10) |
| 5 | bowl_in_top_drawer → plate | 0% (0/10) |
| 6 | bowl_on_ramekin → plate | 0% (0/10) |
| 7 | bowl_next_to_cookie_box → plate | **80%** (8/10) |
| 8 | bowl_on_stove → plate | 0% (0/10) |
| 9 | bowl_next_to_plate → plate | 30% (3/10) |

**Running total：31/90 = 34.4%**（与 cron 报的一致）

**缺失：第 10 个 task**（libero_spatial 共 10 tasks，task order [0-9]，第 10 个未执行）

**日志路径：** `/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log`

**异常信息：** 无错误日志输出——进程被外部信号杀掉（SIGKILL/OOM），不是代码内异常。日志末尾是 task 9 的正常成功率输出，无 traceback。当前服务器上有另一个实验 `eval-acr-spatial-v4-obs-only` 在运行（PID 199257，占 346% CPU），可能导致资源竞争。

---
