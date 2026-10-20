# ssh cuda1 prep

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cuda1-prep_20260512T131016_result.json`
- **Structured JSON:** [`5c4ab8c77d0b22db2170.json`](../../sessions/5c/5c4ab8c77d0b22db2170.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是汇报。

---

## 汇报

### 1. DeBERTa NLI 模型

- **状态**: ✅ 可用
- **模型路径**: `/root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large`（ModelScope 下载，完整）
- **HF cache 路径不完整**：`models--cross-encoder--nli-deberta-v3-large/` 缺权重文件（下载被中断）
- **推理验证**: 通过。5 个测试 case 中 4 个正确：
  - ✅ "eating pizza" → "eats something" = entailment
  - ✅ "woman sleeping" → "man running" = contradiction
  - ✅ "cat sat on mat" → "cat is on mat" = entailment
  - ❌ "Obama born Hawaii" → "Obama born US" = contradiction（需要世界知识，NLI 模型已知局限）
  - ✅ "raining" → "sunny" = contradiction
- **运行时注意**: `rewards.py:143` 默认用 HF ID `cross-encoder/nli-deberta-v3-large`，AutoDL 无外网会失败。需传 `--nli_model_name /root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large`

### 2. rerank_nli.py

- **状态**: ✅ dry-run 通过
- `from rerank_nli import *` 成功
- `--help` 正常输出
- 数据格式验证:
  - Keys: `document_text, gold_relations, messages, prompt, sentences`
  - Gold relations: 7条/sample，keys = `evidence, evidence_sids, head, relation, tail`
  - Evidence 格式为 sentence list
- **注意**: 同上，`--nli_model_name` 默认值需改为本地路径

### 3. train_grpo.py API 兼容性

- **`--help` 正常**（GRPOConfig 实例化在 main() 中，不被触发）
- **兼容性问题**:

| 参数 | 状态 | 说明 |
|------|------|------|
| `max_completion_length` | ✅ | GRPOConfig 支持 |
| `num_generations` | ✅ | GRPOConfig 支持 |
| `temperature` | ✅ | GRPOConfig 支持 |
| `beta` | ✅ | GRPOConfig 支持 |
| **`max_prompt_length`** | ❌ | **GRPOConfig 无此参数，train_grpo.py:67 运行时会报错** |
| `max_seq_length` / `max_length` | ❌ | 两者都不存在 |

- **vLLM 版本警告**: TRL 支持 0.11.0–0.17.1，当前装了 0.18.1
- **需修复**:
  1. `train_grpo.py:67`：移除 `max_prompt_length=grpo_args.max_prompt_length,`，改为在 tokenization/数据预处理阶段手动截断 prompt
  2. 运行时需传 `--nli_model_name` 为本地路径

---
