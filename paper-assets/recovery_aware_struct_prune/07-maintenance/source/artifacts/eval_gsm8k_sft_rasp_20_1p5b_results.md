# Eval: GSM8K SFT RASP 20% 1.5B

## 核心指标

| 指标 | 值 |
|---|---|
| **Accuracy** | **26.91%** (0.2691) |
| Stderr | ±1.22% |
| n_correct | 355 |
| n_total | 1319 |
| Mode | greedy (T=0.0, do_sample=false) |
| EOS rate | 94.16% (77/1319 truncated) |
| Avg response length | 378.6 tokens |

## Checkpoint

- **model_path**: `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b`
- **result_file**: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json`
- **log_file**: 不存在（未找到对应 .log 文件）

## GRPO Delta 计算

| 方法 | GSM8K Accuracy |
|---|---|
| SFT RASP 20% 1.5B | 26.91% |
| GRPO RASP 20% 1.5B | 26.16% |
| **GRPO delta** | **-0.75 pp** |

## 结论

**Negative**。SFT baseline (26.91%) 高于 GRPO (26.16%)，GRPO delta 为负 (-0.75 pp)。GRPO 在 RASP 20% 1.5B 设定下未能超越 SFT recovery。

注：ROADMAP 记录的 interim accuracy (27.64%) 高于本次最终结果 (26.91%)，差异可能源于评估配置差异（greedy vs sampling）。
