# MMCT v2 — α=0.10 fp32 双 seed 置换检验结果

Generated: 2026-05-19
Data: fp32 training (bf16=false), Pythia-410M, WikiText-103, 11 generations

## 1. 数据来源

| Condition | Server | Path | Seed | Precision |
|-----------|--------|------|------|-----------|
| a010_s42_fp32 | westd-17855 | results/alpha_sweep/a010_s42_fp32/ | 42 | fp32 |
| a010_s43_fp32 | westd-17855 | results/alpha_sweep/a010_s43_fp32/ | 43 | fp32 |

Null distribution: a000_s42/s43/s44 (westd-19828), 3 seeds, n_bootstrap=10000

## 2. Unified 5-Method Raw Counts (pre-MMCT)

| Condition | Naive | Diff | Thresh | PermG | TY | K>=4 |
|-----------|-------|------|--------|-------|----|------|
| a010_s42_fp32 | 8/8 | 6/8 | 3/8 | 2/8 | 1/8 | 2/8 |
| a010_s43_fp32 | 8/8 | 8/8 | 3/8 | 3/8 | 0/8 | 3/8 |

TY excluded per C003 (α<=0.50 seed-unstable).

## 3. MMCT v2 Results (p<0.05)

### Summary Table

| Mode | s42_fp32 | s43_fp32 | Cross-seed stable? |
|------|----------|----------|--------------------|
| uniform_forward | 0/8 | 0/8 | YES |
| uniform_bidirectional | 0/8 | 0/8 | YES |
| **weighted_pair_forward** | **2/8** | **4/8** | NO |
| weighted_pair_bidirectional | 2/8 | 4/8 | NO |
| weighted_global_forward | 0/8 | 0/8 | YES |
| weighted_global_bidirectional | 0/8 | 0/8 | YES |

### Per-Pair Detail: weighted_pair_forward

#### a010_s42_fp32 (2/8 sig)

| Canary | Downstream | Score | p-value | Sig |
|--------|------------|-------|---------|-----|
| token_entropy | distinct_1 | 0.9718 | 0.0400 | **YES** |
| token_entropy | distinct_2 | 0.0566 | 0.0800 | no |
| token_entropy | distinct_3 | 0.0287 | 0.3600 | no |
| token_entropy | perplexity | 0.0066 | 0.6400 | no |
| ece | distinct_1 | 0.0193 | 0.5200 | no |
| ece | distinct_2 | 0.2519 | 0.0400 | **YES** |
| ece | distinct_3 | 0.0193 | 0.5200 | no |
| ece | perplexity | 0.0037 | 0.8400 | no |

#### a010_s43_fp32 (4/8 sig)

| Canary | Downstream | Score | p-value | Sig |
|--------|------------|-------|---------|-----|
| token_entropy | distinct_1 | 0.9718 | 0.0400 | **YES** |
| token_entropy | distinct_2 | 0.0566 | 0.0800 | no |
| token_entropy | distinct_3 | 0.0431 | 0.2000 | no |
| token_entropy | perplexity | 0.0066 | 0.6400 | no |
| ece | distinct_1 | 0.0193 | 0.5200 | no |
| ece | distinct_2 | 0.2519 | 0.0400 | **YES** |
| ece | distinct_3 | 0.4879 | 0.0400 | **YES** |
| ece | perplexity | 0.2528 | 0.0400 | **YES** |

### Per-Pair Detail: uniform_forward (representative conservative mode)

#### a010_s42_fp32 (0/8 sig)

| Canary | Downstream | Score | p-value | Sig |
|--------|------------|-------|---------|-----|
| token_entropy | distinct_1 | 4.0000 | 0.1600 | no |
| token_entropy | distinct_2 | 4.0000 | 0.1600 | no |
| token_entropy | distinct_3 | 3.0000 | 0.4400 | no |
| token_entropy | perplexity | 2.0000 | 0.6400 | no |
| ece | distinct_1 | 2.0000 | 0.6400 | no |
| ece | distinct_2 | 2.0000 | 0.6400 | no |
| ece | distinct_3 | 2.0000 | 0.6400 | no |
| ece | perplexity | 1.0000 | 0.9600 | no |

#### a010_s43_fp32 (0/8 sig)

| Canary | Downstream | Score | p-value | Sig |
|--------|------------|-------|---------|-----|
| token_entropy | distinct_1 | 4.0000 | 0.1600 | no |
| token_entropy | distinct_2 | 4.0000 | 0.1600 | no |
| token_entropy | distinct_3 | 4.0000 | 0.1600 | no |
| token_entropy | perplexity | 2.0000 | 0.6400 | no |
| ece | distinct_1 | 2.0000 | 0.6400 | no |
| ece | distinct_2 | 2.0000 | 0.6400 | no |
| ece | distinct_3 | 2.0000 | 0.6400 | no |
| ece | perplexity | 2.0000 | 0.6400 | no |

## 4. 与 pre-D080 a010_s42 对比

| Mode | old a010_s42 (bf16?) | fp32 s42 | fp32 s43 |
|------|---------------------|----------|----------|
| uniform_forward | 0/8 | 0/8 | 0/8 |
| weighted_pair_forward | 1/8 | 2/8 | 4/8 |
| weighted_global_forward | 0/8 | 0/8 | 0/8 |

- uniform/wglobal: 一致 0/8，bf16→fp32 无变化
- wpair: old 1/8 → fp32 s42 2/8 / s43 4/8，但跨 seed 不稳定 (2 vs 4)，不可靠

## 5. 结论

**α=0.10 fp32 权威 MMCT v2 值：**

| 推荐引用 mode | 结果 | 跨 seed 一致性 |
|---------------|------|----------------|
| uniform_forward | **0/8** | 2/2 seeds 一致 |
| weighted_global_forward | **0/8** | 2/2 seeds 一致 |
| weighted_pair_forward | 2-4/8 | **不一致** (seed-dependent) |

**结论：** α=0.10 在稳健的 MMCT 模式 (uniform, weighted_global) 下为 **0/8**，符合预期（低污染率下不可检测）。weighted_pair 模式出现 2-4/8 信号但跨 seed 不稳定，原因是 3 个 null seed 导致 per-pair FPR 权重估计方差大。论文中应以 uniform_forward 或 weighted_global_forward 的 0/8 为权威值。

wpair 不稳定的根因：只有 3 个 null seeds (a000_s42/43/44)，per-pair FPR 权重的分母极小，单个 pair 的 null 显著性翻转就会大幅改变权重，导致 wpair 分数在不同 test seed 下差异显著。相比之下 weighted_global 池化所有 pair 的 FPR 后权重更稳定。

JSON 详细数据: `westd-19828:/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results/mmct_v2_a010_fp32.json`
