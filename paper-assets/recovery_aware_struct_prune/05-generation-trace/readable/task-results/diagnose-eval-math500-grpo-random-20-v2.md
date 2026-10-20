# diagnose eval math500 grpo random 20 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_grpo_random_20_v2_20260522T000921_result.json`
- **Structured JSON:** [`fc4c1cf4a56161659d80.json`](../../sessions/fc/fc4c1cf4a56161659d80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 根因：代码 bug（`IsADirectoryError`）

评估**跑完了全部 500/500 题**（耗时 ~10 小时），在最后保存结果时崩溃：

```
IsADirectoryError: [Errno 21] Is a directory: '/root/runs/recovery_aware_struct_prune/eval_math500_grpo_random_20_v2'
```

`--output_path` 传入的是目录路径，而运行时的代码版本在 `open()` 时未做 `isdir` 转换，直接尝试把目录当文件写入。当前服务器上的代码（lines 218-220）已有 `isdir` 检查，说明实验启动时跑的是旧版代码。

### 结果可用性

- **准确率已知**：**12.00% (60/500)**，stderr ±0.0145（从日志中读取）
- **逐题详细结果丢失**：JSON 未写入磁盘，output 目录下只有 log 文件
- 无 OOM、无 CUDA error、无磁盘满、模型文件完整

### 建议修复方案

1. **直接重试**即可——当前服务器代码已修复 `isdir` bug，cuda:1 当前空闲（0MB 占用）。同样命令重跑会自动生成 `eval_math500_checkpoint-100.json`
2. 预计耗时 ~10 小时，无需改参数

---
