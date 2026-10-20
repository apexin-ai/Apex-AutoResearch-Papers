# ops constrained eval prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_constrained_eval_prep_20260515T230314_result.json`
- **Structured JSON:** [`97ab19600ed4137347ec.json`](../../sessions/97/97ab19600ed4137347ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the report:

---

## DocRED Constrained Eval 准备就绪报告

### 检查清单

| # | 检查项 | 状态 |
|---|--------|------|
| 1 | Qwen merged model (`qwen_lora_docred_merged`) | **PASS** — 4 shards, ~15.2GB, config/tokenizer 完整 |
| 2 | Llama merged model (`llama_lora_docred_merged`) | **PASS** — 4 shards, ~14.9GB, config/tokenizer 完整 |
| 3 | 约束文件 (`ontology_constraints_docred.json`) | **PASS** — 63KB, keys: `entity_types`(6), `relation_types`(96), `relation_constraints`(96 relations with valid_pairs), `summary` |
| 4 | 脚本 `--mode` 选项 | **PASS** — choices: `unconstrained`, `grammar_only`, `semantic_only`, `full_s1`, `full_s2` |
| 5 | SciERC hardcode 检查 | **PASS** — SciERC 逻辑在 lines 65/160/186/216/636-637，均有 `if dataset == "scierc"` 分支保护，不影响 docred 路径 |

### 当前 Unconstrained Eval 进度

| 模型 | 日志进度 | JSONL 行数 | 完成度 |
|------|---------|-----------|--------|
| **Qwen** | 487/998 | 525 | ~49% |
| **Llama** | 659/998 | 739 | ~66% |

Llama 预计 ~1-1.5h 完成，Qwen 预计 ~2h 完成。

### Constrained Eval 提交命令

**Qwen constrained (full_s1):**
```bash
cd /root/schema_semantic_constrained_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup python run_constrained_extraction.py \
  --mode full_s1 \
  --dataset docred \
  --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged \
  --data_path data/docred/dev.json \
  --constraints_path data/docred/ontology_constraints_docred.json \
  --output_path outputs/w5_qwen_docred_lora_full_s1_eval.jsonl \
  --max_new_tokens 2048 \
  > ~/runs/schema_semantic_constrained_ie/w5_qwen_docred_lora_constrained_eval.log 2>&1 &
```

**Llama constrained (full_s1):**
```bash
cd /root/schema_semantic_constrained_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup python run_constrained_extraction.py \
  --mode full_s1 \
  --dataset docred \
  --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged \
  --data_path data/docred/dev.json \
  --constraints_path data/docred/ontology_constraints_docred.json \
  --output_path outputs/w5_llama_docred_lora_full_s1_eval.jsonl \
  --max_new_tokens 2048 \
  > ~/runs/schema_semantic_constrained_ie/w5_llama_docred_lora_constrained_eval.log 2>&1 &
```

**注意**: 两个 constrained eval 需在对应 unconstrained eval 完成后启动（释放 GPU 显存）。如需顺序执行两个 constrained，可在第一个命令后加 `wait` 再启动第二个。

---
