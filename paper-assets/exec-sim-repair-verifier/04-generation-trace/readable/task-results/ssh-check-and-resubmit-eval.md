# ssh check and resubmit eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-and-resubmit-eval_20260519T232129_result.json`
- **Structured JSON:** [`0196d0daad82c299be23.json`](../../sessions/01/0196d0daad82c299be23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：不需要重提交。** 两个进程都是正确的 eval。

| GPU | PID | 进程 | 运行时间 | 显存占用 | GPU Util |
|-----|-----|------|---------|---------|----------|
| 0 | 876210 | `eval_repo_cls.py` CLS 8B s456 ckpt-2200 | ~2 min | 17,452 MiB | 77% |
| 3 | 876070 | `eval_repo_cls.py` DeepSeek CLS s456 ckpt-2163 | ~2 min | 16,886 MiB | 71% |

两个进程参数都用了 `--output`（非 `--output_dir`），checkpoint/model 路径正确。与你给的命令有两处小差异：`--batch_size 1`（非 16）、输出文件名是 `eval_summary.json`/`predictions.jsonl`（非 `eval_repo_cls.json`/`eval_repo_cls_predictions.jsonl`），但这些不影响功能正确性。

另外 GPU 2 上有 PID 833672 占用 29,606 MiB，GPU 1 空闲（0 MiB，但 GPU-Util 显示 100% 可能是瞬时波动）。

---
