# TRL 1.1.0 GRPOTrainer Prompt 长度处理分析

## TRL 版本

**1.1.0**（已在服务器验证）

## GRPOConfig 中所有长度相关参数

| 参数 | 默认值 | 作用 |
|------|--------|------|
| `max_completion_length` | 256 | 生成的 completion 最大 token 数（仅控制 completion，不控制 prompt） |
| `vllm_max_model_length` | None（从模型 config 推断） | vLLM 的 context window 大小，建议设为 max_prompt_length + max_completion_length |
| `mask_truncated_completions` | False | 是否将被截断的 completion 从 loss 中排除 |

**`max_prompt_length` 参数不存在。** GRPOConfig 和 GRPOTrainer 中均无此参数。

## Prompt Tokenization 流程

源码位置：`grpo_trainer.py:1262` `_tokenize_prompts()` 方法。

### Conversational 格式
```python
tokenized = self.processing_class.apply_chat_template(
    conversation=prompts,
    tools=self.tools or None,
    chat_template=self.chat_template,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    **self.chat_template_kwargs,
)
prompt_ids = tokenized["input_ids"]
```

### 非 Conversational 格式
```python
prompt_ids = self.processing_class(text=prompts)["input_ids"]
```

**两种路径都没有传 `truncation=True` 或 `max_length` 参数。** Prompt 以原始长度完整保留。

虽然 tokenizer 初始化时设置了 `truncation_side="left"`（line 317），但这只是设置了默认截断方向，并不会自动启用截断——需要在调用 tokenizer 时显式传 `truncation=True` 才会生效。

## Generation 时的长度限制

### vLLM 路径
```python
sampling_params = {"max_tokens": max_completion_length, ...}
```
- `max_tokens` 仅限制生成的 completion token 数
- 如果 prompt_length + max_completion_length > vllm_max_model_length，vLLM 会**报错**

### Regular (transformers) 路径
```python
generation_kwargs = {"max_new_tokens": self.max_completion_length, ...}
unwrapped_model.generate(**generate_inputs, generation_config=self.generation_config)
```
- `max_new_tokens` 仅限制新生成的 token 数
- 如果 prompt 超过模型的 positional encoding 范围，行为未定义（可能 silent failure）

## Completion 截断（存在，但仅用于 completion）

- `_truncate_at_image_boundary()`（line 1496）：截断 completion 到 `max_completion_length`，同时避免切断图像 token 序列
- `is_truncated` 检测（line 1875）：通过检查 completion 最后一个 token 是否为 EOS 来判断是否被截断
- `mask_truncated_completions`：将截断的 completion 排除出 loss 计算

这些都只作用于 **completion 端**，与 prompt 无关。

## 结论

**TRL 1.1.0 GRPOTrainer 没有内置 prompt 截断机制。**

- 不存在 `max_prompt_length` 参数
- `_tokenize_prompts()` 不做任何 prompt 截断
- `max_completion_length` 仅控制 completion 长度
- 唯一的间接约束是 `vllm_max_model_length`（vLLM 的 context window），但它不会截断 prompt，而是在 prompt 过长时直接报错

## 建议

**需要在 data_utils.py 中手动加 prompt 截断。** 否则过长的 prompt 会导致：

1. **vLLM 模式**：直接报错退出训练（prompt + max_completion_length > max_model_length）
2. **Transformers 模式**：超出模型 context window 时行为不可预测，可能静默产生垃圾输出

建议在数据预处理阶段对 prompt 做左截断（left truncation），截断长度设为 `model_max_length - max_completion_length`，确保 prompt + completion 不超过模型上限。TRL 已设置 `truncation_side="left"`，可直接利用：

```python
max_prompt_length = model_max_length - max_completion_length
tokenized = tokenizer(text, truncation=True, max_length=max_prompt_length)
```
