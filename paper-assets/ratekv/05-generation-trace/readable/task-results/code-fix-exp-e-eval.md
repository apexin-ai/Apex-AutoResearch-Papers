# code fix exp e eval

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_exp_e_eval_20260514T013707_result.json`
- **Structured JSON:** [`ca6118afd1fb534d762e.json`](../../sessions/ca/ca6118afd1fb534d762e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交并更新 registry。

**修复摘要：**
- 原因：`run_exp_e.py` eval 阶段调用 `load_dataset("wikitext", ...)` 时 HuggingFace Hub 网络不通（`Network is unreachable`），进程崩溃
- 修复：写了 `run_exp_e_eval_fix.py`，直接从本地 arrow 缓存文件加载 WikiText-2，绕过 Hub 请求
- 修复了原 `run_exp_e_eval.py` 的 3 个 bug：未提取 `profiles` 字段、device 错误、solver 参数名错误
- 已在 tmux session `exp_e_eval` 中启动，模型正在加载到 cuda:1，solver 结果确认一致

---
