# code llama 3seed downstream ci

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_3seed_downstream_ci_20260515T215434_result.json`
- **Structured JSON:** [`94af56c89b43633fedc0.json`](../../sessions/94/94af56c89b43633fedc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交并运行中。

**状态**：
- 脚本 `run_llama_3seed_downstream_ci.py` 已创建并通过 dry-run
- tmux 会话 `llama_3seed_ci` 在 cuda:1 上运行
- MCKP 分配：{4: 253, 8: 1, 2: 2}, budget=0.2500
- 模型正在加载，随后执行 bf16 baseline → uniform 4-bit → 3×MCKP-k2 评估
- 日志：`/root/ratekv/llama_3seed_downstream_ci.log`
- 输出：`/root/ratekv/artifacts/llama_3seed_downstream_ci_results.json`

---
