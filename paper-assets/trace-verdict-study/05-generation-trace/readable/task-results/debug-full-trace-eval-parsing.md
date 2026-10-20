# debug full trace eval parsing

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_full-trace-eval-parsing_20260515T011243_result.json`
- **Structured JSON:** [`486ac010db1819dd7de9.json`](../../sessions/48/486ac010db1819dd7de9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确诊完成。

## 诊断结论

### 1. Eval verdict extraction 逻辑
- 函数：`evaluate.py:classify_prediction()` (第49行)
- 提取方式：`max_new_tokens=1` → 检查输出是否包含 "pass"/"fail"
- **三条件使用完全相同的 eval 路径**，eval 脚本本身无 bug

### 2. 训练数据格式对比
三条件的 output 格式完全一致，都是单 token `"pass"` (token 6385) 或 `"fail"` (token 18403)。

### 3. 根因：token 计数 mismatch 导致训练标签被截断

**`format_training_data.py` 用 raw token 计数（无 chat template）做截断预算：**
```python
MAX_SEQ_LENGTH = 2048
full_tokens = tokenizer.encode(full_input + label, add_special_tokens=False)  # 不含 chat template
```

**`train_sft.py` 用 chat template 包装后再按 `max_length=2048` 截断：**
```python
# to_chat_text() 添加了 system prompt + role markers
# Qwen chat template 自带 system prompt "You are Qwen..."
# 实测 overhead = 31 tokens
```

**结果：** 数据格式化将 trace 截断到 raw ≤ 2048 tokens。训练时 chat template 加了 31 tokens → 实际 2079 tokens → 超过 `max_length=2048` → TRL 从右侧截断 31 tokens → **output label "pass"/"fail" 被完全切掉**。

### 4. 关键数据

| 条件 | pass 样本超 2048 (chat-wrapped) | fail 样本超 2048 | 影响 |
|------|------|------|------|
| no_trace | 0% | 0% | 正常 |
| vota | 89.4% (10.6% 保留) | 79.4% | 仍有 ~360 条 pass 标签可学 → 99.16% |
| **full_trace** | **100%** | 79.4% | **0 条 pass 标签** → 只学到 "fail" → 28.4% |

验证：full_trace 训练集 3107 条 pass 样本，**0 条**在 chat-wrapped 后 ≤ 2048 tokens。模型在训练中从未见过 "pass" 标签。

### 5. 修复方案

**方案 A（快速修复）：** `train_sft.py` 中 `max_length` 从 2048 改为 2080：
```python
max_length=2080,  # 2048 + chat template overhead (31 tokens)
```

**方案 B（根本修复）：** `format_training_data.py` 的 `_truncate_trace` 中，token 预算需减去 chat template overhead：
```python
MAX_SEQ_LENGTH = 2048
CHAT_TEMPLATE_OVERHEAD = 32  # 含 system prompt + role markers
EFFECTIVE_BUDGET = MAX_SEQ_LENGTH - CHAT_TEMPLATE_OVERHEAD  # 2016
```

**推荐同时做 A + B**，然后重新格式化数据 + 重训 full_trace。

预期修复后 full_trace accuracy 应 ≥ vota (99%)，因为 full_trace 包含更多信息。

---
