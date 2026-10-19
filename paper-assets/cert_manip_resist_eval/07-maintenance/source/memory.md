# Memory — cert_manip_resist_eval

## 方法论验证

### Plug-in MI vs Closed-form K_eff (2026-05-24)
- 两种 K_eff 计算方式排序高度一致：within-K rank Spearman ~0.86
- 系统性偏移：closed-form K_eff 偏高（mean 4.29 vs plug-in 3.38）
  - 原因：plug-in MI 的 Miller-Madow 校正增大 MI → exp(-2·MI) 更小 → K_eff 更低
- Overall r=0.97 受跨 K 值分布拉伸影响，within-K 真实一致性 0.86-0.87
- element-wise |exp(-2·MI) - (1-ρ²)| 均值 0.22：Gaussian copula 近似引入中等偏差但不影响排序
- **结论**：closed-form 近似对论文中排序类 claim 有效，但绝对值不可直接比较

### κ-diversity vs K_eff 对比 (2026-05-25)
- κ-diversity（pairwise Cohen's kappa 均值）与 K_eff rank ρ > 0.985，但 FDR 显著性模式完全相反
- κ-diversity: 8→7→6（随 K 递减），K_eff: 3→7→8（随 K 递增）
- **结论**：predictor shift 是 K_eff 的 MI-based 公式独有，κ-diversity 无法复制
- **Director 判断**：ρ=0.986 下声称 "K_eff 捕捉独特结构" 在 peer review 中太脆弱。不用于 rebuttal 核心论点

### MC 校准 (2026-05-25)
- WCB 在所有 36 条件下不 over-reject（1000 perms × 999 bootstrap）
- 最坏 rejection rate 1.6%（K=3），远低于 α=0.05
- **结论**：WCB 检验保守可信，论文显著性结果非 type-I error inflation

### 合成数据验证 (2026-05-25)
- DGP: 15 models, vulnerability ~ Beta(2,5), MI confounding correlated with vulnerability
- Scenario A (true shift, β=-0.008): rejection rate 13.5%→61%→52.5%（power peaks at K=5, K=7 回落因 cluster 数 13→9）
- Scenario B (null): rejection rate 1%→0%→0%（无 shift 模式）
- **结论**：shift 不是 artifact，但 K=7 显著性增加靠样本量弥补功效下降，非效应量增大
- 支持 Director 判断：聚焦 uniform positive + η_max decline，不以 predictor shift 为核心

### η_max 衰减 metric-agnostic (2026-05-25)
- η_max β_std under κ-diversity: 0.190→0.104→0.075（单调衰减 -60%）
- η_max β_std under K_eff: 0.266→0.101→0.084（单调衰减 -68%）
- **结论**：η_max 效应随 K 稀释是 robust finding，不依赖 diversity metric 选择

### Fractional Logit V1→V2 数据修正 (2026-05-25, 2026-05-26 updated)
- V1 registry 记录（已废弃）：K_eff sig 4/12, 9/12, 10/12
- V2 JSON ground truth (`frac_logit_clustered`):
  - K_eff sig: **9/12, 11/12, 12/12**（upward shift）
  - η_max sig: **6/12, 4/12, 4/12**（downward shift, 强化 "η_max K≥5 不显著" 叙事）
- V2 JSON 其他变体：`frac_logit` basic = 2/7/7, `frac_logit_robust_HC1` = 12/12/12
- ⚠️ 旧版 memory 错误记录 "9/9/9 无 shift"——已修正
- ⚠️ 旧版论文 η_max sig (FL) 使用了 robust_HC1 值 (8/8/6) 而非 clustered (6/4/4)——已修正 (2026-05-26)
- Direction concordance (JSON): K_eff 36/36, η_max 35/36 → 71/72 = 98.6%

### Bayesian 非单调性解释 (2026-05-25)
- 后验集中 ratio 单调递减 0.890→0.874→0.867（大 K 时权重集中于高准确率评委）
- K_eff CV 压缩 0.157→0.148→0.131（大 K 时预测变量 range 窄）
- 双重压缩在 K=7 削弱 K_eff 统计功效，K=5 是甜蜜点

## 决策与约束

### Temperature 不是有效 IV (2026-05-23)
- Temperature 0→1 改变 K_eff < 0.03，accuracy < 1%
- 不能用 temperature 作为 K_eff 的工具变量

### V2 数据定稿 (2026-05-24)
- 废弃 regime_transition_corrected.json（不可审计）
- K=5 K_eff: 10→7, K=7 K_eff: 9→8, K=5 η_max: 0→2
- 所有数据来自可审计 V2 脚本（seed=42, _is_valid_score）

### 论文数据审计修正 (2026-05-26 updated)
- Adaptive R²: 论文写 0.275，正确值 0.256（来自 registry k5_rf_contrast）
- Fractional logit 全部对齐 `frac_logit_clustered` JSON ground truth：
  - K_eff sig: 9/12, 11/12, 12/12（论文已修正）
  - η_max sig: 6/12, 4/12, 4/12（论文已修正）
  - Direction concordance: 71/72 = 98.6%（论文已修正）

### 论文叙事方向 (Director 指令 2026-05-25)
- predictor shift 不作为核心贡献（太脆弱：κ-div 反向 + β_std 非单调）
- 聚焦：uniform positive direction + η_max monotonic decline + aggregation gradient
- 不在 rebuttal 中使用 "K_eff 独特性" 论点

### K_eff-η_max 固有共线性 (2026-05-25)
- 合成数据确认 corr(K_eff, η_max) ≈ -0.68 是 panel 结构固有属性，非数据异常
