# ops submit llama rsft train cuda2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_llama_rsft_train_cuda2_20260517T030342_result.json`
- **Structured JSON:** [`00051ef63ab803ffba9a.json`](../../sessions/00/00051ef63ab803ffba9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**执行摘要：**
- cuda:2 确认空闲 → 训练已启动（PID 404050），当前占用 ~14.8 GB
- 模块名修正：`freige.training.rsft_trainer`（非 `rsft_train`）
- 参数修正：`--rsft_data_path`（非 `--scored_data`），`--num_epochs`（非 `--epochs`），无 `--top_k`
- 训练数据：8829 samples 确认
- tmux session: `plan_016_llama_rsft_train`
- Registry: `plan_016_llama_rsft_train` → RUNNING, `plan_016_llama_ced_scoring` → DONE(success)

---
