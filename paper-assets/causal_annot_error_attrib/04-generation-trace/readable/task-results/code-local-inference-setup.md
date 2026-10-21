# code local inference setup

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_local_inference_setup_20260521T010835_result.json`
- **Structured JSON:** [`65eda4c04326fcd2ef6f.json`](../../sessions/65/65eda4c04326fcd2ef6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 标注结果

| Dataset | Prompt | Samples | Parse Rate | Accuracy | Diag Avg |
|---|---|---|---|---|---|
| civil_comments | zero-shot | 1500 | 100% | 74.2% | 0.717 |
| civil_comments | few-shot-3 | 1500 | 100% | 68.9% | 0.730 |
| civil_comments | few-shot-5 | 1500 | 100% | 73.9% | 0.749 |
| vast | zero-shot | 1500 | 99.9% | 48.0% | 0.473 |
| vast | few-shot-3 | 1500 | 100% | 46.1% | 0.453 |
| vast | few-shot-5 | 1500 | 100% | 46.5% | 0.459 |

### 执行摘要

- **模型**: Qwen2.5-7B-Instruct（本地，RTX 5090）
- **方案**: vLLM 的 flash_attn 与 RTX 5090 (sm_120/Blackwell) 不兼容，改用 transformers + `model.generate()` 批量推理（batch_size=8）
- **产出**: 6 个 JSONL + 6 个 confusion matrix NPZ，在 `results/{civil_comments,vast}/qwen2.5-7b_*.{jsonl,npz}`
- **model_key**: `qwen2.5-7b`，output 中 model 字段为 `qwen2.5-7b-local`
- **代码修改**: 服务器上的 `annotate.py` 已添加 `--local-model` 参数 + `LocalAnnotationPipeline` 类，与现有 API 标注完全兼容

---
