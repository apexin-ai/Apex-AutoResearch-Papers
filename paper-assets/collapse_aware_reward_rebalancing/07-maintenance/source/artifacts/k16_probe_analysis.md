# K=16 Full-FT LR=2e-5 Probe Analysis

**Experiment**: `carr_fullft_lr2e5_k16_probe_01`
**Date**: 2026-05-17
**Runtime**: ~9.2 hours (33194s)
**Config**: K=16 (6.25% retention), Full-FT, LR=2e-5, 3 epochs/gen, 3 generations, 2000 prompts

## Core Metrics Per Generation

| Metric | Gen 0 | Gen 1 | Gen 2 | Change (0→2) |
|--------|-------|-------|-------|--------------|
| mean_quality | 0.1162 | 0.1162 | 0.1149 | -1.1% |
| vendi_score | 107.32 | 106.73 | 107.11 | **-0.19%** |
| self_bleu | 0.0057 | 0.0050 | 0.0058 | +2.9% |
| perplexity | 8.50 | 8.02 | 7.71 | -9.3% |
| mean_nn_distance | 0.7057 | 0.7065 | 0.7092 | +0.50% |
| complexity_mean | 2.887 | 2.848 | 2.818 | -2.4% |

## Vendi Decline

```
vendi_decline_pct = (107.32 - 107.11) / 107.32 * 100 = 0.19%
```

**远低于 5% 阈值。P1 未通过。**

## Training Loss (Gen 2)

| Epoch | Loss |
|-------|------|
| 0.2 | 0.206 |
| 1.0 | 0.200 |
| 2.0 | 0.129 |
| 3.0 | 0.097 |

模型确实在学习（loss 从 0.206 降到 0.097），但未导致 diversity collapse。

## 与之前实验对比

| Condition | K | Mode | LR | Vendi Change |
|-----------|---|------|-----|-------------|
| K=4 LoRA | 4 | LoRA | 2e-4 | -0.28% |
| K=8 LoRA | 8 | LoRA | 2e-4 | -0.03% |
| K=4 Full-FT | 4 | Full-FT | 5e-6 | +0.91% |
| K=4 Full-FT | 4 | Full-FT | 2e-5 | +0.68% |
| No-curation Full-FT | 1 | Full-FT | 5e-6 | +1.38% |
| No-curation Full-FT | 1 | Full-FT | 2e-5 | +0.047% |
| **K=16 Full-FT** | **16** | **Full-FT** | **2e-5** | **-0.19%** |

K=16 的 Vendi 下降幅度与 K=4 LoRA 相当（-0.19% vs -0.28%），均在噪声范围内。

## 结论

**结果: NEGATIVE（假设未验证）**

即使在 K=16 (6.25% retention) + Full-FT LR=2e-5 的极端条件下，3 代 iterative training 仍未触发可观测的 semantic collapse：
- Vendi Score 仅下降 0.19%，远低于 5% 阈值
- Self-BLEU 无上升趋势
- NN distance 微升（diversity 方向）
- Perplexity 持续下降说明模型在学习，但学到的不是趋同模式

**对论文 Claim 5 的影响**: 进一步强化 "quality-based curation does not cause semantic collapse" 的核心论点。在所有测试条件中（K=1/4/8/16, LoRA/Full-FT, LR=5e-6/2e-5），3 代内均未观察到 collapse。这表明 reward-based filtering 的 survival bias 不足以在短期 iterative training 中产生 mode collapse。

## Paths

- **Final checkpoint**: `/root/autodl-tmp/carr/outputs_fullft_lr2e5_k16/gen_2/condition_0/merged`
- **Results JSON**: `/root/autodl-tmp/carr/outputs_fullft_lr2e5_k16/fullft_lr2e5_k16_results.json`
- **Log**: `~/runs/collapse_aware_reward_rebalancing/carr_fullft_lr2e5_k16_probe_01.log`
- **Format diversity metrics**: 未记录（此实验未包含 opening_entropy/near_dup_start_rate）
