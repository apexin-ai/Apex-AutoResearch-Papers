# urgent pi05 process conflict

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_pi05-process-conflict_20260521T033630_result.json`
- **Structured JSON:** [`ee40dc52bfbc35018986.json`](../../sessions/ee/ee40dc52bfbc35018986.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结果

| 项目 | 详情 |
|------|------|
| **发现进程数** | 2 个 |
| **PID 802639** | 启动 09:49，运行 1h47m，旧版命令（缺 `--n_rollouts`/`--K`/`--output_file` 参数）→ **已 kill** |
| **PID 811006** | 启动 11:30，运行 6m，新版完整命令，输出到 `eval_pi05_baseline_object_seed42_r2.json` → **保留** |
| **代码状态** | ✅ MEAN_STD 修复版（`self.state_mean`/`self.state_std`，无 q01/q99） |
| **执行操作** | kill 802639，释放 13GB 显存；无需修复代码、无需重新部署 |
| **最终状态** | cuda:0 上唯一进程 **PID 811006**，占用 10960 MiB |

---
