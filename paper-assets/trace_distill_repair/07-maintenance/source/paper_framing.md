# Paper Framing — Diagnostic Trace Distillation (DTD)

> 目标会议: EMNLP 2026 ARR May (DDL: 2026-05-25)
> 状态: 初稿，待 MVP 结果验证后修订

---

## 1. Core Thesis

**Structure-aware segmentation of execution traces (call subtrees, loop iteration groups, exception propagation chains), filtered by a distilled 0.6B model, yields more effective trace context for LLM-based program repair than either raw full traces or line-level filtering — overturning the negative conclusions of Wang et al. (EMNLP 2025) about trace utility.**

---

## 2. Core Claims

### Claim 1: Structure > Lines
**Claim**: 结构化 trace 分段（函数调用子树、循环迭代组、异常传播链）作为 LLM 修复上下文，效果显著优于行级过滤和全量 trace。

- **Evidence 类型**: 定量对比 + 统计显著性检验
- **对应实验**: 4-condition repair comparison on BugsInPy — no-trace / full-trace / line-filtered / structural-filtered，报告 pass@1 和 win rate，McNemar's test 或 paired bootstrap

### Claim 2: Trace 有用，但需要正确的粒度
**Claim**: Wang2025 关于 "trace utility limited" 的负面结论源于粒度选择不当（原始行级 trace），而非 trace 本身无价值。结构化过滤后 trace 在多数配置下带来正向效果。

- **Evidence 类型**: 对照实验复现 + 消融分析
- **对应实验**: 在 Wang2025 相同评测设置下（或尽量对齐的子集），对比 raw trace vs. structural-filtered trace 的效果翻转；按 trace 复杂度分桶分析（short/medium/long trace），展示结构化过滤在 long trace 上优势最大

### Claim 3: 小模型蒸馏可替代大模型在线推理做 trace 过滤
**Claim**: 经 teacher-student 蒸馏训练的 0.6B 模型，在 trace segment 过滤任务上逼近 teacher（DeepSeek-V4 级别）的标注质量，且推理成本降低 10x+。

- **Evidence 类型**: student vs. teacher 一致性 + 下游修复效果保持率
- **对应实验**: (1) student-teacher agreement rate on held-out segments; (2) repair pass@1: teacher-filtered vs. student-filtered（差距 <3pp 为成功）; (3) 推理延迟和成本对比

---

## 3. Story Arc

### Problem
Execution trace 包含丰富的运行时语义（变量状态、控制流路径、异常传播），理论上是程序修复的强信号源。但现有工作的使用方式存在根本性问题：

- **全量 trace 过长过杂**: Wang2025 和 Haque2025 系统性验证了直接拼入 prompt 效果有限，且 trace 越复杂效果越差
- **行级过滤噪声大**: 逐行筛选丢失了 trace 中的层次结构信息（哪些调用属于同一逻辑单元、循环的迭代模式、异常的传播路径）
- **大模型在线推理成本高**: LDB 逐 block 用 LLM 验证，DynaFix/TraceRepair 每轮全量 trace 喂大模型——成本高且不可离线

结果：领域内形成了 "trace 对 LLM 修复帮助有限" 的共识（Wang2025），但这是粒度和方法的问题，不是 trace 本身的问题。

### Insight
Trace 的核心价值不在逐行内容，而在**结构**：
- **函数调用子树**: 定位 bug 所在的调用链上下文
- **循环迭代组**: 暴露状态累积异常（第 N 次迭代开始偏离预期）
- **异常传播链**: 追溯 root cause 到 symptom 的因果路径

结构化分段保留语义关联性，丢弃冗余细节——这是人类开发者阅读 trace 的自然方式。

### Method
**Diagnostic Trace Distillation (DTD)** — 两阶段方案：

1. **结构化分段器**: 解析 execution trace 为三类结构单元（call subtrees / loop groups / exception chains），产生语义完整的 segments
2. **Teacher-Student 蒸馏过滤器**: Teacher（大 LLM）标注每个 segment 的 diagnostic relevance；Student（0.6B 模型）学习 teacher 的过滤判断，部署时仅需 student 推理

### Results（预期，待 MVP 验证）
在 BugsInPy 上的 repair pass@1 排序：

```
structural-filtered > line-filtered > full-trace > no-trace
```

关键预期：
- 结构化过滤在长 trace（>2K tokens）上优势最显著
- Student 模型过滤质量接近 teacher（agreement >85%，下游 pass@1 差距 <3pp）
- 端到端推理成本较 DynaFix/TraceRepair 降低一个数量级

---

## 4. Reviewer Concerns

### RC1: "结构化分段对多少 trace 可行？解析失败怎么办？"
- **风险**: Python 动态特性导致 trace 结构不规整，解析覆盖率不足
- **预备回应**: 报告分段成功率（MVP pass 标准 ≥80%）；对解析失败的 case 回退到行级过滤（graceful degradation）；分析失败 case 的模式（如 C extension calls、generator/coroutine）

### RC2: "Teacher 标注质量如何保证？会不会 garbage in garbage out？"
- **风险**: Teacher LLM 本身对 trace segment relevance 的判断不可靠
- **预备回应**: 报告 teacher 标注的人工抽查 precision（MVP 标准 ≥0.6）；设计 inter-annotator agreement 实验（teacher vs. 人类开发者）；teacher 错误主要是 false negative（保守丢弃），对下游修复的伤害有限

### RC3: "为什么不直接用大模型过滤，而要蒸馏小模型？"
- **风险**: 审稿人质疑蒸馏的必要性，认为直接用大模型过滤即可
- **预备回应**: (1) 成本：大模型过滤每个 trace 需 $0.01-0.05，大规模使用不现实；(2) 延迟：0.6B 模型推理 <100ms vs. API 调用 1-3s；(3) 可离线：无需联网即可部署；(4) 实验数据：teacher-filtered vs. student-filtered 效果差距 <3pp

### RC4: "BugsInPy 规模太小（40/493），结论能泛化吗？"
- **风险**: 小样本上的结论统计效力不足
- **预备回应**: (1) MVP 用 40 个验证方向，full paper 扩展到 200+ instances；(2) 补充 SWE-bench-lite 子集作为 cross-benchmark 验证；(3) 按 bug 类型/项目/trace 复杂度分层分析，展示效果一致性

### RC5: "与 LDB 的 basic block 分段相比，你的结构化分段好在哪里？"
- **风险**: LDB 已经做了结构化分段（basic block），审稿人认为 DTD 的分段只是 LDB 的变体
- **预备回应**: (1) 粒度不同：LDB 的 basic block 是编译器级 CFG 概念，DTD 的分段是语义级（函数调用子树 = 逻辑功能单元，循环组 = 状态演化模式，异常链 = 因果路径）；(2) 使用方式不同：LDB 用大 LLM 在线逐块验证，DTD 用蒸馏小模型离线过滤；(3) 直接对比实验：DTD segments vs. basic block segments 作为修复上下文

---

## 5. Positioning vs. Prior Work

### vs. Wang2025 "Do Code Semantics Help?"（核心对标）
- **关系**: 直接修正其负面结论
- **Wang2025 结论**: Execution trace 对 Code LLM 帮助有限（6 组配置仅 2 组正向）
- **DTD 论点**: 其结论的根因是 trace 使用方式（原始行级拼接）而非 trace 本身。结构化过滤后，trace 在多数配置下带来显著正向效果
- **叙事策略**: 不攻击 Wang2025 的实验本身（其实验是 sound 的），而是指出其 trace representation 选择的局限性，DTD 提供了更合理的 trace 使用范式

### vs. Haque2025 "Towards Effectively Leveraging Execution Traces"
- **关系**: 互补验证，DTD 提供 Haque2025 缺少的解决方案
- **Haque2025** 诊断了问题（trace 复杂度增加→效果递减）但未提出结构化解决方案
- **DTD** 提供了结构化分段 + 蒸馏过滤的完整方案

### vs. LDB (ACL 2024)
- **关系**: 方法论启发 + 直接改进
- **差异**: (1) LDB 用 basic block（CFG 级），DTD 用语义级结构分段；(2) LDB 依赖大 LLM 在线推理做逐块验证，DTD 用蒸馏小模型离线过滤；(3) LDB 面向代码生成调试，DTD 面向已有 bug 修复

### vs. DynaFix (2025) / TraceRepair (2026)
- **关系**: 同期竞争者，不同技术路线
- **DynaFix**: 迭代式全量 trace + 大 LLM 推理，token 消耗仍然很高
- **TraceRepair**: Multi-agent debate + 全量 trace 作逻辑过滤器，依赖多个大 LLM agent
- **DTD 差异化**: 预过滤范式——用轻量蒸馏模型在 trace 进入 repair LLM 前完成结构化筛选，与上述方法正交（可叠加使用）

### vs. TraceFixer (2023) / TraceCoder (ICSE 2026)
- **TraceFixer**: 扁平变量快照表示，限于单行 bug；DTD 用层次化结构分段，处理多行复杂修复
- **TraceCoder**: 面向 LLM 生成代码的调试，非已有 bug 修复；依赖多 agent 推理链

### vs. Learned Context Compression (SWEzze / SWE-Pruner / Squeez / CodeComp)
- **关系**: 同属 learned compression 方法群，但操作对象和结构利用方式不同
- **现有方法的操作对象**: SWEzze 和 SWE-Pruner 操作 static code；Squeez 操作 flat text tool output；TACO 操作 terminal output；CodeComp 操作 KV cache
- **共同局限**: 这些方法都不利用 execution trace 的层次结构（call tree / loop iteration / exception chain），将输入视为扁平文本序列进行压缩
- **DTD 差异化**: DTD 是第一个将 learned compression 应用到 execution trace 并利用其内在层次结构（函数调用子树、循环迭代组、异常传播链）的工作
- **支撑论据**: CodeComp 的实验结论——structure-aware compression > structure-agnostic compression——直接支持 DTD 的核心假设：利用 trace 的结构信息比忽略结构的压缩更有效

---

## Future Direction / Preliminary Evidence

### DTD 作为即插即用的 trace 预处理器
**Claim**: DTD 的结构化过滤可作为前端模块集成到不同的 repair pipeline（prompt-based / agentic），均带来增益。

- **Evidence 类型**: 跨 pipeline 集成实验
- **对应实验**: 将 DTD 过滤后的 trace 分别喂给 (a) 单轮 prompt repair, (b) 类 RepairAgent 的多轮 agentic repair，对比有无 DTD 前端的效果差异
- **状态**: 降级为 future direction（D003 决策），不作为本文核心贡献。待核心实验完成后，如有余力可提供初步证据。

---

*本文档为初稿。MVP 结果（结构化 vs. 行级过滤 win rate、teacher 标注质量）将决定 claims 的强度和实验设计的最终方案。*
