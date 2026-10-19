# research unixcoder feasibility

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_unixcoder_feasibility_20260516T051050_result.json`
- **Structured JSON:** [`cf7013236131a68acf62.json`](../../sessions/cf/cf7013236131a68acf62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

## UniXcoder 配置
- Model: `microsoft/unixcoder-base`
- Architecture: RobertaModel
- Model type: roberta
- Hidden size: 768
- Num layers: 12
- Max position: 1026（有效 **1024 token**，减去 BOS/EOS）
- Vocab size: 51,416
- Param count: **125.9M**（fp16 约 252MB）
- LoRA target_modules: `["query", "value"]`

## train.py 适配
- 可直接加载: **基本可以**，`AutoModel.from_pretrained('microsoft/unixcoder-base')` 正常工作，`last_hidden_state` 存在，mean pooling 兼容
- 需要改动:
  1. **contrastive_model.py `_apply_lora`**：`target_modules` 硬编码为 `["q_proj", "v_proj"]`（Qwen 命名），UniXcoder 用 `["query", "value"]`（RoBERTa 命名）。需要改成参数化或自动检测
  2. **`--max-seq-length`**：运行时传 `1024` 而非 `2048`
  3. **`dtype=torch.float16`**：UniXcoder 原生 fp32，`AutoModel.from_pretrained(..., dtype=torch.float16)` 对 RoBERTa 可能需要改为 `torch_dtype=torch.float16` 或 `.half()`
- 改动量: **小**（核心改动仅 LoRA target_modules 一处，其余是运行参数）
- Embedding 提取方式: mean pooling（已实现，直接兼容）

## 训练估算
- VRAM: **<2GB**（模型 252MB + LoRA 微量，seq_len 1024 batch=8 下的 activation 很小）
- 单 run: **~5-15min**（125M 模型比 3B 快约 20x，受 I/O 和 data loading 限制下限约 5min）
- 3×1 seed 总计: **~15-45min**
- 服务器：2× RTX PRO 6000 Blackwell (98GB)，VRAM 完全不是问题，可与现有 Qwen 训练并行

## 结论
- 推荐: **UniXcoder**
- 原因:
  - max_position=1026 → 有效 1024 token，截断 confound 比 CodeBERT(512) 减半，满足 Reviewer 要求
  - 125.9M 参数，与 CodeBERT-base 同量级，对比公平
  - RoBERTa 架构，`AutoModel` 直接加载，适配成本极低
  - 唯一必须改动：LoRA `target_modules` 从 `["q_proj", "v_proj"]` 改为 `["query", "value"]`，约 3 行代码
  - 训练极快，VRAM 极小，不影响现有实验

---
