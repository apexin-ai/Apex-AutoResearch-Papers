# debug exp002 minkpp crash

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_exp002-minkpp-crash_20260514T105031_result.json`
- **Structured JSON:** [`667b468cca65414ee468.json`](../../sessions/66/667b468cca65414ee468.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 完整 Traceback

```
File "signal_minkpp.py", line 161, in compute_minkpp_signal
    lp = compute_token_logprobs(target_model, target_tok, text, max_length)
File "signal_minkpp.py", line 96, in compute_token_logprobs
    return token_log_probs[0].cpu().numpy()
TypeError: Got unsupported ScalarType BFloat16
```

### 根因

`signal_minkpp.py:compute_token_logprobs` 返回 `token_log_probs[0].cpu().numpy()`，模型以 bfloat16 推理，bfloat16 tensor 无法直接转 numpy。需要 `.float()` 中间转换。

### selfcritique 没有独立 bug

selfcritique 看起来"FAIL"是因为 compute_signals.py 按顺序执行 `embedding → minkpp → selfcritique`，minkpp 崩溃后进程直接退出，selfcritique 从未运行。dryrun4 测试证实 selfcritique 独立运行 **PASS**。

### 当前状态：已修复，已在跑

- `signal_minkpp.py` 已在 18:46:03 修复为 `.cpu().float().numpy()`
- 新的 batch run (PID 353388) 在 18:46:36 启动，使用修复后的代码
- 9 个任务（3 dosages × 3 benchmarks），GPU 0
- 当前在 task 1/9 (d000_s42/mmlu)，进程 353390 活跃运行中（724% CPU, 4138 MiB GPU）
- 无需额外干预

---
