# research literature linkage eval results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_linkage_eval_results_20260518T201311_result.json`
- **Structured JSON:** [`32c80a7d98b4b44d853c.json`](../../sessions/32/32c80a7d98b4b44d853c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 文献联动分析结果

### 一、literature_map 中已有的相关论文

**Rejection Sampling / Selection Strategy 相关（7篇核心）：**
- **RAFT** (TMLR 2024) — 经典 RSFT 框架：迭代 generate-rank-filter-SFT
- **A Minimalist Approach** (arXiv 2504.11343, 2025) — key_theoretical_support。RAFT 匹配 GRPO/PPO 性能，GRPO 优势主要来自丢弃全错 prompt 而非 reward normalization
- **RS-DPO** (NAACL 2024 Findings) — 系统组合 rejection sampling + DPO，有 threshold/temperature 敏感性 ablation
- **RIFT** (arXiv 2601.09253, 2026) — direct_competitor。指出 RSFT 丢弃负样本的浪费，提出 reward-informed reweighting
- **AdaSTaR** (NeurIPS 2025) — RSFT random sampling 导致训练不平衡，提出 diversity + curriculum sampling，减少 58.6% FLOPs
- **TrajFusion** (arXiv 2602.04391, 2026) — 超越 binary accept/reject，融合部分正确轨迹
- **Rejection Sampling Secretly Performs PPO** (ICML 2025) — RSFT 与 PPO 在 marginal KL 约束下理论等价

**GRPO for IE 相关（7篇核心）：**
- **R1-RE** (arXiv 2507.04642, 2025) — direct_competitor。首个 RLVR (GRPO + verifiable reward) 用于 RE
- **ReasoningNER** (arXiv 2511.11978, 2025) — direct-competitor。GRPO 用于 NER，composite reward
- **EvidenceRL** (arXiv 2603.19532, 2026) — closest_competitor。GRPO 同时优化 grounding + correctness，hallucination 减少 5x
- **E-GRPO** (ICLR 2026) — closest_prior_work。Entity-aware reward 给 near-miss 负样本部分分数
- **GDPO** (ICML 2026) — closest_prior_work。多 reward GRPO 归一化 collapse 问题
- **R2GRPO** (arXiv 2505.22068, 2025) — MimicSFT + relevance/rule-mining reward 用于科学 IE
- **MORE-R1** (arXiv 2603.09478, 2026) — GRPO 用于多模态 RE

**训练动态 / Learning Curve 相关（5篇核心）：**
- **DAPO** (NeurIPS 2025) — entropy collapse 诊断；accuracy=0/1 prompt 产生零梯度
- **Dr. GRPO** (COLM 2025) — std(r)→0 导致 advantage explosion
- **Defeating the Training-Inference Mismatch via FP16** (arXiv 2510.26788, 2025) — BF16 在 150-600 steps 导致 collapse（与你们 GRPO bf16 实验直接相关）
- **RFT Naturally Mitigates Forgetting** (arXiv 2507.05386, 2025) — RFT 梯度被 reward variance 缩放，充当 regularizer
- **R1-RE** — GRPO 训练后 sentence-level RE 无 catastrophic forgetting

### 二、Web 搜索新发现（map 中可能缺少的）

| 论文 | Venue/Year | 关键发现 | 是否建议加入 map |
|------|-----------|---------|----------------|
| **RFT (Yuan et al.)** "Scaling Relationship on Learning Mathematical Reasoning" | arXiv 2308.01825, 2023 | rejection sampling 关键因子是 distinct reasoning paths 数量而非仅正确性；LLaMA-7B GSM8K 35.9%→49.3% | **是** — selection quality/diversity 的基础性证据，支撑 CED vs random 实验 |
| **GTPO** "Stabilizing GRPO via Gradient and Entropy Control" | arXiv 2508.03772, 2025 | 解决 GRPO gradient conflicts + policy collapse | 检查是否已在 map — 如无则加入 |
| **GRPO Effective Loss** (arXiv 2503.06639, 2025) | arXiv, 2025 | GRPO 渐近等价于 oracle policy gradient，理论最优性证明 | 检查是否已在 map |
| **Reward-based Input Construction for Cross-doc RE** | arXiv 2405.20649, 2024 | RL 训练 input sentence selection for RE | **是** — RL + RE 的直接先例 |
| **Adaptive RL Planning for Complex IE** | arXiv 2406.11455, 2024 | RL + LLM for IE，address false positives | **是** — RL + LLM IE 的最相关先例 |
| **Hierarchical Framework for RE with RL** (Takanobu et al.) | arXiv 1811.03925, 2018 | 早期 RL for joint entity-relation extraction | 可选 — 经典但较老 |

### 三、与实验结果的文献关联

**Random vs CED RSFT (gap=4.82pp)：**
- literature_map 已覆盖 RSFT 方法论论文（RAFT, AdaSTaR, RIFT），但**缺少 RFT (Yuan et al. 2023) 这篇 selection quality 的基础性实证**。该论文证明 distinct reasoning paths > random sampling，直接支撑 CED scoring 的价值。
- 无论文在 IE 任务上做过 scored vs random ablation — 你们的 4.82pp gap 是该领域的新数据点。

**GRPO bf16 ckpt-100 (+3.74pp over SFT)：**
- R1-RE 报告了 GRPO 在 sentence-level RE 上无 catastrophic forgetting，但未报告 learning curve。
- BF16 collapse 论文 (arXiv 2510.26788) 值得关注 — 需监控 GRPO 训练后期是否出现类似 collapse。
- EvidenceRL 是最直接的对比对象（也用 GRPO 优化 evidence grounding）。

### 四、建议

**建议更新 literature_map：**
1. 加入 **RFT (Yuan et al. 2023)** — role: theoretical_support，category: rsft_methodology。selection diversity/quality 的基础性证据。
2. 加入 **Reward-based Input Construction for Cross-doc RE** (2024) — role: related_method，category: rl_for_ie
3. 加入 **Adaptive RL Planning for Complex IE** (2024) — role: related_method，category: rl_for_ie
4. 检查 **GTPO** 和 **GRPO Effective Loss** 是否已在 map 中，如无则补充

---
