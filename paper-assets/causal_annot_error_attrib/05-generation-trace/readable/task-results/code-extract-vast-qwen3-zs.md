# code extract vast qwen3 zs

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_extract_vast_qwen3_zs_20260522T113310_result.json`
- **Structured JSON:** [`ab65fff4f30923967c3f.json`](../../sessions/ab/ab65fff4f30923967c3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**vast/qwen3_zero-shot CM**（已保存到 `artifacts/plan011_new_cms_vast_qwen3_zs.json`）：
- n_valid = 1499（1500 行中 1 条 skipped）
- Accuracy = 0.5117
- NPZ 实际已存在于 `/home/sonny/causal_annot_error_attrib/results/vast/qwen3_zero-shot_confusion_matrix.npz`，与 JSONL 计算结果完全一致

**其他 JSONL 缺失 NPZ 的情况**（均不完整，非 1500 行）：

| 文件 | 行数 | 状态 |
|------|------|------|
| vast/llama4_zero-shot | 1496 | 近完成 |
| vast/qwen2.5-7b_zero-shot | 1499 | 近完成 |
| vast/llama4_few-shot-5 | 346 | 未完成 |
| vast/qwen3_few-shot-3 | 77 | 未完成 |
| civil_comments/qwen3_zero-shot | 1079 | 未完成 |
| civil_comments/qwen3_few-shot-3 | 1496 | 近完成 |
| civil_comments/qwen3_few-shot-5 | 1492 | 近完成 |
| humaid/llama4_few-shot-3 | 1498 | 近完成 |
| humaid/llama4_few-shot-5 | 1471 | 部分完成 |
| humaid/deepseek_few-shot-3 | 1345 | 部分完成 |
| humaid/deepseek_few-shot-5 | 1237 | 部分完成 |
| humaid/qwen3_few-shot-3 | 1423 | 部分完成 |

没有其他 1500 行完整的 JSONL 缺 NPZ。

---
