# code llama sparsity sweep

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-sparsity-sweep_20260512T022148_result.json`
- **Structured JSON:** [`80ebd744c341404e3ef0.json`](../../sessions/80/80ebd744c341404e3ef0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交。

- **Job**: `llama-sparsity-sweep` (PID 18296)
- **Server**: seetacloud-bjb2-structtts, cuda:0
- **Sparsity levels**: 50%, 55%, 60%, 65%, 70%
- **Log**: `~/runs/redundancy-compound-sparsity/llama-sparsity-sweep.log`
- **结果输出**: `/home/sonny/redundancy-compound-sparsity/results/neg_cross_model/llama_sparsity_sweep_results.json`

脚本会对 20 道 MATH 题逐一生成 + forward pass 收集 perturbation，预计运行 30-60 分钟。可用 `check-training-status` 查看进度。

---
