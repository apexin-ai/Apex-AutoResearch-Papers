# code docred lora eval prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_docred_lora_eval_prep_20260515T182621_result.json`
- **Structured JSON:** [`19875e0c40fc011761a1.json`](../../sessions/19/19875e0c40fc011761a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪。汇总：

**脚本路径**: `scripts/run_docred_lora_eval.sh`

**Merged checkpoint 路径**:
- Qwen: `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged`
- Llama: `/root/autodl-tmp/checkpoints/llama_lora_docred_merged`

**4 个 eval 命令**:

| 命令 | mode | model | device | output |
|------|------|-------|--------|--------|
| `qwen_unconstrained` | unconstrained | qwen_lora_docred_merged | cuda:1 | `outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl` |
| `qwen_constrained` | full_s1 | qwen_lora_docred_merged | cuda:1 | `outputs/w5_qwen_docred_lora_constrained_eval.jsonl` |
| `llama_unconstrained` | unconstrained | llama_lora_docred_merged | cuda:0 | `outputs/w5_llama_docred_lora_unconstrained_eval.jsonl` |
| `llama_constrained` | full_s1 | llama_lora_docred_merged | cuda:0 | `outputs/w5_llama_docred_lora_constrained_eval.jsonl` |

所有命令：`--dataset docred`, `--data_path data/docred/dev.json`, `--constraints_path data/docred/ontology_constraints_docred.json`, `--max_new_tokens 4096`, `--batch_size 1`

**DocRED vs SciERC 差异**:
- 无特殊处理差异。`run_constrained_extraction.py` 通过 `--dataset docred` 参数切换数据加载函数 (`load_docred_data`) 和 prompt 模板，约束文件也是独立的 `ontology_constraints_docred.json`
- SciERC 的 merged model 在 `checkpoints/` 下有 symlink → autodl-tmp；DocRED 训练完成后需要确认 merged 目录是否正确写入（或手动创建 symlink）

**用法**: `bash scripts/run_docred_lora_eval.sh qwen_unconstrained` 单跑，或 `all` 全跑。语法校验通过。

---
