# RSFT + DocRE Literature Scan Report
**Date**: 2026-05-15
**Scope**: Rejection sampling for IE/RE, recent DocRE methods, RL for IE, CED-related work

---

## 1. New Papers Found

### Direct Competitors (RL for RE/IE)

| Paper | Venue | Role | Key Difference from FREIGE |
|-------|-------|------|---------------------------|
| **R1-RE** (Dai et al., arXiv 2507.04642) | arXiv 2025 | `direct-competitor` | 首个 RLVR for RE。但：句子级 RE（SemEval-2010），非 DocRE；用 online GRPO 非 RSFT；无 evidence 组件；关注 OOD 泛化而非 evidence quality |
| **MORE-R1** (arXiv 2603.09478) | arXiv 2026 | `method-component` | 多模态 RE + GRPO。不同模态，但验证 RL for RE 趋势 |
| **REAR** (Luo et al.) | EMNLP 2025 Findings | `method-component` | RL for Event Argument Extraction。不同 IE 子任务，非 DocRE |
| **Graph-R1** (Luo et al., arXiv 2507.21892) | ICML 2026 | `background` | Agentic GraphRAG + RL，含 n-ary RE。QA 场景非 DocRE |

### RSFT Methodology

| Paper | Venue | Role | Relevance |
|-------|-------|------|-----------|
| **"Minimalist Approach: Rejection Sampling to Reinforce"** (Xiao et al., arXiv 2504.11343) | arXiv 2025 | `key-theoretical-support` | 证明 RAFT 与 GRPO 表现相当；GRPO 优势主要来自丢弃全错 prompt。直接支持我们 RSFT > GRPO 的发现 |
| **TrajFusion** (Deng et al., arXiv 2602.04391) | arXiv 2026 | `method-component` | 超越传统 RSFT：融合错误+正确轨迹。Future work 方向 |
| **"RSFT Secretly Performs PPO"** (ICML 2025) | ICML 2025 | `theoretical-support` | RSFT 隐式执行 constrained PPO。为 RSFT 有效性提供理论基础 |

### Recent LLM-based DocRE Methods

| Paper | Venue | Role | Relevance |
|-------|-------|------|-----------|
| **RelPrior** (arXiv 2511.08143) | arXiv 2025 | `key-baseline` | 已知 baseline，+2.06-2.38pp。我们 +5.98pp 显著更优 |
| **LMRC** (arXiv 2408.13889) | arXiv 2024 | `method-component` | Two-stage DocRE (filter NA pairs + LLM classify) |
| **Ru-LLM** (NLPCC 2025) | NLPCC 2025 | `method-component` | 逻辑规则约束 LLM for DocRE，inference-time 验证 |
| **GLiDRE** (arXiv 2508.00757) | arXiv 2025 | `background` | Dual-encoder 零/少样本 DocRE，不同范式 |
| **AutoRE** (arXiv 2403.14888) | arXiv 2024 | `background` | Mistral-7B + QLoRA for DocRE，我们 SFT baseline 类似 |
| **Adaptive RL Planning for IE** (arXiv 2406.11455) | arXiv 2024 | `background` | RL 优化抽取顺序，非模型微调 |

---

## 2. Novelty Assessment

**结论：我们的 novelty 完全成立，且独特性更加清晰。**

### 三个核心新颖点均无先例：

1. **RSFT for DocRE（首次）**
   - 搜索未发现任何在 IE/RE 任务上使用 rejection sampling / RSFT 的工作
   - R1-RE 是最接近的竞争者，但用 online GRPO 而非 offline RSFT，且是句子级 RE
   - RSFT 在 NLP 领域主要用于 math reasoning，向 structured IE 的迁移是全新的

2. **NLI-based CED Reward for RE Training（首次）**
   - 无人用 NLI evidence discrimination 作为 RE 训练的 reward signal
   - Drift (ACL 2025) 用 faithfulness reward 但针对 rationale generation
   - CED 的对比判别结构在 IE 中完全没有先例

3. **GRPO 在 DocRE 上的 catastrophic forgetting 分析（首次）**
   - R1-RE 在句子级 RE 上 GRPO 成功，但我们发现 DocRE 上 GRPO 全线失败
   - 这个 negative result 本身就有价值，配合 RSFT 的成功形成完整故事

### 定量优势：
- 我们 +5.98pp rel_F1 vs RelPrior +2.06-2.38pp
- RSFT 同时提升 rel_f1 和 evi_f1，不存在 trade-off

---

## 3. Suggested Citations

### Must Cite（核心引用）

1. **R1-RE** (arXiv 2507.04642) — 最接近的 RL for RE 工作，需要明确区分
2. **"Minimalist Approach"** (arXiv 2504.11343) — RSFT 理论支撑，证明 RSFT 与 GRPO 竞争力
3. **RelPrior** (arXiv 2511.08143) — LLM-based DocRE SOTA baseline
4. **"RSFT Secretly Performs PPO"** (ICML 2025) — RSFT 理论基础

### Should Cite（重要背景）

5. **REAR** (EMNLP 2025) — RL for IE 趋势验证
6. **MORE-R1** (arXiv 2603.09478) — RL for RE 跨模态趋势
7. **LMRC** (arXiv 2408.13889) — LLM-based DocRE 方法对比
8. **TrajFusion** (arXiv 2602.04391) — RSFT 进展，future work 连接
9. **AutoRE** (arXiv 2403.14888) — LLM + QLoRA for DocRE baseline
10. **Ru-LLM** (NLPCC 2025) — 规则约束 DocRE，与 CED 的 inference vs training 对比

### Optional Cite（视空间）

11. **Graph-R1** (ICML 2026) — RL + knowledge extraction 广义趋势
12. **GLiDRE** (arXiv 2508.00757) — DocRE 领域活跃度
13. **Adaptive RL Planning for IE** (arXiv 2406.11455) — RL for IE 早期工作

---

## 4. Positioning Recommendations

### Related Work 结构建议：
- **RL/RSFT for NLP**: R1-RE, REAR, MORE-R1, "Minimalist Approach", "RSFT=PPO"
- **LLM-based DocRE**: RelPrior, LMRC, Ru-LLM, AutoRE
- **Evidence & Faithfulness Rewards**: Drift, INFUSE, CED（我们的）

### Key Framing：
> While R1-RE (2025) first applied RLVR to sentence-level RE with online GRPO, document-level RE presents unique challenges—structured multi-triple output and evidence grounding—that make online RL unstable (catastrophic forgetting). We show that offline RSFT with NLI-based CED reward provides a more effective training paradigm, achieving +5.98pp rel_F1 improvement on DocRED, significantly outperforming prior LLM-based methods like RelPrior (+2.38pp).
