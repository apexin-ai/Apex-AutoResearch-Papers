# code mistral adaptation

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral_adaptation_20260516T025856_result.json`
- **Structured JSON:** [`a60dfc334b141cb4628e.json`](../../sessions/a6/a60dfc334b141cb4628e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 改动摘要

### 修改的文件

| 文件 | 改动 |
|------|------|
| `run_constrained_extraction.py` | 行623-627: 默认模型候选列表新增 Llama/Mistral 路径；行631: 错误信息改为通用 |
| `download_mistral.sh` | **新建**，39行，HF下载+验证脚本 |

### 为什么只改了2行

现有代码已完全模型无关：
- **AutoModelForCausalLM**: 自动加载 MistralForCausalLM
- **apply_chat_template**: Mistral v0.3 tokenizer 自带 chat template，正确处理 system/user 角色
- **`_chat_template_kwargs`**: 对非 Qwen 模型返回 `{}`，Mistral 不需要 `enable_thinking`
- **pad_token**: 已有 `pad_token = eos_token` 兜底
- **XGrammar**: 32K vocab + 标准 BPE，完全兼容

运行时只需 `--model_path /root/autodl-tmp/models/mistralai/Mistral-7B-Instruct-v0.3` 即可，其余参数与 Qwen/Llama 完全一致。`download_mistral.sh` 未执行，等 GPU 实验完成后再运行。

---
