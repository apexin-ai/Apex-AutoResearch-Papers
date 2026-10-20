# Llama-3.1-8B-Instruct Cross-Model Validation Commands

Generated: 2026-05-14
Dry-run verified: unconstrained OK, full_s1 OK (fallback counter working)

## SciERC

### Llama SciERC unconstrained (cuda:0)
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && nohup python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/llama_scierc_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048 > /tmp/llama_scierc_unconstrained.log 2>&1 &
```

### Llama SciERC full_s1 (cuda:1)
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && nohup python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/llama_scierc_full_s1.jsonl --device cuda:1 --batch_size 1 --max_new_tokens 2048 > /tmp/llama_scierc_full_s1.log 2>&1 &
```

## DocRED

### Llama DocRED unconstrained (cuda:0)
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && nohup python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096 > /tmp/llama_docred_unconstrained.log 2>&1 &
```

### Llama DocRED full_s1 (cuda:1)
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_full_s1.jsonl --device cuda:1 --batch_size 1 --max_new_tokens 4096 > /tmp/llama_docred_full_s1.log 2>&1 &
```

## Execution Plan

1. DocRED 完成后先跑 SciERC（两卡并行：unconstrained cuda:0, full_s1 cuda:1）
2. SciERC 完成后跑 DocRED（同样两卡并行）
3. Fallback count 从 log 文件中提取：`grep "Grammar-first fallback" /tmp/llama_scierc_full_s1.log | tail -5`

## Notes

- Fallback counter 确认在 `compiler/type_mask_processor.py` 中（L204, L387-399）
- Dry-run 中 full_s1 触发 2 次 fallback（1 sample），说明 Llama 也有 semantic/grammar 冲突
- Fallback count 仅输出到 stderr log，不在 JSONL 输出中——需要保留 log 文件用于分析
