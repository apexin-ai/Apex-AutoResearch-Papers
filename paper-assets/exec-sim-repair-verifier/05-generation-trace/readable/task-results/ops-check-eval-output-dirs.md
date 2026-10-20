# ops check eval output dirs

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-eval-output-dirs_20260513T184403_result.json`
- **Structured JSON:** [`8ffc2d1f332de6503417.json`](../../sessions/8f/8ffc2d1f332de6503417.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
subset500 目录: 空（仅 . 和 ..），创建于 May 14 01:52
tok1024 目录: 空（仅 . 和 ..），创建于 May 14 01:09
污染风险: no（两个目录均为空，无旧文件残留）
PID 167481: running（已运行 44m19s）
当前进度: 320/500  running_acc=67.5%（最后更新 02:42:56 UTC）
GPU 状态:
  cuda:0: 24923/32607 MiB, 65%
  cuda:1: 25960/32607 MiB, 93%  ← eval 进程（CUDA_VISIBLE_DEVICES=1）
  cuda:2: 10779/32607 MiB, 47%
  cuda:3: 25751/32607 MiB, 36%
```

注意：predictions.jsonl 尚未写入磁盘，脚本可能在全部推理完成后一次性写出。按当前速率（~6min/40样本），剩余 180 样本预计还需 ~27min。

---
