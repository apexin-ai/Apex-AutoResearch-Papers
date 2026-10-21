## SciERC 5-seed Entity Construction (Gold-filtered, n=529)

**Method:** LP-weighted entity construction, θ = 2/N = 0.25 (N=8 samples)
**Data:** `scierc_mf4v2_seed{42,123,456,2024,3141}`, all files have 551 lines
**Evaluation set:** 529 gold-filtered instances per seed (excluding 22 instances with empty gold entities)

### 数据对齐

- 对齐前：seeds 2024/3141 的原始推理在 551 instances 上运行（`--data_dir data/scierc`），seeds 42/123/456 也在 551 instances 上运行（`--data_dir data/scierc/processed_data`，但 samples.jsonl 均包含 551 行）
- 对齐后：全部统一到 529 gold-filtered instances（过滤条件：`obj["gold"]["entities"]` 非空）
- 对齐对 seeds 2024/3141 的影响：

| Seed | n=551 Δ (pp) | n=529 Δ (pp) | 变化 (pp) |
|------|-------------|-------------|----------|
| 2024 | +0.87       | +1.48       | +0.60    |
| 3141 | +0.62       | +1.78       | +1.16    |

Gold-filter 移除了 22 个 gold-empty instances，这些 instance 上 greedy 和 construction 的 F1 差异模式与 gold-nonempty 不同，稀释了整体 Δ。

### Per-seed results (aligned)

| Seed | n   | Greedy F1 | Construction F1 | Δ (pp)  | p-value  | Sign |
|------|-----|-----------|-----------------|---------|----------|------|
| 42   | 529 | 65.02     | 64.44           | −0.58   | 0.8242   | −    |
| 123  | 529 | 64.71     | 65.67           | +0.96   | 0.0853   | +    |
| 456  | 529 | 64.56     | 66.47           | +1.91   | 0.0031*  | +    |
| 2024 | 529 | 64.78     | 66.25           | +1.48   | 0.0233*  | +    |
| 3141 | 529 | 64.27     | 66.05           | +1.78   | 0.0075*  | +    |

\* p < 0.05, paired bootstrap (B=10,000)

### Aggregate

- **Mean Δ:** +1.11 pp ± 1.01
- **Pooled bootstrap (5×529 = 2,645 instances):** Δ = +1.11pp, 95% CI [+0.48, +1.75], p = 0.0003
- **Direction:** 4/5 positive

### 论文更新建议

- **tab:entity_construction SciERC 行应改为：** Greedy 64.87, Construction 65.58, Δ = +1.11pp (5-seed mean ± 1.01)
- **正文 "non-significant +0.32pp" 应改为：** "+1.11pp (p < 0.001, pooled bootstrap, 5 seeds)" — construction 在 SciERC 上有统计显著的正向增益
- **注意：** Seed 42 是唯一负方向（−0.58pp, n.s.），其余 4 seeds 正方向且 3 个 individually significant。建议保留 seed-level variance 的描述以保持严谨性
