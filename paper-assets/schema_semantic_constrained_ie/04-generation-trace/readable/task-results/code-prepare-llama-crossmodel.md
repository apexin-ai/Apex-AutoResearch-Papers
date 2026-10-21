# code prepare llama crossmodel

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_llama_crossmodel_20260514T043051_result.json`
- **Structured JSON:** [`d1af206cf774292ecaff.json`](../../sessions/d1/d1af206cf774292ecaff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。以下是 Llama-3.1-8B cross-model 验证的兼容性报告。

---

## Llama-3.1-8B 兼容性评估

### 1. 模型加载 — ✅ 兼容
- `AutoModelForCausalLM` + `AutoTokenizer`，通用接口
- 默认路径硬编码为 Qwen3-8B（line 616-622），但 `--model_path` 参数可覆盖，**无需改代码**

### 2. Chat Template — ❌ 需要修改
**唯一的硬性不兼容点。** 三处 `apply_chat_template` 调用传了 Qwen3 特有参数：
- `run_constrained_extraction.py:416` — `enable_thinking=False`
- `run_constrained_extraction.py:464` — `enable_thinking=False`
- `run_constrained_extraction.py:505` — `enable_thinking=False`

Llama tokenizer 不识别 `enable_thinking`，会抛 `TypeError`。**修复方案**: 条件传参，检测 tokenizer 是否支持该参数。

### 3. Semantic Constraint (First-Token Masking) — ✅ 兼容（需验证）
- `ensure_first_token_map()` 和 `_build_first_token_map()` 动态从 tokenizer 计算，**无硬编码 token ID**
- `compile_type_constraints()` 有运行时碰撞检查（两个 entity type 共享 first token → ValueError）
- **风险点**: SciERC 的 Method/Material/Metric 和 DocRED 的 MISC 都以 M 开头，需确认 Llama tokenizer 不会产生 first-token 碰撞。大概率没问题（常见英文单词通常有独立 BPE token），但建议跑前先用脚本验证

### 4. XGrammar — ✅ 兼容
- `xgr.TokenizerInfo.from_huggingface(tokenizer, vocab_size=...)` 是通用 HF 接口
- Grammar 编译基于 JSON Schema，与 tokenizer 无关

### 5. 模型下载 — ✅ 已存在
- 路径: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct/`
- 大小: 15GB，4 个 safetensors shard + tokenizer 文件齐全
- HF 模型 ID: `meta-llama/Llama-3.1-8B-Instruct` ([HuggingFace](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct))

---

## 需要的代码修改

**仅 1 处改动**（3 个调用点）：`enable_thinking=False` 条件化

```python
# 方案: 构造 chat_template kwargs
chat_kwargs = dict(tokenize=False, add_generation_prompt=True)
if "enable_thinking" in inspect.signature(tokenizer.apply_chat_template).parameters:
    chat_kwargs["enable_thinking"] = False

text = tokenizer.apply_chat_template(msgs, **chat_kwargs)
```

或更简单：`try/except` 包一层。

## 建议的运行命令

```bash
cd /root/schema_semantic_constrained_ie

# SciERC full_s2 (与 Qwen3 实验对齐)
python run_constrained_extraction.py \
  --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct \
  --dataset scierc \
  --mode full_s2 \
  --output_path results/scierc_llama31_8b_full_s2.jsonl

# 其他 modes 对齐 Qwen 实验
python run_constrained_extraction.py \
  --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct \
  --dataset scierc \
  --mode unconstrained \
  --output_path results/scierc_llama31_8b_unconstrained.jsonl
```

## 预计准备时间

- 代码修改: ~10 分钟（`enable_thinking` 条件化 + first-token 碰撞验证脚本）
- 测试运行（几个 sample）: ~5 分钟
- 全量运行: 与 Qwen3 实验耗时相当

批准后可立即开始改代码。

---
