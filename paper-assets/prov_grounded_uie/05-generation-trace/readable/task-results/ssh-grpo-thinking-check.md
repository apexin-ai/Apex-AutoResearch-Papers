# ssh grpo thinking check

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_grpo-thinking-check_20260512T223648_result.json`
- **Structured JSON:** [`737218169240bbb348b3.json`](../../sessions/73/737218169240bbb348b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有文件已修复。下面是完整报告：

---

## 排查报告

### 1. 上次 GRPO test 的 completion 文本
两个 GRPO test 的输出目录（`/tmp/grpo_test/`, `/tmp/grpo_test_v2/`）只保存了 auto-generated model card 和 trainer_state，**没有保存 completion 文本**。但有完整的训练日志：
- `/tmp/grpo_test.log` — max_completion_length=128
- `/tmp/grpo_test_v2_1024.log` — max_completion_length=1024

### 2. 单样本 generation 输出
```
&lt;think>

&lt;/think>

{"relations": [{"head": "Piraeus", "tail": "Greece", "relation": "country", ...}]}
```
生成了有效 JSON，458 tokens 后正常终止。

### 3. `&lt;think>` 标签
**是的，模型输出包含 `&lt;think>\n\n&lt;/think>` 标签**，但 thinking 内容为空（仅换行符），不消耗有效 tokens。`&lt;think>`(id=151667) 和 `&lt;/think>`(id=151668) 是词汇表中的 token，但 `skip_special_tokens=True` 不会剥离它们。

### 4. Qwen3 tokenizer `enable_thinking=False`
tokenizer 支持 `enable_thinking=False`，但效果是在 prompt 模板中插入 `&lt;think>\n\n&lt;/think>\n\n` 作为 generation prompt 的一部分，让模型跳过 thinking 直接输出。

### 5. TRL GRPOTrainer 配置
TRL 通过 `chat_template_kwargs` 传递给 `apply_chat_template`，设置 `{"enable_thinking": False}` 即可。

### 6. 结论：reward 全零的根本原因

**不是 thinking mode 导致的。** 根本原因是 **TRL GRPOConfig 的采样参数默认值与 Qwen3 不兼容**：

| 参数 | Qwen3 模型默认 | TRL GRPOConfig 默认 | 影响 |
|------|---------------|-------------------|------|
| `top_k` | 20 | **0（禁用）** | 无 top-k 过滤，全词表采样 |
| `top_p` | 0.95 | 1.0 | 无 nucleus 过滤 |
| `temperature` | 0.6 | 1.0（我们设了 0.7） | 略高 |

`train_grpo.py` 没有传递 `top_k` 和 `top_p` 给 GRPOConfig，导致 TRL 使用默认值 `top_k=0`（完全禁用 top-k 过滤）。

**因果链**：`top_k=0` → 全词表无约束采样 → 模型无法可靠生成 EOS → 所有 completion 截断在 max_completion_length → 截断的 JSON 无法解析 → reward=0 → train_loss=0

**实验验证**：
- `top_k=0, top_p=1.0`: 生成 1024 tokens 不终止 ✗
- `top_k=20, top_p=0.95`: 生成 228 tokens 正常终止 ✓
- 使用 kwargs（继承模型配置）: 生成 490 tokens 正常终止 ✓

### 7. 修复方案（已应用到服务器）

**config.py**: 新增 `top_k=20`, `top_p=0.95` 到 GRPOArgs

**train_grpo.py**: 
- 传递 `top_k` 和 `top_p` 给 GRPOConfig
- 添加 `chat_template_kwargs={"enable_thinking": False}` 禁用 thinking mode

**rewards.py**: `parse_json_output` 增加 `&lt;think>` 标签剥离作为 fallback safety

---
