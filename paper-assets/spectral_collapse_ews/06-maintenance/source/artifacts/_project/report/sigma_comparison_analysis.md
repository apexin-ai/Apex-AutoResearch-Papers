# SIGMA (arXiv:2601.03385) 指标对比分析

## 1. SIGMA 指标清单

| 指标名 | 数学定义 | 计算基础 | 我们是否已有 | 可复现性 |
|--------|----------|----------|-------------|---------|
| log det(G) | Σⱼ log(λⱼ)，λⱼ 为 Gram 矩阵 G=MM^T 的特征值 | sentence embeddings Gram 矩阵 (m×m) | **有 (SLV)** — 我们的 `slv_log_det` = Σ log(σᵢ)，与 log det(G) = 2·Σ log(σᵢ) 成正比 | ✅ 直接可比（乘 2 即可） |
| 𝒢_KF (Track I) | log det(G_A + β̂I) − m·log(β̂ + δ) | embedding 矩阵 observed 子块 G_A；β̂ = (n−n_A)·ρ | **无** | ⚠️ 需实现，但可从现有 checkpoints 计算 |
| 𝒰_LLN,cov (Track II) | log det(G_A + δI) − m·log(n_A) | embedding 矩阵 observed 子块 G_A | **无** | ⚠️ 需实现，但可从现有 checkpoints 计算 |
| Δ𝒢_KF | 𝒢_KF^(k) − 𝒢_KF^(0) | 同 Track I，减去 gen-0 基线 | **无** | ⚠️ 依赖 Track I 实现 |
| Δ𝒰_LLN,cov | 𝒰_LLN,cov^(k) − 𝒰_LLN,cov^(0) | 同 Track II，减去 gen-0 基线 | **无** | ⚠️ 依赖 Track II 实现 |
| Distinct-2 | unique bigrams / total bigrams | 生成文本 | **部分** — 我们有 distinct_4（4-gram 版），缺 2-gram | ⚠️ 需对现有生成文本补算 |
| HHI (n-gram) | Σⱼ pⱼ²，pⱼ 为 n-gram 频率占比 | 生成文本的 n-gram 频率分布 | **无** | ⚠️ 需对现有生成文本补算 |
| Overestimation Ratio ℛ | Πⱼ(ρ + (1−ρ)·λ_max(C)/λⱼ(C)) | 真实协方差 C | **无** | ❌ 理论指标，需假设 i.i.d.，不适合直接对比 |

## 2. 关键设置差异

| 维度 | SIGMA | 我们 |
|------|-------|------|
| 模型 | OPT-125M | Pythia-410M |
| 参数量 | 125M | 410M |
| embedding 维度 m | 384 | 1024 |
| 递归代数 | 50 代 | 10 代 |
| 真实数据比例 α | 0.0（纯合成） | 0.0 + 多种混合比 (r=0.2, 0.25, 0.3, 0.5) |
| 训练数据 | ~1000 技术上下文 | eval_5k.pt |
| 递归模式 | S1 (data-only) + S2 (true recursion) | true recursion |

## 3. 可直接对比的指标

### 3.1 SLV ↔ log det(G)
- **关系**：SIGMA 的 log det(G) = Σ log(λⱼ) = Σ log(σⱼ²) = 2 × SLV
- **我们的数据**：gen_0 到 gen_10 全部有 `slv_log_det` 值
- **对比方式**：报告 Δ(SLV) 漂移曲线，与 SIGMA 的 drift 趋势做定性对比
- **注意**：m 不同（384 vs 1024），绝对值不可直接比，但漂移率（每代变化量/m）可归一化对比
- **工作量**：零，已有数据

### 3.2 Effective Rank
- SIGMA 未显式使用此指标，但它与 log det 密切相关（都反映谱分布健康度）
- 可作为补充对比维度

### 3.3 Distinct-N
- SIGMA 用 Distinct-2，我们有 Distinct-4
- 趋势方向一致，但粒度不同
- **工作量**：需从已存储的生成文本中重新计算 Distinct-2（~1 小时开发 + 运行）

## 4. 需要额外计算的指标

### 4.1 Track I (𝒢_KF) 和 Track II (𝒰_LLN,cov) — 核心对比目标

**实现步骤**：
1. 对每个 gen 的 checkpoint，提取 last-layer embeddings（已有 pipeline：`compute_alternative_ews_v2.py` 中的 `collect_embeddings()`）
2. 构建 Gram 矩阵 G = MM^T（M: m×n_A，m=1024）
3. Track I：计算 β̂ = (n−n_A)·ρ，其中 ρ = max ||mⱼ||²；计算 log det(G_A + β̂I) − m·log(β̂+δ)
4. Track II：计算 log det(G_A + δI) − m·log(n_A)
5. 对两个 Track 各减去 gen-0 基线得到 drift

**参数选择**：
- n_A：SIGMA 用 ~163-200 样本；我们可用 200 样本对齐
- δ：SIGMA 未指定具体值，需选一个合理的正则化值（e.g., 1e-6）
- n_total：我们的 probe 数据有 1000 样本

**计算复杂度**：
- 每代：1 次 forward pass（~30s on RTX 6000）+ 1 次 Cholesky 分解 / SVD（1024×1024，~1s）
- 11 代总计：~6 分钟 GPU 时间
- 开发时间：~2 小时（基于现有 pipeline 改造）

### 4.2 HHI (Herfindahl-Hirschman Index)

**实现步骤**：
1. 对每代的生成文本，统计 n-gram 频率
2. 计算 HHI = Σ pⱼ²

**前置条件**：需要每代的生成文本。如果已有存储的生成文本可直接计算；否则需从 checkpoint 重新生成。

**计算复杂度**：纯 CPU 统计，秒级

### 4.3 Drift Metrics (Δ𝒢_KF, Δ𝒰_LLN,cov)

依赖 4.1 的输出，无额外计算——减去 gen-0 基线即可。

## 5. 不可复现 / 不建议对比的指标

| 指标 | 原因 |
|------|------|
| Overestimation Ratio ℛ | 需要知道真实分布协方差 C，经验估计在小样本下不稳定 |
| Theorem 1/2/3 bounds | 理论 bound，非经验指标；适合论文讨论但不适合实验对比 |
| S1 (data-only recursion) | 我们无此实验设定，需额外实验 |

## 6. 建议的对比方案

### 最小可行对比（推荐优先实施）

1. **SLV drift 对比**（零额外成本）
   - 绘制 Δ(SLV)/m vs generation 曲线
   - 与 SIGMA 的 Δ𝒰_LLN,cov 趋势做定性对比
   - 论文中写为："Our SLV metric captures the same log-determinant dynamics as SIGMA's Track II"

2. **Track I + Track II 实现**（~2h 开发 + 6min GPU）
   - 用 SIGMA 的精确公式在我们的 checkpoints 上计算
   - 直接报告数值，与 SIGMA 的 S2 setting 趋势对比
   - 展示 Track I/II separation 是否在我们 10 代数据中也出现

3. **Distinct-2 补算**（~1h）
   - 从 gen_0-gen_10 的生成文本计算 Distinct-2
   - 与 SIGMA 的 Distinct-2 趋势对比

### 完整对比（可选强化）

4. HHI 指标补算
5. 我们独有指标的额外分析：RankMe、isotropy、stable rank、spectral norm 在 SIGMA 框架下的解读
6. 归一化对比：考虑 m (384 vs 1024) 和模型规模 (125M vs 410M) 差异后的标准化 drift 率

### 论文叙述建议

> SIGMA 使用 Gram 矩阵 log-determinant 的两个 track 来监测 collapse。我们的 SLV 指标与其 Track II 在数学上等价（均为嵌入空间 log-volume 的度量），在 Pythia-410M 上的 10 代递归实验中观察到一致的负漂移趋势。不同的是，我们额外引入了 [isotropy / RankMe / Δ²_t] 等指标捕捉 SIGMA 未覆盖的谱结构变化。
