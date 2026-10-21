# code fix repo level sample weight

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-repo-level-sample-weight_20260512T112618_result.json`
- **Structured JSON:** [`2a1367fa9be3d612cdd8.json`](../../sessions/2a/2a1367fa9be3d612cdd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验正常启动，正在预处理数据。

## 修复摘要

**根因**：HuggingFace Trainer 默认 `remove_unused_columns=True`，会移除模型 `forward()` 签名中不存在的列。`sample_weight` 在 `preprocess_split` 中正确添加到 Dataset，但在送入 `compute_loss` 前被 Trainer 剥离，导致 `KeyError: 'sample_weight'`。

**修复**：在两个脚本的 `TrainingArguments` 中添加 `"remove_unused_columns": False`，保留 `sample_weight` 列供 `WeightedCausalLMTrainer.compute_loss` 使用。

## 实验状态

| 实验 | PID | tmux session | GPU | 状态 |
|------|-----|-------------|-----|------|
| repo-level-cls | 34670 | `repo-level-cls` | cuda:2 | 正常启动，class weights: fail=1.7009, pass=0.2991 |
| repo-level-cwm | 34752 | `repo-level-cwm` | cuda:3 | 正常启动，正在预处理 |

---
