# code flashinfer install

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_flashinfer_install_20260519T162318_result.json`
- **Structured JSON:** [`1e4cd03d596aa843c205.json`](../../sessions/1e/1e4cd03d596aa843c205.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

安装完成。汇总：

**安装方式**: pip（已预装，`Requirement already satisfied`）

**版本**: flashinfer-python **0.6.11.post3**

**注意**: Blackwell GPU (SM 12.x) 需要 CUDA ≥12.9，当前环境 CUDA 12.8 会输出警告 `Failed to get device capability`，但导入正常。

**Sparse/mask 相关 API**:

顶层:
- `flashinfer.BlockSparseAttentionWrapper` — 块稀疏注意力
- `flashinfer.VariableBlockSparseAttentionWrapper` — 可变块稀疏注意力
- `flashinfer.sparse` — 稀疏注意力子模块
- `flashinfer.top_k_mask_logits` — top-k mask logits

`flashinfer.sparse` 子模块:
- `BlockSparseAttentionWrapper`
- `VariableBlockSparseAttentionWrapper`
- `MaskMode`
- `convert_bsr_mask_layout`
- `segment_packbits`
- `block_sparse_attention_run_trace`
- `variable_block_sparse_attention_run_trace`
- `determine_attention_backend`

---
