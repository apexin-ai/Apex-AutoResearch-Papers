# research scope expansion code check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_scope-expansion-code-check_20260516T024436_result.json`
- **Structured JSON:** [`bb4c5a0c4e3abc81a6ea.json`](../../sessions/bb/bb4c5a0c4e3abc81a6ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完成，汇报如下：

---

## 检查结果

### 1. Sparsity 参数：✅ 纯 CLI 参数，改值即可

| 脚本 | 参数名 | 默认值 | 位置 |
|------|--------|--------|------|
| `prune.py` | `--sparsity` (float) | 0.35 | L165 |
| `run_unstructured_baseline.py` | `--sparsity` (float) | 0.20 | L93 |

改 `--sparsity 0.25` 或 `--sparsity 0.30` 即可，无需改代码。sparsity 通过 `original_params * args.sparsity` 计算目标裁剪量，统一排序后贪心裁剪，逻辑完全参数化。

### 2. SFT 脚本：✅ Model-agnostic

两个 SFT 脚本（`train_sft_warmup.py`, `sft_recovery.py`）均：
- 通过 `--model_path` 传入模型路径（required 参数）
- 用 `AutoTokenizer.from_pretrained` + `load_pruned_model` 加载，无硬编码
- `sft_recovery.py` 用 `tokenizer.apply_chat_template()` 构建训练数据，自动适配模型自带 template
- `train_sft_warmup.py` 用 generic chat message 格式（`messages=[{role, content}]`）

换模型只需改 `--model_path`。

### 3. GRPO 脚本：✅ Model-agnostic

`train_grpo.py`：
- `--model_path` 传入，`AutoTokenizer` + `load_pruned_model` 加载
- **无 "Qwen" 字符串**（grep 0 匹配）
- **无 `apply_chat_template` 调用** — prompt 是纯文本构建（L164-170: `"Solve the following math problem step by step. Put your final answer in \boxed{}.\n\nQuestion: ..."`）
- reward 函数用正则提取 `\boxed{}`/`####`/最后数字，完全模型无关

换模型只需改 `--model_path`。

### 4. Qwen2.5 特定 Hardcode：⚠️ 仅注释级别

| 文件 | 位置 | 内容 | 影响 |
|------|------|------|------|
| `prune.py` | L2 docstring | "Qwen2.5 architecture" | 仅注释，不影响运行 |
| `prune.py` | L160 argparse description | "Qwen2.5 model" | 仅 help 文本 |

实际剪枝逻辑基于通用 config 属性（`num_attention_heads`, `num_key_value_heads`, `hidden_size`, `intermediate_size`），GQA-group 裁剪 + SwiGLU MLP 裁剪对所有同架构模型通用。`model_utils.py` 完全 generic。

### 5. 第二模型推荐：**Qwen2.5-Math-7B**

| 候选 | 架构兼容 | 代码改动 | 实验意义 | 风险 |
|------|---------|---------|---------|------|
| **Qwen2.5-Math-7B** | ✅ 同 Qwen2.5 架构，GQA/MLP 完全一致 | 零改动 | 数学专长模型做 GSM8K 更有说服力（reviewer 角度） | 无 |
| DeepSeek-R1-Distill-Qwen-1.5B | ⚠️ Qwen2 架构兼容，但 1.5B | 需处理 `&lt;think>` reasoning tokens、可能需调 GRPO prompt | 1.5B 模型 20-30% 剪枝可能过于激进，reward desert 风险高 | 中高 |

**结论**：Qwen2.5-Math-7B 零代码改动，只需在各脚本的 `--model_path` 指向新模型路径。

---
