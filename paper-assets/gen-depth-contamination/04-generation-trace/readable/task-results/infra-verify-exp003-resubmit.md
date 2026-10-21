# infra verify exp003 resubmit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify_exp003_resubmit_20260513T064705_result.json`
- **Structured JSON:** [`84e0ca904e805b0f4bc1.json`](../../sessions/84/84e0ca904e805b0f4bc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-003 正在正常运行，无需修复。**

状态报告：

1. **状态**：运行中
2. **tmux session**：`exp_003_decoding_ablation` 存在，PID 29459
3. **当前任务**：ablation config 1 (greedy decoding)，正在执行 `run_exp003_ablation.sh 1`
4. **进度**：depth 1 生成中，28/313 batches (~9%)，seed data (depth 0) 已完成 5000 samples
5. **主 Python 进程**：PID 29472，CPU 91.4%，参数 `--no_sample`（greedy），`--num_samples 5000 --max_depth 5`
6. **GPU**：45% 利用率，3919 MiB 显存占用
7. **启动时间**：14:43（约 4 分钟前）

日志显示命令正确展开为 4 个顺序 ablation（`sh 1 && sh 2 && sh 3 && sh 4`），当前正在跑第一个。按 ~6s/batch 估算，depth 1 还需约 29 分钟，整个 config 1（5 个 depth）约 2.5 小时，全部 4 个 config 约 10 小时。

---
