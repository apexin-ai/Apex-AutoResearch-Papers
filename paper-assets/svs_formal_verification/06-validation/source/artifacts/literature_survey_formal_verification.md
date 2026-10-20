# 文献调研：形式验证 + LLM 推理链验证

> 调研日期：2026-05-14
> 覆盖时间范围：2024–2026

---

## ⚠️ Novelty 风险警告

**发现两篇高度相似的竞品论文：**

1. **VeriCoT** (2025.11) — 将 CoT 每步 formalize 为 FOL (SMT-LIB)，用 Z3 做逻辑一致性/蕴含检查
2. **VERGE** (2026.01) — 将 LLM 输出分解为原子 claims，autoformalize 为 FOL，用 Z3 验证，**且使用 Minimal Correction Subsets (MCS) 定位错误**

我们的方法核心组件（FOL formalization + Z3 + MCS）在这两篇论文中均已出现。**但我们的差异化要素——IC 量化评分 (MCS_size/total_claims) 作为 graded verifier 用于 chain selection、以及 Premise-Conditioned Verification (PCV) 概念——尚未被覆盖。** 详见第五节 Novelty 评估。

---

## 一、直接竞品（方法高度相似）

### 1.1 VeriCoT — 🔴 高风险

- **标题**: VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks
- **年份/会议**: 2025.11, arXiv 2511.04662, OpenReview 投稿
- **核心方法**:
  - 将 CoT 的每个推理步骤 autoformalize 为 SMT-LIB 格式的一阶逻辑 (FOL)
  - 两阶段 autoformalization pipeline：(1) 用现有逻辑词汇翻译 (2) 扩展词汇表达新概念
  - 用 Z3 SMT solver 做逻辑验证：对 document/background/commonsense 型步骤做 consistency check；对 inference 型步骤做 entailment check
  - 验证信号用于三个下游任务：推理时 self-reflection、SFT 数据蒸馏、DPO 偏好微调
- **评估数据集**: ProofWriter, LegalBench-SARA, BioASQ
- **与我们的关系**:
  - **相同点**: FOL formalization + Z3 验证 + 验证信号用于推理质量评估
  - **差异点**:
    - VeriCoT 做 binary 验证（valid/invalid），不做 graded consistency scoring
    - VeriCoT 不计算 MCS，无 IC = MCS_size/total_claims 量化指标
    - VeriCoT 无 Premise-Conditioned Verification 概念
    - VeriCoT 的 chain selection 方式不同（self-reflection 而非 graded ranking）
    - VeriCoT 侧重非数学领域（法律、生物 QA），我们侧重数学/逻辑推理

### 1.2 VERGE — 🔴 高风险

- **标题**: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning
- **作者**: Vikash Singh et al.
- **年份/会议**: 2026.01, arXiv 2601.20055
- **核心方法**:
  - 将 LLM 输出分解为 atomic claims
  - Autoformalize 为一阶逻辑
  - 用 Z3 (v4.12.2) 做一致性验证
  - **使用 Minimal Correction Subsets (MCS) 精确定位逻辑错误**
  - 三大创新：(1) 多模型共识 via 形式语义等价检查 (2) 语义路由：逻辑 claims 用 solver，常识 claims 用 LLM 集成 (3) MCS 错误定位
  - 迭代 refinement：MCS 反馈 → LLM 修正 → 重新验证
- **性能**: GPT-OSS-120B 上平均提升 18.7%
- **与我们的关系**:
  - **相同点**: FOL + Z3 + MCS 是我们方法的核心组件，VERGE 全都用了
  - **差异点**:
    - VERGE 用 MCS 做 error localization + iterative correction，我们用 MCS 计算 graded IC score
    - VERGE 目标是 refinement（修正错误推理），我们目标是 chain selection（选最优推理链）
    - VERGE 无 Premise-Conditioned Verification
    - VERGE 的 MCS 是定性的（定位哪些 claims 有问题），我们的 IC = MCS_size/total_claims 是定量 ranking 信号
    - VERGE 有语义路由机制区分逻辑/常识 claims，我们没有

### 1.3 FoVer — 🟡 中高风险

- **标题**: FoVer: First-Order Logic Verification for Natural Language Reasoning
- **作者**: Yu Pei, Yongping Du, Xingnan Jin
- **年份/会议**: TACL 2025 (EMNLP 2025 展示)
- **核心方法**:
  - 自动化 pipeline：NL → FOL（LLM 驱动） → Z3 验证
  - 验证推理文本的逻辑正确性
- **评估数据集**: ProofWriter, FOLIO, REVEAL (真实 LLM 输出)
- **与我们的关系**:
  - **相同点**: NL→FOL→Z3 pipeline 几乎一致
  - **差异点**: FoVer 做 binary 正确性验证，不做 graded scoring 或 chain selection；无 MCS 计算；无 PCV

---

## 二、相关工作（问题相似，方法不同）

### 2.1 Typed Chain-of-Thought (TCoT)

- **标题**: Typed Chain-of-Thought: A Curry-Howard Framework for Verifying LLM Reasoning
- **年份/会议**: 2025.10, arXiv 2510.01069 (提交 ICLR 2026，已撤稿)
- **核心方法**: 用 Curry-Howard 同构将 CoT 映射为类型化程序，通过 type checking 验证推理忠实度。构建 Typed Reasoning Graphs (TRGs)，定义 Coverage、Evidence Validity Rate、Path Existence 等形式化指标
- **与我们的关系**: 不同的形式化范式（类型系统 vs FOL/SMT），但目标类似——验证 CoT 的逻辑正确性。可作为 alternative approach 引用

### 2.2 SAFE

- **标题**: Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification
- **年份/会议**: ACL 2025 (arXiv 2506.04592)
- **核心方法**: 用 Lean4 形式化每步数学推理，提供形式证明以检测幻觉。结合 Formal Verifier + PRM 双信号，聚合为回顾性/前瞻性分数
- **与我们的关系**: 同为形式验证 CoT 的工作，但用 Lean4 而非 Z3，限于数学领域，且需要完整的形式证明（我们只需一致性检查）

### 2.3 CRV (Circuit-based Reasoning Verification)

- **标题**: Verifying Chain-of-Thought Reasoning via Its Computational Graph
- **作者**: Zheng Zhao et al.
- **年份/会议**: ICLR 2026 Oral (arXiv 2510.09312)
- **核心方法**: 白盒方法——分析正确/错误 CoT 步骤的 attribution graph 结构差异，训练分类器检测推理错误
- **与我们的关系**: 完全不同的技术路线（内部表征分析 vs 形式逻辑验证），但解决同一问题。作为 complementary approach 引用

### 2.4 SSV (Semantic Self-Verification)

- **标题**: Instantiation-based Formalization of Logical Reasoning Tasks using Language Models and Logical Solvers
- **年份/会议**: IJCAI 2025
- **核心方法**: 用 LLM 生成具体实例化 (concrete instantiations) 来验证抽象形式化的正确性。AR-LSAT 上达到 71.3%，验证通过的案例精度 100%
- **与我们的关系**: 创新的 formalization 验证机制，可作为我们 autoformalization 质量保证的参考技术

### 2.5 Foundations of Global Consistency Checking

- **标题**: Foundations of Global Consistency Checking with Noisy LLM Oracles
- **年份/会议**: 2026.01, arXiv 2601.13600
- **核心方法**: 形式化用 noisy LLM oracle 检查全局事实一致性的问题。自适应 divide-and-conquer 算法定位 minimal inconsistent subsets (MUSes)，通过 hitting-set 计算 minimal repairs
- **与我们的关系**: 理论基础高度相关——同样研究 consistency checking + minimal inconsistent subset。但使用 LLM oracle 而非 SMT solver，关注事实一致性而非逻辑一致性

### 2.6 NL2FOL

- **标题**: NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection
- **作者**: Abhinav Lalwani et al.
- **年份/会议**: 2024.05, arXiv 2405.02318
- **核心方法**: 分步将自然语言 autoformalize 为 FOL，用 SMT solver 推理验证逻辑谬误
- **性能**: LOGIC 数据集 F1=78%, LOGICCLIMATE F1=80%
- **与我们的关系**: autoformalization pipeline 的直接技术参考

---

## 三、技术组件参考

### 3.1 Autoformalization

| 论文 | 年份 | 方向 | 备注 |
|------|------|------|------|
| NL2FOL | 2024 | NL→FOL (SMT solver) | 逻辑谬误检测 |
| Autoformalization Survey | 2025 | 全面综述 | arXiv 2505.23486 |
| Neurosymbolic NL Formalization | 2025 | NL→FOL + 验证 | arXiv 2511.09008 |

### 3.2 Z3/SMT in NLP

| 论文 | 年份 | 用法 | 备注 |
|------|------|------|------|
| VeriCoT | 2025 | SMT-LIB + Z3 验证 CoT | 最直接参考 |
| VERGE | 2026 | Z3 验证 + MCS | 最直接参考 |
| FoVer | 2025 | Z3 验证 NL 推理 | TACL |
| FoVer-PRM | 2025 | Z3/Isabelle 生成 PRM 训练数据 | arXiv 2505.15960 |
| MANTRA | 2026 | SMT 验证 LLM agent 合规性 | arXiv 2605.06334 |

### 3.3 Verifier & Chain Selection

| 论文 | 年份 | 方法 | 会议 |
|------|------|------|------|
| Self-Consistency (Wang et al.) | 2022/2023 | Majority voting | ICLR 2023 |
| CISC | 2025 | Confidence-weighted voting | ACL Findings 2025 |
| GenRM | 2024 | Generative verifier + Best-of-N | ICLR 2025 |
| PRM Survey | 2025 | Process/Outcome reward models | arXiv 2510.08049 |
| Trust but Verify Survey | 2025 | 验证方法全面综述 | arXiv 2508.16665 |
| On Learning Verifiers | 2025 | PAC-learning framework for verifiers | NeurIPS 2025 |
| 4/δ Bound | 2025 | LLM-Verifier 收敛定理 | arXiv 2512.02080 |
| CREST | 2025 | Consistency-driven self-training | NAACL 2025 |

### 3.4 Test-Time Compute & Scaling

| 论文 | 年份 | 核心贡献 | 会议 |
|------|------|----------|------|
| Scaling Test-Time Compute (Snell et al.) | 2024 | Compute-optimal TTS 策略 | ICLR 2025 |
| Art of Scaling TTS | 2025 | 大规模 TTS 策略对比 | arXiv 2512.02008 |
| TTS Survey | 2025 | What/How/Where/How Well | testtimescaling.github.io |

---

## 四、关键论文详细对比表

| 维度 | 我们 (PCV+IC) | VeriCoT | VERGE | FoVer |
|------|--------------|---------|-------|-------|
| Formalization | FOL | FOL (SMT-LIB) | FOL | FOL |
| Solver | Z3 | Z3 | Z3 | Z3 |
| 验证类型 | Internal consistency | Consistency + Entailment | Consistency | Correctness |
| MCS 使用 | 计算 IC score (MCS/total) | ❌ | Error localization | ❌ |
| Graded scoring | ✅ IC ∈ [0,1] | ❌ Binary | ❌ Binary→修正 | ❌ Binary |
| Chain selection | ✅ (核心目标) | Self-reflection | ❌ (做 refinement) | ❌ |
| Premise-conditioned | ✅ PCV | ❌ | ❌ | ❌ |
| 目标任务 | 数学/逻辑推理 | 法律/生物QA | 通用推理 | 逻辑推理 |
| 与 self-consistency 对比 | ✅ 直接替代 | ❌ | ❌ | ❌ |

---

## 五、Novelty 评估

### 已有的组件（非新颖）
- **NL → FOL autoformalization**: VeriCoT, FoVer, NL2FOL 等多篇论文已做
- **Z3 验证 CoT**: VeriCoT, VERGE, FoVer 均已实现
- **MCS 计算**: VERGE 已使用（用于 error localization）

### 我们的差异化贡献（潜在新颖性）

1. **IC = MCS_size / total_claims 作为 graded verifier** 🟢
   - 现有工作要么做 binary verification（VeriCoT, FoVer），要么用 MCS 定位错误（VERGE）
   - 将 MCS 比例转化为连续的一致性分数，作为推理链质量的量化指标，这是新的
   - 需强调与 VERGE 的区别：VERGE 用 MCS 做定性定位，我们用 MCS 做定量评分

2. **Premise-Conditioned Verification (PCV)** 🟢
   - 将题目 premises 作为固定约束加入 Z3 验证，检查推理链与题目条件的一致性
   - 现有工作均未显式区分 "题目约束" 和 "推理生成的 claims"
   - 这是一个清晰的 conceptual contribution

3. **IC 作为 chain selection 机制替代 self-consistency** 🟢
   - 现有 formal verification 工作（VeriCoT 做 self-reflection，VERGE 做 refinement），无人将形式验证分数直接用于 Best-of-N chain selection
   - 与 self-consistency (majority voting) 直接对比是新的实验设置

### 综合评估

**Novelty 等级：中等偏上 (Moderate-High)**

个体技术组件不新，但组合方式和应用目标有新颖性。核心卖点：
- PCV 是概念层面的贡献
- IC graded scoring 是方法层面的贡献
- Chain selection 应用是系统层面的贡献

**建议定位**：不宜宣称 "首次将形式验证用于 CoT 验证"（VeriCoT/VERGE/FoVer 已做），应定位为 "首次将形式化一致性检查转化为 graded chain selection 机制，并提出 premise-conditioned verification 框架"。

**关键风险**：VERGE 的 MCS 使用与我们最为接近，论文中必须清晰说明两者目标和用法的本质区别。

---

## 六、建议引用列表

### 必须引用（直接相关）
1. VeriCoT (arXiv 2511.04662) — 最近的 FOL+Z3 验证 CoT 工作
2. VERGE (arXiv 2601.20055) — MCS + Z3 验证，最接近的竞品
3. FoVer (TACL 2025) — FOL 验证 pipeline 先驱
4. Self-Consistency (Wang et al., ICLR 2023) — 我们直接替代的 baseline
5. NL2FOL (arXiv 2405.02318) — autoformalization 技术参考

### 强烈建议引用
6. SAFE (ACL 2025, arXiv 2506.04592) — Lean4 形式验证 CoT
7. Typed Chain-of-Thought (arXiv 2510.01069) — 另一种形式化验证范式
8. CRV (ICLR 2026 Oral, arXiv 2510.09312) — CoT 验证的白盒方法
9. SSV/Instantiation-based Formalization (IJCAI 2025) — formalization 验证
10. Global Consistency Checking (arXiv 2601.13600) — 一致性检查理论基础
11. Scaling Test-Time Compute (Snell et al., ICLR 2025) — TTS 理论基础
12. Trust but Verify Survey (arXiv 2508.16665) — 验证方法综述
13. GenRM (ICLR 2025, arXiv 2408.15240) — Generative verifier baseline
14. FoVer-PRM (arXiv 2505.15960) — 形式验证用于 PRM 训练

### 可选引用
15. CISC (ACL Findings 2025) — 改进的 self-consistency
16. On Learning Verifiers (NeurIPS 2025, arXiv 2505.22650) — verifier 学习理论
17. 4/δ Bound (arXiv 2512.02080) — LLM-Verifier 收敛保证
18. PRM Survey (arXiv 2510.08049) — PRM 综述
19. Autoformalization Survey (arXiv 2505.23486) — autoformalization 综述
20. CREST (NAACL 2025) — consistency-driven self-training
