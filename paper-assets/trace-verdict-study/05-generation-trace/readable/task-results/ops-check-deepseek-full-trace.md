# ops check deepseek full trace

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-deepseek-full-trace_20260515T145318_result.json`
- **Structured JSON:** [`dc4dc845a58595d269d9.json`](../../sessions/dc/dc4dc845a58595d269d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结果

| 项目 | 状态 |
|------|------|
| **进程状态** | **ALIVE** — PID 112299 (`python train/train_sft.py --condition full_trace`), 运行 ~1h06m |
| **训练进度** | step 129/444 (29%), ~36s/step, 预计还需 ~3h10m |
| **GPU 0** | 100% 利用率, 71567/97887 MiB — 被 full_trace 占用，**不空闲** |
| **GPU 1** | 100% 利用率, 22423/97887 MiB — 被 `deepseek_exception_only_seed42` (PID 107198) 占用 |
| **Checkpoint** | 尚无 safetensors 产出（正常，129/444 step，可能在训练结束后才保存） |
| **tmux** | read-only 模式无法查 tmux，但进程链完整（112289→112293→112299）确认存活 |

### 日志中 "Terminated/EXIT_CODE=129" 解释

这是**第一次运行**（13:39 UTC 启动，被 SIGHUP 杀掉）的 EXIT trap 追加写入。当前是第二次运行（13:47 UTC 启动），用 `>` 截断了日志后开始写入，但第一次运行的 trap 稍后触发，用 `>>` 追加了 `EXIT_CODE=129` 到日志末尾。同理 `/tmp/agent-ml-exit/` 的 exit file 也是第一次运行留下的。

**结论**：进程正常运行中，registry 状态应从 PREPARING 更新为 RUNNING。

---
