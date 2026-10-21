# Memory — schema_semantic_constrained_ie

## 70B LoRA S2 过度约束 ⚠️ (2026-05-22)

70B LoRA SciERC full_s2: DR=0% 但 R-F1 暴跌到 36.28（vs S1 44.53, -8.45pp），E-F1 也降到 62.35。S2 在 70B 上过度约束导致 recall 大幅下降。论文不应 claim S2 在 70B 上有效。

## 70B LoRA 五路消融完整 Pattern (2026-05-22)

| Config | DR% | R-F1 |
|--------|-----|------|
| Unc | 1.5 | 44.73 |
| Grammar | 1.5 | 44.63 |
| Semantic | 0.6 | 44.73 |
| S1 | 0 | 44.53 |
| Beam4 S1 | 0 | 44.81 |
| S2 | 0 | 36.28 ⚠️ |

Grammar 零贡献、semantic 主力（与 ZS pattern 一致）、S2 过度约束、beam 最优。

## Entity Order: 完全 Order-Invariant ✅ (2026-05-22, corrected)

Fair comparison 确认：shuffled 和 original 输出逐字节一致。OntoCoDec 完全 order-invariant。教训：对比实验必须用同一版本评估工具。

## 70B ZS 消融：Scale-Dependent Layer Contribution (2026-05-22)

70B ZS 上 grammar-only 对 DR 几乎无贡献（6.41→6.33%），semantic layer 是 DR 主力（→1.01%，84%）。与 8B 不同。Grammar 价值随模型能力递减，semantic 恒定。

## TCR + Beam Search 发现 (2026-05-22)

TCR beam4 Qwen/Llama 均确认：beam candidates 已 type-consistent（TCR score 全 1.0），TCR 冗余。价值仅限 greedy。

## 70B LoRA Beam4 S1 SciERC (2026-05-22)

R-F1 44.81 (+0.28pp vs greedy S1), DR=0%, CF=1 (vs CF=15)。

## vLLM guided_json = GCD (2026-05-22)

等价于 grammar-only ablation。DR≈15%, RV=0%, ET=0%。

## Bootstrap 交叉验证 (2026-05-22)

SciERC 0.00pp，DocRED 0.04-0.11pp。Registry 值为权威。

## Lucky violations (2026-05-22)

TP 中 DR violation：SciERC 0.42%, DocRED Qwen 0.02%, Llama 1.07%。绝大多数 FP。

## 70B LoRA DocRED 200-doc (2026-05-22)

DR→0%, R-F1 43.95 (+0.15pp)。Scale-independent composability confirmed。

## 高-κ 关系 (2026-05-22)

SciERC α≥0.67，DocRED 12/96 α≥0.36 (3.8% gold)。高-κ≠低性能。

## WikiEvents Power (2026-05-22)

n=20 CI ±3.0pp, MDE 2.0pp, RoV power≈1.0。
