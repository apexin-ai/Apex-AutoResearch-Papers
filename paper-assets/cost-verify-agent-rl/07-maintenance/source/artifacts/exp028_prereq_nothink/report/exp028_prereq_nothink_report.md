## Qwen3-1.7B 零样本 eval (enable_thinking=False)

### 方法
- 修改 tokenizer_config.json chat_template，将 `enable_thinking` 条件从 `is defined and is false` 改为 `is not defined or is false`，使默认行为变为关闭 thinking
- 效果：模板在 `<|im_start|>assistant\n` 后预填充 `<think>\n\n</think>\n\n`（空 think block），抑制模型进入 thinking mode
- 其余设置与之前 prereq zeroshot 完全一致（16 episodes，val_only，140 games）

### 结果
| 指标 | thinking=True (之前) | thinking=False (本次) |
|------|---------------------|----------------------|
| success | 0% | 0% |
| action_is_valid | 0.75% | 0% |
| manager_invalid_action | ~99.25% | 100% |
| response_length | ~1024 (满) | 51.19 |
| episodes 跑满 50 步 | 100% | 100% |

### 样本输出 (thinking=False)
模板预填充的空 think block 后，模型仍然生成新的 `<think>` 块：
```
<think>

</think>

<think>[Assessment: neutral] I need to find a cool cup. The microwave is a likely location. [Suggestion: go to microwave 1]
```
- 模型在闭合的 `</think>` 之后没有输出 action 命令，而是开了一个新的 `<think>` 块
- 新 `<think>` 块没有闭合 `</think>`，action parser 无法提取有效 action
- 所有 episode 的 action 历史显示完全相同的模式，模型陷入循环

### 结论
**Thinking 模式不是根因。** 关闭 thinking 后表现反而略差（0.75% → 0% valid）。

根本问题是 Qwen3-1.7B 的 instruction-following 能力不足以处理 ALFWorld 的 action 格式要求：
1. thinking=True 时：模型生成长 think 内容但不输出有效的 action 命令
2. thinking=False 时：模型忽略空 think block 暗示，自行生成新的 think block，同样不输出 action

thinking 假设可以排除，0% success 的根因是模型能力本身。
