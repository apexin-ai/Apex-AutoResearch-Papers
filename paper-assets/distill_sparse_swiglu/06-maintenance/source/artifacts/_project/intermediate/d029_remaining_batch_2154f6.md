# D029 Benchmark 统一重跑 — 剩余待跑命令

> 生成时间: 2026-05-16
> 评测脚本: src/benchmark_eval.py (few-shot: ARC-c=25, WG=5, MMLU=5, GSM8K=8)

## 当前 GPU 状态

| GPU | PID | 实验 | 脚本 | 备注 |
|-----|-----|------|------|------|
| cuda:0 | 200697 | d030_kl30_uniform | benchmark_eval.py | KL 30% uniform allocation (D030) |
| cuda:1 | 201003 | lm_eval_mistral_kl_50pct | lm_eval_sparse.py | **0-shot，非 benchmark_eval，需重跑** |

## 已完成的 benchmark_eval 结果

**无。** `results/benchmark/` 下 bench_teal30, bench_teal50, d030_kl30_uniform 目录均为空（未产出 results.json）。

## 共用前缀

```bash
ENV_PREFIX="source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1"
TASKS="wikitext2,arc_challenge,winogrande,mmlu,gsm8k"
```

## cuda:1 队列（先空出，优先 Mistral 条件）

### 1. Mistral KL 50% — bench_mistral_kl50_s42
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 && python -u src/benchmark_eval.py --exp_id bench_mistral_kl50_s42 --model_name_or_path /root/autodl-tmp/models/mistral-7b --checkpoint checkpoints/mistral_kl_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 1' > /root/distill_sparse_swiglu/logs/bench_mistral_kl50_s42.log 2>&1 &
```

### 2. Mistral Dense — bench_mistral_dense
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 && python -u src/benchmark_eval.py --exp_id bench_mistral_dense --model_name_or_path /root/autodl-tmp/models/mistral-7b --dense --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 1' > /root/distill_sparse_swiglu/logs/bench_mistral_dense.log 2>&1 &
```

### 3. KL 50% (global top-k) — bench_kl50_s42
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 && python -u src/benchmark_eval.py --exp_id bench_kl50_s42 --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 1' > /root/distill_sparse_swiglu/logs/bench_kl50_s42.log 2>&1 &
```

### 4. KL 30% (global top-k) — bench_kl30_s42
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 && python -u src/benchmark_eval.py --exp_id bench_kl30_s42 --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 1' > /root/distill_sparse_swiglu/logs/bench_kl30_s42.log 2>&1 &
```

### 5. KL 70% (global top-k) — bench_kl70_s42
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 && python -u src/benchmark_eval.py --exp_id bench_kl70_s42 --checkpoint checkpoints/kl_sparsity70_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.7 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 1' > /root/distill_sparse_swiglu/logs/bench_kl70_s42.log 2>&1 &
```

## cuda:0 队列（d030 完成后）

### 6. Dense baseline — bench_dense
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 && python -u src/benchmark_eval.py --exp_id bench_dense --dense --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0' > /root/distill_sparse_swiglu/logs/bench_dense.log 2>&1 &
```

### 7. TEAL 50% — bench_teal50
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 && python -u src/benchmark_eval.py --exp_id bench_teal50 --baseline_mode teal_vanilla --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0' > /root/distill_sparse_swiglu/logs/bench_teal50.log 2>&1 &
```

### 8. TEAL 30% — bench_teal30
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 && python -u src/benchmark_eval.py --exp_id bench_teal30 --baseline_mode teal_vanilla --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0' > /root/distill_sparse_swiglu/logs/bench_teal30.log 2>&1 &
```

### 9. WINA 50% — bench_wina50
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 && python -u src/benchmark_eval.py --exp_id bench_wina50 --baseline_mode wina --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0' > /root/distill_sparse_swiglu/logs/bench_wina50.log 2>&1 &
```

### 10. STE 50% — bench_ste50_s42
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 && python -u src/benchmark_eval.py --exp_id bench_ste50_s42 --checkpoint checkpoints/ste_baseline_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0' > /root/distill_sparse_swiglu/logs/bench_ste50_s42.log 2>&1 &
```

### 11. BCE iso-compute 50% — bench_bce_iso50_s42
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 && python -u src/benchmark_eval.py --exp_id bench_bce_iso50_s42 --checkpoint checkpoints/bce_isocompute_v2_s42/predictor_bce.pt --sparsity_mode per_token --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0' > /root/distill_sparse_swiglu/logs/bench_bce_iso50_s42.log 2>&1 &
```

## 时间估算

每个 benchmark_eval 约 45 分钟（5 tasks × few-shot）。

| GPU | 任务数 | 预估时长 |
|-----|--------|----------|
| cuda:1 | 5 | ~3.75h |
| cuda:0 | 6 | ~4.5h |

总 wall clock ≈ 4.5h（两 GPU 并行后取 max）。

## 排除项

| 条件 | 原因 |
|------|------|
| SPON | benchmark_eval.py 无 SPON baseline_mode，checkpoint 为 spon_biases.pt 格式不兼容 |
| d030_kl30_uniform | D030 实验（KL 30% + uniform allocation），已在 cuda:0 运行中，非 D029 范围 |
| 多种子 KL 50% (s0/s1/s123/s456) | D029 只跑代表性种子 s42，种子方差分析另做 |

## 验证命令

完成后批量检查结果：
```bash
for d in bench_dense bench_kl50_s42 bench_kl30_s42 bench_kl70_s42 bench_teal50 bench_teal30 bench_wina50 bench_ste50_s42 bench_bce_iso50_s42 bench_mistral_kl50_s42 bench_mistral_dense; do
  echo -n "$d: "
  if [ -f "results/benchmark/$d/results.json" ]; then
    python3 -c "import json; r=json.load(open('results/benchmark/$d/results.json')); print('OK', {k:v for k,v in r.get('results',{}).items() if 'acc' in str(v)})"
  else
    echo "MISSING"
  fi
done
```
