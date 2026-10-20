# Literature Freshness Check (2025-2026)

> 检查日期: 2026-05-18 | 目标: 发现 OntoCoDec 的遗漏竞品和应引用工作

---

## 直接竞品

| Title | Venue/Year | 关系 | 摘要 |
|-------|-----------|------|------|
| **BoostCD / BoostIE: Combining Constrained and Unconstrained Decoding via Boosting** | EMNLP 2025 Main | **直接竞品** | 对同一输入分别做 constrained 和 unconstrained decoding，用学习的 boosted model 组合两组预测。应用于 closed IE，声称互补性可消除各自错误。与 OntoCoDec 的区别：需要训练 boosted model，而 OntoCoDec 是 training-free；BoostCD 不区分格式约束和语义约束两层。**必须在 Related Work 中 address。** |
| **Grammar-Constrained Decoding for Structured IE (Clinical Trial Abstracts)** | Frontiers in AI, 2025 (PMC11747381) | **直接竞品** | 用 CFG grammar 约束 fine-tuned encoder-decoder (Longformer, Flan-T5) 做临床试验摘要的结构化 IE。发现 constrained > unconstrained 5-13 F1 points。与 OntoCoDec 的区别：只有格式层约束，无 type-level 语义约束；用小模型 fine-tuning 而非 LLM zero-shot。**应引用，作为 grammar-constrained IE 的实证支持。** |
| **GCD-IE: Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning** (Geng et al.) | EMNLP 2023 (v6 更新至 2025) | **直接竞品** | Input-dependent grammar 用于 IE、entity disambiguation、constituency parsing，无需 fine-tuning。已在 literature_map 中。v6 可能有新实验，需检查更新内容。OntoCoDec 在此基础上增加了 type-level 语义约束层。 |

## 应引用

### Constrained Decoding 质量问题（需在论文中 address）

| Title | Venue/Year | 关系 | 摘要 |
|-------|-----------|------|------|
| **Grammar-Aligned Decoding (ASAp)** | NeurIPS 2024 | 理论基础 | 证明 naive GCD 会扭曲 LLM 分布，产出虽合法语法但低质量。提出 ASAp 用近似 expected futures 做 adaptive sampling。**OntoCoDec 的 Layer 2 type constraint 也是 masking+renormalization，需 acknowledge 此风险并论证为何 IE 场景下 type constraints 的约束空间足够大不会严重扭曲分布。** |
| **The Format Tax** | arXiv 2604.03616 (2026) | 重要背景 | 结构化输出要求降低开放权重模型的推理和写作性能，但闭源模型几乎无此问题。"Format-requesting instructions 本身即造成大部分性能损失，甚至在 decoder constraint 生效前"。提出 free-form first + reformat 的两步方案。**需在 Discussion 中 address：OntoCoDec 的 constrained decoding 是否引入 format tax，以及 IE 任务的 format tax 与 reasoning 任务是否不同。** |
| **The Hidden Cost of Structure** | RANLP 2025 | 重要背景 | 通过 log-probability 分析证明 constrained decoding 迫使模型偏离自然语言偏好模式。指出 instruction-tuning 可能无意中降低结构化输出能力。 |
| **DCCD: Draft-Conditioned Constrained Decoding** | arXiv 2603.03305 (2026) | 互补方法/替代方案 | 两步 training-free 方法：先 unconstrained draft，再 conditioned constrained decoding。通过 KL-projection 视角分析，draft conditioning 增大 feasible mass 减小 "projection tax"。**与 OntoCoDec 互补：可在 Future Work 中讨论将 DCCD 与 OntoCoDec 的 type constraints 结合。** |
| **From Hallucination to Structure Snowballing** | arXiv 2604.06066 (2026) | 相关 | 用 Outlines constrained decoding 做 structured reflection，发现 "structure snowballing" 新失败模式。8B 模型上 constrained decoding 不改善自我修正反而触发格式陷阱。**IE 场景不涉及 reflection/self-correction，但需了解此局限性。** |

### Constrained Decoding 效率（OntoCoDec 使用 xgrammar）

| Title | Venue/Year | 关系 | 摘要 |
|-------|-----------|------|------|
| **Pre³: Enabling DPDA for Faster Structured LLM Generation** | ACL 2025 | 工程相关 | 将 LR(1) grammar 预编译为 DPDA，TPOT 降低 40%，吞吐提升 36%。与 OntoCoDec 使用 xgrammar 的 Layer 1 互补，可在 efficiency 讨论中引用。 |
| **ZapFormat: Earley-Driven Dynamic Pruning for Efficient Structured Decoding** | ICML 2025 | 工程相关 | 基于 Earley 算法动态剪枝无效状态，constrained decoding 速度提升 2x。同属 constrained decoding 效率优化。 |
| **JSONSchemaBench** (Geng et al.) | arXiv 2501.10868 (2025) | Benchmark | 首个系统评估 constrained decoding 框架的 benchmark，比较 efficiency/coverage/quality。包含 xgrammar 评测。**OntoCoDec 可用此 benchmark 定位 Layer 1 的性能。** |

### IE with LLMs（方法对比）

| Title | Venue/Year | 关系 | 摘要 |
|-------|-----------|------|------|
| **PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction** | EMNLP 2025 Industry | 互补方法 | 不约束解码，而是优化 JSON schema 使其对 LLM 更友好。SWDE 上 extraction accuracy 提升 64.7%。与 OntoCoDec 互补：OntoCoDec 约束解码过程，PARSE 优化输入 schema。 |
| **SLOT: Structuring the Output of Large Language Models** | EMNLP 2025 Industry | 替代方案 | Post-hoc 方法：LLM 自由生成文本，再用专门模型转为 structured JSON。解耦 formatting 和 task-specific generation。Fine-tuned Mistral-7B + constrained decoding 达 99.5% schema accuracy。**作为 "post-hoc structuring vs. inline constrained decoding" 的对比方法，需在 Related Work 中讨论。** |
| **GUIDEX: Guided Synthetic Data for Zero-Shot IE** | ACL 2025 Findings | 相关方法 | GoLLIE 同组后续工作。自动定义 domain-specific schemas + 生成合成标注数据。Llama 3.1 + GUIDEX 在 7 个 zero-shot NER benchmark 上 SOTA。与 OntoCoDec 不同方向：GUIDEX 解决 zero-shot 泛化，OntoCoDec 解决输出合法性。 |
| **G&O: Generate & Organize for IE** | arXiv 2402.13364 (2024) | 替代方案 | 两步 prompting：先自由文本生成内容，再组织为结构化格式。零样本 NER 和 RE 上显著提升 precision。**作为 "two-step decoupling" 范式的代表，需在 Related Work 中与 OntoCoDec 的 "inline constraint" 范式对比。** |
| **Schema Reinforcement Learning** | ACL 2025 Main | 相关方法 | 用 fine-grained schema validator 做 RL reward，训练 LLM 生成合法 JSON。SchemaBench 上超越 SFT baseline。与 OntoCoDec 不同：需要训练，OntoCoDec 是 inference-time。 |

### Surveys

| Title | Venue/Year | 关系 | 摘要 |
|-------|-----------|------|------|
| **A Survey of Generative Information Extraction** | COLING 2025 | 领域综述 | 系统梳理 generative IE 方法，覆盖 NER/RE/EE 各子任务。Related Work 写作可参考其分类框架。 |
| **Large LMs for Generative IE: A Survey** | Frontiers of Computer Science, 2025 | 领域综述 | 另一篇综合 survey，按 IE 子任务和技术分类。可交叉引用。 |

## 不需引用（已排除）

| Title | 原因 |
|-------|------|
| Type-Constrained Code Generation (ACL 2025) | 代码生成方向，非 IE |
| Lazy-k Decoding (EMNLP 2023) | Token classification 的约束解码，非生成式 IE；且为 2023 年论文，非新工作 |
| StructEval (2025) | 评估 LLM 结构化输出能力的 benchmark，不针对 IE |

---

## 结论与建议

### 1. 是否有遗漏的直接竞品？

**是。BoostCD/BoostIE (EMNLP 2025) 是最重要的遗漏竞品。** 它同样使用 constrained decoding 做 closed IE，且发表在 EMNLP 2025 main conference。必须在 Related Work 中 address，并明确差异化：
- BoostCD 需要训练 boosted model，OntoCoDec 完全 training-free
- BoostCD 将 constrained/unconstrained 视为两个 "weak learner"，OntoCoDec 将约束分为格式层和语义层
- BoostCD 不利用 ontology schema 的 type 信息做 token-level 约束

### 2. 是否有需要在 Related Work 中 address 的新工作？

**需 address 的关键工作（按优先级）：**

1. **BoostCD** — 直接竞品，必须 address
2. **SLOT / G&O** — "post-hoc structuring" 替代范式，需讨论 inline vs. post-hoc 的 trade-off
3. **DCCD** — 另一种缓解 constrained decoding 质量损失的方法，与 OntoCoDec 可能互补
4. **Grammar-Aligned Decoding** — 理论上指出 naive GCD 的分布扭曲问题，需论证 OntoCoDec 的约束不会严重扭曲
5. **PARSE** — schema optimization 互补方向
6. **Schema RL** — training-based 替代方案
7. **GUIDEX** — GoLLIE 后续，同领域

### 3. 是否有与我们结论矛盾的发现？

**有潜在风险，但可化解：**

- **The Format Tax (2026)** 和 **The Hidden Cost of Structure (RANLP 2025)** 均指出 constrained decoding 可能降低输出质量。但它们主要针对 reasoning/writing 任务，IE 的 extraction 任务复杂度较低，且 OntoCoDec 的 type constraints 是 domain-specific 的窄约束（不是全格式重写）。**建议在论文中加入消融实验：对比有/无 type constraints 时的 extraction quality，证明 OntoCoDec 的约束不引入显著 quality degradation。**

- **Structure Snowballing (2026)** 发现 constrained decoding 在 8B 模型上触发格式陷阱。**需确认 OntoCoDec 在小模型上的表现，如有类似问题需 acknowledge。**

- **DCCD** 和 **G&O** 都主张 "先自由生成再约束/格式化" 优于 "inline 约束"。**OntoCoDec 需要实验证据证明 inline type constraints 在 IE 场景下优于 post-hoc filtering。**

### 4. 行动建议

| 优先级 | 行动 |
|--------|------|
| **P0** | 将 BoostCD 加入 literature_map 和 Related Work |
| **P0** | 在 Related Work 中增加 "Constrained Decoding Quality" 讨论段落，address Grammar-Aligned Decoding / Format Tax / Hidden Cost |
| **P1** | 加入 SLOT、G&O 作为 "post-hoc structuring" 对比方向 |
| **P1** | 加入 DCCD 作为互补方法 |
| **P1** | 引用 JSONSchemaBench 支撑 xgrammar 选择 |
| **P2** | 引用 Pre³、ZapFormat 作为 constrained decoding 效率优化背景 |
| **P2** | 引用 GUIDEX、Schema RL 作为 IE with LLMs 的最新工作 |
| **P2** | 引用 COLING 2025 survey 作为领域综述 |
