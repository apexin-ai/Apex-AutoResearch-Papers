# bench_mistral_kl50_s42 预验证报告

**日期**: 2026-05-16
**实验**: D029 — Mistral-7B KL 50% sparsity 统一 few-shot benchmark eval

---

## 前置条件检查清单

| # | 检查项 | 状态 | 详情 |
|---|--------|------|------|
| 1 | Predictor checkpoint | ✅ | `checkpoints/mistral_kl_s42/predictor_kl_normalized.pt` (145MB) |
| 2 | Base model | ✅ | `/root/autodl-tmp/models/mistral-7b/` — 3 shard safetensors, config, tokenizer 齐全 |
| 3 | 模型架构兼容性 | ✅ | Mistral-7B: hidden=4096, intermediate=14336, 32 layers — 与 Llama-3.1-8B intermediate_size 一致，bottleneck_size=128 兼容 |
| 4 | benchmark_eval.py Mistral 支持 | ✅ | `--model_name_or_path` 可覆盖默认 Llama 路径；代码用通用 `mlp.gate_proj/up_proj/down_proj` 接口，无 Llama 硬编码 |
| 5 | sparsity_mode=teal_global | ✅ | 脚本支持 `choices=["per_token", "teal_global"]` |
| 6 | allocation=global_topk | ✅ | 脚本支持 `choices=["global_topk", "uniform"]`，默认 global_topk |
| 7 | Few-shot 设置 | ✅ | 硬编码 `LM_EVAL_DEFAULTS`: ARC-c=25, WG=5, MMLU=5, GSM8K=8 — 无需手动指定 |
| 8 | lm-eval 安装 | ✅ | `/root/miniconda3/lib/python3.12/site-packages/lm_eval` 已安装 |
| 9 | 结果目录 | ✅ | `results/benchmark/bench_mistral_kl50_s42/` 已存在且为空，无冲突 |
| 10 | GPU 可用性 | ⏳ | cuda:1 当前被 bce_isocompute_v3_s42 占用（RUNNING），需等其完成 |

## 推荐启动命令

```bash
CUDA_VISIBLE_DEVICES=1 nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 && python -u src/benchmark_eval.py \
  --exp_id bench_mistral_kl50_s42 \
  --model_name_or_path /root/autodl-tmp/models/mistral-7b \
  --checkpoint checkpoints/mistral_kl_s42/predictor_kl_normalized.pt \
  --sparsity_mode teal_global \
  --sparsity_target 0.5 \
  --allocation global_topk \
  --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k \
  --gpu 0' > /root/distill_sparse_swiglu/logs/bench_mistral_kl50_s42.log 2>&1 &
```

**参数说明**:
- `CUDA_VISIBLE_DEVICES=1` + `--gpu 0`: 映射物理 cuda:1 → 逻辑 cuda:0
- `nohup`: 符合 C002 约束（禁止裸 tmux）
- `HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1`: 离线模式，避免网络请求
- `teal_global` + `global_topk`: 静态校准 mask，可复现

## 潜在问题

### ⚠️ Registry PENDING 条目的 sparsity_mode 不一致

Registry 中已有 `bench_mistral_kl50_s42` PENDING 条目，但其命令使用 `--sparsity_mode per_token`（动态逐 token mask），而非 `teal_global`（静态校准 mask）。上述推荐命令使用 `teal_global + global_topk`，与 d030 系列一致。提交前需确认使用哪种模式，或是否需要两种都跑。

### 参考: d030_kl50_uniform 命令格式

```bash
python -u src/benchmark_eval.py --exp_id d030_kl50_uniform \
  --checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt \
  --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform \
  --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0
```

d030 用 `allocation=uniform`，本实验用 `allocation=global_topk`——这是有意区分。