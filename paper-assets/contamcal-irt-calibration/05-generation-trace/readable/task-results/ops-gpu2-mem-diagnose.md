# ops gpu2 mem diagnose

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu2-mem-diagnose_20260514T074245_result.json`
- **Structured JSON:** [`d2ecdfd7b5bee56bf8cf.json`](../../sessions/d2/d2ecdfd7b5bee56bf8cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到关键对比信息了。

## 诊断报告

### 1. 模型是否正确
**正确。** cmdline 和日志均确认加载 `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B`。

### 2. dtype
**bf16 正确。** 代码 `torch_dtype=torch.bfloat16` + SFTConfig `bf16=True`。日志中的 `torch_dtype is deprecated! Use dtype instead!` 仅是重命名警告，transformers 仍以 bf16 加载模型（向后兼容的别名，所有跑的任务都有这个警告）。

### 3. device_map
**无问题。** 代码中未设 `device_map`，通过 `CUDA_VISIBLE_DEVICES=2` 映射到 GPU 2。

### 4. 真正原因：**batch_size 差异**

对比两个训练配置：

| 参数 | 0.5B d025 (当前) | 1.5B d100 (参考 10046 MiB) |
|------|---------|---------|
| batch_size | **4** | **1** |
| grad_accum | 4 | 16 |
| max_seq_length | 2048 | 2048 |
| gradient_checkpointing | 无 | 无 |

`batch_size=4` 意味着每步前向传播同时处理 4 条 2048 token 的序列。无 gradient_checkpointing 时，24 层 transformer 每层需保存 ~10 个中间张量用于反向传播。激活显存粗估：

- 0.5B batch=4: 24 层 × ~330 MB/层 ≈ **7.9 GB** 纯激活
- 1.5B batch=1: 28 层 × ~150 MB/层 ≈ **4.1 GB** 纯激活

加上模型权重、优化器、CUDA 缓存分配器 overhead，0.5B batch=4 达到 21 GB 是可以解释的。**显存占用高是 batch_size=4 + 无 gradient_checkpointing 的正常结果，不是 bug。**

之前的 0.5B d005 v3 和 d100 也用 batch_size=4，如果它们也跑过，显存应该类似。

### 5. 结论

**不需要 kill 重提交。** 训练正常运行（loss ~1.5，正常收敛），只是与 1.5B 的对比不公平（batch_size 不同）。

如果后续想降低 0.5B 显存占用（比如同 GPU 跑别的任务），修复方案：
- `--batch-size 1 --grad-accum 16`（保持相同有效 batch_size=16，显存降至 ~6-8 GB）
- 或在 SFTConfig 中启用 `gradient_checkpointing=True`（batch_size=4 不变，显存约减半）

---
