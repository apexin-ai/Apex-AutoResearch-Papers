# Scorer 权重分析 · seed1 / acib_v5_div_reg / checkpoint-5000

**Run**: `acib_v5_div_reg`（seed sweep 标号 seed1，内部 `seed=42`），step 5000
**Checkpoint**: `/root/acib/outputs/acib_v5_div_reg/checkpoint-5000/checkpoint.pt`
**分析脚本**: `/root/acib/scripts/analyze_scorer.py`
**采样**: n_batches=4, batch_size=8 → 32 samples × 128 tokens（2 相机 × 64 tokens）

---

## 1. 分布类型判断

**结论：bimodal（强 U 型）**

| 指标 | 值 | 判断 |
|------|-----|------|
| Bimodality coefficient (Sarle) | **0.937** | 阈值 5/9≈0.556，远超 → bimodal |
| Excess kurtosis | −1.93 | 显著小于 0，平台型/双峰特征 |
| Skewness | −0.04 | 对称 |
| frac(w < 0.2) | **41.4%** | 双峰左侧聚集 |
| frac(w > 0.8) | **49.2%** | 双峰右侧聚集 |
| frac(0.4 ≤ w ≤ 0.6) | **1.5%** | 中间几乎清空 |

直方图 10 个 bin 占比（粗略形状）：

```
[0.0–0.1] 28.2% ███████████
[0.1–0.2] 13.2% █████
[0.2–0.3]  5.6% ██
[0.3–0.4]  2.1% █
[0.4–0.5]  1.1%
[0.5–0.6]  0.4%
[0.6–0.7]  0.1%
[0.7–0.8]  0.0%
[0.8–0.9]  0.0%
[0.9–1.0] 49.2% ████████████████████
```

> Logit 分布（pre-sigmoid）也佐证：mean=1.45, std=**3.76**, 范围 [−3.83, +6.06]。logit 高 std 说明 scorer 对 token 给出强烈、远离 0 的决策，sigmoid 把绝大多数 token 推到饱和区，这是 bimodality 的直接原因。

## 2. 关键统计量

```
weight: mean=0.5535  std=0.4399  median=0.4709  range=[0.0213, 0.9977]
logit:  mean=1.4524  std=3.7581  range=[-3.83, 6.06]

per-token (mean over 32 samples):
  top-10% tokens mean weight: 0.9944
  bottom-10% tokens mean weight: 0.0491
  ratio: 20.24×

per-sample (within each sample):
  top-10% tokens mean: 0.9949
  bottom-10% tokens mean: 0.0440
  ratio: 22.59×
```

`scorer_std=0.440`（任务描述的 0.445 与此吻合）反映的是 weight 分布两端聚集导致的高方差，不是均值附近的高熵。

## 3. Token importance 空间模式

**布局**: 128 tokens = 2 相机 × 64 tokens/相机，每相机重排为 **8×8 grid**（SmolVLA PixelShuffle=4）。

可用图（服务器路径，需查看 PNG）：
- 单 sample × 相机 heatmap：`/root/acib/outputs/scorer_analysis_seed1_step5000/token_importance_heatmap.png`
- 跨 32 sample 平均 heatmap（"哪些位置被持续重视"）：`/root/acib/outputs/scorer_analysis_seed1_step5000/avg_importance_per_camera.png`
- 全局 weight + logit 直方图：`/root/acib/outputs/scorer_analysis_seed1_step5000/scorer_weight_histogram.png`

**从统计量推断的空间模式**（未直接 OCR heatmap，需人工核对图像确认）：

- `per_token_top10/bottom10 = 20.24`、`within_sample = 22.59`。两者接近 → token importance 在样本间相对稳定，scorer 学到的是**位置/区域结构**而非每帧重判一次。
- top-10 tokens 平均权重 0.994 → 它们几乎总是"开"；bottom-10 平均 0.049 → 几乎总是"关"。
- 这意味着 8×8 grid 上大部分位置已经形成"恒亮"或"恒灭"的两类，少数 token 处于过渡带（参见 frac middle 1.5%）。

**Task-relevance 核对清单（依赖 heatmap 查看）**：
- third-person 相机：高权位置应集中在桌面、物体、机械臂工作区，而非天花板/背景墙
- wrist 相机：高权位置应跟随末端执行器视场内的物体
- 若热区出现在图像四角/纯背景 → scorer 学到的是任务无关的位置先验

## 4. 与之前版本对比

| 版本 | reg 项 | scorer_std | 分布 | 备注 |
|------|--------|-----------|------|------|
| v4 `acib_v4_agg_kl` | agg_kl only | 0.135 → **0.009** (collapse) | gaussian 压扁到均值附近 | scorer 失去判别力 |
| v5 `stopgrad_entropy` | stopgrad + 熵 | scorer 输出 → **0** | trivial collapse（全零） | 退化方向相反 |
| **v5 `div_reg`（当前）** | diversity_lambda=0.1 | **0.440** | **bimodal (BC=0.937)** | 健康双峰，token 区分度强 |

`diversity_lambda` 项有效解决了前两版的 collapse：
- v4 的 agg_kl 把所有 token 推向同一均值（std → 0）
- v5_stopgrad 把所有 token 推向 0（trivial）
- v5_div_reg 通过 diversity 正则把 token 分成两类，得到 U 型分布——这正是 "informational bottleneck via gating" 的理想形态：scorer 在做近似 hard selection，同时保持端到端可导

## 5. MVP 判断建议

**PASS（脚本自动判定一致）**

理由：
1. 分布是清晰 bimodal（BC=0.937，>> 阈值 0.556）
2. within-sample top10/bottom10 ratio = 22.59，远超阈值 3
3. 两端各占 ~40-50%，中间死区（<1.5% 在 0.4-0.6），逼近 hard gating
4. 相对 v4/v5_stopgrad 的 collapse，diversity 正则把 scorer 从两种退化基底救回到判别状态

**遗留风险（在判 PASS 前需人工核对 heatmap PNG）**：
- 空间分布若聚集在背景/边角而非任务区域，bimodality 也可能是"学到 position prior"而非 task-conditioned selection。脚本无法自动判断这一点。
- per-token vs within-sample ratio 几乎相等（20.24 vs 22.59），说明高权 token 在样本间高度一致。如果热图证实位置在物体区，是好信号；如果在固定背景区，反而提示 condition（language）未被有效利用。

**建议下一步**：
1. 查看 `token_importance_heatmap.png` 和 `avg_importance_per_camera.png`，确认热区落在桌面/手臂/物体而非背景
2. （可选）对另一 task 的 prompt 重跑一次，看 heatmap 是否随 language 条件移动 → 若不变则 condition 在 scorer 里被忽略，需检查 condition_source / stop_grad_task

---

## 附：脚本说明

`/root/acib/scripts/analyze_scorer.py`：
- 加载 `checkpoint.pt`，用 `ACIBPolicy.from_pretrained` 重建 policy + scorer，`load_state_dict(strict=False)`
- forward 走 `policy(batch)`，触发 scorer 缓存 `policy._cached_logits`（acib_policy.py 内置 hook，见 line 18/45/51/53）
- 聚合 4 batch × 8 samples = 32 samples，输出权重/logit 统计 + heatmap + JSON
- 内置 MVP 启发式 verdict：bimodal+ratio>3 → PASS
- 输出 JSON: `/root/acib/outputs/scorer_analysis_seed1_step5000/scorer_analysis.json`
