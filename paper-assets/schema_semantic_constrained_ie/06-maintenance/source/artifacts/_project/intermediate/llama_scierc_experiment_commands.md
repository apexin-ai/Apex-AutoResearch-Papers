# Llama-3.1-8B SciERC Cross-Model Validation (D009)

## Compatibility Status (verified 2025-05-14)
- Code: ZERO modifications needed
- Tokenizer: enable_thinking=False silently ignored by Llama template
- XGrammar: TokenizerInfo + GrammarCompiler + schema compilation all OK
- First-token uniqueness: All 6 SciERC entity types have unique first tokens
  - Task(6396), Method(3607), Material(13721), Metric(55410), OtherScientificTerm(11663), Generic(20560)
- Dry-run: 2 samples × 2 modes = 4/4 success, JSON parse 100%

## Experiment 1: Unconstrained Baseline

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/schema_semantic_constrained_ie
nohup python run_constrained_extraction.py \
  --mode unconstrained \
  --dataset scierc \
  --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct \
  --data_path data/processed_data/test.json \
  --constraints_path ontology_constraints.json \
  --output_path outputs/phase2_scierc_llama_unconstrained.jsonl \
  --device cuda:0 \
  --max_new_tokens 2048 \
  > /tmp/llama_unconstrained.log 2>&1 &
```

## Experiment 2: Full S1 (Grammar + Semantic)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/schema_semantic_constrained_ie
nohup python run_constrained_extraction.py \
  --mode full_s1 \
  --dataset scierc \
  --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct \
  --data_path data/processed_data/test.json \
  --constraints_path ontology_constraints.json \
  --output_path outputs/phase2_scierc_llama_full_s1.jsonl \
  --device cuda:0 \
  --max_new_tokens 2048 \
  > /tmp/llama_full_s1.log 2>&1 &
```

## Estimated Runtime
- 551 samples × ~5s/sample = ~46 min per experiment
- Total: ~92 min sequential, or ~46 min if run on separate GPUs

## GPU Notes
- Llama-3.1-8B bf16 ≈ 16GB VRAM
- Both GPUs have ~80GB free (DocRED using ~17.5GB each)
- Can run both experiments in parallel on cuda:0 and cuda:1
