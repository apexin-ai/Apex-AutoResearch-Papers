# research literature coverage check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_coverage_check_20260521T000228_result.json`
- **Structured JSON:** [`eb6dad3f572e97a684e6.json`](../../sessions/eb/eb6dad3f572e97a684e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搜索完成。去重后整理如下（已排除与已引用论文重复的 Geng et al. 2603.11228，以及跨方向重复的 Drayson et al.）。

---

## 方向 1: Model Collapse / Self-Consuming Models (2025+)

### [方向 1] 论文 1

**Title**: LLM as a Broken Telephone: Iterative Generation Distorts Information
**Authors**: Mohamed et al.
**Venue/Year**: ACL 2025
**arXiv ID**: 2502.20258

**为什么相关**: 直接研究推理时链式生成中的信息失真，与本文 generation depth 概念高度对应
**建议引用**: Yes — inference-chain collapse 最接近的顶会论文
**如果引用，建议位置**: Related Work + Introduction（区分 training-loop 和 inference-chain collapse 时）

> 注意：与已引用的 "Qi et al. broken_telephone" 是不同论文（不同作者团队）。

---

### [方向 1] 论文 2

**Title**: Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World
**Authors**: Kazdan et al.
**Venue/Year**: ICML 2025
**arXiv ID**: 2410.16713

**为什么相关**: 系统比较三种 training workflow 下的 collapse 行为，是 Gerstgrasser et al. (COLM 2024) 的扩展
**建议引用**: Yes — 但需与已引用 Gerstgrasser et al. 做区分
**如果引用，建议位置**: Related Work

---

### [方向 1] 论文 3

**Title**: Machine-Generated Text Detection Prevents Language Model Collapse
**Authors**: Drayson et al.
**Venue/Year**: EMNLP 2025
**arXiv ID**: 2502.15654

**为什么相关**: 直接连接 AI text detection 和 model collapse 两个方向——用检测器过滤合成数据防 collapse，支撑 depth-aware detection 的应用价值
**建议引用**: Yes — detection + collapse 交叉的代表性工作
**如果引用，建议位置**: Introduction (motivation) 或 Discussion (broader impact)

---

### [方向 1] 论文 4

**Title**: Position: Model Collapse Does Not Mean What You Think
**Authors**: Schaeffer et al.
**Venue/Year**: ICML 2025 (Position Paper)
**arXiv ID**: 2503.03150

**为什么相关**: 梳理 model collapse 8 种不同定义，可用来支撑"现有定义未覆盖 inference-chain 场景"的论点
**建议引用**: Yes — 用于 positioning
**如果引用，建议位置**: Introduction 或 Related Work 开头

---

## 方向 2: AI Text Detection — Beyond Binary (2025+)

### [方向 2] 论文 1

**Title**: Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement
**Authors**: Cheng et al.
**Venue/Year**: WWW 2025
**arXiv ID**: 2410.14259

**为什么相关**: 提出 LLM Role Recognition 多类分类，量化 LLM involvement 程度，与本文 generation depth 作为序数指标的思路高度一致
**建议引用**: Yes — "beyond binary" 范式最直接的相关工作
**如果引用，建议位置**: Related Work (fine-grained detection) + Introduction

---

### [方向 2] 论文 2

**Title**: Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection
**Authors**: Li et al.
**Venue/Year**: arXiv 2026
**arXiv ID**: 2604.04932

**为什么相关**: 四类分类（pure human / LLM-polished human / humanized LLM / pure LLM），与本文 depth 分级理念接近
**建议引用**: Yes — 最新 fine-grained detection 工作
**如果引用，建议位置**: Related Work

---

### [方向 2] 论文 3

**Title**: Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text
**Authors**: Rao et al.
**Venue/Year**: arXiv 2025
**arXiv ID**: 2508.14190

**为什么相关**: 统一框架同时做检测+源归属，本文的 depth 识别也是一种更细粒度的归属任务
**建议引用**: Yes — 尤其本文涉及 source attribution 作为 downstream task
**如果引用，建议位置**: Related Work

---

### [方向 2] 论文 4

**Title**: FAID: Fine-Grained AI-Generated Text Detection Using Multi-Task Auxiliary and Multi-Level Contrastive Learning
**Authors**: Ta et al.
**Venue/Year**: NAACL 2025
**arXiv ID**: 2505.14271

**为什么相关**: 多级对比学习实现 human/AI/collaborative 细粒度分类，与本文 feature-based 方法形成 supervised vs. zero-shot 对照
**建议引用**: Yes
**如果引用，建议位置**: Related Work

---

## 方向 3: Iterative/Recursive LLM Generation (2025+)

### [方向 3] 论文 1

**Title**: Recursive Training Loops in LLMs: How Training Data Properties Modulate Distribution Shift in Generated Data?
**Authors**: Kovac et al.
**Venue/Year**: EMNLP 2025 (Oral)
**arXiv ID**: 2504.03814

**为什么相关**: 量化递归循环中词汇/语义多样性如何调控分布漂移，与本文 generation depth 导致的属性漂移直接对应
**建议引用**: Yes — 训练侧量化递归生成分布偏移，与本文推理侧观察互补
**如果引用，建议位置**: Related Work

---

### [方向 3] 论文 2

**Title**: LLM Probability Concentration: How Alignment Shrinks the Generative Horizon
**Authors**: Yang et al.
**Venue/Year**: arXiv 2025
**arXiv ID**: 2506.17871

**为什么相关**: 发现 aligned LLM 输出分布逐步集中（Branching Factor 递减），与本文 depth 增加时 entropy 降低的现象理论呼应
**建议引用**: Yes — 从概率集中角度解释 entropy 随 depth 递减的机制
**如果引用，建议位置**: Related Work 或 Discussion

---

### [方向 3] 论文 3

**Title**: Escaping Mode Collapse in LLM Generation via Geometric Regulation
**Authors**: Du & Tanaka-Ishii
**Venue/Year**: arXiv 2026
**arXiv ID**: 2605.00435

**为什么相关**: 将 mode collapse 解释为表示空间的几何坍缩，为 generation chain 输出趋于均质化提供 representation-level 解释
**建议引用**: Yes — Discussion 中解释深层 generation chain 均质化现象
**如果引用，建议位置**: Discussion

---

### [方向 3] 论文 4

**Title**: PADBen: A Comprehensive Benchmark for Evaluating AI Text Detectors Against Paraphrase Attacks
**Authors**: Zha et al.
**Venue/Year**: arXiv 2025
**arXiv ID**: 2511.00416

**为什么相关**: 评估迭代 paraphrase 对检测器的影响，揭示递归 paraphrase 的"语义位移但保留生成模式"现象
**建议引用**: Yes — 从攻击视角证明 iterative chain 改变统计属性
**如果引用，建议位置**: Related Work (AI text detection)

---

## 方向 4: LLM Output Distributional Analysis (2025+)

### [方向 4] 论文 1

**Title**: Diversity Boosts AI-Generated Text Detection (DivEye)
**Authors**: Basani & Chen
**Venue/Year**: ICLR 2026
**arXiv ID**: 2509.18880

**为什么相关**: 从 reference LM 的 token-level surprisal 提取高阶统计特征用于零样本检测，技术路线与本文高度一致
**建议引用**: Yes — **最直接的 parallel work，必须引用并做对比**
**如果引用，建议位置**: Related Work + Introduction

---

### [方向 4] 论文 2

**Title**: AI-Generated Text is Non-Stationary: Detection via Temporal Tomography
**Authors**: West et al.
**Venue/Year**: arXiv 2025
**arXiv ID**: 2508.01754

**为什么相关**: 用小波变换捕捉 token-level discrepancy 的非平稳性，发现 AI 文本段间统计变化比人类少 73.8%
**建议引用**: Yes — 互补的信号处理视角，支撑 entropy dynamics 随 depth 变化的分析
**如果引用，建议位置**: Related Work + Discussion

---

### [方向 4] 论文 3

**Title**: Entropy-Lens: The Information Signature of Transformer Computations
**Authors**: Ali et al.
**Venue/Year**: arXiv 2025 (revised 2026)
**arXiv ID**: 2502.16570

**为什么相关**: 用中间层 entropy profile 作为 LLM 计算签名，发现其具有模型家族特异性，强化 entropy 作为 fingerprint feature 的理论动机
**建议引用**: Yes — 支撑不同 generator 留下不同 fingerprint 的发现
**如果引用，建议位置**: Related Work + Introduction

---

### [方向 4] 论文 4

**Title**: Not All Tokens Are Created Equal: Perplexity Attention Weighted Networks for AI Generated Text Detection (PAWN)
**Authors**: Miralles-González et al.
**Venue/Year**: Information Fusion, Vol. 125, 2025
**arXiv ID**: 2501.03940

**为什么相关**: 根据 perplexity 和位置加权 token 贡献，与本文考虑哪些 token 的 entropy 信号对区分 depth 最有价值的设计有共鸣
**建议引用**: Yes — supervised vs. zero-shot 方法对比
**如果引用，建议位置**: Related Work

---

### [方向 4] 论文 5

**Title**: Unveiling Intrinsic Dimension of Texts: from Academic Abstract to Creative Story
**Authors**: Pedashenko et al.
**Venue/Year**: arXiv 2025
**arXiv ID**: 2511.15210

**为什么相关**: 发现 intrinsic dimension 与 entropy 互补，不同文体 ID 呈稳定分层——generation depth 是否也导致 ID 变化？
**建议引用**: Optional — Future Work 方向
**如果引用，建议位置**: Discussion / Future Work

---

## 优先级总结

**必须引用（强相关，遗漏会被 reviewer 指出）:**
1. **DivEye** (Basani & Chen, ICLR 2026) — 技术路线最接近的 parallel work
2. **Beyond Binary** (Cheng et al., WWW 2025) — fine-grained detection 最直接的先驱
3. **Drayson et al.** (EMNLP 2025) — detection + collapse 桥梁

**强烈建议引用:**
4. **Schaeffer et al. Position Paper** (ICML 2025) — collapse 定义辨析，支撑 positioning
5. **Kazdan et al. Collapse or Thrive** (ICML 2025) — training-loop collapse 最新全面研究
6. **Temporal Tomography** (West et al.) — 互补的信号处理视角
7. **Yang et al. Probability Concentration** — 解释 entropy 随 depth 递减的机制

**酌情引用:**
8-17: 其余论文视 page limit 和具体段落需求取舍

---
