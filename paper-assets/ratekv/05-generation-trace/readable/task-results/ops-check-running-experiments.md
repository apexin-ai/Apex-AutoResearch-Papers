# ops check running experiments

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_running_experiments_20260516T030645_result.json`
- **Structured JSON:** [`758bec0e0714693acd32.json`](../../sessions/75/758bec0e0714693acd32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

### 1. llama_longctx_8k_eval — **已完成，成功**
- 进程：**不在运行**，已正常退出
- 输出文件：`/root/ratekv/artifacts/llama_8k_eval_results.json`（May 16 11:01）
- 结果摘要：BF16 8K PPL=5.5958, MCKP PPL=6.0537, Uniform 4-bit PPL=6.0364
- 耗时：3.9min

### 2. internlm2_constrained_mckp — **已完成，失败**
- 进程：**不在运行**，崩溃退出
- 输出文件：**无**（artifacts 中没有对应结果文件）
- 日志：`/root/ratekv/logs/internlm2_constrained_mckp.log`
- 错误：`ModuleNotFoundError: No module named 'transformers.models.internlm2'`
  - BF16 baseline 阶段跑完了（PPL=9.7920），在 uniform 4-bit 阶段 `patch_attention` 时崩溃
  - 根因：`eval_ppl.py:_get_rotary_fn()` 尝试动态导入 `transformers.models.internlm2`，但 HuggingFace transformers 没有内置的 InternLM2 模块

### 其他
- tmux 仅有 `gemma2_9b_full_pipeline` session（无关）
- 服务器上正在下载 Qwen2.5-32B（PID 393106）

Registry 应将 `llama_longctx_8k_eval` 标记为 DONE，`internlm2_constrained_mckp` 标记为 FAILED。

---
