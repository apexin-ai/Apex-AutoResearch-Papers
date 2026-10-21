# Pythia-1.4B effective_rank +62% 异常分析

## 数据来源

| 实验 | 路径 | 模型 | α | seed |
|------|------|------|---|------|
| **主分析对象** | `scale_check/pythia14b_a050_s42` | Pythia-1.4B | 0.50 | 42 |
| 410M 对比 | `alpha_sweep/a050_s42` | Pythia-410M | 0.50 | 42 |
| 1.4B α=1.00 参考 | `generalize/pythia14b_wiki_a100_s42` | Pythia-1.4B | 1.00 | 42 |
| 1.4B α=1.00 s43 | `generalize/pythia14b_wiki_a100_s43` | Pythia-1.4B | 1.00 | 43 |

---

## 逐代数据表

### Pythia-1.4B, α=0.50, seed 42 (scale_check)

| Gen | eff_rank | token_entropy | distinct_1 | distinct_2 | distinct_3 | perplexity |
|-----|----------|---------------|------------|------------|------------|------------|
| 0   | 50.76    | 2.946         | 0.0993     | 0.5208     | 0.8129     | 19.68      |
| 1   | 75.55    | 2.134         | 0.0998     | 0.5205     | 0.8072     | 20.71      |
| 2   | 82.63    | 2.122         | 0.0847     | 0.4439     | 0.7260     | 25.53      |
| 3   | 81.94    | 2.154         | 0.0763     | 0.3819     | 0.6311     | 26.99      |
| 4   | 82.24    | 2.142         | 0.0715     | 0.3380     | 0.5549     | 28.74      |
| 5   | 82.39    | 2.159         | 0.0686     | 0.3128     | 0.5081     | 30.63      |
| 6   | 83.30    | 2.160         | 0.0668     | 0.2930     | 0.4695     | 31.75      |
| 7   | 83.35    | 2.222         | 0.0657     | 0.2832     | 0.4495     | 32.04      |
| 8   | 82.15    | 2.211         | 0.0649     | 0.2740     | 0.4313     | 33.35      |
| 9   | 82.23    | 2.222         | 0.0641     | 0.2670     | 0.4182     | 34.63      |
| 10  | 82.21    | 2.227         | 0.0636     | 0.2622     | 0.4079     | 35.14      |

### Pythia-410M, α=0.50, seed 42 (alpha_sweep)

| Gen | eff_rank | token_entropy | distinct_1 | distinct_2 | distinct_3 | perplexity |
|-----|----------|---------------|------------|------------|------------|------------|
| 0   | 46.61    | 3.234         | 0.0982     | 0.5178     | 0.8127     | 26.95      |
| 1   | 58.56    | 2.517         | 0.0975     | 0.5141     | 0.8104     | 22.96      |
| 2   | 63.59    | 2.498         | 0.0827     | 0.4311     | 0.7153     | 26.38      |
| 3   | 64.59    | 2.564         | 0.0756     | 0.3838     | 0.6401     | 27.48      |
| 4   | 65.11    | 2.549         | 0.0706     | 0.3346     | 0.5493     | 28.69      |
| 5   | 63.86    | 2.546         | 0.0674     | 0.3089     | 0.5048     | 29.94      |
| 6   | 62.23    | 2.567         | 0.0658     | 0.2897     | 0.4663     | 30.19      |
| 7   | 62.22    | 2.608         | 0.0639     | 0.2727     | 0.4305     | 30.77      |
| 8   | 60.85    | 2.611         | 0.0627     | 0.2631     | 0.4133     | 31.58      |
| 9   | 59.53    | 2.633         | 0.0623     | 0.2565     | 0.3981     | 32.11      |
| 10  | 59.33    | 2.632         | 0.0616     | 0.2513     | 0.3873     | 32.64      |

### Pythia-1.4B, α=1.00, seed 42 (generalize, 参考)

| Gen | eff_rank | token_entropy | distinct_1 | distinct_2 | distinct_3 | perplexity |
|-----|----------|---------------|------------|------------|------------|------------|
| 0   | 50.76    | 2.946         | 0.0993     | 0.5208     | 0.8129     | 19.68      |
| 1   | 86.65    | 1.527         | 0.0998     | 0.5205     | 0.8072     | 62.05      |
| 2   | 103.59   | 1.284         | 0.0824     | 0.4226     | 0.6918     | 141.75     |
| 3   | 98.58    | 1.247         | 0.0785     | 0.3864     | 0.6333     | 211.13     |
| 4   | 104.98   | 1.322         | 0.0758     | 0.3627     | 0.5917     | 280.50     |
| 5   | 106.41   | 1.264         | 0.0734     | 0.3452     | 0.5601     | 347.69     |
| 6   | 104.38   | 1.276         | 0.0715     | 0.3270     | 0.5270     | 406.49     |
| 7   | 102.87   | 1.283         | 0.0700     | 0.3153     | 0.5048     | 466.84     |
| 8   | 101.07   | 1.365         | 0.0696     | 0.3137     | 0.5027     | 535.68     |
| 9   | 100.43   | 1.316         | 0.0688     | 0.3069     | 0.4902     | 623.04     |
| 10  | 96.56    | 1.334         | 0.0684     | 0.3024     | 0.4812     | 677.24     |

---

## Q1: effective_rank 逐代变化轨迹

**结论：gen_0→1 的阶跃式跳变，非渐进上升。**

Pythia-1.4B α=0.50 的 effective_rank 变化分为两个阶段：

1. **Phase transition (gen 0→2)**：50.76 → 75.55 → 82.63，两代内完成 +63% 的跃升。其中 gen_0→1 单步贡献 +48.9%（24.8 个绝对值），是整个变化的主体。
2. **Plateau (gen 2→10)**：在 81.9~83.4 之间窄幅波动（标准差 0.53），完全稳定。

这不是逐代累积的漂移，而是一次性的 **regime shift**。gen_0→1 的训练即触发了 embedding 空间的结构性重组。

---

## Q2: effective_rank 与 diversity 指标的时间关系

**结论：存在明确的 "剪刀差" 模式，但有时间错位。**

关键观察：

| 时间窗口 | effective_rank | distinct_1/2/3 | token_entropy | perplexity |
|----------|---------------|-----------------|---------------|------------|
| gen 0→1  | +48.9% 跳变    | 几乎不变 (d3: 0.813→0.807) | -27.5% 骤降 (2.95→2.13) | +5.2% 微升 |
| gen 1→10 | 稳定 ~82       | 持续下降 (d3: 0.807→0.408, -49.5%) | 稳定 ~2.15-2.23 | +69.7% 持续上升 |

三层剪刀差：

1. **effective_rank vs distinct_n（经典剪刀差）**：effective_rank 在 gen_0→1 跳升后保持高位，distinct_1/2/3 则从 gen_1 开始持续下滑至 gen_10。两者在 gen_1 后形成持续扩大的剪刀口。

2. **effective_rank vs token_entropy（同步跳变）**：token_entropy 在 gen_0→1 与 effective_rank 同时发生剧变（但方向相反：entropy 下降，rank 上升）。之后两者都趋于稳定。这暗示 gen_0→1 的 phase transition 同时改变了 token-level 分布和 embedding-level 几何结构。

3. **effective_rank vs perplexity（渐进分离）**：perplexity 持续线性上升（19.7→35.1），而 effective_rank 在 gen_2 后不再变化。模型生成质量在持续退化，但 embedding 空间结构已经"锁定"在新的配置上。

**时间错位的含义**：effective_rank 的 phase transition 发生在 surface-level diversity 崩塌之前。embedding 空间的结构性重组是 collapse 的先行指标，先于 n-gram diversity 的下降。

---

## Q3: 与 Pythia-410M α=0.50 的对比

**结论：410M 也有 effective_rank 上升，但模式完全不同。这是 scale-amplified 现象，而非 scale-specific。**

| 特征 | Pythia-410M (1024-dim) | Pythia-1.4B (2048-dim) |
|------|------------------------|------------------------|
| 初始 eff_rank | 46.61 | 50.76 |
| 峰值 eff_rank | 65.11 (gen 4) | 83.35 (gen 7) |
| 终值 eff_rank | 59.33 | 82.21 |
| 净变化 | +27.3% | +62.0% |
| 轨迹形状 | 倒 U 型（rise-then-fall） | 阶跃函数（jump-then-plateau） |
| 跳变速度 | 渐进，4 代升至峰值 | 急剧，1 代完成主体跳变 |
| 后期趋势 | gen 4→10 回落 -8.9% | gen 2→10 几乎不变 |

关键差异的可能解释：

- **容量效应**：1.4B 的 2048-dim embedding 空间为 singular value 的"扩散"提供了更多自由度。410M 在 1024-dim 空间中更快触及有效维度的上界，导致先升后降。
- **Phase transition vs gradual shift**：1.4B 的更大参数量可能支持更锐利的 phase transition（类似于统计物理中系统尺寸越大，相变越尖锐）。
- **Plateau stability**：1.4B 的 embedding 空间足够大，可以在 "diffuse" 状态下稳定维持而不饱和。410M 的空间有限，"diffuse" 状态不稳定，最终回落。

α=1.00 的 1.4B 数据提供额外佐证：同样是 1.4B 模型，α=1.00 时 effective_rank 峰值达到 106.4（比 α=0.50 的 83.4 高 28%），perplexity 达到 677（比 α=0.50 的 35 高 19 倍）。更强的 collapse 驱动力 → 更高的 effective_rank。两个 seed（s42/s43）在 α=1.00 下都表现出类似模式（s43 峰值 100.8），确认这不是随机波动。

---

## Q4: 解释假说

### 假说验证："embedding 空间扩散 + 局部集中"

原始假说：1.4B 模型在 collapse 过程中出现 "embedding 空间扩散但局部集中"，即模型输出占用更多维度，但每个维度内的 token 多样性下降。

**数据判定：假说成立，且可以精化。**

支撑证据：

1. **Effective rank 上升 = singular value 均匀化 = 输出占用更多维度**：gen_0 时，少数主导 singular value 贡献了大部分方差（rank ≈ 51）；gen_1 后，方差更均匀地分布到更多维度（rank ≈ 82）。

2. **Distinct_n 下降 = surface token 多样性下降**：d3 从 0.813 降至 0.408，表明模型生成文本中的 unique 3-gram 比例减半。

3. **Token entropy 骤降 = token 分布集中化**：从 2.95 降至 2.13，模型的 next-token 预测分布变得更尖锐/确定。

4. **Perplexity 上升 = 确定但"错误"的预测**：模型输出的 token 分布更集中（低 entropy），但与真实分布偏离更大（高 perplexity）。

### 精化后的机制解释

**"Confident diffusion" 假说**：

model collapse 导致 1.4B 模型进入一种 "自信但失焦" 的状态：

- 模型在 token 层面变得更加确定（low token_entropy），倾向于反复使用少量 token 模式（low distinct_n）
- 但这些"自信的重复模式"在 embedding 空间中并不集中在同一方向，而是分散在多个正交方向上
- 结果是 singular value 分布变得更均匀（high effective_rank），同时 surface diversity 下降

直觉类比：把 embedding 空间想象成一个球面。健康模型的输出在球面上形成几个密集的高维"簇"（low rank, high diversity within clusters）。collapse 后，模型输出变成许多分散的低维"点"（high rank, low diversity per point）。整体占用了更多维度，但每个方向上的内容更贫乏。

### 为什么 1.4B 比 410M 更极端

1. **更大的 embedding 空间 (2048 vs 1024)** 为 "扩散" 提供了更多自由度，effective_rank 可以跳到更高的绝对值
2. **更多参数带来更锐利的 phase transition**：一次训练就足以重组 embedding 空间几何结构（gen_0→1 的阶跃），而 410M 需要多代逐渐调整
3. **1.4B 的 overparameterization** 使得 "扩散" 状态可以稳定维持（plateau），而 410M 的参数不足以支撑该状态，最终回落

### α 依赖性

α=1.00（全合成训练）下的 1.4B 数据进一步确认：
- effective_rank 峰值 106（vs α=0.50 的 83）：更强 collapse → 更强扩散
- Perplexity 677（vs α=0.50 的 35）：更严重的生成退化
- 但 effective_rank 在 α=1.00 后期出现缓慢回落（106→97），暗示存在一个上界，可能与 embedding 空间的实际有效维度相关

---

## Paper-ready explanation

> In Pythia-1.4B, effective rank rises sharply from 50.8 to 82.2 (+62%) within the first two generations of iterative training, then plateaus for the remaining eight generations. This increase occurs simultaneously with a drop in token entropy (2.95 to 2.13) and precedes the steady decline in surface-level diversity (distinct-3 falling from 0.81 to 0.41). The pattern is consistent with a "confident diffusion" mechanism: as model collapse reduces the model's output to a narrower set of repetitive token patterns, these patterns project onto a broader, more uniform set of embedding dimensions, elevating the effective rank. The 410M model shows a qualitatively different, inverted-U trajectory (+27%, peaking at generation 4 then declining), suggesting that larger embedding spaces (2048-dim vs 1024-dim) both amplify the magnitude of this spectral reorganization and stabilize the diffuse configuration.

> Effective rank thus functions as an early-warning collapse indicator that is paradoxically anti-correlated with surface diversity: it rises precisely because the model's output distribution is losing its structured, peaked geometry in embedding space.
