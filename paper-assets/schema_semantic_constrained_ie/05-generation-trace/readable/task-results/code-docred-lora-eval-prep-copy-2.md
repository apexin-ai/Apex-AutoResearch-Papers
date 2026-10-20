# code docred lora eval prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_docred_lora_eval_prep_20260515T181757_result.json`
- **Structured JSON:** [`b2bcaf788723c5929b5d.json`](../../sessions/b2/b2bcaf788723c5929b5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

参数解析通过。以下是 4 个完整的 submit 命令和分析。

---

## 4 个 Eval 命令

### 1. Qwen DocRED LoRA — unconstrained
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && CUDA_VISIBLE_DEVICES={GPU} python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_qwen_lora_docred_unconstrained.jsonl --max_new_tokens 2048 --resume"
```

### 2. Qwen DocRED LoRA — constrained (full_s1)
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && CUDA_VISIBLE_DEVICES={GPU} python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_qwen_lora_docred_constrained.jsonl --max_new_tokens 2048 --resume"
```

### 3. Llama DocRED LoRA — unconstrained
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && CUDA_VISIBLE_DEVICES={GPU} python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_llama_lora_docred_unconstrained.jsonl --max_new_tokens 2048 --resume"
```

### 4. Llama DocRED LoRA — constrained (full_s1)
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && CUDA_VISIBLE_DEVICES={GPU} python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_llama_lora_docred_constrained.jsonl --max_new_tokens 2048 --resume"
```

---

## 预估运行时间

| Eval | 样本数 | 参考 avg/sample | 预估总时间 |
|------|--------|-----------------|-----------|
| unconstrained | 998 | ~13s | ~3.5h |
| full_s1 (constrained) | 998 | ~18s | ~5h |

参考来源：zero-shot DocRED eval 的历史日志（Llama unconstrained ~7-18s/sample, Qwen full_s1 ~10-28s/sample）。LoRA 模型同架构同大小，推理速度应一致。

## 注意事项

1. **参数名是 `--constraints_path`（有 s）**，不是 `--constraint_path`
2. **必须传 `--dataset docred`**，脚本靠这个参数选数据加载函数和 prompt 模板
3. **max_new_tokens=2048 够用**——历史对比：mt6144 vs 默认 2048 的成功率几乎相同（unconstrained 931 vs 930, full_s1 908 vs 907）
4. **加了 `--resume`**——万一中断可断点续跑
5. **每个 eval 占 1 张 GPU ~16GB 显存**（8B 模型 bf16），可在不同 GPU 上并行跑 2 个

---
