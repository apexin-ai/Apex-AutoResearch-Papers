# research literature verification

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_verification_20260513T030831_result.json`
- **Structured JSON:** [`e987e99037e7a32e4806.json`](../../sessions/e9/e987e99037e7a32e4806.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部10篇论文搜索完成。以下是汇总结果。

---

## 任务 A：论文验证结果

| # | 论文简称 | arXiv ID | 验证状态 | 真实作者 | 备注 |
|---|---------|----------|---------|---------|------|
| 1 | ERBP | 2512.14879 | **VERIFIED** | Jingwei Chen（独立研究者，中国株洲） | 单作者，"et al." 不准确但人名正确 |
| 2 | EntroPIC | 2511.15248 | **VERIFIED** | Kai Yang, Xin Xu, Yangkun Chen, Weijie Liu, Jiafei Lyu, Zichuan Lin, Deheng Ye, Saiyong Yang | 腾讯混元 / 港科大，"Kai Yang et al." 正确 |
| 3 | Data Mixing Laws | 2403.16952 | **VERIFIED** | Jiasheng Ye, Peiju Liu, Tianxiang Sun, Jun Zhan, Yunhua Zhou, Xipeng Qiu | ICLR 2025 accepted |
| 4 | Demystifying Synthetic Data | 2510.01631 | **VERIFIED** | Feiyang Kang et al.（10+ 作者） | 2025-10 提交 |
| 5 | Scaling Laws of Synthetic Data | 2503.19551 | **VERIFIED** | Zeyu Qin, Qingxiu Dong, Xingxing Zhang, Li Dong et al. | 2025-03 提交，v3 修订于 2025-10 |
| 6 | How to Tame Your LLM | 2512.05162 | **VERIFIED** | C. M. Wyss | 单作者，2025-12 提交 |
| 7 | A Closer Look at Model Collapse | 2509.16499 | **VERIFIED** | Lianghe Shi, Meng Wu, Huijie Zhang, Zekai Zhang, Molei Tao, Qing Qu | 完整标题含副标题 "From a Generalization-to-Memorization Perspective" |
| 8 | Spectral Dynamics of Weights | 2408.11804 | **VERIFIED** | David Yunis, Kumar Kshitij Patel, Samuel Wheeler, Pedro Savarese, Gal Vardi, Karen Livescu, Michael Maire, Matthew R. Walter | 完整标题 "...through the Spectral Dynamics of Weights" |
| 9 | Neural Collapse vs Low-rank Bias | 2405.14468 | **VERIFIED** | Peter Súkeník, Marco Mondelli, Christoph Lampert | 完整标题含副标题 "Is Deep Neural Collapse Really Optimal?" |
| 10 | An Effective Gram Matrix | 2504.16450 | **VERIFIED** | Rubing Yang, Pratik Chaudhari | 完整标题 "...Characterizes Generalization in Deep Networks" |

**结论：10篇全部真实存在，无幻觉论文。** ERBP 的 "et al." 标注需修正为单作者。

---

## 任务 B：Novelty vs EntroPIC 分析

**与 EntroPIC 的差异性分析（Novelty Statement）**

EntroPIC（Yang et al., 2025）与本工作均采用 PI 控制范式稳定训练过程，且均证明了纯比例控制（P-only）不足以应对累积误差，积分项（I-term）不可或缺。然而，两者在三个核心维度上存在本质差异：

**控制变量不同。** EntroPIC 调节的是 RL 训练中正/负样本的 loss 系数，作用于参数更新空间；我们调节的是 iterative pretraining 中 synthetic-to-real 的数据混合比例，作用于数据空间。前者是梯度信号的加权，后者是训练数据分布的重构。

**控制信号不同。** EntroPIC 以 policy 输出分布的 entropy 为反馈信号，直接度量模型输出的多样性；我们以权重矩阵的 spectral effective rank 为反馈信号，度量的是模型内部表征的维度利用率。Effective rank 是一个更早期的 collapse 前兆指标——entropy 下降时 collapse 可能已经开始，而 spectral rank 的收缩往往先于可观测的性能退化。

**应用场景不同。** EntroPIC 解决的是 RLHF/GRPO 等强化学习阶段的 entropy collapse（模型过早收敛到确定性策略），目标是维持探索-利用平衡；我们解决的是 iterative synthetic pretraining 中的 model collapse（多轮自训练导致分布退化），目标是在持续使用合成数据时防止表征坍缩。

**共同点与方法论传承。** 两者共享 PI 控制的方法论内核，均源于经典控制理论在 ML 训练动态中的应用。EntroPIC 的工作验证了 PI 控制在 ML 训练稳定性问题上的有效性，为本工作的方法论选择提供了旁证支持。但 control surface 的根本差异（参数空间 loss weighting vs 数据空间 mixing ratio，policy entropy vs spectral effective rank）确保了充分的新颖性。

---
