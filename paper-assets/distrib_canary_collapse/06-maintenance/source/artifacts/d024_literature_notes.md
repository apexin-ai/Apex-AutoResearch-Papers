# D024: 合成数据 Dose-Response 非单调性文献调研

## 核心问题

我们在 α-sweep 实验中观测到 diversity collapse 与合成数据比例 α 之间的非单调关系：
- α=0.00: distinct_1 drift -13.8%
- α=0.25: distinct_1 drift -40.3%（最强退化）
- α=0.50: distinct_1 drift -33~35%（退化减弱）

问：文献中是否有类似报告？有何理论解释？

## 文献检索结论

**直接报告非单调 dose-response 的论文：零。** 这是一个文献空白。

现有论文几乎一致假设 "more synthetic → more collapse" 的单调关系，或只关注 "有/无 collapse" 的二分问题。但以下理论工作间接支持非单调性的存在。

## 最相关的 3 篇论文

### 1. He, Xu & Cheng (2025). "Golden Ratio Weighting Prevents Model Collapse." arXiv:2502.18049

**发现：** 在迭代训练中，最优 real data 权重（最小化长期预测误差）在 Gaussian estimation、GLM、非参数估计中均收敛到黄金比例倒数 1/φ ≈ 0.618。更关键的是，**最优权重 w*(λ) 作为正则化参数 λ 的函数既非单调也非凸**。

**与我们结果的关系：** 如果最优权重本身是非单调的，那么在不同 α 下的 risk landscape 也是非单调的。这意味着 α=0.25 可能恰好处于 risk landscape 的一个"局部最大值"——不是最多合成数据时 collapse 最严重，而是在某个特定比例处最危险。

**局限：** 理论基于线性回归和高斯分布，未直接推广到 LLM diversity metrics。

### 2. Xu & Cheng (2025). "Preventing Model Collapse Under Overparametrization: Optimal Mixing Ratios." arXiv:2509.22341

**发现：** 在过参数化 regime（插值学习 + ridge 回归）中分析最优混合比例。
- 插值学习：最优 real data 比例收敛到 1/φ
- Ridge 回归：最优比例受谱几何控制，至少为 1/2
- **variance 行为的非单调性：** w > 1/3 时 variance 随迭代单调递减；w < 1/3 时 variance 可能增长——存在临界阈值

**与我们结果的关系：** 1/3 临界阈值与我们观测到的 α=0.25 和 α=0.50 之间的行为差异有概念上的对应。虽然参数空间不完全对齐，但"存在临界 mixing ratio 使得行为质变"与我们的非单调观测一致。

### 3. Chen et al. (2025). "Characterizing Model Behavior Under Synthetic Data Training." arXiv:2510.05133

**发现：**
- 20% synthetic 以下性能稳定，30% 以上退化加速
- ECE 先于 accuracy 退化
- **未报告非单调性**——关注的是阈值效应（safe zone vs danger zone），未细粒度扫描中间区间的 diversity metrics

**与我们结果的关系：** 他们的 20-30% 阈值与我们 α=0.25 处出现最强 collapse 的观测部分一致——α=0.25 恰好处于其"danger zone 入口"。但他们未测试 α=0.50 是否反而比 α=0.30 轻，因此无法确认或否认非单调性。

## 补充相关论文

### 4. Gillman et al. (2024). "Self-Correcting Self-Consuming Loops." arXiv:2402.07087, ICML 2024

引入 self-correction function 后，即使 100% synthetic data 也能避免 collapse。暗示 dose-response 关系可被 intervention 完全改变——不同 α regime 下可能存在不同 training dynamics。

### 5. Truong (2025). "Entropy Collapse" — 已在 literature_map 中

一阶相变框架：如果 α=0.25 和 α=0.50 处于不同 universality class 或相变边界的不同侧，可以解释非单调行为。

### 6. Bakshi & Chakraborty (2026). "From Collapse to Improvement" — 已在 literature_map 中

αt/nt trajectory 交互决定 collapse/improvement/consistency 三种 regime。不同 α 值可能落入不同 regime，导致非单调的宏观行为。

## 对我们结果的潜在解释

综合文献，三种最可信的解释（按可能性排序）：

### 解释 1: "最危险区间"假说（最可能）
α=0.25 处于合成数据"刚好够破坏分布尾部、但不足以让模型快速饱和"的区间。参考 He et al. 的黄金比例理论，risk landscape 在 mixing ratio 空间上本身不是单调的——存在 worst-case ratio 使 risk 最大化。α=0.25（real weight=0.75）可能接近这个 worst-case。

### 解释 2: 饱和效应（次可能）
α=0.50 下模型在前几代就快速进入 collapsed attractor，后续迭代只是在该 attractor 附近微小扰动，generation-over-generation 的 drift 自然变小。而 α=0.25 的 collapse 更慢但更持续，累积 drift 反而更大。可通过检查各 generation 的 distinct_1 轨迹形状验证：如果 α=0.50 呈"快速下降后平台"而 α=0.25 呈"持续缓慢下降"，则支持此解释。

### 解释 3: Regime 切换（需更多证据）
α=0.25 和 α=0.50 可能触发了不同训练 regime（类似 Bakshi 2026 的三 regime 分类），各 regime 下 diversity 退化机制不同。

## 对 Paper Framing 的建议

**这是 novel finding。** 文献中没有关于 diversity dose-response 非单调性的直接报告。

1. **Novelty claim**: "We identify a non-monotonic dose-response relationship between synthetic data fraction and diversity collapse, where intermediate mixing ratios (α≈0.25) produce worse diversity degradation than higher ratios (α≈0.50)."

2. **理论锚点**: 引用 He et al. 2025 的黄金比例理论作为非单调 risk landscape 的理论先例，但强调他们的结果是关于 prediction risk 而非 diversity metrics，我们首次在 diversity/collapse metrics 上展示此现象。

3. **实验验证需求**: 为使 claim 更 robust，需要：
   - 更细粒度的 α sweep（0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50）
   - 多个 diversity metrics（distinct-1, distinct-2, Self-BLEU, type-token ratio）同时验证
   - 至少 3 个 random seeds 的置信区间
   - 逐 generation 轨迹分析以区分解释 1 vs 解释 2

4. **Section 位置**: 建议在 Results 部分以独立 subsection 呈现（"Non-monotonic dose-response in diversity collapse"），而非 Discussion——因为这是实证发现而非推测。

## 搜索关键词记录
- "model collapse synthetic data mixing ratio dose response non-monotonic"
- "self-consuming generative models mixing ratio synthetic data proportion"
- "iterative training synthetic data contamination ratio threshold saturation"
- "golden ratio weighting synthetic data model collapse"
- "model collapse sweet spot worst case synthetic data proportion"
- "synthetic data non-monotonic U-shaped diversity collapse"
- "model collapse phase transition regime change critical threshold"
