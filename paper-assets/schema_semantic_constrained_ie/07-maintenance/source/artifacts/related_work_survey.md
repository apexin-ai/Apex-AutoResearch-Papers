# OntoCoDec Related Work Survey

## 1. Grammar-Constrained Decoding

### SynCode | TMLR 2025
- **Title:** SynCode: LLM Generation with Grammar Augmentation
- **Authors:** Ugare, Suresh, Kang, Misailovic & Singh (UIUC)
- **核心方法:** 通用语法约束解码框架，确保 LLM 输出严格遵循给定的上下文无关文法 (CFG)。核心是离线构建的 **DFA mask store**——从目标语言文法的 DFA 导出的高效查找表。在生成过程中，增量解析器处理部分输出生成 accept sequences（可合法跟随的终结符序列），然后通过 DFA mask store 过滤无效 token。在 Python/Go 代码上消除 96.07% 语法错误，JSON schema 验证 100%。
- **约束类型:** 纯语法约束（CFG/EBNF），不涉及语义。
- **与 OntoCoDec 的关系:** SynCode 与 XGrammar 属同一技术路线——token-level grammar masking。OntoCoDec 的 Grammar 层实现了类似的格式约束功能，但 OntoCoDec 在此之上叠加了 Semantic 层（domain/range 约束），这是 SynCode 不提供的。SynCode 是 model-agnostic 的纯推理时方法，不涉及 FT+CD composability。
- **BibTeX key:** `ugare2025syncode`
- **ArXiv:** 2403.01632

### IterGen | ICLR 2025
- **Title:** IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking
- **Authors:** Ugare, Gumaste, Suresh, Singh & Misailovic (UIUC)
- **核心方法:** 在 SynCode 的语法约束基础上引入 **语义感知的迭代回溯机制**。用户定义程序化语义约束检查器，当生成过程中检测到语义违规时，利用 symbol-to-position mapping 回溯到特定文法符号位置重新生成。通过复用 KV cache 保证回溯效率。在 SQL 生成上准确率从无约束 28.9% 提升至 41.63%（显著优于 SynCode 的 35.22%），隐私泄露从 51.4% 降至 0%。
- **约束类型:** Hybrid（CFG 语法约束 + 用户手写的程序化语义检查器）。
- **与 OntoCoDec 的关系:** IterGen 是目前最接近 OntoCoDec 的工作——同样结合语法+语义约束。**核心区别**在于：(1) IterGen 的语义约束需用户为每个任务手写检查逻辑，OntoCoDec 从 ontology schema 自动编译；(2) IterGen 用回溯修复违规，OntoCoDec 用前向约束传播预防违规；(3) IterGen 面向 code/SQL 生成，OntoCoDec 面向 IE 任务。IterGen 不涉及 FT+CD composability。
- **BibTeX key:** `ugare2025itergen`
- **ArXiv:** 2410.07295

### XGrammar | MLSys 2025
- **Title:** XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models
- **Authors:** Dong et al.
- **核心方法:** 将词表划分为 context-independent（离线预检）和 context-dependent（运行时检查）两类 token，结合 persistent stack-based pushdown automata 高效执行 CFG 约束，比先前方法快 100x。
- **与 OntoCoDec 的关系:** OntoCoDec 的 Grammar 层直接基于 XGrammar 实现 JSON schema + enum 约束，消除 RV/ET violations。XGrammar 提供格式正确性保证，但不处理语义层约束（domain/range），这正是 OntoCoDec Semantic 层的贡献。
- **BibTeX key:** `dong2025xgrammar`
- **ArXiv:** 2411.15100

### Outlines | arXiv 2023
- **Title:** Efficient Guided Generation for Large Language Models
- **Authors:** Willard & Louf
- **核心方法:** 将受约束文本生成重构为有限状态机（FSM）中的状态转移，为每个 FSM 状态离线构建词表索引，实现正则表达式约束的 O(1) 均摊 per-token 检查，扩展至 LALR(1) parser 支持 CFG。
- **与 OntoCoDec 的关系:** Outlines 是 grammar-constrained decoding 的开源先驱之一，与 XGrammar 属同一技术路线。OntoCoDec 选择 XGrammar 而非 Outlines 是因为其更高效的 vocabulary 预处理和对 LLM serving 框架（vLLM/SGLang）的原生集成。
- **BibTeX key:** `willard2023outlines`
- **ArXiv:** 2307.09702

### LMQL | PLDI 2023
- **Title:** Prompting Is Programming: A Query Language for Large Language Models
- **Authors:** Beurer-Kellner, Fischer & Vechev
- **核心方法:** SQL 风格的 LLM 查询语言，将自然语言 prompt 与程序控制流和声明式约束（类型、长度、正则、停止条件）结合，运行时编译为 token-level masking，减少 26-85% API 成本。
- **与 OntoCoDec 的关系:** LMQL 提供通用的声明式约束框架，但约束表达能力限于格式层面（类型、长度、正则）。OntoCoDec 的 Semantic 层引入了 IE 任务特有的 domain/range 本体约束，超越了通用格式约束的范畴。
- **BibTeX key:** `beurer-kellner2023lmql`
- **ArXiv:** 2212.06094

### DOMINO | ICML 2024
- **Title:** Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation
- **Authors:** Beurer-Kellner, Fischer & Vechev
- **核心方法:** 提出 non-invasive constrained decoding 算法，在执行 CFG 约束的同时最小化对 LLM 原始分布的扭曲，利用预计算和 speculative decoding 实现甚至超过无约束生成的吞吐。
- **与 OntoCoDec 的关系:** DOMINO 关注 distribution distortion 问题——约束解码如何改变 LLM 的 token 分布。OntoCoDec 的 F1 无损结果从实验角度呼应了这一方向：精心设计的约束不必牺牲生成质量。
- **BibTeX key:** `beurer-kellner2024domino`
- **ArXiv:** 2403.06988

### Grammar-Aligned Decoding (ASAp) | NeurIPS 2024
- **Title:** Grammar-Aligned Decoding
- **Authors:** Park, Wang, Berg-Kirkpatrick, Polikarpova & D'Antoni
- **核心方法:** 证明 naive token masking 会扭曲 LLM 的条件分布，提出 ASAp（Adaptive Sampling with Approximate expected futures）算法，在保证语法正确性的同时保持对原始 LM 分布的无偏性。
- **与 OntoCoDec 的关系:** ASAp 解决的是 grammar-constrained decoding 的理论正确性问题。OntoCoDec 的 logits masking 也面临类似的分布扭曲风险，但实验证明在 IE 任务上 F1 无损，说明 IE 场景中合法约束的 masking 影响有限。
- **BibTeX key:** `park2024grammar`
- **ArXiv:** 2405.21047

---

## 2. Vocabulary/Type-Constrained Generation

### GENRE | ICLR 2021
- **Title:** Autoregressive Entity Retrieval
- **Authors:** De Cao, Izacard, Riedel & Petroni
- **核心方法:** 首个用自回归生成方式检索实体的系统，基于 fine-tuned BART 逐 token 生成实体名，用 prefix trie 约束 beam search 只允许生成合法实体标识符，在 20+ entity disambiguation/linking 基准上达到 SOTA。
- **与 OntoCoDec 的关系:** GENRE 的 trie-based constrained beam search 是 vocabulary-constrained generation 的经典范式。OntoCoDec 的 Semantic 层借鉴类似思路（限制输出到合法类型/实体），但不需要构建 trie，而是通过 logits masking 直接在 token 级别实施 domain/range 约束。
- **BibTeX key:** `decao2021genre`
- **ArXiv:** 2010.00904

### GenIE | NAACL 2022
- **Title:** GenIE: Generative Information Extraction
- **Authors:** Josifoski, De Cao, Peyrard, Petroni & West
- **核心方法:** 自回归 seq2seq 模型生成 (subject, relation, object) 三元组，结合 trie-based lexical constraints（强制输出合法实体/关系标识符）和 state-based constraints（强制合法三元组结构），实现端到端抽取。
- **与 OntoCoDec 的关系:** GenIE 是将 vocabulary constraint 应用于 IE 的先驱，但需要 fine-tuning 专用模型。OntoCoDec 的关键优势是 training-free——直接在通用 LLM 上通过解码时约束实现，无需额外训练。
- **BibTeX key:** `josifoski2022genie`
- **ArXiv:** 2112.08340

### NeuroLogic Decoding | NAACL 2021
- **Title:** NeuroLogic Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints
- **Authors:** Lu, West, Zellers, Le Bras, Bhagavatula & Choi
- **核心方法:** 将词汇约束表达为谓词逻辑公式（合取/析取 of must-include/must-exclude tokens），在每步通过 pruning 和 re-ranking beams 执行约束，渐近复杂度等同标准 beam search。
- **与 OntoCoDec 的关系:** NeuroLogic 处理的是 lexical inclusion/exclusion 约束（"生成必须包含词 X"），而 OntoCoDec 的 Semantic 层处理的是 relational/type 约束（"关系 R 的 head 必须是类型 T"）。约束语义层次不同。
- **BibTeX key:** `lu2021neurologic`
- **ArXiv:** 2010.12884

### Grammar-Constrained Decoding for Structured NLP | EMNLP 2023
- **Title:** Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning
- **Authors:** Geng, Josifoski, Peyrard & West
- **核心方法:** 提出 grammar-constrained decoding（GCD）统一框架：每步将违反形式文法的 token logits 设为负无穷，保证结构合法输出，无需 fine-tuning。引入 input-dependent grammars 增加灵活性。在 IE、entity disambiguation、constituency parsing 上验证。
- **与 OntoCoDec 的关系:** 这是最直接的前驱工作——同样对 IE 任务使用 logits masking。但 Geng et al. 的约束限于语法层面（输出格式合法），OntoCoDec 在此基础上增加了语义层约束（domain/range 合法），是从格式正确到语义正确的扩展。
- **BibTeX key:** `geng2023gcd`
- **ArXiv:** 2305.13971

---

## 3. Structural Constraints for Information Extraction

### UIE | ACL 2022
- **Title:** Unified Structure Generation for Universal Information Extraction
- **Authors:** Lu, Liu, Dai et al.
- **核心方法:** 定义 Structured Extraction Language（SEL）统一编码不同 IE 输出结构（entity, relation, event, sentiment），配合 schema-based prompt（Structural Schema Instructor）和大规模预训练 text-to-structure 模型，在 4 个 IE 任务 13 个数据集上达到 SOTA。
- **与 OntoCoDec 的关系:** UIE 通过训练让模型"学会"输出合法结构，但无法保证推理时不违反 schema 约束。OntoCoDec 是 decoding-time enforcement，提供硬性保证——违反 domain/range 的输出不可能被生成。
- **BibTeX key:** `lu2022uie`
- **ArXiv:** 2203.12277

### GoLLIE | ICLR 2024
- **Title:** Annotation Guidelines improve Zero-Shot Information-Extraction
- **Authors:** Sainz, Garcia-Ferrero, Agerri et al.
- **核心方法:** 将 annotation guidelines 表达为 Python class 定义（dataclass），fine-tune Code-LLaMA 生成 Python 代码形式的结构化输出，通过 code-based schema 表达实现强零样本泛化到未见 IE schema。
- **与 OntoCoDec 的关系:** GoLLIE 用 Python 类型系统隐式表达类型约束，但执行仍依赖模型训练。OntoCoDec 在解码时显式执行本体约束，两者互补——GoLLIE 的 code-based schema 可与 OntoCoDec 的 decoding-time enforcement 结合。
- **BibTeX key:** `sainz2024gollie`
- **ArXiv:** 2310.03668

### CodeIE | ACL 2023
- **Title:** Large Code Generation Models are Better Few-Shot Information Extractors
- **Authors:** Li, Sun, Tang et al.
- **核心方法:** 将 IE 结构化输出重构为代码生成任务，用 code-LLM（Codex）+ code-style prompts 执行 NER 和 RE，代码形式天然捕获 IE 输出的结构性。在 few-shot 设置下一致优于 fine-tuned IE 模型和 NL-LLM prompting。
- **与 OntoCoDec 的关系:** CodeIE 通过代码形式化提高结构一致性，但仍是 soft constraint（模型可能生成非法代码）。OntoCoDec 的 Grammar+Semantic 层提供 hard constraint——输出格式和语义类型均被强制保证。
- **BibTeX key:** `li2023codeie`
- **ArXiv:** 2305.05711

### InstructUIE | arXiv 2023
- **Title:** Multi-task Instruction Tuning for Unified Information Extraction
- **Authors:** Wang, Zhou, Zu et al.
- **核心方法:** 构建 IE INSTRUCTIONS 基准（32 个 IE 数据集统一为 text-to-text 格式 + 专家指令），fine-tune Flan-T5 实现单模型处理 NER/RE/EE。指令微调的小模型大幅超越 GPT-3.5。
- **与 OntoCoDec 的关系:** InstructUIE 靠 instruction tuning 提高 IE 输出质量，但无结构保证。OntoCoDec 与 InstructUIE 正交——可在 instruction-tuned 模型上叠加 decoding-time 约束进一步消除违规。
- **BibTeX key:** `wang2023instructuie`
- **ArXiv:** 2304.08085

### BoostCD / BoostIE | EMNLP 2025
- **Title:** Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction
- **Authors:** Šakota & West (EPFL)
- **核心方法:** 两阶段 boosting 范式融合约束与无约束解码的互补优势。**Phase 1**：同一基础模型分别以约束模式和无约束模式解码，得到两个"弱预测"——约束解码保证结构合法但内容可能有误，无约束解码内容质量更好但可能违反结构约束。**Phase 2**：学习的自回归 boosted model 融合两个弱预测，利用两种解码方式的互补错误模式。BoostIE 是 BoostCD 在闭合信息抽取上的实例化，进一步用 DPO 增强分布外泛化。在 in-distribution 和 out-of-distribution 均优于先前方法。
- **约束类型:** Grammar + learned correction。底层约束来自 IE schema（关系类型、实体类型），boosted model 学习纠错。
- **与 OntoCoDec 的关系:** BoostCD 与 OntoCoDec 解决相似问题（约束解码质量退化）但方法论根本不同：BoostCD 通过训练 boosted model 学习融合两种解码结果，**需额外训练且 model-specific**；OntoCoDec 通过精心设计的 ontology 约束（Grammar+Semantic 分层）在单次前向约束解码中同时保证质量和合法性，**training-free 且 model-agnostic**。此外 BoostCD 的约束粒度是 sequence-level（整体输出融合），OntoCoDec 是 token-level + sequence-level 联合约束。BoostIE 支持动态约束（无需重训基础模型），OntoCoDec 同样支持（schema 变更→重新编译约束）。
- **BibTeX key:** `sakota2025boostcd`
- **ArXiv:** 2506.14901

### ADELIE | EMNLP 2024
- **Title:** Aligning Large Language Models on Information Extraction
- **Authors:** Qi, Peng, Wang et al. (THU-KEG)
- **核心方法:** 构建 IEInstruct 高质量对齐语料，用 SFT + DPO 训练 LLM 进行 IE，覆盖 closed IE、open IE、on-demand IE。ADELIE 在开源模型中达到 SOTA，同时保持通用 LLM 能力。
- **与 OntoCoDec 的关系:** ADELIE 代表 training-time alignment 路线，通过 preference optimization 让模型偏好合法输出。OntoCoDec 是 decoding-time enforcement 路线，提供更强保证且 training-free。两者可叠加使用。
- **BibTeX key:** `qi2024adelie`
- **ArXiv:** 2405.05008

---

## 4. Type-Checking / Ontology Validation in NLP

### ODKE+ | arXiv 2025
- **Title:** ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs
- **Authors:** Khorshidi, Nikfarjam, Shankar et al. (Apple)
- **核心方法:** 动态生成针对每种实体类型的 ontology snippets（含 domain/range 约束），用于对齐 LLM 抽取结果与 schema 约束。处理 9M+ Wikipedia 页面，19M facts，98.8% precision across 195 predicates。
- **与 OntoCoDec 的关系:** ODKE+ 在 prompt 层面注入 ontology 约束，属于 soft guidance。OntoCoDec 在 decoding 层面强制执行 domain/range 约束，属于 hard enforcement。ODKE+ 无法保证 0% violation rate，OntoCoDec 可以。
- **BibTeX key:** `khorshidi2025odke`
- **ArXiv:** 2509.04696

### Open IE with Entity Focused Constraints | Findings of EACL 2023
- **Title:** Open Information Extraction with Entity Focused Constraints
- **Authors:** Upadhyay, Balalau & Manolescu
- **核心方法:** 将 entity-type 知识作为约束注入 Open IE，通过 constrained inference（解码时）和 constraint-aware training 两种机制实现，在 CaRB 上 F1 提升 29.17%。
- **与 OntoCoDec 的关系:** 与 OntoCoDec 最相近的工作之一——同样在解码时利用 entity type 约束。但该方法针对 Open IE 的通用类型约束，OntoCoDec 针对 closed IE 的 ontology-specific domain/range 约束，粒度更细。
- **BibTeX key:** `upadhyay2023openie`

### EnriCo | arXiv 2024
- **Title:** EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction
- **Authors:** Zaratiana, Tomeh, Dauxais, Holat & Charnois
- **核心方法:** Attention-based enriched representations for joint entity and relation extraction，结合一套 constrained decoding 算法在推理时强制执行任务特定的结构约束（如 entity type compatibility for relations）。
- **与 OntoCoDec 的关系:** EnriCo 在传统 joint extraction 模型上加 constrained decoding，OntoCoDec 在 LLM 上做。EnriCo 的约束是模型特定的，OntoCoDec 的约束来自外部 ontology，更通用、可复用。
- **BibTeX key:** `zaratiana2024enrico`
- **ArXiv:** 2404.12493

### LLM as KG Curators | GenAIK 2025
- **Title:** Can LLMs be Knowledge Graph Curators for Validating Triple Insertions?
- **Authors:** Regino & dos Reis
- **核心方法:** 用 prompt-based 多阶段验证管线引导 LLM 评估 RDF triple 插入的 domain/range 一致性和语义连贯性。
- **与 OntoCoDec 的关系:** 典型的 post-hoc validation 方法——先生成再验证。OntoCoDec 是 preventive 方法——在生成时就阻止违规，不需要后续验证和纠错循环。
- **BibTeX key:** `regino2025kgcurator`

---

## 5. Constrained Decoding Quality Concerns

### Let Me Speak Freely? | EMNLP 2024
- **Title:** Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models
- **Authors:** Tam, Wu, Tsai, Lin, Lee & Chen
- **核心方法:** 系统研究结构化格式约束（JSON, XML, YAML）对 LLM 推理能力的影响。发现刚性格式约束损害推理密集型任务（数学、多跳 QA）但有利于分类任务（slot-filling、intent detection）。约束越严格，性能退化越大。
- **与 OntoCoDec 的关系:** 这是 OntoCoDec 需要直接回应的 concern。OntoCoDec 在 SciERC 上证明 F1 无损（甚至略有提升），说明在 IE 任务场景下——属于该论文发现的"分类任务"范畴——约束解码不仅不损害质量，反而可能有益。
- **BibTeX key:** `tam2024letmespeak`
- **ArXiv:** 2408.02442

### CRANE | ICML 2025
- **Title:** CRANE: Reasoning with Constrained LLM Generation
- **Authors:** Banerjee, Suresh, Ugare, Misailovic & Singh
- **核心方法:** 从理论角度解释为什么将 LLM 输出约束到 restrictive grammars（只允许语法合法的最终答案）会降低推理能力。提出 alternating strategy：在 unconstrained generation（推理/CoT）和 constrained generation（结构化输出）之间交替，在 GSM-symbolic 和 FOLIO 上提升最多 10 个百分点。
- **与 OntoCoDec 的关系:** CRANE 的发现验证了 OntoCoDec S2 策略（两通道分离）的合理性——S2 将推理（生成候选）和约束（格式化输出）分离到两个 pass，正是 CRANE 理论推荐的 alternating approach。
- **BibTeX key:** `banerjee2025crane`
- **ArXiv:** 2502.09061

### Structure Snowballing | arXiv 2026
- **Title:** From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection
- **Authors:** Zhou (Saarland University)
- **核心方法:** 发现 constrained decoding 应用于 LLM self-correction/reflection 时的新失败模式——"structure snowballing"：满足严格格式规则的认知负荷将模型推入格式陷阱而非改善推理。揭示结构粒度与模型内部容量之间的张力。
- **与 OntoCoDec 的关系:** OntoCoDec 避免了 snowballing 风险：其约束是 task-specific 的 IE 本体约束而非通用格式约束，且约束空间有限（合法类型集合远小于 free-form 生成空间），不会引入过度的认知负荷。
- **BibTeX key:** `zhou2026snowballing`
- **ArXiv:** 2604.06066

### The Hidden Cost of Structure | RANLP 2025
- **Title:** The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance
- **Authors:** Schall & de Melo
- **核心方法:** 跨 11 个模型和多个基准的系统实证研究。发现 base model 和 instruction-tuned model 在结构约束下表现分化：尽管约束保证格式合法，constrained decoding 在推理密集型任务上常降低语义正确性 10-30%。
- **与 OntoCoDec 的关系:** OntoCoDec 的实验在 instruction-tuned model 上进行，且 IE 任务是"extraction"而非"reasoning"，属于该论文发现的约束解码影响较小的任务类型。F1 无损结果与该论文的观察一致。
- **BibTeX key:** `schall2025hiddencost`

---

## 6. OntoCoDec 在 Landscape 中的定位

### 审稿人指定论文对比表

| Method | Constraint Source | Granularity | Composability (FT+CD) | Model-Agnostic | Task | Semantic Constraints |
|--------|------------------|-------------|----------------------|----------------|------|---------------------|
| **SynCode** (TMLR'25) | 手写 CFG/EBNF | Token-level | ✗ | ✓ | Code/JSON gen | ✗ |
| **IterGen** (ICLR'25) | 手写 CFG + 手写语义检查 | Token + symbol-level backtrack | ✗ | ✓ | SQL/Code gen | ✓ (手写) |
| **BoostCD/BoostIE** (EMNLP'25) | IE schema | Sequence-level (boosting) | ✓ (需训练 boosted model) | 部分 | Closed IE | ✓ (隐式学习) |
| **OntoCoDec (Ours)** | **Ontology schema 自动编译** | **Token + sequence-level** | **✓ (training-free)** | **✓** | **IE** | **✓ (自动编译)** |

### 核心差异化

OntoCoDec 在约束解码 landscape 中占据独特位置，体现为四个维度的创新：

**1. 约束来源自动化 (vs. SynCode/IterGen)**
- SynCode/IterGen 需手工编写 CFG 规则和语义检查程序
- OntoCoDec 从 ontology schema 自动编译约束，schema 变更时无需重写约束规则

**2. 约束层次：从格式到语义 (vs. SynCode/XGrammar/Outlines)**
- 现有 grammar-constrained decoding（SynCode, XGrammar, Outlines, LMQL）保证**格式正确性**（valid JSON, enum values）
- 现有 vocabulary-constrained generation（GENRE, NeuroLogic）保证**词汇合法性**（输出在预定义词表中）
- OntoCoDec 增加**语义正确性**层（domain/range 约束），将约束从 syntactic 扩展到 semantic

**3. Training-free + Model-agnostic (vs. BoostCD/BoostIE)**
- BoostCD 需额外训练 boosted model + DPO，且 model-specific
- OntoCoDec 的约束解码组件直接应用于任何自回归 LLM，无需额外训练
- 两者均支持动态约束，但 OntoCoDec 更轻量（只需重新编译 schema→约束）

**4. 前向预防 vs. 回溯修复 (vs. IterGen) / 后融合 (vs. BoostCD)**
- IterGen 生成→检测违规→回溯→重新生成（reactive）
- BoostCD 生成两个候选→训练模型融合（post-hoc learning）
- OntoCoDec 在每步前向传播中直接屏蔽非法 token（preventive），无需回溯或融合

**5. 质量保持：约束无损**
- 约束解码质量 concern（Let Me Speak Freely, CRANE, Structure Snowballing）指出约束常损害推理
- OntoCoDec 在 SciERC 上 DR violation 15.37%→0.93%（↓94%）且 F1 无损，反驳"约束必损质量"的 narrative
- OntoCoDec S2 策略（两通道分离）符合 CRANE 理论推荐的 alternating approach

### 技术栈定位

```
Layer 3 (OntoCoDec Semantic): domain/range logits masking ← 本文贡献
Layer 2 (OntoCoDec Grammar):  JSON schema + enum constraints ← 基于 XGrammar
Layer 1 (LLM):                base language model generation
```

- Layer 2 消除 format violations（RV/ET），与 Outlines/LMQL/SGLang 同层
- Layer 3 消除 semantic violations（DR），是 OntoCoDec 独有的贡献
- 两层组合（S1 单通道或 S2 两通道）实现从格式到语义的完整约束覆盖

### 与各 paradigm 的关系总结

| Paradigm | 代表工作 | OntoCoDec 关系 |
|----------|----------|---------------|
| Grammar-constrained decoding | **SynCode**, XGrammar, Outlines, LMQL | OntoCoDec Grammar 层基于此；Semantic 层是超越 |
| Iterative/backtracking generation | **IterGen** | 同样结合语法+语义约束，但需手写检查器且用回溯；OntoCoDec 自动编译+前向预防 |
| Boosted constrained decoding | **BoostCD/BoostIE** | 同为 IE 约束解码，但需训练 boosted model；OntoCoDec training-free |
| Vocabulary/type-constrained generation | GENRE, GenIE, GCD | OntoCoDec 借鉴 logits masking 技术，但约束来自 IE ontology 而非固定词表 |
| Structural constraint for IE | UIE, GoLLIE, CodeIE | 这些方法靠 training/prompting，OntoCoDec 是 decoding-time enforcement，两者互补 |
| Ontology validation | ODKE+, EnriCo | Post-hoc validation vs. preventive enforcement 的本质区别 |
| Constrained decoding quality | Let Me Speak Freely, CRANE | OntoCoDec F1 无损实验直接回应此 concern，S2 策略符合 CRANE 理论 |
