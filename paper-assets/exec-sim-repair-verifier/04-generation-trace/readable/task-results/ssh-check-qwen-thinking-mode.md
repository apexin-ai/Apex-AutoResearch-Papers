# ssh check qwen thinking mode

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-qwen-thinking-mode_20260521T143720_result.json`
- **Structured JSON:** [`18df8b37588385a1bf15.json`](../../sessions/18/18df8b37588385a1bf15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结果

### 1. `enable_thinking=False` 代码实现（eval_repo_cwm.py）

**正确实现，但不是根因。**

- **L53-58**: `get_chat_template_kwargs()` 正确检测 Qwen tokenizer 是否支持 `enable_thinking` 参数，返回 `{"enable_thinking": False}`。该 dict 传递给所有 `apply_chat_template()` 调用。
- **L128-129**: `parse_cwm_prediction()` 有 `&lt;/think>` 兜底 strip：
  ```python
  if "&lt;/think>" in text:
      text = text.split("&lt;/think>")[-1]
  ```
- **L235-240**: `model.generate()` 不传 `enable_thinking`（正确——这是 chat template 参数，不是 generate 参数）。

### 2. generation_config.json

Qwen3-8B base model 配置：
```json
{"do_sample": true, "temperature": 0.6, "top_k": 20, "top_p": 0.95}
```
**无任何 thinking 相关字段。** LoRA checkpoints 也没有自己的 `generation_config.json`。

### 3. 实际输出验证（s42 full test: 9784 样本）

| 指标 | 值 |
|------|-----|
| 总样本 | 9784 |
| unparseable | **6236 (63.7%)** |
| 含 `&lt;/think>` 标签的输出 | **仅 30 (0.3%)** |
| 空 gen_text | 0 |
| 输入截断 | 0 |
| gen_text 平均长度 | 149.8 tokens (median 125) |

### 4. `&lt;/think>` 泄露的具体样式

30 个含 `&lt;/think>` 的样本中，模型先生成一段 pytest 进度条输出（如 `[ 28%]`），然后在中间突然插入 `&lt;/think>`，之后输出 code diff 或另一段测试 trace。例如 (line 198):
```
...xarray/tests/test_indexes.py [ 39%\n&lt;/think>\n\n## Code\ndiff --git a/xarray/core/dataset.py ...
```
parser 的 strip 逻辑正确处理了这些（取 `&lt;/think>` 之后的内容），但剩余内容通常也不含 PASS/FAIL 判定词。

### 5. 根因判定

**Thinking mode 不是 53% unparseable 的根因。** `enable_thinking=False` 对 99.7% 的输出生效。

**真正的根因：模型生成冗长的 pytest 执行 trace（进度条 `[  1%]`、`[  3%]`…），在到达 PASS/FAIL 判定前就触发了 eos token 停止生成。** mean gen length 只有 149.8 tokens，模型在输出完整 test summary 之前就停了。这是 CWM 模型的输出质量问题，不是 thinking mode 问题。

### 6. 建议

- **不需要额外修改 thinking mode 配置**——当前实现已经正确
- unparseable 的真正修复方向：改进 `parse_cwm_prediction()` 的 keyword matching 逻辑（如从 progress bar 中的 `F` 提取 fail 信号），或增大 `max_new_tokens`，或调整训练数据让模型生成更简洁的输出

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "do_sample": true,
    "temperature": 0.6,
    "top_k": 20,
    "top_p": 0.95
  }
}
```

</details>

---
