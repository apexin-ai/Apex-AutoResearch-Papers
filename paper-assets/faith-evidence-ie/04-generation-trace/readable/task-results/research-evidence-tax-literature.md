# research evidence tax literature

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_evidence_tax_literature_20260519T172353_result.json`
- **Structured JSON:** [`8926d9bfdfbe0b320394.json`](../../sessions/89/8926d9bfdfbe0b320394.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

综合文献搜索和项目 `literature_map.yaml` 分析，结果如下：

---

## 最相关论文

### 1. Wei et al. (2022) — Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- **NeurIPS 2022** | [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- **核心发现**: CoT 仅在 ~100B 参数模型上有益；小模型生成"流畅但不合逻辑"的推理链，性能反而下降
- **与我们的异同**: 方向一致但维度不同——他们研究 prompting 时的 scale threshold，我们研究 SFT 训练时 evidence generation 作为 implicit CoT 的 scale-dependent tax。**我们的发现将 "CoT 收益随规模递增" 反转为 "evidence tax 随规模递减"**，且在更小的模型规模范围 (1.7B–14B) 观察到连续梯度变化，而非二元 emergent threshold

### 2. Sprague et al. (2024) — Mind Your Step (by Step): CoT can Reduce Performance
- **NeurIPS 2024** | [arXiv:2410.21333](https://arxiv.org/abs/2410.21333)
- **核心发现**: CoT 在某些任务上降低性能高达 36.3%（o1-preview vs GPT-4o）；隐式推理优于显式 token-level 推理
- **与我们的异同**: 最直接的支撑——他们证明 "显式推理可以伤害性能"，我们将其量化为 scale-dependent curve。**他们未研究 scale dependency**，我们补充了 "何时显式推理从有害变为无害" 的 scaling law

### 3. Meincke, Mollick et al. (2025) — The Decreasing Value of Chain of Thought in Prompting
- **Wharton Technical Report** | [SSRN:5285532](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5285532)
- **核心发现**: 更强的模型从 CoT 中受益越少（4-13% vs 历史 >30%），latency 增加 35-600%
- **与我们的异同**: 最接近的 "scale-dependent diminishing returns" 发现，但在 prompting 设定。**我们在 SFT fine-tuning 设定下复现了相同趋势，且提供了具体的三点 scale curve (1.7B/8B/14B)**

---

## 已在 literature_map.yaml 中的相关条目

项目已收录上述 3 篇论文（分别在 `evidence_generation_tradeoff` 类别下），以及：
- **Latent CoT survey** (Chen et al. 2025) — latent vs explicit reasoning 的理论框架
- **CoT-ER** (Yin et al. 2023, EMNLP Findings) — evidence+CoT 在 prompting 下有益 RE，与 SFT 下有害形成对比
- **Resck et al. (2024, NAACL)** — performance-explainability Pareto frontier 形式化

---

## 文献定位

**Extends prior work**: Wei et al. 和 Sprague et al. 分别建立了 "CoT 需要足够规模" 和 "CoT 可伤害性能" 两个论点，但**无人在 SFT/fine-tuning 设定下量化 evidence generation 作为 implicit CoT 的 scale-dependent performance cost curve**。我们的三点 scaling curve (−7.7pp → −0.78pp → +0.03pp) 是该方向的首个实证结果。

## 建议引用方式

1. **Wei et al. (2022)** — 引为 CoT scale-dependency 的奠基工作，说明显式推理收益的 scale 门槛已有先例
2. **Sprague et al. (2024)** — 引为 "CoT 可降低性能" 的直接证据，我们的 evidence tax 是其在 generative IE 中的实例
3. **Meincke et al. (2025)** — 引为 "CoT 收益随模型能力递减" 的最新 empirical evidence，我们在 fine-tuning 设定下 confirm 此趋势

一句话总结：**我们的 scale-dependent evidence tax curve 是 CoT scaling 文献在 generative IE fine-tuning 设定下的首个系统量化，属于 extends prior work。**

---
