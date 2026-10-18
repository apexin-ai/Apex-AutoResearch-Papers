# research decoding strategy signal attenuation

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_decoding_strategy_signal_attenuation_20260514T203338_result.json`
- **Structured JSON:** [`8346b60e82afad99cc24.json`](../../sessions/83/8346b60e82afad99cc24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搜索完成。以下是综合分析结果。

---

## 文献检索结果：解码策略 × 递归生成/模型坍塌

### 一、直接相关论文

#### 1. 模型坍塌核心文献（已讨论尾部截断机制）

| 论文 | 作者 | 年份/会议 | 核心发现 |
|------|------|-----------|----------|
| [AI models collapse when trained on recursively generated data](https://www.nature.com/articles/s41586-024-07566-y) | Shumailov et al. | 2024, Nature | 递归训练导致模型遗忘分布尾部，最终坍塌至低方差点估计。使用 top-p=0.9, τ=0.9 生成数据，但**未系统对比不同解码策略的影响** |
| [The Curse of Recursion: Training on Generated Data Makes Models Forget](https://arxiv.org/abs/2305.17493) | Shumailov et al. | 2023, arXiv | Nature 版的早期预印本，首次提出 model collapse 概念 |
| [A Tale of Tails: Model Collapse as a Change of Scaling Laws](https://arxiv.org/abs/2402.07043) | Dohmatob et al. | 2024, ICML | **关键论文**。证明递归生成对重尾分布的两种破坏方式：(1) 截断尾部 (cutting off)，(2) 压缩尾部 (narrowing)。即使 1% 合成数据混入也可触发坍塌。直接支持我们的 top-k 假说 |
| [Strong Model Collapse](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf) | — | 2025, ICLR | 更严格的理论框架 |
| [A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective](https://arxiv.org/html/2509.16499v1) | — | 2025 | 用熵衰减解释坍塌：合成数据熵逐代下降 → 模型从泛化转向记忆 |

#### 2. 解码策略对文本多样性的影响

| 论文 | 作者 | 年份/会议 | 核心发现 |
|------|------|-----------|----------|
| [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751) | Holtzman et al. | 2020, ICLR | **奠基论文**。nucleus sampling 动态调整截断阈值，适应分布形状；top-k 固定截断，在平坦分布时丢失多样性，在尖锐分布时引入噪声。Self-BLEU 和 Zipfian 分析证明 nucleus 更接近人类文本多样性 |
| [Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation](https://arxiv.org/abs/2410.06097) | Lee et al. | 2025, COLING | 大规模实证对比 top-k / top-p / temperature / beam search / contrastive search，用 diversity + coherence + MAUVE 三指标评估。nucleus 产生的局部归一化失真最小 |
| [Guided Generation for Enhanced Output Diversity in LLMs](https://aclanthology.org/2025.emnlp-main.713.pdf) | — | 2025, EMNLP | 探索引导生成提升多样性 |

#### 3. 递归生成检测/缓解

| 论文 | 作者 | 年份 | 核心发现 |
|------|------|------|----------|
| [Machine-generated text detection prevents language model collapse](https://arxiv.org/abs/2502.15654) | — | 2025 | 用机器文本检测器的置信度引导重采样，防止坍塌 |
| [Is Model Collapse Inevitable? Breaking the Curse by Accumulating Real and Synthetic Data](https://arxiv.org/html/2404.01413v2) | — | 2024 | 混合真实+合成数据可避免坍塌 |
| [Countering Model Collapse via Dynamic Center-Edge Sampling](https://www.mdpi.com/2079-9292/15/4/869) | — | 2025 | 用聚类采样策略（中心扰动+边缘过滤）延缓坍塌 |

---

### 二、关键发现与空白分析

**已有先例（部分）：**
- Dohmatob et al. (2024) 的 "tail cutting/narrowing" 理论为我们的假说提供了直接理论支撑：top-k 的固定截断 ≈ 更激进的尾部切割
- Holtzman et al. (2020) 证明了 top-k 在多样性上劣于 nucleus 的量化证据

**明确的空白（novelty 点）：**

1. **无人研究解码策略对递归生成深度信号可检测性的影响。** 现有文献关注的是解码策略如何影响生成质量/多样性，或递归训练如何导致坍塌，但**没有论文将两者连接起来研究"深度估计的准确性如何受解码策略调控"**

2. **无人量化不同解码策略下深度区分度的衰减速率。** 我们的 3×3 实验发现 top-k 导致 -8.6pp 准确率下降，这是全新的实证证据

3. **因果链是新的：** top-k 截断 → 输出更快同质化 → 深层递归文本特征趋同 → 分类器无法区分深度 —— 这条链将 Holtzman 的截断理论、Dohmatob 的尾部损失理论与我们的深度估计任务串联起来

---

### 三、literature_map.yaml

项目中尚无 `literature_map.yaml`。建议创建并补充以下条目：

| 条目 ID | 论文 | 与本项目关系 |
|---------|------|-------------|
| `shumailov2024nature` | Shumailov et al. 2024, Nature | model collapse 定义、尾部遗忘机制 |
| `shumailov2023curse` | Shumailov et al. 2023 | 早期预印本，递归训练实验设计参考 |
| `dohmatob2024tails` | Dohmatob et al. 2024, ICML | 尾部截断/压缩理论，直接支持 top-k 假说 |
| `holtzman2020nucleus` | Holtzman et al. 2020, ICLR | top-k vs nucleus 多样性对比，解码策略选择依据 |
| `lee2025decoding` | Lee et al. 2025, COLING | 解码超参数对多样性/一致性的大规模实证 |
| `collapse_closer_look2025` | 2025 | 熵衰减与泛化→记忆转变 |
| `detection_prevents2025` | 2025 | 检测驱动的坍塌预防 |

是否需要我现在创建 `literature_map.yaml` 并写入这些条目？

---
