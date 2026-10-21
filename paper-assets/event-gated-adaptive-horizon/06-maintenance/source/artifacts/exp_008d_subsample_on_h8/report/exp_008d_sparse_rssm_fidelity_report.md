# exp_008d (s1) 稀疏 RSSM Fidelity 跨 Seed 验证

## 目标
用 exp_008d (seed=1, Walker Walk, trained dt_emb, 55K steps) 验证 exp_066 (seed=0) 发现的 "fidelity gap precedes VE" 时序因果模式。

## Checkpoint 限制
**exp_008d 仅有 `latest.pt` (step 55K)，无中间 checkpoint。** 无法做计划中的 25K vs 75K 两点对比。
- 原因：实验在 55K 步停止，且未设置 checkpoint_every
- 替代策略：使用 exp_063 已有的 55K fidelity 数据 + exp_066 (s0) 完整时序作对比

## 数据来源
1. **exp_066 (s0)**: 完整时序 fidelity 分析（10K-65K，每 5K 一个 checkpoint），来自 `timeseries_analysis_v2.json`
2. **exp_063**: exp_008d (s1) 在 55K 的 fidelity 分析，来自 `results.json`
3. **exp_008d metrics.jsonl**: VE ratio 轨迹

## 结果

### 1. exp_066 (s0) 时序因果关系（已确认）

| Step | SS ratio (dt2/dt1) | OL ratio (dt2/dt1) | VE ratio | 解读 |
|------|-------------------|--------------------|---------:|------|
| 10K  | 1.047             | 0.937              | 0.005 | 无 gap, 无 VE |
| 15K  | 1.077             | 1.027              | 0.022 | 微弱 gap, 无 VE |
| 20K  | 1.104             | 1.092              | 0.156 | gap 出现, VE 仍低 |
| **25K** | **1.041**       | **1.218**          | **0.163** | **OL gap 22%, VE 仍低 → gap precedes VE** |
| 30K  | 1.247             | 1.446              | 0.215 | gap 增长, VE 仍低 |
| 35K  | 1.243             | 1.509              | 0.229 | gap 稳定高, VE 仍低 |
| **40K** | **1.350**       | **1.378**          | **1.591** | **VE spike! gap 早于 VE 15K 步** |
| 45K  | 1.398             | 1.382              | 0.360 | VE 暂回落 |
| 50K  | 1.466             | 1.556              | 0.616 | gap 持续增大 |
| 55K  | 1.373             | 1.515              | 0.621 | |
| 60K  | 1.610             | 1.348              | 1.399 | VE 再次 spike |
| 65K  | 1.678             | 1.384              | 1.399 | gap 最大, VE 持续高 |

**因果方向确认**：OL fidelity gap 在 25K 已达 1.22x，而 VE ratio 仅 0.16。VE 首次 spike 在 40K (1.59)，滞后 fidelity gap 出现 ~15K 步。

### 2. exp_008d (s1) 55K 截面数据

来自 exp_063 分析：

| Metric | dt=1 | dt=2 (single) | dt=2/dt=1 ratio |
|--------|------|---------------|----------------:|
| Single-step reward MAE | 0.0543 | 0.1464 | **2.695x** |
| Single-step obs MSE | 26.93 | 42.02 | **1.560x** |
| Chained (2×dt=1) reward MAE | 0.0543 | 0.0760 | 1.399x |

同时间点 VE ratio: **1.666** (value_mean=137.88, eval_return=82.75)

### 3. 跨 Seed 对比 (55K 时间点)

| Metric | exp_066 (s0) @ 55K | exp_008d (s1) @ 55K | 比较 |
|--------|-------------------|--------------------:|------|
| SS fidelity ratio | 1.373x | **2.695x** | s1 gap 是 s0 的 1.96 倍 |
| OL fidelity ratio | 1.515x | N/A (exp_063 未做 OL) | — |
| VE ratio | 0.621 | **1.666** | s1 VE 是 s0 的 2.68 倍 |
| eval_return | ~60.8 | 82.7 | |

**关键发现**：s1 的 fidelity gap 更严重（2.7x vs 1.4x），VE 也更严重（1.67 vs 0.62），两者正相关。

### 4. exp_008d VE 轨迹

| Step | value_mean | eval_return | VE ratio | 状态 |
|------|-----------|-------------|--------:|------|
| 5K   | 0.001     | 31.0        | ~0      | 正常 |
| 15K  | 3.37      | 153.7       | 0.022   | 正常 |
| 25K  | 25.94     | 167.2       | 0.155   | VE 低 |
| 35K  | 60.11     | 146.3       | 0.411   | VE 开始上升, eval 开始下降 |
| 45K  | 97.53     | 140.8       | 0.693   | VE 加速 |
| 55K  | 137.88    | 82.7        | 1.666   | 完全 collapse |

VE 轨迹与 exp_066 (s0) 一致：25K 处 VE 低（0.155 vs 0.163），然后逐步恶化。

## 结论

### 支持 "fidelity gap early, VE late" 的证据

1. **直接证据 (s0)**：exp_066 完整时序确认 fidelity gap 在 25K 已存在（OL 1.22x），VE 在 40K 才首次 spike（1.59x），滞后 ~15K 步。

2. **跨 seed 一致性 (s1)**：
   - exp_008d 在 55K 有更大的 fidelity gap（2.7x vs s0 的 1.4x）
   - 对应更严重的 VE（1.67 vs s0 的 0.62）
   - VE 轨迹模式一致：25K 处 VE 低（0.155），35-55K 快速恶化
   - **更大的 fidelity gap 对应更严重的 VE**，符合因果方向预测

3. **局限**：
   - exp_008d 无 25K checkpoint，不能直接验证该 seed 25K 处的 fidelity gap
   - 跨 seed 的定量比较受到不同训练动态的影响
   - 因果方向的直接时序证据仅来自 s0（exp_066）

### 总结
跨 seed 数据**支持**但不能**独立确认**时序因果方向。s0 的完整时序加上 s1 的截面强相关（更大 gap → 更大 VE），共同支持 "fidelity gap drives VE" 的因果假说。
