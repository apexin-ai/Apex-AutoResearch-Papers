# 第三模型兼容性调研报告

**日期:** 2026-05-16
**目标:** 评估 Mistral-7B-Instruct-v0.3 和 Gemma-2-9B-it 与 OntoCoDec pipeline 的兼容性

---

## 1. 模型对比总表

| 维度 | Mistral-7B-Instruct-v0.3 | Gemma-2-9B-it |
|------|--------------------------|---------------|
| **Model ID** | `mistralai/Mistral-7B-Instruct-v0.3` | `google/gemma-2-9b-it` |
| **参数量** | 7.25B | 9B |
| **磁盘占用 (BF16)** | ~14.5 GB | ~18.5 GB |
| **License** | Apache 2.0 | Gemma License (需接受协议) |
| **Max Context** | 32,768 tokens | 8,192 tokens |
| **Vocab Size** | 32,768 | 256,128 |
| **Tokenizer** | SentencePiece BPE (LlamaTokenizerFast) | SentencePiece BPE |
| **Attention** | GQA (32 heads / 8 KV heads) | GQA (16 heads / 8 KV heads) + sliding window |
| **量化版本** | GGUF / AWQ / GPTQ 均有 | GGUF / AWQ / GPTQ 均有 |
| **Min transformers** | ≥ 4.42.0 | ≥ 4.42.3 |
| **System Role** | ✅ 支持 | ❌ 不支持 (需嵌入 user message) |
| **XGrammar 兼容** | ✅ 无已知问题 | ⚠️ 有重复循环风险 |

---

## 2. Chat Template 对比

### 现有模型

**Qwen3-8B:**
```
<|im_start|>system\n{system}<|im_end|>\n<|im_start|>user\n{user}<|im_end|>\n<|im_start|>assistant\n
```
- 特殊参数: `enable_thinking=False` 禁用扩展思考

**Llama-3.1-8B-Instruct:**
```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n{system}<|eot_id|><|start_header_id|>user<|end_header_id|>\n{user}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n
```

### 候选模型

**Mistral-7B-Instruct-v0.3:**
```
<s>[INST] {system}\n\n{user} [/INST]
```
- system message 嵌入第一个 `[INST]` 块内
- 通过 `tokenizer.apply_chat_template()` 自动处理

**Gemma-2-9B-it:**
```
<bos><start_of_turn>user\n{user}<end_of_turn>\n<start_of_turn>model\n
```
- **不支持 system role**，system prompt 需手动拼入 user message
- role 用 `model` 而非 `assistant`（但 apply_chat_template 会自动映射）

### OntoCoDec 适配分析

当前代码使用 `tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)` 统一处理。

- **Mistral:** 直接兼容，`messages = [{"role": "system", ...}, {"role": "user", ...}]` 无需改动
- **Gemma:** 需要在构建 messages 前将 system content 合并到 user message 中，因为 Gemma 不接受 system role。需改动 prompt 构建逻辑。

---

## 3. Tokenizer 与 XGrammar 兼容性

### XGrammar 集成点

OntoCoDec 的 XGrammar 调用方式:
```python
tokenizer_info = xgr.TokenizerInfo.from_huggingface(tokenizer, vocab_size=tokenizer.vocab_size)
compiler = xgr.GrammarCompiler(tokenizer_info)
```

此接口接受任何 HuggingFace tokenizer，两个模型均可通过。

### TypeConstraintProcessor 兼容性

关键逻辑: `compile_type_constraints()` 依赖 entity type 的 first token ID 唯一性。

| 模型 | Vocab Size | First-Token 冲突风险 |
|------|-----------|---------------------|
| Qwen3-8B | 151,936 | 已验证无冲突 |
| Mistral-7B | 32,768 | **需验证** — 小 vocab 更易冲突 |
| Gemma-2-9B | 256,128 | 冲突风险低（大 vocab） |

**Mistral 的 32K vocab 是主要风险点。** DocRED 的 6 种 entity type (PER/ORG/LOC/TIME/NUM/MISC) 大概率无冲突，但 SciERC 的 type 名称更长更复杂，需要实际验证。

### 其他 Tokenizer 注意事项

- **Mistral:** 需安装 `sentencepiece` 包，否则 tokenizer 加载失败
- **Gemma:** vocab 256K 会导致 XGrammar FSM 索引构建较慢（vs Mistral 的 32K），但不影响功能

---

## 4. 已知问题与风险

### Mistral-7B-Instruct-v0.3

| 风险 | 严重度 | 应对 |
|------|--------|------|
| tokenizer.model 曾被误删 | 低 | 指定 revision 或清理缓存 |
| HF tokenizer 与 mistral_common 有微小差异 | 低 | IE 任务影响可忽略 |
| 需要 sentencepiece 依赖 | 低 | `pip install sentencepiece` |

**总体: 低风险，标准 MistralForCausalLM 架构，生态成熟。**

### Gemma-2-9B-it

| 风险 | 严重度 | 应对 |
|------|--------|------|
| flash_attention_2 输出错误 | **高** | 必须用 `attn_implementation="eager"` |
| Constrained decoding 重复循环 | **中** | 需设 `repetition_penalty=1.1` |
| 不支持 system role | 中 | 需修改 prompt 构建代码 |
| 微调时 NaN/loss=0 | 中 | 当前仅做推理，不影响 |
| 8K max context (vs Mistral 32K) | 中 | DocRED 长文档可能截断 |
| Logit soft-capping 改变分布 | 低 | 需测试对 constrained decoding 的影响 |

**总体: 中高风险，需要多处适配。**

---

## 5. OntoCoDec 适配工作量估算

### Mistral-7B-Instruct-v0.3 — 约 10-15 行改动

1. **模型路径配置** (~3 行): 添加 Mistral 候选路径到 auto-detect 逻辑
2. **移除 Qwen3 特有参数** (~2 行): 去掉 `enable_thinking=False`（条件化已有逻辑或按模型分支）
3. **安装 sentencepiece** (~1 行): requirements.txt 加依赖
4. **验证 first-token 唯一性** (~0 行代码改动): 现有 `compile_type_constraints()` 会自动检查并报错

**无需重构，纯增量改动。**

### Gemma-2-9B-it — 约 30-50 行改动

1. **模型路径配置** (~3 行): 同上
2. **Attention 实现** (~3 行): 加载时指定 `attn_implementation="eager"`
3. **System prompt 合并** (~10-15 行): 对 Gemma 模型将 system message 拼入 user message
4. **Generation 参数** (~5 行): 对 Gemma 添加 `repetition_penalty=1.1`
5. **Context 长度处理** (~10 行): 添加文档截断逻辑 (8K limit)
6. **移除 Qwen3 特有参数** (~2 行): 同上
7. **测试 soft-capping 与 TypeConstraintProcessor 交互** (不确定工作量)

**需要修改 prompt 构建和生成参数，但不需要重构核心 constraint 架构。**

---

## 6. 推荐

### 推荐 Mistral-7B-Instruct-v0.3 作为第三模型

**理由:**

1. **适配成本最低:** ~10 行改动 vs Gemma 的 ~40 行，且全是增量修改
2. **XGrammar 兼容性好:** 无 soft-capping 干扰，无重复循环风险，32K 小 vocab 使 FSM 构建更快
3. **长上下文:** 32K context 覆盖 DocRED 所有文档长度，无需截断
4. **License 最宽松:** Apache 2.0，无需接受协议
5. **架构简洁:** 标准 MistralForCausalLM，无 sliding window / logit capping 等特殊机制
6. **与现有模型形成互补:** Qwen3-8B (中国)、Llama-3.1-8B (Meta)、Mistral-7B (欧洲) 覆盖三大模型系列，7B 参数量提供不同规模的对比点

**Gemma-2-9B-it 作为备选:**
- 优势是 9B 参数量与 Qwen3-8B 更接近，且知识蒸馏训练可能带来更好的 IE 性能
- 但 `attn_implementation="eager"` 会显著降低推理速度，soft-capping + constrained decoding 的交互是未知风险
