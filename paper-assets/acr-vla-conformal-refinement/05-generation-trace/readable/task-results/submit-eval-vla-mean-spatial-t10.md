# submit eval vla mean spatial t10

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_eval-vla-mean-spatial-t10_20260514T221721_result.json`
- **Structured JSON:** [`08512501416571977332.json`](../../sessions/08/08512501416571977332.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

T10 rollout 正在进行中（每 5 个 rollout 输出一次进度）。预计 ~1-2h 完成。

总结当前状态：

**方案**: 单任务补跑（非全部重跑）
- 修改 `evaluate.py` 添加 `--start_task 9` 参数，跳过已完成的 T1-T9
- 任务已在 tmux session `eval-vla-mean-spatial-t10` 中运行
- 结果将输出到 `/root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json`
- Registry 已注册为 `eval-vla-mean-spatial-t10`（RUNNING）

**已有 T1-T9 结果** (31/90 = 34.4%):
| Task | Success Rate |
|------|-------------|
| between_plate_and_ramekin | 70% (7/10) |
| next_to_ramekin | 100% (10/10) |
| from_table_center | 0% (0/10) |
| on_cookie_box | 30% (3/10) |
| in_top_drawer | 0% (0/10) |
| on_ramekin | 0% (0/10) |
| next_to_cookie_box | 80% (8/10) |
| on_stove | 0% (0/10) |
| next_to_plate | 30% (3/10) |
| on_wooden_shelf | **运行中** |

**Kill 原因**: 磁盘空间正常（root 58%, data 40%），可能是系统级 OOM 或 AutoDL 实例维护。无法从日志中确认具体原因（无 traceback）。

等 T10 完成后需手动合并结果到完整的 10/10 汇总。可用 `tail /root/autodl-tmp/logs/eval-vla-mean-spatial-t10.log` 监控进度。

---
