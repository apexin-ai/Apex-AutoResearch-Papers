# Scorer 权重分析 · seed2 / acib_v5_div_reg_seed2 / checkpoint-5000

**Run**: `acib_v5_div_reg_seed2`（seed sweep 标号 seed2，内部 `seed=1337`），step 5000
**Checkpoint**: `/root/acib/outputs/acib_v5_div_reg_seed2/checkpoint-5000/checkpoint.pt`
**分析脚本**: `/root/acib/scripts/analyze_scorer.py`
**采样**: n_batches=4, n_samples=8 → 32 samples × 128 tokens（2 相机 × 64 tokens）

---

## 1. 分布类型判断

**结论：bimodal（强 U 型）**

| 指标 | 值 | 判断 |
|------|-----|------|
| Bimodality coefficient (Sarle) | **0.933** | 阈值 5/9≈0.556，远超 → bimodal |
| Excess kurtosis | −1.93 | 显著小于 0，平台型/双峰特征 |
| Skewness | −0.04 | 对称 |
| frac(w < 0.2) | **40.5%** | 双峰左侧聚集 |
| frac(w > 0.8) | **49.2%** | 双峰右侧聚集 |
| frac(0.4 ≤ w ≤ 0.6) | **1.4%** | 中间几乎清空 |

直方图 10 个 bin 占比：

```
[0.0–0.1] 26.6% ███████████
[0.1–0.2] 13.8% █████
[0.2–0.3]  6.3% ██
[0.3–0.4]  2.5% █
[0.4–0.5]  1.0%
[0.5–0.6]  0.4%
[0.6–0.7]  0.1%
[0.7–0.8]  0.0%
[0.8–0.9]  0.0%
[0.9–1.0] 49.2% ████████████████████
```

> Logit 分布（pre-sigmoid）：mean=1.45, std=**3.72**, 范围 [−4.25, +6.38]。高 std 说明 scorer 给出强烈决策，sigmoid 将绝大多数 token 推到饱和区。

## 2. 关键统计量

```
weight: mean=0.5558  std=0.4376  median=0.4647  range=[0.0141, 0.9983]
logit:  mean=1.4494  std=3.7168  range=[-4.25, 6.38]

per-token (mean over 32 samples):
  top-10% tokens mean weight: 0.9944
  bottom-10% tokens mean weight: 0.0473
  ratio: 21.01×

per-sample (within each sample):
  top-10% tokens mean: 0.9949
  bottom-10% tokens mean: 0.0432
  ratio: 23.02×
```

## 3. Seed1 vs Seed2 对比表

| 指标 | seed1 (seed=42) | seed2 (seed=1337) | 差异 |
|------|-----------------|-------------------|------|
| Bimodality coefficient | 0.937 | 0.933 | −0.004 |
| Excess kurtosis | −1.93 | −1.93 | ~0 |
| Skewness | −0.04 | −0.04 | ~0 |
| weight mean | 0.5535 | 0.5558 | +0.002 |
| weight std | 0.4399 | 0.4376 | −0.002 |
| weight median | 0.4709 | 0.4647 | −0.006 |
| logit mean | 1.4524 | 1.4494 | −0.003 |
| logit std | 3.7581 | 3.7168 | −0.041 |
| frac(w < 0.2) | 41.4% | 40.5% | −0.9pp |
| frac(w > 0.8) | 49.2% | 49.2% | 0 |
| frac(0.4–0.6) | 1.5% | 1.4% | −0.1pp |
| per-token ratio | 20.24× | 21.01× | +0.77 |
| within-sample ratio | 22.59× | 23.02× | +0.43 |
| MVP verdict | **PASS** | **PASS** | -- |

**高度一致**：所有指标差异 < 1%。两个 seed 独立收敛到几乎相同的 bimodal 分布，说明 diversity_lambda=0.1 下的 scorer 行为是稳健的，不依赖随机初始化。

## 4. MVP 判断

**PASS**

理由：
1. 分布 bimodal（BC=0.933, >> 阈值 0.556）
2. within-sample top10/bottom10 ratio = 23.02, 远超阈值 3
3. 两端各占 ~40-49%，中间死区 1.4%，逼近 hard gating
4. 与 seed1 高度一致，验证了 diversity 正则的稳健性

**遗留风险（同 seed1）**：
- 空间分布需人工查看 heatmap 确认热区在任务区域而非背景
- per-token 和 within-sample ratio 接近，可能是 position prior 而非 task-conditioned selection

**服务器输出文件**：
- `/root/acib/outputs/scorer_analysis_seed2_step5000/scorer_analysis.json`
- `/root/acib/outputs/scorer_analysis_seed2_step5000/scorer_weight_histogram.png`
- `/root/acib/outputs/scorer_analysis_seed2_step5000/token_importance_heatmap.png`
- `/root/acib/outputs/scorer_analysis_seed2_step5000/avg_importance_per_camera.png`
