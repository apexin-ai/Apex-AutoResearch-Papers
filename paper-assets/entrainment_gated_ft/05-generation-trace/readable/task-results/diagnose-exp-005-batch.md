# diagnose exp 005 batch

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-005-batch_20260522T163242_result.json`
- **Structured JSON:** [`2380c5bd942a0971970d.json`](../../sessions/23/2380c5bd942a0971970d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/exp-005-batch/diagnosis.md`。

**根因**：`run_eval_download.sh` 在 00:30:51 尝试加载 HGRN h3-1 模型，但 `model.safetensors` 文件仍在被其他进程下载（mtime 00:33），导致 `SafetensorError: incomplete metadata, file not fully covered`。

**次要问题**：`run_hgrn_chain.sh` 恢复脚本用了 `python -m lm_eval` 而非 patched wrapper，导致 transformers 不认识 `hgrn` 架构。

**修复**：重新下载模型并验证完整性，修复 hgrn_chain.sh 使用 FLA patch，评估前增加 safetensors 完整性检查。

---
