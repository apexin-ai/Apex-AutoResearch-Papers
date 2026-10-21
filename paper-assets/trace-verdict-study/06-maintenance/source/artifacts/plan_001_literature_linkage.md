# plan_001 Literature Linkage

## 关键发现

- plan_001 (vota_no_ae) 结果：去掉 actual/expected 值后 accuracy 99.4%，与 VOTA v5 (99.2%) 持平
- 结论：assertion 的具体值（actual/expected）对 verdict 分类冗余，模型依赖的是 trace 行为模式（控制流、异常模式、方法调用序列）

## 已有文献对比

### 直接支持

**Haque et al. (2025)** "Towards Effectively Leveraging Execution Traces for Program Repair"
- literature_map 已收录 (trace-compression, background)
- 关系：**强支持**。发现 trace 复杂度（长度 + 变量数量）增加时效果递减，LLM-optimized 精简格式优于原始 trace。plan_001 的发现是这一规律在 verdict 分类场景的验证——去掉 actual/expected 值相当于降低 trace 复杂度，效果不降反微升。

**Wang et al. (2025)** "Do Code Semantics Help?"
- literature_map 已收录 (execution-trace-llm, direct-competitor)
- 关系：**补充**。该文发现 execution trace 对 SFT 帮助有限，但未区分 trace 中哪些组件有用。plan_001 进一步回答了"why"：原始 trace 中大量具体值是噪声，结构信号才是关键。

**ET-CoT / PyTracify (2025)** "Making LLMs Program Interpreters via Execution Trace Chain of Thought"
- literature_map 已收录 (trace-compression, method-component)
- 关系：**支持**。PyTracify 生成 sub-line 粒度的结构化 trace（本质是 trace abstraction），效果优于原始 trace。与 plan_001 一致：结构化抽象 > 原始值堆砌。

### 间接相关

**ND-Slicer (2024)** "Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning"
- literature_map 已收录 (trace-compression, method-component)
- 关系：**思路一致**。从完整 trace 中提取关键依赖关系（结构信息），而非保留全部变量值。

## 新发现论文

### 1. Ferrando et al. (2025) — 强支持

- **Title**: "What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces"
- **Authors**: Lorenzo Ferrando, Nicola Ferraro, et al.
- **Year**: 2025
- **Venue**: arXiv 2503.05703
- **Key finding**: 对比三种 scratchpad 策略——regular（每步记录所有变量值）、compact（仅记录变化的变量）、dynamic（维护单一状态表示）。Compact scratchpad 略优于 regular，两者都优于 dynamic。CruxEval/MBPP ~80% accuracy。
- **与 plan_001 关系**: **强支持**。Compact（仅变化量）≥ Regular（全部值），直接印证 plan_001 的发现：完整的 actual/expected 值是冗余信息，精简后不损失甚至略有提升。区别在于他们研究 output prediction，plan_001 研究 verdict classification，但结论方向一致。

### 2. TraceCoder (ICSE 2026) — 支持

- **Title**: "TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code"
- **Authors**: (ICSE 2026 Research Track)
- **Year**: 2026
- **Venue**: ICSE 2026
- **Key finding**: 在代码特定位置插入 diagnostic probes 捕获细粒度运行时 trace，而非记录全量 trace。Pass@1 相对提升 34.43%。
- **与 plan_001 关系**: **支持**。选择性 trace 采集（probe 特定位置）优于全量记录，与 plan_001 的"去掉具体断言值不影响判断"方向一致——关键是 trace 的结构位置和行为模式，不是每个变量的具体值。

### 3. TraceRepair (2026) — 支持

- **Title**: "Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate"
- **Authors**: Jiaqing Wu et al.
- **Year**: 2026
- **Venue**: arXiv 2604.02647
- **Key finding**: Probe agent 捕获 "critical variables 的 execution snapshots"（而非全部变量），作为 multi-agent debate 的 objective repair basis。修复 392 个缺陷，超越所有对比方法。
- **与 plan_001 关系**: **支持**。"Critical variables" 的选择性捕获思路与 plan_001 的发现一致：不需要所有值，关键信息点的结构化表示就够了。

### 4. Demystifying Errors (2025) — 间接支持

- **Title**: "Demystifying Errors in LLM Reasoning Traces: An Empirical Study of Code Execution Simulation"
- **Authors**: (arXiv 2512.00215)
- **Year**: 2025
- **Venue**: arXiv
- **Key finding**: LLM 在循环中容易遗漏或多算变量修改，函数返回值预测出现错误值和错误位置。说明 LLM 对具体值的追踪能力弱于对结构模式的理解。
- **与 plan_001 关系**: **间接支持**。如果 LLM 本身不擅长精确值追踪，那么 trace 中的 actual/expected 具体值对模型来说就是低信噪比信息，去掉反而减少噪声。这为 plan_001 的结果提供了一个机制解释。

## 综合分析

plan_001 的发现（assertion 值冗余，行为模式是核心）与现有文献**高度一致**，无矛盾文献：

| 维度 | 已有文献证据 | plan_001 贡献 |
|------|-------------|--------------|
| 值冗余 | Compact ≥ Regular scratchpad (Ferrando 2025) | 首次在 verdict 分类中验证：去掉 actual/expected 不降点 |
| 复杂度有害 | Trace 越长越多变量，效果越差 (Haque 2025) | 去值 = 降低复杂度，accuracy 99.4% vs 99.2% |
| 选择性优于全量 | Probe-based > full trace (TraceCoder, TraceRepair) | VOTA 的 trace 行为模式 > 全量值信息 |
| LLM 值追踪能力弱 | 循环/返回值预测差 (Demystifying 2025) | 提供了"为什么值冗余"的机制解释 |

**plan_001 的独特贡献**：现有文献主要在 code repair / output prediction 任务上研究 trace 组件重要性，plan_001 首次在 **verdict classification (pass/fail)** 场景验证了这一规律，且效果更极端（99.4% accuracy，几乎零降幅）。

## literature_map.yaml 更新建议

```yaml
# 添加到 execution-trace-llm 类别
      - title: "What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces"
        authors: "Lorenzo Ferrando, Nicola Ferraro, et al."
        year: 2025
        venue: "arXiv 2503.05703"
        role: method-component
        key_finding: "对比 regular/compact/dynamic 三种 scratchpad 策略，compact（仅记录变化变量）略优于 regular（记录全部变量值）。直接支持 plan_001 发现：完整值信息冗余，精简不损失效果。"

# 添加到 trace-compression 类别
      - title: "TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code"
        authors: "ICSE 2026 Research Track"
        year: 2026
        venue: "ICSE 2026"
        role: background
        key_finding: "在特定位置插入 diagnostic probes 而非全量 trace 记录，Pass@1 提升 34.43%。选择性 trace 采集优于全量，支持 VOTA 的行为模式抽象思路。"

      - title: "Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate"
        authors: "Jiaqing Wu et al."
        year: 2026
        venue: "arXiv 2604.02647"
        role: background
        key_finding: "Probe agent 选择性捕获 critical variables 的 execution snapshots 用于 multi-agent repair debate，修复 392 个缺陷。验证了选择性 trace 信息优于全量记录。"

# 添加到 execution-trace-llm 类别
      - title: "Demystifying Errors in LLM Reasoning Traces: An Empirical Study of Code Execution Simulation"
        authors: "arXiv 2512.00215"
        year: 2025
        venue: "arXiv"
        role: evaluation
        key_finding: "LLM 在循环中频繁遗漏/多算变量修改，函数返回值预测不准。说明 LLM 对具体值追踪能力弱于结构理解，为 plan_001 发现（值冗余）提供机制解释。"
```
