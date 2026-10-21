# Diagnostic: perlayer_kl_k16_eval_v2 Failure

## 失败根因

**`nohup` 不 source `.bashrc`，导致 `HF_HOME` 未设置。**

- `.bashrc` 中有 `export HF_HOME=/root/autodl-tmp/.hf_cache`
- 所有 lm-eval 数据集已缓存在 `/root/autodl-tmp/.hf_cache/datasets/`（ai2_arc, winogrande, mmlu, gsm8k, hellaswag, piqa 均存在）
- 但 nohup 启动时 HF_HOME 未生效，datasets 库去默认路径 `/root/.cache/huggingface/datasets/` 找——该目录不存在
- WikiText-2 PPL 成功（8.6737）是因为 wikitext eval 由 benchmark_eval.py 自己实现，不走 lm-eval 的 datasets.load_dataset

## Parent 对比 (perlayer_kl_k16_s42_v3_eval)

| | Parent (v3_eval) | v2 |
|---|---|---|
| 错误 | `[Errno 101] Network is unreachable` → HF Hub 连不上 | `OfflineModeIsEnabled` → 离线模式下找不到本地缓存 |
| 根因 | 同样没有 HF_HOME → 找不到本地缓存 → 尝试联网下载 → 网络不可达 | 加了 `HF_DATASETS_OFFLINE=1` 禁止联网 → 但 HF_HOME 仍缺失 → 本地缓存找不到 |
| WikiText-2 | PPL = 8.6737 ✓ | PPL = 8.6737 ✓ |
| 崩溃点 | arc_challenge 加载 | arc_challenge 加载 |

两次是同一根因的不同表现：缺 HF_HOME → 缓存路径错误。v2 的 `HF_DATASETS_OFFLINE=1` 只是把"网络不可达"换成了"离线模式无缓存"。

## K=8 成功对比

没有找到 K=8 eval 的日志文件。参考其他成功的 eval 日志（c1_ablation_30pct_s42_eval_34887, kl50_s42_uniform_eval），这些成功运行的特征是：
- 在交互式 shell 中启动（.bashrc 被 source，HF_HOME 生效）
- 或当时网络可用，datasets 能从 HF Hub 下载

## 修复命令

```bash
nohup env HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_OFFLINE=1 WANDB_MODE=disabled \
  python -u /root/distill_sparse_swiglu/src/benchmark_eval.py \
  --exp_id perlayer_kl_k16_eval_v3 \
  --checkpoint /root/distill_sparse_swiglu/checkpoints/perlayer_kl_k16_s42_v3/predictor_perlayer_kl_k4.pt \
  --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform \
  --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k,hellaswag,piqa \
  --seq_len 2048 --gpu 0 \
  > /root/runs/distill_sparse_swiglu/perlayer_kl_k16_eval_v3.log 2>&1 &
```

显式传 `HF_HOME=/root/autodl-tmp/.hf_cache`，不依赖 .bashrc 加载。

## Checkpoint 确认

`predictor_perlayer_kl_k4.pt` 存在（145MB），无问题。
