# validate llama dryrun

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_validate_llama_dryrun_20260514T104630_result.json`
- **Structured JSON:** [`430d092f1581a68ff0bd.json`](../../sessions/43/430d092f1581a68ff0bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已获取全部所需信息。汇报如下：

---

## Dry-run 验证结果

### 1. 模型文件
**存在且完整。** 4 个 safetensors shard（~15GB），config.json / tokenizer.json / tokenizer_config.json 齐全。

### 2. Tokenizer 加载
**成功。** `vocab_size=128000, eos=<|eot_id|>`，chat template 正常工作（Llama 3.1 格式带 system header）。

### 3. 脚本参数解析
**正常。** `--model_path` 支持自定义路径，所有必要参数均可通过命令行传入。

### 4. Qwen-specific hardcode 检查

两处需注意，但 **不需要改代码**：

| 位置 | 内容 | 影响 |
|------|------|------|
| L28-31 `_chat_template_kwargs()` | 检测 `'qwen' in name` 时传 `enable_thinking=False`，否则返回空 dict | **无影响** — Llama 路径不含 "qwen"，走 `return {}` 分支，正确 |
| L622-629 默认 model_path | fallback 路径写死为 Qwen3-8B，找不到则报错 | **无影响** — 我们显式传 `--model_path`，不走 fallback |

**结论：脚本对 Llama 完全兼容，无需修改。**

### 5. 四个 Llama 实验命令（复制即用）

**a) llama_scierc_unconstrained**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/llama_scierc_unconstrained.jsonl --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --device cuda:0 --batch_size 1"
```

**b) llama_scierc_full_s1**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/llama_scierc_full_s1.jsonl --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --device cuda:0 --batch_size 1"
```

**c) llama_docred_unconstrained**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_unconstrained.jsonl --max_new_tokens 4096 --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --device cuda:0 --batch_size 1"
```

**d) llama_docred_full_s1**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_full_s1.jsonl --max_new_tokens 4096 --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --device cuda:0 --batch_size 1"
```

### 注意事项
- **GPU 占用**：当前 cuda:0 和 cuda:1 都被 DocRED 实验占用，需等完成后再执行。Llama-8B bfloat16 约需 ~16GB 显存，单卡 A6000 (48GB) 足够。
- **`--resume` 支持**：脚本有 `--resume` 参数可断点续跑，建议加上以防中断。

---
