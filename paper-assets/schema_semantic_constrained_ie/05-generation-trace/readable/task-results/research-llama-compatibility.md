# research llama compatibility

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_llama-compatibility_20260514T073500_result.json`
- **Structured JSON:** [`9ea6aa549f6556f26131.json`](../../sessions/9e/9ea6aa549f6556f26131.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Llama-3.1-8B 兼容性报告

### 结论：开箱即用，零代码修改

只需传 `--model_path` 指向 Llama 路径即可。

---

### 逐项检查结果

**1. 模型加载 ✅**
- `--model_path` 是 CLI 参数，不是硬编码。默认值 fallback 到 Qwen 路径，但传参即覆盖
- 使用 `AutoTokenizer` + `AutoModelForCausalLM`，模型无关

**2. Prompt 模板 ✅**
- 全部通过 `tokenizer.apply_chat_template()` 构造，自动适配模型格式
- Qwen 特有逻辑仅在 `_chat_template_kwargs()` 中：检测到 `'qwen' in name` 时传 `enable_thinking=False`，非 Qwen 模型返回空 dict，不影响

**3. Constrained Decoding ✅**

| 组件 | 兼容性 | 原因 |
|------|--------|------|
| XGrammar | ✅ | `xgr.TokenizerInfo.from_huggingface()` 是 tokenizer 无关的 |
| TypeConstraintProcessor (first-token masking) | ✅ | 已验证 Llama-3.1-8B tokenizer 对所有 entity type 名称的 first token 唯一 |

Llama-3.1-8B first-token 验证结果：
```
SciERC:  Task=6396, Method=3607, Material=13721, Metric=55410, OtherScientificTerm=11663, Generic=20560  — 全部唯一 ✅
DocRED:  PER=9851, ORG=46027, LOC=12321, TIME=18621, NUM=17946, MISC=44  — 全部唯一 ✅
```

**4. pad_token ✅**
- Llama `pad_token=None`，代码已处理：`if tokenizer.pad_token is None: tokenizer.pad_token = tokenizer.eos_token`

**5. 配置文件 ✅**
- `ontology_constraints.json` 定义的是 schema 约束（entity types, relation types, valid pairs），与模型无关

---

### 推理命令模板

Llama-3.1-8B-Instruct 已在服务器上：`/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`

```bash
# SciERC — 5种模式任选
MODEL=/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct

python3 run_constrained_extraction.py \
  --mode full_s1 \
  --dataset scierc \
  --model_path $MODEL \
  --data_path data/processed_data/test.json \
  --constraints_path ontology_constraints.json \
  --output_path outputs/phase2_scierc_full_s1_llama.jsonl \
  --device cuda:0

# DocRED
python3 run_constrained_extraction.py \
  --mode full_s1 \
  --dataset docred \
  --model_path $MODEL \
  --data_path data/docred/dev.json \
  --constraints_path data/docred/ontology_constraints_docred.json \
  --output_path outputs/phase2_docred_full_s1_llama.jsonl \
  --device cuda:0
```

---
