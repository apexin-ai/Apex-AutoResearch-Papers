# d003_reasoning_traces 实验分析

## 实验配置
- **模型**: DeepSeek-R1-Distill-Qwen-14B
- **数据**: MATH reasoning traces (20 traces)
- **总 tokens**: 30,063 (prefill 24,050 + eval 6,013)
- **Budget ratio**: 0.5 (cache budget = 12,025)
- **Grace window**: 175

## 结果

| Strategy | PPL | vs Full (%) | vs Random (%) | Elapsed (s) |
|----------|-----|-------------|---------------|-------------|
| full | 1.2120 | — | -1.23% | 216.0 |
| recency | 1.2170 | +0.41% | -0.82% | 229.3 |
| random | 1.2271 | +1.25% | — | 229.1 |
| ema_0.9 | 1.2522 | +3.32% | +2.04% | 1180.7 |
| ema_0.7 | 1.2706 | +4.83% | +3.54% | 1178.1 |
| ema_0.5 | 1.2780 | +5.45% | +4.15% | 1179.3 |

## 关键发现

1. **Sanity check: FAIL** — EMA eviction 未能优于 random eviction，反而显著更差
   - Best EMA (γ=0.9) PPL=1.2522 vs Random PPL=1.2271，EMA 差 2.04%
   - 成功标准要求 EMA 优于 random ≥ 5%，实际 EMA 劣于 random 2.04%

2. **Recency eviction 表现最佳** — PPL=1.217，仅比 full cache 差 0.41%，优于 random 0.82%

3. **EMA γ 越大越好** — γ=0.9 > 0.7 > 0.5，但即便最优 γ 也不如 random

4. **与 WikiText-2 实验一致** — 两个数据集上 EMA 均劣于 random：
   - WikiText-2: EMA vs random = -1.77%（EMA 更差）
   - Reasoning traces: EMA vs random = -2.04%（EMA 更差）

5. **EMA eviction 速度极慢** — EMA 策略耗时 ~1180s vs random/recency ~229s（约 5x 慢），因为需要逐 token 更新 score

## 对比前序实验 (d003_wikitext_32k)

| 指标 | WikiText-2 32K | Reasoning Traces |
|------|---------------|-----------------|
| ppl_full | 7.18 | 1.212 |
| ppl_ema_0.9 | 7.78 | 1.2522 |
| ppl_random | 7.64 | 1.2271 |
| ppl_recency | 7.18 | 1.217 |
| EMA vs random | -1.77% | -2.04% |
| recency vs full | +0.00% | +0.41% |

两个数据集一致表明：EMA attention score 不是有效的 token 重要性指标。

## 结论

EMA-based O(1) KV cache eviction 在两个不同类型的数据集上均未通过 sanity check。EMA score 作为 token 重要性指标的基本假设不成立——它不能有效区分应保留和应驱逐的 KV cache entries。

Recency（保留最近的 tokens）是更强的 baseline，在 reasoning traces 上几乎无损（+0.41% PPL）。这暗示 reasoning traces 的注意力模式高度局部化，远处 token 的重要性衰减很快。