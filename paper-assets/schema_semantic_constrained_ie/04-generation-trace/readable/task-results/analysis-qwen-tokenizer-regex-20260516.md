# analysis qwen tokenizer regex 20260516

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen_tokenizer_regex_20260516_20260516T115345_result.json`
- **Structured JSON:** [`64adea03fefc662cd28c.json`](../../sessions/64/64adea03fefc662cd28c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：**无影响** — Warning 是 transformers 4.57.6 的 false positive

### Warning 完整内容

```
The tokenizer you are loading from '/root/autodl-tmp/checkpoints/qwen_lora_docred_merged' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
```

### 根因分析

`transformers/tokenization_utils_base.py:2466-2483` 的版本检查逻辑有 gap：

- `transformers_version <= 4.57.2` → 进入 model_type 检查，非 Mistral 系列直接跳过（正确路径）
- `transformers_version >= 5.0.0` → 直接跳过
- **4.57.3 ~ 4.99.x 之间** → 落入 else，无条件设置 `mistral_config_detected = True`，触发 warning

模型 config.json 中 `transformers_version: 4.57.6`、`model_type: qwen3`，恰好命中这个 gap。**Llama 的 checkpoint 同样中招**，证明这是版本检查的 bug，不是 Qwen 特有问题。

### 对 Constrained Decoding 的影响：零

1. **XGrammar 不使用 pre-tokenizer regex**。它只读取 vocab（token→bytes 映射）来构建约束 mask。pre-tokenizer regex 只在 encode 新文本时用到，与 decode-time 的 token constraint 无关。

2. **实际验证通过**：
   - `xgr.TokenizerInfo.from_huggingface(tokenizer)` 成功，vocab_size=151669
   - JSON schema grammar 编译正常
   - Bitmask 生成正确（初始状态仅允许 5 个 token，即 `{` 及其变体）

3. **Qwen 的 pre-tokenizer regex 本身是正确的**（标准 tiktoken/GPT-4o pattern）。如果错误地设置 `fix_mistral_regex=True`，反而会把 Qwen 的正确 regex 替换成 Mistral 的 tekken regex，造成真正的问题。

4. **两个模型条件一致**：Qwen 和 Llama 都产生同一 warning，实验间结果可比性不受影响。

### 建议

无需修复。如果想消除 warning 噪音，可以在加载时显式传 `fix_mistral_regex=False`（明确告诉 transformers 不需要修正），或等待 transformers 下个版本修复此 bug。**绝对不要设置 `fix_mistral_regex=True`**。

---
