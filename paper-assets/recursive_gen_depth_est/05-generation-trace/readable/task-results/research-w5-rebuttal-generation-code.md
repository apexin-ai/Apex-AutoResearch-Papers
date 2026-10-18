# research w5 rebuttal generation code

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_w5_rebuttal_generation_code_20260515T110650_result.json`
- **Structured JSON:** [`4994cc16d678aefb1f21.json`](../../sessions/49/4994cc16d678aefb1f21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：**无条件生成（Unconditional）**

### 关键证据

**1. 生成代码** (`scripts/generate_next_depth.py`)

文件开头 docstring 直接声明：
> "用 LoRA 微调后的模型**无条件生成**下一代文本。seed_id 为独立递增编号（0..num_samples-1），**不与上一代数据对应**。"

核心代码（约第 72-73 行）：
```python
input_ids = torch.tensor([[bos_token_id]] * cur_batch_size, device=device)
attention_mask = torch.ones_like(input_ids)
```

`model.generate()` 的 `input_ids` 仅含单个 BOS token，无任何上一代文本作为 prompt。

**2. 训练代码** (`scripts/lora_finetune.py`)

Docstring 声明：
> "每代从 base model 重新微调。"

训练流程：加载 base model → 全新 LoRA adapter → 在 depth N 文本上做标准 causal LM (next-token prediction) → 保存 adapter。训练数据就是上一轮生成的文本，但用于学习分布特征，不用于 generation-time conditioning。

**3. Pipeline 流程** (`scripts/run_pipeline.sh`)

```
depth_0 文本 → LoRA finetune → adapter_0 → 无条件生成 → depth_1 文本
depth_1 文本 → LoRA finetune → adapter_1 → 无条件生成 → depth_2 文本
...
```

每步 generation 都只以 BOS token 启动，不输入任何上一代文本。

### Rebuttal 可引用文本

> **Generation is strictly unconditional.** Each depth-N+1 corpus is produced by sampling from a BOS token alone — no depth-N passage is used as a prompt or prefix during generation (`input_ids = [[bos_token_id]]`, `generate_next_depth.py` L72). The `seed_id` field is an independent counter (0…4999) with no correspondence to any depth-N document. Consequently, **no passage-level lineage exists between depths**: the sole information channel from depth N to depth N+1 is the LoRA weight update obtained by fitting the depth-N distribution via standard next-token prediction (`lora_finetune.py`). This design is intentional — it ensures that any depth-distinguishing signal captured by our estimator reflects cumulative parametric degradation in the model, not surface-level textual inheritance.

---
