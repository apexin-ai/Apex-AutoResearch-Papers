# R9-C2: Generation-Time Compound Sparsity Accuracy Evaluation

## Summary

| Model | Sparsity | Dense Acc | Sparse Acc | Δ |
|-------|----------|-----------|------------|---|
| DeepSeek-R1-Distill-Qwen-7B | 0.15 | 52% (26/50) | 34% (17/50) | -18pp |
| DeepSeek-R1-Distill-Qwen-7B | 0.30 | 52% (26/50) | 10% (5/50) | -42pp |
| Qwen2.5-7B-Instruct | 0.15 | 32% (16/50) | 32% (16/50) | 0pp |
| Qwen2.5-7B-Instruct | 0.30 | 32% (16/50) | 14% (7/50) | -18pp |

## Setup
- Benchmark: MATH-500, 50 stratified problems (10 per difficulty × 5 levels, seed=42)
- Compound sparsity: head pruning (Frobenius norm importance) + KV cache eviction (cumulative attention)
- Attention: eager (required for importance scoring)
- Precision: bf16
- Max new tokens: 2048
- Server: westd-22162, 4× RTX 6000 Pro 48GB

## Key Findings

1. **Reasoning models are fragile under sparsity**: DS loses 18pp even at mild s=0.15, and collapses to 10% at s=0.30 — its long chain-of-thought breaks when intermediate attention patterns are disrupted
2. **Standard instruct models are robust at low sparsity**: QW shows zero accuracy loss at s=0.15, indicating many heads and KV positions are redundant for instruction-following
3. **s=0.30 is universally destructive**: Both models show significant degradation, suggesting this exceeds the redundancy budget
4. **Phase-gating is essential**: These results validate that compound sparsity needs an accuracy-aware gating mechanism — applying uniform sparsity is too aggressive for reasoning tasks

## Output Files (on westd-22162)
- /root/autodl-tmp/pacs/analysis_output/accuracy_eval_ds_s015.json
- /root/autodl-tmp/pacs/analysis_output/accuracy_eval_ds_s030.json
- /root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s015.json
- /root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s030.json

## Script
- /root/autodl-tmp/pacs/run_accuracy_eval.py
