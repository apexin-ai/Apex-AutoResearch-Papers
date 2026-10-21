# diagnose eval perdof object norm003 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-perdof-object-norm003-seed44_20260518T133049_result.json`
- **Structured JSON:** [`b6dd3922f7a9cf5063d6.json`](../../sessions/b6/b6dd3922f7a9cf5063d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常运行。

**诊断结果：**

| 项目 | 内容 |
|---|---|
| **错误** | `bash: line 1: python: command not found` (EXIT_CODE=127) |
| **根因** | 原命令用 `source /root/miniconda3/bin/activate && python ...`，但 `submit_training_job` 通过 tmux 在 `sh` 下执行，`source` 是 bash 内置命令，`sh` 下静默失败，导致 `python` 不在 PATH |
| **修复** | 直接使用绝对路径 `/root/miniconda3/bin/python`，与同服务器成功实验（PID 832702 等）一致 |
| **GPU** | cuda:2 空闲，沿用原分配 |
| **状态** | 已重新提交，PID 853859，日志显示 evaluate.py 已正常加载参数并开始执行 |

---
