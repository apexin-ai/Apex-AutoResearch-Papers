# eval_kl30_teal_30pct 评估命令

## 背景

KL 30% predictor 此前在 sparsity_target=0.5（默认值）下评估，报告 TEAL PPL=13.63，需要用 sparsity_target=0.3 重新评估获得真实值。

## Checkpoint

```
/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt  (145MB)
```

## 1. PPL 评估 (evaluate.py)

```bash
cd /root/distill_sparse_swiglu && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=0 nohup python -u src/evaluate.py \
  --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b \
  --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt \
  --sparsity_target 0.3 \
  --gpu 0 \
  --max_eval_samples 200 \
  > logs/eval_kl30_teal_30pct.log 2>&1 &
```

查看结果：
```bash
tail -30 /root/distill_sparse_swiglu/logs/eval_kl30_teal_30pct.log
```

## 2. Downstream benchmark (benchmark_eval.py)

### 2a. Per-token predictor 模式

```bash
cd /root/distill_sparse_swiglu && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=0 nohup python -u src/benchmark_eval.py \
  --exp_id kl30_pertoken_30pct \
  --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt \
  --sparsity_mode per_token \
  --sparsity_target 0.3 \
  --tasks wikitext2,arc_challenge,winogrande \
  --gpu 0 \
  > logs/bench_kl30_pertoken_30pct.log 2>&1 &
```

### 2b. TEAL global mask 模式

```bash
cd /root/distill_sparse_swiglu && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=0 nohup python -u src/benchmark_eval.py \
  --exp_id kl30_teal_global_30pct \
  --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt \
  --sparsity_mode teal_global \
  --sparsity_target 0.3 \
  --tasks wikitext2,arc_challenge,winogrande \
  --gpu 0 \
  > logs/bench_kl30_teal_global_30pct.log 2>&1 &
```

结果路径：
- `results/benchmark/kl30_pertoken_30pct/results.json`
- `results/benchmark/kl30_teal_global_30pct/results.json`

## GPU 用量与时长估算

| 评估 | GPU | 显存 | 预计时长 |
|------|-----|------|---------|
| evaluate.py (PPL) | cuda:0 单卡 | ~18-20GB (LLaMA-3.1-8B + predictor) | 15-25 min |
| benchmark_eval.py per_token | cuda:0 单卡 | ~18-20GB | 30-60 min (取决于 task 数) |
| benchmark_eval.py teal_global | cuda:0 单卡 | ~18-20GB | 30-60 min |

均在 RTX PRO 6000 Blackwell (48GB) 舒适范围内。可在 cuda:0 和 cuda:1 上并行跑两个任务。

## 注意事项

1. **参数名是 `--checkpoint`，不是 `--predictor_path`** — 任务模板中的参数名有误
2. **`--sparsity_target` 默认 0.5** — 两个脚本都是，不传 0.3 会得到 50% 稀疏度的结果（此前的 13.63 就是这个问题）
3. **evaluate.py 无 `--output_dir`** — 结果打印到 stdout，必须重定向日志保存
4. **约束 C001** — 仅限 cuda:0 和 cuda:1
5. **约束 C002** — 必须用 nohup 启动，不能裸 tmux
6. **并行策略** — evaluate.py 在 cuda:0，benchmark_eval.py 在 cuda:1 可以同时跑；或者串行跑省心
