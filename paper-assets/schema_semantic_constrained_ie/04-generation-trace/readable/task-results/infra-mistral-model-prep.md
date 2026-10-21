# infra mistral model prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_mistral_model_prep_20260516T041654_result.json`
- **Structured JSON:** [`0c0f7d438b491d1377e6.json`](../../sessions/0c/0c0f7d438b491d1377e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 任务完成总结

### 1. 模型下载路径
```
/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3  (symlink)
→ /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3-ms/mistralai/Mistral-7B-Instruct-v0___3/
```
- 3 个分片：model-00001 (4.7GB) + model-00002 (4.7GB) + model-00003 (4.3GB) = 13.7GB
- 通过 ModelScope 下载（HuggingFace 超时失败）

### 2. Tokenizer 兼容性结论：完全兼容，无需修改代码

验证点：
| 检查项 | 结果 |
|--------|------|
| `apply_chat_template` (system+user) | `&lt;s>[INST] {system}\n\n{user}[/INST]` |
| `apply_chat_template` (user only) | `&lt;s>[INST] {user}[/INST]` |
| `_chat_template_kwargs` | 返回 `{}` (非 Qwen，不传 enable_thinking) |
| `pad_token` 处理 | None → 已有代码设为 eos_token |
| XGrammar `TokenizerInfo.from_huggingface` | vocab_size=32768, OK |
| `GrammarCompiler` | OK |
| Entity type first token 映射 | 所有 6 种类型正确编码 |
| 无硬编码特殊 token | 代码全部通过 `apply_chat_template` |

### 3. 代码修改：无

所有 3 个核心脚本 (`run_extraction.py`, `run_extraction_docred.py`, `run_constrained_extraction.py`) 均通过 `--model_path` 参数自动适配，无模型特定逻辑（除 Qwen 的 `enable_thinking=False`，对 Mistral 不触发）。

### 4. Generation config 建议

| 参数 | SciERC | DocRED |
|------|--------|--------|
| `max_new_tokens` | 1024 | 4096 |
| `do_sample` | False | False |
| `temperature` | None (greedy) | None (greedy) |

与现有 Qwen/Llama 配置一致，无需调整。Mistral 上下文窗口 32K tokens 足够。

### 运行示例
```bash
# SciERC
python run_extraction.py --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/scierc/test.json --output_path outputs/mistral_scierc.jsonl

# DocRED
python run_extraction_docred.py --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/docred/dev.json --output_path outputs/mistral_docred.jsonl

# Constrained extraction
python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/scierc/test.json --constraints_path ontology_constraints.json --output_path outputs/mistral_constrained.jsonl
```

---
