# code cwm eval incremental save

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cwm-eval-incremental-save_20260514T123735_result.json`
- **Structured JSON:** [`2cad9bd4353bf6c8b127.json`](../../sessions/2c/2cad9bd4353bf6c8b127.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程正常运行中（状态 Rl+），不受磁盘上文件修改的影响。

### 改动总结

**修改了 `eval_repo_cwm.py`**，添加增量 JSONL 写入 + 续跑支持：

1. **`run_inference` 新增参数** `incremental_path`, `completed_indices`
2. **批次跳过**：如果整个 batch 的 index 都在 `completed_indices` 中，直接 skip（续跑时跳过已完成部分）
3. **逐条写盘**：每处理完一个 sample，立即 `open(path, 'a')` + `flush()` 追加一行 JSON 到 `results_incremental.jsonl`
4. **`main()` 中的续跑逻辑**：启动时如果 `results_incremental.jsonl` 已存在，加载已完成的 index 集合，传给 `run_inference` 跳过
5. **结果合并**：inference 完成后 `all_results = completed_results + results`，按 index 排序，用于计算最终 metrics 和写入原有的 summary JSON / predictions JSONL
6. **原有写入逻辑不变**：最终仍然写 `eval_repo_cwm.json` + `eval_repo_cwm_predictions.jsonl`，保持兼容

增量文件路径：`{output_dir}/results_incremental.jsonl`。下次重启脚本时自动检测并续跑。

---
