# Qwen3 SciERC Training: Thinking Tokens Confirmation

## 1. enable_thinking 配置状态

| 训练配置 | 文件 | enable_thinking 设置 | 实际生效值 |
|----------|------|---------------------|-----------|
| ft_001 (SciERC) | `train_config.yaml` | **未设置** | `True` (默认值) |
| ft_002 (SciERC) | `train_config_v2.yaml` | **未设置** | `True` (默认值) |
| ft_002_v2 (SciERC) | `train_config_v2.yaml` | **未设置** | `True` (默认值) |
| CoNLL-2003 | `train_config_conll2003.yaml` | `false` | `False` |
| WNUT-17 | `train_config_wnut17.yaml` | `false` | `False` |

**LLaMA Factory 0.9.4 默认值**: `data_args.enable_thinking` 定义在 `llamafactory/hparams/data_args.py:122`，默认 `True`。SciERC 训练配置未覆盖此参数，因此使用默认值 `True`。

## 2. 训练日志中的 thinking token 证据

所有三次 SciERC 训练日志均包含：

```
[WARNING] llamafactory.data.template:148 >> You are using reasoning template,
please add `_nothink` suffix if the model is not a reasoning model. e.g., qwen3_vl_nothink
<think>
</think>
<think>
</think>
...
```

| 日志文件 | 时间戳 | 包含 `<think>` |
|----------|--------|----------------|
| `ft_001_train.log` | 2026-05-14 14:09:15 | Yes |
| `ft_002_train.log` | 2026-05-14 15:43:17 | Yes |
| `ft_002v2_train.log` | 2026-05-14 16:10:02 | Yes |

## 3. LLaMA Factory enable_thinking 机制 (template.py)

当 `enable_thinking=True` 且训练数据不含 `<think>`/`</think>` 时（正是 SciERC 的情况），LLaMA Factory 的行为（`template.py:424-431`）：

```python
if (
    self.thought_words[0].strip() not in messages[-1]["content"]
    and self.thought_words[1].strip() not in messages[-1]["content"]
):  # add empty cot
    if not self.enable_thinking:  # do not compute loss
        prompt_ids += self.get_thought_word_ids(tokenizer)
    else:  # do compute loss
        response_ids = self.get_thought_word_ids(tokenizer) + response_ids
```

- **`enable_thinking=True`（SciERC）**: 空 `<think>\n</think>\n\n` 被 **prepend 到 response_ids**，纳入 loss 计算。模型被训练在每个 JSON 响应前先输出空 thinking block。
- **`enable_thinking=False`（CoNLL/WNUT）**: 空 `<think>\n</think>` 被 append 到 prompt_ids，**不参与 loss 计算**。

## 4. 结论

**Thinking tokens 在 SciERC 训练时实际被激活。**

具体表现：
- 每个训练样本的 response 前被自动注入空 thinking block `<think>\n</think>\n\n`
- 这些 token 被纳入 loss 计算，模型学会在输出 JSON 前先产生空 thinking block
- 但 thinking block 始终为空（训练数据不含任何推理链），不存在实际的 chain-of-thought 内容

**推理时的处理**：
- `apply_chat_template(enable_thinking=False)` + XGrammar JSON constrained decoding 确保推理输出不含任何 thinking tokens
- 这构成了一个 train-test distribution mismatch：训练时模型预期输出 `<think>\n</think>` → JSON，推理时直接输出 JSON

**影响评估**：
- 空 thinking block 仅含 4-5 个 token（`<think>`, `\n`, `</think>`, `\n\n`），在 2048 cutoff_len 中占比极小
- 不存在推理链泄漏（thinking block 始终为空）
- 主要影响：模型的 token 分布被轻微偏移（学会先输出 thinking 标记再输出 JSON），推理时跳过这些 token 可能对首 token 概率分布有微弱影响
- CoNLL-2003 和 WNUT-17 不受影响（已显式设置 `enable_thinking: false`）
