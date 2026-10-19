# Process Check Loop 5 — 2026-05-16T~12:30 UTC

## 1. lm_eval_teal_50pct (PID 190830, cuda:1)

**Status: ALIVE** — running 2h30m

- 子进程 PID 190835 占 GPU 1 ~20GB
- 当前进度: loglikelihood requests 56% (35551/63389)，正在跑 MMLU
- 速度 ~530 it/s，预估剩余 ~53s 完成 loglikelihood 阶段
- 但 loglikelihood 之后可能还有 generate_until (gsm8k) 阶段
- 结果目录 `results/lm_eval_teal_50pct/` 尚未创建

**预计**: 再 30-60 分钟完成全部 benchmark。

## 2. lm_eval_kl_s42 (DONE)

**结果 (plan_007/results.json)**:

| Benchmark | Score | 随机基线 | 判定 |
|-----------|-------|---------|------|
| arc_challenge | 0.3771 (acc_norm) | 0.25 | 略高于随机 |
| winogrande | 0.6156 | 0.50 | 中等 |
| mmlu | 0.2591 | 0.25 | 接近随机 |
| gsm8k | 0.0121 (exact_match) | ~0 | 几乎为零 |

**summary.json 中 raw acc 细节**:
- arc_challenge: acc=0.3063, acc_norm=0.3259
- winogrande: acc=0.6212
- mmlu: acc=0.2359 (stem 0.2287, humanities 0.2429, social_sciences 0.2255, other 0.2430)
- gsm8k: strict=0.0182, flexible=0.0197

**结论**: kl_s42 模型（KL 蒸馏 50% sparsity, seed 42）质量极差。MMLU 接近随机猜测，gsm8k 近乎为零，arc/winogrande 仅略高于随机。确认 negative 判定。

耗时: ~3010s (~50 min)

## 3. GPU 状态

| GPU | 型号 | 利用率 | 显存占用 | 进程 |
|-----|------|--------|----------|------|
| 0 | RTX PRO 6000 Blackwell | 0% | 16213/97887 MiB | PID 191340: lm_eval_kl_30pct (sparsity 30%) |
| 1 | RTX PRO 6000 Blackwell | 92% | 19991/97887 MiB | PID 190835: lm_eval_teal_50pct |

**注意**: GPU 0 上发现未在任务列表中的进程——PID 191340 正在跑 `lm_eval_sparse.py --sparsity_target 0.3 --predictor_path checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --output_path results/lm_eval_kl_30pct`，已运行 2h32m。0% GPU 利用率可能表示正在做 CPU-bound 的 tokenization 或 I/O 阶段。

## 4. 建议下一步

1. **等待 lm_eval_teal_50pct 完成**（预计 30-60 min），收集 TEAL 50% sparsity 的 benchmark 对比数据
2. **监控 lm_eval_kl_30pct** (GPU 0)——确认是否正常运行，0% GPU util 需关注（可能卡住或刚进入 generate 阶段间歇）
3. **kl_s42 结论已明确**: 50% sparsity 的 KL 蒸馏模型质量不可接受，需要考虑降低 sparsity target 或换蒸馏策略
4. 如果 kl_30pct 结果也 negative，说明 KL predictor 方案整体有问题，应重点关注 TEAL 方案
