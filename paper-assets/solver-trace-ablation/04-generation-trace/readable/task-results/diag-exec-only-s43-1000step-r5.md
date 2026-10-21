# diag exec only s43 1000step r5

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exec-only-s43-1000step-r5_20260516T235414_result.json`
- **Structured JSON:** [`3c5b7621148536133f31.json`](../../sessions/3c/3c5b7621148536133f31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### r5 失败原因
- **EXIT_CODE=129 (SIGHUP)**，进程被 `Killed`，仅完成 4 步
- 日志时间 `07:50:22` 启动，r6 tmux session 创建于 `07:51:34`
- **确认怀疑成立**：r6 提交时使用了同一 `output_dir` (`plan001_exec_only_s43_1000_r2`) 并占用同一 GPU (cuda:0)，r5 的 tmux session 被杀导致 SIGHUP

### r6 状态：健康运行中
| 项目 | 状态 |
|------|------|
| tmux session | `exec-only-s43-1000step-r6` 存活 |
| PID 991155 | 运行中，CPU 111%，RSS ~2.6GB |
| GPU 占用 | 85110 MiB on GPU-0 |
| 训练进度 | step 14/1000，~12.6s/step，预计 ~3.5h 完成 |
| reward 趋势 | step 14 prove_rate=0.375, parse_rate=1.0，正常 |

### 注意
r6 没有独立日志文件（未重定向到 `~/runs/`），训练输出仅在 tmux pane 内。如果 tmux 被意外关闭，输出会丢失。不过 TRL 会有 checkpoint 保存，训练结果不会丢。

---
