# padding_side 检查报告

**检查日期**: 2026-05-19  
**检查文件**: `iterative_train.py` (westd-17855 & westd-19828)

---

## 1. padding_side 当前设置

**未设置。** `iterative_train.py` 中没有任何 `tokenizer.padding_side = 'left'` 的代码。

Tokenizer 初始化（约 L226）仅设置了 `pad_token`：
```python
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
```

GPT-NeoX/Pythia tokenizer 默认 `padding_side='right'`。

## 2. generation batch_size 设置

- `--gen_batch_size` 默认值：**16**
- 6.9B 实验实际使用：**16**（`config.json` 确认）
- 小模型实验（alpha_sweep）实际使用：**16**（`config.json` 确认）

## 3. 问题确认：right-padding + batch_size>1

**存在问题。** `generate_synthetic_data()` 函数（L94-122）：

```python
enc = tokenizer(batch_prompts, return_tensors="pt", truncation=True,
                max_length=args.max_length // 2, padding=True)  # 默认 right-padding
```

- `padding=True` 使用默认 `padding_side='right'`
- `gen_batch_size=16`，batch 内 prompt 长度不一，必然触发 padding
- 虽然 `attention_mask` 正确传入 `model.generate()`，但 right-padding 下 decoder-only 模型的 position embedding 和 KV cache 处理不正确

**training 阶段不受影响**：`tokenize_dataset()` 使用 `padding="max_length"`，配合 `DataCollatorForLanguageModeling` 做 causal LM，right-padding 在训练时无问题（attention mask 正确屏蔽）。

**metrics.py 不受影响**：只做 forward pass 计算 perplexity/entropy 等指标，不调用 `generate()`。

## 4. 日志 padding 警告

| 实验 | 服务器 | 警告次数 |
|------|--------|----------|
| scale_69b_a100_s42 | westd-17855 | **3130** |
| alpha_sweep_a050_s42 | westd-19828 | **3443** |

警告内容（每个 batch 的每次 `generate()` 调用触发一次）：
```
[transformers] A decoder-only architecture is being used, but right-padding was detected! 
For correct generation results, please set `padding_side='left'` when initializing the tokenizer.
```

**所有实验（6.9B 和全部小模型）均受影响。**

## 5. 影响评估与建议

### 影响程度

- **系统性偏差**：right-padding 导致 batch 中较短 prompt 的 generation 质量下降（position embedding 错位）
- **一致性**：所有 alpha 值、所有 seed、所有模型规模均使用相同错误配置，因此**相对比较（alpha 间、seed 间、model 间）仍然有效**
- **绝对质量**：每代 synthetic data 质量均低于正确配置下的水平，可能导致 collapse 速度偏快（噪声累积效应）

### 修复建议

在 `main()` 中 tokenizer 初始化后、`generate_synthetic_data()` 调用前添加：

```python
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = 'left'  # 添加此行
```

**注意**：training 阶段需要 right-padding，所以需要在 generation 和 training 之间切换 padding_side，或者在 `generate_synthetic_data()` 函数内临时切换：

```python
def generate_synthetic_data(model, tokenizer, prompts_dataset, args):
    model.eval()
    device = next(model.parameters()).device
    generated_texts = []
    
    original_padding_side = tokenizer.padding_side
    tokenizer.padding_side = 'left'  # generation 需要 left-padding
    
    # ... generation code ...
    
    tokenizer.padding_side = original_padding_side  # 恢复
    return Dataset.from_dict({"text": generated_texts})
```

### 是否需要重跑实验

**不建议重跑已完成实验**。理由：
1. 所有实验一致受影响，相对比较有效
2. 论文核心 claim 是 collapse 趋势和 canary metric 的预测能力，这些是相对信号
3. 重跑成本极高（6.9B 实验尤其）

**建议**：修复后在一个代表性配置（如 pythia-410m, α=1.0, seed=42）上重跑，对比修复前后 metrics 差异，在论文 appendix 中报告此 robustness check。
