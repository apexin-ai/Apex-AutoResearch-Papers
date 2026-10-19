# code fix output file bug

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-output-file-bug_20260515T165248_result.json`
- **Structured JSON:** [`7b939776d4033f6335de.json`](../../sessions/7b/7b939776d4033f6335de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 台服务器已修复。

## 总结

**根因**：seed=42 的 CRM 实验（crm_obs_only, crm_perdof, crm_scalar 等）在 submit_training_job 时命令中没有包含 `--output_file` 参数，导致 argparse 使用默认值 `None`，日志打印 `output_file=None`，最终不生成 JSON 结果文件。JSON 文件后来靠 `parse_log_to_json.py` 从日志手工生成。

**修复**：在 `main()` 中 `parse_args()` 之后、打印 args 之前，增加自动生成默认输出路径的逻辑：

```python
if args.output_file is None:
    args.output_file = f"logs/eval_{args.benchmark}_{args.mode}_seed{args.seed}.json"
```

**已同步的服务器**：
- bjb2-40593 — `/root/acr-vla-conformal-refinement/src/evaluate.py` (line 390)
- bjb1-18228 — `/root/acr-vla-conformal-refinement/src/evaluate.py` (line 398, 此版本多 `--start_task` 参数)
- bjb1-32546 — `/root/acr-vla-conformal-refinement/src/evaluate.py` (line 390)
- bjb2-28827 — `/root/acr-vla-conformal-refinement/src/evaluate.py`

**注意**：当前正在运行的 seed=43 实验进程不受此修复影响（它们已经有 `--output_file` 在命令行中）。此修复确保未来所有实验无论是否显式传 `--output_file`，都会生成 JSON 输出。

---
