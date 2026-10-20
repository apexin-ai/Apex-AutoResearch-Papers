# PALADIN 深度对比分析 + Negative Result Paper 相关工作

调研日期: 2026-05-14

---

## 1. PALADIN 深度分析 (arXiv 2509.25238)

### 1.1 基本信息
- **标题**: PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases
- **作者**: Sri Vatsa Vuddanti, Aarav Shah, Satwik Kumar Chittiprolu, Tony Song, Sunishchal Dev, Kevin Zhu, Maheep Chaudhary
- **日期**: September 25, 2025
- **状态**: arXiv preprint (无正式会议发表记录)

### 1.2 Recovery Rate 数字验证

**paper_framing.md 写的 32.76% → 89.68% — ✅ 已确认准确**

完整结果表 (PaladinEval benchmark):

| Model | Baseline RR | PALADIN RR | Baseline TSR | PALADIN TSR | PALADIN CSR |
|-------|------------|------------|-------------|-------------|-------------|
| Gemma-3-12B-Instruct | 32.76% | 89.7% | 57.4% | 87.4% | 82.6% |
| Qwen-2.5-14B-Instruct | 33.48% | 94.7% | — | 79.5% | 94.6% |
| LLaMA-3.1-8B-Instruct | 21.83% | 79.8% | 17.5% | 78.7% | 80.7% |
| AM-Thinking V1 | — | 96.1% | — | 81.2% | 88.7% |

Baselines 对比: PALADIN (Gemma, 89.7% RR) > CRITIC (76.34% RR) > ToolReflect > ToolBench Agent > Vanilla

### 1.3 ToolScan Taxonomy: 7 个 Failure Types

来源: ToolScan (arXiv 2411.13547, Kokane et al., Nov 2024, 18 位作者)

| # | Error Type | 描述 | 与我们的 Operator 对比 |
|---|-----------|------|----------------------|
| 1 | Tool Hallucination | 调用不存在的工具 | 无对应 — ALFWorld 无 tool catalog |
| 2 | Argument Hallucination | 参数错误或缺失 | 类似 C1 (context_truncation) 的信息缺失 |
| 3 | Invalid Tool Invocation | 工具调用格式/语法错误 | 无对应 — ALFWorld action 无严格 API schema |
| 4 | Partial Tool Execution | 工具返回不完整 | 类似 C4 (observation_masking) |
| 5 | Tool Output Hallucination | 编造工具返回结果 | 无对应 — ALFWorld 环境返回真实 observation |
| 6 | Invalid Intermediate Reasoning | 推理链路错误 | 类似 P1 (step_order_swap) + P2 (sub_goal_deletion) |
| 7 | Re-entrant Error Handling | 无限重试/循环 | 无对应 — ALFWorld 无 retry 机制 |

**核心差异**: ToolScan 的 7 类中有 5 类（1/2/3/5/7）是 tool-use 特有的、**具备显式错误信号**的 failure mode。ALFWorld 的 4 个 operators 没有显式错误信号 — 这支持了 paper_framing 中 "error observability" 的假说。

### 1.4 训练规模

| 维度 | PALADIN | TaxEI (ours) | 差异倍数 |
|------|---------|-------------|---------|
| 总 trajectories | 50K+ | 9,029 | ~5.5× |
| 注入比例 | 80% failure / 20% clean | ~52% injected / 48% clean | PALADIN 更激进 |
| Epochs | 1 | — | — |
| Base models | Gemma-3-27B, Qwen-2.5-14B, LLaMA-3.1-8B, AM-Thinking V1 | Qwen3-8B | PALADIN 多模型验证 |
| LoRA config | rank=16, α=32, bf16 | — | — |
| 硬件 | NVIDIA H200 SXM | RTX 5090 ×4 | — |
| 数据生成 | GPT-5 API | GPT-5.2 | — |

**重要发现**: PALADIN 用 80% failure / 20% clean 比我们的 50/50 更激进，但在 5× 更大的数据规模上。这提示**规模可能是关键变量** — 80% injection 在 50K 样本上可能提供足够的 recovery pattern diversity，但在 9K 样本上就变成噪声。

### 1.5 多 Seed 验证与统计检验

- **PALADIN 没有报告多 seed 验证。** 没有跨 random seed 的 variance/std。
- 统计显著性: Bootstrap N=1000, p<0.01
- 评估用固定 seed=42 (GPT-5 grading)
- **这是一个可利用的弱点**: 我们的 paper 可以指出 PALADIN 的单 seed 评估可能掩盖了训练不稳定性，而我们的多 seed 实验揭示了 error injection 导致的高方差问题。

### 1.6 PALADIN 的系统组成

**关键发现 — PALADIN 不仅仅是 SFT**:
- Training: LoRA fine-tuning on 50K+ recovery trajectories
- **Inference**: Taxonomy-driven retrieval from 55+ failure exemplars

Ablation 结果 (去掉 inference-time retrieval):
| Model | Full RR | w/o Retrieval RR | Drop |
|-------|---------|-----------------|------|
| Gemma-12B | 89.7% | 61.4% | -28.3pp |
| Qwen-14B | 94.7% | 73.3% | -21.4pp |
| LLaMA-8B | 79.8% | 48.6% | -31.2pp |

**意义**: PALADIN 的 +57pp 提升中，约 30pp 来自 inference-time retrieval，不是纯 SFT 效果。我们的 TaxEI 是纯 SFT，没有 retrieval augmentation。这是一个重要的 confound，paper 中应该讨论。

### 1.7 PALADIN 没有涉及 embodied planning — ✅ 已确认

---

## 2. ALFWorld SOTA 水位

| Method | ALFWorld SR | Year | Type | 备注 |
|--------|------------|------|------|------|
| Reflexion + GPT-4 | ~97% | 2023 | Multi-trial self-reflection | 最多 12 轮 retry，非单次 |
| CoEx | 93.28% | 2025 (EMNLP Findings) | World model + hierarchical planning | 单次，arXiv 2507.22281 |
| AgentPRM (3B) | 91.0% | 2025 | Process reward model + actor-critic | 70K rollouts, arXiv 2502.10325 |
| InversePRM (3B) | 86.6% | 2025 | Inverse process reward | 更 sample-efficient |
| ReAct + GPT-4 | ~73% | 2023 | Few-shot prompting | 单次 |
| **Our Vanilla SFT (Qwen3-8B)** | **65.3%** | **2026** | **SFT on GPT-5.2 trajectories** | **3-seed mean** |
| BUTLER (original) | ~45% | 2021 | DAgger in TextWorld | 原始基线 |

**我们的 65.3% 定位**: 低于 GPT-4 few-shot (73%) 但远高于原始 BUTLER (45%)。在 SFT-only、开源 8B 模型的范畴内算合理水平，但离 SOTA (93%) 有显著差距。这为 paper 提供了上下文 — 我们的 vanilla baseline 本身是功能性的（+22.7pp over baseline），degradation 来自 injection augmentation。

---

## 3. 相关 Negative Result Papers & 学习从失败中学习的工作

### 3.1 直接竞争/互补论文

#### (a) Exploring Expert Failures (EEF)
- **arXiv**: 2504.13145 (Apr 2025)
- **作者**: Li-Cheng Lan et al.
- **核心**: 从失败的 expert trajectories 中提取有价值的 action，加入 SFT 训练
- **结果**: WebShop 62% win rate (vs RFT 53.6%, GPT-4 35.6%)；SciWorld >81
- **关键区别**: EEF 从真实失败中**提取好的部分**，我们是**主动注入坏的部分**。EEF 成功因为它保留了 beneficial signal；我们失败可能因为 injection 引入了 noise 而非 signal
- **对我们 paper 的意义**: 强化 "error injection ≠ learning from errors" 的论点

#### (b) AgentDebug / AgentErrorTaxonomy
- **arXiv**: 2509.25370 (Sep 2025)
- **作者**: Kunlun Zhu et al. (UIUC, 18 co-authors)
- **核心**: 跨 ALFWorld/GAIA/WebShop 的错误分类法 (5 维: memory/reflection/planning/action/system) + debugging framework
- **结果**: +24% all-correct accuracy, +17% step accuracy, up to 26% task success improvement
- **关键区别**: 他们分析**真实 agent 失败**并提供**针对性反馈**，不是 SFT data augmentation
- **对我们 paper 的意义**: 他们的 taxonomy 比我们更细粒度，但方法论完全不同（inference-time debugging vs training-time injection）

#### (c) CRITIC
- **arXiv**: 2305.11738 (May 2023, published ICLR 2024)
- **作者**: Zhibin Gou, Zhihong Shao et al.
- **核心**: Tool-interactive self-correction — LLM 用外部工具验证并修正自己的输出
- **与 PALADIN 的关系**: PALADIN 的 baseline，PALADIN outperforms CRITIC by +13.3pp RR

#### (d) "LLMs Cannot Self-Correct Reasoning Yet"
- **arXiv**: 2310.01798 (Oct 2023, published ICLR 2024)
- **核心**: 没有外部反馈时 LLMs 无法可靠自我纠正，有时反而更差
- **对我们 paper 的意义**: 支持 "内部错误处理在缺乏显式反馈时困难" 的论点。ALFWorld 正是缺乏显式错误反馈的场景

### 3.2 Embodied Planning 相关工作

#### (e) Reflective Test-Time Planning (RTTP)
- **arXiv**: 2602.21198 (Feb 2026)
- **核心**: Test-time reflection for embodied LLMs, coupling reflection-in-action + reflection-on-action
- **结果**: 33.65% avg SR vs best baseline 11.20% on long-horizon household tasks
- **对我们 paper 的意义**: 他们发现 embodied LLMs 是 "brittle static oracles that cannot learn from failures" — 直接支持我们的 negative finding

#### (f) XENON / Experience-based Knowledge Correction
- **arXiv**: 2505.24157 (May 2025)
- **核心**: 从经验中算法化修正知识，解决 LLMs 的错误先验
- **对我们 paper 的意义**: 与我们的 taxonomy labels 不同，XENON 在 test-time 修正知识而非 training-time augmentation

#### (g) Imagine-then-Plan (ITP)
- **arXiv**: 2601.08955 (Jan 2026)
- **核心**: World model + adaptive lookahead for agent learning
- **评估**: ALFWorld + ScienceWorld + WebShop + StableToolBench
- **对我们 paper 的意义**: 代表 embodied planning 的另一条路径 — world model 而非 error injection

#### (h) LEAFE / Internalizing Agency from Reflective Experience
- **arXiv**: 2603.16843 (Mar 2026)
- **核心**: 从反思性经验中内化 agency，强调 "robust decision-making under feedback"
- **对我们 paper 的意义**: 进一步证明 embodied domain 需要 feedback loop，不是静态 SFT augmentation

### 3.3 Data Augmentation 负面结果

#### (i) 小规模 synthetic data 的反效果
- **来源**: Llama 3 8B translation SFT 实验 (Sep 2024)
- **发现**: 1K-2K augmented samples 实际**降低**了性能；需要 207K 才看到 +13 BLEU 提升
- **对我们 paper 的意义**: 直接支持 "scale 不够时 augmentation 反而有害" 的假说。我们的 4.7K injected samples 可能正处于有害区间

#### (j) Model Collapse from Synthetic Data
- **来源**: 2025 多项研究
- **发现**: 迭代在自身输出上 fine-tune 会导致 "model collapse"；scaling up 不能克服 bias 反而可能加剧
- **对我们 paper 的意义**: 我们的 injected trajectories 是 GPT-5.2 生成 + 程序化注入，不完全是 "自身输出"，但 synthetic corruption 的噪声效应类似

### 3.4 其他 Taxonomy-Guided Error Injection 工作

**除 PALADIN 外，没有找到其他 taxonomy-guided error injection for agent training 的工作。** PALADIN 是这个方向的开创性工作，我们是第一个尝试将其迁移到 embodied planning 的（也是第一个报告失败的）。

---

## 4. Insights from Negative Results Workshop

### 4.1 Workshop 信息
- **全称**: Workshop on Insights from Negative Results in NLP
- **历史**: 2020 (EMNLP), 2021 (EMNLP), 2022, 2024
- **2026**: Co-located with EMNLP 2026, Budapest, Oct 22-29
- **官网**: https://insights-workshop.github.io/

### 4.2 投稿要求 (基于历史 CFP，2026 CFP 尚未发布)
- **Short papers**: ≤4 pages (excluding references), EMNLP two-column format
- **Non-archival abstracts**: 1-2 pages for previously published work
- **Archival**: 原创短论文进入 proceedings
- **Appendix**: 可附 PDF (preprocessing, model params, pseudocode 等)

### 4.3 受欢迎的主题
- 跨硬件/random seed 的稳定性问题 ✅ (我们有 3.3× variance)
- Ablation 研究揭示组件贡献膨胀 ✅ (taxonomy labels 无显著优于 random)
- 数据集/技术跨域泛化失败 ✅ (tool-use → embodied 迁移失败)
- 预训练 vs fine-tuning 贡献分析
- 广泛适用的训练/微调建议 ✅ (injection ratio 与 scale 的交互)

### 4.4 审稿标准
- 强调**严谨方法论** + **解释性假说**
- 不是简单报告实验失败，而是要有 insight
- 我们的 paper 完美契合: 有清晰的 structural analysis (6 维对比 tool-use vs embodied planning)

---

## 5. 关键发现总结

### 5.1 paper_framing.md 数字校验

| Claim | paper_framing 写的 | 实际验证 | 状态 |
|-------|-------------------|---------|------|
| PALADIN RR baseline | 32.76% | 32.76% (Gemma-3-12B) | ✅ 准确 |
| PALADIN RR improved | 89.68% | 89.7% (四舍五入差异) | ✅ 准确 |
| ToolScan 7 failure types | 7 | 7 | ✅ 准确 |
| 50K+ trajectories | 50K+ | 50K+ | ✅ 准确 |
| 80% recovery / 20% clean | 80/20 | 80% failure-rich / 20% clean | ✅ 准确 |
| +57pp Recovery Rate | +57pp | +56.94pp (32.76→89.7) | ✅ 准确 |

### 5.2 paper_framing.md 需要更新的内容

1. **PALADIN 不是纯 SFT**: 包含 inference-time retrieval (55+ exemplars)。去掉 retrieval 后 RR 降 ~30pp。当前 framing 没有提及这一点，应补充为额外 confound
2. **ALFWorld SOTA 应补充**: CoEx 93.28%, AgentPRM 91.0% — 提供我们 65.3% 的上下文
3. **相关工作 EEF 很重要**: "从失败中提取好信号" vs "注入坏信号" 是不同路径，EEF 成功而我们失败，强化了 "injection 方向错误" 的论点
4. **PALADIN 也没做多 seed**: 可以在 paper 中指出这是该领域的普遍问题，我们的多 seed 实验反而是贡献

### 5.3 对 Paper Framing 的建议

**新增对比维度**: 除了现有的 6 维对比，建议增加第 7 维:

| Dimension | Tool-Use (PALADIN ✓) | Embodied Planning (TaxEI ✗) |
|-----------|----------------------|------------------------------|
| **System architecture** | SFT + inference-time retrieval (55+ exemplars) | Pure SFT, no retrieval | 

这意味着 PALADIN 的成功可能部分归因于 retrieval augmentation 而非纯 error injection。

---

## 6. 推荐引用列表

### 必引 (核心对比)
1. PALADIN — arXiv 2509.25238, Vuddanti et al., 2025
2. ToolScan — arXiv 2411.13547, Kokane et al., 2024
3. CRITIC — arXiv 2305.11738, Gou et al., 2023 (ICLR 2024)
4. ALFWorld — arXiv 2010.03768, Shridhar et al., 2021

### 强烈推荐引 (支撑论点)
5. EEF — arXiv 2504.13145, Lan et al., 2025 (失败 trajectory 的正确利用方式)
6. AgentDebug — arXiv 2509.25370, Zhu et al., 2025 (agent error taxonomy + ALFWorld)
7. "LLMs Cannot Self-Correct" — arXiv 2310.01798, Huang et al., 2024 (ICLR 2024)
8. AgentPRM — arXiv 2502.10325, Choudhury, 2025 (ALFWorld SOTA context)

### 可选引 (丰富讨论)
9. CoEx — arXiv 2507.22281, Kim et al., 2025 (EMNLP Findings, ALFWorld SOTA)
10. RTTP — arXiv 2602.21198, 2026 (embodied LLM brittleness)
11. Reflexion — arXiv 2303.11366, Shinn et al., 2023 (NeurIPS 2023, ALFWorld multi-trial)
12. LEAFE — arXiv 2603.16843, 2026 (reflective experience for agents)
