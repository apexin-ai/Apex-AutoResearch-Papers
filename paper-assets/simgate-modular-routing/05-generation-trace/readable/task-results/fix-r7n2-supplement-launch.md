# fix r7n2 supplement launch

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_r7n2-supplement-launch_20260516T070432_result.json`
- **Structured JSON:** [`2d69e78ea7408fb30b6e.json`](../../sessions/2d/2d69e78ea7408fb30b6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动。

**结果：**
- **PID**: 9298
- **GPU1 显存占用**: 13213 MiB / 32607 MiB
- **GPU1 利用率**: 41%
- **训练进度**: 已开始 epoch 1（~12% 完成，约 1 it/s）
- **tmux session**: `r7n2-supp`
- **日志**: `/tmp/r7n2_supplement.log`

修复了 `r7n2_scale_study.py` 第 650-653 行的语法错误（`--dry_run` 和 `--scales` 参数定义交错）后训练正常运行。

---
