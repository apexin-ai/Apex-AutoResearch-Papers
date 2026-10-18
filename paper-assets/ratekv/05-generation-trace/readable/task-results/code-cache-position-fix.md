# code cache position fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cache-position-fix_20260513T205335_result.json`
- **Structured JSON:** [`783965ef461998b951b9.json`](../../sessions/78/783965ef461998b951b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**修改清单：**
- `profiler.py` 第89行：`model(input_ids, use_cache=False)` → `model(input_ids, use_cache=False, cache_position=torch.arange(input_ids.shape[1], device=input_ids.device))`
- `eval_ppl.py` 第134行：`model(chunk, use_cache=False)` → `model(chunk, use_cache=False, cache_position=torch.arange(chunk.shape[1], device=chunk.device))`

**grep 确认：** 两个文件中所有 `model(` 调用均已包含 `cache_position=`。

**--output 参数：** run_mvp.py 第50行已有 `--output` 参数，第222行正确使用 `args.output`，无需修改。

**Smoke test：** `SMOKE TEST OK, logits shape: torch.Size([1, 2, 152064])`

**进程清理：** PID 130821 已清理。

---
