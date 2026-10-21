# BoostCD / GCD / IterGen 量化对比数据

> 提取日期: 2026-05-20 | 用途: Reviewer 要求 §6 Related Work 对 BoostCD 做更具体对比

---

## BoostCD (Sakota & West, EMNLP 2025)

**论文**: "Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction" (arXiv:2506.14901)

- **数据集**: Wiki-cIE Code (合成, ~1.8M train / 10K val / 50K test) + 50 篇 Wikipedia 自然文本 (OOD)。使用 ~600 条 REBEL 样本做 DPO。
- **SciERC 结果**: **无**。不使用 SciERC、DocRED、ACE05 或任何标准 NLP IE benchmark。评测完全基于 Wiki/Wikidata。
- **任务定义**: Closed IE (cIE)——从文本提取 (subject, relation, object) 三元组，所有实体/关系必须属于预定义 KB (Wikidata)。
- **输出格式**: 线性化三元组 `[s] subject [r] relation [o] object [e]`，实体为 **English Wikipedia 标题**（非 Wikidata QID），关系为 **Wikidata 关系标签**（人类可读名称）。
- **模型**: FlanT5-base (~250M params)，base model 和 boosted model 均用此架构。未使用大规模 LLM。
- **约束类型**: **仅 KB membership 约束**——基于实体/关系名称的 prefix trie，确保输出的实体和关系存在于 KB 中。无 domain-range type constraint，无 Wikidata property constraint。另强制线性化格式（delimiter 顺序）。
- **KB 规模**: 2.6M 实体 (关联 English Wikipedia)，888 关系。
- **关键指标**:
  - Wiki-cIE Code test: BoostIE Micro F1 = **52.35** (vs SynthIE 35.30, ReLiK 21.79)
  - Wikipedia 自然文本 OOD: BoostIE+DPO Micro F1 = **34.93** (vs ReLiK 23.99, SynthIE 8.76)
  - 声称: +17.05 Micro F1 (in-distribution), +10.94 Micro F1 (OOD) over prior best
- **错误分析** (50 Wikipedia 样本):
  - Misclassified entity: BoostIE **0.00** vs SynthIE 0.09 (KB 约束消除实体分类错误)
  - Unrelated triplets: BoostIE+DPO **0.08** vs SynthIE 0.60
- **Baselines**: SynthIE 400k (Josifoski et al., 2023), ReLiK (Orlando et al., 2024), GenIE (仅用于 DPO 数据生成)
- **方法核心**: 两阶段 boosting——Phase 1 base model 分别做 constrained 和 unconstrained decoding 得两个弱预测；Phase 2 boosted model 学习融合互补错误。

### 与 OntoCoDec 不可比维度

1. **数据集不重叠**: BoostCD 用 Wiki-cIE Code / Wikipedia 自然文本；OntoCoDec 用 SciERC (科学文献领域)。无共同评测集。
2. **任务定义不同**: BoostCD 做 closed IE (KB-grounded triplet extraction, 实体须存在于 2.6M Wikidata 实体中)；OntoCoDec 做 span-level NER + RE (实体为文本 span，非 KB 链接)。
3. **约束类型不同**: BoostCD 仅用 KB membership 约束 (prefix trie)；OntoCoDec 用 schema-level semantic constraints (domain-range type constraints, ontological consistency)。
4. **输出粒度不同**: BoostCD 输出 Wikipedia 标题 + Wikidata 关系名；OntoCoDec 输出文本 span + schema-defined 关系类型。
5. **模型规模不同**: BoostCD 用 FlanT5-base (250M)；OntoCoDec 评测涵盖不同规模 LLM。
6. **评估指标不可比**: BoostCD 的 F1 基于 Wikidata triplet exact match；OntoCoDec 基于 span-level strict/relaxed F1。

---

## GCD (Geng, Josifoski, Peyrard & West, EMNLP 2023)

**论文**: "Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning" (arXiv:2305.13971)

- **数据集**:
  - cIE: SynthIE-text (合成, 10K val / 50K test, KB: 2.7M Wikidata 实体, ~888-1000 关系)
  - Entity Disambiguation: AIDA-CoNLL, MSNBC, ACE2004, AQUAINT, CLUEWEB, WIKI
  - Constituency Parsing: Penn Treebank test split
- **SciERC 结果**: **无**。GCD 不在 SciERC 上评测。IE 评测仅用 SynthIE-text (Wikidata-based)。
- **任务定义**: 三个任务——(1) Closed IE: 从 KB 中提取三元组；(2) Entity Disambiguation: 将 mention 链接到 KB 实体；(3) Constituency Parsing: 句法分析树。
- **输出格式**: Wikidata 实体/关系 **文本名称**（非 QID），格式 `[s] entity_name [r] relation_name [o] entity_name`。
- **模型**: LLaMA-7B / 13B / 33B, Vicuna-7B / 13B, GenIE T5-base (baseline)。纯 few-shot，无微调。
- **约束类型**: **Context-Free Grammar (CFG)**，通过 Grammatical Framework (GF) 实现。两种模式：
  - IIG (Input-Independent Grammar): 固定语法，候选集=整个 KB
  - IDG (Input-Dependent Grammar): 语法随输入变化，候选集更窄更强
- **关键指标 (cIE, 4-shot, SynthIE-text)**:
  - LLaMA-33B constrained: F1 = **36.0** (vs unconstrained 17.5)
  - LLaMA-13B constrained: F1 = **30.6** (vs unconstrained 12.9)
  - GenIE T5-base (fine-tuned): F1 = **34.8**
  - 约束解码使 LLaMA-33B few-shot 略超过 fine-tuned GenIE
- **约束满足率**:
  - cIE/ED with grammar: **100% valid** (by construction)
  - CP with IDG: **100% validity** (vs unconstrained 54.3%-69.4%)
- **延迟**: cIE 约 69ms/token (由于百万级语法规则)
- **Baselines**: GenIE T5-base (cIE), BLINK/GENRE/ReFinED (ED), Vinyals/Dyer/Kitaev (CP)

### 可比性评估

- **与 BoostCD 同一团队 (EPFL dlab)**，BoostCD 是 GCD 的后续工作。
- **与 OntoCoDec 不可比**: 同样的维度——不用 SciERC、任务为 Wikidata-grounded closed IE 而非 span-level RE、约束是 KB membership grammar 而非 schema semantic constraints、输出为 KB entity name 而非 text span。
- GCD 的 CFG 框架是通用的，理论上可以编码 domain-range constraints，但论文中未实现此类约束。

---

## IterGen (Ugare et al., ICLR 2025)

**论文**: "IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking" (arXiv:2410.07295)

- **数据集**: Spider (text-to-SQL, 1034 题) + DecodingTrust privacy benchmark (100 题, Enron email)
- **SciERC 结果**: **无**。不涉及任何 IE 数据集。
- **任务定义**: (1) Text-to-SQL (schema constraint enforcement); (2) Privacy leakage prevention。**无任何信息抽取任务。**
- **模型**: Qwen2.5-0.5B / 1.5B / Coder-1.5B, Llama-3.2-1B / 3B (SQL); Llama-2-7B-chat / Llama-3-8B (privacy)。全部为小到中等模型 (0.5B-8B)。
- **约束类型**: **CFG (Lark EBNF 语法)**，LR shift-reduce parser。核心创新为 **backtracking**——通过 symbol-to-position mapping 和 KV cache 维护实现前进/后退。SQL 中将 table/column 名编码为 CFG non-terminal。
- **关键指标**:
  - SQL (Spider): IterGen 平均 overall acc **41.6%** vs SynCode 35.1% vs Standard 27.6%
  - 最佳单模型: Qwen2.5-Coder-1.5B + IterGen exec acc **88.8%**
  - Privacy: **0 leaks** across all 9 models (vs standard 45-67 leaks / 100 prompts)
  - 声称 "18.5% mean improvement over SynCode"
- **Baselines**: Standard (unconstrained greedy), SynCode (Ugare et al., 2024, 同一作者前作)

### 可比性评估

- **与 OntoCoDec 完全不可比**: IterGen 不做 IE 任务，应用域为 SQL 生成和隐私保护。
- **方法论关联**: IterGen 的 backtracking + semantic check 思路与 OntoCoDec 的 schema constraint checking 在抽象层面相似（都在解码过程中施加语义约束），但具体实现和应用场景完全不同。
- IterGen 的 CFG + backtracking 是通用框架，理论上可扩展到 IE，但论文未探索此方向。

---

## 三方对比总结

| 维度 | BoostCD | GCD | IterGen | OntoCoDec (ours) |
|------|---------|-----|---------|------------------|
| 会议 | EMNLP 2025 | EMNLP 2023 | ICLR 2025 | — |
| IE 任务 | Closed IE (KB-grounded) | Closed IE (KB-grounded) | 无 IE 任务 | Span-level NER+RE |
| 评测数据 | Wiki-cIE Code | SynthIE-text | Spider (SQL) | SciERC 等 |
| SciERC | **否** | **否** | **否** | **是** |
| 约束类型 | KB membership (trie) | CFG (GF) | CFG + backtracking | Schema semantic |
| 输出格式 | Wikipedia title + Wikidata rel | Wikidata entity/rel name | SQL / text | Text span + rel type |
| 模型 | FlanT5-base (250M) | LLaMA 7-33B | Qwen/Llama 0.5-8B | LLM (多规模) |
| 核心差异 | Boosting 融合 C/U 解码 | Grammar 统一框架 | Backtracking 迭代修正 | 本体语义约束 |

**结论**: 三篇论文均不在 SciERC 上评测，任务定义 (KB-grounded closed IE vs span-level IE) 和约束类型 (KB membership / CFG vs schema semantic constraints) 存在本质差异，直接数值对比不具意义。
