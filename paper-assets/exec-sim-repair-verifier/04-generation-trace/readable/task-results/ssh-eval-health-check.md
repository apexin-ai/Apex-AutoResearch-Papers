# ssh eval health check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval-health-check_20260519T231959_result.json`
- **Structured JSON:** [`10a076b5f29bd1c85cf2.json`](../../sessions/10/10a076b5f29bd1c85cf2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认结果：

**两个 eval 都因参数错误立即崩溃了（EXIT_CODE=2）。** 原始 PID 875433 和 875580 均已死亡。

**根因**：命令用了 `--output_dir`，但脚本实际参数是 `--output`。

正确参数名：
- `--output` — Summary JSON 输出路径（默认 `eval_repo_cls.json`）
- `--pred_output` — Predictions JSONL 输出路径（默认 `eval_repo_cls_predictions.jsonl`）

**当前 GPU 状态**（来自 nvidia-smi）：
| GPU | 显存占用 | PID | 说明 |
|-----|---------|-----|------|
| 0 | 17173/32607 MiB | 876210 | 有进程在跑（不是你的 eval） |
| 1 | 0 MiB | — | 空闲 |
| 2 | 29615/32607 MiB | 833672 | 有进程在跑 |
| 3 | 16377/32607 MiB | 876070 | 有进程在跑（不是你的 eval） |

两个 eval 需要用 `--output` 替代 `--output_dir` 重新提交。需要我现在修复命令并重跑吗？

---
