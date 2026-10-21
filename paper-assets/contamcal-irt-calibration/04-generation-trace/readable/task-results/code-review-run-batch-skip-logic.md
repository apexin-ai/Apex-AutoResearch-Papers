# code review run batch skip logic

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code-review_run_batch_skip_logic_20260515T200323_result.json`
- **Structured JSON:** [`3add02aebcc3421d43ad.json`](../../sessions/3a/3add02aebcc3421d43ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：skip 是**一次性检查**，不是逐任务检查

关键代码在 `main()` 函数中：

**Task list 构建阶段**（启动时执行一次）：
```python
for dosage in dosages:
    for benchmark in benchmarks:
        if skip_completed and merged_output_exists(model_name, dosage, benchmark):
            skipped.append(...)
            continue
        task = build_task(...)
        tasks.append(task)
```

**执行阶段**（无 re-check）：
```python
for i, task in enumerate(tasks, 1):
    # 直接执行，不重新检查 merged_output_exists
    result = subprocess.run(task["cmd"], ...)
```

`merged_output_exists` 检查的是 `signals_merged_{benchmark}.json` 文件是否存在，但**只在构建 task list 时调用一次**。执行循环里没有任何重新扫描 output 目录的逻辑。

**这是一个 bug。** 场景：signals_3B_v5 在 cuda:4 启动，构建 task list 时 d025/mmlu 尚未完成，被加入队列。如果另一个 GPU 上的进程随后先完成了 d025/mmlu 并写入了 `signals_merged_mmlu.json`，v5 执行到 d025/mmlu 时不会重新检查，会重复计算。

**修复方案**：在执行循环里、每个 task 执行前加一次 `merged_output_exists` 检查：

```python
for i, task in enumerate(tasks, 1):
    # 逐任务 re-check
    if skip_completed and merged_output_exists(model_name, task["dosage"], task["benchmark"]):
        logger.info("[%d/%d] SKIP (completed by another process): %s", ...)
        continue
    # ... 原有执行逻辑
```

需要修复吗？

---
