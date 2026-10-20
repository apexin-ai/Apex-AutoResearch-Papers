# VeriCoT 深入调研报告

> 调研日期: 2026-05-14 | 目的: 为 SVS reframe 准备差异化分析

---

## 1. VeriCoT 方法总结

**论文**: VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks
**作者**: Yu Feng, Nathaniel Weir, Kaj Bostrom, Sam Bayless, Darion Cassel, Sapana Chaudhary, Benjamin Kiesl-Reiter, Huzefa Rangwala
**发表**: ICLR 2026 (Poster) | arXiv: 2511.04662 (Nov 2025)

### 1.1 核心 Pipeline

```
CoT Step Cᵢ → [Stage 1: Autoformalize → SMT-LIB Fᵢ] → [Stage 2: Extend Vocab if needed, ≤3 retries]
            → [Contradiction Check: ℱᵢ₋₁ ⊨ ¬Fᵢ ?]
            → [Entailment Check: ℱᵢ₋₁ ⊨ Fᵢ ?]
            → [Premise Generation: if not entailed, LLM proposes premises Pᵢ]
            → Output: {entailed | contradicted | ungrounded | untranslatable}
```

**关键设计决策**:
- **验证粒度**: Step-level（逐步验证，每步 Cᵢ 独立形式化并检查）
- **验证类型**: 同时做 entailment + contradiction check（两者都有）
- **形式化模型**: Claude-3.5-Sonnet-V2 负责 autoformalization 和 premise generation
- **求解器**: Z3 SMT solver，支持 linear arithmetic、uninterpreted functions、quantifiers
- **编码格式**: SMT-LIB 语言
- **Premise 来源**: LLM 生成（非题目给定），分为 source context / commonsense / prior step 三类

### 1.2 验证判定逻辑

**Binary，非 graded**。每步判定为四类之一：

| 判定 | 条件 | 含义 |
|------|------|------|
| Entailed | P ∪ {F₁,...,Fᵢ₋₁} ⊨ Fᵢ | 逻辑有效 |
| Contradicted | P ∪ {F₁,...,Fᵢ₋₁} ⊨ ¬Fᵢ | 逻辑矛盾 |
| Ungrounded | 以上均不成立 | 前提不充分 |
| Untranslatable | 3次重试仍无法形式化 | 超出 FOL 表达力 |

整条链验证结果 = pass（所有步骤 entailed）/ fail（任一步骤非 entailed）。**无连续分数**。

### 1.3 验证信号的三种用途

1. **Inference-time self-reflection**: 将验证反馈（含符号翻译、premises、solver 判定）回传给 LLM，重新生成 CoT
2. **SFT**: 用验证通过的 CoT 构建训练集
3. **DPO**: 用 (verified CoT, unverified CoT) 对构建偏好数据

---

## 2. 实验配置

### 2.1 数据集

| 数据集 | 领域 | Train | Test | 类型 |
|--------|------|-------|------|------|
| ProofWriter | 逻辑推理 | 5,000 | 400 | 规则+事实→推断 |
| BioASQ | 生物医学 QA | 5,049 | 340 | 科学推理 |
| LegalBench-SARA | 法律推理 | — | 367 | 法规解释 |

**注意**: 未测试 FOLIO、LogiQA、PrOntoQA。数据集范围比 LOGIC-LM/LINC 窄。

### 2.2 模型

| 角色 | 模型 |
|------|------|
| CoT 生成 + Autoformalization + Premise gen | Claude-3.5-Sonnet-V2 |
| Fine-tuning 目标 | Qwen2.5-7B-Instruct |

**注意**: 未做 cross-model validation（如用 GPT-4 生成 CoT + 另一模型形式化）。

### 2.3 核心指标与结果

| 数据集 | Pass Rate | Precision | VCAR |
|--------|-----------|-----------|------|
| ProofWriter | 45.2% | 94.1% | 42.5% |
| BioASQ | 25.3% | 84.3% | 21.3% |
| SARA | 15.2% | 87.0% | 13.2% |

- **Self-reflection**: 平均 +46% relative pass rate, +41% relative VCAR
- **SFT**: +3% absolute accuracy (BioASQ 77.4→79.7%, ProofWriter 47.5→51.1%)
- **DPO**: +18.4% relative pass rate improvement
- **Baseline 对比**: Pass rate 45.2% vs 14.8%（ProofWriter, baseline 未明确指定）

### 2.4 VeriCoT vs SVS 当前配置对比

| 维度 | VeriCoT | SVS (当前) |
|------|---------|-----------|
| **验证类型** | Entailment + Contradiction | Entailment (D012 pivot 后) |
| **验证粒度** | Step-level | Claim-level |
| **验证判定** | Binary (pass/fail) | Graded (entailed/total_claims 连续分数) |
| **Premise 来源** | LLM 生成 (source/commonsense/prior) | 题目给定 premises (PCV) |
| **Chain selection** | 单链验证+反思 | 多链采样+分数排序选择 |
| **形式化模型** | Claude-3.5-Sonnet-V2 | DeepSeek V3.2 |
| **链生成模型** | Claude-3.5-Sonnet-V2 | Qwen2.5-14B / DeepSeek V3.2 |
| **数据集** | ProofWriter, BioASQ, SARA | ProofWriter (当前), LogiQA (计划) |
| **训练依赖** | 无 (inference-time) + SFT/DPO | 无 (inference-time only) |
| **Pass rate** | 15-45% | ~85% formalization rate |
| **SMT 编码** | SMT-LIB | Z3 Python API |

---

## 3. Chain Selection 关键问题（核心差异化确认）

### 3.1 VeriCoT 不做 chain selection

经确认，VeriCoT：
- **仅验证单条链**，不做 multi-chain sampling
- Self-reflection 是**串行重试**（验证失败→反馈→重新生成单条链→再验证），不是并行采样
- DPO 训练时构造 (verified, unverified) pairs，但这是**训练信号**不是 inference-time selection
- 无任何 best-of-n 或 reranking 机制

### 3.2 PC-CoT 的 Certified Self-Consistency（部分相关）

PC-CoT (Typed Chain-of-Thought, ICLR 2026) 提出 "Certified Self-Consistency"：
- 采样多条 CoT → type-check 每条 → **只对通过 type-check 的链做多数投票**
- 这是 **binary filter + SC**，不是 graded scoring selection
- 数据集仅 GSM8K（数学），与逻辑推理不同赛道

### 3.3 PRoSFI 的 Graded Scoring（部分相关）

PRoSFI (ICML 2026) 用 graded reward 做 RL 训练：
- R=1.0 (correct+all verified), R=0.3 (correct+unverified), R=0.1 (incorrect), R=0.0 (format fail)
- 但这是**训练信号**，不用于 inference-time chain selection

### 3.4 结论

**"Graded formal verification score for inference-time chain selection" 是 SVS 的独特贡献点。** 现有工作要么做 binary verify（VeriCoT, LINC, LOGIC-LM），要么做 graded reward for training（PRoSFI），要么做 binary filter + SC（PC-CoT）。无人将连续验证分数直接用于 test-time chain ranking/selection。

---

## 4. 相关工作全景

### 4.1 Formal Verification for CoT（2023-2026）

| 方法 | 年份/会议 | 验证器 | 粒度 | 判定 | Chain Selection | 关键区别 |
|------|-----------|--------|------|------|----------------|----------|
| **LINC** | EMNLP 2023 | Prover9 | Problem-level | Binary | No | LLM→FOL→theorem prover，不验证 CoT 步骤 |
| **LOGIC-LM** | EMNLP 2023 | Symbolic solver | Problem-level | Binary | No | NL→符号→求解，有 self-refinement |
| **SatLM** | NeurIPS 2023 | SAT solver | Problem-level | Binary | No | 声明式编程范式 |
| **VeriCoT** | ICLR 2026 | Z3 SMT | Step-level | Binary | No | 逐步 entailment+contradiction |
| **PC-CoT** | ICLR 2026 | Type checker | Step-level | Binary (typed) | 部分 (Certified SC) | Curry-Howard 对应 |
| **VERGE** | arXiv 2026 | Z3/SMT | Step-level | Graded? | 部分 (trajectory) | 生成时集成 formal guidance |
| **PRoSFI** | ICML 2026 | Z3/Prover9 | Step-level | Graded (RL reward) | No (training only) | Structured intermediaries for RL |
| **LogicReward** | ICLR 2026 | Isabelle | Step-level | Graded (reward) | No (training only) | 形式验证→reward for SFT/DPO |
| **SVS (ours)** | — | Z3 SMT | Claim-level | Graded (continuous) | **Yes** | Graded IC for chain selection |

### 4.2 关键观察

1. **Binary → Graded 趋势明显**: 2023 年工作全是 binary，2026 年开始出现 graded scoring（PRoSFI, VERGE, LogicReward），但都用于 training reward
2. **Chain selection 空白**: 无人将 formal verification score 用于 inference-time chain selection
3. **Autoformalization 是共同瓶颈**: VeriCoT 45% pass rate, PC-CoT 40-60% typing rate，说明 LLM→formal 翻译远未成熟

---

## 5. VeriCoT 局限性分析

### 5.1 已确认局限

| 局限 | 严重程度 | SVS 是否克服 |
|------|----------|-------------|
| **极低 pass rate** (15-45%) | 致命 | 部分——SVS 85% formalization rate 但粒度不同不直接可比 |
| **Premise 由 LLM 生成** | 中等 | SVS 用题目 premises (PCV)，更可靠 |
| **Binary 判定丢失信息** | 中等 | SVS graded scoring 保留连续信息 |
| **单链验证无选择能力** | 中等 | SVS 多链选择 |
| **仅 Claude-3.5 做形式化** | 中等 | 部分——SVS 用 DeepSeek V3.2，也是单一模型 |
| **数据集窄** (3个) | 次要 | 部分——SVS 当前也只有 ProofWriter |
| **无 cross-model validation** | 次要 | 计划中（Qwen chain gen + DeepSeek formalization） |
| **Autoformalization faithfulness 未验证** | 中等 | 共同问题 |

### 5.2 VeriCoT pass rate 低的根因

ProofWriter 上 45.2% pass 意味着 **54.8% 的 CoT 无法通过验证**。可能原因：
1. Step-level 逐步累积验证过于严格——任一步失败全链失败
2. LLM-generated premises 质量不稳定
3. 跨步 vocabulary 对齐困难
4. SMT-LIB 编码限制

SVS 的 claim-level 验证 + 连续分数设计天然对此更鲁棒——即使部分 claim 无法验证，仍可输出有区分力的分数。

---

## 6. 差异化分析与 Reframe 建议

### 6.1 SVS 残余差异化（按强度排序）

| 差异点 | 强度 | 支撑论据 | 需要的实验证据 |
|--------|------|----------|---------------|
| **Graded IC for chain selection** | ⭐⭐⭐ 强 | 无人做过；binary filter+SC 是最近 alternative | d > 0.15 + ablation: graded IC vs binary filter+SC |
| **PCV (题目 premises 驱动)** | ⭐⭐ 中 | VeriCoT 用 LLM-gen premises 有 fabrication 风险 | PCV vs LLM-gen premise ablation |
| **实用 pass rate** | ⭐⭐ 中 | VeriCoT 15-45%，SVS 85% formalization | 直接对比数字 |
| **Training-free** | ⭐ 弱 | VeriCoT 也是 training-free at inference | — |

### 6.2 Reframe 方向建议

**如果 entailment IC 实验成功 (d > 0.15)**:

**推荐 framing**: "Graded Formal Verification as a Test-Time Chain Selection Mechanism"

核心 narrative:
> 现有 formal verification for CoT 工作（VeriCoT, LINC, LOGIC-LM）将验证视为 binary accept/reject，丢弃大量信息。我们提出将 claim-level entailment checking 转化为连续验证分数（IC score），首次实现 formal-verification-guided test-time chain selection。相比 binary filter + self-consistency，graded selection 在 [数据集] 上提升 [X]%。

**必须做的 ablation**:
1. **SVS graded IC** vs **Binary filter + SC** (模拟 VeriCoT 风格)
2. **SVS graded IC** vs **SC alone** (baseline)
3. **PCV (题目 premises)** vs **LLM-generated premises** (区分于 VeriCoT)
4. **IC score 分布分析**: correct vs wrong chains 的 IC 分数分布可视化

**论文 Related Work 定位**:
- VeriCoT → "binary single-chain verification; we extend to graded multi-chain selection"
- VERGE → "MCS for error localization + refinement; we use MCS-derived score for selection"
- PRoSFI → "graded reward for training; we use graded score at inference without training"
- PC-CoT → "Certified Self-Consistency = binary filter + SC; we show graded scoring outperforms"

### 6.3 Reframe 需要回答的 Reviewer 预期问题

1. **"Graded scoring 比 binary filter+SC 好多少？"** → 必须有 ablation 数字
2. **"为什么不直接用 VeriCoT 的 pass/fail 做 filter？"** → 需证明 graded 的信息增益
3. **"Autoformalization 本身可靠吗？"** → 需要 faithfulness analysis 或 caveat
4. **"为什么只在 ProofWriter 测？"** → 需扩展至少一个数据集

---

## 7. 风险评估与备选方向

### 7.1 如果 entailment IC 成功 (d > 0.15)

- **乐观路径**: Graded chain selection 是清晰的贡献点，论文可行
- **需补充**: Binary filter ablation + 第二数据集 + faithfulness analysis
- **目标会议**: ACL/EMNLP 2026 或 NeurIPS 2026

### 7.2 如果 entailment IC 弱信号 (0 < d ≤ 0.15)

- **分层分析**: True/False 子集可能有信号（61% Unknown 是 confound）
- **数据集切换**: ProofWriter depth-1/2/3 可能更适合（推理链短，形式化更准确）
- **FOLIO**: 更多 True/False，更少 Unknown

### 7.3 如果 entailment IC 失败 (d ≤ 0)

**备选方向 A: 方法论比较研究**
- "Formal Verification Scores as Chain Selectors: A Systematic Comparison"
- 比较 IC score / binary filter / self-consistency / ORM 在多数据集上的表现
- 贡献点：系统性 benchmark + 失败模式分析
- 风险：纯比较研究 novelty 偏低

**备选方向 B: Autoformalization Faithfulness**
- arXiv:2604.19459 揭示 axiom fabrication + premise mistranslation
- SVS 框架可用于检测 autoformalization 错误（IC 低→可能形式化不忠实）
- 贡献点：formalization faithfulness detector
- 风险：需要 gold FOL annotations

**备选方向 C: Hybrid Scoring**
- 将 IC score 与 LLM-based verifier（如 LogicReward）组合
- formal verification 捕捉逻辑错误，learned verifier 捕捉语义错误
- 贡献点：互补融合
- 风险：engineering complexity

---

## 8. 搜索来源

- [VeriCoT Paper (arXiv)](https://arxiv.org/abs/2511.04662)
- [VeriCoT OpenReview](https://openreview.net/forum?id=zHuV3Vatov)
- [VeriCoT Full HTML](https://arxiv.org/html/2511.04662v1)
- [PC-CoT / Typed Chain-of-Thought](https://arxiv.org/pdf/2510.01069)
- [VERGE](https://arxiv.org/pdf/2601.20055)
- [PRoSFI](https://arxiv.org/html/2603.29500v1)
- [LogicReward GitHub](https://github.com/Aiden0526/Logic-Reward)
- [LINC](https://arxiv.org/abs/2310.15164)
- [LOGIC-LM](https://arxiv.org/abs/2305.12295)
- [SatLM](https://arxiv.org/abs/2305.09656)
- [VeriCoT Summary](https://www.emergentmind.com/topics/vericot)
