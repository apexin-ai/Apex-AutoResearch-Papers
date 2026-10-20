# evaluate.py 版本差异分析

## 文件版本信息

| 版本 | 文件 | Size | MD5 | 修改日期 |
|------|------|------|-----|----------|
| 原版 (reference) | `evaluate.py.bak_20260521` | 37591 bytes | `001a9bc23f808c47d25ef9eaeecb81f1` | 2026-05-21 14:18 |
| 当前版 | `evaluate.py` | 37978 bytes | `f02bf98b92cb23813ae2843252d3d9f0` | 2026-05-23 02:35 |

差异：+387 bytes，+2 行新增，4 行修改。无 git history（手动编辑）。

## 修改内容

### 修改 1：token_type_ids 剥离（`load_model_and_tokenizer`，新增 lines 101-102）

```python
# Strip token_type_ids to avoid ValueError on models that reject it (e.g. Falcon3)
tokenizer.model_input_names = [n for n in getattr(tokenizer, "model_input_names", []) if n != "token_type_ids"]
```

- **影响范围**：所有 benchmark（共享的模型加载函数）
- **对 Qwen2.5 的影响**：**无**。Qwen tokenizer 的 `model_input_names` 不含 `token_type_ids`，此行为 no-op
- **对 Falcon3 的影响**：修复 Falcon3 tokenizer 传入 `token_type_ids` 导致的 ValueError 崩溃

### 修改 2：system_prompt 添加（4 处，GSM8K / HumanEval / paraphrased 路径）

所有修改均为同一模式：`format_as_chat(tokenizer, ...)` → `format_as_chat(tokenizer, ..., system_prompt="You are a helpful assistant.")`

| 行号 (新) | 函数 | 代码路径 |
|-----------|------|----------|
| 323 | `evaluate_gsm8k` | instruct 模型的 CoT 生成 prompt |
| 379 | `evaluate_humaneval` | instruct 模型的代码生成 prompt |
| 556 | `evaluate_paraphrased` | paraphrased GSM8K 生成 prompt |
| 588 | `evaluate_paraphrased` | paraphrased HumanEval 生成 prompt |

- **影响范围**：GSM8K、HumanEval、paraphrased eval（仅 generation-based 路径）
- **对结果的影响**：添加 system message 会改变 prompt template，**可能影响 GSM8K/HumanEval 分数**

## 未修改的代码路径

| 函数 | 行号范围 | Benchmark | 状态 |
|------|---------|-----------|------|
| `evaluate_mcq` | 163-249 | **MMLU, ARC-Challenge** | **完全未变** |
| `compute_choice_logprobs` | 144-161 | MMLU/ARC logprob 计算 | 未变 |
| `format_mcq_example` | 250-269 | few-shot 格式化 | 未变 |
| `evaluate_paraphrased` MCQ 路径 | 507, 512 | paraphrased MMLU/ARC | 未变 |
| `main` | 706+ | 主流程 | 未变 |

`evaluate_mcq` 内部的 `format_as_chat` 调用在原版中已正确处理：
- 非 instruct 路径 (line 217)：`format_as_chat(tokenizer, raw_prompt_body) + mc_suffix` — 无 system_prompt（logprob 评估，正确）
- instruct/generation 路径 (line 225)：`format_as_chat(tokenizer, raw_prompt, system_prompt=sys_msg)` — 原版已有 system_prompt

## 结论

1. **MMLU 和 ARC eval 逻辑完全未变**。`evaluate_mcq` 函数零修改。
2. 修改**不仅限于** token_type_ids。还包含 GSM8K/HumanEval/paraphrased 路径的 system_prompt 添加。
3. token_type_ids 修复对 Qwen2.5 系列模型是 no-op，仅影响 Falcon3。
4. system_prompt 修改影响 GSM8K 和 HumanEval 的 instruct 评估结果，需注意跨版本数据一致性（C009/C010）。

## C009 更新建议

新 reference md5：`f02bf98b92cb23813ae2843252d3d9f0`（37978 bytes）

由于此版本包含 system_prompt 变更（影响 GSM8K/HumanEval），切换 reference 后：
- 已有的 MMLU/ARC 数据与新版兼容（逻辑未变）
- 已有的 GSM8K/HumanEval 数据需确认是否需要用新版重跑
