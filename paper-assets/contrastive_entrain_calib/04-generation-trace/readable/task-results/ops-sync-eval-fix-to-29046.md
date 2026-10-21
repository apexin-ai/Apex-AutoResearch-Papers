# ops sync eval fix to 29046

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sync-eval-fix-to-29046_20260519T093954_result.json`
- **Structured JSON:** [`a6b9d9fb3989199ba1fa.json`](../../sessions/a6/a6b9d9fb3989199ba1fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

发现情况与预期相反。两边 `generate_single_response` 的关键差异：

**28034（1838行）**：
```python
prompt_text = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True,
    enable_thinking=False,
)
...
return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
```
- `enable_thinking=False` 直接调用，无 try/except
- **无** regex 后处理

**29046（1845行）**：
```python
try:
    prompt_text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True,
        enable_thinking=False,
    )
except TypeError:
    prompt_text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True,
    )
...
text = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
text = re.sub(r'&lt;think>.*?&lt;/think>', '', text, flags=re.DOTALL).strip()
return text
```
- `enable_thinking=False` 有 try/except 兜底（兼容不支持该参数的 tokenizer）
- **有** regex 后处理（strip `&lt;think>` 标签）

**结论：29046 版本实际上更完善（多了 try/except 兼容 + regex 后处理）。28034 版本反而缺少 regex 后处理。**

你确定要用 28034 的版本覆盖 29046 吗？还是反过来，把 29046 的版本同步到 28034？

---
