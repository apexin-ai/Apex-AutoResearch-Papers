# 信道级联 + DPI 理论框架草案

> 将递归生成建模为 iterated lossy channel，用 Data Processing Inequality 约束 depth-discriminability 的 fundamental limit。

---

## 1. 信道级联模型形式化

### 基本设定

设 X₀ 为人类撰写的文本（seed text），表示为某概率空间上的随机变量。LLM 的生成过程建模为一个随机信道：

$$\mathcal{T}: \mathcal{X} \to \mathcal{X}$$

将输入文本映射到输出文本。递归生成形成 Markov chain：

$$X_0 \to X_1 \to X_2 \to \cdots \to X_k$$

其中 $X_{i+1} = \mathcal{T}(X_i)$，即 depth-$(i+1)$ 的文本由 depth-$i$ 的文本经过一次 LLM 信道产生。

**关键假设**：

- **(A1) 时不变信道**：同一 LLM + 同一 decoding strategy 在每次迭代中使用相同的信道 $\mathcal{T}$。（prompt-chain 设定下成立；retrain-chain 需放宽为 $\mathcal{T}_i$）
- **(A2) Markov 性**：$X_{i+1}$ 仅依赖 $X_i$，不依赖 $X_0, \ldots, X_{i-1}$（prompt-chain 逐段独立生成时成立）
- **(A3) 有损信道**：$\mathcal{T}$ 是 non-invertible 的——生成过程丢失关于输入的信息（sampling 引入 noise，decoding 策略截断分布尾部）

### 形式化表述

$$X_0 \xrightarrow{\mathcal{T}} X_1 \xrightarrow{\mathcal{T}} X_2 \xrightarrow{\mathcal{T}} \cdots \xrightarrow{\mathcal{T}} X_k$$

这是一个齐次 Markov chain（在假设 A1 下），其转移核由 LLM 的条件分布 $p_\theta(\cdot | x)$ 决定。

---

## 2. Data Processing Inequality 约束

### DPI 基本形式

对于 Markov chain $X_0 \to X_1 \to \cdots \to X_k$，DPI 给出：

$$I(X_0; X_k) \leq I(X_0; X_{k-1}) \leq \cdots \leq I(X_0; X_1) \leq H(X_0)$$

即 $I(X_0; X_k)$ 关于 $k$ 单调非递增。

**直觉**：每经过一次 LLM 信道，关于原始人类文本 $X_0$ 的信息只会减少或不变，绝不增加。递归生成是不可逆的信息丢失过程。

### 严格衰减条件

当 $\mathcal{T}$ 是 strictly lossy channel（即 $I(X_i; X_{i+1}) < H(X_i)$ for all $i$）时，衰减是严格的：

$$I(X_0; X_k) < I(X_0; X_{k-1}) \quad \forall k \geq 1$$

这对应于 LLM 生成过程中 sampling noise 不可消除的事实——任何 temperature > 0 或 nucleus/top-k 截断都引入不可逆信息损失。

### 与 Depth Discriminability 的联系

两个不同深度 $k, k'$ 的文本 $X_k, X_{k'}$ 的可区分性取决于它们的分布差异。定义可区分性度量：

$$D(k, k') = d(P_{X_k}, P_{X_{k'}})$$

其中 $d$ 是某种分布距离（JSD、MMD、Total Variation 等）。

**关键观察**：随着 $k$ 增大，$P_{X_k}$ 趋近于信道 $\mathcal{T}$ 的不动点分布 $P^*$（如果存在），相邻深度的分布差异趋于零：

$$D(k, k+1) \to 0 \quad \text{as} \quad k \to \infty$$

---

## 3. K* 的理论解释

### 定义

$K^*$ 是 **判别饱和边界（discriminability saturation boundary）**：

$$K^* = \max\{k : D(k-1, k) > \epsilon\}$$

其中 $\epsilon$ 是 noise floor（对应于有限样本下的统计检验 power limit）。

### Information-Theoretic 解释

$K^*$ 对应于 $I(X_0; X_k)$ 降至 noise floor 的临界深度：

$$K^* \approx \min\{k : I(X_0; X_k) - I(X_0; X_{k+1}) < \delta\}$$

其中 $\delta$ 是 MI 增量的可检测下限。

**关键 insight**：$K^*$ 不是分类器的能力上限，而是 **information-theoretic impossibility boundary**——任何方法（无论多复杂）都无法区分 depth $> K^*$ 的文本，因为原始人类文本的信息已经被信道噪声完全淹没。

### 与 Channel Capacity 的关系

信道 $\mathcal{T}$ 的 "contraction rate" $\rho$ 控制 MI 衰减速度：

$$I(X_0; X_k) \leq \rho^k \cdot H(X_0) \quad (\text{if exponential decay})$$

- $\rho$ 接近 1（低噪声信道，如 greedy decoding）→ 衰减慢，$K^*$ 大
- $\rho$ 接近 0（高噪声信道，如 high-temperature sampling）→ 衰减快，$K^*$ 小

**但这里有一个反直觉的 nuance**：虽然 high-temperature 使 $\rho$ 更小（信息丢失更快），但它同时保持了更高的 diversity，使相邻深度的分布差异可能更大。因此 $K^*$ 与 decoding strategy 的关系不是简单单调的——这正是需要实验验证的假设。

---

## 4. Propositions / Theorems 骨架

### Proposition 1: MI 单调衰减（DPI 直接推论）

**Statement**: 设 $X_0 \to X_1 \to \cdots \to X_k$ 为上述递归生成 Markov chain。则对任意 $k \geq 1$：

$$I(X_0; X_k) \leq I(X_0; X_{k-1})$$

等号成立当且仅当 $X_{k-1} \to X_k$ 是 sufficient statistic（即信道 $\mathcal{T}$ 是无损的，实际中不成立）。

**Proof sketch**:
直接由 DPI 定理得出。$X_0 \to X_{k-1} \to X_k$ 构成 Markov chain，DPI 立即给出 $I(X_0; X_k) \leq I(X_0; X_{k-1})$。严格不等号由 $\mathcal{T}$ 的 strictly lossy 性质保证（sampling 引入不可消除的噪声）。$\square$

**论文中的作用**：建立理论基础——depth discrimination 必然随深度退化，这不是分类器缺陷，而是信息论必然。

---

### Proposition 2: 不动点收敛与 K* 有限性

**Statement**: 若信道 $\mathcal{T}$ 具有唯一不动点分布 $P^*$（即 $\mathcal{T}(P^*) = P^*$），且 $\mathcal{T}$ 关于某分布度量 $d$ 是 contractive 的（$d(\mathcal{T}(P), \mathcal{T}(Q)) \leq \rho \cdot d(P, Q)$，$0 < \rho < 1$），则：

(a) $d(P_{X_k}, P^*) \leq \rho^k \cdot d(P_{X_0}, P^*)$

(b) $D(k, k+1) = d(P_{X_k}, P_{X_{k+1}}) \leq (\rho^k + \rho^{k+1}) \cdot d(P_{X_0}, P^*)$

(c) 对任意 $\epsilon > 0$，$K^*(\epsilon)$ 有限。

**Proof sketch**:
(a) 由 contractive mapping theorem 的标准迭代 bound。
(b) 三角不等式：$d(P_{X_k}, P_{X_{k+1}}) \leq d(P_{X_k}, P^*) + d(P_{X_{k+1}}, P^*)$，代入 (a) 得结论。
(c) $D(k, k+1)$ 以几何速率趋于 0，因此超过 $\epsilon$ 的 $k$ 值数量有限。$\square$

**论文中的作用**：证明 $K^*$ 的有限性是理论必然——saturation 不是方法缺陷而是系统属性。同时给出 $K^* = O(\log(d(P_{X_0}, P^*)/\epsilon) / \log(1/\rho))$ 的粗略 scaling。

---

### Proposition 3: 衰减速率与 Decoding Strategy 的关系（经验驱动假设）

**Statement（Conjecture，标注为 empirically motivated）**: 设 $\rho(\tau)$ 为 temperature 为 $\tau$ 时信道 $\mathcal{T}_\tau$ 的 contraction rate。在以下简化假设下（unigram-level，忽略序列结构）：

(a) $\rho(\tau)$ 关于 $\tau$ 非单调：存在 $\tau^*$ 使得 $\rho(\tau)$ 在 $\tau < \tau^*$ 时随 $\tau$ 递增，在 $\tau > \tau^*$ 时随 $\tau$ 递减。

(b) 直觉：极低 temperature（近 greedy）→ 信道近确定性 → $\rho$ 大但 diversity 低 → MI 本身小。极高 temperature → 信道近均匀随机 → $\rho$ 小 → MI 快速衰减。中间 temperature 平衡两个效应。

**Proof sketch**: 此为 conjecture，不提供证明。给出 unigram softmax 信道的显式 contraction rate 计算作为 supporting analysis，实验验证 $K^*(\tau)$ 的非单调性。

**论文中的作用**：将 decoding strategy 对 $K^*$ 的影响从 ad hoc 观察提升为 hypothesis-driven 研究。用 AIC/BIC model comparison 区分 exponential vs. polynomial MI 衰减。

---

## 5. 计算上的 Tractable Proxy

### JSD 作为 MI 近似

Mutual information 在高维文本空间中不可直接计算。我们采用 Jensen-Shannon Divergence (JSD) 作为 computationally tractable proxy：

$$\text{JSD}(P_{X_k} \| P_{X_{k'}}) = \frac{1}{2} D_{\text{KL}}(P_{X_k} \| M) + \frac{1}{2} D_{\text{KL}}(P_{X_{k'}} \| M)$$

其中 $M = \frac{1}{2}(P_{X_k} + P_{X_{k'}})$。

**在 unigram level 上计算**：将 $P_{X_k}$ 估计为 depth-$k$ 文档集合的 empirical unigram distribution。

**局限性（必须在论文中承认）**：
- Unigram JSD 忽略序列结构（bigram, trigram, syntactic patterns）
- 不等价于真正的 MI——JSD 是 distributional divergence，MI 是 sample-level information quantity
- 但 DPI 的定性结论（单调衰减）仍成立，因为 $\text{JSD}(P_{X_k} \| P_{X_0})$ 在 Markov chain 下也满足类似的单调性

**补充度量**：
- Pairwise classifier AUC 作为 empirical discriminability 的非参数度量
- Feature-space Mahalanobis distance 作为多维度的分布距离

---

## 6. 理论与实验的对接

| 理论预测 | 实验验证方法 |
|---|---|
| $I(X_0; X_k)$ 单调衰减 | JSD$(P_{X_0}, P_{X_k})$ 随 $k$ 递减曲线 |
| $K^*$ 有限 | Pairwise AUC 矩阵 + 操作性 K* 定义 |
| 衰减速率 $\rho$ 由 decoding strategy 控制 | $K^*(\text{greedy})$ vs. $K^*(p{=}0.95)$ vs. $K^*(T{=}1.2)$ |
| Exponential vs. polynomial decay | AIC/BIC model comparison on JSD decay curves |
| 不动点 $P^*$ 存在 | 检验 $P_{X_k}$ 对 $k$ 的收敛性（JSD$(P_{X_k}, P_{X_{k+1}}) \to 0$） |

---

## 7. 与既有理论的关系

- **Shumailov et al. (Nature 2024)**：他们的 tail disappearance → diversity loss → mode conflation 三阶段模型对应我们的 $P_{X_k} \to P^*$ 收敛过程中的不同阶段——尾部消失是收敛初期，mode conflation 是收敛后期
- **Strong Model Collapse (Dohmatob et al., ICLR 2025)**：他们的 statistical learning theory bound 与我们的 DPI bound 互补——他们关注 retrain-chain 下 generalization error 的增长，我们关注 distributional information 的衰减
- **JPEG 重压缩类比**：JPEG 信道也是 contractive mapping（量化步骤不可逆），K* 对应 JPEG recompression detection 的 cycle limit——在图像 forensics 中已被充分研究的问题

---

## 8. 写作注意事项

1. **措辞校准**：Propositions 1-2 是严格的（DPI + contractive mapping 标准结果）；Proposition 3 标注为 "empirically motivated conjecture"，不 overclaim
2. **JSD proxy 局限性**：在 Method section 设专段讨论 unigram 近似的局限和 justification
3. **信道假设**：A1（时不变）和 A2（Markov）在 prompt-chain 下合理，在 retrain-chain 下需要放宽——在 Discussion 中讨论
4. **不做"完整证明"**：论文风格是 proposition + proof sketch + experimental validation，不是纯理论论文的 full proof 风格。重点在 theory-experiment connection
5. **Appendix 安排**：完整的 contraction rate 计算、unigram softmax channel 分析放 appendix
