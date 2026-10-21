# Plan 007 Full Benchmark Eval Commands

## Few-shot 设置 (benchmark_eval.py 硬编码)
- ARC-c: 25-shot
- WinoGrande: 5-shot
- MMLU: 5-shot
- GSM8K: 8-shot

⚠️ lm_eval_sparse.py / lm_eval_teal.py 默认 0-shot，结果不可比

## Checkpoints (全部已验证存在)
- kl_sparsity70_s42/predictor_kl_normalized.pt
- ste_baseline_s42/predictor_kl_normalized.pt
- bce_isocompute_v2_s42/predictor_bce.pt
- mistral_kl_s42/predictor_kl_normalized.pt

## 命令 (共用前缀)
```
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1
```

### 1. TEAL 30% → bench_teal30
python -u src/benchmark_eval.py --exp_id bench_teal30 --baseline_mode teal_vanilla --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0

### 2. KL 70% → bench_kl70_s42
python -u src/benchmark_eval.py --exp_id bench_kl70_s42 --checkpoint checkpoints/kl_sparsity70_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.7 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0

### 3. STE 50% → bench_ste50_s42
python -u src/benchmark_eval.py --exp_id bench_ste50_s42 --checkpoint checkpoints/ste_baseline_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0

### 4. BCE iso-compute 50% → bench_bce_iso50_s42
python -u src/benchmark_eval.py --exp_id bench_bce_iso50_s42 --checkpoint checkpoints/bce_isocompute_v2_s42/predictor_bce.pt --sparsity_mode per_token --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0

### 5. WINA 50% → bench_wina50
python -u src/benchmark_eval.py --exp_id bench_wina50 --baseline_mode wina --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0

### 6. Mistral KL 50% → bench_mistral_kl50_s42
python -u src/benchmark_eval.py --exp_id bench_mistral_kl50_s42 --model_name_or_path /root/autodl-tmp/models/mistral-7b --checkpoint checkpoints/mistral_kl_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0

## 执行顺序 (双GPU并行, ~135min total)
Batch 1: cuda:0=TEAL30, cuda:1=KL70
Batch 2: cuda:0=STE50, cuda:1=BCE_iso50
Batch 3: cuda:0=WINA50, cuda:1=Mistral_KL50
