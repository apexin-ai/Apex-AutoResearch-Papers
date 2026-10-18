# ops submit llama 8k eval

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_llama_8k_eval_20260516T025548_result.json`
- **Structured JSON:** [`da46d98f6658a873bb4a.json`](../../sessions/da/da46d98f6658a873bb4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

- **脚本同步**：`run_llama_8k_eval.py` 已上传到 `/root/ratekv/`
- **依赖**：`eval_ppl.py`、`solver.py`、两个 profile JSON 均已存在
- **环境**：2x RTX PRO 6000 Blackwell，模型已在 `/root/autodl-tmp/models/`
- **实验已提交**：tmux session `llama_longctx_8k_eval`，运行在 `cuda:1`（通过 `CUDA_VISIBLE_DEVICES=1`）
- **Registry**：`llama_longctx_8k_eval` → RUNNING
- **日志**：`/root/ratekv/logs/llama_longctx_8k_eval.log`

早期日志显示 solver 已完成（bit distribution: {4:253, 8:1, 2:2}），模型加载完毕，正在进行 8K stride PPL 评估。

---
