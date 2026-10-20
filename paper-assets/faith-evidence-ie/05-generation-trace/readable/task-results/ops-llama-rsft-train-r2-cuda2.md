# ops llama rsft train r2 cuda2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama_rsft_train_r2_cuda2_20260517T031125_result.json`
- **Structured JSON:** [`f30a8785e01961c2cdf5.json`](../../sessions/f3/f30a8785e01961c2cdf5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**总结**：
- **R1 OOM 原因**：未加 `--quantize` 和 `--bf16`，8B 模型以 fp32 加载（~32GB），无剩余空间给 LoRA/optimizer/activations
- **R2 修复**：`--quantize`（4-bit QLoRA）+ `--bf16` + batch_size=2 + grad_accum=8
- **状态**：cuda:2 上 PID 405397 稳定运行，29GB/32GB，步速 ~9.5s/step，预计 ~4.4h 完成（1656 步）
- **tmux session**：`plan_016_llama_rsft_r2`
- **日志**：`/root/runs/faith-evidence-ie/plan_016_llama_rsft_train_r2.log`

---
