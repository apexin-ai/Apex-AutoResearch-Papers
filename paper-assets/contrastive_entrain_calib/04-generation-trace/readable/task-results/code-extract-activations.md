# code extract activations

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_extract_activations_20260518T051500_result.json`
- **Structured JSON:** [`4f46f86263b29d6f081b.json`](../../sessions/4f/4f46f86263b29d6f081b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法正确，参数列表完整：`input`（位置参数）、`--model-path`、`--output-dir`、`--batch-size`、`--device`、`--max-samples`。

脚本已写入 `artifacts/data/extract_activations.py`，核心设计：

- **全层 sweep**：通过 `output_hidden_states=True` 提取所有 transformer 层（跳过 embedding 层），输出 shape `(num_layers, 2, hidden_dim)`
- **Token 边界定位**：逐步 tokenize 定位 critical turn 的 user/assistant 边界。先 tokenize 到 user turn 末尾找 `<|im_end|>` 前最后一个 content token；再用 `add_generation_prompt=True` 确定 assistant role marker 结束位置（即 content 起始位置），并与完整序列做前缀对齐验证，不匹配时有 probe fallback
- **OOM 自动降级**：捕获 `torch.cuda.OutOfMemoryError`，自动将 batch_size 减半重试，直到 1
- **输出**：`.pt` 文件（`torch.save`，list of dicts）+ `.jsonl` 元数据文件
- **Qwen3 兼容**：`enable_thinking=False` 避免 thinking token 干扰，`trust_remote_code=True`，bfloat16 加载

---
