# code verify truncation fix

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-truncation-fix_20260515T192729_result.json`
- **Structured JSON:** [`ebb856102766a29f6fec.json`](../../sessions/eb/ebb856102766a29f6fec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。汇报如下：

---

## 1. `to_chat_text()` 截断逻辑（定义在 `train/train_sft.py`）

```
overhead_msg = chat_template(empty_user + label)   # 构造只含模板标记+label的消息
overhead_len = tokenize(overhead_msg)               # 计算模板+label占用的token数
budget = max(0, 2048 - overhead_len)                # 剩余token预算全给input
content_ids = tokenize(input)[:budget]              # 截断input到预算内
truncated_input = decode(content_ids)               # 解码回文本
最终文本 = chat_template(truncated_input + label)    # 组装：截断后的input + 完整label
```

核心思路：先算 label + 模板开销，剩余 budget 分配给 input（trace），只截 input 不截 label。

## 2. Label-preserving 满足情况：**是**

实测验证（DeepSeek tokenizer, full_trace 训练集）：
- 原始 input 2783 tokens → 截断后总序列恰好 **2048 tokens**
- 末尾保留了 `pass\n<|EOT|>`，label 未丢失
- `label in text[-30:]` = **True**

## 3. `train_sft.py` DeepSeek 相关配置

| 配置项 | 值 |
|--------|-----|
| `max_length` | **2048** |
| `load_best_model_at_end` | **TEMP_DISABLED**（已注释） |
| `save_total_limit` | **TEMP_DISABLED**（已注释） |
| `metric_for_best_model` | **TEMP_DISABLED**（已注释） |
| DeepSeek 模型路径 | 通过 `--model_path` 传入，无硬编码 |

## 4. 结论

**D023 阻塞令可解除。** `to_chat_text()` 的 label-preserving truncation 修复已就绪，逻辑正确，实测通过。DeepSeek v3 实验可以提交。

---
