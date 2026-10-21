# code extract frontier cms

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_extract_frontier_cms_20260522T055917_result.json`
- **Structured JSON:** [`3b407f711b6995b949f1.json`](../../sessions/3b/3b407f711b6995b949f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

22 confusion matrices 已提取并保存到 `artifacts/plan011_frontier_cms.json`。

**覆盖情况：**
- **CivilComments** (7 configs): deepseek/fs5 ✓, qwen2.5-7b/{zs,fs3,fs5} ✓, qwen3/{zs,fs3,fs5} ✓
- **HuMAID** (7 configs): deepseek/{zs,fs3,fs5} ✓, llama4/{zs,fs3,fs5} ✓, qwen3/{zs,fs3} ✓
- **VAST** (8 configs): deepseek/zs ✓, llama4/{zs,fs3,fs5} ✓, qwen2.5-7b/{zs,fs3,fs5} ✓

**特别提到的 frontier 数据已全部包含：**
- CivilComments: deepseek/fs5 (acc=0.741), qwen3/fs3 (acc=0.811), qwen3/fs5 (acc=0.821)
- VAST: llama4/zs (acc=0.523), llama4/fs3 (acc=0.501)

**注意事项：**
- vast/llama4_few-shot-5 只有 346 样本（JSONL 不完整，280KB vs 完整文件~1.2MB）
- civil_comments/qwen3_zero-shot 只有 1079 样本（JSONL 521KB，可能未跑完）
- vast/deepseek_zero-shot 只有 1000 样本
- NPZ 来源的矩阵 label 顺序可能与 JSONL 来源不同（如 vast NPZ 用 [pro, con, neutral]，JSONL 用 [con, neutral, pro]），使用时注意 `labels` 字段

---
