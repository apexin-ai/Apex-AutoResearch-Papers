# analysis w7 qwen tokenizer regex

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w7_qwen_tokenizer_regex_20260516T063043_result.json`
- **Structured JSON:** [`ae517eaa012a5d3cd912.json`](../../sessions/ae/ae517eaa012a5d3cd912.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有调查完成。

---

## 报告：w7_qwen_scierc_ft_grammar_only tokenizer regex 警告

### 1. 完整警告文本

```
The tokenizer you are loading from '/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged'
with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e.
This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag
when loading this tokenizer to fix this issue.
```

### 2. Regex pattern 差异

**merged checkpoint 与原始 Qwen3-8B 的 tokenizer.json 完全一致**——pre_tokenizer、normalizer、vocab (151643)、merges (151387) 全部相同。

Regex pattern（两者相同）：
```
(?i:'s|'t|'re|'ve|'m|'ll|'d)|[^\r\n\p{L}\p{N}]?\p{L}+|\p{N}| ?[^\s\p{L}\p{N}]+[\r\n]*|\s*[\r\n]+|\s+(?!\S)|\s+
```

### 3. Tokenizer 输出一致性

| 测试字符串 | token 数 | 匹配 |
|---|---|---|
| `{"entities": [{"text": "BERT"...}]}` | 17 | MATCH |
| `{"relations": [{"head": "CNN"...}]}` | 24 | MATCH |
| OtherScientificTerm | 4 | MATCH |
| Evaluate-for | 2 | MATCH |
| Feature-of / Part-of / Hyponym-of | 2/2/4 | MATCH |
| `&lt;think>...\n&lt;/think>\n\n{"entities":...}` | 26 | MATCH |
| 含缩写的句子（It's, we've, they'll） | - | MATCH |

**All match: True**。vocab size 均为 151669。

### 4. fix_mistral_regex 适用性

- `fix_mistral_regex=True` 被接受，但**会把正确的 Qwen regex 替换成 Mistral regex**
- 碰巧对 IE 测试字符串输出一致，但 regex 完全不同（Mistral regex 无 contraction 分支、分大小写字母类别），存在边界 case 风险
- **不应使用**

### 5. 触发原因（transformers 4.57.6 bug）

源码 `tokenization_utils_base.py:2466`：

```python
if transformers_version and version.parse(transformers_version) <= version.parse("4.57.2"):
    if _is_local and model_type not in ["mistral", "mistral3", ...]:
        return tokenizer  # 正确跳过非 Mistral 模型
elif transformers_version and version.parse(transformers_version) >= version.parse("5.0.0"):
    return tokenizer  # 新版本直接跳过
# 4.57.3 ~ 4.57.x 的模型掉进间隙 → 误触发 warning
mistral_config_detected = True
```

merged checkpoint 的 config.json：`transformers_version: 4.57.6`、`model_type: qwen3`。4.57.6 落入 `(4.57.2, 5.0.0)` 间隙，model_type 检查被跳过。原始 Qwen3-8B 因路径不同（无 config.json 或版本不在范围内）未触发。

### 6. w5 系列情况

**w5 Qwen 和 w5 Llama 均有完全相同的警告**，结果已验证合理。

### 7. 结论：**无影响，无需重跑**

- tokenizer.json 字节级一致
- 所有 token IDs 完全匹配
- 警告是 transformers 4.57.6 的已知 false positive
- w5/w7 使用同一 tokenizer，DR 对比有效
- 实验分析中可注明：`"Warning is a false positive in transformers 4.57.6 (_maybe_fix_mistral_regex version gap bug); tokenizer files are identical to the original Qwen3-8B, verified by token ID comparison."`

---
