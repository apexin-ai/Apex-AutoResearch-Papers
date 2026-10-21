# EnriCo & IterGen vs OntoCoDec 定性对比

## 1. EnriCo (Zaratiana et al.)

### 1.1 方法概述

- **标题**: EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction
- **作者**: Urchade Zaratiana, Nadi Tomeh, Yann Dauxais, Pierre Holat, Thierry Charnois (FI Group & LIPN, CNRS UMR 7030, France)
- **Venue**: arXiv preprint (2404.12493), April 2024; 未发表于正式会议
- **代码**: https://github.com/urchade/EnriCo (Apache-2.0)
- **核心方法**: 两阶段架构: (1) 基于 attention 的 enriched span/relation 表征学习 (需要训练), (2) ASP (Answer Set Programming) solver 在推理时执行全局约束解码。模型先对所有候选 span 和 relation 打分，然后 ASP solver 在满足约束的前提下找到最高分的全局解。
- **Base models**: ALBERT (albert-xxlarge-v1) for ACE05/CoNLL04; SciBERT (scibert-base-uncased) for SciERC. 注意：这是 encoder-only 分类模型，不是 autoregressive LLM。

### 1.2 约束能力详解

**通用约束 (所有数据集)**:
- **Unique Type Assignment**: 每个 entity/relation 只能有一个类型 → 类似 OntoCoDec 的 ET constraint
- **Non-overlapping Spans**: 预测的 entity span 不能重叠 → OntoCoDec 无此约束 (JSON 格式天然不涉及 span overlap)
- **Consistency**: relation 必须连接两个合法 entity; 不允许 "non-entity" pair → 类似 OntoCoDec 的结构约束

**数据集特定约束 (Domain-Range)**:
- **CoNLL04**: 手工定义 5 个合法 (head_type, tail_type) → relation 三元组 (e.g., (Person, Organization) → Work_For)
- **ACE05**: 手工定义 40+ 合法三元组
- **SciERC**: **未应用任何数据集特定约束** (论文称 "annotation guidelines insufficiently detailed")

**未支持的约束类型**:
- **RV (Relation Vocabulary) constraints**: 不适用 (非生成式模型，relation 从固定候选集选择)
- **Cross-field consistency**: 未提及
- **Cardinality constraints**: 未提及

### 1.3 约束执行机制

- **时机**: Post-scoring optimization，不是 token-level masking
- **流程**: 神经网络打分 → ASP solver 接收分数作为偏好 → solver 在硬约束下返回最高分合法解
- **Fast variant**: 不用 ASP solver，而是对不合法 entity-relation pair 设 -∞ bias，然后 argmax (条件逻辑，非 token masking)
- **速度**: ASP Joint 6.7 sent/s; ASP Entity First 5.5 sent/s; Fast variant 21.7 sent/s

### 1.4 约束来源与换 ontology 成本

- **约束来源**: **手工编写**
  - CoNLL04: 引用 Roth & Yih 2004 的约束定义
  - ACE05: 从 LDC annotation guidelines 手动提取
  - SciERC: 因 guideline 不够详细而未定义约束
- **换 ontology 成本**: **中等偏高**。需要: (1) 更新 bias value tables, (2) 修改 ASP 规则库, (3) 需要领域专家审查。无需重新训练。
- **对比 OntoCoDec**: OntoCoDec 从 ontology JSON schema 自动编译约束，换 ontology 只需提供新 JSON 文件。

### 1.5 vs OntoCoDec 关键差异

1. **模型架构根本不同**: EnriCo 是 encoder-only 分类模型 (ALBERT/SciBERT)，OntoCoDec 适用于任意 autoregressive LLM
2. **约束执行方式不同**: EnriCo 是 post-scoring global optimization (ASP solver)，OntoCoDec 是 token-level real-time masking during decoding
3. **约束来源不同**: EnriCo 手工编写 ASP 规则，OntoCoDec 自动从 ontology schema 编译
4. **训练需求不同**: EnriCo 的表征模块需要监督训练 (filtering loss + classification loss)，OntoCoDec 完全 training-free
5. **DR 约束覆盖**: EnriCo 对 SciERC 未应用 DR 约束，OntoCoDec 对所有数据集统一支持
6. **适用范围**: EnriCo 绑定特定 encoder 模型，OntoCoDec 可即插即用于任何 LLM

---

## 2. IterGen (Ugare et al.)

### 2.1 方法概述

- **标题**: IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking
- **作者**: Shubham Ugare, Rohan Gumaste, Tarun Suresh, Gagandeep Singh, Sasa Misailovic (University of Illinois Urbana-Champaign)
- **Venue**: ICLR 2025 (Conference Poster)
- **代码**: https://github.com/uiuc-arc/itergen, http://structuredllm.com
- **核心方法**: 通用 grammar-guided LLM generation 框架，用户用 BNF 格式的 CFG 定义输出语法。关键创新是支持基于 grammar symbol 的双向导航 (forward/backward)，通过维护 KV cache、decoding trace (token tree) 和 symbol position map 实现高效 backtracking。
- **Training-free**: 是。纯 inference-time 库，不需要任何训练。
- **Base models**: Qwen2.5 (0.5B, 1.5B, Coder-1.5B), Llama-3.2-1B, Llama-3.2-3B, Llama-2-7b-chat-hf, Meta-Llama-3-8B, Llama-3-8B-Instruct

### 2.2 约束能力详解

**核心 API**:
- `forward(stop_symbol, count)`: 生成到指定 grammar symbol 处停止
- `backward(symbol, count)`: 回退到之前的 symbol 位置，撤销生成内容
- `view(symbol)`: 查看当前生成中所有指定 symbol 的值

**支持的 semantic constraints (通过用户编写 Python 程序)**:
- **SQL**: 验证 table_name 和 column_name 是否存在于给定 schema 中
- **Privacy**: 检测生成文本是否包含敏感信息 (e.g., email 地址)，若包含则 backtrack
- **Vega-Lite**: (1) field name 必须是 dataframe 中的合法列名, (2) field type 必须匹配列的数据类型, (3) aggregation 必须是合法值 (count, mean, average, sum)

**约束指定方式**: 用户写 Python 程序，在循环中调用 forward → view → (条件判断) → backward。约束逻辑完全由用户代码实现，IterGen 只提供导航原语。

**不支持的 (与 IE 相关)**:
- **Entity type constraints**: 未设计，需用户自行实现
- **Relation vocabulary constraints**: 未设计
- **Domain-range constraints**: 未设计
- **IE-specific 任何功能**: IterGen 是通用框架，不针对 IE 任务

### 2.3 Latency 与 Overhead

**SQL generation (Table 1, Spider dataset, 平均)**:
- Standard: ~0.607s-1.083s per query
- SynCode: ~0.581s-1.525s per query
- IterGen: ~0.687s-1.520s per query
- IterGen 生成更多 tokens (因 backtracking 导致 resample)，平均多 ~3-8 tokens

**Privacy (Table 2, DecodingTrust)**:
- Standard: 0.24s-0.57s
- IterGen: 0.38s-0.78s
- overhead ~40%-60%

**Vega-Lite (Table 3, NLV Corpus)**:
- SynCode: 3.36s-4.43s
- IterGen: 3.96s-5.00s
- overhead ~10%-15%

**Backtracking overhead 来源**: (1) 废弃的 tokens 需重新采样, (2) 每步检查约束的处理开销, (3) IterGen session 初始化的固定开销。通过 KV cache 复用避免了 prefill 重复计算。

### 2.4 评估详情

| Task | Dataset | Metric | Key Result |
|------|---------|--------|------------|
| SQL generation | Spider (1034 problems) | Accuracy, Execution % | Avg accuracy 41.63% vs SynCode 35.22% vs Standard 28.9%; Execution 75.84% vs 63.72% vs 50.28% |
| Privacy | DecodingTrust (Enron emails) | Leaks count | 标准生成 45-67 leaks → IterGen 0 leaks (100% 消除) |
| Vega-Lite | NLV Corpus (814 examples) | Accuracy, Execution % | IterGen 30.47% accuracy vs SynCode 24.69% (Llama-3-8B) |

### 2.5 局限性 (论文 Section 6 明确提到)

1. **仅支持 single sequence generation**，不支持 batch generation
2. **Recurrence penalty heuristic** 可能在第一个 token 处过度偏移 LLM 分布
3. **无 IE 应用**: 论文未在任何 IE 任务上评估

### 2.6 vs OntoCoDec 关键差异

1. **通用 vs IE 专用**: IterGen 是通用 structured generation 框架，OntoCoDec 专为 IE 设计
2. **约束执行方式**: IterGen 通过 generate-check-backtrack 循环 (rejection sampling 变体)，OntoCoDec 通过 proactive token-level masking 预防违规
3. **约束效率**: OntoCoDec 在 token 生成时直接 mask 不合法 token，不浪费计算; IterGen 先生成再检查，违规时需回退重采样
4. **约束指定**: IterGen 需要用户写 Python 程序实现每种约束; OntoCoDec 从 ontology JSON 自动编译，零编程
5. **Grammar formalism**: IterGen 用 CFG (BNF/Lark EBNF) + LR parser; OntoCoDec 用 xgrammar
6. **IE constraint coverage**: OntoCoDec 一体化支持 ET/RV/DR constraints; IterGen 无内置 IE 约束支持
7. **Batch 支持**: IterGen 不支持 batch; OntoCoDec 支持情况未确认

---

## 3. 三方对比表

| 维度 | OntoCoDec | EnriCo | IterGen |
|------|-----------|--------|---------|
| **约束执行时机** | Decoding-time (token-level masking) | Post-scoring (ASP solver / -∞ bias) | Generate-check-backtrack loop |
| **Training-free** | ✓ | ✗ (表征模块需训练，约束推理免训练) | ✓ |
| **ET constraints** | ✓ (Layer 1 grammar) | ✓ (unique type assignment) | ✗ (需用户自行实现) |
| **RV constraints** | ✓ (Layer 1 grammar) | N/A (非生成式) | ✗ (需用户自行实现) |
| **DR constraints** | ✓ (Layer 2 semantic) | 部分 (CoNLL04/ACE05 手工定义; SciERC 无) | ✗ (需用户自行实现) |
| **CF consistency** | Majority voting post-hoc | 未提及 | 未提及 |
| **约束来源** | Auto-compiled from ontology JSON | 手工编写 ASP 规则 | 用户编写 Python 程序 |
| **换 ontology 成本** | 只需新 JSON schema | 需重写 ASP 规则 + 领域专家审查 | 需重写 constraint checking 代码 |
| **Base model 兼容性** | Any autoregressive LLM | 绑定特定 encoder (ALBERT/SciBERT) | Any autoregressive LLM |
| **IE-specific design** | ✓ | ✓ | ✗ (通用框架) |
| **Latency overhead** | <15% | ASP: 3-4x slower; Fast variant comparable | ~10%-60% depending on task |
| **评估数据集** | SciERC, DocRED | SciERC, CoNLL04, ACE05 | Spider (SQL), DecodingTrust, NLV Corpus |
| **评估任务** | IE (NER + RE) | IE (NER + RE) | SQL generation, privacy, Vega-Lite |
| **Venue** | (submission) | arXiv preprint 2024 | ICLR 2025 |
| **Proactive vs Reactive** | Proactive (prevent violations) | Proactive (eliminate invalid combos) | Reactive (detect then backtrack) |
| **Open-source** | - | ✓ (Apache-2.0) | ✓ |

---

## 4. 建议论文段落

### 4.1 Related Work 段落（英文，直接可用）

**Constrained Inference for IE:**

EnriCo (Zaratiana et al., 2024) formulates joint entity and relation extraction as a constrained optimization problem, using Answer Set Programming (ASP) to enforce structural constraints such as non-overlapping spans and valid domain-range type combinations at inference time. However, EnriCo operates on encoder-based classification models (ALBERT, SciBERT) rather than autoregressive LLMs, requires supervised training for its representation module, and relies on hand-crafted ASP rules that must be manually derived from annotation guidelines for each new dataset. In contrast, OntoCoDec is fully training-free, applies to any autoregressive LLM, and automatically compiles all constraints from a declarative ontology schema without manual rule engineering.

**General-purpose Constrained Generation:**

IterGen (Ugare et al., 2025) introduces a grammar-guided generation framework with backtracking, enabling users to navigate forward and backward through generated output based on grammar symbols and programmatically enforce semantic constraints. While IterGen demonstrates effectiveness for SQL generation and privacy protection, it is a general-purpose library that provides navigation primitives rather than IE-specific constraint enforcement. Users must manually implement each constraint as Python code, and the reactive generate-check-backtrack paradigm incurs additional overhead from discarded tokens. OntoCoDec instead proactively masks invalid tokens during decoding, preventing constraint violations before they occur, and automatically derives IE-specific constraints (entity types, relation vocabulary, domain-range compatibility) from the ontology schema.

### 4.2 OntoCoDec 差异化优势总结

1. **Fully automatic constraint compilation**: OntoCoDec 从 ontology JSON schema 自动编译所有约束 (ET, RV, DR)，换 ontology 零编程成本。EnriCo 需要手工编写 ASP 规则且 SciERC 上甚至无法定义约束; IterGen 需要用户为每种约束编写 Python 检查代码。

2. **Proactive token-level prevention vs reactive correction**: OntoCoDec 在 token 生成时直接 mask 不合法选项，从根本上防止违规。EnriCo 在全部打分后做 global optimization (不同范式)。IterGen 先生成再检查、违规后 backtrack 重采样，浪费计算资源。

3. **Training-free + LLM-agnostic**: OntoCoDec 不需要任何训练，可即插即用于任何 autoregressive LLM。EnriCo 需要训练 encoder 模型且绑定特定架构。IterGen 虽然也 training-free 且 LLM-agnostic，但缺乏 IE-specific 约束设计。

4. **Integrated IE constraint taxonomy**: OntoCoDec 提供层次化约束体系 (Layer 1: grammar → ET + RV; Layer 2: semantic → DR)，覆盖 IE 任务的主要约束类型。EnriCo 和 IterGen 都没有这种系统性的 IE 约束分类。

5. **Low overhead**: OntoCoDec latency overhead <15%。EnriCo 的 ASP solver 带来 3-4x 性能下降 (Fast variant 避免 ASP 但牺牲 joint optimization)。IterGen 的 backtracking overhead 在 10%-60% 之间。

---

## Sources

- [EnriCo arXiv](https://arxiv.org/abs/2404.12493)
- [EnriCo HTML](https://arxiv.org/html/2404.12493v1)
- [EnriCo GitHub](https://github.com/urchade/EnriCo)
- [IterGen arXiv](https://arxiv.org/abs/2410.07295)
- [IterGen OpenReview](https://openreview.net/forum?id=ac93gRzxxV)
- [IterGen ICLR page](https://iclr.cc/virtual/2025/poster/29157)
- [Zaratiana homepage](https://urchade.github.io/)
