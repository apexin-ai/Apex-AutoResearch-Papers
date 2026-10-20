# diag llama docred full s1 mt6144

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_llama_docred_full_s1_mt6144_20260515T082058_result.json`
- **Structured JSON:** [`f389a39c97b7537c7692.json`](../../sessions/f3/f389a39c97b7537c7692.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

**根因**：`CUDA error: invalid device ordinal`。命令用了 `--device cuda:1`，但启动实验的 tmux session 很可能设了 `CUDA_VISIBLE_DEVICES=0`，导致进程只能看到一块 GPU，`cuda:1` 不存在。`nvidia-smi` 确认硬件有 2 块 RTX PRO 6000，硬件无问题。崩溃位置：`run_constrained_extraction.py:655` → transformers `caching_allocator_warmup` (modeling_utils.py:6090)。

**当前状态**：日志已被新运行覆盖，新运行切到 `cuda:0` 正常推理中（输出文件 34KB）。需注意如果 unconstrained 实验也在 `cuda:0`，两个实验共用同一 GPU 有 OOM 风险。

报告已写入 `artifacts/llama_docred_full_s1_mt6144/failure_diagnosis.md`。

---
