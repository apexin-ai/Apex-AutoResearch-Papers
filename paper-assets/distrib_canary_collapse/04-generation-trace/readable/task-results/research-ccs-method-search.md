# research ccs method search

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ccs_method_search_20260520T091321_result.json`
- **Structured JSON:** [`3f0947e42cf37054337d.json`](../../sessions/3f/3f0947e42cf37054337d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have enough information. Let me compile the structured report.

---

## 1. CCS / Multispatial CCM 可用实现

### CCS (Convergent Cross Sorting, Breston 2021)

| 项目 | 详情 |
|------|------|
| **官方实现** | [lbreston/CCS](https://github.com/lbreston/CCS) — **MATLAB only**，5个文件（`CCS.m`, `convergence.m`, `fnnTDsweep.m`），8 stars |
| **Python 实现** | **不存在。** PyPI 无 CCS 包，GitHub 无 Python port |
| **最短测试长度** | 论文测试到 L=50，未测 L<50。T=11 未经验证 |
| **论文** | [Scientific Reports 2021](https://www.nature.com/articles/s41598-021-98864-2)；[限制性分析 (2023)](https://royalsocietypublishing.org/doi/10.1098/rsos.221590) 指出 CCS 在极短序列上的限制 |

### Multispatial CCM (Clark et al. 2015)

| 项目 | 详情 |
|------|------|
| **R 实现** | [multispatialCCM](https://cran.r-project.org/web/packages/multispatialCCM/) — R 包，CRAN 上可用，[GitHub](https://github.com/adamtclark/multispatialCCM) |
| **Python 实现** | **不存在。** 无 Python port |
| **核心思路** | 将多个短序列（spatial replicates）拼接为一个长向量（NA 分隔），对拼接后序列做 CCM + 自举检验 |
| **最短长度** | 论文验证 T≥5 可行（需要多个 spatial replicates） |
| **适用性** | **高度适配我们场景**：我们有 N 个 seed/layer 的短序列（T=11 或 T=20），可视为 spatial replicates |
| **论文** | [Clark et al. 2015, Ecology](https://esajournals.onlinelibrary.wiley.com/doi/abs/10.1890/14-1479.1) |

### 其他 Python CCM 包（均不支持 CCS/Multispatial）

| 包 | 状态 | 备注 |
|----|------|------|
| [skccm](https://pypi.org/project/skCCM/) | vanilla CCM only | scikit-learn 风格 API，不支持 multispatial |
| [causal_ccm](https://github.com/PrinceJavier/causal_ccm) | vanilla CCM + PAI | 不支持 CCS/multispatial |
| [pyCCM](https://github.com/C-Naoki/pyCCM) | vanilla CCM | 同上 |
| [ccmMul](https://github.com/SharathSPhD/ccmMul) | multivariate CCM（多变量，非 multispatial） | 不同概念 |
| pyccm (PyPI) | vanilla CCM, Python 2.7 | 过时 |

---

## 2. 自行实现的可行性评估

### CCS Python 实现（~2-3天工作量）

从 MATLAB 源码提取的核心算法：

```
CCS(x, y, lag, tau, dim, thresh):
  1. 延迟嵌入重构: 构建 Le×dim 矩阵 X, Y
     Le = L - 1 - (dim-1)*tau,  行 i: [x[i+T], x[i+T-tau], ..., x[i]]
  2. 距离矩阵: dX = pdist2(X,X), dY = pdist2(Y,Y)  (Le×Le)
  3. 去对角线: 用 std*thresh 阈值掩码移除临近点
  4. 展平+排序: xflat, yflat → 独立排序获取 rank (归一化到 [0,1])
  5. 交叉排序: r_xcy = X的rank按Y的排序重排, r_ycx 反之
  6. NERR²: se = (r_xcy - rank)², null = rank² - rank + 1/3
     RVP = cumsum(-(se - null) / null) / count
  7. 指数拟合: f(x) = a + b*exp(c*x), 加权最小二乘
  8. 耦合分数: C = f(0)，即 y 截距，裁剪到 [-1, 1]
```

**依赖**: numpy, scipy（`cdist`, `curve_fit`）

**风险**: T=11 时 Le = 11 - 1 - (E-1)*tau。若 E=2, tau=1 → Le=9，距离矩阵仅 9×9=81 个元素（去对角线后更少），排序统计量极不稳定。**CCS 在 T=11 上大概率不可靠。**

### Multispatial CCM Python 实现（~1-2天，推荐）

核心思路更简单：
1. 将 K 个短序列（每个 T=11）拼接，NA 分隔 → 有效长度 ~K*11
2. 对拼接序列做标准 CCM（跳过 NA 邻居）
3. 自举显著性检验

**可直接基于 skccm 修改**，只需加 NA-aware 的距离计算和拼接逻辑。我们有 ~40+ seeds × multiple layers，spatial replicates 充足。

**推荐方案**: 实现 Multispatial CCM wrapper 包裹 skccm，工作量最小且理论上对 T=11 场景最适配。

---

## 3. 三篇论文关键内容

### 3.1 Gu et al. — 未找到精确匹配

搜索 "Gu 2025 ICLR spotlight cross-lingual alignment emergence" 未找到完全匹配的论文。最接近的候选：

- **Jiawei Gu et al. "CMR Scaling Law"** (EMNLP 2024)：发现 loss、mixture ratio、training tokens 之间的 power-law 关系，定义了 Critical Mixture Ratio (CMR)。但这是关于 continual pre-training 而非 cross-lingual alignment emergence。[arXiv:2407.17467](https://arxiv.org/abs/2407.17467)
- **"Data Mixing Can Induce Phase Transitions in Knowledge Acquisition"** (2025)：critical mixing ratio 遵循与 model size 的 power law。[arXiv:2505.18091](https://arxiv.org/pdf/2505.18091)
- **Wang et al. "Probing the Emergence of Cross-lingual Alignment during LLM Training"** (ACL Findings 2024)：观察到 cross-lingual neuron overlap 与下游性能高度相关。[arXiv:2406.13229](https://arxiv.org/abs/2406.13229)

**需要确认**: Director 引用的论文标题/作者可能有偏差，请核实。

### 3.2 Truong & Truong (2025) — Entropy Collapse

**论文**: [Entropy Collapse: A Universal Failure Mode of Intelligent Systems](https://arxiv.org/html/2512.12381)
**作者**: Truong Xuan Khanh & Truong Quynh Hoa

**关键公式**:

| 概念 | 公式 |
|------|------|
| 临界阈值 | α_c(β) = 1/(1-β)，α=反馈放大，β=有界新颖性再生 |
| 序参量 | m = 1 - H_ss/H_max |
| Class 判定 | κ = f″(1/N)，κ>0 → Class 1，κ=0 → Class 2 |

**两个 Universality Classes**:

| | Class 1 (κ>0, convex) | Class 2 (κ=0, linear) |
|---|---|---|
| 相变类型 | 一阶不连续 | 二阶连续 |
| 熵跳变 | Δm₀ = 0.698 | 0 |
| 迟滞 | ΔH_hyst ≈ 2.73 nats | 无 |
| 弛豫指数 | ν = 1 | ν = 1/2 |
| 可逆性 | **不可逆** | **可逆** |
| 例子 | 所有 power-law 反馈、multiplicative weights | 线性反馈 |

**与我们场景的对应**:
- 我们的 entropy collapse（训练中 token distribution diversity 下降）属于 **Class 1**（softmax 是 convex feedback）
- 一阶相变意味着 **collapse 无渐进预警**（CSD indicators 可能失效），与我们 CSD 检验结果一致
- 不可逆性解释了为什么 collapse 后无法恢复

### 3.3 Dakos et al. (2012) — CSD 方法论综述

**论文**: [Methods for Detecting Early Warnings of Critical Transitions](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0041010), PLoS ONE 7(7): e41010

**核心方法清单**:

**Metric-based（滑动窗口内计算）**:
| 指标 | 检测什么 | 公式/方法 |
|------|----------|-----------|
| AR(1) | 自相关增强（critical slowing down 核心信号）| lag-1 自相关系数 |
| Variance / SD | 方差增大 | 滚动窗口内二阶矩 |
| Skewness | 分布不对称 | 三阶标准化矩 |
| Kurtosis | 尾部变厚 | 四阶标准化矩 |
| Spectral reddening | 低频功率增加 | 功率谱分析 |
| DFA | 长程相关 | 去趋势波动分析（需 >100 数据点） |

**趋势检验**: Kendall τ 秩相关，接近 1 = 强增趋势

**显著性检验**: 
1. 对去趋势残差拟合 ARMA(p,q)
2. 生成 1000 个 surrogate 序列
3. 比较原始 Kendall τ 与 surrogate 分布
4. 跨所有参数组合（窗口大小、带宽）做敏感性分析

**与我们场景的对应**:
- 我们 T=11 远低于 DFA 要求的 >100 → DFA 不可用
- 滑动窗口法需要足够长的序列 → 窗口=half length=5 点，统计量不可靠
- 这正是为什么需要 Multispatial CCM（利用多 seed/layer replicates 弥补单序列太短的问题）
- Truong 的 Class 1 结论（一阶相变无渐进预警）从理论上解释了 CSD 在我们场景失效的根因

---

## 总结建议

**因果检验推荐路径**: 实现 Multispatial CCM Python wrapper（基于 skccm + NA-aware 拼接），利用我们丰富的 seed/layer replicates。CCS 对 T=11 风险太高（距离矩阵太小）。

**Gu 论文**: 未找到精确匹配，需 Director 确认具体标题或 arXiv ID。

---
