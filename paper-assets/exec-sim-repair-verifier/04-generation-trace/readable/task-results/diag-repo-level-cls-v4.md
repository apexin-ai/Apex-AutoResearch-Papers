# diag repo level cls v4

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_repo-level-cls-v4_20260513T063442_result.json`
- **Structured JSON:** [`c7f00ac99c57df6b8497.json`](../../sessions/c7/c7f00ac99c57df6b8497.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：进程在 step 3000 的 eval 阶段 (75%, 3528/4668) 被系统外部 kill，疑似 OOM killer。日志无任何 Python error/traceback/CUDA error，无 stderr 文件——典型的静默系统级 kill。

**存活 Checkpoint**：
| Checkpoint | eval_loss |
|-----------|-----------|
| **checkpoint-200** | **0.0701** ★ BEST，完好 |
| checkpoint-2400 | 0.1504 |
| checkpoint-2600 | 0.2466 |

**值得注意**：best metric 在 step 200 之后从未被超越，后续 13 次 eval loss 在 0.13-0.36 间剧烈震荡，训练质量存疑。当前 GPU 上有新进程 PID 2935724 在运行（~9min, 12376MiB VRAM）。

报告已写入 `artifacts/diag_cls_v4.md`。

---
