# Director coordination — Part 8 of 8

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

[← Part 7](part-007.md) · [Transcript overview](../director-coordination-copy-2.md) · [Structured JSON](../../../sessions/eb/ebac95f2406b6d6dc37e.json)

## Round 180

### Tool call

_source line 2500 · 2026-05-23T10:28:01.113383+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- Venue：EMNLP 2026（通过 ARR 统一审稿）\n- Deadline：2026-05-25\n- 格式：ACL 长文，正文 8 页限制（不含 references、limitations、ethics）\n- 匿名：double-blind\n- 论文路径：artifacts/_project/paper/main.tex\n- PDF 路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_25/submitted.pdf\n\n## Overall Assessment 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- OntoCoDec 相对于现有 constrained decoding 方法（XGrammar、Outlines、SGLang、PICARD、KG-Trie）的增量贡献\n- 与 schema-aware IE 方法（GoLLIE、KnowCoder、Sainz et al.）的定位差异是否清晰\n- Entity registry + dynamic masking 是否构成足够的技术新颖性\n- Proposition 1（context-free 不足以表达 domain/range constraints）是否是 well-known fact\n\n### 2. 完整性评估\n- 论文的 claim 是否都有充分的实验支持\n- Contribution 声明是否准确、是否 overclaim\n- Abstract 中的数字是否与正文一致\n- 是否有重要的实验缺失（如：更多模型族的 70B 验证、更多数据集、更多 fine-tuning 方法）\n- WikiEvents pilot（n=20）作为 \"task generalization\" 证据是否充分\n- 70B 验证仅用 AWQ INT4 单模型族，是否足以支撑 scalability claim\n\n### 3. 写作质量\n- 论文结构是否清晰、逻辑流是否通顺\n- 术语使用是否一致（DR/RV/ET/CF 的定义和使用）\n- 图表质量和信息密度\n- Abstract 是否准确反映论文内容\n- Related work 的覆盖度和定位准确性\n\n### 4. 格式合规性（EMNLP 2026 / ACL 格式）\n- 正文是否在 8 页以内\n- 匿名处理是否彻底（代码链接、数据链接、自引）\n- Limitations section 是否存在且内容充分\n- Ethics statement 是否存在\n- References 格式是否正确\n\n### 5. 遗漏的相关工作\n- 检查是否遗漏了重要的近期工作（2024-2025 年的 constrained decoding、IE、schema enforcement 相关论文）\n- 特别关注：CRANE (Banerjee et al., 2025)、EnriCo (Zaratiana et al., 2024)、IterGen (Ugare et al., 2025) 等是否被充分讨论\n\n请给出完整的审稿意见，包含：Summary、Strengths（逐条）、Weaknesses（逐条，标注严重程度 [Critical/Major/Minor]）、Questions、Missing References、Overall Assessment（评分+置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- Venue：EMNLP 2026（通过 ARR 统一审稿）\n- Deadline：2026-05-25\n- 格式：ACL 长文，正文 8 页限制（不含 references、limitations、ethics）\n- 匿名：double-blind\n- 论文路径：artifacts/_project/paper/main.tex\n- PDF 路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_25/submitted.pdf\n\n## Overall Assessment 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- OntoCoDec 相对于现有 constrained decoding 方法（XGrammar、Outlines、SGLang、PICARD、KG-Trie）的增量贡献\n- 与 schema-aware IE 方法（GoLLIE、KnowCoder、Sainz et al.）的定位差异是否清晰\n- Entity registry + dynamic masking 是否构成足够的技术新颖性\n- Proposition 1（context-free 不足以表达 domain/range constraints）是否是 well-known fact\n\n### 2. 完整性评估\n- 论文的 claim 是否都有充分的实验支持\n- Contribution 声明是否准确、是否 overclaim\n- Abstract 中的数字是否与正文一致\n- 是否有重要的实验缺失（如：更多模型族的 70B 验证、更多数据集、更多 fine-tuning 方法）\n- WikiEvents pilot（n=20）作为 \"task generalization\" 证据是否充分\n- 70B 验证仅用 AWQ INT4 单模型族，是否足以支撑 scalability claim\n\n### 3. 写作质量\n- 论文结构是否清晰、逻辑流是否通顺\n- 术语使用是否一致（DR/RV/ET/CF 的定义和使用）\n- 图表质量和信息密度\n- Abstract 是否准确反映论文内容\n- Related work 的覆盖度和定位准确性\n\n### 4. 格式合规性（EMNLP 2026 / ACL 格式）\n- 正文是否在 8 页以内\n- 匿名处理是否彻底（代码链接、数据链接、自引）\n- Limitations section 是否存在且内容充分\n- Ethics statement 是否存在\n- References 格式是否正确\n\n### 5. 遗漏的相关工作\n- 检查是否遗漏了重要的近期工作（2024-2025 年的 constrained decoding、IE、schema enforcement 相关论文）\n- 特别关注：CRANE (Banerjee et al., 2025)、EnriCo (Zaratiana et al., 2024)、IterGen (Ugare et al., 2025) 等是否被充分讨论\n\n请给出完整的审稿意见，包含：Summary、Strengths（逐条）、Weaknesses（逐条，标注严重程度 [Critical/Major/Minor]）、Questions、Missing References、Overall Assessment（评分+置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 2501 · 2026-05-23T10:28:02.532027+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1418
}
```

</details>

---


### Assistant

_source line 2502 · 2026-05-23T10:28:15.144091+00:00_

Round 1 已启动：
- 视觉审查 Agent：已派发（fire-and-forget）
- Reviewer 1（方法严谨性 + 实验设计）：已分配
- Reviewer 2（新颖性 + 完整性 + 写作质量）：已分配

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 181

## Round 181

2 recorded events


### User

_source line 2503 · 2026-05-23T10:34:45.947414+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

---

## Summary

本文提出 OntoCoDec，一个将 IE 本体论编译为两层 token-level 约束的框架：grammar layer（基于 XGrammar 的 CFG）负责 JSON 结构和词汇约束，semantic layer（entity registry + dynamic masking）负责 domain/range 类型约束。作者提出三级约束分类法（context-free / prefix-decidable with state / non-local），并通过 pumping lemma 证明 Level 2 约束超出 CFG 表达能力（Proposition 1）。实验在 SciERC（7 relations）、DocRED（96 relations）和 WikiEvents pilot（n=20）上评估，覆盖 3 个 8B 模型族 + 1 个 70B 模型（AWQ INT4），报告了 zero-shot 和 LoRA fine-tuning 两种设置下的消融实验。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | Proposition 1 证明正确；消融设计严谨（5-way ablation + bootstrap CI + Bonferroni correction）；但 κ-DR 相关性 n=3 无统计效力，CF trade-off 实质影响被淡化 |
| Excitement | 3/5 | 解决了真实问题（15-18% violation rates），但核心洞察（grammar 不能约束跨实体类型一致性）在 constrained decoding 社区已是 known intuition，贡献偏工程化 |
| Reproducibility | 4/5 | 超参数、prompts、硬件配置详尽（Appendix I）；承诺 acceptance 后开源；唯一缺失是代码尚不可用 |
| Overall Assessment | 3.5 | Borderline Conference |
| Confidence | 4/5 | 本人熟悉 constrained decoding 和结构化 IE 领域 |

---

## 主要优势

**S1.** 三级约束分类法（§3 Constraint decidability taxonomy）概念清晰且有实用价值。将 IE 类型约束按可判定性分为 context-free / prefix-decidable with state / non-local 三级，为该领域提供了一个有用的思维框架。Proposition 1 的 pumping lemma 证明（Appendix O）在技术上正确：通过构造 $w_n = \tau_B^{n-1}\tau_A\;\texttt{REL}(h{=}e_n, r, \tau_A)$ 并分析 pumping 对 position→type binding 的破坏，论证严谨。Position-based 到 name-based 的推广论证（Appendix O "Position indexing vs. name referencing"）也合理。

**S2.** 消融实验设计优秀。5-way ablation on SciERC（Table 1: unconstrained / grammar-only / GCD-equiv / semantic-only / S1 / S2）是该论文最强的实验贡献，每层的边际贡献清晰可见（grammar 3% DR reduction, semantic 24%, 组合 94%）。GCD-equiv 通过 vLLM `guided_json` 外部验证（Appendix S）增强了可信度。

**S3.** 统计方法严谨。Bootstrap CI（10,000 iterations, Table 6）、Bonferroni correction for multiple comparisons、Cohen's d effect sizes 的使用在 NLP 论文中不常见且值得肯定。per-configuration corrected p-values 的报告（Qwen3-8B/SciERC p_adj=1.00 等）是诚实的。

**S4.** Cross-model 验证覆盖面好。3 个 tokenizer family（Qwen BPE、Llama BPE、Mistral SentencePiece）× 2 datasets（Table in §5, Appendix Q）验证了 continuation masking 的 tokenizer-agnostic 性。

**S5.** 工程完整性强。Appendix 31 页覆盖了几乎所有可预见的质疑：causal tracing（Appendix C）、cascade error analysis（Appendix C）、order invariance（Appendix N）、prompt sensitivity（Appendix I）、document length effect（Appendix H）、quantization robustness（Appendix R）、sampling robustness（Appendix E）。这是我见过的附录最充分的论文之一。

**S6.** Grammar-first fallback 机制设计合理。优先保证 JSON 结构完整性、将类型违规作为 soft error 处理的设计哲学符合实际部署需求（§4, Eq. 2）。Fallback causal tracing（Appendix C Table 4）提供了有力的机制验证。

---

## Must-Fix 问题（影响接收决定）

**N1** [Critical] κ-DR 相关性（n=3）统计上无意义，但被赋予过高叙事地位

- 具体位置：§4 "Constraint Tightness" paragraph; Figure 3 (p.23)
- 问题：κ̄ 与 DR reduction 的相关性仅基于 3 个数据点（WikiEvents κ̄=0.029, SciERC κ̄=0.333, DocRED κ̄=0.842）。论文报告 p=0.138 并称"descriptive"，但该结果出现在正文 §4 的独立段落中，配有定义式（κ(r) = 1 − |σ(r)|/|E|²），在 Appendix 中有独立的 case study（Appendix N, P）和 Figure 3。这种叙事比重暗示 κ 是一个有解释力的指标，但 n=3 时任意 3 个单调点都能产生类似相关性。此外，论文自己承认"entity type confusability is a critical co-factor"（§4），这意味着 κ 是 confounded variable，不能独立解释 DR reduction。
- 为什么影响接收：Reviewer 会认为这是 overclaiming——用无统计效力的相关性暗示因果关系。
- 建议修改方向：（1）将 κ 降格为"描述性案例对比"而非"相关性"，删除 p 值报告（n=3 的 p 值本身就误导）；（2）在正文中明确声明"three schemas are insufficient to establish a general relationship"；（3）或者增加 2-3 个不同 schema 的数据集验证。

**N2** [Critical] CF 作为结构性 trade-off 被低估——zero-shot greedy 下 CF rate 9.90% 是一个严重的实用性问题

- 具体位置：Table 1 (CF column); §5.1 "Cross-field violation analysis"; §4 "Greedy limitation and fallback cascade"
- 问题：在 zero-shot greedy S1 下，DR 从 15.37% 降至 0.93%（↓94%），但 CF 从 0.08% 升至 9.90%。Total violation rate（DR+CF）从 15.45% 降至 10.83%，仅降低 30%。论文将 DR→CF 称为"severity downgrade"（§5.1），但这需要更充分的论证：(a) CF 意味着同一实体在不同 triple 中被赋予不同类型，这在下游知识图谱应用中可能同样严重；(b) 论文声称 CF 可通过 post-hoc TCR 解决（Appendix M, 18-92% reduction），但 TCR 并未集成到系统中，而是作为 future work 提及。
- Abstract 中"reduces domain/range violations by 62% on average"和"near-complete DR elimination"的表述在有 9.90% CF 的情况下可能误导读者，因为它选择性地报告了一种违规类型的改善而忽略了另一种的恶化。
- 为什么影响接收：Total violation reduction 仅 30%（zero-shot greedy）的系统难以支撑 §7 中"constraint enforcement is preserved under INT4"这类强表述。Reviewer 期望看到对 DR→CF trade-off 的更诚实的讨论。
- 建议修改方向：（1）在 Abstract 和 Introduction 中同时报告 DR reduction 和 CF increase，给出 total violation 的净变化；（2）将 beam search（k=4, 所有 violation→0%）作为推荐配置而非可选项，或更明确地讨论 greedy 的局限性；（3）提供 CF 对下游任务影响的定量分析（比如 CF triples 中有多少是 gold match）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [Major] Proposition 1 的实际价值：formalizing known intuition vs. genuine theoretical contribution

- 具体位置：§3 Proposition 1; Appendix O
- 问题：在 constrained decoding 领域，grammar 不能约束跨位置的语义依赖关系是广泛已知的直觉。XGrammar (Dong et al., 2025)、GCD (Geng et al., 2023)、Outlines (Willard and Louf, 2023) 的论文都隐含地承认了这一点。Proposition 1 将这个直觉形式化为 pumping lemma 证明，这本身是有价值的，但论文将其作为核心贡献之一（Introduction bullet 1: "a two-layer constrained decoding framework, formalizing a known intuition"），这个定位的诚实性值得肯定，但也意味着理论新颖性有限。
- 补充说明：工程适用性段落（§3 "Engineering applicability"）承认有限实体集理论上是 regular 但 DFA 状态数指数级爆炸（6^17 ≈ 1.6×10^13 for SciERC）。这个论证对于实际价值更重要，但也意味着 Proposition 1 的不可能性结论是渐近的（unbounded entities），与实际有限场景之间有 gap。
- 建议：明确区分"理论贡献"（pumping lemma proof for unbounded case）和"工程贡献"（exponential DFA for finite case），避免将两者混为一个统一的不可能性论证。

**W2** [Major] Scale-dependent layer interaction 缺乏因果解释

- 具体位置：§3 "Empirical Observation"; §5.1 Table 1 vs. §5 "70B-class validation"
- 问题：8B semantic-only 仅 24% DR reduction，70B semantic-only 达 84%。这是一个重要发现，但论文仅称其为"empirical observation"，未提供因果解释。可能的假设包括：(a) 70B 模型的 vocabulary logit distribution 更集中于合法类型，使 semantic masking 更有效；(b) 70B 模型的 relation 名称生成更准确，减少了 grammar layer 对 vocabulary enforcement 的需求；(c) 模型容量影响 first-seen registration 准确率。论文在 Appendix C（Fallback Causal Tracing）提供了一些线索（Llama-3.1-8B 触发 5,882 fallbacks vs. Qwen 0 fallbacks），但未将此与 scale-dependent observation 联系起来。
- 建议：分析 8B vs. 70B 在 semantic-only 模式下的 fallback 频率差异，提供 scale-dependent interaction 的机制解释。

**W3** [Major] Fine-tuning 仅验证 LoRA，composability claim 的泛化性不足

- 具体位置：§5.1 "Composability with fine-tuning"; Table 2; Limitations §1
- 问题：Fine-tuning composability 是论文的核心卖点之一（Introduction bullet 3），但仅在 LoRA 上验证。Appendix L 提到 full fine-tuning "confirms constraints remain effective (DR→0%)"但这是单个配置（2 × 8B）的结果。QLoRA、prefix tuning、adapters 等其他 PEFT 方法未涉及。不同 fine-tuning 方法对 logit distribution 的影响不同，可能改变 grammar-semantic interaction。
- Limitations 中承认了这一点（"Evaluation is limited to one fine-tuning method (LoRA)"），但 Introduction 中的 composability claim 未加限定。
- 建议：在 Introduction 和 Abstract 中限定 composability claim 为"demonstrated with LoRA fine-tuning"，或追加 1-2 种 PEFT 方法的验证。

**W4** [Major] S1 vs. S2 对比缺乏深入分析

- 具体位置：§3.4; Table 1 (S1 R-F1 8.36 vs. S2 R-F1 8.03)
- 问题：S2（two-pass）在 R-F1 上低于 S1（single-pass），但在 CF 上更优（8.03% vs. 9.90%）。论文简单声明"S1 achieves higher R-F1 at comparable DR (§5.1) and is the primary configuration"，但未分析 S2 的 R-F1 下降原因。可能的因素：(a) two-pass 的 error propagation（第一 pass 遗漏的实体在第二 pass 中不可恢复）；(b) input-dependent grammar 的 over-constraint；(c) 额外的 inference pass 引入的 sampling noise。在 zero-shot 8.36 vs. 8.03 的水平上，0.33pp 差异是否显著？论文未报告 S1 vs. S2 的 bootstrap CI。
- 建议：提供 S1 vs. S2 的 paired bootstrap test；分析 S2 失败 case 以确定 R-F1 下降的来源。

**W5** [Major] WikiEvents pilot（n=20）对论文贡献有限

- 具体位置：§5.2; Table in Appendix Q
- 问题：20 个文档的 pilot，MDE≈±5.0pp，本身承认 statistical power 不足。这个结果既不能证明 OntoCoDec 在 event extraction 上有效，也不能证明无效。论文将其定位为"preliminary pilot"是诚实的，但它占用了正文空间（§5.2）且给人一种凑实验的印象。
- 建议：将 WikiEvents 移至 Appendix，或在正文中仅用一句话提及。释放的空间可用于更深入地分析 S1 vs. S2 或 scale-dependent interaction。

**W6** [Minor] Baseline 缺少与 training-time constraint enforcement 方法的直接对比

- 具体位置：§5; §6 Related Work
- 问题：论文的主要 baseline 是内部消融（unconstrained, grammar-only, semantic-only）和 grammar-constrained decoding 等价物（GCD-equiv via vLLM）。GoLLIE 对比仅在 WikiEvents pilot 上进行（Appendix S, n=20, 5 predicted relations）。论文在 §6 和 §7 讨论了 training-time 方法（GoLLIE, KnowCoder, REBEL, UIE）是"complementary rather than competing"，这个定位合理，但缺少任何直接的 apples-to-apples 对比使读者难以判断 OntoCoDec 相对于 training-time enforcement 的实际优势。
- 建议：至少在一个主数据集（如 SciERC）上与 GoLLIE 或 KnowCoder 的公开结果进行 violation rate 对比（即使 F1 不可直接比较，violation rate 是 task-agnostic 的）。

---

## 小问题（不影响接收）

- §3 "Constraint decidability taxonomy" 使用 `\paragraph` 标签 `\label{sec:decidability}` 但这在 LaTeX 中可能不可靠引用，建议改为 subsection 或在相邻 section 中引用。
- Table 1 信息密度很高（9 列），建议考虑将 violation rates 和 F1 分成两个 sub-table 或使用更大的字号。
- §3 "Engineering applicability": "$6^{17} \approx 1.6 \times 10^{13}$" 应更精确地说明这是针对 SciERC 的 worst-case 估计（median 17 entities），实际单文档可能更少。
- Appendix O 的 proof 中 Case 1 的论证可以更精确：pumping τ_B tokens shifts τ_A 的位置，但需要明确 relation reference 是 positional（proof 中假设）而非 name-based（实际系统），这个区分在后续段落中有讨论但 proof 本体中不够清晰。
- "near-complete DR elimination"（Abstract）在 zero-shot greedy 下 DR=0.93% 时基本成立，但 fine-tuning 后 DR≤0.09% 才真正接近 complete——建议区分两种设置下的 claim 强度。

---

## Questions for Authors

**Q1.** Schema coverage gaps 占 fine-tuning residual DR 的 33%（§Limitations）。当 training data 的 type pair 分布不覆盖所有合法 ontology pair 时，系统会 over-restrict。能否量化 SciERC 和 DocRED 的 schema 对 ground truth ontology 的覆盖率？是否考虑过基于 ontology hierarchy（而非 observed pairs）构建 constraint？

**Q2.** Entity registry 的 first-seen semantics（§3.3）在长文档中的行为如何？DocRED 文档平均 19 entities，但 outlier 文档的 entity 数可达多少？registry 的 O(|entities| × |types|) 复杂度在 100+ entities 时是否有实测性能数据？

**Q3.** Continuation masking（§3.3 "Tokenizer-agnostic type masking"）对 morphologically similar types（如 Protein vs. Protein_Complex，Limitations 中提及）的实际失败率是多少？Appendix K 是否有相关数据？

**Q4.** Table 6 报告 DRΔ 的 bootstrap CI（例如 Qwen3-8B SciERC: −1.95 to −1.11, CI [−2.57, −1.11]），但 R-F1 的 CI 很宽（如 [−1.07, −0.64]），可能导致 R-F1 变化不显著。在 R-F1 本身就很低的 zero-shot 设置中（8-13%），violation reduction 的实际下游价值如何量化？

---

## Missing References

- Ning et al., 2025. "Type-Aware Constrained Generation for Biomedical NER" (如存在)——检查 biomedical IE 中是否有类似的 type-constrained decoding 工作。
- 论文引用看起来完整，覆盖了 constrained decoding（XGrammar, GCD, Outlines, SGLang, BoostCD）和 IE（SciERC, DocRED, REBEL, UIE, GoLLIE, KnowCoder）的主要工作。

---

## 总体评分

**Overall**: 3.5 — Borderline Conference

**一句话总结**: 技术实现扎实、消融设计优秀的约束解码框架，但理论贡献偏 formalize known intuition，κ-DR 相关性无统计效力，且 DR→CF trade-off 被低估，综合来看处于 Conference/Findings 边界。

**详细判断依据**: 论文解决了一个真实且重要的问题（LLM-based IE 中 15-18% 的本体违规率），提出了一个 clean 的两层架构，配有正确的理论证明和全面的消融实验。统计方法（bootstrap CI, Bonferroni correction, Cohen's d）在 NLP 论文中罕见且值得肯定。31 页 Appendix 回答了大量预期问题。然而，核心理论贡献（Proposition 1）本质上是将已知直觉形式化，而非新发现；κ-DR correlation（n=3, p=0.138）不应以相关性的形式呈现；CF trade-off 使 zero-shot greedy 下的 total violation 仅降低 30%，削弱了实用性论述；fine-tuning 仅验证 LoRA；WikiEvents pilot 统计效力不足。若 N1（κ overclaiming）和 N2（CF trade-off 诚实呈现）能在 revision 中解决，评分可升至 4.0。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2504 · 2026-05-23T10:34:58.904047+00:00_

Reviewer 1 的审稿意见已收到。等待 Reviewer 2 完成审稿后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 182

## Round 182

2 recorded events


### User

_source line 2505 · 2026-05-23T10:35:01.491150+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：我给出 **Overall 3.5（Borderline Conference）**，Soundness 3.5，Excitement 3，Reproducibility 4，Confidence 4。

两个 Critical 问题：
1. **κ-DR 相关性（n=3）** 无统计效力但被赋予过高叙事地位
2. **CF trade-off 被低估**——zero-shot greedy 下 total violation 仅降 30%（DR↓94% 但 CF 从 0.08%→9.90%）

四个 Major 问题：Proposition 1 偏 formalize known intuition、scale-dependent interaction 缺因果解释、fine-tuning 仅验 LoRA、S1 vs S2 对比深度不足。

主要优势：消融设计优秀（5-way + bootstrap CI + Bonferroni）、cross-model 验证充分、31 页 appendix 极其详尽。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2506 · 2026-05-23T10:35:16.811809+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成审稿后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 183

## Round 183

6 recorded events


### User

_source line 2507 · 2026-05-23T10:38:24.641960+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

审查侧重：新颖性 + 完整性 + 写作质量 + 格式合规 + 遗漏相关工作

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 论文针对 grammar-constrained decoding 无法执行 IE 类型约束这一真实缺陷提出了干净的形式化和实用的两层架构，评估异常扎实，但核心技术新颖性中等，若干关键实验证据不足以支撑其 contribution claim 的广度。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 技术方法正确，Proposition 1 证明完整，ablation 设计严谨；但个别实验证据（WikiEvents n=20, n=3 tightness 相关性）偏弱 |
| Excitement | 3/5 | 问题重要且实用，但核心方案（stateful logit processor + entity registry）概念上是现有 constrained decoding 的自然延伸，增量性偏强 |
| Reproducibility | 4/5 | 实验细节充分（exp_id、超参、数据集配置均有文档），代码承诺 acceptance 后释放；70B 实验需要 AWQ INT4 量化，可能有硬件门槛 |
| Confidence | 4/5 | 本人熟悉 constrained decoding 和 IE 文献，仔细阅读了全文及关键附录 |

---

## Summary

OntoCoDec 提出将 IE 本体编译为两层 token 级解码约束的框架：grammar layer 通过 XGrammar 保证结构有效性和词汇约束，semantic layer 通过运行时 entity registry + dynamic logit masking 保证 domain/range 类型约束。核心理论贡献是 Proposition 1（domain/range 约束超出 CFG 表达能力），核心实践贡献是跨三个模型族、两个 RE 数据集的系统性 ablation 证实 DR 违规几乎完全消除（≤0.09%），以及 DR↔CF trade-off 的清晰分析。评估覆盖零样本、LoRA 微调、beam search、70B 尺度验证和 WikiEvents event extraction pilot。

---

## 主要优势

**S1.** 问题定义精准且有实际意义。论文清晰识别了 grammar-constrained decoding（XGrammar/Outlines/SGLang）的能力边界——无法执行跨字段的 domain/range 类型约束——并给出了形式化论证（Proposition 1, §3）。constraint decidability taxonomy（Level 1/2/3）是一个有用的概念框架。

**S2.** 实验设计极为扎实——这是本文最大亮点。五路 ablation（Table 1: unconstrained → grammar → GCD-equiv → semantic → S1/S2）清晰解剖了每个 layer 的独立与交互贡献。Cross-model 验证（Qwen3-8B, Llama-3.1-8B, Mistral-7B × SciERC/DocRED）、fine-tuning composability（Table 2, Bonferroni-corrected CIs）、beam search sweep（k∈{1,2,4,8}）、downstream impact 分析（仅 0.49% blocked triples match gold labels）均展现了罕见的实验严谨性。grammar-only 行实际复现了 GCD/BoostCD 的结果（Table 1 row 2），构成了内建的 baseline 比较。

**S3.** 对 limitations 的诚实和透明度异常高。论文主动报告了：CF 作为 trade-off（而非隐藏）、n=3 tightness 相关性的 p=0.138（不显著）、WikiEvents n=20 的 MDE≈±5.0pp、70B 验证为单一模型族、GoLLIE 比较的方法论局限。三段式 Limitations section 覆盖了 constraint scope / evaluation coverage / engineering considerations，内容充实。这种自我批评的态度显著提高了论文的可信度。

**S4.** 工程设计考虑周全。tokenizer-agnostic type masking（跨 byte-level BPE 和 SentencePiece，处理 SEN/SID/SIDE 等前缀共享类型）、grammar-first fallback 策略（保证 JSON 结构完整性优先于类型约束）、pair-based sequential enforcement（比独立 domain/range 检查严格 33-37%，§4 non-rectangularity analysis）均体现了从理论到工程的细致打磨。

**S5.** 写作质量高。8 页正文在高信息密度下保持了良好的逻辑流；符号使用一致（DR/RV/ET/CF 在 §5 定义后始终如一）；图表设计紧凑且信息量大；Related Work 的三轴组织（constrained decoding / schema-aware IE / constraint enforcement in IE）清晰有效。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] WikiEvents n=20 作为 "task generalization" 证据严重不足，但被列为 contribution

- 具体位置：§1 Contribution 2 ("a preliminary n=20 event extraction pilot provides directional evidence of task generalization")、§5.2、Appendix WikiEvents Pilot (Table 47)
- 问题：WikiEvents fine-tuning 评估仅用 20 篇文档（官方 test split），MDE≈±5.0pp，论文自身承认统计能力不足以检测小 F1 差异。但 Contribution 2 仍将 "directional evidence of task generalization" 列为贡献的一部分。n=20 的 pilot 在 peer review 中不构成 generalization 证据——这是 feasibility demonstration 而非 validation。零样本 WikiEvents 评估（Table 47, n=246 docs）本身验证了词汇约束消除（EV, RoV→0%），有意义；但 fine-tuning composability 的 n=20 无法支撑任何有置信度的结论。Trigger F1 shifts 有 -5.4/-0.6pp 的宽 CI，进一步说明统计功效不足。
- 为什么影响接收：如果论文声称 task generalization 但证据不足，审稿人有理由质疑 contribution 声明的准确性。这不是不可修复的问题，但需要调整 framing。
- 建议修改方向：(1) 将 Contribution 2 中的 WikiEvents 部分降级为 "preliminary feasibility check"，不列入正式 contribution；(2) 或在完整数据集上做正式评估；(3) 至少在 Contribution 声明中加入显式 caveat。

**N2** [critical] GoLLIE 比较存在严重方法论缺陷，但被用于定位论文的差异化

- 具体位置：§6 Related Work ("GoLLIE-7B achieves zero DR under zero-shot evaluation, but at the cost of near-complete output suppression (5 predicted relations vs. >1,100...)")、Appendix GoLLIE Comparison (Table)
- 问题：Appendix 中 GoLLIE-7B 比较将零样本 GoLLIE-7B vs. LoRA+S1 微调的 OntoCoDec 进行对比（Table caption 注明了这一差异）。结论是 GoLLIE "通过近乎完全的输出抑制实现形式正确性"（5 predicted relations vs. >1,100）。但这不是公平比较：GoLLIE 未经微调自然输出少，OntoCoDec 经过 LoRA 微调自然输出多。微调本身就会增加输出量，这一混淆变量未被控制。§6 主文引用此附录结果来定位与 GoLLIE 的差异（"near-complete output suppression"），但读者可能不会仔细检查附录中的实验条件不对等。公平比较应为：(a) 两者均零样本，或 (b) 两者均微调。
- 为什么影响接收：GoLLIE 是论文最直接的 schema-aware IE baseline。当前比较可能被解读为 cherry-picking 对己方有利的设置。如果 GoLLIE fine-tuned 后输出量正常化但仍保持低 DR，则 OntoCoDec 的差异化叙事需要重新调整。
- 建议修改方向：(1) 添加 GoLLIE-7B 零样本 vs. OntoCoDec 零样本的同等条件比较；(2) 如果 GoLLIE 微调评估不可行（evaluation protocol 不兼容），在正文 §6 中明确说明不可比的原因（而非仅在附录 caption 注明），并删除 "near-complete output suppression" 的结论性表述或添加条件限定。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] Proposition 1 的新颖性被高估——这是 well-known fact 的领域应用

- 具体位置：§3 Method、§1 Contribution 1
- 问题：Proposition 1 声称 domain/range type constraints 超出 CFG 表达能力。但 PDA 无法执行 random-access stack lookup 是形式语言理论的基本知识（cross-serial dependencies, copy languages 等），并非新发现。论文在 Contribution 1 中诚实地称之为 "formalizing a known intuition for the IE setting"，但同时将其列为第一大贡献，且在 §3 中用相当大的篇幅展开（proof sketch + engineering applicability + empirical observation）。Appendix O 的 pumping lemma 证明正确但不深刻——本质上构造了一个 copy-language 变体。
- 建议：降低 Proposition 1 的展示权重。它作为 motivating observation 是充分的，但不应占据 contribution 列表的首位。将重点移至两层架构的工程设计和实证发现。

**W2** [major] 70B 验证仅限单一模型族，但 Contribution 3 标题为 "scale validation"

- 具体位置：§1 Contribution 3 ("Single-family scale validation on Llama-3.1-70B")、§5 (70B-class validation)
- 问题：所有 70B 实验均使用 Llama-3.1-70B-Instruct AWQ INT4 量化。论文在正文中标注了 "single-family" 和 "cross-family verification remains future work"，这些 caveats 诚实。但 scale-dependent layer interaction（semantic-only 在 70B 达 84% DR reduction vs. 8B 的 24%）是否为 Llama-specific 现象？量化影响已通过 8B ablation 排除（Appendix quantization），但模型族影响未验证。
- 建议：Contribution 3 应更准确地标注为 "preliminary single-family scale observation"，并在 Discussion 中明确讨论 cross-family verification 的必要性。

**W3** [major] DR↔CF trade-off 在零样本场景下的严重程度讨论不足

- 具体位置：§5.1 Cross-field violation analysis、§7 Discussion
- 问题：论文将 DR→CF 转换定位为 "severity downgrade"（DR 不可恢复 vs. CF 可 post-hoc 解决），这是合理的框架。但零样本下 CF 从 0.08% 升至 9.90%（Table 1, S1 row），是 substantial 的新错误引入。TCR 消除 18-92% CF（Appendix TCR），但范围极宽，最低仅 18%。论文声称零样本是一大应用场景（无需 fine-tuning），但在该场景下 ~10% CF 率的实际影响未充分讨论。
- 建议：在 Discussion 中添加对零样本 CF 率实际影响的分析（例如 CF violations 在下游 KG 中导致多少实际矛盾？）。

**W4** [minor] constraint tightness 分析（n=3, p=0.138）在正文中占据过多空间

- 具体位置：§4 Constraint Composition (Constraint Tightness paragraph)
- 问题：κ̄ 与 DR reduction 的关系基于 n=3 个 schema（WikiEvents 0.029, SciERC 0.333, DocRED 0.842），p=0.138 不显著。论文正确标注为 "descriptive"，但在正文 §4 中用了整段讨论。n=3 的描述性观察不适合作为正文的 highlighted finding。
- 建议：压缩至 1-2 句话，将详细讨论移至附录。

---

## 小问题（不影响接收）

- **M1** Abstract 声称 "F1 41-47%"，但 Table 2 中 Qwen DocRED S1 的 R-F1 为 40.79%。40.79 严格来说低于 41%。建议改为 "R-F1 40-47%" 或保留 "41-47%" 但添加 rounding 说明。

- **M2** CRANE (Banerjee et al., 2025) 仅在 Appendix B 讨论，未在主文 §6 Related Work 提及。CRANE 关于 constrained decoding 抑制 reasoning 的理论分析与 S2 在 70B 下 R-F1 降低 8.45pp 的现象直接相关（S2 的 over-constraining 可能正是 CRANE 所分析的问题），值得在主文中至少引用。

- **M3** DocRED 使用 development set（因 test annotations 不公开）的说明仅在 §5 的 footnote 1 中，建议在 Setup 段落正文中显著说明。

- **M4** Figure 1 的 "Token Masking" 部分展示了 mask 计算流程，但缺少一个具体端到端示例（某个 type-bearing position 的实际 logit masking 过程），一个 running example 会提升可读性。

- **M5** §3.1 中 "100% preservation across all configurations" 表述不清——建议改为 "grammar guarantees entity-before-relation ordering in all configurations"。

- **M6** §2 中 empirical constraints 的 99.0-99.4% coverage 意味着 0.6-1.0% valid type pairs 未覆盖（由 grammar-first fallback 处理）。对 open-domain 或 schema evolution 场景的影响未在 Limitations 中讨论。

---

## Missing References 检查

论文对关键相关工作的覆盖充分：
- CRANE (Banerjee et al., 2025) ✓ 已引用（Appendix B 详细讨论，建议主文提及）
- EnriCo (Zaratiana et al., 2024) ✓ 已引用（§6 + Appendix B）
- IterGen (Ugare et al., 2025) ✓ 已引用（§6）
- SynCode, XGrammar, Outlines, SGLang, PICARD, KG-Trie ✓ 均已引用
- GoLLIE, KnowCoder, GCD, BoostCD ✓ 均已引用
- 未发现重大遗漏。

---

## 格式合规性检查（EMNLP 2026 / ACL 格式）

- **正文页数**：8 页（§1-§7 在 pages 1-8 内），Limitations 以 \clearpage 起始于 page 9 ✓
- **匿名处理**：\author{Anonymous ACL submission}，未发现代码/数据链接泄露身份，Ethics Statement 中 "Code and data will be released upon acceptance" 合规 ✓
- **Limitations section**：存在，三段覆盖 constraint scope / evaluation coverage / engineering considerations ✓ 内容充分
- **Ethics statement**：存在 ✓
- **References 格式**：ACL natbib 格式 ✓
- **\usepackage[review]{acl}**：启用了 review 模式（行号 + 匿名 footer）✓

---

## Questions for Authors

**Q1.** Proposition 1 是否已在其他文献中以类似形式出现过？如果是，本文的形式化有何增量？请指出与已有 cross-serial dependency 不可由 CFG 表达的结论的本质区别。

**Q2.** GoLLIE-7B 在 LoRA fine-tuning 后的 SciERC 表现如何？如果 GoLLIE fine-tuned 后输出量正常化但仍保持低 DR，则 OntoCoDec 的差异化需要重新评估。

**Q3.** Scale-dependent layer interaction（semantic-only 在 70B 达 84% vs. 8B 的 24%）是否有理论预期支持？例如，70B 模型更好的 vocabulary calibration 是否解释了 semantic layer 的独立有效性？

**Q4.** 在零样本部署场景下，~10% CF rate 对下游 KG construction 的实际影响有多大？论文是否有对 CF violations 导致的 KG 矛盾数量的分析？

---

## Overall Assessment 总结

**Overall: 3.5 (Borderline Conference)** | **Confidence: 4/5**

本文解决了一个有实际意义的问题，提出了干净的形式化和实用的两层架构，实验设计和执行质量在同类论文中属上乘。最大优势在于评估的深度和 limitations 的透明度。

主要不足：(1) 核心技术新颖性中等——entity registry + dynamic masking 是 stateful logit processor 的自然应用，Proposition 1 是已知结论在 IE 场景的直接应用；(2) 关键实验证据有缺口——WikiEvents n=20 不足以支撑 task generalization claim，GoLLIE 比较方法论不公平，70B 验证为单一模型族；(3) 零样本场景下 DR→CF trade-off 的实际影响讨论不足。

论文质量足以被 Findings 接收。是否能进入主会议取决于对"扎实的工程+实验贡献 vs. 有限的概念新颖性"的权衡。若修复 N1（WikiEvents framing）和 N2（GoLLIE 比较公平性），评分有望上调至 3.5-4.0 区间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2508 · 2026-05-23T10:38:58.327447+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿意见\n\n### Overall: 3.5 (Borderline Conference) | Soundness 3.5 | Excitement 3 | Reproducibility 4 | Confidence 4\n\n### Must-Fix 问题\n\n**N1** [Critical] κ-DR 相关性（n=3）统计上无意义，但被赋予过高叙事地位\n- §4 \"Constraint Tightness\" 段落中，κ̄ 与 DR reduction 的相关性仅基于 3 个数据点（WikiEvents κ̄=0.029, SciERC κ̄=0.333, DocRED κ̄=0.842），p=0.138。虽标注 \"descriptive\"，但在正文中配有定义式、Appendix 中有独立 case study 和 Figure 3，叙事比重暗示 κ 有解释力。n=3 时任意单调点都能产生类似相关性。且论文承认 \"entity type confusability is a critical co-factor\"，意味着 κ 是 confounded variable。\n\n**N2** [Critical] CF 作为结构性 trade-off 被低估——zero-shot greedy 下 CF rate 9.90% 是严重实用性问题\n- DR 从 15.37%→0.93%（↓94%），但 CF 从 0.08%→9.90%。Total violation（DR+CF）从 15.45% 降至 10.83%，仅降 30%。论文将 DR→CF 称为 \"severity downgrade\" 但论证不充分。Abstract 选择性报告 DR reduction 而忽略 CF increase 可能误导读者。\n\n### Should-Fix 问题\n\n**W1** [Major] Proposition 1 的实际价值：formalizing known intuition vs. genuine theoretical contribution\n**W2** [Major] Scale-dependent layer interaction 缺乏因果解释（8B semantic-only 24% vs. 70B 84%）\n**W3** [Major] Fine-tuning 仅验证 LoRA，composability claim 泛化性不足\n**W4** [Major] S1 vs. S2 对比缺乏深入分析（R-F1 差异是否显著？S2 失败 case 分析？）\n**W5** [Major] WikiEvents pilot（n=20）对论文贡献有限\n**W6** [Minor] Baseline 缺少与 training-time constraint enforcement 方法的直接对比\n\n---\n\n请逐条回应上述 N1、N2、W1-W6。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿意见\n\n### Overall: 3.5 (Borderline Conference) | Soundness 3.5 | Excitement 3 | Reproducibility 4 | Confidence 4\n\n### Must-Fix 问题\n\n**N1** [Critical] κ-DR 相关性（n=3）统计上无意义，但被赋予过高叙事地位\n- §4 \"Constraint Tightness\" 段落中，κ̄ 与 DR reduction 的相关性仅基于 3 个数据点（WikiEvents κ̄=0.029, SciERC κ̄=0.333, DocRED κ̄=0.842），p=0.138。虽标注 \"descriptive\"，但在正文中配有定义式、Appendix 中有独立 case study 和 Figure 3，叙事比重暗示 κ 有解释力。n=3 时任意单调点都能产生类似相关性。且论文承认 \"entity type confusability is a critical co-factor\"，意味着 κ 是 confounded variable。\n\n**N2** [Critical] CF 作为结构性 trade-off 被低估——zero-shot greedy 下 CF rate 9.90% 是严重实用性问题\n- DR 从 15.37%→0.93%（↓94%），但 CF 从 0.08%→9.90%。Total violation（DR+CF）从 15.45% 降至 10.83%，仅降 30%。论文将 DR→CF 称为 \"severity downgrade\" 但论证不充分。Abstract 选择性报告 DR reduction 而忽略 CF increase 可能误导读者。\n\n### Should-Fix 问题\n\n**W1** [Major] Proposition 1 的实际价值：formalizing known intuition vs. genuine theoretical contribution\n**W2** [Major] Scale-dependent layer interaction 缺乏因果解释（8B semantic-only 24% vs. 70B 84%）\n**W3** [Major] Fine-tuning 仅验证 LoRA，composability claim 泛化性不足\n**W4** [Major] S1 vs. S2 对比缺乏深入分析（R-F1 差异是否显著？S2 失败 case 分析？）\n**W5** [Major] WikiEvents pilot（n=20）对论文贡献有限\n**W6** [Minor] Baseline 缺少与 training-time constraint enforcement 方法的直接对比\n\n---\n\n请逐条回应上述 N1、N2、W1-W6。"
  }
}
```

</details>

---


### Tool result

_source line 2509 · 2026-05-23T10:39:16.036050+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17708
}
```

</details>

---


### Tool call

_source line 2510 · 2026-05-23T10:39:16.086713+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿意见\n\n### Overall: 3.5 (Borderline Conference) | Soundness 4 | Excitement 3 | Reproducibility 4 | Confidence 4\n\n### Must-Fix 问题\n\n**N1** [Critical] WikiEvents n=20 作为 \"task generalization\" 证据严重不足，但被列为 contribution\n- §1 Contribution 2 将 \"directional evidence of task generalization\" 列为贡献的一部分。n=20 的 pilot 不构成 generalization 证据，是 feasibility demonstration 而非 validation。\n\n**N2** [Critical] GoLLIE 比较存在严重方法论缺陷，但被用于定位论文差异化\n- Appendix 中 GoLLIE-7B 比较将零样本 GoLLIE-7B vs. LoRA+S1 微调的 OntoCoDec 进行对比。§6 引用此结论（\"near-complete output suppression\"）来定位差异化，但实验条件不对等。公平比较应为两者均零样本或两者均微调。\n\n### Should-Fix 问题\n\n**W1** [Major] Proposition 1 的新颖性被高估——这是 well-known fact 的领域应用\n**W2** [Major] 70B 验证仅限单一模型族，但 Contribution 3 标题为 \"scale validation\"\n**W3** [Major] DR↔CF trade-off 在零样本场景下的严重程度讨论不足\n**W4** [Minor] constraint tightness 分析（n=3, p=0.138）在正文中占据过多空间\n\n### 小问题\n\n**M1** Abstract \"F1 41-47%\" 但 Table 2 Qwen DocRED S1 R-F1=40.79，低于 41%\n**M2** CRANE (Banerjee et al., 2025) 仅在 Appendix B 讨论，S2 在 70B 下 R-F1 降低 8.45pp 与 CRANE 关于 constrained decoding 抑制 reasoning 的分析直接相关\n**M3** DocRED 使用 dev set 的说明仅在 footnote 1，应更显著\n**M4** Figure 1 缺少端到端 running example\n**M5** §3.1 \"100% preservation across all configurations\" 表述不清\n**M6** empirical constraints 0.6-1.0% 未覆盖 valid type pairs 对 schema evolution 的影响未讨论\n\n---\n\n请逐条回应上述 N1、N2、W1-W4、M1-M6。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿意见\n\n### Overall: 3.5 (Borderline Conference) | Soundness 4 | Excitement 3 | Reproducibility 4 | Confidence 4\n\n### Must-Fix 问题\n\n**N1** [Critical] WikiEvents n=20 作为 \"task generalization\" 证据严重不足，但被列为 contribution\n- §1 Contribution 2 将 \"directional evidence of task generalization\" 列为贡献的一部分。n=20 的 pilot 不构成 generalization 证据，是 feasibility demonstration 而非 validation。\n\n**N2** [Critical] GoLLIE 比较存在严重方法论缺陷，但被用于定位论文差异化\n- Appendix 中 GoLLIE-7B 比较将零样本 GoLLIE-7B vs. LoRA+S1 微调的 OntoCoDec 进行对比。§6 引用此结论（\"near-complete output suppression\"）来定位差异化，但实验条件不对等。公平比较应为两者均零样本或两者均微调。\n\n### Should-Fix 问题\n\n**W1** [Major] Proposition 1 的新颖性被高估——这是 well-known fact 的领域应用\n**W2** [Major] 70B 验证仅限单一模型族，但 Contribution 3 标题为 \"scale validation\"\n**W3** [Major] DR↔CF trade-off 在零样本场景下的严重程度讨论不足\n**W4** [Minor] constraint tightness 分析（n=3, p=0.138）在正文中占据过多空间\n\n### 小问题\n\n**M1** Abstract \"F1 41-47%\" 但 Table 2 Qwen DocRED S1 R-F1=40.79，低于 41%\n**M2** CRANE (Banerjee et al., 2025) 仅在 Appendix B 讨论，S2 在 70B 下 R-F1 降低 8.45pp 与 CRANE 关于 constrained decoding 抑制 reasoning 的分析直接相关\n**M3** DocRED 使用 dev set 的说明仅在 footnote 1，应更显著\n**M4** Figure 1 缺少端到端 running example\n**M5** §3.1 \"100% preservation across all configurations\" 表述不清\n**M6** empirical constraints 0.6-1.0% 未覆盖 valid type pairs 对 schema evolution 的影响未讨论\n\n---\n\n请逐条回应上述 N1、N2、W1-W4、M1-M6。"
  }
}
```

</details>

---


### Tool result

_source line 2511 · 2026-05-23T10:39:17.395885+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1309
}
```

</details>

---


### Assistant

_source line 2512 · 2026-05-23T10:39:21.003924+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 184

## Round 184

2 recorded events


### User

_source line 2513 · 2026-05-23T10:39:23.543078+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**评分摘要**：Overall 3.5 (Borderline Conference)，Soundness 4/5，Excitement 3/5，Confidence 4/5。

**核心判断**：论文实验设计和执行质量上乘（五路 ablation、跨模型验证、beam sweep、downstream impact 分析），limitations 的透明度也罕见地高。但核心新颖性中等（entity registry + dynamic masking 是自然延伸，Proposition 1 是已知结论的 IE 应用），且两个关键实验证据有缺陷需修复：

- **N1**：WikiEvents n=20 不足以支撑 "task generalization" contribution claim
- **N2**：GoLLIE 比较将零样本 GoLLIE vs. 微调 OntoCoDec 对比，方法论不公平

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2514 · 2026-05-23T10:39:30.254214+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 185

## Round 185

2 recorded events


### User

_source line 2515 · 2026-05-23T10:41:49.105098+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### N1: κ-DR 相关性（n=3）统计上无意义，但被赋予过高叙事地位

**[AGREE] R1-N1**: 同意这一关切，我在自己的审稿中也提出了类似问题（我的 W4）。

n=3 的描述性观察确实不具有统计推断价值，R1 指出 "任意单调点都能产生类似相关性" 是准确的。论文在 §4 中给出了 κ(r) 的正式定义、schema mean κ̄ 的计算，并在 Appendix 中有独立 case study（Appendix κ-case-study）和分析，叙事权重确实与 n=3 的证据强度不匹配。

R1 补充指出 κ 是 confounded variable（entity type confusability 是 co-factor），这一点论文自身也承认（§4: "entity type confusability is a critical co-factor"），进一步削弱了 κ 的独立解释力。

但我认为严重程度上 R1 给了 [Critical] 可能略高。论文确实标注了 "descriptive (n=3, p=0.138)"，且未在 Contribution 列表中声称 κ 为贡献。修复方式是压缩 §4 中的篇幅（从一段缩减为 1-2 句），将详细分析移至附录，而非删除 κ 指标本身——该指标作为描述性工具仍有概念价值。**建议严重程度：Major 而非 Critical。**

---

### N2: CF 作为结构性 trade-off 被低估——zero-shot greedy 下 CF rate 9.90%

**[AGREE] R1-N2（部分同意，部分补充）**: 我在自己的审稿中提出了相关问题（我的 W3），但 R1 的数据分析比我的更尖锐。

R1 的核心计算是准确的：Table 1 中 unconstrained Tot=15.45%（DR 15.37% + CF 0.08%）→ S1 Tot=10.83%（DR 0.93% + CF 9.90%），total violation 仅降 30%。这确实是一个重要视角。

但我需要补充几点 R1 未充分考虑的信息：

1. **Abstract 并未完全隐瞒 CF**。Abstract 第三段明确写道："In zero-shot settings, cross-field rates are higher (up to 12%) but decrease with model calibration." 虽然没有给出起始点（从 ~0%），但提及了 zero-shot CF 可高达 12%。

2. **DR 和 CF 的质性差异是真实的**。论文在 §7 论述："DR is irrecoverable, while CF is amenable to post-hoc resolution (TCR eliminates 18-92%)"。DR 违规意味着三元组的类型对在本体中根本不存在（如 Task→Used-for→Material），这类错误在 KG 中不可修复。CF 违规则是同一实体在不同三元组中被赋予不同但各自有效的类型（如 "ResNet" 既为 Method 又为 OtherScientificTerm），可通过 post-hoc type consensus 解决。将两者简单相加为 "total violation" 忽略了这一质性差异。

3. **论文的主要推荐配置是 fine-tuned + beam**（§5: beam k=2 Pareto-optimal, k=4 eliminates all），在该配置下 CF≤0.11%。Zero-shot greedy 更多是 diagnostic probe（§5 开头明确说明），不是主要部署建议。

**但 R1 的核心批评仍然成立**：论文在 Abstract 中突出报告 DR reduction（"near-eliminates domain/range violations (<0.1%)"）而将 CF increase 放在后文，在叙事上确实存在不平衡。建议修改 Abstract 使 DR↔CF trade-off 的 framing 更加对称，特别是在 zero-shot 场景下。

**总结**：同意 R1 的关切方向，但严重程度应为 Major 而非 Critical，原因是：(a) Abstract 确实提及了 zero-shot CF；(b) DR 和 CF 的质性差异是真实的；(c) 主要推荐配置（fine-tuned + beam）下 trade-off 很小。

---

### W1: Proposition 1 的实际价值

**[AGREE] R1-W1**: 完全同意。我在自己的审稿中将此列为 W1 [Major]，与 R1 的评估一致。

PDA 无法执行 random-access stack lookup 是形式语言理论的基本知识。论文诚实地称之为 "formalizing a known intuition"（§1 Contribution 1），但仍将其列为三大贡献之首，且在 §3 中投入了大量篇幅（proof sketch + engineering applicability analysis + empirical observation）。Appendix O 的 pumping lemma 证明构造了一个 copy-language 变体，技术上正确但不深刻。

Engineering applicability 段落（DFA states ≈ 6^17 ≈ 1.6×10^13 for SciERC）是有价值的补充——它说明即使 finite case 理论上 regular，实际构造也不可行。但这仍然是 well-known 的 state explosion 问题在具体场景的实例化。

两位 reviewer 对此问题的一致判断应当给予作者修改的明确信号。

---

### W2: Scale-dependent layer interaction 缺乏因果解释

**[AGREE] R1-W2**: 同意这是一个 gap，我在 Questions for Authors 中也提出了类似问题（Q3）。

论文报告了一个有趣的经验观察（semantic-only 在 8B 只达 24% DR reduction vs. 70B 达 84%），但未提供因果解释。R1 要求因果解释是合理的——至少应讨论候选假设。可能的解释包括：

1. 70B 模型更好的 vocabulary calibration → 即使不强制词汇约束，也更倾向于生成有效关系类型 → semantic layer 的类型 masking 更有效
2. 70B 模型的 logit distribution 更 peaked → semantic masking 更少与 grammar masking 冲突 → 更少触发 grammar-first fallback

论文在 §3 标注为 "Empirical Observation" 并在 §7 仅说 "suggests grammar-constrained decoding is necessary but increasingly insufficient as models improve"，这个归纳是合理但浅层的。

不过我注意到，要求严格的因果解释可能对论文的篇幅和实验成本要求过高。至少应添加 1-2 句关于可能机制的讨论（例如检查 70B 下 fallback 触发率是否显著低于 8B，这在现有实验数据中应该可以获得）。

---

### W3: Fine-tuning 仅验证 LoRA，composability claim 泛化性不足

**[REBUT] R1-W3**: 部分不同意。

1. **Full fine-tuning 已在附录验证**。Limitations §3 明确写道："Full fine-tuning confirms constraints remain effective (DR→0%; Appendix full-ft)"。虽然只在 Appendix 中报告，但这意味着 composability 不限于 LoRA——至少 LoRA 和 full fine-tuning 两种方法都已验证。

2. **论文的 claim 是关于 constraint enforcement 与 fine-tuning 的 composability**，而非特定于 LoRA 的 composability。核心机制（runtime logit masking）不依赖于 fine-tuning 方法——它在模型输出层面操作，对模型内部权重如何获得不可知。不同 PEFT 方法（QLoRA、adapters、prefix-tuning）改变的是模型权重，不改变输出 logits 的生成方式，因此 composability 在机制上是有保证的。

3. 但我同意 R1 的关切有一定道理：不同 fine-tuning 方法可能产生不同的 violation rate distribution（例如 QLoRA 的量化可能影响 logit precision），从而影响 enforcement 的实际效果。**论文应在 Limitations 中将此作为 caveat 说明**（目前 Limitations 仅提到 "other fine-tuning methods warrant further investigation"，措辞偏弱）。

**总结**：R1 的关切有道理但作为 [Major] 略重。论文已验证两种 fine-tuning 方法（LoRA + full FT），且 composability 的机制论证是成立的。建议在 Limitations 中加强 caveat 即可。

---

### W4: S1 vs. S2 对比缺乏深入分析

**[AGREE] R1-W4**: 同意 S1 vs. S2 的分析不够深入。

论文在 §3.4 定义了 S1（单遍）和 S2（两遍），在 Table 1 中给出了对比数据（SciERC 8B ZS: S1 DR=0.93% R-F1=8.36 vs. S2 DR=0.97% R-F1=8.03），并在 70B Appendix 中报告了 S2 的 R-F1 降低 8.45pp。但缺乏：

1. **S1 vs. S2 差异的统计显著性检验**——主文中未报告
2. **S2 failure case 分析**——70B 下 S2 R-F1 降低 8.45pp 的具体原因是什么？论文说 "over-constraining"，但未给出具体 case 说明哪些 constraints 是 over-constraining 的
3. **S2 何时优于 S1 的指导**——论文只说 S1 是 "primary configuration"，但未讨论在什么条件下 S2 可能更好

不过，S1 vs. S2 的分析在论文叙事中是次要的（论文明确以 S1 为主要配置），且 §3.4 已提供了设计动机。这是一个 "nice to have" 的深入分析，而非必须修复的缺陷。**建议严重程度维持 Major 但不影响接收决定。**

---

### W5: WikiEvents pilot（n=20）对论文贡献有限

**[AGREE] R1-W5**: 完全同意。我在自己的审稿中将此列为 N1 [Critical]——是我审稿意见中严重程度最高的问题之一。

WikiEvents fine-tuning 的 n=20 不足以支撑任何有置信度的结论。论文自身的 power analysis 确认 MDE≈±5.0pp，trigger F1 shifts 有宽 CI，per-document variance 高（std/mean > 0.5）。将此列入 Contribution 2 的一部分（"directional evidence of task generalization"）是 overclaim。

零样本 WikiEvents 评估（n=246 docs, Table 47）本身有价值——验证了 EV/RoV 消除和 tokenizer-agnostic design 的跨任务适用性。但 fine-tuning composability 的 n=20 只能算 feasibility check。

两位 reviewer 对此问题的一致判断应促使作者将 WikiEvents 从 Contribution 声明中降级。

---

### W6: Baseline 缺少与 training-time constraint enforcement 方法的直接对比

**[AGREE] R1-W6**: 同意，这与我的 N2（GoLLIE 比较方法论缺陷）直接相关。

论文定位为与 training-time 方法（GoLLIE, KnowCoder）正交且互补，但 Appendix GoLLIE Comparison 中的对比是不公平的：GoLLIE-7B 零样本 vs. OntoCoDec LoRA+S1 微调。这不是 controlled comparison。

R1 提出的要点与我的 N2 互相印证：缺少与 training-time constraint enforcement 方法的公平直接对比是论文的一个显著弱点。论文声称"complementary"但未通过实验验证 complementarity——例如，GoLLIE + OntoCoDec 是否优于单独的 GoLLIE 或单独的 OntoCoDec？

不过我注意到论文在 §6 中说 "direct comparison is methodologically constrained by incompatible evaluation protocols"——如果这是真的（GoLLIE 使用 code-style schema encoding，评估流程不同），则不公平不是作者故意为之，而是方法论限制。论文应更透明地解释这一限制的具体内容。

---

## 总结：两位 Reviewer 的共识与分歧

**共识问题**（两位 Reviewer 均提出）：
1. Proposition 1 新颖性有限（R1-W1, R2-W1）
2. WikiEvents n=20 证据不足（R1-W5, R2-N1）
3. CF trade-off 在零样本下的严重程度讨论不足（R1-N2, R2-W3）
4. 缺少与 GoLLIE 等 training-time 方法的公平对比（R1-W6, R2-N2）
5. κ-DR 相关性叙事权重过高（R1-N1, R2-W4）

**R1 独有关切**：
- Scale-dependent interaction 缺乏因果解释（R1-W2）——R2 在 Questions 中提出但未列为 weakness
- S1 vs. S2 分析不足（R1-W4）——R2 未提出
- LoRA-only composability（R1-W3）——R2 未提出，且 R2 认为有 partial rebuttal 基础

**R2 独有关切**：
- GoLLIE 比较的方法论不公平（R2-N2）——R1 提出了更广泛的 "缺少 training-time 对比"（R1-W6），R2 指出了具体的不公平实验设置
- 70B 单一模型族问题（R2-W2）——R1 未单独提出
- Abstract F1 range 不精确（R2-M1）——minor

**我对 R1 总体评估的看法**：R1 给出 Overall 3.5 与我一致。R1 的 Soundness 3.5 比我的 4.0 略低，主要因为 R1 对 κ 分析和 CF trade-off 赋予了更高严重程度（Critical vs. 我的 Minor/Major）。我认为 R1 的 N1（κ 分析）严重程度偏高——应为 Major 而非 Critical；R1 的 N2（CF trade-off）在数据层面分析到位，但未充分考虑 DR/CF 的质性差异和论文推荐的 fine-tuned+beam 配置。整体而言，两份审稿意见在方向上高度一致，对论文形成了清晰的修改信号。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2516 · 2026-05-23T10:41:57.101006+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 186

## Round 186

2 recorded events


### User

_source line 2517 · 2026-05-23T10:41:59.594876+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 审稿意见的逐条回应。核心结论：

- **5 个共识问题**：Proposition 1 新颖性、WikiEvents n=20、CF trade-off 讨论不足、GoLLIE 对比公平性、κ-DR 相关性权重过高
- **3 个 [AGREE]**：W1 (Prop 1)、W4 (S1/S2)、W5 (WikiEvents) — 完全同意
- **3 个 [AGREE with nuance]**：N1（同意但建议降级为 Major）、N2（数据准确但需考虑 DR/CF 质性差异）、W2（因果解释 gap 真实但要求可能过高）
- **1 个 [REBUT]**：W3 (LoRA-only) — full FT 已在 appendix 验证，且 composability 机制论上不依赖 fine-tuning 方法
- **1 个 [AGREE]**：W6 — 与我的 N2 互相印证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2518 · 2026-05-23T10:42:06.231375+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 187

## Round 187

10 recorded events


### User

_source line 2519 · 2026-05-23T10:42:36.344514+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R2-N1: WikiEvents n=20 作为 "task generalization" 证据不足**

同意。§1 Contribution 2 将 WikiEvents pilot 列为贡献的一部分，原文为"a preliminary n=20 event extraction pilot provides directional evidence of task generalization (§5.2)"。虽然使用了"preliminary"和"directional"两个限定词，但将 n=20、MDE≈±5.0pp 的结果放在 contribution bullet 中，在叙事上将其提升到了 contribution-level evidence 的地位。我在自己的 W5 中也独立指出了这一问题。

补充：n=20 的 pilot 不仅统计效力不足，而且 §5.2 仅用一个短段落描述结果，释放的正文空间不如用于深入分析 S1 vs. S2 或 scale-dependent interaction 更有价值。建议：(1) 从 Contribution 2 中删除 WikiEvents 的表述；(2) 将 §5.2 移至 Appendix；(3) 如要保留，应改为"feasibility demonstration"而非"directional evidence of task generalization"。

---

**[AGREE] R2-N2: GoLLIE 比较方法论缺陷**

同意核心判断。Appendix S（Table in app:gollie-comparison）对比 GoLLIE-7B zero-shot（5 predicted relations / 100 docs）vs. OntoCoDec LoRA+S1（~1100 predicted relations / 100 docs），实验条件不对等。GoLLIE-7B 在 SciERC 上 zero-shot 生成极少输出（54% 文档为空），这主要反映 GoLLIE 未在 SciERC schema 上训练，而非两种方法的内在差异。

但需补充两个 nuance：

1. **定位合理性**：论文在 §1 和 §6 将 OntoCoDec 定位为与 training-based methods "orthogonal and complementary"（§1 倒数第二段），而非直接竞争。GoLLIE 比较的目的是展示 training-based 方法在 unseen schema 上的行为模式（near-complete abstention），而非声称 OntoCoDec 优于 GoLLIE。这个定位本身是合理的。

2. **可操作的修改方向**：公平对比需要：(a) 两者均 zero-shot on SciERC（但 OntoCoDec zero-shot R-F1 仅 8%，GoLLIE 仅 5 predictions，两者都不 informative）；(b) GoLLIE fine-tuned on SciERC vs. OntoCoDec fine-tuned（但 GoLLIE 的训练框架不同于 LoRA，仍非 apples-to-apples）；(c) 最诚实的做法是删除 Appendix S 的直接对比表，改为定性讨论两种 paradigm 的 trade-off。

---

### Should-Fix

**[AGREE] R2-W1: Proposition 1 新颖性被高估**

同意，与我的 W1 一致。论文自己在 Contribution 1 中承认是"formalizing a known intuition for the IE setting"，但 pumping lemma proof（Appendix O）和正文中 Proposition 1 的 prominent presentation（§3 的独立 boldface 定理）给人的印象是这是一个 substantial theoretical contribution。实际上，任何使用过 grammar-constrained decoding 处理 IE 的研究者都知道 grammar 不能约束跨位置语义依赖——这是 engineering observation 而非 theoretical surprise。

proof 本身在技术上是正确的（我在 Round 1 审稿中已验证），但其价值更接近"使已知直觉 rigorous"而非"发现新的不可能性结果"。论文的 engineering applicability 段落（§3: DFA 状态数 $6^{17} \approx 1.6 \times 10^{13}$）实际上比 Proposition 1 本身更 informative，因为它解决的是实际问题（finite entity sets 的 intractability）而非渐近问题（unbounded entity sets 的 impossibility）。

---

**[AGREE] R2-W2: 70B 验证单一模型族但称 "scale validation"**

同意。Contribution 3 标题"Single-family scale validation on Llama-3.1-70B (AWQ INT4)"中"single-family"是一个限定词，但仍称为"scale validation"有 overclaiming 之嫌。具体来说：

- 仅测试 Llama 一个模型族，未覆盖 Qwen-72B 或 Mistral-Large
- 使用 AWQ INT4 量化，虽然 Appendix R 确认 8B 量化不影响 enforcement，但无 70B FP16 对比（Limitations 中承认"a direct 70B FP16 comparison exceeds our hardware capacity"）
- scale-dependent interaction（semantic-only 24% → 84% DR reduction）是一个 interesting finding，但基于单一模型族的单一数据点，不足以称为"validated"

建议将 Contribution 3 改为"Preliminary 70B exploration"或"Single-model scale probe"，不使用"validation"一词。

---

**[AGREE] R2-W3: DR↔CF trade-off 讨论不足**

强烈同意，与我的 N2（Critical）一致。这是我和 R2 共同认为的最重要问题之一。

补充 R2 的论点：

- Zero-shot greedy S1: total violation rate 从 15.45% 降至 10.83%（DR 0.93% + CF 9.90%），净降幅仅 30%
- Fine-tuning 后 total violation 从 1.95% 降至 1.18%（DR 0→0 + CF 0→1.18%），CF 反而从 0 增加到 1.18%
- Table 2 中 Qwen3-8B SciERC FT: unconstrained DR=1.95%, CF=0；S1: DR=0, CF=1.18%。total violation 从 1.95% 降至 1.18%，绝对值改善仅 0.77pp

论文将 CF 定性为"correctable side effect"（§1 Contribution 2），但 TCR（Appendix M）未集成到系统中，beam search（k=4）的 1.39× latency 在部署中可能 unacceptable。

---

**[AGREE] R2-W4: κ 分析在正文中占据过多空间**

同意，与我的 N1（Critical）一致。§4 "Constraint Tightness"段落为 κ 给出了独立定义式（κ(r) = 1 − |σ(r)|/|E|²）、三个数据点的具体数值（WikiEvents 0.029, SciERC 0.333, DocRED 0.842）、p 值（0.138），并在 Appendix 中有独立的 case study（Appendix N, P）。对于一个 n=3、p=0.138 的"descriptive"观察，这个叙事比重过高。

---

### 小问题

**[AGREE] R2-M1: Abstract F1 范围不准确**

同意。Abstract 声称"F1 41-47%"，但 Table 2 中 Qwen3-8B DocRED S1 R-F1=40.79%，低于 41%。这是一个 factual inconsistency。应修正为"F1 40-47%"或"R-F1 ~41-47%"。

§1 Introduction 中也有"R-F1 41-47%"的表述（"R-F1 41--47\% ($\pm$0.8\,pp, $+$10\% latency)"），同样需要修正。

---

**[AGREE] R2-M2: CRANE 与 S2 在 70B 下的 R-F1 降低相关**

同意。S2 在 70B 下 R-F1 降低 8.45pp（Limitations 中报告），而 CRANE（Banerjee et al., 2025）的核心论点正是 constrained decoding 会抑制 reasoning。论文在 Appendix B（Extended Related Work, "Quality Impact of Constrained Decoding"段落）讨论了 CRANE，并提到"A two-pass variant (S2), explored in ablation (Section 5), separates extraction and constraint enforcement into distinct passes, analogous to CRANE's alternating strategy"。但这个 connection 仅出现在 Appendix B，未在正文的 S2 讨论中提及。

S2 在 70B 下的显著降级（vs. 8B 下 S1/S2 comparable）正是 CRANE 理论预测的现象：larger models 对 constraint 的 reasoning interference 更敏感。这个 connection 应在正文 §3.4 或 §5 70B results 段落中明确指出。

---

**[AGREE] R2-M3: DocRED dev set 说明应更显著**

同意。当前仅在 footnote 1（§5 Setup）中提及"DocRED test annotations are not publicly available; we evaluate on the development set"。考虑到 DocRED 是两个主要评估数据集之一，这一重要 caveat 应提升到正文级别（如 Setup 段落的第一句话）。

---

**[AGREE] R2-M4: Figure 1 缺少端到端 running example**

同意。Figure 1 是一个抽象架构图，展示 IE Ontology → Constraint Layers (Grammar Compilation + Token Masking) 的流程，但不包含具体的输入文本、实体、关系和 masking 过程。§3.3 中有一个文本形式的 running example（"for Used-for (dom={Method}, range={Task}), entity 'ResNet' (Method) passes..."），但未 visualize 在图中。

对于一个 decoding-time 方法，一个展示具体 token-level masking 过程的 step-by-step example（如 input sentence → entity generation → registry population → relation generation → type masking）会极大提升可读性。

---

**[AGREE] R2-M5: "100% preservation across all configurations" 表述不清**

同意。§3.1 原文为"The grammar structurally enforces entity-before-relation ordering (100% preservation across all configurations)"。"100% preservation"容易被误读为"100% of predictions are preserved"或"100% F1 preservation"。实际含义是"entity-before-relation ordering is maintained in 100% of outputs across all experimental configurations"。建议改为"maintained in all N documents across all configurations"（给出具体 N），消除歧义。

---

**[AGREE] R2-M6: Schema coverage gap 对 schema evolution 的影响未讨论**

同意。Limitations 中提到"schema gaps arise from training-data-derived constraints that may not cover all valid type pairs"，Appendix（residual DR analysis）报告 schema coverage gaps 占 fine-tuning residual DR 的 33%。但论文未讨论 schema evolution 场景：当新的 valid type pairs 出现时（如新增实体类型或关系），现有 constraints 会 over-restrict。这在实际部署中是一个重要考量，值得在 Limitations 或 Discussion 中简短提及。

---

### 总结

R2 的 12 个问题中，我全部 AGREE。其中 N1（WikiEvents contribution overclaim）、N2（GoLLIE 对比方法论缺陷）与我自己独立发现的问题一致或互补。R2 的 W3（DR↔CF trade-off）与我的 N2 高度重合，是两位 reviewer 共同认为的最重要修改点。M1（F1 范围 factual error）和 M2（CRANE connection）是我未独立注意到的有效发现。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2520 · 2026-05-23T10:43:08.224974+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2521 · 2026-05-23T10:43:08.275765+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T10:27:23.095879+00:00\", \"completed_at\": \"2026-05-23T10:31:47.427271+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"主文 8 页仅 3 个 display items（1 figure + 2 tables），对于实证型论文偏少（通常 5-8 个）。大量实验结果全部推入附录，审稿人在主文中缺乏足够的视觉锚点来快速评估实验力度。建议将至少 1-2 个关键结果表或 ablation 图提至主文\"}, {\"severity\": \"warning\", \"dimension\": \"page 4-5\", \"message\": \"Method 段连续 2 页纯文本，无 figure/table/algorithm box 穿插。Section 3.1-3.3 的解码策略描述可考虑用 Algorithm 伪代码或流程图打断文字墙\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Related Work + Discussion/Conclusion 合占 1 整页纯文本，紧接在 Table 2（page 7）之后。Discussion 段无任何总结性图表（如 radar chart 或对比概览图）辅助审稿人快速抓取核心 takeaway\"}, {\"severity\": \"info\", \"dimension\": \"page 32\", \"message\": \"Table 35 使用红色删除线+绿色新增文字展示纠错案例。红/绿对比对色盲用户不友好，建议改为蓝/橙或增加额外视觉标记（如下划线/波浪线）\"}, {\"severity\": \"info\", \"dimension\": \"page 39\", \"message\": \"末页内容填充约 60-65%，略低于 2/3 标准。可通过调整附录末尾表格分布或微调间距改善\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 内部组件标注文字偏小（约正文 60%），在打印场景下可能影响可读性。建议适当增大关键标签字号\"}, {\"severity\": \"info\", \"dimension\": \"page 25, 28, 31\", \"message\": \"多页堆叠 4 张表格，信息密度极高。虽为附录可接受，但部分表格（如 Table 18/19、Table 24/25/26/27）内容相关可考虑合并以减少视觉碎片化\"}, {\"severity\": \"info\", \"dimension\": \"page 6-7\", \"message\": \"Table 1 和 Table 2 使用 booktabs 风格、最优值加粗标注，格式专业。小数位数在同列内一致\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Table 3 展示 prompt 模板，内部文字较小但作为附录示例可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 20\", \"message\": \"Figure 2 散点图、[page 23] Figure 3 柱状图、[page 29] Figure 4 双面板图——附录图表分辨率充足、轴标签清晰\"}], \"counts\": {\"critical\": 0, \"warning\": 3, \"info\": 7}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2522 · 2026-05-23T10:43:09.733862+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2523 · 2026-05-23T10:43:09.985889+00:00_

1	# Review Issues Tracker — schema_semantic_constrained_ie
2	# Updated: R24 Action Matrix dispatched, 2026-05-23
3	
4	# ============================================================
5	# Round 24 — Issues with actions dispatched
6	# ============================================================
7	
8	- id: "R16-W5"
9	  summary: "Proposition 1 定位过高 + 理论-实践 gap 桥接不充分"
10	  category: framing
11	  severity: critical
12	  status: in_progress
13	  first_raised_round: 14
14	  last_seen_round: 24
15	  mentions:
16	    - round: 19
17	      reviewers: [1, 2]
18	      note: "共识定位为 systems contribution。"
19	    - round: 23
20	      reviewers: [1, 2]
21	      note: "与 R23-W2/W7 合并。降低理论贡献措辞。"
22	    - round: 24
23	      reviewers: [1, 2]
24	      note: "R24-MF1 (critical)。R23 写作降级不够——需重写定位为 formalizing known intuition + DFA 可行边界 + proof sketch 扩展。R1/R2 分歧：R2 认为 trivial, R1 认为分类法有架构指导价值。"
25	  action_items:
26	    - round: 19
27	      action: "§7 Discussion 定位 systems contribution"
28	      assigned_to: paper_agent
29	      status: completed
30	    - round: 21
31	      action: "§3 论证 semantic layer 非显而易见"
32	      assigned_to: paper_agent
33	      status: completed
34	    - round: 23
35	      action: "降低 Proposition 1 强度 + κ 统计限定"
36	      assigned_to: paper_agent
37	      status: completed
38	    - round: 24
39	      action: "§1 C1 重写 'formalizing known intuition' + §3 DFA 可行边界(SciERC 6^10, DocRED 6^30) + proof sketch 4-5行 + 区分 theoretical impossibility vs engineering impracticality"
40	      assigned_to: paper_agent
41	      status: in_progress
42	  resolution: ""
43	  resolution_round: null
44	
45	- id: "R16-W1"
46	  summary: "κ-DR 相关性 n=3 呈现不当——Abstract/§1 仍用 correlate"
47	  category: framing
48	  severity: critical
49	  status: in_progress
50	  first_raised_round: 12
51	  last_seen_round: 24
52	  mentions:
53	    - round: 22
54	      reviewers: [1, 2]
55	      note: "R22 解决：加 empirical + scale-dependent qualifier + descriptive only。"
56	    - round: 24
57	      reviewers: [1, 2]
5
…[truncated 16308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 2524 · 2026-05-23T10:46:42.662882+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: R25 fresh review, 2026-05-23\n\n# ============================================================\n# Round 25 — Active Issues\n# ============================================================\n\n- id: \"R16-W5\"\n  summary: \"Proposition 1 定位过高 + 理论-实践 gap 桥接不充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 25\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"共识定位为 systems contribution。\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"与 R23-W2/W7 合并。降低理论贡献措辞。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-MF1 (critical)。R23 写作降级不够。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R1-W1+R2-W1 完全共识 [Major]。论文已改为 'formalizing a known intuition'，定位诚实但仍列为 Contribution 1 首位且 §3 篇幅过大。两位 Reviewer 认为 engineering applicability (DFA 6^17 states) 比 Proposition 1 本身更有价值。多轮复发但严重程度已从 critical 降为 warning——定位措辞已改善，问题在于展示权重。\"\n  action_items:\n    - round: 19\n      action: \"§7 Discussion 定位 systems contribution\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"§3 论证 semantic layer 非显而易见\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 23\n      action: \"降低 Proposition 1 强度 + κ 统计限定\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"§1 C1 重写 'formalizing known intuition' + §3 DFA 可行边界 + proof sketch 扩展\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 25\n      action: \"降低 Proposition 1 展示权重：从 Contribution 1 首位降级，或将 engineering applicability 作为主要论述重心而非 pumping lemma proof\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W1\"\n  summary: \"κ-DR 相关性 n=3 呈现不当——正文 §4 叙事权重过高\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 25\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R22 解决：加 empirical + scale-dependent qualifier + descriptive only。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-MF2 (critical)。R23 只改了 §4，Abstract/§1 仍用 correlate。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R1-N1+R2-W4 完全共识。§4 已标注 descriptive (n=3, p=0.138)，但正文中 κ 仍有独立定义式+整段分析+Appendix case study。叙事权重与 n=3 证据强度不匹配。R2 建议降 Critical→Major，因未列入 Contribution。R1 指出 κ 是 confounded variable (entity type confusability)。共识：压缩 §4 至 1-2 句，详细分析移 Appendix。\"\n  action_items:\n    - round: 22\n      action: \"全文加 empirical + scale-dependent qualifier\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 23\n      action: \"加 descriptive only (n=3, p=0.138)\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"全文统一 correlate → observed pattern\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 25\n      action: \"§4 Constraint Tightness 压缩为 1-2 句描述性观察，删除 p 值报告（n=3 的 p 值本身误导），详细分析移 Appendix\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W5\"\n  summary: \"70B 验证单一模型族 + Contribution 声称 'scale validation' overclaim\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W4。Abstract 加 '(AWQ INT4)' + §5.3 量化限制声明。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-MF3 (critical)。Contribution 拆分要求。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R2-W2+R1 AGREE [Major]。Contribution 3 已标 'Single-family scale validation' 但仍用 'validation'。仅 Llama-3.1-70B AWQ INT4，无 Qwen-72B/Mistral-Large，无 FP16 对比。Scale-dependent interaction (24%→84%) 基于单一模型族单一数据点。需改 'preliminary observation/probe'。\"\n  action_items:\n    - round: 23\n      action: \"Abstract 加 '(AWQ INT4)' + §5.3 量化限制声明\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"Contribution 拆分为 C2(8B)+C3(70B preliminary)+C4(部署)\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 25\n      action: \"Contribution 3 改 'Preliminary 70B exploration' 或 'Single-model scale probe'，不用 'validation'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W4\"\n  summary: \"WikiEvents n=20 不足以支撑 task generalization contribution claim\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"降级 contribution list + Preliminary Pilot 标题。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-SF3。复发——Table 仍在正文。必须移 Appendix。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R2-N1 [Critical]+R1-W5 [Major]，完全共识。§1 Contribution 2 仍包含 'directional evidence of task generalization'。n=20, MDE≈±5.0pp 不构成 generalization 证据。两位 Reviewer 一致要求：(1)从 Contribution 删除 WikiEvents；(2)§5.2 移至 Appendix 或正文仅 1 句概述；(3)如保留改为 feasibility demonstration。多轮复发，升级为 critical。\"\n  action_items:\n    - round: 23\n      action: \"降级 contribution list + 标题改 Preliminary Pilot\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"Table 移至 Appendix + 正文压缩为 1-2 句\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 25\n      action: \"从 Contribution 2 完全删除 WikiEvents 表述 + §5.2 移至 Appendix + 正文最多保留 1 句 feasibility mention\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-N2\"\n  summary: \"GoLLIE 比较方法论不公平——零样本 GoLLIE vs. 微调 OntoCoDec\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-N2 [Critical]+R1-W6 [Minor] 交叉后共识 [Critical]。Appendix S 对比 GoLLIE-7B zero-shot (5 predicted relations) vs. OntoCoDec LoRA+S1 (~1100 predictions)。§6 引用此结论('near-complete output suppression')定位差异化，但实验条件不对等——GoLLIE 未在 SciERC 训练导致输出少，非方法内在差异。R1 补充：定位为 'complementary' 合理，但附录对比表应删除或改为定性讨论。注：R23-W3 曾标 resolved(R24 R1 rebut 有效)，但 R25 fresh review 重新发现并升级。\"\n  action_items:\n    - round: 25\n      action: \"删除 Appendix S 直接对比表，改为定性讨论两种 paradigm trade-off；§6 删除或限定 'near-complete output suppression' 表述，显著说明不可比原因\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W1\"\n  summary: \"DR↔CF trade-off 在零样本场景下严重程度讨论不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1-N2 [Critical]+R2-W3 [Major]，交叉后共识 [Major]。Zero-shot greedy S1: total violation 15.45%→10.83% 仅降 30% (DR↓94% 但 CF 0.08%→9.90%)。Abstract 突出 DR reduction 但 CF increase 不对称。R2 补充：(1)Abstract 确实提及 zero-shot CF 可达 12%；(2)DR/CF 质性差异真实(DR 不可恢复 vs CF 可 post-hoc)；(3)推荐配置 fine-tuned+beam 下 trade-off 很小。共识：Abstract framing 需更对称，§7 Discussion 需扩展 CF 实际影响分析。\"\n  action_items:\n    - round: 25\n      action: \"Abstract 同时报告 DR reduction 和 CF increase 的 net effect + §7 Discussion 扩展 zero-shot CF 实际影响(如 CF violations 中多少 match gold labels) + 明确推荐 beam k≥2 作为 zero-shot 部署配置\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W2\"\n  summary: \"Scale-dependent layer interaction 缺乏因果解释\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1-W2 [Major]+R2 Q3 AGREE。Semantic-only 在 8B 仅 24% DR reduction vs. 70B 达 84%，论文仅称 'empirical observation' 无因果解释。候选假设：(1)70B vocabulary calibration 更好；(2)logit distribution 更 peaked；(3)fallback 频率差异。现有数据(Appendix C fallback tracing)应可提供部分解释但未连接。\"\n  action_items:\n    - round: 25\n      action: \"§3 或 §5 添加 1-2 句关于 scale-dependent interaction 的机制讨论，至少分析 8B vs 70B semantic-only 下的 fallback 频率差异\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W3\"\n  summary: \"S1 vs S2 对比缺乏深入分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1-W4 [Major]+R2 AGREE。S2 R-F1 低于 S1 (8.03 vs 8.36) 但 CF 更优 (8.03% vs 9.90%)，差异未做统计检验。70B 下 S2 降 8.45pp 未分析具体 failure case。S2 何时优于 S1 无指导。R2 注：S1/S2 分析是次要叙事，Major 但不影响接收。\"\n  action_items:\n    - round: 25\n      action: \"提供 S1 vs S2 的 paired bootstrap test + 70B S2 failure case 分析 + 在何种条件下推荐 S2 的指导\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M1\"\n  summary: \"Abstract F1 范围 '41-47%' 与 Table 2 数据不一致 (Qwen DocRED S1 R-F1=40.79%)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-M1+R1 AGREE。Factual inconsistency。应改为 'R-F1 40-47%' 或加 rounding 说明。§1 也有同样问题。\"\n  action_items:\n    - round: 25\n      action: \"Abstract + §1 中 'F1 41-47%' 修正为 'R-F1 40-47%'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M2\"\n  summary: \"CRANE (Banerjee et al., 2025) 仅在 Appendix B 讨论，应在主文提及\"\n  category: related_work\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-M2+R1 AGREE。S2 在 70B 下 R-F1 降 8.45pp 正是 CRANE 预测的 constraint→reasoning interference 现象。Appendix B 已讨论但 connection 应在主文 §3.4 或 §5 70B 段明确指出。\"\n  action_items:\n    - round: 25\n      action: \"§3.4 或 §5 70B 段添加 CRANE reference，指出 S2 70B 降级与 CRANE 理论预测一致\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M3\"\n  summary: \"DocRED dev set 使用说明应从 footnote 提升至正文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-M3+R1 AGREE。DocRED 是两大评估数据集之一，使用 dev set 而非 test set 的 caveat 仅在 footnote 1。\"\n  action_items:\n    - round: 25\n      action: \"§5 Setup 段正文中显著说明 DocRED 使用 development set (test annotations unavailable)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M4\"\n  summary: \"Figure 1 缺少端到端 running example\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-M4+R1 AGREE。§3.3 有文本 running example 但未可视化。一个 token-level masking step-by-step 示例会极大提升可读性。注：与 R20-W5(wont_fix due to space) 相关，但 R25 从不同角度提出。\"\n  action_items:\n    - round: 25\n      action: \"考虑在 Figure 1 或新 Figure 中添加具体的 masking 过程示例\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M5\"\n  summary: \"Schema coverage gap 对 schema evolution 场景的影响未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-M6+R1 AGREE。Empirical constraints 0.6-1.0% 未覆盖 valid type pairs。新增实体类型或关系时 constraints 会 over-restrict。Limitations 应简短提及。\"\n  action_items:\n    - round: 25\n      action: \"Limitations 或 Discussion 加 1-2 句 schema evolution caveat\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Carried from prior rounds — status updated for R25\n# ============================================================\n\n- id: \"R24-SF1\"\n  summary: \"缺乏 OntoCoDec 作为 constraint enforcement method 的明确定位声明\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2-N2, R1 rebut 部分有效。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 未作为独立 issue 提出，但 §1 已有 'orthogonal and complementary' 定位。与 R25-N2 (GoLLIE 比较公平性) 相关。\"\n  action_items:\n    - round: 24\n      action: \"§1 加定位声明\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-SF2\"\n  summary: \"R-F1 41-47% 在正文中缺乏 LLM-based generative RE 上下文定位\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"正文缺上下文。\"\n    - round: 25\n      note: \"R25 未单独提出。§5 Setup 已有 'R-F1 range (41-47% under LoRA) is consistent with recent LLM-based generative RE benchmarks' 定位。可能已部分修复。\"\n  action_items:\n    - round: 24\n      action: \"§5 Setup 加 1-2 句 LLM-based generative RE 典型 F1 范围定位\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W12\"\n  summary: \"First-seen semantics 级联错误影响未量化\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"§3.3 formalize + Limitations 加 entity-first 约束。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-SF4。要求数据量化。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R1 在 §5.1 Cross-field violation analysis 中注意到论文已报告 cascade error 数据 (correct locks 2.5× more frequent than cascade errors, 7.3%)。R2 未单独提出。可能已部分修复——需确认正文中数据是否充分。\"\n  action_items:\n    - round: 24\n      action: \"Agent 分析 245 CF violations 中 first-seen 级联 vs 合法歧义分解\"\n      assigned_to: main_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-SF5\"\n  summary: \"§7 Discussion 过于压缩——缺 DR↔CF trade-off 等讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"需压缩 §6 释放空间。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 与 R25-W1 (CF trade-off 讨论不足) 直接相关。§7 仍仅约 0.5 页。需扩展 DR↔CF trade-off、per-triple vs global enforcement、training-based complementarity 讨论。\"\n  action_items:\n    - round: 24\n      action: \"压缩 §6 + §7 扩展为 3 段\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 25\n      action: \"§7 扩展 CF 实际影响分析 + beam search 推荐\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-SF7\"\n  summary: \"LoRA 超参从 SciERC 直接转移到 DocRED 缺乏论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"DDL 内无法补实验，承认限制。\"\n    - round: 25\n      note: \"R25 未单独提出。Limitations 已有 'LoRA hyperparameters were tuned on SciERC and transferred to DocRED without dataset-specific optimization, which may underestimate DocRED potential'。可能已修复。\"\n  action_items:\n    - round: 24\n      action: \"§5 Setup + Limitations 承认超参转移限制\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W2\"\n  summary: \"算法创新有限——主要是 XGrammar + stateful logits processor 的系统集成\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"降低 Proposition 1 强度。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"合并到 R16-W5/MF1。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R1(Excitement 3/5)+R2(Excitement 3/5) 一致：核心方案是现有 constrained decoding 的自然延伸，entity registry + dynamic masking 概念上非 surprising。论文价值主要在实证而非概念。与 R16-W5 紧密相关。\"\n  action_items:\n    - round: 25\n      action: \"合并到 R16-W5 处理——将论文重心从理论贡献转向实证贡献和工程设计\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior Rounds — Resolved (confirmed in R25 or earlier)\n# ============================================================\n\n- id: \"R23-W1\"\n  summary: \"CF 违规占残余违规 64%，与标题 'Type-Constrained IE' 形成 gap\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R24 未作为独立 weakness。R25 CF 讨论转向 zero-shot severity (R25-W1) 而非 title gap。\"\n  resolution_round: 24\n\n- id: \"R23-W3\"\n  summary: \"GoLLIE 对比不公平 + 缺少与训练基方法的系统性对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"§6 GoLLIE 段重写。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 rebut 有效——已有三层对比。标 resolved。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 fresh review 重新发现并升级为 R25-N2 [Critical]。R24 的 'resolved' 判断错误——§6 重写和定位声明未解决 Appendix S 对比表的方法论不公平。合并到 R25-N2。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W6\"\n  summary: \"Zero-shot 实验占主文 ~3 页但 R-F1 仅 4-8%，篇幅分配失衡\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R24 未提及。R25 未提及。压缩有效。\"\n  resolution_round: 24\n\n- id: \"R23-W7\"\n  summary: \"Proposition 1 实际意义论证 gap\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      note: \"合并到 R16-W5。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W8\"\n  summary: \"'Empirical enabling dependency' 重复 ≥6 次\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R24/R25 均未提及。修复有效。\"\n  resolution_round: 24\n\n- id: \"R23-W9\"\n  summary: \"Fallback 频率模型依赖性未在正文讨论\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R24/R25 均未作为独立 issue。R25 R1-S6 还肯定了 fallback causal tracing (Appendix C)。\"\n  resolution_round: 24\n\n- id: \"R23-W10\"\n  summary: \"Continuation masking prefix collision 频率未量化\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      note: \"R25 R1-Q3 追问了 morphologically similar types 的失败率。未被 R25 列为 weakness 但作为 question 保留。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W11\"\n  summary: \"Beam width sensitivity 讨论不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      note: \"R25 未单独提出。论文 §5 已有 beam sweep (k∈{1,2,4,8})，R1-S2 肯定了 beam search 评估。可能已修复。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-D1\"\n  summary: \"Limitations 长度是否 excessive\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R24/R25 均评 Limitations 充分。R25 R2-S3 特别肯定了三段式 Limitations 的透明度。\"\n  resolution_round: 24\n\n- id: \"R16-MF3\"\n  summary: \"CF trade-off 在 Abstract 中 framing 偏乐观\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  resolution: \"Abstract CF 分层报告。R25 仍有相关问题(R25-W1)但性质不同——不是隐瞒 CF 而是叙事不对称。\"\n  resolution_round: 22\n\n- id: \"R16-W4\"\n  summary: \"70B AWQ INT4 quantization 对约束效果的影响未隔离\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 21\n  resolution: \"Appendix R 4 组配置验证。R25 R1-S4 肯定了 quantization robustness 验证。\"\n  resolution_round: 22\n\n- id: \"R16-W3\"\n  summary: \"WikiEvents fine-tuning composability 仅 n=20 文档\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      note: \"合并到 R23-W4。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出至第 9 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  resolution: \"R25 格式检查确认主文 §1-§7 在 page 1-8。\"\n  resolution_round: 22\n\n- id: \"R18-M2\"\n  summary: \"Figure 1 视觉层次不够分明\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      note: \"R25 Visual Check info: Figure 1 内部组件标注文字偏小(约正文 60%)。R2-M4 要求端到端 running example。问题从'视觉层次'转为'缺少具体示例'。合并到 R25-M4。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W1\"\n  summary: \"Proposition 1 证明中 position→name 转换缺乏形式论证\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      note: \"R25 R1 小问题中提到 Appendix O proof Case 1 的 position vs. name-based 区分不够清晰。问题仍存在但严重程度低。合并到 R16-W5。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W4\"\n  summary: \"主文 Related Work §6 过于精简\"\n  category: related_work\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 23\n  resolution: \"R25 R2-S5 肯定 Related Work 三轴组织清晰有效。无关精简问题。\"\n  resolution_round: 23\n\n- id: \"R24-SF6\"\n  summary: \"Contribution 2 过度打包\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      note: \"R25 仍见 Contribution 2 包含多项内容。合并到 R23-W5 处理。\"\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Won't Fix\n# ============================================================\n\n- id: \"R20-W5\"\n  summary: \"Running example 仍不充分\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"空间限制无法在正文加完整 running example。R25-M4 从不同角度重新提出。\"\n  resolution_round: 20\n\n- id: \"R20-W6\"\n  summary: \"Zero-shot 评估实际意义有限（R-F1 仅 4-8%）\"\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 23\n  resolution: \"ZS 定位为 diagnostic probe。R25 未复发。\"\n  resolution_round: 23\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: R25 fresh review, 2026-05-23\n\n# ============================================================\n# Round 25 — Active Issues\n# ============================================================\n\n- id: \"R16-W5\"\n  summary: \"Proposition 1 定位过高 + 理论-实践 gap 桥接不充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 25\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"共识定位为 systems contribution。\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"与 R23-W2/W7 合并。降低理论贡献措辞。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-MF1 (critical)。R23 写作降级不够。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R1-W1+R2-W1 完全共识 [Major]。论文已改为 'formalizing a known intuition'，定位诚实但仍列为 Contribution 1 首位且 §3 篇幅过大。两位 Reviewer 认为 engineering applicability (DFA 6^17 states) 比 Proposition 1 本身更有价值。多轮复发但严重程度已从 critical 降为 warning——定位措辞已改善，问题在于展示权重。\"\n  action_items:\n    - round: 19\n      action: \"§7 Discussion 定位 systems contribution\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"§3 论证 semantic layer 非显而易见\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 23\n      action: \"降低 Proposition 1 强度 + κ 统计限定\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"§1 C1 重写 'formalizing known intuition' + §3 DFA 可行边界 + proof sketch 扩展\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 25\n      action: \"降低 Proposition 1 展示权重：从 Contribution 1 首位降级，或将 engineering applicability 作为主要论述重心而非 pumping lemma proof\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W1\"\n  summary: \"κ-DR 相关性 n=3 呈现不当——正文 §4 叙事权重过高\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 25\n  mentions:\n    - round: 22\n      reviewers: [1, 2]\n      note: \"R22 解决：加 empirical + scale-dependent qualifier + descriptive only。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-MF2 (critical)。R23 只改了 §4，Abstract/§1 仍用 correlate。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R1-N1+R2-W4 完全共识。§4 已标注 descriptive (n=3, p=0.138)，但正文中 κ 仍有独立定义式+整段分析+Appendix case study。叙事权重与 n=3 证据强度不匹配。R2 建议降 Critical→Major，因未列入 Contribution。R1 指出 κ 是 confounded variable (entity type confusability)。共识：压缩 §4 至 1-2 句，详细分析移 Appendix。\"\n  action_items:\n    - round: 22\n      action: \"全文加 empirical + scale-dependent qualifier\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 23\n      action: \"加 descriptive only (n=3, p=0.138)\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"全文统一 correlate → observed pattern\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 25\n      action: \"§4 Constraint Tightness 压缩为 1-2 句描述性观察，删除 p 值报告（n=3 的 p 值本身误导），详细分析移 Appendix\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W5\"\n  summary: \"70B 验证单一模型族 + Contribution 声称 'scale validation' overclaim\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W4。Abstract 加 '(AWQ INT4)' + §5.3 量化限制声明。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-MF3 (critical)。Contribution 拆分要求。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R2-W2+R1 AGREE [Major]。Contribution 3 已标 'Single-family scale validation' 但仍用 'validation'。仅 Llama-3.1-70B AWQ INT4，无 Qwen-72B/Mistral-Large，无 FP16 对比。Scale-dependent interaction (24%→84%) 基于单一模型族单一数据点。需改 'preliminary observation/probe'。\"\n  action_items:\n    - round: 23\n      action: \"Abstract 加 '(AWQ INT4)' + §5.3 量化限制声明\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"Contribution 拆分为 C2(8B)+C3(70B preliminary)+C4(部署)\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 25\n      action: \"Contribution 3 改 'Preliminary 70B exploration' 或 'Single-model scale probe'，不用 'validation'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W4\"\n  summary: \"WikiEvents n=20 不足以支撑 task generalization contribution claim\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"降级 contribution list + Preliminary Pilot 标题。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-SF3。复发——Table 仍在正文。必须移 Appendix。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R2-N1 [Critical]+R1-W5 [Major]，完全共识。§1 Contribution 2 仍包含 'directional evidence of task generalization'。n=20, MDE≈±5.0pp 不构成 generalization 证据。两位 Reviewer 一致要求：(1)从 Contribution 删除 WikiEvents；(2)§5.2 移至 Appendix 或正文仅 1 句概述；(3)如保留改为 feasibility demonstration。多轮复发，升级为 critical。\"\n  action_items:\n    - round: 23\n      action: \"降级 contribution list + 标题改 Preliminary Pilot\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"Table 移至 Appendix + 正文压缩为 1-2 句\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 25\n      action: \"从 Contribution 2 完全删除 WikiEvents 表述 + §5.2 移至 Appendix + 正文最多保留 1 句 feasibility mention\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-N2\"\n  summary: \"GoLLIE 比较方法论不公平——零样本 GoLLIE vs. 微调 OntoCoDec\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-N2 [Critical]+R1-W6 [Minor] 交叉后共识 [Critical]。Appendix S 对比 GoLLIE-7B zero-shot (5 predicted relations) vs. OntoCoDec LoRA+S1 (~1100 predictions)。§6 引用此结论('near-complete output suppression')定位差异化，但实验条件不对等——GoLLIE 未在 SciERC 训练导致输出少，非方法内在差异。R1 补充：定位为 'complementary' 合理，但附录对比表应删除或改为定性讨论。注：R23-W3 曾标 resolved(R24 R1 rebut 有效)，但 R25 fresh review 重新发现并升级。\"\n  action_items:\n    - round: 25\n      action: \"删除 Appendix S 直接对比表，改为定性讨论两种 paradigm trade-off；§6 删除或限定 'near-complete output suppression' 表述，显著说明不可比原因\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W1\"\n  summary: \"DR↔CF trade-off 在零样本场景下严重程度讨论不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1-N2 [Critical]+R2-W3 [Major]，交叉后共识 [Major]。Zero-shot greedy S1: total violation 15.45%→10.83% 仅降 30% (DR↓94% 但 CF 0.08%→9.90%)。Abstract 突出 DR reduction 但 CF increase 不对称。R2 补充：(1)Abstract 确实提及 zero-shot CF 可达 12%；(2)DR/CF 质性差异真实(DR 不可恢复 vs CF 可 post-hoc)；(3)推荐配置 fine-tuned+beam 下 trade-off 很小。共识：Abstract framing 需更对称，§7 Discussion 需扩展 CF 实际影响分析。\"\n  action_items:\n    - round: 25\n      action: \"Abstract 同时报告 DR reduction 和 CF increase 的 net effect + §7 Discussion 扩展 zero-shot CF 实际影响(如 CF violations 中多少 match gold labels) + 明确推荐 beam k≥2 作为 zero-shot 部署配置\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W2\"\n  summary: \"Scale-dependent layer interaction 缺乏因果解释\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1-W2 [Major]+R2 Q3 AGREE。Semantic-only 在 8B 仅 24% DR reduction vs. 70B 达 84%，论文仅称 'empirical observation' 无因果解释。候选假设：(1)70B vocabulary calibration 更好；(2)logit distribution 更 peaked；(3)fallback 频率差异。现有数据(Appendix C fallback tracing)应可提供部分解释但未连接。\"\n  action_items:\n    - round: 25\n      action: \"§3 或 §5 添加 1-2 句关于 scale-dependent interaction 的机制讨论，至少分析 8B vs 70B semantic-only 下的 fallback 频率差异\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W3\"\n  summary: \"S1 vs S2 对比缺乏深入分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R1-W4 [Major]+R2 AGREE。S2 R-F1 低于 S1 (8.03 vs 8.36) 但 CF 更优 (8.03% vs 9.90%)，差异未做统计检验。70B 下 S2 降 8.45pp 未分析具体 failure case。S2 何时优于 S1 无指导。R2 注：S1/S2 分析是次要叙事，Major 但不影响接收。\"\n  action_items:\n    - round: 25\n      action: \"提供 S1 vs S2 的 paired bootstrap test + 70B S2 failure case 分析 + 在何种条件下推荐 S2 的指导\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M1\"\n  summary: \"Abstract F1 范围 '41-47%' 与 Table 2 数据不一致 (Qwen DocRED S1 R-F1=40.79%)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-M1+R1 AGREE。Factual inconsistency。应改为 'R-F1 40-47%' 或加 rounding 说明。§1 也有同样问题。\"\n  action_items:\n    - round: 25\n      action: \"Abstract + §1 中 'F1 41-47%' 修正为 'R-F1 40-47%'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M2\"\n  summary: \"CRANE (Banerjee et al., 2025) 仅在 Appendix B 讨论，应在主文提及\"\n  category: related_work\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-M2+R1 AGREE。S2 在 70B 下 R-F1 降 8.45pp 正是 CRANE 预测的 constraint→reasoning interference 现象。Appendix B 已讨论但 connection 应在主文 §3.4 或 §5 70B 段明确指出。\"\n  action_items:\n    - round: 25\n      action: \"§3.4 或 §5 70B 段添加 CRANE reference，指出 S2 70B 降级与 CRANE 理论预测一致\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M3\"\n  summary: \"DocRED dev set 使用说明应从 footnote 提升至正文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-M3+R1 AGREE。DocRED 是两大评估数据集之一，使用 dev set 而非 test set 的 caveat 仅在 footnote 1。\"\n  action_items:\n    - round: 25\n      action: \"§5 Setup 段正文中显著说明 DocRED 使用 development set (test annotations unavailable)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M4\"\n  summary: \"Figure 1 缺少端到端 running example\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-M4+R1 AGREE。§3.3 有文本 running example 但未可视化。一个 token-level masking step-by-step 示例会极大提升可读性。注：与 R20-W5(wont_fix due to space) 相关，但 R25 从不同角度提出。\"\n  action_items:\n    - round: 25\n      action: \"考虑在 Figure 1 或新 Figure 中添加具体的 masking 过程示例\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M5\"\n  summary: \"Schema coverage gap 对 schema evolution 场景的影响未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R2-M6+R1 AGREE。Empirical constraints 0.6-1.0% 未覆盖 valid type pairs。新增实体类型或关系时 constraints 会 over-restrict。Limitations 应简短提及。\"\n  action_items:\n    - round: 25\n      action: \"Limitations 或 Discussion 加 1-2 句 schema evolution caveat\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Carried from prior rounds — status updated for R25\n# ============================================================\n\n- id: \"R24-SF1\"\n  summary: \"缺乏 OntoCoDec 作为 constraint enforcement method 的明确定位声明\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2-N2, R1 rebut 部分有效。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 未作为独立 issue 提出，但 §1 已有 'orthogonal and complementary' 定位。与 R25-N2 (GoLLIE 比较公平性) 相关。\"\n  action_items:\n    - round: 24\n      action: \"§1 加定位声明\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-SF2\"\n  summary: \"R-F1 41-47% 在正文中缺乏 LLM-based generative RE 上下文定位\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"正文缺上下文。\"\n    - round: 25\n      note: \"R25 未单独提出。§5 Setup 已有 'R-F1 range (41-47% under LoRA) is consistent with recent LLM-based generative RE benchmarks' 定位。可能已部分修复。\"\n  action_items:\n    - round: 24\n      action: \"§5 Setup 加 1-2 句 LLM-based generative RE 典型 F1 范围定位\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W12\"\n  summary: \"First-seen semantics 级联错误影响未量化\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"§3.3 formalize + Limitations 加 entity-first 约束。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-SF4。要求数据量化。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R1 在 §5.1 Cross-field violation analysis 中注意到论文已报告 cascade error 数据 (correct locks 2.5× more frequent than cascade errors, 7.3%)。R2 未单独提出。可能已部分修复——需确认正文中数据是否充分。\"\n  action_items:\n    - round: 24\n      action: \"Agent 分析 245 CF violations 中 first-seen 级联 vs 合法歧义分解\"\n      assigned_to: main_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-SF5\"\n  summary: \"§7 Discussion 过于压缩——缺 DR↔CF trade-off 等讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"需压缩 §6 释放空间。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 与 R25-W1 (CF trade-off 讨论不足) 直接相关。§7 仍仅约 0.5 页。需扩展 DR↔CF trade-off、per-triple vs global enforcement、training-based complementarity 讨论。\"\n  action_items:\n    - round: 24\n      action: \"压缩 §6 + §7 扩展为 3 段\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 25\n      action: \"§7 扩展 CF 实际影响分析 + beam search 推荐\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-SF7\"\n  summary: \"LoRA 超参从 SciERC 直接转移到 DocRED 缺乏论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"DDL 内无法补实验，承认限制。\"\n    - round: 25\n      note: \"R25 未单独提出。Limitations 已有 'LoRA hyperparameters were tuned on SciERC and transferred to DocRED without dataset-specific optimization, which may underestimate DocRED potential'。可能已修复。\"\n  action_items:\n    - round: 24\n      action: \"§5 Setup + Limitations 承认超参转移限制\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W2\"\n  summary: \"算法创新有限——主要是 XGrammar + stateful logits processor 的系统集成\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"降低 Proposition 1 强度。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"合并到 R16-W5/MF1。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 R1(Excitement 3/5)+R2(Excitement 3/5) 一致：核心方案是现有 constrained decoding 的自然延伸，entity registry + dynamic masking 概念上非 surprising。论文价值主要在实证而非概念。与 R16-W5 紧密相关。\"\n  action_items:\n    - round: 25\n      action: \"合并到 R16-W5 处理——将论文重心从理论贡献转向实证贡献和工程设计\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior Rounds — Resolved (confirmed in R25 or earlier)\n# ============================================================\n\n- id: \"R23-W1\"\n  summary: \"CF 违规占残余违规 64%，与标题 'Type-Constrained IE' 形成 gap\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R24 未作为独立 weakness。R25 CF 讨论转向 zero-shot severity (R25-W1) 而非 title gap。\"\n  resolution_round: 24\n\n- id: \"R23-W3\"\n  summary: \"GoLLIE 对比不公平 + 缺少与训练基方法的系统性对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"§6 GoLLIE 段重写。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1 rebut 有效——已有三层对比。标 resolved。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 fresh review 重新发现并升级为 R25-N2 [Critical]。R24 的 'resolved' 判断错误——§6 重写和定位声明未解决 Appendix S 对比表的方法论不公平。合并到 R25-N2。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W6\"\n  summary: \"Zero-shot 实验占主文 ~3 页但 R-F1 仅 4-8%，篇幅分配失衡\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R24 未提及。R25 未提及。压缩有效。\"\n  resolution_round: 24\n\n- id: \"R23-W7\"\n  summary: \"Proposition 1 实际意义论证 gap\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      note: \"合并到 R16-W5。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W8\"\n  summary: \"'Empirical enabling dependency' 重复 ≥6 次\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R24/R25 均未提及。修复有效。\"\n  resolution_round: 24\n\n- id: \"R23-W9\"\n  summary: \"Fallback 频率模型依赖性未在正文讨论\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R24/R25 均未作为独立 issue。R25 R1-S6 还肯定了 fallback causal tracing (Appendix C)。\"\n  resolution_round: 24\n\n- id: \"R23-W10\"\n  summary: \"Continuation masking prefix collision 频率未量化\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      note: \"R25 R1-Q3 追问了 morphologically similar types 的失败率。未被 R25 列为 weakness 但作为 question 保留。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W11\"\n  summary: \"Beam width sensitivity 讨论不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      note: \"R25 未单独提出。论文 §5 已有 beam sweep (k∈{1,2,4,8})，R1-S2 肯定了 beam search 评估。可能已修复。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-D1\"\n  summary: \"Limitations 长度是否 excessive\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R24/R25 均评 Limitations 充分。R25 R2-S3 特别肯定了三段式 Limitations 的透明度。\"\n  resolution_round: 24\n\n- id: \"R16-MF3\"\n  summary: \"CF trade-off 在 Abstract 中 framing 偏乐观\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  resolution: \"Abstract CF 分层报告。R25 仍有相关问题(R25-W1)但性质不同——不是隐瞒 CF 而是叙事不对称。\"\n  resolution_round: 22\n\n- id: \"R16-W4\"\n  summary: \"70B AWQ INT4 quantization 对约束效果的影响未隔离\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 21\n  resolution: \"Appendix R 4 组配置验证。R25 R1-S4 肯定了 quantization robustness 验证。\"\n  resolution_round: 22\n\n- id: \"R16-W3\"\n  summary: \"WikiEvents fine-tuning composability 仅 n=20 文档\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      note: \"合并到 R23-W4。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出至第 9 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  resolution: \"R25 格式检查确认主文 §1-§7 在 page 1-8。\"\n  resolution_round: 22\n\n- id: \"R18-M2\"\n  summary: \"Figure 1 视觉层次不够分明\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      note: \"R25 Visual Check info: Figure 1 内部组件标注文字偏小(约正文 60%)。R2-M4 要求端到端 running example。问题从'视觉层次'转为'缺少具体示例'。合并到 R25-M4。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W1\"\n  summary: \"Proposition 1 证明中 position→name 转换缺乏形式论证\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      note: \"R25 R1 小问题中提到 Appendix O proof Case 1 的 position vs. name-based 区分不够清晰。问题仍存在但严重程度低。合并到 R16-W5。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W4\"\n  summary: \"主文 Related Work §6 过于精简\"\n  category: related_work\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 23\n  resolution: \"R25 R2-S5 肯定 Related Work 三轴组织清晰有效。无关精简问题。\"\n  resolution_round: 23\n\n- id: \"R24-SF6\"\n  summary: \"Contribution 2 过度打包\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      note: \"R25 仍见 Contribution 2 包含多项内容。合并到 R23-W5 处理。\"\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Won't Fix\n# ============================================================\n\n- id: \"R20-W5\"\n  summary: \"Running example 仍不充分\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"空间限制无法在正文加完整 running example。R25-M4 从不同角度重新提出。\"\n  resolution_round: 20\n\n- id: \"R20-W6\"\n  summary: \"Zero-shot 评估实际意义有限（R-F1 仅 4-8%）\"\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 23\n  resolution: \"ZS 定位为 diagnostic probe。R25 未复发。\"\n  resolution_round: 23\n"
  }
}
```

</details>

---


### Tool result

_source line 2525 · 2026-05-23T10:46:42.765763+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml\", \"bytes\": 21328}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2526 · 2026-05-23T10:49:48.806273+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "report": "# Round 25 审稿报告 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**Target Venue**: EMNLP 2026 (ARR May cycle)\n**Reviewers**: R1（方法严谨性+实验设计）、R2（新颖性+完整性+写作质量）\n**轮次**: Round 1（fresh review，无上轮记忆）\n**收敛**: 1 轮交叉后收敛，5 个完全共识问题，1 个分歧已解决\n\n---\n\n## Summary\n\nOntoCoDec 提出将 IE 本体编译为两层 token-level 解码约束的框架：grammar layer 通过 XGrammar 保证 JSON 结构和词汇约束（Level 1: context-free），semantic layer 通过运行时 entity registry + dynamic logit masking 保证 domain/range 类型约束（Level 2: prefix-decidable with state）。核心理论贡献是 Proposition 1（pumping lemma 证明 domain/range 约束超出 CFG 表达能力）。实验覆盖 3 个 8B 模型族（Qwen3-8B, Llama-3.1-8B, Mistral-7B）× 2 个 RE 数据集（SciERC, DocRED），加 1 个 70B 单模型族验证（Llama-3.1-70B AWQ INT4）和 WikiEvents event extraction pilot（n=20）。在 zero-shot 和 LoRA fine-tuning 两种设置下，DR 违规几乎完全消除（fine-tuned ≤0.09%），但引入 CF 违规作为 trade-off。\n\n---\n\n## Strengths\n\n**S1.** [共识] 实验设计极为扎实——本文最大亮点。五路 ablation on SciERC（Table 1: unconstrained / grammar-only / GCD-equiv / semantic-only / S1 / S2）清晰解剖了每层的独立与交互贡献。GCD-equiv 通过 vLLM `guided_json` 外部验证（Appendix S）增强可信度。跨模型验证（3 tokenizer families × 2 datasets）、fine-tuning composability（Table 2, Bonferroni-corrected CIs）、beam search sweep（k∈{1,2,4,8}）、downstream impact 分析（仅 0.49% blocked triples match gold labels）均展现了罕见的实验严谨性。\n\n**S2.** [共识] 统计方法严谨。Bootstrap CI（10,000 iterations）、Bonferroni correction for multiple comparisons、Cohen's d effect sizes 的使用在 NLP 论文中不常见。per-configuration corrected p-values 的诚实报告（如 SciERC p_adj=1.00）值得肯定。\n\n**S3.** [共识] Limitations 的透明度异常高。三段式 Limitations 覆盖 constraint scope / evaluation coverage / engineering considerations，主动报告了 CF trade-off、n=3 tightness 相关性不显著、WikiEvents n=20 统计效力不足、70B 单一模型族限制等。这种自我批评的态度显著提高了论文可信度。\n\n**S4.** [共识] 工程完整性强。31 页 Appendix 覆盖了几乎所有可预见的质疑：causal tracing、cascade error analysis、order invariance、prompt sensitivity、document length effect、quantization robustness、sampling robustness。跨 3 个 tokenizer family 的 continuation masking 验证了 tokenizer-agnostic 设计。Grammar-first fallback 机制优先保证 JSON 结构完整性的设计哲学符合实际部署需求。\n\n**S5.** [共识] 问题定义精准且有实际意义。论文清晰识别了 grammar-constrained decoding 的能力边界——无法执行跨字段 domain/range 类型约束——并给出了形式化论证。15-18% 的 baseline violation rate 证实了问题的实际严重性。\n\n**S6.** [R2] 写作质量高。8 页正文在高信息密度下保持了良好的逻辑流；符号使用一致（DR/RV/ET/CF 始终如一）；Related Work 的三轴组织（constrained decoding / schema-aware IE / constraint enforcement in IE）清晰有效。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [Critical, 完全共识] **WikiEvents n=20 不足以支撑 \"task generalization\" contribution claim**\n- §1 Contribution 2 将 WikiEvents pilot 列为贡献一部分：\"a preliminary n=20 event extraction pilot provides directional evidence of task generalization\"。n=20, MDE≈±5.0pp 不构成 generalization 证据，属 feasibility demonstration 而非 validation。零样本 WikiEvents 评估（n=246, Table 47）验证了 EV/RoV 消除，有价值；但 fine-tuning composability 的 n=20 无法支撑有置信度的结论。\n- **要求**: 从 Contribution 2 完全删除 WikiEvents 表述；§5.2 移至 Appendix 或正文仅保留 1 句 feasibility mention。\n\n**MF2** [Critical, 完全共识] **GoLLIE 比较方法论不公平，但被用于定位论文差异化**\n- Appendix S 对比 GoLLIE-7B zero-shot（5 predicted relations / 100 docs）vs. OntoCoDec LoRA+S1（~1100 predicted relations）。§6 引用此结论（\"near-complete output suppression\"）定位差异化，但实验条件不对等——GoLLIE 未在 SciERC 训练导致输出少，非方法内在差异。论文的\"complementary\"定位合理，但 Appendix S 的直接对比表支撑不了这个定位。\n- **要求**: 删除 Appendix S 直接对比表，改为定性讨论；§6 删除或显著限定\"near-complete output suppression\"表述，并显著说明不可比原因。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [Major, 完全共识] **κ-DR 相关性（n=3）在正文 §4 叙事权重过高**\n- §4 \"Constraint Tightness\" 段为 κ 给出了独立定义式、三个 schema 的具体数值、p=0.138，Appendix 有独立 case study 和 Figure 3。叙事权重与 n=3 证据强度严重不匹配。κ 还是 confounded variable（entity type confusability 是 co-factor）。论文已标注\"descriptive\"但展示比重暗示 κ 有独立解释力。\n- R1 初评 Critical，R2 交叉后建议降为 Major（因未列入 Contribution），Director 采纳 Major。\n- **要求**: §4 Constraint Tightness 压缩为 1-2 句描述性观察，删除 p 值报告（n=3 的 p 值本身误导），详细分析移 Appendix。\n\n**SF2** [Major, 完全共识] **Proposition 1 新颖性有限——formalizing known intuition**\n- PDA 无法执行 random-access stack lookup 是形式语言理论基本知识。论文诚实称之为\"formalizing a known intuition\"（§1 C1），但仍列为三大贡献之首，§3 投入大量篇幅（proof sketch + engineering applicability + empirical observation）。Appendix O pumping lemma 证明正确但不深刻——构造了 copy-language 变体。Engineering applicability（DFA 6^17 states）比 Proposition 1 本身更有价值。\n- **要求**: 降低 Proposition 1 展示权重——从 Contribution 首位降级，或将 engineering applicability 作为主要论述重心。\n\n**SF3** [Major, 完全共识] **DR↔CF trade-off 在零样本场景下严重程度讨论不足**\n- Zero-shot greedy S1: total violation 15.45%→10.83%（DR↓94% 但 CF 0.08%→9.90%），净降幅仅 30%。Abstract 突出 DR reduction 但 CF increase 叙事不对称。R2 补充：(1) Abstract 确实提及 zero-shot CF 可达 12%；(2) DR/CF 质性差异真实（DR 不可恢复 vs CF 可 post-hoc）；(3) 推荐配置 fine-tuned+beam 下 trade-off 很小。\n- R1 初评 Critical，R2 交叉后提供 nuance 建议降为 Major，Director 采纳 Major。\n- **要求**: Abstract framing 更对称地报告 DR reduction 和 CF increase；§7 Discussion 扩展 zero-shot CF 实际影响分析；明确推荐 beam k≥2 作为 zero-shot 部署配置。\n\n**SF4** [Major, 完全共识] **70B 验证单一模型族但 Contribution 3 称\"scale validation\"**\n- 所有 70B 实验仅 Llama-3.1-70B AWQ INT4，无 Qwen-72B/Mistral-Large，无 FP16 对比。Scale-dependent interaction（semantic-only 24%→84%）是否为 Llama-specific 未知。论文已标 \"single-family\" 但仍用\"validation\"一词。\n- **要求**: Contribution 3 改\"Preliminary 70B exploration\"或\"Single-model scale probe\"，不用\"validation\"。\n\n**SF5** [Major, R1 提出 R2 同意] **Scale-dependent layer interaction 缺乏因果解释**\n- Semantic-only 在 8B 仅 24% DR reduction vs. 70B 达 84%，论文仅称\"empirical observation\"无因果解释。候选假设（vocabulary calibration / logit distribution / fallback 频率差异）均未讨论。现有数据（Appendix C fallback tracing）应可提供部分解释但未连接。\n- **要求**: §3 或 §5 添加 1-2 句关于可能机制的讨论，至少分析 8B vs 70B semantic-only 下的 fallback 频率差异。\n\n**SF6** [Major, R1 提出 R2 同意] **S1 vs S2 对比缺乏深入分析**\n- S1 vs S2 差异未做统计检验。70B 下 S2 R-F1 降低 8.45pp 的具体原因未分析。S2 何时优于 S1 无指导。R2 注：S1/S2 是次要叙事，Major 但不影响接收。\n- **要求**: 提供 S1 vs S2 paired bootstrap test；分析 70B S2 failure case；讨论 S2 推荐条件。\n\n### Minor\n\n**M1** [R1 提出 R2 rebut，R2 论点有效] Fine-tuning 仅验证 LoRA。R2 指出 full FT 已在 Appendix 验证，且 composability 机制上不依赖 fine-tuning 方法。Limitations 中 caveat 可适当加强。\n\n---\n\n## Reviewer Consensus（[AGREE] 标注）\n\n以下问题两位 Reviewer 完全一致：\n\n1. **WikiEvents n=20 从 Contribution 降级** — R1-W5 [Major] + R2-N1 [Critical]，R1 交叉 AGREE R2。升级为 Critical。\n2. **GoLLIE 比较方法论不公平** — R2-N2 [Critical] + R1-W6 [Minor]，R1 交叉 AGREE R2 并补充 nuance。升级为 Critical。\n3. **Proposition 1 新颖性有限** — R1-W1 [Major] + R2-W1 [Major]，双方交叉 AGREE。\n4. **κ-DR 相关性叙事权重过高** — R1-N1 + R2-W4，双方交叉 AGREE。\n5. **CF trade-off 讨论不足** — R1-N2 + R2-W3，双方交叉 AGREE（含 nuance）。\n6. **70B 单一模型族 overclaim \"validation\"** — R2-W2 [Major]，R1 交叉 AGREE。\n7. **Scale-dependent interaction 缺因果解释** — R1-W2 [Major]，R2 交叉 AGREE。\n8. **S1 vs S2 分析不足** — R1-W4 [Major]，R2 交叉 AGREE。\n\n## Reviewer Divergence（[REBUT] 标注）\n\n**唯一分歧：LoRA-only composability**\n- R1 认为仅验证 LoRA 是 Major 缺陷，composability claim 泛化性不足。\n- R2 [REBUT]：Full fine-tuning 已在 Appendix 验证；composability 机制不依赖 fine-tuning 方法（runtime logit masking 对模型权重来源不可知）；不同 PEFT 方法改变权重不改变 logits 生成方式。\n- **Director 裁定**：R2 的 rebut 有效。已验证两种 fine-tuning 方法（LoRA + full FT），且机制论证成立。降为 Minor，在 Limitations 加强 caveat 即可。\n\n---\n\n## Questions for Authors\n\n**Q1.** Schema coverage gaps 占 fine-tuning residual DR 的 33%。当 training data 的 type pair 分布不覆盖所有合法 ontology pair 时，系统会 over-restrict。能否量化 SciERC 和 DocRED 的 schema 对 ground truth ontology 的覆盖率？是否考虑过基于 ontology hierarchy 构建 constraint？\n\n**Q2.** Entity registry 的 first-seen semantics 在长文档中的行为如何？DocRED outlier 文档的 entity 数可达多少？registry 在 100+ entities 时是否有实测性能数据？\n\n**Q3.** Continuation masking 对 morphologically similar types（如 Protein vs. Protein_Complex）的实际失败率？\n\n**Q4.** 在 R-F1 仅 8-13% 的 zero-shot 设置中，violation reduction 的实际下游价值如何量化？\n\n**Q5.** Proposition 1 是否已在其他文献中以类似形式出现过？与已有 cross-serial dependency 不可由 CFG 表达的结论的本质区别？\n\n**Q6.** GoLLIE-7B 在 LoRA fine-tuning 后的 SciERC 表现如何？如果 GoLLIE fine-tuned 后输出量正常化但仍保持低 DR，则 OntoCoDec 的差异化需要重新评估。\n\n**Q7.** Scale-dependent layer interaction（semantic-only 70B 84% vs. 8B 24%）是否有理论预期支持？70B 模型更好的 vocabulary calibration 是否解释了 semantic layer 的独立有效性？\n\n---\n\n## Missing References\n\n论文对关键相关工作的覆盖充分。CRANE (Banerjee et al., 2025)、EnriCo (Zaratiana et al., 2024)、IterGen (Ugare et al., 2025)、SynCode、XGrammar、Outlines、SGLang、PICARD、KG-Trie、GoLLIE、KnowCoder、GCD、BoostCD 均已引用。\n\n唯一建议：CRANE 仅在 Appendix B 讨论，但 S2 在 70B 下 R-F1 降低 8.45pp 与 CRANE 关于 constrained decoding 抑制 reasoning 的分析直接相关，应在主文 §3.4 或 §5 70B 段至少引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时 ~4.5 分钟）\n\n**Warnings (3)**:\n1. 主文 8 页仅 3 个 display items（1 figure + 2 tables），对于实证型论文偏少（通常 5-8 个）。大量实验结果全部推入附录，审稿人在主文中缺乏足够的视觉锚点。建议将至少 1-2 个关键结果表或 ablation 图提至主文。\n2. Method 段（§3.1-3.3）连续 2 页纯文本，无 figure/table/algorithm box 穿插。建议用 Algorithm 伪代码或流程图打断文字墙。\n3. Related Work + Discussion/Conclusion 合占 1 页纯文本，无总结性图表辅助审稿人抓取核心 takeaway。\n\n**Info (7)**:\n- Table 35 红/绿对比对色盲用户不友好\n- 末页内容填充约 60-65%\n- Figure 1 内部标注文字偏小（约正文 60%）\n- 多页附录堆叠 4 张表格，可考虑合并\n- Table 1/2 格式专业（booktabs + 加粗最优值 + 小数位一致）✓\n- Table 3 prompt 模板文字较小但可接受\n- 附录 Figure 2/3/4 分辨率和轴标签清晰 ✓\n\n---\n\n## Overall Assessment\n\n**Overall: 3.5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 4/5 | 3.75 |\n| Excitement | 3/5 | 3/5 | 3.0 |\n| Reproducibility | 4/5 | 4/5 | 4.0 |\n| Confidence | 4/5 | 4/5 | 4.0 |\n| **Overall** | **3.5** | **3.5** | **3.5** |\n\n**判断依据**：论文解决了一个有实际意义的问题（LLM-based IE 中 15-18% 的本体违规率），提出了干净的两层架构，配有正确的理论证明和极其全面的消融实验。统计方法（bootstrap CI, Bonferroni, Cohen's d）在 NLP 论文中罕见且值得肯定。31 页 Appendix 和三段式 Limitations 的透明度是显著优势。\n\n主要不足：(1) 核心技术新颖性中等——entity registry + dynamic masking 是现有 constrained decoding 的自然延伸，Proposition 1 是已知结论在 IE 场景的应用（Excitement 3/5）；(2) 两个关键实验证据有缺陷——WikiEvents n=20 不支撑 task generalization claim，GoLLIE 比较方法论不公平；(3) 零样本场景下 DR→CF trade-off 的净效果被叙事不对称地呈现。\n\n**Findings vs. Conference 的关键判断维度**：论文的实验质量和透明度足以被 Findings 接收。是否能进入主会议取决于对\"扎实的工程+实验贡献 vs. 有限的概念新颖性\"的权衡。若 MF1（WikiEvents framing）和 MF2（GoLLIE 比较公平性）在 revision 中修复，且 SF2（Proposition 1 展示权重）和 SF3（CF trade-off 对称呈现）得到改善，评分有望上调至 3.5-4.0 区间。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 1：Proposition 1 定位为\"formalizing a known intuition\"是诚实的，但列为首位贡献且 §3 篇幅过大，给人 substantial theoretical contribution 的印象。建议降级或重新排序。\n- Contribution 2：WikiEvents 部分应完全删除。\n- Contribution 3：\"Single-family scale validation\"中\"validation\"应改为\"exploration\"或\"probe\"。\n- \"F1 41-47%\"：Table 2 Qwen DocRED S1 R-F1=40.79%，低于 41%。修正为\"R-F1 40-47%\"。\n\n### §3 Method\n- Proposition 1 proof sketch 技术正确，但不深刻。Engineering applicability（DFA 6^17 states）比 Proposition 1 本身更 informative。\n- §3.1 \"100% preservation across all configurations\"表述不清，建议改为\"entity-before-relation ordering is maintained in all N documents across all configurations\"。\n- Continuation masking 设计合理，跨 3 个 tokenizer family 验证了 tokenizer-agnostic 性。\n\n### §4 Constraint Composition\n- Constraint Tightness 段落应压缩为 1-2 句。删除 p=0.138 报告（n=3 的 p 值本身误导）。κ 作为描述性工具仍有概念价值，但详细分析应在 Appendix。\n\n### §5 Experiments\n- 五路 ablation（Table 1）是论文最强的实验贡献。\n- Cross-field violation analysis（§5.1）数据充分：cascade error 分解（7.3% cascade vs. 2.5× correct locks）是有力证据。\n- Fine-tuning composability（Table 2）报告严谨。\n- §5.2 WikiEvents：正文应压缩至 1 句或移至 Appendix。\n- 70B results：scale-dependent interaction 需因果讨论；S2 在 70B 的降级应引用 CRANE。\n- DocRED 使用 dev set 的说明应从 footnote 1 提升至 Setup 段正文。\n\n### §6 Related Work\n- 三轴组织有效。\n- GoLLIE 段应删除或显著限定\"near-complete output suppression\"表述。\n- CRANE 应在主文提及，不仅限于 Appendix B。\n\n### §7 Discussion and Conclusion\n- 目前约 0.5 页，过于压缩。需扩展：DR↔CF trade-off 实际影响、per-triple vs. global enforcement 路线图、schema evolution 考量。\n\n### Limitations\n- 三段式结构充分，覆盖面好。\n- 建议加强 fine-tuning 方法泛化性的 caveat（不仅\"other fine-tuning methods warrant further investigation\"，应指出不同 PEFT 方法对 logit distribution 的影响可能不同）。\n- 添加 schema evolution 对 empirical constraints 的影响讨论。\n\n### Format Compliance (EMNLP 2026)\n- ✅ 正文 8 页（§1-§7 在 pages 1-8）\n- ✅ 匿名处理（Anonymous ACL submission，无身份泄露）\n- ✅ Limitations section 存在且充分\n- ✅ Ethics statement 存在\n- ✅ References ACL natbib 格式\n- ✅ \\usepackage[review]{acl} 启用 review 模式"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "report": "# Round 25 审稿报告 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**Target Venue**: EMNLP 2026 (ARR May cycle)\n**Reviewers**: R1（方法严谨性+实验设计）、R2（新颖性+完整性+写作质量）\n**轮次**: Round 1（fresh review，无上轮记忆）\n**收敛**: 1 轮交叉后收敛，5 个完全共识问题，1 个分歧已解决\n\n---\n\n## Summary\n\nOntoCoDec 提出将 IE 本体编译为两层 token-level 解码约束的框架：grammar layer 通过 XGrammar 保证 JSON 结构和词汇约束（Level 1: context-free），semantic layer 通过运行时 entity registry + dynamic logit masking 保证 domain/range 类型约束（Level 2: prefix-decidable with state）。核心理论贡献是 Proposition 1（pumping lemma 证明 domain/range 约束超出 CFG 表达能力）。实验覆盖 3 个 8B 模型族（Qwen3-8B, Llama-3.1-8B, Mistral-7B）× 2 个 RE 数据集（SciERC, DocRED），加 1 个 70B 单模型族验证（Llama-3.1-70B AWQ INT4）和 WikiEvents event extraction pilot（n=20）。在 zero-shot 和 LoRA fine-tuning 两种设置下，DR 违规几乎完全消除（fine-tuned ≤0.09%），但引入 CF 违规作为 trade-off。\n\n---\n\n## Strengths\n\n**S1.** [共识] 实验设计极为扎实——本文最大亮点。五路 ablation on SciERC（Table 1: unconstrained / grammar-only / GCD-equiv / semantic-only / S1 / S2）清晰解剖了每层的独立与交互贡献。GCD-equiv 通过 vLLM `guided_json` 外部验证（Appendix S）增强可信度。跨模型验证（3 tokenizer families × 2 datasets）、fine-tuning composability（Table 2, Bonferroni-corrected CIs）、beam search sweep（k∈{1,2,4,8}）、downstream impact 分析（仅 0.49% blocked triples match gold labels）均展现了罕见的实验严谨性。\n\n**S2.** [共识] 统计方法严谨。Bootstrap CI（10,000 iterations）、Bonferroni correction for multiple comparisons、Cohen's d effect sizes 的使用在 NLP 论文中不常见。per-configuration corrected p-values 的诚实报告（如 SciERC p_adj=1.00）值得肯定。\n\n**S3.** [共识] Limitations 的透明度异常高。三段式 Limitations 覆盖 constraint scope / evaluation coverage / engineering considerations，主动报告了 CF trade-off、n=3 tightness 相关性不显著、WikiEvents n=20 统计效力不足、70B 单一模型族限制等。这种自我批评的态度显著提高了论文可信度。\n\n**S4.** [共识] 工程完整性强。31 页 Appendix 覆盖了几乎所有可预见的质疑：causal tracing、cascade error analysis、order invariance、prompt sensitivity、document length effect、quantization robustness、sampling robustness。跨 3 个 tokenizer family 的 continuation masking 验证了 tokenizer-agnostic 设计。Grammar-first fallback 机制优先保证 JSON 结构完整性的设计哲学符合实际部署需求。\n\n**S5.** [共识] 问题定义精准且有实际意义。论文清晰识别了 grammar-constrained decoding 的能力边界——无法执行跨字段 domain/range 类型约束——并给出了形式化论证。15-18% 的 baseline violation rate 证实了问题的实际严重性。\n\n**S6.** [R2] 写作质量高。8 页正文在高信息密度下保持了良好的逻辑流；符号使用一致（DR/RV/ET/CF 始终如一）；Related Work 的三轴组织（constrained decoding / schema-aware IE / constraint enforcement in IE）清晰有效。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [Critical, 完全共识] **WikiEvents n=20 不足以支撑 \"task generalization\" contribution claim**\n- §1 Contribution 2 将 WikiEvents pilot 列为贡献一部分：\"a preliminary n=20 event extraction pilot provides directional evidence of task generalization\"。n=20, MDE≈±5.0pp 不构成 generalization 证据，属 feasibility demonstration 而非 validation。零样本 WikiEvents 评估（n=246, Table 47）验证了 EV/RoV 消除，有价值；但 fine-tuning composability 的 n=20 无法支撑有置信度的结论。\n- **要求**: 从 Contribution 2 完全删除 WikiEvents 表述；§5.2 移至 Appendix 或正文仅保留 1 句 feasibility mention。\n\n**MF2** [Critical, 完全共识] **GoLLIE 比较方法论不公平，但被用于定位论文差异化**\n- Appendix S 对比 GoLLIE-7B zero-shot（5 predicted relations / 100 docs）vs. OntoCoDec LoRA+S1（~1100 predicted relations）。§6 引用此结论（\"near-complete output suppression\"）定位差异化，但实验条件不对等——GoLLIE 未在 SciERC 训练导致输出少，非方法内在差异。论文的\"complementary\"定位合理，但 Appendix S 的直接对比表支撑不了这个定位。\n- **要求**: 删除 Appendix S 直接对比表，改为定性讨论；§6 删除或显著限定\"near-complete output suppression\"表述，并显著说明不可比原因。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [Major, 完全共识] **κ-DR 相关性（n=3）在正文 §4 叙事权重过高**\n- §4 \"Constraint Tightness\" 段为 κ 给出了独立定义式、三个 schema 的具体数值、p=0.138，Appendix 有独立 case study 和 Figure 3。叙事权重与 n=3 证据强度严重不匹配。κ 还是 confounded variable（entity type confusability 是 co-factor）。论文已标注\"descriptive\"但展示比重暗示 κ 有独立解释力。\n- R1 初评 Critical，R2 交叉后建议降为 Major（因未列入 Contribution），Director 采纳 Major。\n- **要求**: §4 Constraint Tightness 压缩为 1-2 句描述性观察，删除 p 值报告（n=3 的 p 值本身误导），详细分析移 Appendix。\n\n**SF2** [Major, 完全共识] **Proposition 1 新颖性有限——formalizing known intuition**\n- PDA 无法执行 random-access stack lookup 是形式语言理论基本知识。论文诚实称之为\"formalizing a known intuition\"（§1 C1），但仍列为三大贡献之首，§3 投入大量篇幅（proof sketch + engineering applicability + empirical observation）。Appendix O pumping lemma 证明正确但不深刻——构造了 copy-language 变体。Engineering applicability（DFA 6^17 states）比 Proposition 1 本身更有价值。\n- **要求**: 降低 Proposition 1 展示权重——从 Contribution 首位降级，或将 engineering applicability 作为主要论述重心。\n\n**SF3** [Major, 完全共识] **DR↔CF trade-off 在零样本场景下严重程度讨论不足**\n- Zero-shot greedy S1: total violation 15.45%→10.83%（DR↓94% 但 CF 0.08%→9.90%），净降幅仅 30%。Abstract 突出 DR reduction 但 CF increase 叙事不对称。R2 补充：(1) Abstract 确实提及 zero-shot CF 可达 12%；(2) DR/CF 质性差异真实（DR 不可恢复 vs CF 可 post-hoc）；(3) 推荐配置 fine-tuned+beam 下 trade-off 很小。\n- R1 初评 Critical，R2 交叉后提供 nuance 建议降为 Major，Director 采纳 Major。\n- **要求**: Abstract framing 更对称地报告 DR reduction 和 CF increase；§7 Discussion 扩展 zero-shot CF 实际影响分析；明确推荐 beam k≥2 作为 zero-shot 部署配置。\n\n**SF4** [Major, 完全共识] **70B 验证单一模型族但 Contribution 3 称\"scale validation\"**\n- 所有 70B 实验仅 Llama-3.1-70B AWQ INT4，无 Qwen-72B/Mistral-Large，无 FP16 对比。Scale-dependent interaction（semantic-only 24%→84%）是否为 Llama-specific 未知。论文已标 \"single-family\" 但仍用\"validation\"一词。\n- **要求**: Contribution 3 改\"Preliminary 70B exploration\"或\"Single-model scale probe\"，不用\"validation\"。\n\n**SF5** [Major, R1 提出 R2 同意] **Scale-dependent layer interaction 缺乏因果解释**\n- Semantic-only 在 8B 仅 24% DR reduction vs. 70B 达 84%，论文仅称\"empirical observation\"无因果解释。候选假设（vocabulary calibration / logit distribution / fallback 频率差异）均未讨论。现有数据（Appendix C fallback tracing）应可提供部分解释但未连接。\n- **要求**: §3 或 §5 添加 1-2 句关于可能机制的讨论，至少分析 8B vs 70B semantic-only 下的 fallback 频率差异。\n\n**SF6** [Major, R1 提出 R2 同意] **S1 vs S2 对比缺乏深入分析**\n- S1 vs S2 差异未做统计检验。70B 下 S2 R-F1 降低 8.45pp 的具体原因未分析。S2 何时优于 S1 无指导。R2 注：S1/S2 是次要叙事，Major 但不影响接收。\n- **要求**: 提供 S1 vs S2 paired bootstrap test；分析 70B S2 failure case；讨论 S2 推荐条件。\n\n### Minor\n\n**M1** [R1 提出 R2 rebut，R2 论点有效] Fine-tuning 仅验证 LoRA。R2 指出 full FT 已在 Appendix 验证，且 composability 机制上不依赖 fine-tuning 方法。Limitations 中 caveat 可适当加强。\n\n---\n\n## Reviewer Consensus（[AGREE] 标注）\n\n以下问题两位 Reviewer 完全一致：\n\n1. **WikiEvents n=20 从 Contribution 降级** — R1-W5 [Major] + R2-N1 [Critical]，R1 交叉 AGREE R2。升级为 Critical。\n2. **GoLLIE 比较方法论不公平** — R2-N2 [Critical] + R1-W6 [Minor]，R1 交叉 AGREE R2 并补充 nuance。升级为 Critical。\n3. **Proposition 1 新颖性有限** — R1-W1 [Major] + R2-W1 [Major]，双方交叉 AGREE。\n4. **κ-DR 相关性叙事权重过高** — R1-N1 + R2-W4，双方交叉 AGREE。\n5. **CF trade-off 讨论不足** — R1-N2 + R2-W3，双方交叉 AGREE（含 nuance）。\n6. **70B 单一模型族 overclaim \"validation\"** — R2-W2 [Major]，R1 交叉 AGREE。\n7. **Scale-dependent interaction 缺因果解释** — R1-W2 [Major]，R2 交叉 AGREE。\n8. **S1 vs S2 分析不足** — R1-W4 [Major]，R2 交叉 AGREE。\n\n## Reviewer Divergence（[REBUT] 标注）\n\n**唯一分歧：LoRA-only composability**\n- R1 认为仅验证 LoRA 是 Major 缺陷，composability claim 泛化性不足。\n- R2 [REBUT]：Full fine-tuning 已在 Appendix 验证；composability 机制不依赖 fine-tuning 方法（runtime logit masking 对模型权重来源不可知）；不同 PEFT 方法改变权重不改变 logits 生成方式。\n- **Director 裁定**：R2 的 rebut 有效。已验证两种 fine-tuning 方法（LoRA + full FT），且机制论证成立。降为 Minor，在 Limitations 加强 caveat 即可。\n\n---\n\n## Questions for Authors\n\n**Q1.** Schema coverage gaps 占 fine-tuning residual DR 的 33%。当 training data 的 type pair 分布不覆盖所有合法 ontology pair 时，系统会 over-restrict。能否量化 SciERC 和 DocRED 的 schema 对 ground truth ontology 的覆盖率？是否考虑过基于 ontology hierarchy 构建 constraint？\n\n**Q2.** Entity registry 的 first-seen semantics 在长文档中的行为如何？DocRED outlier 文档的 entity 数可达多少？registry 在 100+ entities 时是否有实测性能数据？\n\n**Q3.** Continuation masking 对 morphologically similar types（如 Protein vs. Protein_Complex）的实际失败率？\n\n**Q4.** 在 R-F1 仅 8-13% 的 zero-shot 设置中，violation reduction 的实际下游价值如何量化？\n\n**Q5.** Proposition 1 是否已在其他文献中以类似形式出现过？与已有 cross-serial dependency 不可由 CFG 表达的结论的本质区别？\n\n**Q6.** GoLLIE-7B 在 LoRA fine-tuning 后的 SciERC 表现如何？如果 GoLLIE fine-tuned 后输出量正常化但仍保持低 DR，则 OntoCoDec 的差异化需要重新评估。\n\n**Q7.** Scale-dependent layer interaction（semantic-only 70B 84% vs. 8B 24%）是否有理论预期支持？70B 模型更好的 vocabulary calibration 是否解释了 semantic layer 的独立有效性？\n\n---\n\n## Missing References\n\n论文对关键相关工作的覆盖充分。CRANE (Banerjee et al., 2025)、EnriCo (Zaratiana et al., 2024)、IterGen (Ugare et al., 2025)、SynCode、XGrammar、Outlines、SGLang、PICARD、KG-Trie、GoLLIE、KnowCoder、GCD、BoostCD 均已引用。\n\n唯一建议：CRANE 仅在 Appendix B 讨论，但 S2 在 70B 下 R-F1 降低 8.45pp 与 CRANE 关于 constrained decoding 抑制 reasoning 的分析直接相关，应在主文 §3.4 或 §5 70B 段至少引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时 ~4.5 分钟）\n\n**Warnings (3)**:\n1. 主文 8 页仅 3 个 display items（1 figure + 2 tables），对于实证型论文偏少（通常 5-8 个）。大量实验结果全部推入附录，审稿人在主文中缺乏足够的视觉锚点。建议将至少 1-2 个关键结果表或 ablation 图提至主文。\n2. Method 段（§3.1-3.3）连续 2 页纯文本，无 figure/table/algorithm box 穿插。建议用 Algorithm 伪代码或流程图打断文字墙。\n3. Related Work + Discussion/Conclusion 合占 1 页纯文本，无总结性图表辅助审稿人抓取核心 takeaway。\n\n**Info (7)**:\n- Table 35 红/绿对比对色盲用户不友好\n- 末页内容填充约 60-65%\n- Figure 1 内部标注文字偏小（约正文 60%）\n- 多页附录堆叠 4 张表格，可考虑合并\n- Table 1/2 格式专业（booktabs + 加粗最优值 + 小数位一致）✓\n- Table 3 prompt 模板文字较小但可接受\n- 附录 Figure 2/3/4 分辨率和轴标签清晰 ✓\n\n---\n\n## Overall Assessment\n\n**Overall: 3.5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 4/5 | 3.75 |\n| Excitement | 3/5 | 3/5 | 3.0 |\n| Reproducibility | 4/5 | 4/5 | 4.0 |\n| Confidence | 4/5 | 4/5 | 4.0 |\n| **Overall** | **3.5** | **3.5** | **3.5** |\n\n**判断依据**：论文解决了一个有实际意义的问题（LLM-based IE 中 15-18% 的本体违规率），提出了干净的两层架构，配有正确的理论证明和极其全面的消融实验。统计方法（bootstrap CI, Bonferroni, Cohen's d）在 NLP 论文中罕见且值得肯定。31 页 Appendix 和三段式 Limitations 的透明度是显著优势。\n\n主要不足：(1) 核心技术新颖性中等——entity registry + dynamic masking 是现有 constrained decoding 的自然延伸，Proposition 1 是已知结论在 IE 场景的应用（Excitement 3/5）；(2) 两个关键实验证据有缺陷——WikiEvents n=20 不支撑 task generalization claim，GoLLIE 比较方法论不公平；(3) 零样本场景下 DR→CF trade-off 的净效果被叙事不对称地呈现。\n\n**Findings vs. Conference 的关键判断维度**：论文的实验质量和透明度足以被 Findings 接收。是否能进入主会议取决于对\"扎实的工程+实验贡献 vs. 有限的概念新颖性\"的权衡。若 MF1（WikiEvents framing）和 MF2（GoLLIE 比较公平性）在 revision 中修复，且 SF2（Proposition 1 展示权重）和 SF3（CF trade-off 对称呈现）得到改善，评分有望上调至 3.5-4.0 区间。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 1：Proposition 1 定位为\"formalizing a known intuition\"是诚实的，但列为首位贡献且 §3 篇幅过大，给人 substantial theoretical contribution 的印象。建议降级或重新排序。\n- Contribution 2：WikiEvents 部分应完全删除。\n- Contribution 3：\"Single-family scale validation\"中\"validation\"应改为\"exploration\"或\"probe\"。\n- \"F1 41-47%\"：Table 2 Qwen DocRED S1 R-F1=40.79%，低于 41%。修正为\"R-F1 40-47%\"。\n\n### §3 Method\n- Proposition 1 proof sketch 技术正确，但不深刻。Engineering applicability（DFA 6^17 states）比 Proposition 1 本身更 informative。\n- §3.1 \"100% preservation across all configurations\"表述不清，建议改为\"entity-before-relation ordering is maintained in all N documents across all configurations\"。\n- Continuation masking 设计合理，跨 3 个 tokenizer family 验证了 tokenizer-agnostic 性。\n\n### §4 Constraint Composition\n- Constraint Tightness 段落应压缩为 1-2 句。删除 p=0.138 报告（n=3 的 p 值本身误导）。κ 作为描述性工具仍有概念价值，但详细分析应在 Appendix。\n\n### §5 Experiments\n- 五路 ablation（Table 1）是论文最强的实验贡献。\n- Cross-field violation analysis（§5.1）数据充分：cascade error 分解（7.3% cascade vs. 2.5× correct locks）是有力证据。\n- Fine-tuning composability（Table 2）报告严谨。\n- §5.2 WikiEvents：正文应压缩至 1 句或移至 Appendix。\n- 70B results：scale-dependent interaction 需因果讨论；S2 在 70B 的降级应引用 CRANE。\n- DocRED 使用 dev set 的说明应从 footnote 1 提升至 Setup 段正文。\n\n### §6 Related Work\n- 三轴组织有效。\n- GoLLIE 段应删除或显著限定\"near-complete output suppression\"表述。\n- CRANE 应在主文提及，不仅限于 Appendix B。\n\n### §7 Discussion and Conclusion\n- 目前约 0.5 页，过于压缩。需扩展：DR↔CF trade-off 实际影响、per-triple vs. global enforcement 路线图、schema evolution 考量。\n\n### Limitations\n- 三段式结构充分，覆盖面好。\n- 建议加强 fine-tuning 方法泛化性的 caveat（不仅\"other fine-tuning methods warrant further investigation\"，应指出不同 PEFT 方法对 logit distribution 的影响可能不同）。\n- 添加 schema evolution 对 empirical constraints 的影响讨论。\n\n### Format Compliance (EMNLP 2026)\n- ✅ 正文 8 页（§1-§7 在 pages 1-8）\n- ✅ 匿名处理（Anonymous ACL submission，无身份泄露）\n- ✅ Limitations section 存在且充分\n- ✅ Ethics statement 存在\n- ✅ References ACL natbib 格式\n- ✅ \\usepackage[review]{acl} 启用 review 模式"
  }
}
```

</details>

---


### Tool result

_source line 2527 · 2026-05-23T10:49:52.975010+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2216d5b8b87a9472ce204aba11481390:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4168
}
```

</details>

---


### Assistant

_source line 2528 · 2026-05-23T10:50:06.546826+00:00_

审稿报告已投递。

**Round 25 审稿完成**。两位 Reviewer 评分一致：**Overall 3.5（Borderline Conference）**。

核心结论：
- **2 个 Must-Fix**：WikiEvents n=20 从 Contribution 降级（Critical）、GoLLIE 比较方法论不公平（Critical）
- **6 个 Should-Fix**：κ-DR 叙事权重过高、Proposition 1 新颖性降级、CF trade-off 对称呈现、70B "validation" overclaim、scale-dependent interaction 因果解释、S1 vs S2 深入分析
- **唯一分歧**（已裁定）：LoRA-only composability — R2 rebut 有效（full FT 已验证 + 机制论证成立），降为 Minor

实验质量和透明度是显著优势，概念新颖性中等（Excitement 3/5）。修复 MF1+MF2 后评分有望上调至 3.5-4.0 区间。Issue tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 188

## Round 188

2 recorded events


### User

_source line 2529 · 2026-05-23T10:50:09.090615+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 全部 12 个问题的逐条回应。核心判断：

- **12/12 全部 AGREE**
- 与我 Round 1 的独立发现高度一致：R2-N1 对应我的 W5，R2-W3 对应我的 N2（CF trade-off），R2-W4 对应我的 N1（κ overclaim）
- R2 新发现的两个有价值问题：M1（Abstract F1 范围 factual error: 40.79% < 41%）和 M2（CRANE 与 S2 70B 降级的未连接讨论）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2530 · 2026-05-23T10:50:24.357658+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**：

- **Overall: 3.5 (Borderline Conference)**，R1/R2 完全一致
- **2 个 Must-Fix (Critical)**：WikiEvents n=20 从 Contribution 降级 + GoLLIE 比较方法论不公平
- **6 个 Should-Fix (Major)**：κ-DR 叙事权重过高、Proposition 1 新颖性有限、CF trade-off 讨论不足、70B "validation" overclaim、scale-dependent interaction 缺因果解释、S1 vs S2 分析不足
- **1 个分歧已裁定**：LoRA-only composability（R2 rebut 有效，降为 Minor）
- **视觉审查**：3 warning（主文 display items 偏少、Method 段纯文本墙、Discussion 无总结图表），0 critical
- **Issue tracker 已同步**：R25 新增 11 条 issue，更新 8 条既有 issue

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 189

## Round 189

70 recorded events


### User

_source line 2531 · 2026-05-23T12:31:37.833459+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema_semantic_constrained_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2532 · 2026-05-23T12:31:44.333117+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2533 · 2026-05-23T12:31:44.384320+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2534 · 2026-05-23T12:31:53.777903+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2535 · 2026-05-23T12:31:53.829383+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2536 · 2026-05-23T12:31:56.842289+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 2537 · 2026-05-23T12:31:56.892949+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2538 · 2026-05-23T12:32:00.106597+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2539 · 2026-05-23T12:32:00.157347+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2540 · 2026-05-23T12:32:09.151857+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2541 · 2026-05-23T12:32:11.060036+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (164 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-23T11:28:52Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 153 个实验 — DONE 151, PREPARING 2\n**DONE 分布**: failed 12, killed 4, negative 15, success 120\n\n### 💾 磁盘余量\n- **westd-16980**:\n  - `/init`: 150M/150M 可用（已用 0%）\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/usr/bin/nvidia-smi`: 432G/879G 可用（已用 49%）\n- **westd-21461**:\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/usr/bin/nvidia-smi`: 817G/879G 可用（已用 3%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `sf2_70b_prompt_sensitivity` [failed] — 2026-05-23T11:28:47 — process dead 5× with no sentinel/W&B — auto-resolved as failed\n- `eval_70b_lora_docred_200_full_s2` [negative] — 2026-05-23T08:04:47\n- `sf2_qwen_int4_docred_s1` [success] — 2026-05-23T07:57:03\n- `sf2_llama_int4_docred_s1` [success] — 2026-05-23T07:13:24\n- `sf2_llama_int4_scierc_s1` [success] — 2026-05-23T05:35:25\n\n### 🔴 最近失败原因 (top 3)\n- `sf2_70b_prompt_sensitivity`: process dead 5× with no sentinel/W&B — auto-resolved as failed\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\
…[truncated 1934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1908
}
```

</details>

---


### Tool call

_source line 2542 · 2026-05-23T12:32:11.060414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2543 · 2026-05-23T12:32:11.813071+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_wikievents_draft}
56	\input{section5_runtime}
57	
58	% === §6 Related Work ===
59	\input{section6_related_work}
60	
61	% === §7 Discussion and Conclusion ===
62	\section{Discussion and Conclusion}
63	\label{sec:discussion}
64	\input{section7_conclusion_compressed}
65	
66	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
67	\clearpage
68	\section*{Limitations}
69	
70	\paragraph{Constraint scope.}
71	CF is an architectural consequence of per-triple independent enforcement: CF$\leftrightarrow$DR represents a fundamental trade-off (eliminating CF re-routes violations to DR; Appendix~\ref{app:cf-dr-tradeoff}), and its impa
…[truncated 5123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 752
}
```

</details>

---


### Tool call

_source line 2544 · 2026-05-23T12:32:11.813578+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2545 · 2026-05-23T12:32:11.864092+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2546 · 2026-05-23T12:32:19.601042+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I found information about EMNLP 2026, though the search results primarily contain information about EMNLP 2026 workshops and tu
…[truncated 1155 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 7787
}
```

</details>

---


### Tool result

_source line 2547 · 2026-05-23T12:32:19.601576+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 7737
}
```

</details>

---


### Tool call

_source line 2548 · 2026-05-23T12:32:26.481406+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 2549 · 2026-05-23T12:32:27.423574+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers submission deadline ARR commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers submission deadline ARR commitment"
  }
}
```

</details>

---


### Tool call

_source line 2550 · 2026-05-23T12:32:28.161510+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 2551 · 2026-05-23T12:32:33.633251+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission deadline ARR commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"}]

Based on the web search results, here is the information about the EMNLP 2026 main conference call for papers submission deadl
…[truncated 1173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 6209
}
```

</details>

---


### Tool result

_source line 2552 · 2026-05-23T12:32:33.984279+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"}]

Based on the search results, here are the ACL Rolling Review 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pag
…[truncated 1155 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 7502
}
```

</details>

---


### Tool result

_source line 2553 · 2026-05-23T12:32:34.038436+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5876
}
```

</details>

---


### Tool call

_source line 2554 · 2026-05-23T12:33:01.007565+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2555 · 2026-05-23T12:33:01.911693+00:00_

1	\begin{abstract}
2	Large language models for information extraction generate structurally valid but ontologically invalid triples---where entity types violate the ontology's domain/range constraints.
3	These violations persist across the capability spectrum and cannot be addressed by grammar-constrained decoding (which lacks cross-field type awareness) or post-hoc filtering (which discards valid predictions).
4	
5	We present \textsc{OntoCoDec}, a framework that compiles information extraction ontologies into composable token-level decoding constraints.
6	A decidability analysis shows that domain/range constraints exceed context-free expressiveness, yielding a two-layer architecture: a grammar layer enforces structural validity and vocabulary membership; a semantic layer enforces type constraints at runtime through stateful masking over a dynamic entity registry.
7	
8	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
9	Evaluated across three 8B-class models and two relation extraction datasets (up to 96 relations), OntoCoDec composed with LoRA fine-tuning reduces domain/range violations to near-zero ($\leq$\,0.21\%) at F1 40--46\%, but introduces cross-field type inconsistencies ($\leq$1.4\%) from per-triple enforcement.
10	Beam search ($k{=}2$) reduces CF to 0.11\% at 1.18$\times$ latency; $k{=}4$ eliminates all violation types at 8B at 1.39$\times$.
11	In zero-shot settings, cross-field rates are higher (up to 12\%) but decrease with model calibration.
12	Zero-shot domain/range reductions span 76--99\% on SciERC and 42--90\% on DocRED; with scale- and schema-dependent layer interaction.
13	\end{abstract}
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 2556 · 2026-05-23T12:33:01.962308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2557 · 2026-05-23T12:33:01.962918+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates follow an observed pattern consistent with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
9	At competitive quality (R-F1 40--46\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering discards up to 74\% of predictions including true positives (Appendix~\ref{app:cross-model-zs}).
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime enforcement.
16	
17	We propose \textbf{OntoCoDec}, a framework that translates IE ontologies into composable layers of decoding-time constraints.
18	A decidability analysis of IE type constraints (\S\ref{sec:decidability}) yields a two-layer architecture:
…[truncated 2836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2558 · 2026-05-23T12:33:02.415205+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 2559 · 2026-05-23T12:33:03.520088+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$, where $\mathcal{P}(\cdot)$ denotes the power set, specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We quantify constraint restrictiveness via \emph{constraint tightness} $\kappa(r)$ (\S\ref{sec:composition}): tighter constraints leave fewer valid type pairs per relation.
11	We define ontology constraints broadly to encompass both formal ontology specifications (e.g., the KAIROS event ontology with explicit role-entity type mappings) and empirically derived type-pair constraints extracted from annotated training data.
12	The latter applies when datasets lack a formal ontology but provide typed annotations (SciERC, DocRED); OntoCoDec compiles both sources into the same constraint representation without modification.
13	Empirical constraints achieve 99\%+ instance-level coverage on held-out data (SciERC 99.0\%, DocRED 99.4\%); uncovered type pairs trigger grammar-first fallback (\S\ref{sec:composition}), ensuring no valid triples are blocked.
14	
15	\paragraph{Grammar-Constrained Decoding.}
16	\label{sec:bg:gcd}
17	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
18	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
19	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $
…[truncated 886 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 2560 · 2026-05-23T12:33:03.520462+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2561 · 2026-05-23T12:33:04.336562+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	\input{fig1_framework}
9	
10	We present OntoCoDec, a framework that translates IE ontologies into token-level constraints enforced during autoregressive generation.
11	The design is guided by a decidability analysis of IE type constraints.
12	
13	\paragraph{Constraint decidability taxonomy.}
14	\label{sec:decidability}
15	We classify IE type constraints into three levels: (1)~\emph{context-free}: vocabulary membership and JSON structure; (2)~\emph{prefix-decidable with state}: domain/range type validity, determined at each type-bearing position given the decoded relation type and entity registry; (3)~\emph{non-local}: cross-entity type consistency, which depends on the full output.
16	Unlike code generation where types are statically declared, IE constraints fall into level~2: entity types are inferred from text, the registry is built dynamically, and constraint targets depend on the co-occurring relation.
17	OntoCoDec enforces levels 1--2 (grammar and semantic layers, respectively); level~3 is addressed by beam search or post-hoc resolution (Appendix~\ref{app:tcr}).
18	
19	\smallskip
20	\noindent
21	Existing grammar-constrained decoding frameworks (e.g., XGrammar) enforce level~1 constraints---structural validity and vocabulary membership---but IE domain/range rules require cross-position entity-type state that context-free grammars cannot express.
22	Even when the entity set is finite, encoding type constraints into a DFA requires $O(|\mathcal{E}|^{|\text{entities}|})$ states: for typical SciERC documents (median 17 entities, 6 types), $6^{17} \approx 1.6{\times}10^{13}$ states; for DocRED (median 19 entities, 6 types), $6^{19} \approx 6.1{\times}10^{14}$---well beyond practical construction for online decoding.
23	Formally, domain/range constraints for unbounded entity sets are not context-free (\tex
…[truncated 7502 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 816
}
```

</details>

---


### Tool call

_source line 2562 · 2026-05-23T12:33:04.387929+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_26/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_26/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2563 · 2026-05-23T12:33:04.790427+00:00_

-rw-r--r-- 1 ubuntu ubuntu 617668 May 23 12:24 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_26/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2564 · 2026-05-23T12:33:04.941315+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2565 · 2026-05-23T12:33:05.042886+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml\", \"content\": \"_next_id: 88\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 主目标调整为 EMNLP 2026 ARR (5/25), AAAI 2027 为后备\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、不要保守、资源会给够。12 天 AI 团队速度足够：Phase 0 (1-2天) →\\n    Phase 1 compiler (2-3天) → Phase 2 experiments (2-3天) → Paper (2-3天)。禁止 fallback\\n    思维，冲最高目标。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 19:14 UTC\\n  summary: SciERC Phase 0 结果确认 GO — domain_range violation rate 15.4%，3× 超阈值\\n  rationale: 'SciERC 全量 test set (551 sentences, 1724 triples): domain_range_violation_rate\\n    = 15.4%，远超 5% go/no-go 阈值。违规分布极不均匀 (Feature-of 33.5%, Compare 42.4% vs Used-for\\n    0.76%)，支持\\\"特定 relation types 需要 decoding-time enforcement\\\"的论文 claim。DocRED dry-run\\n    (37 docs) 同样显示 14.4%。两个数据集均为 GO 信号，MVP 核心假设得到强验证。等 schema-informed prompt 结果确认\\n    prompt 级干预不足以解决问题后正式宣布 MVP 通过。'\\n  related_experiments:\\n  - exp_id: mvp_phase0_violation_rate\\n    role: primary\\n    result: domain_range_violation_rate=15.4%, go_nogo=GO\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 21:48 UTC\\n  summary: MVP 通过，进入 Research 阶段，立即启动 Phase 2 constrained decoding 实验\\n  rationale: Phase 0 三个实验完成：SciERC 15.4%/5.78%, DocRED 18.7% domain_range violation\\n    rate。两个数据集均远超 5% 阈值，核心假设得到强验证。Phase 1 compiler 代码就绪（36 tests 通过），Phase 2 脚本就绪（S1\\n    路径可用，S2 bug 修复中）。cuda:1 空闲，立即启动 Phase 2 SciERC grammar_only/semantic_only/full_s1\\n    实验。\\n  related_experiments:\\n  - exp_id: mvp_phase0_violation_rate\\n    role: primary\\n    result: SciERC DR=15.4%, GO\\n  - exp_id: mvp_phase0_scierc_schema\\n    role: primary\\n    result: SciERC DR=5.78%, prompt insufficient\\n  - exp_id: mvp_phase0_violation_rate_docred\\n    role: primary\\n    result: DocRED DR=18.7%, GO\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-
…[truncated 1469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2566 · 2026-05-23T12:33:13.628026+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2567 · 2026-05-23T12:33:14.593182+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	where $\wedge$ denotes element-wise AND over the vocabulary $V$; a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the scale-dependent layer interaction (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property enforced only by the grammar layer.
12	This dependency is scale-sensitive: 70B semantic-only achieves 84\% DR reduction (vs.\ 24\% on 8B), though grammar remains necessary for RV elimination (\S\ref{sec:70b-results}).
13	
14	\paragraph{Grammar-First Fallback.}
15	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
16	We enforce a \emph{grammar-first fallback}: semantic masking is skipped and the grammar layer alone controls selection.
17	Structural integrity is a hard constraint; type violations are soft errors detectable by downstream validation, with DR (ontologically invalid type pair) more severe than CF (individually valid triples with cross-triple type inconsistency).
18	Extraction tasks are robust to format-level constraints~\cite{tam2024letmespeak}, supporting this asymmetric treatment.
19	
20	\paragraph{Constraint Tightness.}
21	\label{eq:tightness}
22	Per-relation constraint tightness $\kappa(r) = 1 - |\sigma(r)|/|\mathcal{E}|^2$ captures schema restrictiveness; DR reduction correlates descriptively with schema-mean
…[truncated 1415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 965
}
```

</details>

---


### Tool call

_source line 2568 · 2026-05-23T12:33:14.759966+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 2569 · 2026-05-23T12:33:15.563590+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two deployment configurations: greedy S1 (DR\,$\leq$\,0.21\%, $+$10\% latency) and beam S1 (all violations\,$\to$\,0\%, 1.39$\times$ latency); zero-shot evaluation (\S\ref{sec:scierc-results}; Appendix~\ref{app:cross-model-zs}) serves as a diagnostic probe for the fine-tuned setting (R-F1 40--46\%).
8	
9	\paragraph{Setup.}
10	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 development documents; test annotations are not publicly available; 96 relations, $\bar{\kappa}{=}0.842$).
11	RE type constraints are extracted from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) derive from the KAIROS ontology.
12	All constraints are schema-level, independent of evaluation splits.
13	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in Appendix~\ref{app:cross-model-zs}, composability with fine-tuning in \S\ref{sec:composability}.
14	LoRA hyperparameters (rank, $\alpha$, learning rate) were tuned on SciERC and transferred to DocRED without dataset-specific optimization; given the substantial schema complexity difference (7 vs.\ 96 relations), this transfer may underestimate DocRED fine-tuning potential.
15	Our R-F1 range (40--46\% under LoRA) is consistent with recent LLM-based generative RE evaluations on these benchmarks, where document-level closed IE without gold entity spans typically achieves 35--50\%~\cite{wadhwa2023revisiting}; supervised span-based methods operating under different assumptions (gold entity spans, dedicated architectures) are not directly comparable.
16	DocRED development documents 
…[truncated 422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 2570 · 2026-05-23T12:33:15.714598+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2571 · 2026-05-23T12:33:16.317593+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	GCD-equiv.$^\dagger$
41	  & 15.26 & $\downarrow$1\%
42	  & \textbf{0} & \textbf{0}
43	  & 0.04  & 15.30
44	  & 8.75  & 30.91 \\
45	Semantic
46	  & 11.65 & $\downarrow$24\%
47	  & 1.51  & 0.40
48	  & 2.71  & 14.36
49	  & 8.15  & 31.01 \\
50	S1
51	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
52	  & \textbf{0} & \textbf{0}
53	  & 9.90  & \textbf{10.83}
54	  & \textbf{8.36} & 30.98 \\
55	S2
56	  & 0.97  & $\downarrow$94\%
57	  & \textbf{0} & \textbf{0}
58	  & 8.03  & \textbf{9.00}
59	  & 8.03  & \textbf{31.90} \\
60	\bottomrule
61	\end{tabular}}%
62	\caption{Five-way ablation on SciERC (551 docs
…[truncated 7391 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 2572 · 2026-05-23T12:33:16.318054+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2573 · 2026-05-23T12:33:16.468925+00:00_

1	% Section 5 — Event Extraction on WikiEvents (summary; full results in Appendix)
2	
3	\subsection{Preliminary Event Extraction Pilot}
4	\label{sec:wikievents}
5	
6	A preliminary $n{=}20$ WikiEvents pilot confirms constraint applicability to event extraction (Appendix~\ref{app:wikievents-pilot}).
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2574 · 2026-05-23T12:33:21.689868+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 2575 · 2026-05-23T12:33:22.141993+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC, lower on DocRED due to amortization over longer sequences; under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
7	
8	\paragraph{Beam search compatibility.}
9	\label{sec:beam-results}
10	% exp_id: d066_beam_sweep
11	With LoRA, beam search~\cite{anderson2017guided} eliminates all four violation types at 8B on both SciERC and DocRED; at 70B, beam $k{=}4$ achieves DR${=}$RV${=}$ET${=}$0\% with one residual CF on SciERC (Appendix~\ref{app:beam-search}).
12	A beam-width sweep ($k \in \{1,2,4,8\}$) on SciERC reveals $k{=}2$ as Pareto-optimal: R-F1 44.60 (highest), CF 0.11\%, at only 1.18$\times$ greedy S1 latency; $k{=}4$ achieves CF${=}$0\% but lower R-F1 (43.60) at 1.39$\times$ (Table~\ref{tab:beam-sweep}; latencies relative to greedy S1).
13	This yields three deployment tiers: greedy S1 ($+$10\% latency, DR${\leq}$0.21\%, CF${\leq}$1.4\%), beam $k{=}2$ (1.18$\times$, near-zero CF), and beam $k{=}4$ (1.39$\times$, all violations${\to}$0\% at 8B).
14	Per-beam memory overhead is $O(k \times |\text{entities}| \times |\text{types}|)$ for independent entity registry copies, negligible at typical document scales.
15	
16	% exp_ids: r16_70b_scierc_zs_s1, r16_70b_docred_zs_s1, 70b_lora_scierc, 70b_lora_docred_200
17	\paragraph{70B-class validation (single-family).}
18	\label{sec:70b-results}
19	The following results constitute a preliminary single-family scale exploration on Llama-3.1-70B-Instruct (AWQ INT4); cross-family verification (e.g., Qwen-72B) remains future work.
20	All 70B experiments use Llama-3.1-70B-Instruct under AWQ INT4 quantization; an 8B ablation confirms constraint enforcement is unaffected by quantization (Appen
…[truncated 1743 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2576 · 2026-05-23T12:33:22.142530+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2577 · 2026-05-23T12:33:23.196976+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SynCode~\cite{ugare2024syncode}, SGLang~\cite{zheng2024sglang}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} enforce format validity via CFG-based token masking but lack cross-field semantic awareness.
8	PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata; KG-Trie~\cite{luo2025kgtrie} applies trie-based KG constraints during decoding for knowledge-to-text generation.
9	OntoCoDec applies constructive forward masking via a dynamic entity registry, enforcing schema semantics within a single forward pass.
10	
11	\paragraph{Schema-aware IE.}
12	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, and others~\cite{guidex2025,josifoski2022genie,paolini2021tanl,cabot2021rebel,wang2023instructuie,qi2024adelie,fei2022lasuie,lu2022uie,zhou2024universalner} encode ontology structure via training-time internalization without runtime enforcement~\cite{wadhwa2023revisiting}.
13	GoLLIE achieves schema compliance through annotation-guideline-guided generation at training time; OntoCoDec provides orthogonal runtime enforcement, composable with any generative IE system including GoLLIE itself (Appendix~\ref{app:gollie-comparison}).
14	
15	\paragraph{Constraint enforcement in IE.}
16	\citet{roth_yih_2004} and \citet{riedel2010modeling} formulated hard type constraints via ILP; post-hoc validation~\cite{khorshidi2025odke,spires_2024,ontologx_2025} detects violations after generation but discards up to 74\% of predictions.
17	EnriCo~\cite{zaratiana2024enrico} uses ASP; IterGen~\cite{ugare2025itergen} backtracks on violations; \citet{vukovic2024dialogue} combines ontology constraints with const
…[truncated 281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 2578 · 2026-05-23T12:33:23.247705+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 2579 · 2026-05-23T12:33:23.700110+00:00_

1	% Section 7 — Discussion and Conclusion
2	
3	OntoCoDec compiles IE ontologies into composable token-level constraints, validated across 3 datasets, 3+ models, and 2 tasks.
4	The central empirical finding is non-additive layer interaction: grammar alone achieves 3\% DR reduction on SciERC, semantic alone 24\%, but their composition yields 94\% at 8B (\S\ref{sec:scierc-results})---an enabling dependency where grammar-enforced vocabulary membership creates the clean input the semantic layer requires.
5	
6	\paragraph{Scale-dependent layer interaction.}
7	This dependency weakens at scale: at 70B, the semantic layer independently achieves 84\% DR reduction (\S\ref{sec:70b-results}).
8	We hypothesize this reflects improved vocabulary calibration: larger models assign higher probability to ontology-valid tokens, reducing the semantic layer's dependence on grammar-enforced vocabulary membership (Appendix~\ref{app:causal-tracing}).
9	Supporting evidence includes the fallback frequency gap: under LoRA + S1, Qwen-8B triggers 0 grammar-first fallbacks on SciERC while Llama-8B triggers 5{,}882 (Table~\ref{tab:ft-ablation}), yet both achieve DR\,$\leq$\,0.21\%, confirming that fallback frequency does not determine enforcement effectiveness.
10	Grammar-constrained decoding is thus necessary but increasingly insufficient as models improve; constraint enforcement is preserved under INT4 quantization (4$\times$ compression; Appendix~\ref{app:quantization}).
11	
12	\paragraph{DR$\leftrightarrow$CF trade-off.}
13	Greedy S1 reduces DR to $\leq$\,0.21\% but introduces CF (zero-shot $+$9.82\,pp, fine-tuned $+$1.18\,pp)---an architectural consequence of per-triple independent enforcement.
14	Among 248 zero-shot CF violations, 58.1\% involve hallucinated entities (absent from gold) and only 7.3\% are true cascade errors (\S\ref{sec:scierc-results}); fine-tuned CF drops to $\leq$1.4\%.
15	Beam $k{=}2$ reduces CF to 0.11\% at 1.18$\times$ latency (Pareto-optimal; recommended for zero-shot de
…[truncated 1235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2580 · 2026-05-23T12:33:23.700508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/fig1_framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/fig1_framework.tex"
  }
}
```

</details>

---


### Tool result

_source line 2581 · 2026-05-23T12:33:23.751001+00:00_

1	\begin{figure*}[t]
2	\centering
3	\includegraphics[width=\textwidth]{figures/fig1_framework.pdf}
4	\caption{Overview of OntoCoDec. An IE ontology is compiled into two constraint layers: a grammar layer (context-free) and a semantic layer (prefix-decidable with state). At each decoding step, the final mask $M_{\text{final}}(t) = G(t) \cap S(t)$ ensures both structural and type validity; when $S(t) \cap G(t) = \emptyset$, grammar-first fallback preserves JSON integrity.}
5	\label{fig:framework}
6	\end{figure*}
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2582 · 2026-05-23T12:33:35.275558+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_26/submitted.pdf 2>/dev/null | grep -E \"Pages|Page size\"",
  "description": "Check PDF page count and size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_26/submitted.pdf 2>/dev/null | grep -E \"Pages|Page size\"",
    "description": "Check PDF page count and size"
  }
}
```

</details>

---


### Tool result

_source line 2583 · 2026-05-23T12:33:35.878405+00:00_

Pages:           40
Page size:       595.276 x 841.89 pts (A4)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 2584 · 2026-05-23T12:33:36.230203+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "ROADMAP.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "ROADMAP.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2585 · 2026-05-23T12:33:37.184472+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/ROADMAP.md\", \"content\": \"# schema_semantic_constrained_ie — Research Dashboard\\n\\n> 最后更新: 2026-05-23 05:48 UTC | 更新原因: R21 审稿修复完成 + 新实验进展更新\\n\\n## 核心方向\\nOntoCoDec: 两层约束解码（grammar + semantic）将 IE schema 翻译为 token-level constraints，消除 LLM-based IE 的 type violations。**目标: EMNLP 2026 ARR May 25 提交**。详见 paper_framing.md。\\n\\n## 当前进展\\n**阶段**: R21 审稿修复完成 → 最后实验收尾 → Final compile\\n\\n**R21 审稿 (Overall 3.5 Borderline Conference)**:\\n- ✅ 全部 15 个 patch 已写入论文（Abstract 重写、enabling dependency→empirical、Table 1 caption、Limitations 等）\\n- ✅ SF2 INT4 量化对比实验完成 → Appendix P (quantization robustness)\\n- ✅ D4 GoLLIE-7B 复现完成 → Appendix Q (GoLLIE comparison)\\n- ✅ SF5 Bonferroni per-config p-values + Cohen's d → Appendix C\\n- ✅ 论文编译通过，主文 8 页，39 页总计，无 undefined reference\\n\\n**正在跑的实验**:\\n- 🔄 eval_70b_lora_docred_200_full_s2（westd-21461 cuda:1）— 68.5%，~2h\\n- 🔄 70B Prompt Sensitivity（westd-21461 cuda:0）— Worker 已启动\\n- 🔄 westd-16980: 检查 DocRED INT4 可行性\\n\\n## 近期任务\\n- [ ] S2 完成 → 写入 appendix_70b_ablation.tex\\n- [ ] 70B PS 完成 → 评估写入 appendix_prompt_sensitivity.tex\\n- [ ] DocRED INT4（如可行）→ 扩展 Appendix P 量化表\\n- [ ] Final compile + 提交 R23 审稿\\n- [ ] May 25 EMNLP ARR 提交\\n\\n## GPU 预算\\nwestd-21461 cuda:0,1 — 正在跑 (70B PS + S2)\\nwestd-16980 cuda:0,1 — 检查 DocRED INT4 可行性中\\n\\n## 时间线\\n- **May 23 05:45**: R21 patch 完成 + 新实验数据写入\\n- **May 23 ~08:00**: S2 + 70B PS 完成，结果写入\\n- **May 23-24**: Final compile → R23 审稿 → 修复 → 冻结\\n- **May 25**: EMNLP 2026 ARR 提交\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D087 | 2026-05-23 | DocRED FT Semantic-only DR 重验后修正叙事：去掉 \\\"39-72%\\\" ran | w8_llama_docred_ft_semantic_only, w8_qwen_docred_ft_semantic_only |\\n| D086 | 2026-05-23 | R25 审稿报告全面修复：14 项 Action Matrix，全部为写作层面修改 | — |\\n| D085 | 2026-05-22 | Dream dream_20260522T052642 分析完成：Best=2.5, Median= | — |\\n| D084
…[truncated 770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2586 · 2026-05-23T12:33:37.185014+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2587 · 2026-05-23T12:33:38.190788+00:00_

# Review Issues Tracker — schema_semantic_constrained_ie
# Updated: R25 fresh review, 2026-05-23

# ============================================================
# Round 25 — Active Issues
# ============================================================

- id: "R16-W5"
  summary: "Proposition 1 定位过高 + 理论-实践 gap 桥接不充分"
  category: framing
  severity: warning
  status: open
  first_raised_round: 14
  last_seen_round: 25
  mentions:
    - round: 19
      reviewers: [1, 2]
      note: "共识定位为 systems contribution。"
    - round: 23
      reviewers: [1, 2]
      note: "与 R23-W2/W7 合并。降低理论贡献措辞。"
    - round: 24
      reviewers: [1, 2]
      note: "R24-MF1 (critical)。R23 写作降级不够。"
    - round: 25
      reviewers: [1, 2]
      note: "R25 R1-W1+R2-W1 完全共识 [Major]。论文已改为 'formalizing a known intuition'，定位诚实但仍列为 Contribution 1 首位且 §3 篇幅过大。两位 Reviewer 认为 engineering applicability (DFA 6^17 states) 比 Proposition 1 本身更有价值。多轮复发但严重程度已从 critical 降为 warning——定位措辞已改善，问题在于展示权重。"
  action_items:
    - round: 19
      action: "§7 Discussion 定位 systems contribution"
      assigned_to: paper_agent
      status: completed
    - round: 21
      action: "§3 论证 semantic layer 非显而易见"
      assigned_to: paper_agent
      status: completed
    - round: 23
      action: "降低 Proposition 1 强度 + κ 统计限定"
      assigned_to: paper_agent
      status: completed
    - round: 24
      action: "§1 C1 重写 'formalizing known intuition' + §3 DFA 可行边界 + proof sketch 扩展"
      assigned_to: paper_agent
      status: completed
    - round: 25
      action: "降低 Proposition 1 展示权重：从 Contribution 1 首位降级，或将 engineering applicability 作为主要论述重心而非 pumping lemma proof"
      assigned_to: paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R16-W1"
  summary: "κ-DR 相关性 n=3 呈现不当——正文 §4 叙事权重过高"
  category: framing
  severity: warning
  status: open
  first_raised_round: 12
  last_seen_round: 25
  mentions:
    - round: 22
      reviewers: [1, 2]
      note: "R22 解决：加 empirical + scale-dependent qual
…[truncated 19522 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 2588 · 2026-05-23T12:33:38.191297+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null | head -100",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null | head -100",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2589 · 2026-05-23T12:33:38.241866+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2590 · 2026-05-23T12:34:08.185512+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"config.toml\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"config.toml\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 2591 · 2026-05-23T12:34:09.089502+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 2592 · 2026-05-23T12:34:09.140121+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EMNLP 2026\" \"call for papers\" page limit anonymity guidelines site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EMNLP 2026\" \"call for papers\" page limit anonymity guidelines site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool result

_source line 2593 · 2026-05-23T12:34:14.561955+00:00_

Web search results for query: ""EMNLP 2026" "call for papers" page limit anonymity guidelines site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"}]

I found relevant information from the EMNLP 2026 Call for Main Conference Papers. Here are the key guidelines:

**Anonymity Guidelines:**
Following the ACL and ARR policies, there is no anonymity period requirement. Additionally, the reviewing process will be double-blind, with reviewers not seeing authors, nor will authors see reviewers.

**Page Limits:**
The search results don't explicitly state the page limit for main conference papers in the excerpt provided. However, for the Industry Track specifically, accepted papers will be given one additional page of content (up to 7 pages; ethical considerations, limitations, acknowledgements and references do not count against this limit).

The main conference papers page limit information appears to follow ARR submission requirements, but the specific page count wasn't included in the visibl
…[truncated 343 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 5421
}
```

</details>

---


### Tool call

_source line 2594 · 2026-05-23T12:34:43.800651+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 2595 · 2026-05-23T12:35:07.055865+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23255
}
```

</details>

---


### Tool call

_source line 2596 · 2026-05-23T12:35:08.009662+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计 + 统计分析**。\n\n## 审稿目标论文\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_26/submitted.pdf`\n\n## Venue 要求（EMNLP 2026 ARR May cycle）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板, double-blind review\n- **页数限制**: Long paper 8 页正文 + unlimited references\n- **Limitations**: 必须有独立 Limitations section，在 conclusion 之后、references 之前，不计入页数\n- **匿名**: double-blind，作者栏应为 \"Anonymous ACL submission\"\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- Proposition 1（pumping lemma 证明 domain/range constraints 非 context-free）的正确性和实际意义\n- 两层架构（grammar layer + semantic layer）的设计合理性\n- Entity registry 的 first-seen semantics 及其局限性\n- Grammar-first fallback 策略的理论依据\n- Scale-dependent layer interaction (8B: 24% vs 70B: 84% independent DR reduction) 的因果解释\n\n### 2. 实验设计\n- Ablation study 的完整性和对照组设置\n- 数据集选择（SciERC, DocRED, WikiEvents）的覆盖面和代表性\n- WikiEvents n=20 是否足以支撑 task generalization claim\n- 70B 实验仅 Llama-3.1-70B AWQ INT4 单一模型族的限制\n- LoRA 超参从 SciERC 转移到 DocRED 的合理性\n- S1 vs S2 对比的充分性\n\n### 3. 统计分析\n- Bonferroni correction 的正确使用\n- Bootstrap CIs 和 effect sizes 的报告\n- DR reduction 的统计显著性\n- 结论是否被数据支持（特别是 zero-shot 场景下 total violation 仅降 30%，DR↓94% 但 CF 0.08%→9.90%）\n\n### 4. DR↔CF Trade-off\n- 论文对 DR→CF 转换的 framing 是否平衡\n- Abstract 中 DR reduction 的突出与 CF increase 的不对称\n- Beam search 作为 CF 解决方案的实用性评估\n\n请按以下格式输出审稿报告：\n\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[逐条列出]\n\n## Weaknesses\n[逐条列出，标注严重程度: Critical / Major / Minor]\n\n## Questions\n[需要作者澄清的问题]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Detailed Comments\n[逐节详细意见]\n\n## Overall Assessment\n- Score: [用 EMNLP 2026 评分标准]\n- Confidence: [1-5]\n- Excitement: [1-5]\n```",
  "project": "schema_semantic_constrained_ie",
  "chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计 + 统计分析**。\n\n## 审稿目标论文\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_26/submitted.pdf`\n\n## Venue 要求（EMNLP 2026 ARR May cycle）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板, double-blind review\n- **页数限制**: Long paper 8 页正文 + unlimited references\n- **Limitations**: 必须有独立 Limitations section，在 conclusion 之后、references 之前，不计入页数\n- **匿名**: double-blind，作者栏应为 \"Anonymous ACL submission\"\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- Proposition 1（pumping lemma 证明 domain/range constraints 非 context-free）的正确性和实际意义\n- 两层架构（grammar layer + semantic layer）的设计合理性\n- Entity registry 的 first-seen semantics 及其局限性\n- Grammar-first fallback 策略的理论依据\n- Scale-dependent layer interaction (8B: 24% vs 70B: 84% independent DR reduction) 的因果解释\n\n### 2. 实验设计\n- Ablation study 的完整性和对照组设置\n- 数据集选择（SciERC, DocRED, WikiEvents）的覆盖面和代表性\n- WikiEvents n=20 是否足以支撑 task generalization claim\n- 70B 实验仅 Llama-3.1-70B AWQ INT4 单一模型族的限制\n- LoRA 超参从 SciERC 转移到 DocRED 的合理性\n- S1 vs S2 对比的充分性\n\n### 3. 统计分析\n- Bonferroni correction 的正确使用\n- Bootstrap CIs 和 effect sizes 的报告\n- DR reduction 的统计显著性\n- 结论是否被数据支持（特别是 zero-shot 场景下 total violation 仅降 30%，DR↓94% 但 CF 0.08%→9.90%）\n\n### 4. DR↔CF Trade-off\n- 论文对 DR→CF 转换的 framing 是否平衡\n- Abstract 中 DR reduction 的突出与 CF increase 的不对称\n- Beam search 作为 CF 解决方案的实用性评估\n\n请按以下格式输出审稿报告：\n\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[逐条列出]\n\n## Weaknesses\n[逐条列出，标注严重程度: Critical / Major / Minor]\n\n## Questions\n[需要作者澄清的问题]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Detailed Comments\n[逐节详细意见]\n\n## Overall Assessment\n- Score: [用 EMNLP 2026 评分标准]\n- Confidence: [1-5]\n- Excitement: [1-5]\n```",
    "project": "schema_semantic_constrained_ie",
    "chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
````

</details>

---


### Tool result

_source line 2597 · 2026-05-23T12:35:25.411801+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17402
}
```

</details>

---


### Tool call

_source line 2598 · 2026-05-23T12:35:25.562917+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量 + 格式合规**。\n\n## 审稿目标论文\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_26/submitted.pdf`\n\n## Venue 要求（EMNLP 2026 ARR May cycle）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板, double-blind review\n- **页数限制**: Long paper 8 页正文 + unlimited references\n- **Limitations**: 必须有独立 Limitations section，在 conclusion 之后、references 之前，不计入页数\n- **匿名**: double-blind，作者栏应为 \"Anonymous ACL submission\"\n- **Ethics Statement**: 可选但推荐\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- OntoCoDec 的核心创新点是什么？是否超越了 XGrammar + stateful logits processor 的简单集成？\n- Proposition 1 (domain/range constraints 非 context-free) 是否为 novel insight 还是 formalizing known intuition？\n- 与 PICARD、KG-Trie、GoLLIE、KnowCoder 等已有工作的差异化是否足够？\n- Constraint tightness κ 概念是否新颖且有实际价值？\n\n### 2. 完整性检查\n- 论文是否覆盖了所有必要的实验和分析？\n- GoLLIE 对比实验的公平性（零样本 GoLLIE vs 微调 OntoCoDec）\n- 是否遗漏重要的 baseline 或 ablation？\n- Contribution 声称是否被实验充分支持？\n- Abstract 中的数字是否与正文一致（特别是 F1 范围）\n- CRANE (Banerjee et al., 2025) 是否应在主文引用？\n\n### 3. 写作质量\n- 论文结构和叙事流畅性\n- 技术写作的精确性和清晰度\n- 信息密度是否适当（正文 vs Appendix 分配）\n- Discussion 和 Conclusion 是否充分\n- Limitations section 的覆盖面和诚实度\n\n### 4. 格式合规\n- 主文是否在 8 页内？\n- 是否使用 ACL 模板？`\\usepackage[review]{acl}` ✓\n- 匿名性是否满足 double-blind？\n- Limitations section 位置是否正确（conclusion 后、references 前）？\n- 是否有溢出到第 9 页的内容？\n- Abstract 不超过 200 words\n- References 格式一致性\n\n请按以下格式输出审稿报告：\n\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[逐条列出]\n\n## Weaknesses\n[逐条列出，标注严重程度: Critical / Major / Minor]\n\n## Questions\n[需要作者澄清的问题]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Detailed Comments\n[逐节详细意见]\n\n## Overall Assessment\n- Score: [用 EMNLP 2026 评分标准]\n- Confidence: [1-5]\n- Excitement: [1-5]\n```",
  "project": "schema_semantic_constrained_ie",
  "chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量 + 格式合规**。\n\n## 审稿目标论文\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_26/submitted.pdf`\n\n## Venue 要求（EMNLP 2026 ARR May cycle）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板, double-blind review\n- **页数限制**: Long paper 8 页正文 + unlimited references\n- **Limitations**: 必须有独立 Limitations section，在 conclusion 之后、references 之前，不计入页数\n- **匿名**: double-blind，作者栏应为 \"Anonymous ACL submission\"\n- **Ethics Statement**: 可选但推荐\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- OntoCoDec 的核心创新点是什么？是否超越了 XGrammar + stateful logits processor 的简单集成？\n- Proposition 1 (domain/range constraints 非 context-free) 是否为 novel insight 还是 formalizing known intuition？\n- 与 PICARD、KG-Trie、GoLLIE、KnowCoder 等已有工作的差异化是否足够？\n- Constraint tightness κ 概念是否新颖且有实际价值？\n\n### 2. 完整性检查\n- 论文是否覆盖了所有必要的实验和分析？\n- GoLLIE 对比实验的公平性（零样本 GoLLIE vs 微调 OntoCoDec）\n- 是否遗漏重要的 baseline 或 ablation？\n- Contribution 声称是否被实验充分支持？\n- Abstract 中的数字是否与正文一致（特别是 F1 范围）\n- CRANE (Banerjee et al., 2025) 是否应在主文引用？\n\n### 3. 写作质量\n- 论文结构和叙事流畅性\n- 技术写作的精确性和清晰度\n- 信息密度是否适当（正文 vs Appendix 分配）\n- Discussion 和 Conclusion 是否充分\n- Limitations section 的覆盖面和诚实度\n\n### 4. 格式合规\n- 主文是否在 8 页内？\n- 是否使用 ACL 模板？`\\usepackage[review]{acl}` ✓\n- 匿名性是否满足 double-blind？\n- Limitations section 位置是否正确（conclusion 后、references 前）？\n- 是否有溢出到第 9 页的内容？\n- Abstract 不超过 200 words\n- References 格式一致性\n\n请按以下格式输出审稿报告：\n\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[逐条列出]\n\n## Weaknesses\n[逐条列出，标注严重程度: Critical / Major / Minor]\n\n## Questions\n[需要作者澄清的问题]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Detailed Comments\n[逐节详细意见]\n\n## Overall Assessment\n- Score: [用 EMNLP 2026 评分标准]\n- Confidence: [1-5]\n- Excitement: [1-5]\n```",
    "project": "schema_semantic_constrained_ie",
    "chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
````

</details>

---


### Tool result

_source line 2599 · 2026-05-23T12:35:27.022911+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1459
}
```

</details>

---


### Assistant

_source line 2600 · 2026-05-23T12:35:44.943358+00:00_

已完成初始化：

- ✅ 视觉审查 Agent 已派发（fire-and-forget）
- ✅ Reviewer 1（方法严谨性 + 实验设计 + 统计分析）已分配
- ✅ Reviewer 2（新颖性 + 完整性 + 写作质量 + 格式合规）已分配

等待两位 Reviewer 返回独立审稿报告，收齐后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 190

## Round 190

2 recorded events


### User

_source line 2601 · 2026-05-23T12:43:34.047991+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

## Summary

本文提出 OntoCoDec，一个将 IE 本体编译为 token 级解码约束的框架。核心观察是 domain/range 类型约束超越 context-free 表达能力（Proposition 1），因此提出两层架构：grammar 层（基于 XGrammar）保证 JSON 结构和词表合法性，semantic 层（基于 stateful logits processor + 动态 entity registry）在运行时执行类型约束。在 SciERC、DocRED、WikiEvents 上评估，涵盖 3 个 8B 级模型和 1 个 70B 模型。

## Strengths

**S1.** 问题形式化清晰。Proposition 1（domain/range 约束非 context-free）虽然是对已知直觉的形式化，但 pumping lemma 证明（Appendix O）严谨，为两层架构提供了充分的理论动机。

**S2.** 评估极其全面。28 页附录覆盖了五路消融（Table 1）、四路约束消融（Tables 10-11）、beam search 分析（Appendix E）、文档长度分析（Appendix H）、full fine-tuning 对比（Appendix I）、post-hoc type consensus（Appendix M）、constraint tightness 案例研究（Appendix N）、量化鲁棒性（Appendix R）等。可复现性非常强。

**S3.** CF-DR trade-off 分析提供了真正的洞察。论文诚实地识别并量化了 per-triple enforcement 引入 cross-field (CF) 不一致的代价，并展示 beam search (k=4) 可消除全部 violation types。Table 5（page 19）和相关的双因子分析（Figure 2, page 20）质量很高。

**S4.** Limitations section 诚实且全面。覆盖了 CF 的本质限制、评估范围、工程约束等，达到了顶会审稿人期望的坦诚程度。

**S5.** 约束紧度 κ 概念有诊断价值。κ（valid type pairs fraction per relation）提供了一个可量化的 schema 约束强度指标，并被用于解释不同 schema 下的违规模式差异（Appendix N, Tables 45-46）。

**S6.** 框架设计 model-agnostic，与 fine-tuning 正交可组合。Table 2（page 6）展示了 OntoCoDec 与 LoRA 的组合效果，fine-tuned 配置 DR 降至 0%。

## Weaknesses

### Critical

**W1. [Critical] 绝对 F1 低且缺失监督 baseline 对比**
- 具体位置：Table 2 (page 6), Abstract
- 问题：fine-tuned 最优 R-F1 在 SciERC 约 44-45%、DocRED 约 42-47%。监督方法在 SciERC 上 R-F1 可达 60%+。论文完全没有与任何监督 IE baseline（如 PL-Marker, UniRE, OneRel）对比，读者无法判断约束执行在实际提取质量低下时的实用价值。论文聚焦于 violation reduction 指标（DR%, CF%），但如果底层提取质量不足，消除少量违规的边际收益存疑。
- 为什么影响接收：缺少这一对比，reviewer 和读者无法评估方法的实际研究价值——约束解码是在提升一个已经有竞争力的系统，还是在修补一个本就不够好的系统？
- 建议：至少添加 1-2 个代表性监督 baseline 的 F1 数字作为参考线（即使不能做完整对比，引用已发表的数字即可），明确定位 OntoCoDec 的 F1 在领域中的位置。

**W2. [Critical] GoLLIE 对比刻意回避**
- 具体位置：Section 7 (page 8), Appendix S (pages 39-40)
- 问题：GoLLIE 是最直接可比的工作（同样面向 ontology-compliant LLM-based IE），但论文将对比推迟到 future work，理由是 "incompatible evaluation settings"（code-style schema encoding vs. JSON prompting, different model families）。然而这些差异是可以控制的——例如在同一 base model 上同时运行两种方法。附录 S 提供了 GCD-equivalent 的 grammar-only baseline 作为 proxy（Table 17, page 25），但这不能代替与 GoLLIE 的实际对比。
- 为什么影响接收：作为 novelty claim 的一部分，论文需要证明 OntoCoDec 优于或正交于最直接的竞争者。回避对比削弱了 novelty narrative。
- 建议：即使是 approximate comparison（如引用 GoLLIE 在 SciERC/DocRED 上的已发表数字，讨论方法论差异的影响方向），也比完全回避强。

### Major

**W3. [Major] Abstract F1 范围与实际数据不一致**
- 具体位置：Abstract ("F1 40–46%") vs Table 2 (page 6)
- 问题：Abstract 声称 "at F1 40–46%"，但 Table 2 中 DocRED Qwen3-8B 的 R-F1 = 47.43%，超出声称范围。此外，Abstract 的 "F1 40-46%" 没有区分 R-F1 和 E-F1，也没有明确是 zero-shot 还是 fine-tuned 结果。
- 建议：修正为实际范围（如 "R-F1 42–47%"），或分别报告。

**W4. [Major] Contribution 声称与实际覆盖不符（Mistral fine-tuning 缺失）**
- 具体位置：Section 1 Contributions item 1 (page 2)
- 问题：Contribution 1 声称 "Systematic ablation across 3 model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B)... under both zero-shot and LoRA fine-tuned settings"，但实际只有 Qwen 和 Llama 做了 fine-tuning（Table 2, Table 10），Mistral 仅有 zero-shot 结果。这使得 "3 model families under both settings" 的表述具有误导性。
- 建议：修改为 "3 model families in zero-shot, 2 in fine-tuned settings" 或补充 Mistral fine-tuning 实验。

**W5. [Major] WikiEvents 评估过于初步**
- 具体位置：Section 5 (page 5), Appendix P (page 38)
- 问题：WikiEvents fine-tuning 仅 n=20 个文档，结果完全在附录中。Introduction (page 2) 说 "we validate on three English datasets"，但 WikiEvents 的评估深度远不及 SciERC 和 DocRED。将其计入 "three datasets" 有夸大之嫌。
- 建议：在 Introduction 中明确标注 WikiEvents 为 "pilot evaluation" 而非完整验证；或增加 WikiEvents 的评估规模。

**W6. [Major] Proposition 1 的新颖性有限**
- 具体位置：Section 3.1 (page 3), Appendix O (page 37)
- 问题：Proposition 1 证明 domain/range 约束非 context-free，但 cross-field binding 超越 CFG 表达能力在编程语言理论中是公知常识（e.g., variable declaration-use consistency 需要 context-sensitive grammar）。将此作为 "key contribution" 有 overclaim 倾向。证明本身是正确的，但洞察并不新。
- 为什么影响评分：如果 novelty claim 的核心之一建立在形式化已知直觉上，整体新颖性打折扣。
- 建议：降低对 Proposition 1 新颖性的宣称力度，将其定位为 "providing formal justification" 而非 "novel insight"。

### Minor

**W7.** Section 6 Related Work 在 8 页论文中占超过 1 页，信息密度可改善。部分讨论（如 Structural Constraints via Training and Prompting 段落, Appendix B page 14-16）可精简或移至附录。

**W8.** 缩写密度过高：DR, CF, RV, ET, S1, S2, TCR 在 Section 5 集中出现，首次阅读体验较差。建议在 Section 5 开头提供一个简表或在首次使用时更显著地定义。

**W9.** Table 1 (page 6) 有 7 行 × 多列小数字，信息密度高但可读性一般。建议用 bold/highlight 标注关键配置（如最优 vs unconstrained）。

**W10.** Abstract 末尾 "with scale- and schema-dependent layer interaction" 语法不完整（缺主语或动词），应修正。

## Questions

**Q1.** 在 fine-tuned 设置下，CF 违规的实际 downstream 影响是什么？CF ≤1.4% 看起来很低，但这些 CF 违规是否集中在某些高频 relation type 上，从而对特定关系的提取质量产生不成比例的影响？

**Q2.** Constraint tightness κ 与 downstream F1 之间的关系是什么？Table 44 (page 36) 显示高 κ 关系（如 place_of_birth）有零违规，但论文没有分析 κ 与 per-relation F1 的相关性。这能否为 "何时使用约束解码" 提供实践指导？

**Q3.** Entity registry 的 first-seen type assignment 策略是 OntoCoDec 的核心设计选择。论文在 Appendix C (page 17) 分析了 fallback 行为，但如果 first-seen assignment 错误（如 entity 首次出现在不典型的 relation context 中），downstream cascade 的影响有多大？是否有 deferred assignment 的替代方案？

**Q4.** 论文声称 OntoCoDec 与 GoLLIE 正交可组合（page 40）。是否有初步实验验证这一 composability？即使是小规模实验也能大幅增强这一 claim。

## Missing References

- **CRANE (Banerjee et al., 2025)**: 已在参考文献中但 Related Work 中讨论不够充分。考虑到 CRANE 同样做 ontology-to-tools compilation for IE constraint enforcement，应在 Section 6 给予更多篇幅。
- 缺少与近期 constrained decoding survey 的引用（如有的话）。
- 监督 IE 方法（PL-Marker, UniRE, OneRel 等）应至少作为 F1 参考点引用。

## Detailed Comments

### Section 1 (Introduction)
- 信息密度适当，问题动机清晰。Contribution 列表需要修正（W4）。
- "15.4% of triples on SciERC" 和 "18.5% on DocRED" 的 baseline violation rate 有效地建立了问题的严重性。

### Section 3 (Method)
- 两层架构的设计逻辑清晰。Figure 1 (page 3) 有效展示了 grammar layer 和 semantic layer 的分工。
- 3.3 Semantic Layer 的 entity registry 设计是论文的关键贡献，但首次阅读时需要来回翻看才能理解 first-seen semantics 和 fallback 的交互。

### Section 4 (Constraint Composition)
- M_final = M_grammar ∧ M_semantic 的组合公式简洁。
- Grammar-First Fallback 机制（当 S(t)∩G(t) = ∅ 时跳过 semantic masking）是合理的工程决策，论文正确指出这是 "asymmetric treatment"。

### Section 5 (Experiments)
- Table 1 的五路消融设计合理，每个配置都有明确的独立贡献。
- Table 2 的 fine-tuning composability 结果是论文的亮点之一。
- 但 Section 5.1 和 5.2 的行文过于依赖缩写，可读性受损（W8）。

### Section 6 (Related Work)
- 覆盖面广但篇幅过长（W7）。对 GoLLIE 和 KnowCoder 的讨论定位准确（training-based vs. runtime enforcement），但回避实验对比削弱了论述力度（W2）。

### Section 7 (Discussion and Conclusion)
- Scale-dependent layer interaction 的讨论有价值：70B 模型中 semantic 层的独立 DR reduction（84%）远超 grammar 层，而 8B 模型需要两层协作。
- DR↔CF trade-off 的讨论诚实。Per-triple vs. global enforcement 的讨论恰当地指出了未来方向。

### Limitations
- 覆盖面和诚实度优秀。三个段落（Constraint scope, Evaluation coverage, Engineering considerations）系统性地列出了方法的边界条件。

### Appendix
- 28 页附录提供了极强的可复现性。特别是 Appendix G (Reproducibility Details, page 30) 包含了完整的超参数、硬件配置、随机种子信息。
- 但附录体量过大也暗示主文的信息选择可能需要调整——部分关键分析（如 CF-DR trade-off 的定量分析 Table 5）放在附录而非主文，影响了主文的自包含性。

## 格式合规检查

| 检查项 | 结果 | 备注 |
|--------|------|------|
| ACL 模板 (`\usepackage[review]{acl}`) | ✓ | |
| Double-blind (Anonymous ACL submission) | ✓ | |
| 正文页数 ≤ 8 | ✓ | 正文结束于 page 8 底部 |
| Limitations section 位置 | ✓ | Conclusion 之后、References 之前 (page 9) |
| Limitations 为独立 section | ✓ | `\section*{Limitations}` |
| Ethics Statement | ✓ | Page 9，在 Limitations 之后 |
| Abstract ≤ 200 words | ✓ (borderline) | 约 190 words，接近上限 |
| References 格式一致性 | ✓ | ACL 标准格式 |
| 无内容溢出到第 9 页 | ✓ | `\clearpage` 确保 Limitations 另起一页 |

## 总体评分

**Overall**: 3.0 — Findings
**一句话总结**: 工程贡献扎实、评估极其全面的约束解码框架，但核心新颖性有限（本质是 XGrammar + stateful type checker 的自然组合），且缺少与最直接竞争者（GoLLIE）和监督 baseline 的实验对比，难以支撑 main conference 接收。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 形式化正确，实验设计严谨，但 F1 绝对值低且缺少监督 baseline 参照使得 claim 的实际意义不够清晰 |
| Excitement | 2.5/5 | 架构是已有技术的自然组合；Proposition 1 形式化已知直觉；CF trade-off 分析有价值但不构成突破性贡献 |
| Reproducibility | 5/5 | 28 页附录含完整超参数、种子、硬件配置、prompt 模板；承诺 code release |
| Overall Assessment | 3.0/5 | Findings 水平——扎实的工程工作和全面评估，但 novelty 不足以进入 main conference |
| Confidence | 4/5 | 熟悉约束解码和结构化生成领域，仔细阅读了全文及全部附录 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] 缺少监督 baseline F1 参考线
- 具体位置：Table 2 / Section 5
- 问题：R-F1 42-47% 在绝对值上远低于监督方法，但论文完全没有提供参照
- 为什么影响接收：无法判断方法的实际价值
- 建议：添加 SOTA supervised R-F1 数字作为 reference（引用已发表结果即可）

**N2** [critical] GoLLIE 对比缺失
- 具体位置：Section 7, Appendix S
- 问题：最直接可比的方法被推迟到 future work
- 为什么影响接收：novelty claim 缺少关键支撑
- 建议：至少提供 approximate comparison 或 controlled ablation

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract F1 范围不准确（"40-46%" vs 实际 42-47%）
**W2** [warning] Contribution 1 对 Mistral fine-tuning 覆盖的暗示性声称
**W3** [warning] WikiEvents 作为 "third dataset" 的定位与实际评估深度不符
**W4** [warning] Proposition 1 的 novelty overclaim

## 小问题（不影响接收）
- Abstract 末句 "with scale- and schema-dependent layer interaction" 语法不完整
- Section 5 缩写密度过高
- Related Work 篇幅过长（>1 page / 8 pages total）
- Table 1 可读性可改善（标注 key configurations）

## 主要优势
- 评估全面性在同类工作中罕见（28 页附录）
- Limitations section 诚实坦率
- CF-DR trade-off 的量化分析有实际指导价值
- 框架设计 model-agnostic，与 fine-tuning 正交可组合
- Constraint tightness κ 提供了有用的诊断框架


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2602 · 2026-05-23T12:43:40.680004+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 191

## Round 191

2 recorded events


### User

_source line 2603 · 2026-05-23T12:43:53.959840+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**Overall 3.0（Findings 水平）**。论文工程贡献扎实、评估全面性罕见（28 页附录），但两个 critical 问题影响接收——(1) 绝对 F1 仅 42-47% 却完全缺失监督 baseline 参照，(2) 与最直接竞争者 GoLLIE 的实验对比被推迟到 future work。核心架构（XGrammar + stateful type checker）是已有技术的自然组合，Proposition 1 形式化的是已知直觉而非新洞察。CF-DR trade-off 分析和 constraint tightness κ 概念有诊断价值，格式完全合规。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2604 · 2026-05-23T12:44:02.597078+00:00_

Reviewer 2 报告已收到（Overall 3.0 Findings）。等待 Reviewer 1 报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 192

## Round 192

6 recorded events


### User

_source line 2605 · 2026-05-23T12:44:30.157329+00:00_

[Reviewer 1 审稿意见]:

## Summary

OntoCoDec 提出将 IE 本体约束编译为 token-level 解码约束的框架，采用两层架构：grammar layer（基于 XGrammar）保证 JSON 结构和词汇合法性，semantic layer 通过运行时 entity registry 执行 domain/range 类型约束。论文包含 Proposition 1（pumping lemma 证明 domain/range 约束超越 context-free 表达力）和在 SciERC、DocRED、WikiEvents 上的大规模实验。论文非常详尽（40 页，48+ 表格），统计方法规范。

## Strengths

**S1. 新颖且实用的编译框架。** 将 IE 本体约束系统性地编译为解码掩码的想法在 IE 领域是新颖的。两层架构（grammar + semantic）的设计有理论支撑（Proposition 1），将 context-free 可处理的约束与需要运行时状态的约束清晰分离。框架可适用于任意自回归 LLM，不需要模型特定训练。

**S2. 极其充分的实验。** 跨 3 个 8B 模型（Qwen3-8B, Llama-3.1-8B, Mistral-7B）、2 个主数据集 + 1 个 pilot 数据集、zero-shot + fine-tuning 设置的全面评估。5-way ablation（Table 1）、4-way fine-tuning ablation（Tables 10-11）、beam search 兼容性（Tables 23-28）、prompt sensitivity（Table 34）等消融实验覆盖面远超平均水平。

**S3. 严谨的统计方法。** Bootstrap CIs（10,000 iterations, document-level resampling）、Bonferroni correction for k=4 comparisons（α_adj=0.0125）、Cohen's d effect sizes、统计 power analysis（Table 30）的使用在 NLP 论文中属于上乘水准。所有 DR reduction 结果均经过显著性检验。

**S4. 诚实的局限性披露。** 论文在 Limitations（§8）和 Discussion（§7）中明确讨论了 CF trade-off、per-triple enforcement 的架构限制、WikiEvents 的 preliminary 性质、70B 仅用单一模型族等问题。这种透明度值得肯定。

**S5. 良好的可复现性。** Appendix G 提供了详细的超参数、硬件配置（NVIDIA RTX PRO 6000）、随机种子（42, 123, 456）、推理时间等信息。200-document subset justification（§30, p30）论证了 subsampling 的统计充分性。

## Weaknesses

### Critical

**W1. [Critical] DR→CF Trade-off 的框架性问题——净收益在 zero-shot 下远不如 DR reduction 数字所暗示的那么大。**

- 具体位置：Abstract, §5.1 Table 1, §4 Constraint Tightness
- 问题：论文的核心 claim 是 DR reduction to near-zero（<0.21%），但在 zero-shot 下，S1 配置将 DR 从 15.37% 降至 0.17% 的同时，CF 从 0.08% 升至 9.85%（Table 1, SciERC, Qwen3-8B）。总违规率从约 16.7% 降至约 10.1%，即净降幅仅约 40%，远低于 DR 单项 99% 的降幅给读者的印象。Abstract 突出了 DR reduction（"reduces domain/range violations to near zero"），CF increase 被表述为可通过 beam search 缓解的次要问题，但 beam search 带来 1.38× latency 开销，在实际部署中并非免费。
- 为什么影响接收：如果一个约束系统将一种违规转换为另一种违规，净效果应该是论文的核心叙事焦点。当前框架可能误导读者高估该系统的实际 schema compliance 改善。
- 建议：(1) 在 Abstract 和 §5.1 中增加 total violation reduction 的明确报告；(2) 将 CF increase 与 DR reduction 并列为主要发现，而非将 CF 降格为"architectural consequence"。

### Major

**W2. [Major] WikiEvents n=20 不足以支撑 task generalization claim。**

- 具体位置：Abstract（"three...datasets"暗示三个同等重要的评估集）, §5.2, Appendix P
- 问题：WikiEvents 仅评估 20 篇文档，Table 30 显示其 MDE=2.0pp，95% CI 宽达 ±3.9pp。论文诚实地标注了"preliminary"，但 Abstract 将其与 SciERC（551 docs）和 DocRED（998 docs）并列提及，给读者造成三个数据集提供同等证据的印象。n=20 的统计效力不足以支撑任何可靠结论，特别是事件抽取与关系抽取在 schema 结构上有本质差异（event roles vs. binary relations）。
- 建议：(1) 从 Abstract 的主要 claim 中移除 WikiEvents 或明确标注 preliminary；(2) 扩展评估到至少 100+ 文档以提供有意义的统计结论。

**W3. [Major] 70B scale-dependent findings 仅基于单一模型族+INT4 量化，因果解释不足。**

- 具体位置：§5.1（scale-dependent layer interaction）, §7 Discussion, Table 2
- 问题：Scale-dependent interaction（8B: 24% vs 70B: 84% independent DR reduction）是论文的一个重要发现，但仅基于 Llama-3.1-70B AWQ INT4 vs. 三个 8B 模型的比较。这混淆了三个变量：(a) 模型规模（8B vs 70B）, (b) 模型族（Qwen/Mistral vs. Llama）, (c) 量化方式（FP16 vs. INT4）。论文假设差异主要源于"improved vocabulary calibration"（§7），但没有控制实验排除其他因素。特别是，INT4 量化本身可能影响 logit 分布和约束执行效果，Appendix R 仅验证了"constraint enforcement is preserved under INT4 quantization (4× compression)"，但未对比 FP16 vs INT4 在 70B 上的差异。
- 建议：至少增加一个 70B 模型（如 Qwen-72B）或提供 INT4 vs FP16 对比，以分离 scale 效应和 model-family/quantization 效应。

**W4. [Major] Proposition 1 的形式化构造与实际 JSON 输出格式之间存在 gap。**

- 具体位置：Appendix O (p37), §3.1
- 问题：Proposition 1 的证明使用 position-indexed entity references（e_1, e_2, ..., e_n），其中 pumping 通过改变实体位置来破坏类型约束。但论文的实际系统（§3.1）使用 name-based entity references——实体通过名称字符串引用，而非位置索引。在 name-based scheme 下，pumping lemma 的 Case 1 论证（"shifts e_n's position → reference now points to wrong entity"）不直接成立，因为名称引用不受插入新实体的影响。虽然 non-CF-ness 的核心洞察（类型一致性需要跨输出的状态跟踪）是正确的，但证明的具体构造需要更紧密地匹配实际编码格式，或者明确声明证明适用于哪些编码方案。
- 为什么影响接收：如果 Proposition 1 是两层架构的理论基础，其证明的形式化需要无可挑剔。当前证明对 position-based encoding 是正确的，但对 name-based encoding 的适用性未经论证。
- 建议：(1) 明确 Proposition 1 的前提条件（适用于哪类编码方案）；(2) 或者调整证明以直接使用 name-based reference scheme，展示在该 scheme 下 pumping 如何破坏类型约束。

### Minor

**W5. [Minor] CF increase 缺少与 DR reduction 同等的统计检验。**

- 具体位置：§5.1, Table 6
- 问题：DR reduction 得到了完整的 bootstrap + Bonferroni 处理（Table 6, Cohen's d ≥ 3.0），但 CF increase 没有经过同等的显著性检验。论文在 Table 5 报告了 CF 的绝对值，但没有 p-value 或 CI。作为论文承认的主要 trade-off，CF 变化的统计显著性应该与 DR 同等对待。
- 建议：为 CF increase 补充 bootstrap CI 和显著性检验。

**W6. [Minor] First-seen entity registry semantics 的经验分析不充分。**

- 具体位置：§3.3, Table 7（Appendix C）
- 问题：Table 7 显示 GENERIC type 占 CF violations 的 63.3%（155/245 unique conflicts），表明 entity type polysemy 是实际场景中的重要问题。First-seen semantics 的设计选择——以第一次出现的类型锁定后续所有引用——在类型模糊的实体上会系统性地产生错误。论文在 §3.3 简要讨论了这一点，但缺乏对不同 registry 策略（如 majority voting, type inheritance）的实验对比。
- 建议：至少讨论 first-seen 策略在不同类型模糊度下的表现差异（Table 14 的 lucky violation analysis 提供了部分数据，但不够系统）。

**W7. [Minor] Abstract 可能超过 200 words 限制。**

- 具体位置：p1 Abstract
- 问题：EMNLP 2026 限制 abstract 不超过 200 words。从 PDF 视觉判断，当前 abstract 看起来接近或可能超过这一限制（约 230-240 words）。
- 建议：精简 abstract 以确保符合格式要求。

**W8. [Minor] LoRA 超参数跨数据集迁移。**

- 具体位置：§5 Setup, Appendix G
- 问题：LoRA 超参数（rank=16, lr=2e-5 等）在 SciERC 上调优后直接迁移到 DocRED，未进行 dataset-specific tuning。论文承认这"may underestimate DocRED potential"（Limitations §8），但评估结果仍然以现有配置呈现为 DocRED 的能力上界。
- 建议：至少在 DocRED 上做一个小规模超参搜索或 sensitivity analysis。

## Questions

**Q1.** 论文报告 S1 配置下 zero-shot total violation rate 约为 DR(0.17%) + CF(9.85%) + RV(0.08%) + ET(0%) ≈ 10.1%，相比 unconstrained 的 ~16.7%（DR 15.37% + RV 1.28% + ET 0.08%）。请问作者如何看待这一净降幅（约 40%）？在什么场景下，将 DR 转换为 CF 是一个净正向改善？

**Q2.** Proposition 1 的证明使用 position-based entity references。如果实际系统使用 name-based references（如 JSON 中的字符串名称），pumping lemma 的 Case 1 论证是否仍然成立？请解释。

**Q3.** Scale-dependent interaction 的 vocabulary calibration hypothesis（§7）——有没有直接证据表明 70B 模型的 logit 分布更集中在 ontology-valid tokens 上？还是只是从 fallback frequency gap 间接推断？

**Q4.** Grammar-first fallback（§4）的频率在 fine-tuned models 上急剧下降（Qwen-8B LoRA+S1 触发 0 次 grammar-first fallback on SciERC vs. Llama-8B 触发 5,882 次——Table 10）。这一 100× 差异是否暗示 fallback 行为高度依赖于 model-specific tokenizer alignment？如果是，框架的 model-agnostic claim 是否需要限定？

**Q5.** Beam search（k=4）在 SciERC 上消除了所有 CF violations（Table 23-24），但这是否引入了 recall 损失？论文提到 beam search "recovers valid type assignments that greedy decoding missed"，但 R-F1 变化未单独报告 precision/recall breakdown。

## Missing References

- **Guidance (Microsoft, 2023)**：另一个将约束编译到解码的框架，虽然更偏工程工具，但在约束编译理念上与 OntoCoDec 有共通之处。
- **DyGIE++ (Wadden et al., 2019)**：SciERC 上的经典 span-based IE baseline，论文使用 SciERC 但未将其作为 IE baseline 对比（可以理解为 OntoCoDec 是约束框架而非 IE 系统，但值得在 Related Work 中提及）。
- **DeepStruct (Wang et al., 2022)**：大规模结构化预测，与 constrained generation for IE 相关。

## Detailed Comments

### §1 Introduction
- Introduction 的叙事结构清晰：problem → limitation of existing approaches → proposed solution → contributions。三个 contributions 明确且有实验支撑。
- "eliminates all violation types at 8B at 1.39× latency"的措辞需要限定——这仅在 beam search (k=4) + LoRA fine-tuning 下成立，greedy decoding 下 CF 仍然存在。

### §3 Method
- 两层架构的描述清楚。Entity registry 的 first-seen semantics 在 §3.3 中有合理的动机解释。
- Grammar-first fallback（§4）是一个关键设计选择——当 S(t) ∩ G(t) = ∅ 时跳过 semantic masking。这个 fallback 是 CF violations 的主要来源（Table 4 确认：所有 18 个 residual DR violations 发生在 fallback positions）。论文应更早、更突出地讨论这一 trade-off。

### §5 Experiments
- Five-way ablation（Table 1）设计合理，分离了 grammar layer、semantic layer 和 decoding strategy 的各自贡献。
- Table 6 的 Bootstrap CIs 和 Bonferroni correction 使用正确。
- DocRED 评估使用 998 dev docs（因 test annotations 不公开），这是合理的选择但应在主文中更明确提及。
- Zero-shot cross-model validation（Table 48, Appendix Q）在 3 个 8B 模型上验证了一致性，增强了主实验的可信度。

### §7 Discussion
- Scale-dependent layer interaction 的讨论引人深思，但 causal explanation 过于 speculative。
- DR↔CF trade-off 的"Pareto optimal"分析（§19, Figure 2）仅基于 4 个 dataset configurations，数据点太少以支撑回归分析。
- Per-triple vs. global enforcement 的讨论（§7）诚实地承认了架构限制，但未讨论可能的解决方向（如 multi-pass constraint resolution）。

### Appendices
- Appendix O（Proposition 1 proof）：形式化方向正确但有上述 gap。
- Appendix J（Error Analysis and Case Studies）：四个 case studies 质量高，Case 4 特别有价值，展示了约束系统在 trajectory divergence 下的行为。
- Appendix K（Ontology Scalability）：compilation time 和 per-token overhead 的分析（Table 40）增强了实用性论证。

## Overall Assessment

- **Overall**: 3.5 (Borderline Conference)
- **一句话总结**: 新颖的约束编译框架，实验极其充分，但 DR→CF trade-off 的净收益在 zero-shot 下有限，且 scale-dependent findings 的证据基础过窄。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论合理，统计严谨；但 Proposition 1 有形式化 gap，CF trade-off framing 不够平衡，scale-dependent claims 证据不足 |
| Excitement | 3/5 | 编译 IE 本体约束到解码掩码的想法新颖实用，但 per-triple 架构限制（无法处理 cross-field consistency）降低了实际影响力；净违规改善在 zero-shot 下有限 |
| Reproducibility | 4/5 | 详细的超参数、硬件配置、随机种子；200-doc subset 的统计充分性论证；但代码尚未公开 |
| Confidence | 4/5 | 对约束解码和 IE 领域熟悉，仔细阅读了全部 40 页；形式语言理论方面有一定不确定性 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] DR→CF Trade-off 框架性问题
- 具体位置：Abstract, §5.1 Table 1, §4
- 见 W1 详述。Zero-shot 下净总违规仅降约 40%，与 DR 单项 99% 降幅的印象差距过大。需要在 abstract 和主文中明确报告 total violation change。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] WikiEvents n=20 → 从主要 claim 中降级或扩展
**W2** [warning] 70B 仅单一模型族 → 增加对照或限定 claim
**W3** [warning] Proposition 1 形式化 gap → 调整证明或声明适用范围
**W4** [warning] CF increase 缺少统计检验 → 补充 bootstrap CI

## 小问题（不影响接收）

- Abstract 可能超过 200 words（W7）
- LoRA 超参跨数据集迁移未做 sensitivity analysis（W8）
- Table 5 的 CF-DR trade-off pilot 仅 3 models × 2 datasets = 6 data points，难以支撑 Figure 2 的回归分析

## 主要优势

- 将 IE 本体约束系统性编译为解码掩码的新范式
- 极其充分的实验覆盖（40 页，48+ 表格，proper statistics）
- 诚实的局限性讨论和 trade-off 分析
- 良好的可复现性文档
- 框架的模型无关性使其可广泛应用


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2606 · 2026-05-23T12:45:35.495644+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对于每一个 Weakness、Question 和 Missing Reference，用 [AGREE] 表示同意并说明理由，或用 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的完整审稿报告\n\n### Summary\n本文提出 OntoCoDec，一个将 IE 本体编译为 token 级解码约束的框架。核心观察是 domain/range 类型约束超越 context-free 表达能力（Proposition 1），因此提出两层架构：grammar 层（基于 XGrammar）保证 JSON 结构和词汇合法性，semantic 层（基于 stateful logits processor + 动态 entity registry）在运行时执行类型约束。在 SciERC、DocRED、WikiEvents 上评估，涵盖 3 个 8B 级模型和 1 个 70B 模型。\n\n### Strengths\nS1. 问题形式化清晰。Proposition 1 虽然是对已知直觉的形式化，但 pumping lemma 证明严谨，为两层架构提供了充分的理论动机。\nS2. 评估极其全面。28 页附录覆盖了五路消融、四路约束消融、beam search 分析、文档长度分析等。\nS3. CF-DR trade-off 分析提供了真正的洞察。\nS4. Limitations section 诚实且全面。\nS5. 约束紧度 κ 概念有诊断价值。\nS6. 框架设计 model-agnostic，与 fine-tuning 正交可组合。\n\n### Weaknesses\n\n**W1. [Critical] 绝对 F1 低且缺失监督 baseline 对比**\n- fine-tuned 最优 R-F1 在 SciERC 约 44-45%、DocRED 约 42-47%。监督方法在 SciERC 上 R-F1 可达 60%+。论文完全没有与任何监督 IE baseline（如 PL-Marker, UniRE, OneRel）对比，读者无法判断约束执行在实际提取质量低下时的实用价值。\n\n**W2. [Critical] GoLLIE 对比刻意回避**\n- GoLLIE 是最直接可比的工作（同样面向 ontology-compliant LLM-based IE），但论文将对比推迟到 future work。附录 S 提供了 GCD-equivalent 的 grammar-only baseline 作为 proxy，但这不能代替与 GoLLIE 的实际对比。\n\n**W3. [Major] Abstract F1 范围与实际数据不一致**\n- Abstract 声称 \"at F1 40–46%\"，但 Table 2 中部分数据超出或低于此范围。\n\n**W4. [Major] Contribution 声称与实际覆盖不符（Mistral fine-tuning 缺失）**\n- Contribution 1 声称 \"Systematic ablation across 3 model families... under both zero-shot and LoRA fine-tuned settings\"，但 Mistral 仅有 zero-shot 结果。\n\n**W5. [Major] WikiEvents 评估过于初步**\n- WikiEvents 仅 n=20，将其计入 \"three datasets\" 有夸大之嫌。\n\n**W6. [Major] Proposition 1 的新颖性有限**\n- cross-field binding 超越 CFG 在编程语言理论中是公知常识。将此作为 \"key contribution\" 有 overclaim 倾向。\n\n**W7-W10. [Minor]** Related Work 篇幅过长；缩写密度过高；Table 1 可读性一般；Abstract 末句语法不完整。\n\n### Questions\nQ1. fine-tuned 下 CF 违规是否集中在某些高频 relation type 上？\nQ2. κ 与 per-relation F1 的关系？能否为\"何时使用约束解码\"提供指导？\nQ3. first-seen assignment 错误时 downstream cascade 影响有多大？deferred assignment 替代方案？\nQ4. OntoCoDec 与 GoLLIE 正交可组合——是否有初步实验验证？\n\n### Missing References\n- CRANE (Banerjee et al., 2025) 在 Related Work 中讨论不够充分\n- 缺少监督 IE 方法（PL-Marker, UniRE, OneRel）作为 F1 参考点\n- 缺少 constrained decoding survey 引用\n\n### Overall Assessment\n- Score: 3.0 (Findings)\n- Confidence: 4/5\n- Excitement: 2.5/5\n\n---\n\n请对以上每个 Weakness (W1-W10)、Question (Q1-Q4)、Missing Reference 逐条回应 [AGREE] 或 [REBUT]。",
  "project": "schema_semantic_constrained_ie",
  "chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对于每一个 Weakness、Question 和 Missing Reference，用 [AGREE] 表示同意并说明理由，或用 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的完整审稿报告\n\n### Summary\n本文提出 OntoCoDec，一个将 IE 本体编译为 token 级解码约束的框架。核心观察是 domain/range 类型约束超越 context-free 表达能力（Proposition 1），因此提出两层架构：grammar 层（基于 XGrammar）保证 JSON 结构和词汇合法性，semantic 层（基于 stateful logits processor + 动态 entity registry）在运行时执行类型约束。在 SciERC、DocRED、WikiEvents 上评估，涵盖 3 个 8B 级模型和 1 个 70B 模型。\n\n### Strengths\nS1. 问题形式化清晰。Proposition 1 虽然是对已知直觉的形式化，但 pumping lemma 证明严谨，为两层架构提供了充分的理论动机。\nS2. 评估极其全面。28 页附录覆盖了五路消融、四路约束消融、beam search 分析、文档长度分析等。\nS3. CF-DR trade-off 分析提供了真正的洞察。\nS4. Limitations section 诚实且全面。\nS5. 约束紧度 κ 概念有诊断价值。\nS6. 框架设计 model-agnostic，与 fine-tuning 正交可组合。\n\n### Weaknesses\n\n**W1. [Critical] 绝对 F1 低且缺失监督 baseline 对比**\n- fine-tuned 最优 R-F1 在 SciERC 约 44-45%、DocRED 约 42-47%。监督方法在 SciERC 上 R-F1 可达 60%+。论文完全没有与任何监督 IE baseline（如 PL-Marker, UniRE, OneRel）对比，读者无法判断约束执行在实际提取质量低下时的实用价值。\n\n**W2. [Critical] GoLLIE 对比刻意回避**\n- GoLLIE 是最直接可比的工作（同样面向 ontology-compliant LLM-based IE），但论文将对比推迟到 future work。附录 S 提供了 GCD-equivalent 的 grammar-only baseline 作为 proxy，但这不能代替与 GoLLIE 的实际对比。\n\n**W3. [Major] Abstract F1 范围与实际数据不一致**\n- Abstract 声称 \"at F1 40–46%\"，但 Table 2 中部分数据超出或低于此范围。\n\n**W4. [Major] Contribution 声称与实际覆盖不符（Mistral fine-tuning 缺失）**\n- Contribution 1 声称 \"Systematic ablation across 3 model families... under both zero-shot and LoRA fine-tuned settings\"，但 Mistral 仅有 zero-shot 结果。\n\n**W5. [Major] WikiEvents 评估过于初步**\n- WikiEvents 仅 n=20，将其计入 \"three datasets\" 有夸大之嫌。\n\n**W6. [Major] Proposition 1 的新颖性有限**\n- cross-field binding 超越 CFG 在编程语言理论中是公知常识。将此作为 \"key contribution\" 有 overclaim 倾向。\n\n**W7-W10. [Minor]** Related Work 篇幅过长；缩写密度过高；Table 1 可读性一般；Abstract 末句语法不完整。\n\n### Questions\nQ1. fine-tuned 下 CF 违规是否集中在某些高频 relation type 上？\nQ2. κ 与 per-relation F1 的关系？能否为\"何时使用约束解码\"提供指导？\nQ3. first-seen assignment 错误时 downstream cascade 影响有多大？deferred assignment 替代方案？\nQ4. OntoCoDec 与 GoLLIE 正交可组合——是否有初步实验验证？\n\n### Missing References\n- CRANE (Banerjee et al., 2025) 在 Related Work 中讨论不够充分\n- 缺少监督 IE 方法（PL-Marker, UniRE, OneRel）作为 F1 参考点\n- 缺少 constrained decoding survey 引用\n\n### Overall Assessment\n- Score: 3.0 (Findings)\n- Confidence: 4/5\n- Excitement: 2.5/5\n\n---\n\n请对以上每个 Weakness (W1-W10)、Question (Q1-Q4)、Missing Reference 逐条回应 [AGREE] 或 [REBUT]。",
    "project": "schema_semantic_constrained_ie",
    "chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 2607 · 2026-05-23T12:46:00.481970+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24986
}
```

</details>

---


### Tool call

_source line 2608 · 2026-05-23T12:46:00.733567+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对于每一个 Weakness、Question 和 Missing Reference，用 [AGREE] 表示同意并说明理由，或用 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的完整审稿报告\n\n### Summary\nOntoCoDec 提出将 IE 本体约束编译为 token-level 解码约束的框架，采用两层架构：grammar layer 保证 JSON 结构和词汇合法性，semantic layer 通过运行时 entity registry 执行 domain/range 类型约束。论文包含 Proposition 1 和在 SciERC、DocRED、WikiEvents 上的大规模实验。\n\n### Strengths\nS1. 新颖且实用的编译框架。两层架构有理论支撑，将 CF 可处理的约束与需要运行时状态的约束清晰分离。\nS2. 极其充分的实验。跨 3 个 8B 模型、2+1 数据集、zero-shot + fine-tuning 设置。\nS3. 严谨的统计方法。Bootstrap CIs、Bonferroni correction、Cohen's d、统计 power analysis。\nS4. 诚实的局限性披露。\nS5. 良好的可复现性。\n\n### Weaknesses\n\n**W1. [Critical] DR→CF Trade-off 的框架性问题——净收益在 zero-shot 下远不如 DR reduction 数字所暗示的那么大。**\n- Zero-shot S1: DR 15.37%→0.17%，CF 0.08%→9.85%。总违规率从约 16.7% 降至约 10.1%，净降幅仅约 40%。Abstract 突出 DR reduction，CF increase 被降格为次要问题。如果一个约束系统将一种违规转换为另一种违规，净效果应该是核心叙事焦点。\n\n**W2. [Major] WikiEvents n=20 不足以支撑 task generalization claim。**\n- MDE=2.0pp, 95% CI 宽达 ±3.9pp。n=20 的统计效力不足以支撑任何可靠结论。\n\n**W3. [Major] 70B scale-dependent findings 仅基于单一模型族+INT4 量化，因果解释不足。**\n- 混淆三个变量：模型规模、模型族、量化方式。vocabulary calibration hypothesis 缺直接证据。\n\n**W4. [Major] Proposition 1 的形式化构造与实际 JSON 输出格式之间存在 gap。**\n- 证明使用 position-indexed entity references，但实际系统使用 name-based references。pumping lemma Case 1 论证在 name-based scheme 下不直接成立。\n\n**W5. [Minor] CF increase 缺少与 DR reduction 同等的统计检验。**\n**W6. [Minor] First-seen entity registry semantics 的经验分析不充分。**\n**W7. [Minor] Abstract 可能超过 200 words 限制。**\n**W8. [Minor] LoRA 超参数跨数据集迁移。**\n\n### Questions\nQ1. zero-shot 下净总违规仅降约 40%——在什么场景下，将 DR 转换为 CF 是净正向改善？\nQ2. Proposition 1 证明使用 position-based references，name-based 下 pumping lemma Case 1 是否仍成立？\nQ3. vocabulary calibration hypothesis 有直接证据还是仅间接推断？\nQ4. Qwen-8B 触发 0 次 fallback vs Llama-8B 触发 5,882 次——100× 差异是否暗示 fallback 行为高度依赖 model-specific tokenizer？\nQ5. Beam search (k=4) 消除 CF 是否引入 recall 损失？\n\n### Missing References\n- Guidance (Microsoft, 2023)\n- DyGIE++ (Wadden et al., 2019)\n- DeepStruct (Wang et al., 2022)\n\n### Overall Assessment\n- Score: 3.5 (Borderline Conference)\n- Confidence: 4/5\n- Excitement: 3/5\n\n---\n\n请对以上每个 Weakness (W1-W8)、Question (Q1-Q5)、Missing Reference 逐条回应 [AGREE] 或 [REBUT]。",
  "project": "schema_semantic_constrained_ie",
  "chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对于每一个 Weakness、Question 和 Missing Reference，用 [AGREE] 表示同意并说明理由，或用 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的完整审稿报告\n\n### Summary\nOntoCoDec 提出将 IE 本体约束编译为 token-level 解码约束的框架，采用两层架构：grammar layer 保证 JSON 结构和词汇合法性，semantic layer 通过运行时 entity registry 执行 domain/range 类型约束。论文包含 Proposition 1 和在 SciERC、DocRED、WikiEvents 上的大规模实验。\n\n### Strengths\nS1. 新颖且实用的编译框架。两层架构有理论支撑，将 CF 可处理的约束与需要运行时状态的约束清晰分离。\nS2. 极其充分的实验。跨 3 个 8B 模型、2+1 数据集、zero-shot + fine-tuning 设置。\nS3. 严谨的统计方法。Bootstrap CIs、Bonferroni correction、Cohen's d、统计 power analysis。\nS4. 诚实的局限性披露。\nS5. 良好的可复现性。\n\n### Weaknesses\n\n**W1. [Critical] DR→CF Trade-off 的框架性问题——净收益在 zero-shot 下远不如 DR reduction 数字所暗示的那么大。**\n- Zero-shot S1: DR 15.37%→0.17%，CF 0.08%→9.85%。总违规率从约 16.7% 降至约 10.1%，净降幅仅约 40%。Abstract 突出 DR reduction，CF increase 被降格为次要问题。如果一个约束系统将一种违规转换为另一种违规，净效果应该是核心叙事焦点。\n\n**W2. [Major] WikiEvents n=20 不足以支撑 task generalization claim。**\n- MDE=2.0pp, 95% CI 宽达 ±3.9pp。n=20 的统计效力不足以支撑任何可靠结论。\n\n**W3. [Major] 70B scale-dependent findings 仅基于单一模型族+INT4 量化，因果解释不足。**\n- 混淆三个变量：模型规模、模型族、量化方式。vocabulary calibration hypothesis 缺直接证据。\n\n**W4. [Major] Proposition 1 的形式化构造与实际 JSON 输出格式之间存在 gap。**\n- 证明使用 position-indexed entity references，但实际系统使用 name-based references。pumping lemma Case 1 论证在 name-based scheme 下不直接成立。\n\n**W5. [Minor] CF increase 缺少与 DR reduction 同等的统计检验。**\n**W6. [Minor] First-seen entity registry semantics 的经验分析不充分。**\n**W7. [Minor] Abstract 可能超过 200 words 限制。**\n**W8. [Minor] LoRA 超参数跨数据集迁移。**\n\n### Questions\nQ1. zero-shot 下净总违规仅降约 40%——在什么场景下，将 DR 转换为 CF 是净正向改善？\nQ2. Proposition 1 证明使用 position-based references，name-based 下 pumping lemma Case 1 是否仍成立？\nQ3. vocabulary calibration hypothesis 有直接证据还是仅间接推断？\nQ4. Qwen-8B 触发 0 次 fallback vs Llama-8B 触发 5,882 次——100× 差异是否暗示 fallback 行为高度依赖 model-specific tokenizer？\nQ5. Beam search (k=4) 消除 CF 是否引入 recall 损失？\n\n### Missing References\n- Guidance (Microsoft, 2023)\n- DyGIE++ (Wadden et al., 2019)\n- DeepStruct (Wang et al., 2022)\n\n### Overall Assessment\n- Score: 3.5 (Borderline Conference)\n- Confidence: 4/5\n- Excitement: 3/5\n\n---\n\n请对以上每个 Weakness (W1-W8)、Question (Q1-Q5)、Missing Reference 逐条回应 [AGREE] 或 [REBUT]。",
    "project": "schema_semantic_constrained_ie",
    "chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 2609 · 2026-05-23T12:46:02.143916+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1410
}
```

</details>

---


### Assistant

_source line 2610 · 2026-05-23T12:46:05.698139+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 193

## Round 193

2 recorded events


### User

_source line 2611 · 2026-05-23T12:46:08.253629+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**Overall 3.5（Borderline Conference）**。

主要发现：
- **最关键问题**：DR→CF trade-off 的净收益在 zero-shot 下远不如 DR 单项数字暗示的那么大（总违规仅降约 40%，非 99%），abstract 框架性不平衡
- **三个 Major 问题**：WikiEvents n=20 不足以支撑 generalization claim；70B 仅单一模型族+INT4 量化混淆了 scale/family/quantization 三个变量；Proposition 1 证明的 position-based 构造与实际 name-based JSON 格式存在 gap
- **主要优势**：编译 IE 本体约束到解码掩码的想法新颖，实验极其充分（40 页 48+ 表格），统计方法规范（bootstrap + Bonferroni + effect sizes），局限性讨论诚实

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2612 · 2026-05-23T12:46:16.653321+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 194

## Round 194

2 recorded events


### User

_source line 2613 · 2026-05-23T12:47:42.148806+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Weaknesses

**[REBUT] R2-W1: 绝对 F1 低且缺失监督 baseline 对比**

R2 的核心论点是 R-F1 仅 44-45%，而监督方法达 60%+，因此质疑约束执行的实用价值。我认为这混淆了论文的定位。OntoCoDec 明确定位为**约束执行框架**（§1: "compiles IE ontologies into composable token-level decoding constraints"），而非 IE 系统本身。它与 LLM-based IE pipeline 正交可组合（§7 Discussion 和 §5.1 Composability）。

与监督 span-based 方法（PL-Marker, UniRE, OneRel）的直接 F1 对比在方法论上不合理：(1) 这些方法不生成文本，不存在 domain/range violation 问题；(2) 它们使用完全不同的架构（span enumeration/table filling），约束执行对它们无意义。论文的正确对比对象是其他**约束执行方法**——Appendix S (Table 17) 对比了 GCD-equivalent grammar-only baselines，Table 15 对比了 trie-only baseline，Table 12 对比了 post-hoc filtering。

不过，R2 有一个合理的 sub-point：读者需要**绝对 F1 的上下文参考**。论文可以在 §5 Setup 中加一句说明当前 LLM-based IE 的 SOTA 水平作为读者参照，而不必将其作为 baseline 对比。这是 framing 问题，不是实验设计缺陷。

**[REBUT] R2-W2: GoLLIE 对比刻意回避**

R2 称论文"刻意回避"GoLLIE 对比。论文实际上在多处讨论了 GoLLIE：Related Work（§6/Appendix B, p15）详细分析了 GoLLIE 的 training-time enforcement 与 OntoCoDec 的 inference-time enforcement 的区别；§7 Discussion 讨论了两者的互补性；Appendix S (Table 17) 提供了 GCD-equivalent 实验验证 CFG-based enforcement 的等价性（差异 <0.5pp）。

GoLLIE 的核心差异在于它通过 annotation-guideline-guided fine-tuning 实现 schema compliance，依赖于 training data 和 guideline engineering。OntoCoDec 是 inference-time enforcement，不需要额外训练。直接 F1 对比需要控制训练数据、prompt 格式等大量变量，这不是一个简单的 baseline 添加——它需要一个独立的实验设计。论文将其列为 future work 是合理的，但"刻意回避"的措辞过于严厉。

将此评为 [Critical] 我认为偏高。GoLLIE 与 OntoCoDec 解决的是同一问题的不同层面（training-time vs. inference-time），缺少直接对比降低了论文的完整性但不构成方法论缺陷。

**[AGREE] R2-W3: Abstract F1 范围与实际数据不一致**

Abstract 声称 "at F1 40–46%"。Table 2 显示 DocRED fine-tuned（Qwen3-8B）R-F1 达 ~47%，超出此范围。这是一个准确性问题，应修正为实际范围（如 40-47%）。不过严重程度应为 Minor 而非 Major。

**[AGREE] R2-W4: Contribution 声称与实际覆盖不符（Mistral fine-tuning 缺失）**

如果 Contribution 1 声称 "3 model families under both zero-shot and LoRA fine-tuned settings"，但 Mistral-7B 仅有 zero-shot 结果（Table 2 中确实只有 Qwen3-8B 和 Llama-3.1-8B 的 fine-tuning 结果），则 claim 确实 overstated。应修改为 "2 model families under fine-tuned settings" 或补充 Mistral fine-tuning 实验。同意这是 Major 级别。

**[AGREE] R2-W5: WikiEvents 评估过于初步**

与我的 W2 一致。n=20 的统计效力不足以支撑 task generalization claim。论文应从 Abstract 的主要 claim 中降级 WikiEvents 或扩展评估规模。

**[REBUT] R2-W6: Proposition 1 的新颖性有限**

R2 认为 "cross-field binding 超越 CFG 在编程语言理论中是公知常识"，因此 Proposition 1 新颖性有限。我部分不同意。

首先，虽然 cross-reference binding 超越 CFG 在 PL 理论中确实是已知的（如变量声明-使用匹配），但将这一洞察具体应用于 IE 本体约束并形式化是有价值的——这为两层架构提供了 principled motivation，而非 ad hoc 设计。NLP 社区的大量工作（XGrammar, SGLang, LMQL 等）仍在尝试用纯 CFG-based constrained decoding 处理 IE，Proposition 1 解释了为什么这些方法在 domain/range constraints 上必然失败。

其次，论文并未将 Proposition 1 列为 "key contribution"。三个 listed contributions（§1 末尾）分别是：(1) framework + ablation, (2) decidability-driven layer decomposition, (3) scale-dependent interaction analysis。Proposition 1 是 contribution (2) 的一部分，作为设计 rationale 而非独立的理论贡献。R2 说 "overclaim" 不太准确。

不过，我认为论文可以更明确地 acknowledge 这一结果在 PL 理论中的已知性，加一句 "This result parallels well-known limitations of CFGs in programming language theory (e.g., type checking requires context-sensitive mechanisms)" 会使定位更诚实。

**[AGREE] R2-W7: Related Work 篇幅过长**

主文 Related Work（§6）约 1 页，加上 Appendix B 约 2.5 页，总共约 3.5 页。对于 8 页正文的论文，主文 RW 篇幅可以接受，但附录中的 RW 确实偏长。Minor 级别。

**[AGREE] R2-W8: 缩写密度过高**

DR, CF, RV, ET, S1, S2, FT, ZS 等缩写在 §5 中密集出现，确实影响可读性。Minor 级别但应改善。

**[AGREE] R2-W9: Table 1 可读性一般**

Table 1 的 5-way ablation 包含多个 violation rate columns + F1 columns，可读性确实可以改善（如增加 column grouping 或 heatmap shading）。Minor。

**[AGREE] R2-W10: Abstract 末句语法不完整**

如果 Abstract 末句确实语法不完整，应修正。Minor。

---

### Questions

**[对 R2-Q1 的评论] fine-tuned 下 CF 违规是否集中在某些高频 relation type 上？**

论文在 Table 7 (p21, Appendix C) 中部分回答了这个问题：GENERIC type 占 CF violations 的 63.3%（155/245 unique entity-document conflicts），说明 CF 高度集中在 entity type polysemy 的场景。Table 21 (p26) 进一步按 relation 分解了 DR violation rates。R2 的问题是合理的，论文有数据但分析可以更集中——特别是 fine-tuned 设置下的 per-relation CF distribution。

**[对 R2-Q2 的评论] κ 与 per-relation F1 的关系？**

这是一个很好的问题。论文引入了 constraint tightness κ（§4）但确实没有直接报告 κ vs. per-relation F1 的相关性。Table 21 (p26) 提供了 per-relation DR violation rates，Figure 2 (p20) 提供了 residual DR vs. schema restrictiveness 的散点图，但两者未直接连接到 per-relation F1。这是一个有价值的缺失分析——κ 如果能预测"约束解码在哪些 relation 上最有效"，将大大增强框架的实用指导价值。

**[对 R2-Q3 的评论] first-seen assignment 错误时 downstream cascade 影响有多大？**

论文在 Appendix C (Table 7, p21) 和 Appendix J (§J.4, p33) 中讨论了 cascade errors。Table 8 (p21) 报告 "true cascade errors" 仅占 CF violations 的 7.3%（18/248），大部分 CF 由 hallucinated entities（56.1%）和 correct-type locks（18.1%）驱动。Under fine-tuning, cascade errors 被"completely eliminated (0/22)"（Table 8, p21）。这表明 first-seen semantics 在 fine-tuned 设置下风险可控，但 zero-shot 下仍有非零影响。R2 提出的 deferred assignment 替代方案值得探索但不影响当前论文的 soundness。

**[对 R2-Q4 的评论] OntoCoDec 与 GoLLIE 正交可组合？**

论文在 §7 Discussion 和 Appendix S (Table 17) 中讨论了这一可能性，Table 17 的 vLLM guided_json 验证提供了间接证据（CFG enforcement 等价性），但确实没有直接的 OntoCoDec + GoLLIE 组合实验。这作为 future work 是合理的，但如果能提供哪怕是小规模的 pilot 实验，将显著增强论文的 impact。

---

### Missing References

**[REBUT] CRANE (Banerjee et al., 2025) 讨论不够充分**

论文实际上在多处引用了 CRANE：References (p10)、§7 Discussion（"consistent with CRANE (Banerjee et al., 2025)"讨论 CF-DR trade-off 与 CRANE 的一致性）。Appendix B (p15) 在 "Post-hoc Ontology Validation" 小节也讨论了 CRANE 的 constrained multi-field generation 方法。讨论篇幅可以接受——CRANE 使用 conditional generation 而非 constrained decoding，方法差异较大，不需要深度对比。

**[AGREE] 缺少监督 IE 方法作为 F1 参考点**

虽然我在 R2-W1 的 REBUT 中认为直接 baseline 对比不合理，但我同意论文应在 §5 Setup 中提供监督方法的 F1 数字作为**上下文参考**（如 "For reference, supervised span-based methods achieve 60%+ R-F1 on SciERC"），帮助读者理解绝对 F1 水平。这不是实验设计问题而是 presentation 问题。

**[AGREE] 缺少 constrained decoding survey 引用**

如果存在 constrained decoding 的综述论文，引用它会帮助读者理解该领域的全局图景。Minor。

---

### Overall Assessment 回应

R2 给出 3.0 (Findings)，Excitement 2.5/5。我认为这偏低。

R2 的两个 Critical issues（W1 监督 baseline 对比, W2 GoLLIE 对比）在我看来不构成 Critical 级别：W1 混淆了论文定位（约束框架 vs. IE 系统）；W2 将 complementary work 的缺失对比等同于方法论缺陷。如果降级这两个 issues 到 Major，论文的核心贡献——新颖的编译框架 + 极其充分的实验——足以支撑 Borderline Conference (3.5)。

我的评分维持 3.5 (Borderline Conference)。主要扣分来自 DR→CF trade-off 的 framing 问题和 scale-dependent claims 的证据不足，而非 R2 强调的绝对 F1 水平和 GoLLIE 对比缺失。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2614 · 2026-05-23T12:47:47.450718+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 195

## Round 195

2 recorded events


### User

_source line 2615 · 2026-05-23T12:47:50.820264+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 全部意见的逐条交叉回应。

核心判断：
- R2 的两个 Critical（W1 监督 baseline、W2 GoLLIE 对比）被我降级——W1 混淆了约束框架 vs. IE 系统的定位，W2 将 complementary work 缺失等同于方法论缺陷
- W3-W5、W7-W10 基本同意，多为 Minor/Major 级别的 presentation 或 coverage 问题
- W6（Proposition 1 新颖性）部分反驳——PL 理论中的已知性不否定其在 NLP 约束解码语境中的应用价值
- 维持我的 3.5 (Borderline Conference) 评分不变

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2616 · 2026-05-23T12:47:58.911740+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 196

## Round 196

12 recorded events


### User

_source line 2617 · 2026-05-23T12:49:45.595097+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Weaknesses 回应

### W1. [Critical] DR→CF Trade-off 的框架性问题

**[AGREE]** 部分同意 narrative framing 的问题，但对 "净违规率" 的算术框架持保留意见。

R1 指出 zero-shot S1 下总违规率从 ~16.7% 降至 ~10.1%，净降幅仅 ~40%，这个算术本身正确。Abstract 确实将 DR reduction 置于叙事主位，CF increase 被降格为从句（"but introduces cross-field type inconsistencies (≤1.4%) from per-triple enforcement"）——而 ≤1.4% 是 fine-tuned 数字，zero-shot 可达 12%。这种叙事不对称是有效的批评。

但我认为 R1 的 "净违规率" 简单相加框架忽略了一个关键区分：**DR 和 CF 的严重程度和可恢复性不同**。DR 违规意味着 triple 从本体论角度无效（relation 不接受该 entity type），通常需要丢弃；CF 违规意味着同一 entity 在不同 triple 中被赋予不同类型，但每个 triple 内部可能仍然有效。论文的 post-hoc type consensus resolution (Appendix M, Table 8) 证明 CF 可通过投票消除（fine-tuned 下 CF→0），而 DR 无法通过后处理修复。此外，beam search k=4 在 8B 模型上消除全部违规类型（Table 24, page 28），提供了完整的解决路径。

**建议**：论文应在 Abstract 和 Section 5 中更均衡地呈现 DR-CF trade-off，特别是 zero-shot 下的净效果。但评估 "净收益" 时应考虑违规类型的严重程度权重，而非简单相加。

---

### W2. [Major] WikiEvents n=20

**[AGREE]** 完全同意。这与我的 W5 一致。

n=20 的 MDE=2.0pp, 95% CI ±3.9pp，统计效力严重不足。Introduction (page 2) 说 "we validate on three English datasets" 但 WikiEvents 的评估深度远不及 SciERC（551 docs）和 DocRED（998 docs）。将其计入 "three datasets" 有夸大之嫌。Appendix P (page 38) 的结果虽然方向一致（constraint enforcement 有效），但置信区间过宽，无法得出可靠结论。

应降级为 "preliminary pilot" 或显著增加评估规模。

---

### W3. [Major] 70B scale-dependent findings 混淆变量

**[AGREE]** 同意混淆问题存在，但论文已提供部分控制。

R1 正确指出 70B 结果混淆了三个变量：模型规模、模型族（Llama vs Qwen）、量化方式（AWQ INT4 vs FP16）。论文用 Appendix R (page 39) 的 8B 量化消融（Qwen3-8B FP16 vs INT4 对比输出 byte-identical）部分控制了量化效应，但缺少 70B FP16 对比（硬件限制，Limitations page 9 line 88 已声明）。

Vocabulary calibration hypothesis（Section 7, page 8: "larger models assign higher probability to ontology-valid tokens"）确实仅有间接证据（fallback frequency gap, scale-dependent DR）。补充 token-level probability distribution 的直接分析（如比较 70B 和 8B 在 type-constrained positions 上的 logit 分布）将显著增强此 claim。

---

### W4. [Major] Proposition 1 形式化与实际系统的 gap

**[AGREE]** 在形式化构造与系统实现之间存在 gap 这一观察上同意；**[REBUT]** 在这是否 invalidate non-CF 结论上反驳。

R1 准确地指出了证明（Appendix O, page 37）使用 position-indexed entity references（`e_α` 指代第 α 个 entity），而实际系统使用 name-based references（`"head_entity": "John"`）。在 name-based scheme 下，pumping lemma Case 1 的论证（"pumping shifts positions, breaking references"）确实不直接成立——pumping 不改变名字，引用仍然有效。

然而，**non-CF 结论在 name-based scheme 下仍然成立**，只是需要不同的论证路径。Name-based references 引入了一个类似 copy language 的约束：entity 名字必须同时出现在 entity list（作为定义）和 relation field（作为引用），且关联的 type 必须满足 domain/range constraint。这本质上是 cross-serial dependency，已知超越 CFG 表达能力。因此 Proposition 1 的结论正确，但证明的直接适用性有 gap。

**建议**：论文应补充一段讨论，说明 position-based 证明为何可推广到 name-based scheme（或直接提供 name-based variant 的证明）。

---

### W5. [Minor] CF increase 缺少统计检验

**[AGREE]** 合理的一致性要求。论文为 F1 提供了 bootstrap CIs（Table 30, page 31），为 DR 提供了 per-relation breakdown（Tables 21, 26），但 CF increase 没有相应的置信区间或显著性检验。如果 DR reduction 值得严格统计量化，CF increase 也应如此。这是一个容易补救的缺陷。

---

### W6. [Minor] First-seen entity registry 分析不充分

**[AGREE]** 与我的 Q3 一致。Appendix C (page 17-18) 的 fallback causal tracing 分析了 grammar-first fallback 发生的条件（所有 18 个 residual DR violations 仅在 fallback positions 出现），但没有深入分析 first-seen assignment 错误的 cascade 效应。论文提到 "CF increase 来自 per-triple enforcement"，但没有量化：在 CF violations 中，有多少源于 first-seen assignment 错误 vs. legitimate type ambiguity？这一分解在 Limitations (page 9, line 76) 被承认为缺失。

---

### W7. [Minor] Abstract 可能超过 200 words

**[REBUT]** 我的逐词计数结果约 186-190 words，在 200 word 限制内。

逐段计数：
- Para 1（问题陈述）：~43 words
- Para 2（方法概述）：~52 words  
- Para 3（实验结果）：~91 words
- 总计：~186 words

即使将 hyphenated compounds（如 "grammar-constrained", "cross-field", "8B-class"）各计为 2 words，总数仍在 ~195 左右，未超过 200。ARR 通常以 whitespace-separated tokens 计数。

---

### W8. [Minor] LoRA 超参数跨数据集迁移

**[AGREE]** 合理关注。Limitations (page 9, line 82) 已明确声明 "LoRA hyperparameters were tuned on SciERC and transferred to DocRED without dataset-specific optimization, which may underestimate DocRED potential"。但这一 limitation 仅在 Limitations section 提及，Section 5 的实验叙述中没有提醒读者注意此 caveat，可能导致读者高估 DocRED 结果的最优性。

---

## Questions 回应

### Q1. 什么场景下 DR→CF 转换是净正向改善？

**[AGREE]** 这是一个论文应更明确回答的关键问题。我的分析：

1. **Fine-tuned 场景**（论文推荐的 deployment setting）：CF ≤1.4%，DR→0%，净效果明确正向
2. **需要 ontological validity 的 downstream 任务**（如 knowledge graph population）：DR 违规使 triple 不可用，CF 违规的 triple 在单独看时可能仍有效
3. **与 beam search 组合时**：k=4 消除全部违规，无 trade-off
4. **Zero-shot + greedy decoding**（最差情况）：净收益确实有限，论文应更坦率

论文应在 Section 7 添加一段 "deployment recommendations"，明确哪些配置适合哪些场景。

### Q2. Proposition 1 name-based references

已在 W4 回应中详述。**[AGREE]** 证明需要补充 name-based variant 的讨论。结论仍然成立（cross-serial dependency 论证），但当前证明的直接适用性有 gap。

### Q3. Vocabulary calibration hypothesis 的证据

**[AGREE]** 仅有间接推断。Section 7 (page 8) 列出的证据链：(1) 更大模型 fallback 频率更低 → (2) 推测更大模型对 ontology-valid tokens 赋予更高概率 → (3) 因此 semantic layer 独立贡献更大。步骤 (1)→(2) 缺少直接验证（如对比不同模型在 type-constrained positions 的 token probability distributions）。

### Q4. Qwen-8B vs Llama-8B fallback 差异

**[AGREE]** 这是一个重要观察。100× 差异（0 vs 5,882）强烈暗示 fallback 行为高度依赖 tokenizer 的 type name encoding。Section 7 (page 8) 仅说 "fallback frequency does not determine enforcement effectiveness"，但没有解释 *why* 差异如此之大。

可能解释：Qwen tokenizer 将所有 type name 编码为 vocabulary 内的 distinguishable prefixes，使 continuation masking 从不需要 fallback；而 Llama tokenizer 对某些 type name 产生 ambiguous prefix splits（如 Appendix K, page 32 提到的 "morphologically similar types"）。论文应提供此分析。

但 R1 的暗示——fallback 依赖性损害 generalizability——需要平衡看待：Table 2 (page 6) 显示两个模型在 fine-tuned 配置下均达到 DR≤0.21%，说明尽管 fallback 行为不同，最终 enforcement 效果一致。

### Q5. Beam search k=4 recall 损失

**[REBUT]** 基于论文证据，beam search k=4 不引入 recall 损失，反而略微提升 F1。

Table 24 (page 28) 显示 beam k=4 on Qwen3-8B SciERC：DR=0, CF=0, R-F1 提升 +0.7pp。Page 27 Discussion 段落说明："beam search recovering valid type assignments that greedy decoding missed due to constraint fallback"——即 beam search 通过探索替代 token sequences 恢复了 greedy decoding 因 fallback 而错过的 valid assignments。

DocRED 上（page 28）："beam search reduces DR by 25% relative"，但 entity misclassification 仍存在——这不是 recall loss，而是 beam exploration 无法修复的 model calibration issue。

---

## Missing References 回应

### Guidance (Microsoft, 2023)

**[AGREE]** 值得在 Related Work Section 6 的 Grammar-Constrained Decoding (page 7) 段落中提及。Guidance 是主要的 constrained decoding library之一，与 XGrammar、Outlines 同属该技术栈。不影响论文的技术贡献，但完整性上应该引用。

### DyGIE++ (Wadden et al., 2019)

**[AGREE]** 与我的 N1 一致。DyGIE++ 是 SciERC 上的标准监督 baseline（SciERC 原始 evaluation paper 即使用 DyGIE++）。即使不做 controlled experiment，引用其 F1 数字作为参照线（~63% Rel-F1 on SciERC）将帮助读者定位 OntoCoDec 的 F1 42-47% 在领域中的位置。

### DeepStruct (Wang et al., 2022)

**[AGREE]** 弱同意。DeepStruct 将结构化预测建模为 seq2seq，与 OntoCoDec 的 structured generation 范式有关联。但相关性不如 DyGIE++ 和 Guidance 直接。可在 Related Work 中简要提及。

---

## 总结

Reviewer 1 的审稿质量很高。在 8 个 Weaknesses 中，我 [AGREE] 6 个（W1 部分同意、W2、W3、W5、W6、W8），[REBUT] 1 个（W7），[AGREE on observation but REBUT on implication] 1 个（W4）。

**我与 R1 的最大分歧**在于：
1. **Overall score**：R1 给 3.5 (Borderline Conference)，我给 3.0 (Findings)。我认为 R1 可能对 novelty 的评估偏高——两层架构本质上是 XGrammar + stateful type checker 的自然组合，Proposition 1 是对已知直觉的形式化。R1 的 S1 称其 "新颖且实用"，但我认为实用性强于新颖性。
2. **CF-DR trade-off 的严重程度**：R1 将此列为唯一 Critical weakness，我认为缺少监督 baseline 对比和 GoLLIE 对比回避同样是 Critical 级问题（但 R1 未提及这两点）。

**R1 未提及但我认为重要的问题**：
- 绝对 F1 低且缺少监督 baseline 参照（我的 N1/W1）
- GoLLIE 对比刻意回避（我的 N2/W2）
- Abstract F1 范围 "40-46%" 与实际 47.43% 不一致（我的 W3）


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2618 · 2026-05-23T12:50:24.982284+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2619 · 2026-05-23T12:50:25.183915+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T12:34:47.518278+00:00\", \"completed_at\": \"2026-05-23T12:38:30.265026+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"前两页为纯文本（Title/Abstract/Introduction/Background），无任何 display item。审稿人在前两页没有视觉锚点，需要翻到第 3 页才看到 Figure 1。建议考虑将核心结果的精简版（如 DR reduction 对比小表或 teaser figure）提前到第 1 页底部或第 2 页顶部\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（架构概览，figure* 全宽）是论文第一个 display item，出现在第 3 页顶部。图表清晰，caption 自包含，传达了两层约束编译架构的核心 message。位置可接受但不算早\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"正文 8 页仅有 3 个 display items（Figure 1 + Table 1 + Table 2），对于一篇实证为主的论文偏少（通常 5-8 个）。大量实验证据（~47 个表 + 3 个图）被推到 appendix，正文视觉密度不足\"}, {\"severity\": \"warning\", \"dimension\": \"page 7-8\", \"message\": \"Related Work（p7）+ Discussion and Conclusion（p8）连续两页纯文本，无任何 figure/table/equation 穿插。审稿人在正文尾段容易疲劳\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 和 Table 2 集中在同一页。两表均使用 booktabs 风格，最优值加粗，小数精度统一，格式专业。但两个关键结果表挤在一页略显拥挤\"}, {\"severity\": \"info\", \"dimension\": \"page 4-5\", \"message\": \"公式渲染正确，行内公式未导致行距异常。Method 部分公式与文字交替节奏可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段落简短合理（约一段），符合 EMNLP 要求。Ethics Statement 排版正常。References 从该页底部开始\"}, {\"severity\": \"info\", \"dimension\": \"page 10-12\", \"message\": \"References 页排版正常，无 overfull，无 [?] 未解析引用，格式统一\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Table 3（Prompt Templates）格式清晰，代码块排版整洁\"}, {\"severity\": \"warning\", \"dimension\": \"page 14-17\", \"message\": \"Appendix B（Extended Related Work）连续 4 页纯文本，无任何 display item。虽然是 appendix，但审稿人翻阅时会感到单调\"}, {\"severity\": \"info\", \"dimension\": \"page 20\", \"message\": \"Figure 2（散点图）清晰可读，使用不同标记形状区分数据点，灰度打印友好\"}, {\"severity\": \"info\", \"dimension\": \"page 24\", \"message\": \"Figure 3（条形图）清晰，颜色区分度好\"}, {\"se
…[truncated 925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2620 · 2026-05-23T12:50:25.184422+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2621 · 2026-05-23T12:50:25.235011+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2622 · 2026-05-23T12:50:50.654944+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2623 · 2026-05-23T12:50:50.750767+00:00_

1	# Review Issues Tracker — schema_semantic_constrained_ie
2	# Updated: Post-R25 framing patch, 2026-05-23
3	
4	# ============================================================
5	# Round 25 — Issues resolved by framing optimization patch
6	# ============================================================
7	
8	- id: "R16-W5"
9	  summary: "Proposition 1 定位过高 + 理论-实践 gap 桥接不充分"
10	  category: framing
11	  severity: warning
12	  status: resolved
13	  first_raised_round: 14
14	  last_seen_round: 25
15	  mentions:
16	    - round: 19
17	      reviewers: [1, 2]
18	      note: "共识定位为 systems contribution。"
19	    - round: 23
20	      reviewers: [1, 2]
21	      note: "与 R23-W2/W7 合并。降低理论贡献措辞。"
22	    - round: 24
23	      reviewers: [1, 2]
24	      note: "R24-MF1 (critical)。R23 写作降级不够。"
25	    - round: 25
26	      reviewers: [1, 2]
27	      note: "R25 R1-W1+R2-W1 完全共识 [Major]。Framing patch 后 C1↔C2 互换（实证为 C1），Prop 1 从 bold theorem 降为 inline mention，§3 以 DFA state explosion 工程论证为主。"
28	  action_items:
29	    - round: 19
30	      action: "§7 Discussion 定位 systems contribution"
31	      assigned_to: paper_agent
32	      status: completed
33	    - round: 21
34	      action: "§3 论证 semantic layer 非显而易见"
35	      assigned_to: paper_agent
36	      status: completed
37	    - round: 23
38	      action: "降低 Proposition 1 强度 + κ 统计限定"
39	      assigned_to: paper_agent
40	      status: completed
41	    - round: 24
42	      action: "§1 C1 重写 'formalizing known intuition' + §3 DFA 可行边界 + proof sketch 扩展"
43	      assigned_to: paper_agent
44	      status: completed
45	    - round: 25
46	      action: "C1↔C2 swap + Prop 1 从 bold theorem 降为 inline + engineering motivation 为主"
47	      assigned_to: paper_agent
48	      status: completed
49	  resolution: "C1↔C2 互换完成——实证贡献（3模型×2数据集 ablation）提升为 C1，Prop 1 降为 C2 的 engineering motivation（inline mention + DFA state explosion）。§3 压缩 Prop 1 展示。"
50	  resolution_round: 25

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 95
}
```

</details>

---


### Tool call

_source line 2624 · 2026-05-23T12:53:18.610057+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: R26 fresh review, 2026-05-23\n\n# ============================================================\n# Round 26 — Active Issues\n# ============================================================\n\n- id: \"R26-W1\"\n  summary: \"DR→CF trade-off 在 Abstract/正文中 framing 不平衡——zero-shot 净违规仅降约 40%\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W1。Abstract framing 需更对称。\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R1-W1 [Critical]+R2 AGREE (with nuance)。完全共识。Zero-shot S1: DR 15.37%→0.17% 但 CF 0.08%→9.85%，总违规 16.7%→10.1% 仅降 40%。Abstract 突出 DR reduction，CF 被降格为从句且引用 fine-tuned 数字 (≤1.4%) 而非 zero-shot (up to 12%)。R2 补充：DR/CF 严重程度不同（DR 不可恢复 vs CF 可 post-hoc），simple 相加不公平，但叙事不对称确实存在。\"\n  action_items:\n    - round: 26\n      action: \"Abstract + §5 中同时报告 DR reduction 和 CF increase 的 net effect + total violation change；§7 Discussion 扩展 CF 实际影响分析 + deployment recommendations\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W2\"\n  summary: \"WikiEvents n=20 不足以支撑 task generalization claim\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 26\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"降级 contribution list + Preliminary Pilot 标题。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 多轮复发升级为 critical。\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R1-W2 [Major]+R2-W5 [Major]，完全共识。n=20, MDE=2.0pp, 95% CI ±3.9pp。Abstract 将其与 SciERC (551 docs) 和 DocRED (998 docs) 并列，暗示三个同等重要的评估集。两位 Reviewer 一致要求降级或扩展。\"\n  action_items:\n    - round: 26\n      action: \"从 Abstract 主 claim 中移除或明确标注 WikiEvents 为 preliminary pilot；§5.2 正文仅保留 1 句 feasibility mention，详细结果留 Appendix\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W3\"\n  summary: \"70B scale-dependent findings 仅基于单一模型族 (Llama-3.1-70B AWQ INT4)，混淆 scale/family/quantization\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W3。Contribution 3 标 'validation' overclaim。\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R1-W3 [Major]+R2 AGREE。Scale-dependent interaction (24%→84%) 混淆模型规模、模型族、量化方式三个变量。Vocabulary calibration hypothesis 仅有间接推断（fallback frequency gap）。8B 量化消融 (Appendix R) 部分控制了量化效应但缺少 70B FP16 对比。\"\n  action_items:\n    - round: 26\n      action: \"Contribution 3 改为 'preliminary single-family scale probe'，不用 'validation'；§7 中 vocabulary calibration hypothesis 标注为 speculative 并列出所需验证实验\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W4\"\n  summary: \"Proposition 1 形式化构造 (position-based) 与实际系统 (name-based) 之间存在 gap\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R1-W4 [Major]+R2 AGREE on gap, REBUT on implication。证明使用 position-indexed entity references，pumping lemma Case 1 (position shift) 在 name-based scheme 下不直接成立。R2 论证结论仍然成立（cross-serial dependency 论证），但当前证明的直接适用性有 gap。共识：需补充讨论，但 non-CF 结论不失效。\"\n  action_items:\n    - round: 26\n      action: \"Appendix O 补充讨论 position-based proof 对 name-based scheme 的适用性，或提供 name-based variant 证明\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W5\"\n  summary: \"绝对 F1 低 (R-F1 40-46%) 且缺失监督 baseline 的上下文参照\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R2-W1 [Critical]+R1 REBUT (定位不同)。R2 认为缺失监督 baseline (PL-Marker 60%+ R-F1) 使读者无法评估方法实用价值。R1 反驳：OntoCoDec 定位为约束框架而非 IE 系统，与 span-based 方法不可比；但同意应提供 F1 上下文参照。分歧记录：R2 视为 Critical 方法论问题，R1 视为 presentation 问题。Director 裁定：降级为 warning——论文定位为约束框架的论证成立，但读者确实需要绝对 F1 的领域参照。\"\n  action_items:\n    - round: 26\n      action: \"§5 Setup 添加 1-2 句说明 LLM-based generative RE 的典型 F1 范围和监督方法的 SOTA 水平作为上下文参照\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W6\"\n  summary: \"GoLLIE 作为最直接可比工作，实验对比被推迟到 future work\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-N2 [Critical]。Appendix S 对比不公平。\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R2-W2 [Critical]+R1 REBUT (方法论差异大、complementary work)。R2：GoLLIE 是最直接竞争者，回避对比削弱 novelty narrative。R1：论文已多处讨论 GoLLIE（§6, §7, Appendix B/S），直接对比需控制大量变量，列为 future work 合理。分歧记录：R2 视为 Critical，R1 降级至 Major。Director 裁定：降级为 warning——GoLLIE 对比的方法论复杂性合理，但至少应引用 GoLLIE 已发表数字进行 approximate comparison。\"\n  action_items:\n    - round: 26\n      action: \"§6 或 Appendix S 引用 GoLLIE 在 SciERC/DocRED 上的已发表 F1 数字 + 明确列出方法论不可比因素；删除或限定 Appendix S 中不公平的直接对比表\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W7\"\n  summary: \"Contribution 1 声称 '3 model families under both settings' 但 Mistral 仅有 zero-shot\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R2-W4 [Major]+R1 AGREE。Contribution 1 '3 model families... under both zero-shot and LoRA fine-tuned settings' 但 Mistral-7B 仅有 zero-shot (Table 2 只有 Qwen + Llama fine-tuning)。有误导性。\"\n  action_items:\n    - round: 26\n      action: \"修改 Contribution 1 为 '3 model families in zero-shot, 2 in fine-tuned settings' 或补充 Mistral fine-tuning\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W8\"\n  summary: \"Proposition 1 新颖性争议——形式化已知直觉 vs. 语境价值\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R2-W6 [Major]+R1 REBUT。R2：cross-field binding 超越 CFG 在 PL 理论中是公知常识，overclaim。R1：PL 已知性不否定 NLP 约束解码语境中的应用价值，论文未将 Prop 1 列为 key contribution。分歧记录在报告中。共识：应 acknowledge PL 理论中的已知性。\"\n  action_items:\n    - round: 26\n      action: \"§3 添加一句 acknowledge PL 理论中 cross-reference binding 超越 CFG 的已知性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M1\"\n  summary: \"Abstract F1 范围 '40-46%' 可能与部分数据不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-M1。应修正范围。\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R2-W3 [Major]+R1 AGREE (降级 Minor)。需核实实际范围并修正。\"\n  action_items:\n    - round: 26\n      action: \"核实 Table 2 全部 R-F1 数据，修正 Abstract 中的范围\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M2\"\n  summary: \"CF increase 缺少与 DR reduction 同等的统计检验\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R1-W5 [Minor]+R2 AGREE。DR reduction 有 bootstrap + Bonferroni，CF increase 仅报告绝对值无 CI/p-value。\"\n  action_items:\n    - round: 26\n      action: \"为 CF increase 补充 bootstrap CI 和显著性检验\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M3\"\n  summary: \"LoRA 超参从 SciERC 转移到 DocRED 的 caveat 仅在 Limitations 提及\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R1-W8 [Minor]+R2 AGREE。§5 实验叙述中未提醒读者此 caveat。\"\n  action_items:\n    - round: 26\n      action: \"§5 Setup 中提及 LoRA 超参跨数据集迁移的 caveat\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M4\"\n  summary: \"正文视觉密度不足——8 页仅 3 个 display items\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [visual_check]\n      note: \"Visual check warning。正文 8 页仅 Figure 1 + Table 1 + Table 2。Related Work + Discussion 连续纯文本。前两页无 display item。\"\n  action_items:\n    - round: 26\n      action: \"考虑从 Appendix 提升 1-2 个关键表/图到正文（如 CF-DR trade-off 表或 beam sweep 表）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Carried from prior rounds — status updated for R26\n# ============================================================\n\n- id: \"R16-W5\"\n  summary: \"Proposition 1 定位过高 + 理论-实践 gap 桥接不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 25\n  resolution: \"R26 fresh review 未作为独立 issue 复发。R26-W8 从不同角度（novelty 而非定位）重新提出。原定位问题已修复。\"\n  resolution_round: 25\n\n- id: \"R16-W1\"\n  summary: \"κ-DR 相关性 n=3 呈现不当\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      note: \"R26 未作为独立 issue 提出。R2-S5 肯定了 κ 的诊断价值。可能已修复或降为 non-issue。待 Research Director 确认。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W4\"\n  summary: \"WikiEvents n=20 不足以支撑 task generalization contribution claim\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      note: \"合并到 R26-W2。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-N2\"\n  summary: \"GoLLIE 比较方法论不公平\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      note: \"合并到 R26-W6。R26 R1 rebut 有效——方法论复杂性被认可，但仍需 approximate comparison。严重程度从 critical 降为 warning。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W1\"\n  summary: \"DR↔CF trade-off 在零样本场景下严重程度讨论不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      note: \"合并到 R26-W1。R26 升级为 critical——两位 Reviewer 完全共识。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W5\"\n  summary: \"70B 验证单一模型族 + Contribution 声称 overclaim\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      note: \"合并到 R26-W3。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W2\"\n  summary: \"Scale-dependent layer interaction 缺乏因果解释\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      note: \"合并到 R26-W3。Vocabulary calibration hypothesis 仍仅有间接证据。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W3\"\n  summary: \"S1 vs S2 对比缺乏深入分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      note: \"R26 未作为独立 issue 提出。可能已降为 non-issue 或被其他讨论覆盖。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M4\"\n  summary: \"Figure 1 缺少端到端 running example\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"空间限制(8页正文)无法容纳 token-level 可视化。\"\n  resolution_round: 25\n\n- id: \"R25-M5\"\n  summary: \"Schema coverage gap 对 schema evolution 场景的影响未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      note: \"R26 未单独提出。Limitations 已有相关讨论。可能已修复。\"\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Resolved in prior rounds (confirmed)\n# ============================================================\n\n- id: \"R23-W1\"\n  summary: \"CF 违规占残余违规 64%，与标题 gap\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R26 未复发。\"\n  resolution_round: 24\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出至第 9 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  resolution: \"R26 格式检查确认主文 §1-§7 在 page 1-8。\"\n  resolution_round: 22\n\n- id: \"R16-MF3\"\n  summary: \"CF trade-off 在 Abstract 中 framing 偏乐观\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  resolution: \"Abstract 已分层报告 CF。R26-W1 从不同角度（叙事不对称）重新提出。\"\n  resolution_round: 22\n\n- id: \"R16-W4\"\n  summary: \"70B AWQ INT4 quantization 对约束效果的影响未隔离\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 21\n  resolution: \"Appendix R 验证。R26 R1-S5 肯定。\"\n  resolution_round: 22"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: R26 fresh review, 2026-05-23\n\n# ============================================================\n# Round 26 — Active Issues\n# ============================================================\n\n- id: \"R26-W1\"\n  summary: \"DR→CF trade-off 在 Abstract/正文中 framing 不平衡——zero-shot 净违规仅降约 40%\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W1。Abstract framing 需更对称。\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R1-W1 [Critical]+R2 AGREE (with nuance)。完全共识。Zero-shot S1: DR 15.37%→0.17% 但 CF 0.08%→9.85%，总违规 16.7%→10.1% 仅降 40%。Abstract 突出 DR reduction，CF 被降格为从句且引用 fine-tuned 数字 (≤1.4%) 而非 zero-shot (up to 12%)。R2 补充：DR/CF 严重程度不同（DR 不可恢复 vs CF 可 post-hoc），simple 相加不公平，但叙事不对称确实存在。\"\n  action_items:\n    - round: 26\n      action: \"Abstract + §5 中同时报告 DR reduction 和 CF increase 的 net effect + total violation change；§7 Discussion 扩展 CF 实际影响分析 + deployment recommendations\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W2\"\n  summary: \"WikiEvents n=20 不足以支撑 task generalization claim\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 26\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"降级 contribution list + Preliminary Pilot 标题。\"\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25 多轮复发升级为 critical。\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R1-W2 [Major]+R2-W5 [Major]，完全共识。n=20, MDE=2.0pp, 95% CI ±3.9pp。Abstract 将其与 SciERC (551 docs) 和 DocRED (998 docs) 并列，暗示三个同等重要的评估集。两位 Reviewer 一致要求降级或扩展。\"\n  action_items:\n    - round: 26\n      action: \"从 Abstract 主 claim 中移除或明确标注 WikiEvents 为 preliminary pilot；§5.2 正文仅保留 1 句 feasibility mention，详细结果留 Appendix\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W3\"\n  summary: \"70B scale-dependent findings 仅基于单一模型族 (Llama-3.1-70B AWQ INT4)，混淆 scale/family/quantization\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-W3。Contribution 3 标 'validation' overclaim。\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R1-W3 [Major]+R2 AGREE。Scale-dependent interaction (24%→84%) 混淆模型规模、模型族、量化方式三个变量。Vocabulary calibration hypothesis 仅有间接推断（fallback frequency gap）。8B 量化消融 (Appendix R) 部分控制了量化效应但缺少 70B FP16 对比。\"\n  action_items:\n    - round: 26\n      action: \"Contribution 3 改为 'preliminary single-family scale probe'，不用 'validation'；§7 中 vocabulary calibration hypothesis 标注为 speculative 并列出所需验证实验\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W4\"\n  summary: \"Proposition 1 形式化构造 (position-based) 与实际系统 (name-based) 之间存在 gap\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R1-W4 [Major]+R2 AGREE on gap, REBUT on implication。证明使用 position-indexed entity references，pumping lemma Case 1 (position shift) 在 name-based scheme 下不直接成立。R2 论证结论仍然成立（cross-serial dependency 论证），但当前证明的直接适用性有 gap。共识：需补充讨论，但 non-CF 结论不失效。\"\n  action_items:\n    - round: 26\n      action: \"Appendix O 补充讨论 position-based proof 对 name-based scheme 的适用性，或提供 name-based variant 证明\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W5\"\n  summary: \"绝对 F1 低 (R-F1 40-46%) 且缺失监督 baseline 的上下文参照\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R2-W1 [Critical]+R1 REBUT (定位不同)。R2 认为缺失监督 baseline (PL-Marker 60%+ R-F1) 使读者无法评估方法实用价值。R1 反驳：OntoCoDec 定位为约束框架而非 IE 系统，与 span-based 方法不可比；但同意应提供 F1 上下文参照。分歧记录：R2 视为 Critical 方法论问题，R1 视为 presentation 问题。Director 裁定：降级为 warning——论文定位为约束框架的论证成立，但读者确实需要绝对 F1 的领域参照。\"\n  action_items:\n    - round: 26\n      action: \"§5 Setup 添加 1-2 句说明 LLM-based generative RE 的典型 F1 范围和监督方法的 SOTA 水平作为上下文参照\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W6\"\n  summary: \"GoLLIE 作为最直接可比工作，实验对比被推迟到 future work\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-N2 [Critical]。Appendix S 对比不公平。\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R2-W2 [Critical]+R1 REBUT (方法论差异大、complementary work)。R2：GoLLIE 是最直接竞争者，回避对比削弱 novelty narrative。R1：论文已多处讨论 GoLLIE（§6, §7, Appendix B/S），直接对比需控制大量变量，列为 future work 合理。分歧记录：R2 视为 Critical，R1 降级至 Major。Director 裁定：降级为 warning——GoLLIE 对比的方法论复杂性合理，但至少应引用 GoLLIE 已发表数字进行 approximate comparison。\"\n  action_items:\n    - round: 26\n      action: \"§6 或 Appendix S 引用 GoLLIE 在 SciERC/DocRED 上的已发表 F1 数字 + 明确列出方法论不可比因素；删除或限定 Appendix S 中不公平的直接对比表\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W7\"\n  summary: \"Contribution 1 声称 '3 model families under both settings' 但 Mistral 仅有 zero-shot\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R2-W4 [Major]+R1 AGREE。Contribution 1 '3 model families... under both zero-shot and LoRA fine-tuned settings' 但 Mistral-7B 仅有 zero-shot (Table 2 只有 Qwen + Llama fine-tuning)。有误导性。\"\n  action_items:\n    - round: 26\n      action: \"修改 Contribution 1 为 '3 model families in zero-shot, 2 in fine-tuned settings' 或补充 Mistral fine-tuning\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W8\"\n  summary: \"Proposition 1 新颖性争议——形式化已知直觉 vs. 语境价值\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R2-W6 [Major]+R1 REBUT。R2：cross-field binding 超越 CFG 在 PL 理论中是公知常识，overclaim。R1：PL 已知性不否定 NLP 约束解码语境中的应用价值，论文未将 Prop 1 列为 key contribution。分歧记录在报告中。共识：应 acknowledge PL 理论中的已知性。\"\n  action_items:\n    - round: 26\n      action: \"§3 添加一句 acknowledge PL 理论中 cross-reference binding 超越 CFG 的已知性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M1\"\n  summary: \"Abstract F1 范围 '40-46%' 可能与部分数据不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewers: [1, 2]\n      note: \"R25-M1。应修正范围。\"\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R2-W3 [Major]+R1 AGREE (降级 Minor)。需核实实际范围并修正。\"\n  action_items:\n    - round: 26\n      action: \"核实 Table 2 全部 R-F1 数据，修正 Abstract 中的范围\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M2\"\n  summary: \"CF increase 缺少与 DR reduction 同等的统计检验\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R1-W5 [Minor]+R2 AGREE。DR reduction 有 bootstrap + Bonferroni，CF increase 仅报告绝对值无 CI/p-value。\"\n  action_items:\n    - round: 26\n      action: \"为 CF increase 补充 bootstrap CI 和显著性检验\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M3\"\n  summary: \"LoRA 超参从 SciERC 转移到 DocRED 的 caveat 仅在 Limitations 提及\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [1, 2]\n      note: \"R26 R1-W8 [Minor]+R2 AGREE。§5 实验叙述中未提醒读者此 caveat。\"\n  action_items:\n    - round: 26\n      action: \"§5 Setup 中提及 LoRA 超参跨数据集迁移的 caveat\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M4\"\n  summary: \"正文视觉密度不足——8 页仅 3 个 display items\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewers: [visual_check]\n      note: \"Visual check warning。正文 8 页仅 Figure 1 + Table 1 + Table 2。Related Work + Discussion 连续纯文本。前两页无 display item。\"\n  action_items:\n    - round: 26\n      action: \"考虑从 Appendix 提升 1-2 个关键表/图到正文（如 CF-DR trade-off 表或 beam sweep 表）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Carried from prior rounds — status updated for R26\n# ============================================================\n\n- id: \"R16-W5\"\n  summary: \"Proposition 1 定位过高 + 理论-实践 gap 桥接不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 25\n  resolution: \"R26 fresh review 未作为独立 issue 复发。R26-W8 从不同角度（novelty 而非定位）重新提出。原定位问题已修复。\"\n  resolution_round: 25\n\n- id: \"R16-W1\"\n  summary: \"κ-DR 相关性 n=3 呈现不当\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      note: \"R26 未作为独立 issue 提出。R2-S5 肯定了 κ 的诊断价值。可能已修复或降为 non-issue。待 Research Director 确认。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W4\"\n  summary: \"WikiEvents n=20 不足以支撑 task generalization contribution claim\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      note: \"合并到 R26-W2。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-N2\"\n  summary: \"GoLLIE 比较方法论不公平\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      note: \"合并到 R26-W6。R26 R1 rebut 有效——方法论复杂性被认可，但仍需 approximate comparison。严重程度从 critical 降为 warning。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W1\"\n  summary: \"DR↔CF trade-off 在零样本场景下严重程度讨论不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      note: \"合并到 R26-W1。R26 升级为 critical——两位 Reviewer 完全共识。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W5\"\n  summary: \"70B 验证单一模型族 + Contribution 声称 overclaim\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      note: \"合并到 R26-W3。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W2\"\n  summary: \"Scale-dependent layer interaction 缺乏因果解释\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      note: \"合并到 R26-W3。Vocabulary calibration hypothesis 仍仅有间接证据。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W3\"\n  summary: \"S1 vs S2 对比缺乏深入分析\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      note: \"R26 未作为独立 issue 提出。可能已降为 non-issue 或被其他讨论覆盖。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M4\"\n  summary: \"Figure 1 缺少端到端 running example\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"空间限制(8页正文)无法容纳 token-level 可视化。\"\n  resolution_round: 25\n\n- id: \"R25-M5\"\n  summary: \"Schema coverage gap 对 schema evolution 场景的影响未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      note: \"R26 未单独提出。Limitations 已有相关讨论。可能已修复。\"\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Resolved in prior rounds (confirmed)\n# ============================================================\n\n- id: \"R23-W1\"\n  summary: \"CF 违规占残余违规 64%，与标题 gap\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R26 未复发。\"\n  resolution_round: 24\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出至第 9 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  resolution: \"R26 格式检查确认主文 §1-§7 在 page 1-8。\"\n  resolution_round: 22\n\n- id: \"R16-MF3\"\n  summary: \"CF trade-off 在 Abstract 中 framing 偏乐观\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  resolution: \"Abstract 已分层报告 CF。R26-W1 从不同角度（叙事不对称）重新提出。\"\n  resolution_round: 22\n\n- id: \"R16-W4\"\n  summary: \"70B AWQ INT4 quantization 对约束效果的影响未隔离\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 21\n  resolution: \"Appendix R 验证。R26 R1-S5 肯定。\"\n  resolution_round: 22"
  }
}
```

</details>

---


### Tool result

_source line 2625 · 2026-05-23T12:53:18.711259+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml\", \"bytes\": 12713}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2626 · 2026-05-23T12:56:09.088482+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 26 审稿报告（Fresh Review）\n## OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**Venue**: EMNLP 2026 (ARR May cycle) | **Deadline**: 2026-05-25 | **Reviewers**: 2 | **Rounds**: 1（交叉分享后共识充分，无需第二轮）\n\n---\n\n## Summary\n\n论文提出 OntoCoDec，一个将 IE 本体约束编译为 token-level 解码约束的框架。核心观察是 domain/range 类型约束超越 context-free 表达能力（Proposition 1），因此采用两层架构：grammar 层（基于 XGrammar）保证 JSON 结构和词汇合法性，semantic 层通过运行时 entity registry 和 dynamic logit masking 执行类型约束。在 SciERC（551 docs）、DocRED（998 docs）和 WikiEvents（n=20 pilot）上评估，涵盖 3 个 8B 级模型和 1 个 70B 模型（Llama-3.1-70B AWQ INT4），zero-shot 和 LoRA fine-tuning 两种设置。\n\n---\n\n## Strengths\n\n**S1. 系统性的约束编译框架。** 将 IE 本体约束编译为可组合的解码层的想法在 IE 领域是新颖的。两层架构的设计有理论支撑（Proposition 1），将 context-free 可处理的约束与需要运行时状态的约束清晰分离。框架 model-agnostic，与 fine-tuning 正交可组合。[R1-S1, R2-S6]\n\n**S2. 极其充分的实验和统计方法。** 40 页论文含 48+ 表格、5-way ablation、4-way fine-tuning ablation、beam search 兼容性、prompt sensitivity、文档长度分析等。统计方法规范：Bootstrap CIs（10,000 iterations）、Bonferroni correction（α_adj=0.0125）、Cohen's d effect sizes、统计 power analysis。可复现性文档详尽（Appendix G）。这一评估覆盖面在同类工作中罕见。[R1-S2/S3/S5, R2-S2]\n\n**S3. DR→CF trade-off 的量化分析有真正洞察。** 论文诚实地识别并量化了 per-triple enforcement 引入 cross-field 不一致的代价，提供了 CF source breakdown（hallucinated entities 58.1%, true cascade errors 7.3%）和 beam search 消除路径。[R1-S4, R2-S3]\n\n**S4. Limitations section 诚实全面。** 三段式结构（Constraint scope, Evaluation coverage, Engineering considerations）系统性地列出了方法的边界条件，达到了顶会审稿人期望的坦诚程度。[R1-S4, R2-S4]\n\n**S5. Constraint tightness κ 有诊断价值。** 提供了可量化的 schema 约束强度指标，用于解释不同 schema 下的违规模式差异。[R2-S5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [Critical, 共识] DR→CF trade-off 的 Abstract/正文 framing 严重不平衡。**\nZero-shot greedy S1 下：DR 15.37%→0.17%（↓99%），但 CF 0.08%→9.85%（↑123×）。总违规率从 ~16.7% 降至 ~10.1%，净降幅仅约 40%——远低于 \"DR reduction to near-zero\" 给读者的印象。Abstract 将 DR reduction 置于叙事主位，CF 被降格为从句且引用 fine-tuned 数字（≤1.4%）而非 zero-shot（up to 12%）。论文认为 DR/CF 严重程度不同（DR 不可恢复 vs CF 可 post-hoc 修复），这有合理性，但当前叙事仍然不够平衡。\n- **要求**：Abstract + §5 中并列报告 DR reduction 和 CF increase 的 net effect（total violation change）；§7 扩展 deployment recommendations（明确哪些配置适合哪些场景）\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [Major, 共识] WikiEvents n=20 不足以支撑 task generalization claim。**\nMDE=2.0pp, 95% CI ±3.9pp，统计效力严重不足。Abstract 将其与 SciERC（551 docs）和 DocRED（998 docs）并列，给读者造成三个数据集同等证据的印象。\n- **要求**：从 Abstract 主 claim 中移除 WikiEvents 或明确标注 preliminary；§5.2 正文最多保留 1 句 feasibility mention\n\n**SF2. [Major, 共识] 70B scale-dependent findings 混淆 scale/family/quantization 三个变量。**\nScale-dependent interaction（8B: 24% vs 70B: 84% independent DR reduction）仅基于 Llama-3.1-70B AWQ INT4 vs 三个 8B 模型。Vocabulary calibration hypothesis（§7）仅有间接推断。8B 量化消融（Appendix R）部分控制了量化效应但缺少 70B FP16 对比。\n- **要求**：Contribution 3 改为 'preliminary single-family scale probe'；§7 中 vocabulary calibration hypothesis 标注为 speculative\n\n**SF3. [Major, 共识] Proposition 1 形式化构造（position-based）与实际系统（name-based）之间存在 gap。**\nPumping lemma 证明使用 position-indexed entity references，但实际系统使用 name-based references。Case 1 论证在 name-based scheme 下不直接成立。R2 论证 non-CF 结论通过 cross-serial dependency 论证仍然成立，但当前证明的直接适用性未经论证。\n- **要求**：Appendix O 补充讨论 position-based proof 对 name-based scheme 的适用性\n\n**SF4. [Major→Warning, Director 裁定] 绝对 F1 低 (R-F1 40-46%) 且缺失监督 baseline 上下文参照。**\nR2 认为 Critical（缺少 PL-Marker 60%+ R-F1 对比使读者无法评估实用价值），R1 REBUT（OntoCoDec 定位为约束框架非 IE 系统，与 span-based 方法不可比）。**Director 裁定**：R1 的定位论证成立——约束框架与 IE 系统的对比方法论不合理。但读者确实需要绝对 F1 的领域参照。降级为 Warning。\n- **要求**：§5 Setup 添加 1-2 句说明 LLM-based generative RE 的典型 F1 范围和监督方法 SOTA 水平作为上下文\n\n**SF5. [Major→Warning, Director 裁定] GoLLIE 实验对比被推迟到 future work。**\nR2 认为 Critical（最直接竞争者回避对比削弱 novelty），R1 REBUT（方法论差异大、已多处讨论 GoLLIE、complementary work）。**Director 裁定**：GoLLIE 对比的方法论复杂性合理（不同 training paradigm + schema encoding + model families），但\"future work\"定位感觉回避。降级为 Warning。\n- **要求**：引用 GoLLIE 已发表 F1 数字进行 approximate comparison；删除或限定 Appendix S 中不公平的直接对比表\n\n**SF6. [Major, 共识] Contribution 1 声称 '3 model families under both settings' 但 Mistral 仅有 zero-shot。**\nTable 2 只有 Qwen + Llama 的 fine-tuning 结果，Mistral-7B 仅 zero-shot。\n- **要求**：修改 Contribution 1 措辞或补充 Mistral fine-tuning\n\n### Minor（不影响接收）\n\n**M1. [Info] Abstract F1 范围可能不准确。** \"F1 40-46%\" 需核实是否与 Table 2 全部数据一致。[R2-W3, R1 AGREE]\n\n**M2. [Info] CF increase 缺少统计检验。** DR reduction 有完整 bootstrap + Bonferroni，CF increase 无 CI/p-value。作为主要 trade-off 应同等对待。[R1-W5, R2 AGREE]\n\n**M3. [Info] LoRA 超参跨数据集迁移。** 超参在 SciERC 调优后直接迁移 DocRED，§5 中未提醒读者此 caveat（仅在 Limitations 提及）。[R1-W8, R2 AGREE]\n\n**M4. [Info] 正文视觉密度不足。** 8 页正文仅 3 个 display items（Figure 1 + Table 1 + Table 2），Related Work + Discussion 连续纯文本。建议从 Appendix 提升 1-2 个关键表/图。[Visual Check]\n\n**M5. [Info] 缩写密度过高。** DR, CF, RV, ET, S1, S2 等在 §5 密集出现，首次阅读体验差。[R2-W8]\n\n**M6. [Info] Proposition 1 新颖性争议。** R2 认为 cross-field binding 超越 CFG 在 PL 理论中是公知常识；R1 认为 NLP 语境中的应用形式化有价值。建议 §3 acknowledge PL 理论中的已知性。[分歧记录]\n\n---\n\n## Reviewer Consensus\n\n以下为两位 Reviewer 达成共识的关键问题：\n\n1. **[AGREE] DR→CF trade-off framing 不平衡**——Abstract 叙事不对称，zero-shot 下净收益远低于 DR 单项数字暗示\n2. **[AGREE] WikiEvents n=20 不足以支撑 generalization claim**——应降级或扩展\n3. **[AGREE] 70B 仅单一模型族**——混淆 scale/family/quantization，应限定 claim\n4. **[AGREE] Proposition 1 证明有 gap**——结论不失效但需补充讨论\n5. **[AGREE] Contribution 1 Mistral 覆盖 overclaim**——措辞应修正\n6. **[AGREE] CF 缺少统计检验**——与 DR reduction 不对等\n\n---\n\n## Reviewer Divergence\n\n1. **监督 baseline 对比的必要性**：R2 [Critical] 认为缺少监督 baseline 使方法价值不清；R1 [REBUT] 认为约束框架与 IE 系统的对比方法论不合理。Director 采纳 R1 定位论证，降级为 Warning。\n2. **GoLLIE 对比的严重程度**：R2 [Critical] 认为回避最直接竞争者；R1 [REBUT] 认为方法论差异大。Director 降级为 Warning，要求 approximate comparison。\n3. **Proposition 1 新颖性**：R2 认为有限（PL 公知）；R1 认为语境新颖。如实记录。\n4. **Overall Score**：R1 给 3.5 (Borderline Conference)；R2 给 3.0 (Findings)。分歧源于 novelty 评估和监督 baseline/GoLLIE 对比的重要性判断。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Zero-shot greedy S1 下总违规率从 ~16.7% 降至 ~10.1%（净降 ~40%）。在什么部署场景下，将 DR 转换为 CF 是净正向改善？论文应提供明确的 deployment recommendations。\n\n**Q2.** Proposition 1 的 pumping lemma 证明使用 position-based entity references。如果实际系统使用 name-based references，pumping lemma Case 1 论证是否仍成立？请解释或补充 name-based variant。\n\n**Q3.** Scale-dependent interaction 的 vocabulary calibration hypothesis——有没有直接证据（如 token-level probability distribution 对比），还是仅从 fallback frequency gap 间接推断？\n\n**Q4.** Qwen-8B 触发 0 次 grammar-first fallback vs Llama-8B 触发 5,882 次（100× 差异，Table 10）。这是否暗示 fallback 行为高度依赖 model-specific tokenizer alignment？如果是，框架的 model-agnostic claim 是否需要限定？\n\n**Q5.** Beam search k=4 消除所有 CF violations（Table 24），但 R-F1 从 greedy S1 的 43.77 降至 43.60（SciERC）。这一 tradeoff 在 DocRED 上如何表现？precision/recall 的具体变化？\n\n**Q6.** Fine-tuned 设置下 CF≤1.4% 的违规是否集中在特定高频 relation type？κ 与 per-relation F1 的关系能否为\"何时使用约束解码\"提供实践指导？\n\n---\n\n## Missing References\n\n- **监督 IE baseline 数字**：PL-Marker, DyGIE++ 等在 SciERC/DocRED 上的已发表 F1 数字应作为上下文参照引用（presentation 需要，非实验对比）[R1 AGREE, R2-W1]\n- **Guidance (Microsoft, 2023)**：主要 constrained decoding 库之一，应在 §6 提及 [R1, R2 AGREE]\n- **DeepStruct (Wang et al., 2022)**：structured prediction as seq2seq，与 OntoCoDec 范式相关 [R1, R2 弱 AGREE]\n- **CRANE (Banerjee et al., 2025)**：已引用但 §6 讨论不够充分（仅 §7 提及），考虑到方法相关性应在 Related Work 更多篇幅 [R2, R1 REBUT——当前讨论篇幅可接受]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。**\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (2026-05-23 12:34-12:38 UTC)\n\n| 严重程度 | 数量 |\n|----------|------|\n| Critical | 1 |\n| Warning | 4 |\n| Info | 13 |\n\n**关键发现：**\n- **[Critical]** 最后一页（p40）仅约 1/5 内容，4/5 为空白，影响专业感\n- **[Warning]** 前两页纯文本无 display item，审稿人缺乏视觉锚点\n- **[Warning]** 正文 8 页仅 3 个 display items（Figure 1 + Table 1 + Table 2），对实证为主的论文偏少\n- **[Warning]** Related Work + Discussion（p7-8）连续纯文本无穿插\n- **[Warning]** Appendix B（Extended Related Work, p14-17）连续 4 页纯文本\n- **[Info]** 所有表格统一 booktabs 风格，格式专业；公式渲染正确；Limitations 排版符合 EMNLP 要求；无 margin 溢出；无 undefined reference\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**Soundness: 3.5/5** — 方法论合理，统计严谨（bootstrap + Bonferroni + effect sizes）。但 Proposition 1 有 position-based/name-based 形式化 gap，CF trade-off framing 不够平衡，scale-dependent claims 证据基础过窄。\n\n**Excitement: 3/5** — 将 IE 本体约束编译为解码掩码的想法新颖实用，但核心架构（XGrammar + stateful type checker）是已有技术的自然组合而非概念性突破。Per-triple 架构限制（无法处理 cross-field consistency without beam search）降低了实际影响力。\n\n**Reproducibility: 5/5** — 28 页附录含完整超参数、硬件配置、随机种子、prompt 模板。统计 power analysis 和 200-doc subset 的充分性论证质量极高。\n\n**Confidence: 4/5**\n\n### 评分理由\n\n论文的核心价值在于**执行质量和评估全面性**而非概念新颖性。两层约束编译框架设计合理、实验覆盖面远超平均水平、统计方法规范、局限性讨论诚实——这些是 Findings 级工作的标志。\n\n降分的主要原因：\n1. **DR→CF trade-off 的叙事不平衡**是最严重的问题——zero-shot 下净总违规仅降约 40%，与 headline claim \"DR reduction to near-zero\" 的印象差距过大\n2. **核心新颖性有限**——entity registry + dynamic masking 概念上非 surprising，Proposition 1 是对 PL 理论已知结论的 IE 应用\n3. **实验覆盖有明确缺口**——WikiEvents n=20、70B 单一模型族、Mistral 仅 zero-shot、GoLLIE 无实验对比\n\nR1 给出 3.5 (Borderline Conference) 主要基于框架的新颖性和实验充分性；R2 给出 3.0 (Findings) 主要基于有限的概念新颖性和缺失的关键对比。Director 综合裁定 3.0——论文的主要贡献是工程实践和实证分析，Findings track 是其恰当定位。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 约 186-190 words，在 200 word 限制内\n- F1 范围 \"40-46%\" 需核实一致性\n- CF 的叙事权重应与 DR 更对称\n- \"with scale- and schema-dependent layer interaction\" 语法不完整\n\n### §1 Introduction\n- 叙事结构清晰（problem → limitation → solution → contributions）\n- Contribution 1 对 Mistral fine-tuning 覆盖的声称需修正\n- \"eliminates all violation types at 8B at 1.39× latency\" 需限定为 beam k=4 + LoRA\n\n### §2 Background\n- 问题形式化清楚，ontology 定义精确\n- 正确识别了 grammar-constrained decoding 的局限性\n\n### §3 Method\n- 两层架构描述清晰，decidability taxonomy 有组织价值\n- Proposition 1 的 position-based/name-based gap 需补充讨论\n- Entity registry 的 first-seen semantics 有合理动机，但替代策略（majority voting, deferred assignment）缺乏讨论\n- DFA state explosion 的工程论证（6^17 states）比 Proposition 1 本身更有实用价值\n\n### §4 Constraint Composition\n- M_final = M_grammar ∧ M_semantic 的组合公式简洁\n- Grammar-First Fallback 是合理的工程决策\n- κ 概念有诊断价值但 n=3 的统计分析应保持描述性定位\n\n### §5 Experiments\n- 五路消融设计合理，fine-tuning composability 是亮点\n- DocRED 使用 dev set 的 caveat 应更早、更显著地提及\n- CF increase 应得到与 DR reduction 同等的统计处理\n- WikiEvents §5.2 仅 1 句交叉引用 Appendix，处理得当\n\n### §6 Related Work\n- 三轴组织（constrained decoding / schema-aware IE / constraint enforcement）清晰有效\n- GoLLIE 定位（training-time vs runtime enforcement）准确但缺实验支撑\n- 篇幅适中但 Appendix B 过长（4 页纯文本）\n\n### §7 Discussion and Conclusion\n- Scale-dependent interaction 讨论有价值但 causal explanation 过于 speculative\n- DR↔CF trade-off 讨论诚实但篇幅不足，缺 deployment recommendations\n- Per-triple vs global enforcement 的讨论恰当指出了未来方向\n\n### Limitations\n- 三段式结构全面诚实\n- 覆盖了 CF 的本质限制、评估范围、工程约束\n- Schema evolution caveat 已存在但可更显著\n\n### Ethics Statement\n- 简洁适当\n\n### 格式合规\n| 检查项 | 结果 |\n|--------|------|\n| ACL 模板 | ✓ `\\usepackage[review]{acl}` |\n| Double-blind | ✓ \"Anonymous ACL submission\" |\n| 正文 ≤ 8 页 | ✓ |\n| Limitations 位置 | ✓ |\n| Abstract ≤ 200 words | ✓ (~190) |\n| Ethics Statement | ✓ |\n| References 格式 | ✓ |\n\n---\n\n## Action Items 优先级排序\n\n| 优先级 | ID | Action | 严重程度 |\n|--------|----|--------|----------|\n| 1 | MF1 | Abstract + §5 并列报告 DR/CF net effect + §7 deployment recommendations | Critical |\n| 2 | SF1 | WikiEvents 从 Abstract 降级 + §5.2 最多 1 句 | Major |\n| 3 | SF3 | Appendix O 补充 name-based scheme 讨论 | Major |\n| 4 | SF6 | Contribution 1 修正 Mistral 覆盖声称 | Major |\n| 5 | SF2 | Contribution 3 改 'preliminary probe' + vocabulary calibration 标 speculative | Major |\n| 6 | SF4 | §5 Setup 添加 LLM-based RE F1 上下文参照 | Warning |\n| 7 | SF5 | GoLLIE approximate comparison + 限定 Appendix S | Warning |\n| 8 | M1-M6 | Abstract F1 范围、CF 统计检验、LoRA caveat、视觉密度、缩写、PL acknowledge | Info |",
  "project": "schema_semantic_constrained_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 26 审稿报告（Fresh Review）\n## OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**Venue**: EMNLP 2026 (ARR May cycle) | **Deadline**: 2026-05-25 | **Reviewers**: 2 | **Rounds**: 1（交叉分享后共识充分，无需第二轮）\n\n---\n\n## Summary\n\n论文提出 OntoCoDec，一个将 IE 本体约束编译为 token-level 解码约束的框架。核心观察是 domain/range 类型约束超越 context-free 表达能力（Proposition 1），因此采用两层架构：grammar 层（基于 XGrammar）保证 JSON 结构和词汇合法性，semantic 层通过运行时 entity registry 和 dynamic logit masking 执行类型约束。在 SciERC（551 docs）、DocRED（998 docs）和 WikiEvents（n=20 pilot）上评估，涵盖 3 个 8B 级模型和 1 个 70B 模型（Llama-3.1-70B AWQ INT4），zero-shot 和 LoRA fine-tuning 两种设置。\n\n---\n\n## Strengths\n\n**S1. 系统性的约束编译框架。** 将 IE 本体约束编译为可组合的解码层的想法在 IE 领域是新颖的。两层架构的设计有理论支撑（Proposition 1），将 context-free 可处理的约束与需要运行时状态的约束清晰分离。框架 model-agnostic，与 fine-tuning 正交可组合。[R1-S1, R2-S6]\n\n**S2. 极其充分的实验和统计方法。** 40 页论文含 48+ 表格、5-way ablation、4-way fine-tuning ablation、beam search 兼容性、prompt sensitivity、文档长度分析等。统计方法规范：Bootstrap CIs（10,000 iterations）、Bonferroni correction（α_adj=0.0125）、Cohen's d effect sizes、统计 power analysis。可复现性文档详尽（Appendix G）。这一评估覆盖面在同类工作中罕见。[R1-S2/S3/S5, R2-S2]\n\n**S3. DR→CF trade-off 的量化分析有真正洞察。** 论文诚实地识别并量化了 per-triple enforcement 引入 cross-field 不一致的代价，提供了 CF source breakdown（hallucinated entities 58.1%, true cascade errors 7.3%）和 beam search 消除路径。[R1-S4, R2-S3]\n\n**S4. Limitations section 诚实全面。** 三段式结构（Constraint scope, Evaluation coverage, Engineering considerations）系统性地列出了方法的边界条件，达到了顶会审稿人期望的坦诚程度。[R1-S4, R2-S4]\n\n**S5. Constraint tightness κ 有诊断价值。** 提供了可量化的 schema 约束强度指标，用于解释不同 schema 下的违规模式差异。[R2-S5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [Critical, 共识] DR→CF trade-off 的 Abstract/正文 framing 严重不平衡。**\nZero-shot greedy S1 下：DR 15.37%→0.17%（↓99%），但 CF 0.08%→9.85%（↑123×）。总违规率从 ~16.7% 降至 ~10.1%，净降幅仅约 40%——远低于 \"DR reduction to near-zero\" 给读者的印象。Abstract 将 DR reduction 置于叙事主位，CF 被降格为从句且引用 fine-tuned 数字（≤1.4%）而非 zero-shot（up to 12%）。论文认为 DR/CF 严重程度不同（DR 不可恢复 vs CF 可 post-hoc 修复），这有合理性，但当前叙事仍然不够平衡。\n- **要求**：Abstract + §5 中并列报告 DR reduction 和 CF increase 的 net effect（total violation change）；§7 扩展 deployment recommendations（明确哪些配置适合哪些场景）\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [Major, 共识] WikiEvents n=20 不足以支撑 task generalization claim。**\nMDE=2.0pp, 95% CI ±3.9pp，统计效力严重不足。Abstract 将其与 SciERC（551 docs）和 DocRED（998 docs）并列，给读者造成三个数据集同等证据的印象。\n- **要求**：从 Abstract 主 claim 中移除 WikiEvents 或明确标注 preliminary；§5.2 正文最多保留 1 句 feasibility mention\n\n**SF2. [Major, 共识] 70B scale-dependent findings 混淆 scale/family/quantization 三个变量。**\nScale-dependent interaction（8B: 24% vs 70B: 84% independent DR reduction）仅基于 Llama-3.1-70B AWQ INT4 vs 三个 8B 模型。Vocabulary calibration hypothesis（§7）仅有间接推断。8B 量化消融（Appendix R）部分控制了量化效应但缺少 70B FP16 对比。\n- **要求**：Contribution 3 改为 'preliminary single-family scale probe'；§7 中 vocabulary calibration hypothesis 标注为 speculative\n\n**SF3. [Major, 共识] Proposition 1 形式化构造（position-based）与实际系统（name-based）之间存在 gap。**\nPumping lemma 证明使用 position-indexed entity references，但实际系统使用 name-based references。Case 1 论证在 name-based scheme 下不直接成立。R2 论证 non-CF 结论通过 cross-serial dependency 论证仍然成立，但当前证明的直接适用性未经论证。\n- **要求**：Appendix O 补充讨论 position-based proof 对 name-based scheme 的适用性\n\n**SF4. [Major→Warning, Director 裁定] 绝对 F1 低 (R-F1 40-46%) 且缺失监督 baseline 上下文参照。**\nR2 认为 Critical（缺少 PL-Marker 60%+ R-F1 对比使读者无法评估实用价值），R1 REBUT（OntoCoDec 定位为约束框架非 IE 系统，与 span-based 方法不可比）。**Director 裁定**：R1 的定位论证成立——约束框架与 IE 系统的对比方法论不合理。但读者确实需要绝对 F1 的领域参照。降级为 Warning。\n- **要求**：§5 Setup 添加 1-2 句说明 LLM-based generative RE 的典型 F1 范围和监督方法 SOTA 水平作为上下文\n\n**SF5. [Major→Warning, Director 裁定] GoLLIE 实验对比被推迟到 future work。**\nR2 认为 Critical（最直接竞争者回避对比削弱 novelty），R1 REBUT（方法论差异大、已多处讨论 GoLLIE、complementary work）。**Director 裁定**：GoLLIE 对比的方法论复杂性合理（不同 training paradigm + schema encoding + model families），但\"future work\"定位感觉回避。降级为 Warning。\n- **要求**：引用 GoLLIE 已发表 F1 数字进行 approximate comparison；删除或限定 Appendix S 中不公平的直接对比表\n\n**SF6. [Major, 共识] Contribution 1 声称 '3 model families under both settings' 但 Mistral 仅有 zero-shot。**\nTable 2 只有 Qwen + Llama 的 fine-tuning 结果，Mistral-7B 仅 zero-shot。\n- **要求**：修改 Contribution 1 措辞或补充 Mistral fine-tuning\n\n### Minor（不影响接收）\n\n**M1. [Info] Abstract F1 范围可能不准确。** \"F1 40-46%\" 需核实是否与 Table 2 全部数据一致。[R2-W3, R1 AGREE]\n\n**M2. [Info] CF increase 缺少统计检验。** DR reduction 有完整 bootstrap + Bonferroni，CF increase 无 CI/p-value。作为主要 trade-off 应同等对待。[R1-W5, R2 AGREE]\n\n**M3. [Info] LoRA 超参跨数据集迁移。** 超参在 SciERC 调优后直接迁移 DocRED，§5 中未提醒读者此 caveat（仅在 Limitations 提及）。[R1-W8, R2 AGREE]\n\n**M4. [Info] 正文视觉密度不足。** 8 页正文仅 3 个 display items（Figure 1 + Table 1 + Table 2），Related Work + Discussion 连续纯文本。建议从 Appendix 提升 1-2 个关键表/图。[Visual Check]\n\n**M5. [Info] 缩写密度过高。** DR, CF, RV, ET, S1, S2 等在 §5 密集出现，首次阅读体验差。[R2-W8]\n\n**M6. [Info] Proposition 1 新颖性争议。** R2 认为 cross-field binding 超越 CFG 在 PL 理论中是公知常识；R1 认为 NLP 语境中的应用形式化有价值。建议 §3 acknowledge PL 理论中的已知性。[分歧记录]\n\n---\n\n## Reviewer Consensus\n\n以下为两位 Reviewer 达成共识的关键问题：\n\n1. **[AGREE] DR→CF trade-off framing 不平衡**——Abstract 叙事不对称，zero-shot 下净收益远低于 DR 单项数字暗示\n2. **[AGREE] WikiEvents n=20 不足以支撑 generalization claim**——应降级或扩展\n3. **[AGREE] 70B 仅单一模型族**——混淆 scale/family/quantization，应限定 claim\n4. **[AGREE] Proposition 1 证明有 gap**——结论不失效但需补充讨论\n5. **[AGREE] Contribution 1 Mistral 覆盖 overclaim**——措辞应修正\n6. **[AGREE] CF 缺少统计检验**——与 DR reduction 不对等\n\n---\n\n## Reviewer Divergence\n\n1. **监督 baseline 对比的必要性**：R2 [Critical] 认为缺少监督 baseline 使方法价值不清；R1 [REBUT] 认为约束框架与 IE 系统的对比方法论不合理。Director 采纳 R1 定位论证，降级为 Warning。\n2. **GoLLIE 对比的严重程度**：R2 [Critical] 认为回避最直接竞争者；R1 [REBUT] 认为方法论差异大。Director 降级为 Warning，要求 approximate comparison。\n3. **Proposition 1 新颖性**：R2 认为有限（PL 公知）；R1 认为语境新颖。如实记录。\n4. **Overall Score**：R1 给 3.5 (Borderline Conference)；R2 给 3.0 (Findings)。分歧源于 novelty 评估和监督 baseline/GoLLIE 对比的重要性判断。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Zero-shot greedy S1 下总违规率从 ~16.7% 降至 ~10.1%（净降 ~40%）。在什么部署场景下，将 DR 转换为 CF 是净正向改善？论文应提供明确的 deployment recommendations。\n\n**Q2.** Proposition 1 的 pumping lemma 证明使用 position-based entity references。如果实际系统使用 name-based references，pumping lemma Case 1 论证是否仍成立？请解释或补充 name-based variant。\n\n**Q3.** Scale-dependent interaction 的 vocabulary calibration hypothesis——有没有直接证据（如 token-level probability distribution 对比），还是仅从 fallback frequency gap 间接推断？\n\n**Q4.** Qwen-8B 触发 0 次 grammar-first fallback vs Llama-8B 触发 5,882 次（100× 差异，Table 10）。这是否暗示 fallback 行为高度依赖 model-specific tokenizer alignment？如果是，框架的 model-agnostic claim 是否需要限定？\n\n**Q5.** Beam search k=4 消除所有 CF violations（Table 24），但 R-F1 从 greedy S1 的 43.77 降至 43.60（SciERC）。这一 tradeoff 在 DocRED 上如何表现？precision/recall 的具体变化？\n\n**Q6.** Fine-tuned 设置下 CF≤1.4% 的违规是否集中在特定高频 relation type？κ 与 per-relation F1 的关系能否为\"何时使用约束解码\"提供实践指导？\n\n---\n\n## Missing References\n\n- **监督 IE baseline 数字**：PL-Marker, DyGIE++ 等在 SciERC/DocRED 上的已发表 F1 数字应作为上下文参照引用（presentation 需要，非实验对比）[R1 AGREE, R2-W1]\n- **Guidance (Microsoft, 2023)**：主要 constrained decoding 库之一，应在 §6 提及 [R1, R2 AGREE]\n- **DeepStruct (Wang et al., 2022)**：structured prediction as seq2seq，与 OntoCoDec 范式相关 [R1, R2 弱 AGREE]\n- **CRANE (Banerjee et al., 2025)**：已引用但 §6 讨论不够充分（仅 §7 提及），考虑到方法相关性应在 Related Work 更多篇幅 [R2, R1 REBUT——当前讨论篇幅可接受]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。**\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (2026-05-23 12:34-12:38 UTC)\n\n| 严重程度 | 数量 |\n|----------|------|\n| Critical | 1 |\n| Warning | 4 |\n| Info | 13 |\n\n**关键发现：**\n- **[Critical]** 最后一页（p40）仅约 1/5 内容，4/5 为空白，影响专业感\n- **[Warning]** 前两页纯文本无 display item，审稿人缺乏视觉锚点\n- **[Warning]** 正文 8 页仅 3 个 display items（Figure 1 + Table 1 + Table 2），对实证为主的论文偏少\n- **[Warning]** Related Work + Discussion（p7-8）连续纯文本无穿插\n- **[Warning]** Appendix B（Extended Related Work, p14-17）连续 4 页纯文本\n- **[Info]** 所有表格统一 booktabs 风格，格式专业；公式渲染正确；Limitations 排版符合 EMNLP 要求；无 margin 溢出；无 undefined reference\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**Soundness: 3.5/5** — 方法论合理，统计严谨（bootstrap + Bonferroni + effect sizes）。但 Proposition 1 有 position-based/name-based 形式化 gap，CF trade-off framing 不够平衡，scale-dependent claims 证据基础过窄。\n\n**Excitement: 3/5** — 将 IE 本体约束编译为解码掩码的想法新颖实用，但核心架构（XGrammar + stateful type checker）是已有技术的自然组合而非概念性突破。Per-triple 架构限制（无法处理 cross-field consistency without beam search）降低了实际影响力。\n\n**Reproducibility: 5/5** — 28 页附录含完整超参数、硬件配置、随机种子、prompt 模板。统计 power analysis 和 200-doc subset 的充分性论证质量极高。\n\n**Confidence: 4/5**\n\n### 评分理由\n\n论文的核心价值在于**执行质量和评估全面性**而非概念新颖性。两层约束编译框架设计合理、实验覆盖面远超平均水平、统计方法规范、局限性讨论诚实——这些是 Findings 级工作的标志。\n\n降分的主要原因：\n1. **DR→CF trade-off 的叙事不平衡**是最严重的问题——zero-shot 下净总违规仅降约 40%，与 headline claim \"DR reduction to near-zero\" 的印象差距过大\n2. **核心新颖性有限**——entity registry + dynamic masking 概念上非 surprising，Proposition 1 是对 PL 理论已知结论的 IE 应用\n3. **实验覆盖有明确缺口**——WikiEvents n=20、70B 单一模型族、Mistral 仅 zero-shot、GoLLIE 无实验对比\n\nR1 给出 3.5 (Borderline Conference) 主要基于框架的新颖性和实验充分性；R2 给出 3.0 (Findings) 主要基于有限的概念新颖性和缺失的关键对比。Director 综合裁定 3.0——论文的主要贡献是工程实践和实证分析，Findings track 是其恰当定位。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 约 186-190 words，在 200 word 限制内\n- F1 范围 \"40-46%\" 需核实一致性\n- CF 的叙事权重应与 DR 更对称\n- \"with scale- and schema-dependent layer interaction\" 语法不完整\n\n### §1 Introduction\n- 叙事结构清晰（problem → limitation → solution → contributions）\n- Contribution 1 对 Mistral fine-tuning 覆盖的声称需修正\n- \"eliminates all violation types at 8B at 1.39× latency\" 需限定为 beam k=4 + LoRA\n\n### §2 Background\n- 问题形式化清楚，ontology 定义精确\n- 正确识别了 grammar-constrained decoding 的局限性\n\n### §3 Method\n- 两层架构描述清晰，decidability taxonomy 有组织价值\n- Proposition 1 的 position-based/name-based gap 需补充讨论\n- Entity registry 的 first-seen semantics 有合理动机，但替代策略（majority voting, deferred assignment）缺乏讨论\n- DFA state explosion 的工程论证（6^17 states）比 Proposition 1 本身更有实用价值\n\n### §4 Constraint Composition\n- M_final = M_grammar ∧ M_semantic 的组合公式简洁\n- Grammar-First Fallback 是合理的工程决策\n- κ 概念有诊断价值但 n=3 的统计分析应保持描述性定位\n\n### §5 Experiments\n- 五路消融设计合理，fine-tuning composability 是亮点\n- DocRED 使用 dev set 的 caveat 应更早、更显著地提及\n- CF increase 应得到与 DR reduction 同等的统计处理\n- WikiEvents §5.2 仅 1 句交叉引用 Appendix，处理得当\n\n### §6 Related Work\n- 三轴组织（constrained decoding / schema-aware IE / constraint enforcement）清晰有效\n- GoLLIE 定位（training-time vs runtime enforcement）准确但缺实验支撑\n- 篇幅适中但 Appendix B 过长（4 页纯文本）\n\n### §7 Discussion and Conclusion\n- Scale-dependent interaction 讨论有价值但 causal explanation 过于 speculative\n- DR↔CF trade-off 讨论诚实但篇幅不足，缺 deployment recommendations\n- Per-triple vs global enforcement 的讨论恰当指出了未来方向\n\n### Limitations\n- 三段式结构全面诚实\n- 覆盖了 CF 的本质限制、评估范围、工程约束\n- Schema evolution caveat 已存在但可更显著\n\n### Ethics Statement\n- 简洁适当\n\n### 格式合规\n| 检查项 | 结果 |\n|--------|------|\n| ACL 模板 | ✓ `\\usepackage[review]{acl}` |\n| Double-blind | ✓ \"Anonymous ACL submission\" |\n| 正文 ≤ 8 页 | ✓ |\n| Limitations 位置 | ✓ |\n| Abstract ≤ 200 words | ✓ (~190) |\n| Ethics Statement | ✓ |\n| References 格式 | ✓ |\n\n---\n\n## Action Items 优先级排序\n\n| 优先级 | ID | Action | 严重程度 |\n|--------|----|--------|----------|\n| 1 | MF1 | Abstract + §5 并列报告 DR/CF net effect + §7 deployment recommendations | Critical |\n| 2 | SF1 | WikiEvents 从 Abstract 降级 + §5.2 最多 1 句 | Major |\n| 3 | SF3 | Appendix O 补充 name-based scheme 讨论 | Major |\n| 4 | SF6 | Contribution 1 修正 Mistral 覆盖声称 | Major |\n| 5 | SF2 | Contribution 3 改 'preliminary probe' + vocabulary calibration 标 speculative | Major |\n| 6 | SF4 | §5 Setup 添加 LLM-based RE F1 上下文参照 | Warning |\n| 7 | SF5 | GoLLIE approximate comparison + 限定 Appendix S | Warning |\n| 8 | M1-M6 | Abstract F1 范围、CF 统计检验、LoRA caveat、视觉密度、缩写、PL acknowledge | Info |",
    "project": "schema_semantic_constrained_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 2627 · 2026-05-23T12:56:13.290462+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2216d5b8b87a9472ce204aba11481390:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4201
}
```

</details>

---


### Assistant

_source line 2628 · 2026-05-23T12:56:29.136933+00:00_

**Round 26 审稿完成。**

报告已投递至 Research Director。

**最终评分：3.0 (Findings)**

核心发现：
- **1 个 Critical**：DR→CF trade-off 的 Abstract/正文 framing 严重不平衡（zero-shot 净违规仅降约 40%，非 headline 暗示的 99%）
- **5 个 Major (Should-Fix)**：WikiEvents n=20 不足以支撑 generalization claim；70B 单一模型族混淆三个变量；Proposition 1 证明 position/name-based gap；F1 缺失上下文参照（降级自 R2 Critical）；GoLLIE 对比缺失（降级自 R2 Critical）；Contribution 1 Mistral 覆盖 overclaim
- **6 个 Info (Minor)**：Abstract F1 范围、CF 统计检验、LoRA 迁移 caveat、正文视觉密度、缩写密度、Proposition 1 novelty
- **主要优势**：评估全面性罕见（40 页 48+ 表格）、统计方法规范、Limitations 诚实、框架 model-agnostic 可组合

R1 (3.5) 与 R2 (3.0) 的分歧主要在 novelty 评估和监督 baseline/GoLLIE 对比的重要性。Director 采纳 R1 的定位论证（约束框架 vs IE 系统不可直接对比）降级相关 issues，但综合评估论文的概念新颖性有限（XGrammar + stateful type checker 的自然组合），Findings track 是恰当定位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 197

## Round 197

2 recorded events


### User

_source line 2629 · 2026-05-23T12:56:31.703916+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 全部审稿意见的逐条回应，汇报给 Review Director。

要点总结：
- 8 个 Weaknesses 中同意 6 个（W1 部分、W2、W3、W5、W6、W8），反驳 1 个（W7 Abstract 字数未超限），W4（Proposition 1 gap）同意观察但反驳其对结论的影响
- 5 个 Questions 中同意 4 个（Q1-Q4），反驳 1 个（Q5：beam k=4 不损失 recall）
- 3 个 Missing References 全部同意
- 与 R1 的主要分歧：R1 给 3.5 我给 3.0，我认为 novelty 更有限；R1 未指出的两个 Critical 问题（缺监督 baseline、GoLLIE 对比回避）我认为同样严重

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2630 · 2026-05-23T12:56:47.189204+00:00_

审稿报告已投递至 Research Director。

**Round 26 审稿完成。**

**最终评分：3.0 (Findings)**

核心结论：
- **1 个 Critical**：DR→CF trade-off 的 Abstract/正文 framing 严重不平衡（zero-shot 净违规仅降 ~40%，非 headline 暗示的 99%）
- **6 个 Major/Warning**：WikiEvents n=20 不足、70B 单一模型族混淆变量、Proposition 1 形式化 gap、缺监督 baseline 上下文参照（降级）、GoLLIE 对比缺失（降级）、Contribution 1 Mistral 覆盖 overclaim
- **6 个 Minor/Info**：Abstract F1 范围、CF 统计检验、LoRA caveat、视觉密度、缩写密度、Proposition 1 PL 已知性
- **主要优势**：评估全面性罕见（40 页 48+ 表格）、统计方法规范、Limitations 诚实、框架 model-agnostic 可组合
- **Reviewer 分歧**：R1 给 3.5（Borderline Conference），R2 给 3.0（Findings），分歧源于 novelty 评估和监督 baseline/GoLLIE 对比的重要性。Director 裁定 3.0——论文主要贡献在工程实践和实证分析，Findings track 是恰当定位

Issue Tracker 已同步更新（12 个 open issues + 历史 resolved issues）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 198

## Round 198

17 recorded events


### User

_source line 2631 · 2026-05-25T21:14:38.196800+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema_semantic_constrained_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2632 · 2026-05-25T21:14:44.230213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2633 · 2026-05-25T21:14:44.282101+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2634 · 2026-05-25T21:14:49.370099+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2635 · 2026-05-25T21:14:49.421165+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2636 · 2026-05-25T21:14:53.598278+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2637 · 2026-05-25T21:14:53.649166+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2638 · 2026-05-25T21:14:58.620261+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2639 · 2026-05-25T21:14:58.620755+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2640 · 2026-05-25T21:15:06.406661+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2641 · 2026-05-25T21:15:06.960077+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (164 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **r16_70b_lora_scierc_eval** (success): 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale\n- **p1_llama_ee_ft** (killed): —\n- **sf2_70b_prompt_sensitivity** (success): 70B LLaMA-3.1 constrained decoding should show consistent violation reduction across different prompt styles, similar to the 8B result where ΔDR was 94.0-94.6% regardless of prompt variant.\n\n## 趋势\n成功 133 / 负向 15 / 失败 11 / 共 164\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-16980: 无 GPU 信息\nwestd-21461: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_phase0_docred_schema_r2: 已被终止 — unknown\n- w1_cf_fallback_docred: 已被终止 — unknown\n- w1_cf_fallback_llama_scierc: 已被终止 — unknown\n- w1_cf_fallback_llama_docred: 已被终止 — unknown\n- w9_qwen_docred_zs_sampling: 训练失败 — unknown\n- p8b_docred_latency: 训练失败 — unknown\n- p1_ee_ft_composability: 训练失败 — unknown\n- p1_ee_ft_composability_r2: 训练失败 — unknown\n- p1_ee_ft_composability_r3: 训练失败 — unknown\n- p1_ee_ft_composabil
…[truncated 269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 2642 · 2026-05-25T21:15:07.010744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2643 · 2026-05-25T21:15:07.061417+00:00_

1	\documentclass[11pt]{article}
2	
3	\PassOptionsToPackage{table}{xcolor}
4	\usepackage[review]{acl}
5	
6	\usepackage{times}
7	\usepackage{latexsym}
8	\usepackage[T1]{fontenc}
9	\usepackage[utf8]{inputenc}
10	\usepackage{microtype}
11	% \usepackage{inconsolata}  % optional per ACL template; not available in this TeX Live
12	\usepackage{graphicx}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{amsmath}
16	\usepackage{amssymb}
17	\usepackage{amsthm}
18	\usepackage{enumitem}
19	\usepackage{pifont}
20	\usepackage{soul}
21	\usepackage{tikz}
22	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Related Work ===
38	\input{section6_related_work}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §5 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §6 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_crossmodel_draft}
56	\input{section5_wikievents_draft}
57	\input{section5_runtime}
58	
59	% === §7 Discussion and Conclusion ===
60	\section{Discussion and Conclusion}
61	\label{sec:discussion}
62	\input{section7_conclusion_compressed}
63	
64	% === Limitations ===
65	\section*{Limitations}
66	
67	Per-triple enforcement creates a DR$\leftrightarrow$CF trade-off; global type consensus during decoding remains future work.
68	Evaluation covers 8B/70B models on two RE and one EE dataset; smaller-model and non-English generalization is untested.
69	Empirical type constraints are derived from training data (9
…[truncated 1141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2644 · 2026-05-25T21:15:07.061817+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2645 · 2026-05-25T21:15:07.262979+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_27/submitted.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_27/submitted.pdf"
  }
}
```

</details>

---


### Tool result

_source line 2646 · 2026-05-25T21:15:07.363879+00:00_

This PDF has 39 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 2647 · 2026-05-25T21:19:32.812447+00:00_

开始审稿流程。先执行初始化和资料检查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 199

## Round 199

12 recorded events


### User

_source line 2648 · 2026-05-25T21:25:01.207383+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
**侧重**: 新颖性 + 完整性 + 写作质量
**Venue**: EMNLP 2026 via ARR (May 2026 cycle)

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**Confidence**: 4/5 (高置信度；熟悉 constrained decoding 和 IE 领域)
**一句话总结**: 工程完整度高、实验扎实的系统论文，但核心技术新颖性有限（stateful masking 已在 code generation 中充分探索），70B 和 WikiEvents 的 generalization claim 支撑不足。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验设计严谨，bootstrap CI + Bonferroni correction + causal tracing 做到了高标准；但 Proposition 1 的形式化有瑕疵（位置索引 vs 名称引用的 gap 降低了证明力度） |
| Excitement / Novelty | 2.5/5 | 技术路线 (ontology → token mask) 直接迁移自 PICARD/Mündler et al.；"从 grammar 扩展到 semantic" 的框架贡献明确但增量性质较强；非加性交互发现有一定新颖性但属于实验观察而非方法创新 |
| Clarity | 4/5 | 写作密度高且结构清晰；但 CF 讨论分散在多处（§5、§4、Appendix B），读者难以一次性获取完整图景 |
| Reproducibility | 4.5/5 | 匿名代码+详细附录+确定性实验(greedy)；LoRA 超参从 SciERC 迁移至 DocRED 未做 dataset-specific tuning 这一点诚实报告 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Novelty claim 过度——与 Mündler et al. (2025, PLDI) 的技术距离被低估

- 具体位置：§1 第3段 ("OntoCoDec fills this gap")、§2 "Constrained decoding" 段、Appendix B "Semantic Constrained Decoding for Code" 段
- 问题：论文承认 Mündler et al. 使用了相同的 "type system → automaton → logits mask" pipeline (Appendix B line 29)，声称差异在于 "IE entity types are inferred from text rather than statically declared"。但 OntoCoDec 的 entity registry 本质上是一个 runtime symbol table——这在 PL 编译器中是标准数据结构。论文未提供任何 IE-specific algorithmic innovation 超越 "将已有范式应用于新领域"。PICARD (2021) 已经实现了 incremental parsing + type checking during decoding；Synchromesh (2022) 已展示 semantic constraints as dynamic token masks conditioned on generation prefix。OntoCoDec 的核心 mask computation（§3.4 Dynamic masking）是 $O(|V|)$ lookup，算法复杂度与 PICARD 一致。
- 为什么影响接收：如果 novelty 主要是 domain adaptation（从 code→IE），论文应在 framing 上诚实承认并强调 IE-specific challenges 的系统工程贡献，而非暗示方法论创新。当前 framing 让读者期待新的约束推理算法，但实际提供的��一个 well-engineered 的领域迁移。
- 建议修改方向：(1) 在 Introduction 中明确说明 "We adapt the type-constrained decoding paradigm (previously demonstrated for code generation) to the IE domain, where entity types must be dynamically inferred"; (2) 将 contribution statement 的重心从 "two-layer framework" 转向 "IE-specific enabling dependency finding" + "systematic empirical characterization of DR/CF trade-off"。

**N2** [critical] Proposition 1 的证明力度被自身 caveat 削弱

- 具体位置：Appendix T (§app:pumping-lemma)，特别是 "Position indexing vs. name referencing" 段落
- 问题：论文的 pumping lemma proof 使用 position-based entity indexing，然后在证明结束后用一段话承认 "Case 1 of the pumping argument does not directly apply under name-based referencing"。论文辩称 "the non-context-free conclusion still holds via a stronger argument: validating type consistency requires a name→type lookup over dynamically generated bindings, which is a random-access map operation"——但这个 "stronger argument" 本身没有给出形式化证明，只是一个直觉性断言。如果要声称正式的 non-context-free result，证明必须在实际使用的表示（name-based referencing）上成立，而非在一个已承认不直接适用的简化表示上成立。
- 为什么影响接收：Proposition 1 被列为第一个 contribution bullet point 的一部分（"Proposition 1; §3.2"）。如果形式化有漏洞，该 contribution 的重量需要降级。
- 建议修改方向：要么 (a) 提供基于 name-based referencing 的完整形式化证明（可能需要用 indexed grammar 或 transducer 理论），要么 (b) 将 Proposition 1 降级为 "informal argument" 并调整 contribution statement。

**N3** [critical] WikiEvents "event extraction generalization" claim 基于 n=20 的 fine-tuning 评估

- 具体位置：§1 Contribution 3 ("event extraction generalization on WikiEvents")、§6.4 (正文只有4行)、Appendix W (Table 8)
- 问题：正文 §6.4 自己写道 "fine-tuning composability is preliminary (n=20)"，Appendix 报告 "MDE≈±5.0 pp; results are directional only"。但 Contribution 3 将 WikiEvents 作为 "supporting validation" 之一列出，且未在 contribution statement 中加任何 caveat。Zero-shot evaluation (n=246) 只验证了 vocabulary constraint (EV/RoV elimination)，而非 OntoCoDec 的核心 semantic constraint (AC remains 1.3-3.8%)。基于 20 个测试文档的 fine-tuning 实验不足以支撑 "generalization" claim。
- 为什么影响接收：过度声称 generalization 是 novelty inflation 的一种形式；reviewer 预期 contribution 有足够的实验支撑。
- 建议修改方向：(1) 将 WikiEvents 从 Contribution 3 降级为 "preliminary evidence suggesting applicability to event extraction" 而非 "generalization"；(2) 在正文中诚实标注 "pilot study" 而非 "validation"；(3) 增加 WikiEvents test set 的样本量（如果数据允许）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "Severity downgrade" framing 对 CF 的处理不够 balanced

- 具体位置：§1 第4段、§7 Discussion、Figure 6
- 问题：论文反复强调 DR→CF 是 "severity downgrade"，但在 zero-shot setting 下：
  - SciERC: DR 从 15.37% 降到 0.93%，但 CF 从 0.08% 升到 9.90%（+9.82 pp）
  - DocRED Llama: CF 达 12.02%
  这意味着 OntoCoDec 在 zero-shot 下引入了大量新的 CF 违规。虽然论���在 §4 和 Appendix B 详细分析了这一 trade-off，但 Introduction 和 Conclusion 中的 framing 给读者的印象是 "violations are simply downgraded" 而非 "one type of violation is traded for another at higher rate"。
- ��议：在 Introduction 中加入一句 "though CF rises to up to 12% under zero-shot, it is practically eliminated by fine-tuning (≤1.4%) or beam search"，让 framing 更加 balanced。

**W2** [warning] 70B validation 基于单一模型族的单一量化变体

- 具体位置：§6.5 (70B-class validation)、§1 Contribution 3
- 问题：所有 70B 结果来自 Llama-3.1-70B AWQ INT4——单一模型族的单一量化配置。论文正文和 contribution statement 中使用的 "scale-dependent" 结论隐含了跨模型族的 generality，但实际数据只有一个数据点。AWQ INT4 量化可能改变模型的 type calibration 行为，这一点虽在 Appendix (app:quantization) 讨论但不在正文中提及。
- 建议：(1) 将 "scale-dependent finding" 的措辞改为 "scale-dependent observation on Llama-3.1-70B"；(2) 在正文中简要承认量化的潜在影响；(3) 如果条件允许，增加一个非 Llama 的 70B-class 模型（如 Qwen2.5-72B）。

**W3** [warning] 未与 GoLLIE 进行直接数值对比

- 具体位置：Appendix U (GoLLIE Comparison)
- 问题：论文声称 OntoCoDec 与 GoLLIE 等 training-based approaches "orthogonal and complementary"（§1 最后一段），但 Appendix U 明确表示没有做直接对比实验，理由是 "incompatible evaluation settings"。对于一篇声称填补 runtime enforcement gap 的论文，不与最强的 schema-aware IE baseline 对比（哪怕在简化设置下）是一个明显的实验缺陷。GoLLIE 的 zero-shot SciERC 结果是公开的，OntoCoDec 可以在相同测试集上对比 violation rate（即使 F1 不直接可比）。
- 建议：即使 F1 不直接可比，至少报告 GoLLIE 在相同 SciERC 测试集上的 DR/CF violation rate，以量化 "training alone cannot eliminate violations" 的 claim。

**W4** [warning] "Near-zero violations" claim scope 需要更清晰的 qualification

- 具体位置：Abstract ("beam search (k=4) achieves near-zero violations")、§6.5
- 问题：Abstract 中 "near-zero violations" 的表述暗示这是 OntoCoDec 的一般性结论。但实际条件是：LoRA fine-tuning + beam k=4 + 特定模型（Llama-3.1-8B achieves DR=RV=ET=0%；Qwen3-8B 仍有 ≤0.01% residual CF）。在不同条件下（zero-shot，greedy），violations 远不是 near-zero（DR 0.93%, CF 9.90%）。
- 建议：Abstract 中明确 "beam search (k=4) with LoRA fine-tuning achieves near-zero violations on 8B models"。

---

## 小问题（不影响接收）

- §3 Preliminaries 定义 $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$，但后文又说 constraints are "extracted from observed type pairs in training data"（§6 Setup），不是来自 formal ontology。这种 empirical constraint table 与 "ontology" 的术语使用有 gap，应在 Preliminaries 中 acknowledge。
- Table 1 的 "GCD-equiv.†" 行使用 vLLM guided_json 而非 GCD 本身——这在脚注中说明了，但 row label "GCD-equiv." 可能让快速阅读的读者误以为使用了 GCD 的官方实现。
- Appendix Discussion Table 5 中 exp_id (phase2_scierc_full_s1) 残留在 caption 中——应在提交前清除。
- §4 "Constraint Tightness" 中 $R^2=0.886$ 的线性拟合基于 n=4 (p=0.058)——论文诚实标注了 "descriptive only"，但即便如此，在正文中引用一个不显著的回归结果并赋予它因果解释框架的地位，可能给读者造成 over-interpretation 的印象。
- Figure caption 6 使用 "irrecoverable" 来描述 DR——这一术语选择略有夸大；在下游 pipeline 中 DR violations 也可以通过 re-extraction 或 human correction 恢复。

---

## 潜在遗漏的相关工作

1. **Draft-Conditioned Constrained Decoding (DCCD)** (Reddy et al., arXiv 2603.03305, March 2026)：该工作提出先无约束生成 draft 再 conditioned constrained decoding 的两步方法，直接解决了 constrained decoding 导致 quality degradation 的问题——与论文 Appendix B "Quality Impact of Constrained Decoding" 段落高度相关，但未被引用。
2. **llguidance** (Microsoft, 2025-2026)：作为 vLLM/SGLang 之外的另一主流 constrained decoding backend（基于 Earley parser），在 "Grammar-Constrained Decoding" related work 中值得提及作为 implementation landscape 的补充。
3. **OntoKG** (arXiv 2604.02618, April 2026)：ontology-oriented KG construction with intrinsic-relational routing——虽然方法不同，但 problem framing 有重叠（ontology-constrained KG construction from text）。

（以上 2-3 条不属于必须引用，但 1 条 DCCD 较为重要，因为它直接回应了论文 discussion 中 "IE is robust to format constraints" 的论证。）

---

## 主要优势

- **实验标准极高**：Bootstrap CI、Bonferroni correction、causal tracing、power analysis、6种 configuration 的交叉验证——这是 NLP 论文中难得的统计严谨性。
- **Transparency 值得称赞**：论文诚实报告 CF trade-off、WikiEvents 样本量限制、线性拟合不显著、GoLLIE 对比困难——这种学术诚信比 over-claiming 好得多。
- **系统设计完整**：grammar-first fallback、continuation masking for BPE、order-invariance verification——这些工程细节展示了 production-ready 的设计。
- **Non-additive interaction finding** 是本文最有价值的实证贡献：grammar-only 3% + semantic-only 24% = composed 94% 这一结果本身就值得发表，尤其是 scale-dependent 的变化趋势（70B 下 semantic-only 达到 84%）。

---

## 总结

这是一篇高质量的系统/实证论文，工程完整度和实验严谨性达到了顶会水准。主要不足在于：(1) 核心技术新颖性有限——本质上是 PICARD/Mündler et al. 的 IE 领域迁移；(2) Proposition 1 的形式化存在已承认的漏洞；(3) 部分 generalization claim（WikiEvents、70B scale）的实验支撑不足。如果作者能降低 novelty claim 的力度，将论文定位为 "rigorous empirical study of type constraint enforcement for IE"（强调 non-additive interaction finding 和 DR/CF trade-off characterization），会更匹配实际贡献。当前版本介于 Conference 和 Findings 之间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2649 · 2026-05-25T21:25:46.008022+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2650 · 2026-05-25T21:25:46.009018+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 2651 · 2026-05-25T21:25:46.009337+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2652 · 2026-05-25T21:25:46.009551+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2653 · 2026-05-25T21:25:46.009806+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool call

_source line 2654 · 2026-05-25T21:25:46.414075+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool call

_source line 2655 · 2026-05-25T21:25:46.565046+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2656 · 2026-05-25T21:25:46.615837+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (164 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **r16_70b_lora_scierc_eval** (success): 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale\n- **p1_llama_ee_ft** (killed): —\n- **sf2_70b_prompt_sensitivity** (success): 70B LLaMA-3.1 constrained decoding should show consistent violation reduction across different prompt styles, similar to the 8B result where ΔDR was 94.0-94.6% regardless of prompt variant.\n\n## 趋势\n成功 133 / 负向 15 / 失败 11 / 共 164\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-16980: 无 GPU 信息\nwestd-21461: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_phase0_docred_schema_r2: 已被终止 — unknown\n- w1_cf_fallback_docred: 已被终止 — unknown\n- w1_cf_fallback_llama_scierc: 已被终止 — unknown\n- w1_cf_fallback_llama_docred: 已被终止 — unknown\n- w9_qwen_docred_zs_sampling: 训练失败 — unknown\n- p8b_docred_latency: 训练失败 — unknown\n- p1_ee_ft_composability: 训练失败 — unknown\n- p1_ee_ft_composability_r2: 训练失败 — unknown\n- p1_ee_ft_composability_r3: 训练失败 — unknown\n- p1_ee_ft_composabil
…[truncated 269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 606
}
```

</details>

---


### Tool result

_source line 2657 · 2026-05-25T21:25:46.616387+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 202
}
```

</details>

---


### Tool result

_source line 2658 · 2026-05-25T21:25:46.616723+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:16:38.989379+00:00\", \"completed_at\": \"2026-05-25T21:20:29.968146+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页纯文本无任何 display item，首个视觉锚点（Figure 1）到 page 3 才出现。对于实证贡献为主的论文，在 page 1 或 2 加入 teaser figure 或核心结果 preview 可强化审稿人第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 5 的 x 轴 relation type 标签旋转后字号偏小（约为正文 60-70%），建议适当增大或使用缩写\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 和 Figure 3 使用红色和蓝/绿色组合，大部分情况可区分，但红绿搭配对 deuteranopia 色盲可能有风险；建议改用 blue+orange 双色方案\"}, {\"severity\": \"info\", \"dimension\": \"page 12-16\", \"message\": \"Appendix B（Extended Related Work）+ C（Extended Discussion）连续 5 页纯文本，虽为 appendix 可接受，但密度极高\"}, {\"severity\": \"info\", \"dimension\": \"page 39\", \"message\": \"末页内容约占 80%，Section T (Use of AI Assistants) 列表较简短，整体可接受\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 2659 · 2026-05-25T21:26:21.418287+00:00_

收到 Reviewer 2 的审稿意见。让我先加载审稿流程并检查当前状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 200

## Round 200

20 recorded events


### User

_source line 2660 · 2026-05-25T21:26:22.416369+00:00_

[系统通知] Reviewer 2 的审稿进程异常终止。
可能原因：消息处理超时（20 分钟 deadline）或子进程崩溃。
如需该 Reviewer 重新审稿，请重新分配审稿任务。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
**Venue**: EMNLP 2026 via ARR (May 2026 cycle)
**审查侧重**: 方法严谨性 + 实验设计

---

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 问题动机清晰、实验异常充分（39页附录），但 CF 违规的根本性限制削弱了"severity downgrade"的核心论证，且贡献以工程整合为主，理论新颖度有限。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 形式化分析（Proposition 1, decidability taxonomy）扎实，实验设计严谨且有大量控制实验，但 DR→CF "severity downgrade" 的论证存在逻辑缺口 |
| Excitement | 3.5/5 | 非加性层交互发现（3%+24%→94%）新颖且有洞见，但语义层本质上是动态查找表+logit masking，方法层面的创新相对有限 |
| Reproducibility | 5/5 | 超参全部报告（App G），确定性验证（Table 29, 3 seeds × 2 models），硬件/软件版本完整，bootstrap power analysis，几乎是教科书级别的可复现性 |
| Overall Assessment | 3.5/5 | 扎实的工程贡献 + 有价值的实证发现，但理论贡献（Proposition 1）与实现之间有 gap，CF 限制是根本性的 |
| Confidence | 4/5 | 熟悉约束解码和 IE 领域，仔细阅读了全文含所有附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DR→CF "severity downgrade" 论证不充分

- 具体位置：§4 (lines 363-375), §5.1 (lines 477-484), Figure 4, Table 8 (p.20)
- 问题：论文将 DR→CF 转换定义为"严重性降级"——DR 是不可恢复的（corrupt KG），CF 是可修复的（individually valid triples）。但 Table 8 显示 58.1% 的 CF violations 来自 "hallucinated entity"（模型生成了输入中不存在的实体名），此时 first-seen type lock 将错误类型传播到该实体的所有后续 triples。这些 CF violations 的下游危害可能与 DR violations 同等严重——它们不仅是"跨 triple 类型不一致"，而是系统性地将错误类型锁定到所有引用该幻觉实体的 triples。论文未量化：每个 hallucinated-entity CF violation 平均影响多少个下游 triple？这些被影响的 triples 中有多少会产生 KG 污染？
- 为什么影响接收：这是论文核心论点（§4, §6 的 "severity downgrade, not error introduction"）的关键支撑。如果 58% 的 CF 实际上也会导致 KG 污染，则 DR→CF 转换的实际收益被高估。
- 建议修改方向：(1) 在 Table 8 基础上增加分析：对每类 CF source，追踪其下游影响（受影响 triple 数 × 是否导致 KG 错误）；(2) 在 §4 的 severity downgrade 讨论中增加限定条件：仅当 first-seen type 正确时，CF 才是真正的 severity downgrade；当 first-seen type 错误（hallucinated entity + true cascade error = 65.4%）时，CF 的危害接近 DR。

**N2** [critical] Proposition 1 的 proof-implementation gap 在正文中未充分交代

- 具体位置：§3 lines 218-222 引用 Proposition 1；完整 proof 在 Appendix O (p.36-37)
- 问题：正文 §3 直接引用"proof via pumping argument in Appendix O"作为两层架构的理论基础，但 proof 使用 position-based entity indexing（e_k at position k），而 OntoCoDec 实际使用 name-based referencing（entity registry keyed by name）。Appendix O (lines 2822-2849) 对此有详细讨论，论证 name-based 严格包含 position-based，因此不削弱结论。但这一关键 nuance 在正文中完全没有提及。读者如果只读正文，会误以为 proof 直接证明了 OntoCoDec 的设计必要性，而实际上 proof 证明的是一个更弱的（position-based）形式化问题。
- 为什么影响接收：Proposition 1 是两层架构的理论支柱（§3 的 design motivation）。正文应让读者清楚 proof 的范围和实现之间的关系，否则有 overclaim 嫌疑。
- 建议修改方向：在 §3 引用 Proposition 1 的地方添加一句："The proof formalizes constraints via position-based indexing; OntoCoDec's name-based entity registry implements a strictly more expressive variant (Appendix O)." 这不需要额外空间，只需一句话。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] SciERC→DocRED 迁移限制了 fine-tuning claims 的 generalizability

- 具体位置：§5 lines 429-433, Table 2
- 问题：所有 fine-tuning 实验仅在 SciERC 上训练 LoRA adapter，然后直接迁移到 DocRED（96 relations, κ̄=0.842）。论文承认"this transfer may underestimate DocRED fine-tuning potential"(line 432)，但 fine-tuning composability 的核心声明（"DR ≤ 0.21% with minimal F1 impact"）主要基于 SciERC 结果。DocRED 的迁移结果（DR=0.01-0.21%）虽然也很好，但由于约束动态在高 κ̄ schema 下有质的不同（grammar-first fallback 频率、semantic mask conflict rate），缺少 DocRED-specific fine-tuning 的 upper bound 对比。
- 建议：在 Limitations 中明确这一点，或增加一组 DocRED-specific fine-tuning 实验（即使只在小子集上）。

**W2** [warning] WikiEvents fine-tuning composability 样本量不足

- 具体位置：§5.3 lines 525-529, Appendix P (p.38), Table 30 (p.30)
- 问题：WikiEvents fine-tuning composability 仅在 n=20 test documents 上评估。Table 30 显示 MDE = ±3.0 pp，远大于预期的 F1 变化量。论文声明"fine-tuning composability is preliminary"(Limitations, line 598)，但主文 §5.3 的措辞（"confirms constraint applicability to event extraction"）暗示了比数据支撑更强的结论。
- 建议：§5.3 的 fine-tuning 部分应更加谨慎地限定措辞，明确标注 preliminary nature。

**W3** [warning] Figure 3 的 dual-factor model 基于 n=4 个数据点，统计说服力不足

- 具体位置：§4 lines 377-385, Figure 3 (p.5), Appendix C (p.18, lines 1560-1571)
- 问题：Figure 3 展示 residual DR vs. κ̄ × RV_baseline 的线性拟合，R²=0.886，但仅有 n=4 个数据点（2 models × 2 datasets）。论文在 Appendix C 中明确承认"p ≈ 0.058; with only four data points, this constitutes a descriptive characterization rather than a confirmatory statistical test"(lines 1565-1568)。但主文 §4 对此的呈现（Figure 3 标题包含 "R²=0.886"）可能让读者高估统计可靠性。
- 建议：§4 主文引用 Figure 3 时应增加 "(n=4, descriptive only)" 的限定。

**W4** [warning] 缺少与运行时语义约束系统的实验对比

- 具体位置：§2 Related Work, Table 16 (p.25)
- 问题：Table 16 与 grammar-based constrained decoding 方法（GCD, BoostCD, vLLM）进行了系统对比，但缺少与任何做运行时语义级约束执行的系统的实验对比。论文引用了 IterGen (Ugare et al., 2025) 和 EnriCo (Zaratiana et al., 2024)，两者都在生成过程中执行语义约束（IterGen 通过 backtracking，EnriCo 通过 ASP constraints）。虽然这些系统针对不同的 IE 子任务或数据集，无法直接公平对比，但缺少任何 runtime semantic enforcement baseline 使得贡献的增量性（over grammar-only）缺乏外部参照。
- 建议：在 Related Work 或 Discussion 中增加一段定性对比表，说明 OntoCoDec 与 IterGen/EnriCo 在 constraint scope、enforcement mechanism、scalability 上的具体差异。

**W5** [warning] Entity registry 的 first-seen semantics 在高实体重复文档中的行为未充分分析

- 具体位置：§3.3 lines 294-306, Appendix C (p.17)
- 问题：Entity registry 使用 first-seen semantics：第一次出现的实体类型锁定所有后续约束检查。论文在 Appendix C 详细分析了 fallback 行为，但未分析：当同一实体在文档中多次出现（如 DocRED 的长文档），且不同出现在不同关系上下文中需要不同类型时，first-seen lock 产生的 CF violations 如何随文档长度和实体重复次数增长？Table 31-32 分析了文档长度对 violation rates 的影响，但只看了总体 violation rates，未单独分析 CF 的文档长度依赖。
- 建议：增加 CF violation rate vs. document length 的分析，或 vs. average entity mention count 的分析。

---

## 小问题（不影响接收）

1. **Abstract 字数**：请确认 Abstract ≤ 200 words（EMNLP 2026 限制）。视觉估算约 220-240 词，可能超限。
2. **符号一致性**：σ(r)（§3.1 line 167）和 dom(r)/range(r)（§3.3 lines 263-265）在不同位置交替使用，建议统一或在首次出现时明确定义关系。
3. **Table 1 标题**：Table 1 标题说 "Five-way ablation" 但实际只有 6 行（包括 Unconstrained），建议改为 "Six-configuration ablation" 或明确说明 Unconstrained 是 baseline 不计入 ablation。
4. **Appendix T — AI 助手声明**：声明使用了 Claude (Anthropic) 进行 code drafting、writing polishing 和 literature summarization。这是透明且合规的，但建议确认 ARR 的 AI 使用政策是否要求在 submission form 中额外声明。
5. **§5.1 "grammar becomes a no-op"**：(line 499) 在 fine-tuning 下 grammar layer 对 DR 的贡献 <0.2 pp，但论文仍声称 grammar 是 semantic layer 的 "prerequisite"（enabling dependency）。这在逻辑上没有矛盾（fine-tuning 使模型已内化 grammar 约束），但可以更清晰地解释为什么 fine-tuning 下 grammar 仍有结构性价值。
6. **匿名性**：Footnote 1 提供了匿名链接 `anonymous.4open.science/r/schema_semantic_constrained_ie-FE20/`，格式合规。

---

## Questions to Authors

1. Table 8 的 hallucinated entity CF violations (58.1%)：这些 CF violations 平均每个影响多少个后续 triples？是否有案例分析表明 first-seen type 错误导致了连锁 KG 污染？
2. 是否考虑过在 entity registry 中实现 "soft" type assignment（如基于 count 的多数投票）而非 first-seen hard lock？如果有，为什么放弃了这个设计？
3. Figure 3 的 dual-factor model 如果增加 Mistral-7B 的两个数据点（Table 48 中有数据），R² 和 p 值如何变化？
4. IterGen (Ugare et al., 2025) 使用 backtracking 解决语义约束冲突——如果 OntoCoDec 的 grammar-first fallback 不触发（即 S(t) ∩ G(t) ≠ ∅），OntoCoDec 是否也保证了 type validity？如果是，能否量化这一比例？

---

## Missing References

- **Zhou et al. (2026)** "From hallucination to structure snowballing" — 论文已引用，但可以更紧密地与 §4 的 constraint interaction analysis 关联，因为 structure snowballing 直接描述了 grammar constraint 导致的级联错误。
- **Geng et al. (2025) JSON-SchemaBench** — 论文已引用，可考虑在 §5 实验部分讨论 OntoCoDec 在 JSON-SchemaBench 上的 schema coverage。
- 无 missing 的关键 baseline reference。引用覆盖全面。

---

## 主要优势

1. **实验深度和广度异常出色**：39 页附录涵盖 49 个 tables、8 个 figures，包括 6-way ablation、cross-model validation（3 models × 2 datasets）、beam search analysis、per-relation breakdown、统计显著性检验、prompt sensitivity analysis、document length analysis、quantization robustness、sampling robustness、lucky violation analysis、full fine-tuning baseline、TCR post-hoc resolution。在 ARR 投稿中罕见地达到了近乎穷尽的实验覆盖。

2. **非加性层交互发现**是真正的 insight：grammar-only 3% + semantic-only 24% → composition 94% (3.5× additive prediction)。这不仅验证了两层设计的必要性，还揭示了 grammar layer 作为 semantic layer 的 enabling prerequisite 的机制（vocabulary + structural enforcement creates clean input for type lookups）。Scale-dependent interaction (24%@8B → 84%@70B) 进一步支撑了这一发现。

3. **形式化分析扎实**：Proposition 1 通过 pumping lemma 证明了 domain/range type constraints 超出 CFG 表达能力，为两层架构提供了理论基础。Finite entity set 的 DFA state explosion analysis 补充了实际工程动机。

4. **可复现性近乎完美**：确定性验证（3 seeds, same-GPU byte-identical for 2/3 seeds, Table 29）、cross-hardware floating-point divergence quantification (σ < 0.5 pp)、200-document subset power analysis、bootstrap CIs with Bonferroni correction。

5. **实际部署价值**：method 无需 constraint-specific training，支持 greedy/beam/sampling decoding，与 LoRA fine-tuning 兼容，runtime overhead +10-13%，constraint compilation < 0.5s。beam search (k=4) 实现 near-zero violations across all metrics on calibrated models。

---

[Reviewer 1 审稿结果]:
获取了 ARR 评分标准。论文共 39 页。先阅读前 10 页，同时渲染剩余页面和获取 ARR review form 详情。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2661 · 2026-05-25T21:26:49.691373+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_post_to_reviewer,get_visual_check_status,get_external_review_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_post_to_reviewer,get_visual_check_status,get_external_review_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2662 · 2026-05-25T21:26:49.742057+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2663 · 2026-05-25T21:26:55.128527+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2664 · 2026-05-25T21:26:55.179357+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2665 · 2026-05-25T21:27:24.608478+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 1 审稿任务（重新分配）\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 via ARR (May 2026 cycle)\n**格式要求**: Long paper, 正文严格 8 页限制, references 无限, Limitations 必须在正文内且不计入页数限制, Abstract ≤ 200 words\n**匿名规则**: ARR 双盲审稿\n\n**论文文件**:\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_27/submitted.pdf`\n\n**你的审查侧重**: **新颖性 + 论文完整性**\n\n请重点关注以下方面：\n1. **新颖性评估**: 论文的核心贡献（两层约束解码架构：grammar layer + semantic layer）相对于现有方法（grammar-only constrained decoding 如 GCD/BoostCD/vLLM, 以及 runtime semantic enforcement 如 IterGen/EnriCo）的增量创新程度。区分工程贡献和学术贡献。\n2. **Related Work 覆盖度**: 是否遗漏了重要的相关工作？引用是否真实且准确？\n3. **论文结构与完整性**: 论文叙事是否连贯？各章节是否完整？Limitations 是否充分？\n4. **写作质量**: 符号一致性、术语定义、图表质量、可读性\n5. **格式合规性**: 检查 Abstract 字数（≤200 words）、正文页数（≤8 pages）、Limitations section 位置和长度、匿名性\n\n**ACL ARR Overall Assessment 评分标准**:\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n请按以下结构输出审稿意见：总体评分 → 官方维度打分（Soundness, Excitement, Reproducibility, Overall Assessment, Confidence）→ Must-Fix → Should-Fix → 小问题 → Questions to Authors → Missing References → 主要优势",
  "reviewer_id": "2",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 1 审稿任务（重新分配）\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 via ARR (May 2026 cycle)\n**格式要求**: Long paper, 正文严格 8 页限制, references 无限, Limitations 必须在正文内且不计入页数限制, Abstract ≤ 200 words\n**匿名规则**: ARR 双盲审稿\n\n**论文文件**:\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_27/submitted.pdf`\n\n**你的审查侧重**: **新颖性 + 论文完整性**\n\n请重点关注以下方面：\n1. **新颖性评估**: 论文的核心贡献（两层约束解码架构：grammar layer + semantic layer）相对于现有方法（grammar-only constrained decoding 如 GCD/BoostCD/vLLM, 以及 runtime semantic enforcement 如 IterGen/EnriCo）的增量创新程度。区分工程贡献和学术贡献。\n2. **Related Work 覆盖度**: 是否遗漏了重要的相关工作？引用是否真实且准确？\n3. **论文结构与完整性**: 论文叙事是否连贯？各章节是否完整？Limitations 是否充分？\n4. **写作质量**: 符号一致性、术语定义、图表质量、可读性\n5. **格式合规性**: 检查 Abstract 字数（≤200 words）、正文页数（≤8 pages）、Limitations section 位置和长度、匿名性\n\n**ACL ARR Overall Assessment 评分标准**:\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n请按以下结构输出审稿意见：总体评分 → 官方维度打分（Soundness, Excitement, Reproducibility, Overall Assessment, Confidence）→ Must-Fix → Should-Fix → 小问题 → Questions to Authors → Missing References → 主要优势",
    "reviewer_id": "2",
    "round_number": "1"
  }
}
```

</details>

---


### Tool call

_source line 2666 · 2026-05-25T21:27:25.060724+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool call

_source line 2667 · 2026-05-25T21:27:25.413789+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2668 · 2026-05-25T21:27:28.485860+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3877
}
```

</details>

---


### Tool result

_source line 2669 · 2026-05-25T21:27:28.486314+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:16:38.989379+00:00\", \"completed_at\": \"2026-05-25T21:20:29.968146+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页纯文本无任何 display item，首个视觉锚点（Figure 1）到 page 3 才出现。对于实证贡献为主的论文，在 page 1 或 2 加入 teaser figure 或核心结果 preview 可强化审稿人第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 5 的 x 轴 relation type 标签旋转后字号偏小（约为正文 60-70%），建议适当增大或使用缩写\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 和 Figure 3 使用红色和蓝/绿色组合，大部分情况可区分，但红绿搭配对 deuteranopia 色盲可能有风险；建议改用 blue+orange 双色方案\"}, {\"severity\": \"info\", \"dimension\": \"page 12-16\", \"message\": \"Appendix B（Extended Related Work）+ C（Extended Discussion）连续 5 页纯文本，虽为 appendix 可接受，但密度极高\"}, {\"severity\": \"info\", \"dimension\": \"page 39\", \"message\": \"末页内容约占 80%，Section T (Use of AI Assistants) 列表较简短，整体可接受\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 3425
}
```

</details>

---


### Tool result

_source line 2670 · 2026-05-25T21:27:28.536946+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3123
}
```

</details>

---


### Tool call

_source line 2671 · 2026-05-25T21:27:37.485760+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2672 · 2026-05-25T21:27:37.536520+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2673 · 2026-05-25T21:27:40.060502+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2674 · 2026-05-25T21:27:41.187871+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (164 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **r16_70b_lora_scierc_eval** (success): 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale\n- **p1_llama_ee_ft** (killed): —\n- **sf2_70b_prompt_sensitivity** (success): 70B LLaMA-3.1 constrained decoding should show consistent violation reduction across different prompt styles, similar to the 8B result where ΔDR was 94.0-94.6% regardless of prompt variant.\n\n## 趋势\n成功 133 / 负向 15 / 失败 11 / 共 164\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-16980: 无 GPU 信息\nwestd-21461: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_phase0_docred_schema_r2: 已被终止 — unknown\n- w1_cf_fallback_docred: 已被终止 — unknown\n- w1_cf_fallback_llama_scierc: 已被终止 — unknown\n- w1_cf_fallback_llama_docred: 已被终止 — unknown\n- w9_qwen_docred_zs_sampling: 训练失败 — unknown\n- p8b_docred_latency: 训练失败 — unknown\n- p1_ee_ft_composability: 训练失败 — unknown\n- p1_ee_ft_composability_r2: 训练失败 — unknown\n- p1_ee_ft_composability_r3: 训练失败 — unknown\n- p1_ee_ft_composabil
…[truncated 269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1127
}
```

</details>

---


### Tool call

_source line 2675 · 2026-05-25T21:27:50.216065+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2676 · 2026-05-25T21:27:50.266777+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2677 · 2026-05-25T21:27:54.799599+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/schema_semantic_constrained_ie/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/schema_semantic_constrained_ie/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6"
  }
}
```

</details>

---


### Tool result

_source line 2678 · 2026-05-25T21:27:57.909734+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "elapsed_ms": 3110
}
```

</details>

---


### Assistant

_source line 2679 · 2026-05-25T21:28:47.842993+00:00_

状态更新：
- **Reviewer 2**: 已重新分配，等待审稿返回
- **视觉审查**: 已完成（0 critical, 1 warning, 4 info）
- **外部审稿**: 未请求

检查项目配置是否启用了外部审稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 201

## Round 201

26 recorded events


### User

_source line 2680 · 2026-05-25T21:34:03.267467+00:00_

[Reviewer 2 审稿意见]:
## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 设计良好、实验扎实的两层约束解码系统，但核心组件（XGrammar + 查找表 + logit masking）的个体新颖性有限，"ontology-compiled"的定位与实际实现（RE 实验中约束从训练数据提取而非本体编译）存在偏差。

## 官方维度打分（来自 ACL ARR review form）
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 核心 claims 有充分实验支撑，统计方法规范（Bonferroni 校正、bootstrap CI、Cohen's d），但"ontology compilation"的 framing 与 RE 实验中从训练数据提取约束的实际做法有偏差 |
| Excitement | 2.5/5 | 工程整合扎实，但各组件缺乏个体新颖性；非加性交互和 scale dependency 是有趣的实证发现，但不足以构成令人兴奋的学术贡献 |
| Reproducibility | 5/5 | 匿名代码仓库、完整 prompt 模板（Table 3）、27 页附录覆盖超参数/数据统计/case study/消融/功率分析/可扩展性基准，再现性极佳 |
| Overall Assessment | 3.5/5 | Borderline Conference — 执行质量达到主会议水准，但新颖性更适合 Findings |
| Confidence | 4/5 | 熟悉约束解码和 IE 领域，仔细审查了论文全文和关键附录 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] "Ontology-Compiled" 定位与实际实现不一致
- 具体位置：Title, Abstract (lines 010-011), Section 3.1 (line 163), Section 5 (lines 419-423)
- 问题：论文标题 "Compiled Schema Constraints" 和方法名 "OntoCoDec (Ontology-Compiled Decoding)" 暗示约束从正式本体编译而来。但 Section 5 (lines 419-423) 明确说明 RE 实验的类型约束是 "extracted from observed type pairs in training data (neither dataset provides a standalone ontology specification)"。只有 WikiEvents 的 EE 实验使用了真正的 KAIROS ontology。这使得论文核心叙事——将 IE 本体编译为 token-level masks——在两个主要评估数据集上并不成立。
- 为什么影响接收：Title/abstract 所承诺的能力（ontology compilation）与实际评估中使用的方法（经验性类型提取）之间的差距可能误导读者。Reviewer 对论文的首要印象来自 title 和 abstract，framing 不当会严重影响可信度。
- 建议修改方向：(1) 修改 title/abstract 更准确地反映约束来源，如 "schema-derived" 或 "type-aware"；(2) 或在 Section 5 开头更突出地讨论约束来源的区别，并明确说明从训练数据提取的约束在什么条件下等价于本体编译。

**N2** [critical] 核心新颖性有限——各组件均为已有技术的直接应用
- 具体位置：Section 3.2, Section 3.3, Section 4
- 问题：Grammar layer 是 XGrammar (Dong et al., 2025) 的直接应用（论文自身承认，Table 1 注释中将 Grammar row 等同于 GCD）；Semantic layer 的核心机制——基于 entity registry 的动态 logit masking——是 constrained beam search 和 type-based filtering 的自然延伸，与 De Cao et al. (2021) 的 autoregressive entity retrieval 和 GenIE (Josifoski et al., 2022) 的 state-based constraints 共享核心思路。两层的组合方式（bitwise AND，Eq. 2）也是标准做法。论文的贡献更多在于系统集成和实证分析，而非方法论创新。
- 为什么影响接收：ACL ARR 的 Excitement 维度评估 novelty 和 impact。论文的 individual components 新颖性不足以支撑主会议接收——Proposition 1 的 decidability analysis 是亮点，但其证明思路（pumping lemma for cross-reference binding）在形式语言理论中是标准技术。
- 建议修改方向：(1) 更明确地将贡献定位为"系统贡献 + 实证发现"而非方法论创新；(2) 强化 Proposition 1 在整体贡献中的比重，讨论其对约束解码社区的更广泛意义；(3) 考虑增加对"为什么这个组合不是 trivial"的论证。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Figure 3 的 scale-dependent 线性拟合基于 n=4 数据点
- 具体位置：Figure 3, Section 5.1 (lines 229-238)
- 问题：Figure 3 展示 residual DR 与 κ̄ × RV_baseline 的线性关系，R²=0.886，但仅基于 4 个数据点（2 models × 2 datasets）。作者标注 "descriptive only"，但视觉上仍给读者强烈暗示存在稳健的线性关系。4 个点的 R² 几乎没有统计意义（自由度=2），任意 4 个非共线点都能产生较高 R²。
- 建议：(1) 增加更多 model×dataset 配置（如 Mistral-7B，已在 Figure 7 中出现但未纳入 Figure 3）；(2) 或弱化线性拟合的展示，仅保留散点图和定性描述。

**W2** [warning] Cross-field (CF) violations 未解决，讨论不够充分
- 具体位置：Limitations (lines 595-596), Section 4 (lines 386-398)
- 问题：Per-triple enforcement 的根本限制在于无法协调不同 triple 中同一 entity 的类型分配。Limitations 中仅一句带过 ("global type consensus during decoding remains future work")。但 CF violations 在 zero-shot 下占总违规的 ~10%（Figure 4, S1 配置下 CF=0.9），fine-tuning 后从 +9.82pp 降至 +1.18pp（lines 503-504），beam search 可进一步缓解但未完全消除。这个限制值得更充分的讨论，特别是：CF 违规的下游影响是什么？它们是否真的是"可纠正的"（如论文声称的 severity downgrade）？
- 建议：在 Limitations 或 Discussion 中增加一段专门讨论 CF violations 的分析。

**W3** [warning] Entity registry 的 first-seen 语义可能引入系统性偏差
- 具体位置：Section 3.3 (lines 294-301), Appendix C (Table 8)
- 问题：Entity registry 使用 first-seen 语义——entity 在首次出现时被分配类型，后续出现均受此约束。Table 8 显示 58.1% 的 CF violations 来自 "hallucinated entity"（模型生成了输入中不存在的实体名），first-seen lock 会将错误的类型传播到后续 triple。虽然 fine-tuning 消除了 cascade errors (0/22 CF)，但 zero-shot 下这是一个系统性问题。论文在 Appendix C 有详细分析，但主文中对此讨论不足。
- 建议：在 Section 3.3 中增加一句说明 first-seen 语义的潜在风险，引导读者参考 Appendix C 的详细分析。

**W4** [warning] 评估覆盖范围有限
- 具体位置：Section 5, Limitations (lines 597-599)
- 问题：RE 评估仅覆盖 SciERC (7 relations) 和 DocRED (96 relations)，EE 仅 WikiEvents (preliminary, n=20)。缺乏对以下方面的评估：(a) 非英语语言；(b) 更大规模的 schema（如 Wikidata 的数千种 relation types）；(c) 更小的模型（<8B）。虽然 Limitations 中有提及，但对于声称"applicable to any autoregressive LM with logits access"（lines 072-073）的系统，评估范围显得不够。
- 建议：明确讨论 schema 规模对编译时间和运行时开销的影响上限（Appendix K 有 scalability benchmarks 到 1000 relations，可在主文中引用）。

## 小问题（不影响接收）

- Abstract 中 footnote 放置代码链接是非标准做法（通常放在 Introduction 末尾），但不违反 ARR 格式规定。
- 缩写较多（DR, CF, RV, ET, OOV, BPE）——首次使用时已定义，但高密度缩写影响可读性，建议在表格标题中展开关键缩写。
- Section 3.4 "Decoding Strategies" 的 S1/S2 命名不够直观，建议改为更具描述性的名称（如 "joint" / "pipeline"）。
- Figure 5 (per-relation DR violation rates) 的 x 轴标签角度使部分 relation 名称难以辨认。
- Lines 431-432: "this transfer may underestimate DocRED fine-tuning potential" — 这个 caveat 重要但容易被忽略，建议在实验小结中重申。
- κ(r) = 1 − |σ(r)|/|E|² 的定义（line 377-378）中 |E|² 应为 |E × E|（即有序对数目），虽然数值等价但符号上可能引起混淆。

## Questions to Authors

1. **RE 约束的忠实性**：从训练数据提取的类型约束在多大程度上与"真正的"本体约束一致？你们是否尝试过使用 SciERC 或 DocRED 的人工标注指南中隐含的类型约束作为 ground truth 来评估经验性约束的准确率？
2. **First-seen 语义的替代方案**：你们是否考虑过使用 soft 或 probabilistic entity registry（如基于 type distribution 的 weighted masking），以缓解 first-seen lock 导致的错误传播？
3. **CF violations 的下游影响**：你们将 DR→CF 转换描述为 "severity downgrade"，但这假设 CF violations 对下游 KG 影响更小。你们是否有定量的下游任务评估来支持这一说法？
4. **大规模 schema 的瓶颈**：Appendix K 展示了到 1000 relations 的 scalability，但 Wikidata-scale 的 schema（~10K+ relations）下编译和运行时表现如何？entity registry 的查询复杂度是否会成为瓶颈？

## Missing References

Related work 覆盖极为全面（主文 2 页 + 附录 4+ 页），未发现明显遗漏。以下供参考但非必须添加：
- Josifoski et al. (2023) "Language Model Decoding as Direct Metrics Optimization" — 讨论了约束解码与度量优化的关系，与论文的 grammar-first fallback 设计有概念联系。
- Frontiers paper on grammar-constrained decoding for clinical trial abstracts (2024) — 不同领域但方法相关。

## 主要优势

1. **理论基础扎实**：Proposition 1 的 decidability analysis 正式建立了 domain/range 约束超越 CFG 表达能力的理论 gap，为两层设计提供了原则性动机。
2. **实验设计极为全面**：3 个模型族 × 3 个数据集 × 多种配置，消融研究（Table 1 五路消融）、cross-model validation (Section 5.2)、event extraction generalization (Section 5.3)、runtime analysis、beam search analysis、scale-dependent analysis (70B)。
3. **统计方法规范**：Bonferroni 校正、10K 次 bootstrap CI、Cohen's d 效应量、document-level resampling——在 NLP 论文中属于高标准。
4. **非加性层交互的实证发现**（3% + 24% → 94%，Figure 2）是一个有洞察力的结果，展示了两层设计的协同效应而非简单叠加。
5. **附录质量极高**：27 页附录覆盖因果追踪（Table 4）、CF 违规来源分析（Tables 7-8）、per-relation 消融（Table 9-10）、功率分析（Appendix G）、order invariance（Appendix N）、pumping lemma 证明（Appendix O）。
6. **实用部署考量**：三级部署方案（greedy S1 / beam k=2 / beam k=4），runtime overhead 分析，fallback 机制——展现了 deployment 意识。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2681 · 2026-05-25T21:34:26.808401+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,get_visual_check_status,get_external_review_status,read_project_file,submit_review_report_to_research_director,update_review_issues,dispatch_visual_check,request_external_review",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,get_visual_check_status,get_external_review_status,read_project_file,submit_review_report_to_research_director,update_review_issues,dispatch_visual_check,request_external_review",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2682 · 2026-05-25T21:34:26.858997+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2683 · 2026-05-25T21:34:28.766151+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_get_project_overview",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_get_project_overview",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2684 · 2026-05-25T21:34:28.816782+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2685 · 2026-05-25T21:34:31.076469+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2686 · 2026-05-25T21:34:31.680356+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (164 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **r16_70b_lora_scierc_eval** (success): 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale\n- **p1_llama_ee_ft** (killed): —\n- **sf2_70b_prompt_sensitivity** (success): 70B LLaMA-3.1 constrained decoding should show consistent violation reduction across different prompt styles, similar to the 8B result where ΔDR was 94.0-94.6% regardless of prompt variant.\n\n## 趋势\n成功 133 / 负向 15 / 失败 11 / 共 164\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-16980: 无 GPU 信息\nwestd-21461: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_phase0_docred_schema_r2: 已被终止 — unknown\n- w1_cf_fallback_docred: 已被终止 — unknown\n- w1_cf_fallback_llama_scierc: 已被终止 — unknown\n- w1_cf_fallback_llama_docred: 已被终止 — unknown\n- w9_qwen_docred_zs_sampling: 训练失败 — unknown\n- p8b_docred_latency: 训练失败 — unknown\n- p1_ee_ft_composability: 训练失败 — unknown\n- p1_ee_ft_composability_r2: 训练失败 — unknown\n- p1_ee_ft_composability_r3: 训练失败 — unknown\n- p1_ee_ft_composabil
…[truncated 269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 2687 · 2026-05-25T21:34:37.704815+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,get_external_review_status,dispatch_visual_check,request_external_review,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,get_external_review_status,dispatch_visual_check,request_external_review,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2688 · 2026-05-25T21:34:37.705366+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2689 · 2026-05-25T21:34:40.869387+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_post_to_reviewer submit_review_report update_review_issues get_visual_check get_external_review dispatch_visual request_external read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_post_to_reviewer submit_review_report update_review_issues get_visual_check get_external_review dispatch_visual request_external read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2690 · 2026-05-25T21:34:41.020547+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2691 · 2026-05-25T21:34:57.267630+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2692 · 2026-05-25T21:34:57.318256+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2693 · 2026-05-25T21:35:00.144169+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2694 · 2026-05-25T21:35:00.194865+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2695 · 2026-05-25T21:35:05.918847+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2696 · 2026-05-25T21:35:06.421232+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2697 · 2026-05-25T21:35:06.421584+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 2698 · 2026-05-25T21:35:06.873633+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_15.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_16.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_17.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_18.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_reports/round_19.md
/home/
…[truncated 743 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2699 · 2026-05-25T21:35:07.125859+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_round_27/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_round_27/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 2700 · 2026-05-25T21:35:07.226653+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_27/submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2701 · 2026-05-25T21:35:43.376603+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2702 · 2026-05-25T21:35:43.377294+00:00_

1	# Review Issues Tracker — schema_semantic_constrained_ie
2	# Updated: R26 fixes verified by Reviewer, 2026-05-23
3	
4	# ============================================================
5	# Round 26 — Resolved after Reviewer verification
6	# ============================================================
7	
8	- id: "R26-W1"
9	  summary: "DR→CF trade-off 在 Abstract/正文中 framing 不平衡"
10	  category: framing
11	  severity: critical
12	  status: resolved
13	  first_raised_round: 25
14	  last_seen_round: 26
15	  action_items:
16	    - round: 26
17	      action: "Abstract severity-framing + §7 L16 修正 >90%→26-52%"
18	      assigned_to: paper_agent
19	      status: resolved
20	  resolution: "Abstract 改用 severity-framing (irrecoverable→correctable)，§7 L16 修正为 '26-52% under fine-tuned greedy S1; beam k=4 eliminates all'。Reviewer 独立验证 26-52% 与 Table 2 一致。"
21	  resolution_round: 26
22	
23	- id: "R26-W2"
24	  summary: "WikiEvents n=20 不足以支撑 task generalization claim"
25	  category: experiment
26	  severity: warning
27	  status: resolved
28	  first_raised_round: 23
29	  last_seen_round: 26
30	  action_items:
31	    - round: 26
32	      action: "§7 '3 datasets' → '2 RE datasets + preliminary pilot'"
33	      assigned_to: paper_agent
34	      status: resolved
35	  resolution: "§7 修正为 '2 RE datasets (SciERC, DocRED) and 3 model families, with a preliminary event extraction pilot'。Reviewer spot-check 通过。"
36	  resolution_round: 26
37	
38	- id: "R26-W3"
39	  summary: "70B scale-dependent findings 仅基于单一模型族，vocabulary calibration hypothesis 缺因果证据"
40	  category: experiment
41	  severity: warning
42	  status: resolved
43	  first_raised_round: 23
44	  last_seen_round: 26
45	  action_items:
46	    - round: 26
47	      action: "§7 vocabulary calibration hypothesis 标注 speculative"
48	      assigned_to: paper_agent
49	      status: resolved
50	  resolution: "§7 改为 'speculative hypothesis' + 'confirming this causal mechanism requires cross-family verification beyond our current scope'。Reviewer 确认适当弱化
…[truncated 1684 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2703 · 2026-05-25T21:35:47.844973+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml",
  "offset": "100",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2704 · 2026-05-25T21:35:47.895693+00:00_

100	  category: writing
101	  severity: warning
102	  status: resolved
103	  first_raised_round: 26
104	  last_seen_round: 26
105	  action_items:
106	    - round: 26
107	      action: "C1 修正 Mistral ZS only"
108	      assigned_to: paper_agent
109	      status: resolved
110	  resolution: "C1 改为 '3 model families in zero-shot; Qwen3-8B and Llama-3.1-8B additionally under LoRA fine-tuning'。Reviewer 确认。"
111	  resolution_round: 26
112	
113	- id: "R26-W8"
114	  summary: "Proposition 1 新颖性争议——PL theory known-ness"
115	  category: framing
116	  severity: info
117	  status: resolved
118	  first_raised_round: 26
119	  last_seen_round: 26
120	  action_items:
121	    - round: 26
122	      action: "§3 添加 PL theory acknowledge"
123	      assigned_to: paper_agent
124	      status: resolved
125	  resolution: "§3 添加 'While cross-reference binding is known to exceed context-free expressiveness in programming language theory, its implications for IE-specific type constraints... have not been formally characterized.' Reviewer 确认。"
126	  resolution_round: 26
127	
128	- id: "R26-M1"
129	  summary: "Abstract F1 范围 '40-46%' 验证"
130	  category: writing
131	  severity: info
132	  status: resolved
133	  first_raised_round: 25
134	  last_seen_round: 26
135	  resolution: "Table 2 R-F1 范围 40.56-45.47，'40-46%' 准确。"
136	  resolution_round: 26
137	
138	- id: "R26-M2"
139	  summary: "CF increase 缺少统计检验"
140	  category: experiment
141	  severity: info
142	  status: open
143	  first_raised_round: 26
144	  last_seen_round: 26
145	  action_items:
146	    - round: 26
147	      action: "低优先级，DDL 后可补"
148	      assigned_to: main_agent
149	      status: open
150	  resolution: ""
151	  resolution_round: null
152	
153	- id: "R26-M3"
154	  summary: "LoRA 超参迁移 caveat"
155	  category: experiment
156	  severity: info
157	  status: resolved
158	  first_raised_round: 24
159	  last_seen_round: 26
160	  resolution: "§5 Setup 已含完整 caveat。"
161	  resolution_round: 26
162	
163	- id: "R26-M4"
164	  summary: "正文视觉密度不足"
1
…[truncated 920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 2705 · 2026-05-25T21:36:40.351134+00:00_

**Reviewer 2 初审已收到** — Overall 3.5 (Borderline Conference)

关键发现摘要：
- **N1 [critical]**：Title/Abstract 中 "Ontology-Compiled" 的 framing 与 RE 实验中从训练数据提取约束的实际做法不一致
- **N2 [critical]**：核心组件（XGrammar + 查找表 + logit masking）个体新颖性有限，贡献更多在系统集成和实证分析
- **W1-W4 [warning]**：Figure 3 线性拟合 n=4 不足、CF violations 讨论不充分、first-seen 语义偏差、评估覆盖有限

等待 Reviewer 1 初审完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 202

## Round 202

10 recorded events


### User

_source line 2706 · 2026-05-25T21:36:42.946841+00:00_

[Reviewer 2 审稿结果]:
Let me fetch the official review form details and read the paper pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2707 · 2026-05-25T21:37:09.577201+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2708 · 2026-05-25T21:37:10.280367+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (164 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **r16_70b_lora_scierc_eval** (success): 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale\n- **p1_llama_ee_ft** (killed): —\n- **sf2_70b_prompt_sensitivity** (success): 70B LLaMA-3.1 constrained decoding should show consistent violation reduction across different prompt styles, similar to the 8B result where ΔDR was 94.0-94.6% regardless of prompt variant.\n\n## 趋势\n成功 133 / 负向 15 / 失败 11 / 共 164\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-16980: 无 GPU 信息\nwestd-21461: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_phase0_docred_schema_r2: 已被终止 — unknown\n- w1_cf_fallback_docred: 已被终止 — unknown\n- w1_cf_fallback_llama_scierc: 已被终止 — unknown\n- w1_cf_fallback_llama_docred: 已被终止 — unknown\n- w9_qwen_docred_zs_sampling: 训练失败 — unknown\n- p8b_docred_latency: 训练失败 — unknown\n- p1_ee_ft_composability: 训练失败 — unknown\n- p1_ee_ft_composability_r2: 训练失败 — unknown\n- p1_ee_ft_composability_r3: 训练失败 — unknown\n- p1_ee_ft_composabil
…[truncated 269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 2709 · 2026-05-25T21:37:10.280784+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2710 · 2026-05-25T21:37:10.532155+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2711 · 2026-05-25T21:37:10.532570+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2712 · 2026-05-25T21:37:10.984744+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:16:38.989379+00:00\", \"completed_at\": \"2026-05-25T21:20:29.968146+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页纯文本无任何 display item，首个视觉锚点（Figure 1）到 page 3 才出现。对于实证贡献为主的论文，在 page 1 或 2 加入 teaser figure 或核心结果 preview 可强化审稿人第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 5 的 x 轴 relation type 标签旋转后字号偏小（约为正文 60-70%），建议适当增大或使用缩写\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 和 Figure 3 使用红色和蓝/绿色组合，大部分情况可区分，但红绿搭配对 deuteranopia 色盲可能有风险；建议改用 blue+orange 双色方案\"}, {\"severity\": \"info\", \"dimension\": \"page 12-16\", \"message\": \"Appendix B（Extended Related Work）+ C（Extended Discussion）连续 5 页纯文本，虽为 appendix 可接受，但密度极高\"}, {\"severity\": \"info\", \"dimension\": \"page 39\", \"message\": \"末页内容约占 80%，Section T (Use of AI Assistants) 列表较简短，整体可接受\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2713 · 2026-05-25T21:37:10.985310+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2714 · 2026-05-25T21:37:11.036058+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml\", \"content\": \"_next_id: 88\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 主目标调整为 EMNLP 2026 ARR (5/25), AAAI 2027 为后备\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、不要保守、资源会给够。12 天 AI 团队速度足够：Phase 0 (1-2天) →\\n    Phase 1 compiler (2-3天) → Phase 2 experiments (2-3天) → Paper (2-3天)。禁止 fallback\\n    思维，冲最高目标。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 19:14 UTC\\n  summary: SciERC Phase 0 结果确认 GO — domain_range violation rate 15.4%，3× 超阈值\\n  rationale: 'SciERC 全量 test set (551 sentences, 1724 triples): domain_range_violation_rate\\n    = 15.4%，远超 5% go/no-go 阈值。违规分布极不均匀 (Feature-of 33.5%, Compare 42.4% vs Used-for\\n    0.76%)，支持\\\"特定 relation types 需要 decoding-time enforcement\\\"的论文 claim。DocRED dry-run\\n    (37 docs) 同样显示 14.4%。两个数据集均为 GO 信号，MVP 核心假设得到强验证。等 schema-informed prompt 结果确认\\n    prompt 级干预不足以解决问题后正式宣布 MVP 通过。'\\n  related_experiments:\\n  - exp_id: mvp_phase0_violation_rate\\n    role: primary\\n    result: domain_range_violation_rate=15.4%, go_nogo=GO\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 21:48 UTC\\n  summary: MVP 通过，进入 Research 阶段，立即启动 Phase 2 constrained decoding 实验\\n  rationale: Phase 0 三个实验完成：SciERC 15.4%/5.78%, DocRED 18.7% domain_range violation\\n    rate。两个数据集均远超 5% 阈值，核心假设得到强验证。Phase 1 compiler 代码就绪（36 tests 通过），Phase 2 脚本就绪（S1\\n    路径可用，S2 bug 修复中）。cuda:1 空闲，立即启动 Phase 2 SciERC grammar_only/semantic_only/full_s1\\n    实验。\\n  related_experiments:\\n  - exp_id: mvp_phase0_violation_rate\\n    role: primary\\n    result: SciERC DR=15.4%, GO\\n  - exp_id: mvp_phase0_scierc_schema\\n    role: primary\\n    result: SciERC DR=5.78%, prompt insufficient\\n  - exp_id: mvp_phase0_violation_rate_docred\\n    role: primary\\n    result: DocRED DR=18.7%, GO\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-
…[truncated 1469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 2715 · 2026-05-25T21:39:16.685374+00:00_

服务器重启，恢复上下文。我没有 `feishu_read_chat_history` 和 `get_project_status` 工具，用已有工具恢复状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 203

## Round 203

6 recorded events


### User

_source line 2716 · 2026-05-25T21:49:40.130603+00:00_

[Reviewer 1 审稿意见]:

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 形式化分析扎实、实验极其充分的工程贡献，但新颖性偏中等，事件抽取验证不足以支撑"结构化 IE"的广泛声称。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | Proposition 1 的 pumping lemma 证明正确，五路消融实验设计严谨，统计方法（Bonferroni 校正 bootstrap CI、Cohen's d）规范。主要扣分：WikiEvents 验证不充分（零样本 n=246，微调 n=20）。 |
| Excitement | 3/5 | 问题重要（生成式 IE 的 schema 合规性），解决方案有原则性，但核心技术是组合已有组件（XGrammar + logit masking），非算法创新。Non-additive interaction 发现有趣但解释直接（grammar 是 semantic 的前置条件）。 |
| Reproducibility | 5/5 | 匿名代码/数据链接已提供；Appendix G 详列所有超参数、硬件/软件版本；Table 29 验证跨种子确定性；200-doc DocRED 子集通过 bootstrap 功效分析验证。 |
| Reviewer Confidence | 4/5 | 对约束解码和结构化 IE 领域较为熟悉，仔细检查了形式化证明和实验设计。 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] WikiEvents 证据不足以支撑"结构化 IE 泛化"声称
- 具体位置：§5.3（lines 522–529）、Limitations（line 598）、Table 47（page 38）、标题
- 问题：论文标题为"Type-Constrained Information Extraction"，摘要和引言将事件抽取（EE）列为三个验证轴之一（line 075–076："event extraction (§5.3)"）。然而 WikiEvents 实验仅有零样本 n=246 文档、微调 composability 仅 n=20 文档。Limitations 节自己承认"fine-tuning composability is preliminary (n=20)"（line 598）。在 unconstrained 基线 EV+RoV 违规已超 85% 的条件下（Table 47），约束执行的有效性几乎是 trivially observable，真正的难点——是否影响 F1——在 n=20 条件下无法可靠回答。
- 为什么影响接收：论文的 scope claim（"Structured IE"）依赖于 EE 泛化，但证据质量远低于 RE 部分。如果 EE 仅为附加验证，标题和引言的 framing 过强；如果 EE 是核心贡献之一，实验规模不足。
- 建议修改方向：(a) 将标题和 framing 限定为 Relation Extraction + 初步 EE 验证；或 (b) 扩大 WikiEvents 评估规模（至少 100+ 文档的微调实验），并在 §5.3 补充完整的 F1 confidence interval 分析。

**N2** [critical] 缺乏与任何现有语义约束 IE 系统的直接对比
- 具体位置：§5（Experiments）、Table 16（Appendix，page 25）、Appendix S（page 39）
- 问题：论文仅与 grammar-only baselines（GCD/BoostCD/vLLM guided_json，Table 16–17）和自身消融进行对比。没有与任何试图执行语义约束的系统进行 head-to-head 评估——如 EnriCo（ASP 约束推理）、SPIRES/OntoGPT（post-hoc ontology validation）、或至少与 schema-informed prompting baseline（Table 13）在完全相同设置下的系统性对比。Appendix S 以"methodologically constrained by incompatible evaluation settings"为由回避了直接对比，这对 training-based 系统（GoLLIE/KnowCoder）可以接受，但对 post-hoc validation 系统（SPIRES, ODKE+）不应成立——它们可以在完全相同的 unconstrained 输出上运行。
- 为什么影响接收：没有 head-to-head 对比，读者无法判断 OntoCoDec 相对于 existing alternatives 的增量价值。Table 12 的 post-hoc filtering vs. constrained decoding 对比是重要一步，但 post-hoc filtering 的实现是最简单的"删除违规 triple"，不代表 post-hoc 方法的最优表现。
- 建议修改方向：至少与一个 post-hoc ontology validation 系统（如 SPIRES 的 validate-then-correct 流程）在相同模型/数据集/prompt 条件下进行对比；或在 SciERC 上复现 EnriCo 的约束推理流程作为 baseline。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Figure 3 的双因子回归统计功效不足，在正文中位置过于突出
- 具体位置：Figure 3（page 5）、§4（lines 377–385）
- 问题：线性拟合 R²=0.886 基于仅 n=4 数据点，p=0.058（不显著于 α=0.05）。论文承认这是"descriptive rather than a confirmatory statistical test"（line 1566–1568），但 Figure 3 位于正文第 5 页且 §4 "Constraint Tightness" 给予其相当篇幅，可能给读者留下比实际更强的证据印象。
- 建议：在 Figure 3 caption 中明确标注 n=4 和 p>0.05；或将其移至附录，在正文中用文字简述描述性趋势。

**W2** [warning] 70B 验证仅覆盖单一模型（Llama-3.1-70B-Instruct AWQ INT4）
- 具体位置：§5.3（lines 553–560）、Tables 18–20（page 25）
- 问题：Scale-dependent interaction 是论文的核心发现之一（Contribution 3），但 70B 验证仅限 Llama-3.1-70B 一个模型。缺少第二个 70B 级别模型（如 Qwen-72B）的验证，削弱了"scale-dependent"结论的 generalizability。AWQ INT4 量化引入了额外混淆因素（虽然 Appendix R 验证了量化鲁棒性，但在非量化 70B 上的结果会更有说服力）。
- 建议：补充至少一个非量化或不同家族的 70B 模型的消融结果（至少 SciERC 零样本）。

**W3** [warning] 约束表来源于训练数据而非形式化 ontology，residual violations 的 33% 归因于 schema coverage gaps
- 具体位置：Limitations（lines 600–603）、Appendix C（lines 1762–1766）
- 问题：Type constraints 从训练集共现统计中提取（99%+ coverage），而非从形式化 ontology 规范编译。这意味着罕见但有效的 type pair 可能缺失，导致 false positive violation detection。Appendix C 的 residual error analysis 显示 33% 的 residual DR 来自 schema coverage gaps（line 1762）。对于声称"automatically compile from IE ontologies"（line 071–072）的系统，这个 gap 值得在正文更明确讨论。
- 建议：在 §3.1 或 §5 中明确区分"complete formal ontology → compiled constraints"和"empirically derived constraint table → compiled constraints"两条路径的保证差异。

**W4** [warning] S2（two-pass）策略在 70B 上造成严重 R-F1 退化但分析不足
- 具体位置：Table 18（page 25，70B SciERC: S2 R-F1 = 36.28 vs. S1 R-F1 = 44.53，降 8.25 pp）
- 问题：S2 在 70B 上的 R-F1 退化（−8.25 pp）远大于 8B 上的差异，但正文（§3.4，lines 341–345）仅用一句话说"S1 achieves higher R-F1 at comparable DR"即略过。Table 18 在附录中提供了数据，但缺乏对 70B S2 失败原因的分析——是 over-constraining 导致 generation degradation，还是 two-pass 的 entity extraction 质量在 70B 上反而下降？
- 建议：在 Appendix 中补充 70B S2 失败的 error analysis（至少定性分析几个 case）。

## 小问题（不影响接收）

- **Footnote 1 匿名链接**: `anonymous.4open.science` 链接符合 double-blind 要求，无匿名性问题。
- **Abstract 长度**: 估计约 170–180 词，在 200 词限制内，合规。
- **正文页数**: 主体文本（含 Limitations）恰好 8 页，References 从第 8 页底部开始，符合格式要求。
- **Limitations section**: 位于正文第 8 页（lines 594–603），非附录，且仅有一个 Limitations section，合规。
- **Table 1 caption 中的 "†" 注释**（"†vLLM guided_json (Kwon et al., 2023)"）: 注释说明在 caption 中而非表格 footnote 中，排版可优化。
- **Figure 2 (page 5)**: "Additive prediction (27%)" 标注的虚线在图中不够清晰，建议加深对比度。
- **Appendix T (page 39)**: AI 辅助声明完整且合规。

## 主要优势

1. **形式化分析扎实**: Proposition 1（Appendix O）通过 pumping lemma 严谨证明 domain/range 约束超出 context-free 表达能力，为两层架构提供原则性动机。证明结构正确，position-based 和 name-based referencing 两种情况均有覆盖。

2. **实验深度罕见**: 39 页、49 个表格、8 张图。五路消融（Table 1）、跨模型验证（Table 48）、微调 composability（Table 2）、beam search 分析（Appendix F）、fallback causal tracing（Table 4）、CF-DR trade-off 分析（Table 5）、prompt sensitivity（Table 34）、document length 分析（Tables 31–33）、量化鲁棒性（Appendix R）、nucleus sampling 鲁棒性（Appendix E）、order invariance（Appendix N）、lucky violation 分析（Table 39）、ontology scalability（Table 40）——覆盖了几乎所有可能的 reviewer 疑问。

3. **统计方法规范**: Bonferroni 校正 bootstrap CIs（10,000 iterations，document-level resampling）、Cohen's d 效应量、跨种子确定性验证（Table 29）、200-doc 子集功效分析。这在 NLP 论文中显著高于平均水平。

4. **诚实的 limitation 分析**: CF-DR trade-off（Table 5）、residual error breakdown（Appendix J.5）、fallback mechanism 的详细量化（Table 4）、lucky violation 分析（Table 39）均展示了系统的真实边界而非只报告最佳结果。Grammar-first fallback 的设计选择以及由此产生的 CF 问题被透明讨论。

5. **实用性**: 无需 constraint-specific training，可组合任何有 logits 接口的 autoregressive LM，与 GoLLIE 等 training-based 系统正交互补（Appendix S）。编译开销线性可控（Table 40：0.32–0.42 s，运行时 overhead 2–3%）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2717 · 2026-05-25T21:50:34.033163+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整初审。请对每个 Must-Fix 和 Should-Fix 逐条回应 `[AGREE]` 或 `[REBUT]`，并简述理由。如有 Reviewer 2 遗漏但你认为重要的点，也请指出。\n\n---\n\n## Reviewer 2 初审（Overall: 3.5, Borderline Conference）\n\n**维度打分**: Soundness 4/5, Excitement 2.5/5, Reproducibility 5/5\n\n### Must-Fix\n\n**R2-N1** [critical] \"Ontology-Compiled\" 定位与实际实现不一致\n- Title/Abstract 暗示约束从正式本体编译，但 RE 实验的类型约束实际从训练数据提取（§5 lines 419-423）。只有 WikiEvents EE 使用了真正的 KAIROS ontology。核心叙事\"将 IE 本体编译为 token-level masks\"在两个主要数据集上不成立。\n- 建议：修改 title/abstract 更准确反映约束来源，如 \"schema-derived\" 或 \"type-aware\"。\n\n**R2-N2** [critical] 核心新颖性有限——各组件均为已有技术的直接应用\n- Grammar layer = XGrammar 直接应用；Semantic layer = constrained beam search + type-based filtering 的自然延伸；两层组合（bitwise AND）为标准做法。Proposition 1 的 pumping lemma 在 PL theory 中是标准技术。\n- 建议：定位为\"系统贡献 + 实证发现\"而非方法论创新。\n\n### Should-Fix\n\n**R2-W1** [warning] Figure 3 线性拟合 n=4 数据点，R²=0.886 几乎无统计意义\n- 建议增加更多 model×dataset 配置或弱化展示。\n\n**R2-W2** [warning] Cross-field (CF) violations 讨论不充分\n- CF 在 zero-shot 下占总违规 ~10%，fine-tuning 后降至 +1.18pp。Limitations 仅一句带过。建议增加专门分析段落。\n\n**R2-W3** [warning] Entity registry first-seen 语义可能引入系统性偏差\n- 58.1% CF violations 来自 hallucinated entity，first-seen lock 传播错误类型。主文讨论不足。\n\n**R2-W4** [warning] 评估覆盖范围有限\n- 缺乏非英语、大规模 schema (>1000 relations)、小模型 (<8B) 评估。\n\n### Questions to Authors\n1. RE 约束从训练数据提取 vs 真正本体约束的一致性？\n2. 是否考虑 soft/probabilistic entity registry？\n3. CF violations 的下游影响是否有定量评估？\n4. Wikidata-scale schema (~10K+ relations) 表现？\n\n---\n\n请逐条 [AGREE] / [REBUT]。",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整初审。请对每个 Must-Fix 和 Should-Fix 逐条回应 `[AGREE]` 或 `[REBUT]`，并简述理由。如有 Reviewer 2 遗漏但你认为重要的点，也请指出。\n\n---\n\n## Reviewer 2 初审（Overall: 3.5, Borderline Conference）\n\n**维度打分**: Soundness 4/5, Excitement 2.5/5, Reproducibility 5/5\n\n### Must-Fix\n\n**R2-N1** [critical] \"Ontology-Compiled\" 定位与实际实现不一致\n- Title/Abstract 暗示约束从正式本体编译，但 RE 实验的类型约束实际从训练数据提取（§5 lines 419-423）。只有 WikiEvents EE 使用了真正的 KAIROS ontology。核心叙事\"将 IE 本体编译为 token-level masks\"在两个主要数据集上不成立。\n- 建议：修改 title/abstract 更准确反映约束来源，如 \"schema-derived\" 或 \"type-aware\"。\n\n**R2-N2** [critical] 核心新颖性有限——各组件均为已有技术的直接应用\n- Grammar layer = XGrammar 直接应用；Semantic layer = constrained beam search + type-based filtering 的自然延伸；两层组合（bitwise AND）为标准做法。Proposition 1 的 pumping lemma 在 PL theory 中是标准技术。\n- 建议：定位为\"系统贡献 + 实证发现\"而非方法论创新。\n\n### Should-Fix\n\n**R2-W1** [warning] Figure 3 线性拟合 n=4 数据点，R²=0.886 几乎无统计意义\n- 建议增加更多 model×dataset 配置或弱化展示。\n\n**R2-W2** [warning] Cross-field (CF) violations 讨论不充分\n- CF 在 zero-shot 下占总违规 ~10%，fine-tuning 后降至 +1.18pp。Limitations 仅一句带过。建议增加专门分析段落。\n\n**R2-W3** [warning] Entity registry first-seen 语义可能引入系统性偏差\n- 58.1% CF violations 来自 hallucinated entity，first-seen lock 传播错误类型。主文讨论不足。\n\n**R2-W4** [warning] 评估覆盖范围有限\n- 缺乏非英语、大规模 schema (>1000 relations)、小模型 (<8B) 评估。\n\n### Questions to Authors\n1. RE 约束从训练数据提取 vs 真正本体约束的一致性？\n2. 是否考虑 soft/probabilistic entity registry？\n3. CF violations 的下游影响是否有定量评估？\n4. Wikidata-scale schema (~10K+ relations) 表现？\n\n---\n\n请逐条 [AGREE] / [REBUT]。",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2718 · 2026-05-25T21:50:53.933292+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19900
}
```

</details>

---


### Tool call

_source line 2719 · 2026-05-25T21:50:54.134918+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整初审。请对每个 Must-Fix 和 Should-Fix 逐条回应 `[AGREE]` 或 `[REBUT]`，并简述理由。如有 Reviewer 1 遗漏但你认为重要的点，也请指出。\n\n---\n\n## Reviewer 1 初审（Overall: 3.5, Borderline Conference）\n\n**维度打分**: Soundness 4/5, Excitement 3/5, Reproducibility 5/5\n\n### Must-Fix\n\n**R1-N1** [critical] WikiEvents 证据不足以支撑\"结构化 IE 泛化\"声称\n- 标题为\"Information Extraction\"，摘要将 EE 列为三个验证轴之一。但 WikiEvents 零样本 n=246、微调 n=20。在 unconstrained 基线 EV+RoV 违规已超 85% 的条件下，约束有效性 trivially observable，真正的 F1 影响在 n=20 下无法可靠回答。\n- 建议：将 framing 限定为 RE + 初步 EE 验证；或扩大 WikiEvents 规模（100+ 文档微调）。\n\n**R1-N2** [critical] 缺乏与现有语义约束 IE 系统的直接对比\n- 仅与 grammar-only baselines 和自身消融对比。缺少与 EnriCo（ASP 约束）、SPIRES/OntoGPT（post-hoc validation）的 head-to-head 评估。Appendix S 以 \"incompatible evaluation settings\" 回避直接对比，对 post-hoc validation 系统不成立——它们可在完全相同的 unconstrained 输出上运行。\n- 建议：至少与一个 post-hoc ontology validation 系统在相同条件下对比。\n\n### Should-Fix\n\n**R1-W1** [warning] Figure 3 n=4 + p=0.058 不显著，在正文中位置过于突出\n- 建议在 caption 标注 n=4 和 p>0.05，或移至附录。\n\n**R1-W2** [warning] 70B 验证仅 Llama-3.1-70B AWQ INT4 一个模型\n- Scale-dependent 是核心发现之一，但 70B 仅一个模型+量化。缺少 Qwen-72B 或非量化模型验证。\n\n**R1-W3** [warning] 约束表源于训练数据，33% residual DR 来自 schema coverage gaps\n- 声称\"compile from IE ontologies\"但实际从训练集共现统计提取。需在正文明确区分两条路径。\n\n**R1-W4** [warning] S2 在 70B 上 R-F1 退化 8.25pp 但分析不足\n- S2 70B 失败原因未分析——over-constraining 还是 entity extraction 质量下降？\n\n### 主要优势\n1. 形式化分析扎实（Proposition 1 pumping lemma 证明正确）\n2. 实验深度罕见（39 页、49 表、8 图）\n3. 统计方法规范（Bonferroni bootstrap CIs、Cohen's d）\n4. 诚实的 limitation 分析（CF-DR trade-off、residual error breakdown）\n5. 实用性（无需约束特定训练、可组合任何 LM）\n\n---\n\n请逐条 [AGREE] / [REBUT]。",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整初审。请对每个 Must-Fix 和 Should-Fix 逐条回应 `[AGREE]` 或 `[REBUT]`，并简述理由。如有 Reviewer 1 遗漏但你认为重要的点，也请指出。\n\n---\n\n## Reviewer 1 初审（Overall: 3.5, Borderline Conference）\n\n**维度打分**: Soundness 4/5, Excitement 3/5, Reproducibility 5/5\n\n### Must-Fix\n\n**R1-N1** [critical] WikiEvents 证据不足以支撑\"结构化 IE 泛化\"声称\n- 标题为\"Information Extraction\"，摘要将 EE 列为三个验证轴之一。但 WikiEvents 零样本 n=246、微调 n=20。在 unconstrained 基线 EV+RoV 违规已超 85% 的条件下，约束有效性 trivially observable，真正的 F1 影响在 n=20 下无法可靠回答。\n- 建议：将 framing 限定为 RE + 初步 EE 验证；或扩大 WikiEvents 规模（100+ 文档微调）。\n\n**R1-N2** [critical] 缺乏与现有语义约束 IE 系统的直接对比\n- 仅与 grammar-only baselines 和自身消融对比。缺少与 EnriCo（ASP 约束）、SPIRES/OntoGPT（post-hoc validation）的 head-to-head 评估。Appendix S 以 \"incompatible evaluation settings\" 回避直接对比，对 post-hoc validation 系统不成立——它们可在完全相同的 unconstrained 输出上运行。\n- 建议：至少与一个 post-hoc ontology validation 系统在相同条件下对比。\n\n### Should-Fix\n\n**R1-W1** [warning] Figure 3 n=4 + p=0.058 不显著，在正文中位置过于突出\n- 建议在 caption 标注 n=4 和 p>0.05，或移至附录。\n\n**R1-W2** [warning] 70B 验证仅 Llama-3.1-70B AWQ INT4 一个模型\n- Scale-dependent 是核心发现之一，但 70B 仅一个模型+量化。缺少 Qwen-72B 或非量化模型验证。\n\n**R1-W3** [warning] 约束表源于训练数据，33% residual DR 来自 schema coverage gaps\n- 声称\"compile from IE ontologies\"但实际从训练集共现统计提取。需在正文明确区分两条路径。\n\n**R1-W4** [warning] S2 在 70B 上 R-F1 退化 8.25pp 但分析不足\n- S2 70B 失败原因未分析——over-constraining 还是 entity extraction 质量下降？\n\n### 主要优势\n1. 形式化分析扎实（Proposition 1 pumping lemma 证明正确）\n2. 实验深度罕见（39 页、49 表、8 图）\n3. 统计方法规范（Bonferroni bootstrap CIs、Cohen's d）\n4. 诚实的 limitation 分析（CF-DR trade-off、residual error breakdown）\n5. 实用性（无需约束特定训练、可组合任何 LM）\n\n---\n\n请逐条 [AGREE] / [REBUT]。",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2720 · 2026-05-25T21:50:55.442532+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1307
}
```

</details>

---


### Assistant

_source line 2721 · 2026-05-25T21:50:59.854918+00:00_

交叉分享已派发。两位 Reviewer 正在审阅对方的审稿意见并准备 [AGREE]/[REBUT] 回应。

等待交叉回应返回后进行收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 204

## Round 204

2 recorded events


### User

_source line 2722 · 2026-05-25T21:51:02.376175+00:00_

[Reviewer 1 审稿结果]:
Round 27 初审完成。

**评分**: Overall 3.5（Borderline Conference）

**核心判断**: 论文的两层约束解码框架有扎实的形式化动机（Proposition 1 证明正确），实验深度在 NLP 论文中罕见（39 页、49 个表格），统计方法规范。但新颖性偏工程导向（组合 XGrammar + logit masking），且两个关键缺陷影响评分：(1) WikiEvents 事件抽取验证过于初步（n=20 微调），不足以支撑标题中"Structured IE"的广泛声称；(2) 缺乏与任何现有语义约束 IE 系统的直接对比实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2723 · 2026-05-25T21:51:13.565071+00:00_

这是 Reviewer 1 的初审摘要，与之前收到的完整初审一致。交叉分享任务已派发给两位 Reviewer，等待他们的 `[AGREE]/[REBUT]` 交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 205

## Round 205

2 recorded events


### User

_source line 2724 · 2026-05-25T21:52:35.229438+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 交叉回应 Reviewer 2

### Must-Fix 回应

**[REBUT] R2-N1: "Ontology-Compiled" 定位与实际实现不一致**

R2 的观察部分正确但结论过重。需区分两个层面：

(1) 编译管线本身是 ontology-to-mask 的：§3 的编译流程（schema → CFG + type constraint table → token-level masks）确实从 ontology 结构编译。管线的输入可以是形式化 ontology（如 KAIROS）或训练数据提取的 co-occurrence table。

(2) R2 的真正关切是约束来源的完整性。RE 数据集约束从训练数据统计提取（99%+ coverage），而非形式化 ontology。Appendix K（Table 40）已验证编译管线可扩展至 200 types / 1000 relations 的合成 ontology。

(3) 关键反驳：标题的 "Compiled Schema Constraints" 描述的是编译方法（schema → compiled masks），而非约束来源。GCD（Geng et al., 2023）也从 JSON schema 编译 grammar constraints，JSON schema 同样可以手写或自动生成。

(4) 但同意：正文应在 §5 更明确标注 SciERC/DocRED 的约束来源是 "empirically derived constraint table"，并讨论 coverage gap（33% residual DR，与我的 W3 一致）。

**总结**：R2-N1 是 legitimate 的 framing 问题，但不构成 critical。降级为 Should-Fix。

---

**[AGREE with nuance] R2-N2: 核心新颖性有限**

R2 对各组件的 characterization 基本准确，但低估了：

(1) 组合的非加性交互（3% + 24% → 94%）是非平凡实证发现，Table 1 五路消融 + Table 4 fallback causal tracing + scale-dependent analysis 共同揭示了 grammar 层作为 semantic 层 "enabling prerequisite" 的机制。

(2) Proposition 1 价值不在技术难度而在结论意义——此前未有 IE type constraint 非 context-free 的形式化证明。

(3) 从 code domain 到 IE domain 的迁移不是 trivial 的——IE 的 flat domain/range sets + dynamic entity registry 与 PL 的 deep subtyping 根本不同。

**总结**：同意主要贡献是系统+实证而非算法创新。但不妨碍 Borderline Conference 水平——ACL venues 接收高质量系统贡献。

---

### Should-Fix 回应

**[AGREE] R2-W1**: 与我的 W1 完全一致。n=4, p=0.058 无统计意义。

**[REBUT] R2-W2**: R2 声称 "Limitations 仅一句带过"，但 CF 分析分布在主文 §5.1（lines 467–489）、§5.3（lines 538–552）、Appendix C（~4 页，Tables 4/5/7/8）、Appendix M（TCR 分析），总计超 5 页含 5 个专门 table。R2 可能忽略了附录中的详尽分析。建议主文增加 forward pointer。

**[AGREE with nuance] R2-W3**: 观察准确（Table 8: 58.1% CF 来自 hallucinated entity），但 Appendix C 已有充分分析，且 fine-tuning 后 cascade errors 完全消除（0/22）。同意主文 §3.3 应增加 1–2 句 failure mode 讨论。

**[AGREE] R2-W4**: 同意缺乏非英语和超大规模 schema 评估。但 Table 40 的 scalability 验证和非英语数据集稀缺性应纳入考量。

---

### R2 遗漏的重要问题

**R2 未提及 WikiEvents 证据不足**。这是我的 N1：零样本 n=246、微调 n=20 的 EE 验证不足以支撑 "Structured IE" 的广泛声称。R2-N1（framing）和我的 N1（evidence）指向同一方向但从不同角度。两者应同时修复。

**R2 的 Excitement 2.5/5 偏低**。虽同意新颖性偏工程导向，但 49 个 table 的实验深度、non-additive interaction 的定量刻画、编译管线的实用性（无需 constraint-specific training）具有独立价值。我给 3/5 更合理。

---

### 综合评分维持

维持 Overall 3.5（Borderline Conference）。与 R2 的主要分歧在于：(1) R2-N1 应为 Should-Fix 而非 Must-Fix；(2) CF 分析并非不充分（R2-W2）。与 R2 的一致点在于：新颖性定位和 Figure 3 统计功效问题。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2725 · 2026-05-25T21:52:58.995152+00:00_

Reviewer 1 交叉回应已收到。

**交叉分享进度：**
| Reviewer | 初审 | 交叉回应 |
|----------|------|----------|
| Reviewer 1 | ✅ 3.5 | ✅ 已完成 |
| Reviewer 2 | ✅ 3.5 | 🔄 等待中 |

**Reviewer 1 交叉回应要点：**
- R2-N1（Ontology framing）：**REBUT** → 建议降级为 Should-Fix，"compiled" 描述编译方法而非约束来源
- R2-N2（新颖性）：**AGREE with nuance** → 同意系统贡献定位，但强调非加性交互和 Proposition 1 的独立价值
- R2-W1（Figure 3）：**AGREE**
- R2-W2（CF 讨论）：**REBUT** → 指出附录已有 5+ 页分析，R2 可能遗漏
- R2-W3（First-seen）：**AGREE with nuance**
- R2-W4（评估覆盖）：**AGREE**
- 补充：R2 遗漏了 WikiEvents n=20 泛化不足问题

等待 Reviewer 2 交叉回应后进入报告合成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 206

## Round 206

2 recorded events


### User

_source line 2726 · 2026-05-25T21:53:01.565085+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心分歧：R2-N1（"Ontology-Compiled" naming）我认为应降级为 Should-Fix；R2-W2（CF 讨论不充分）我认为不成立——附录有超 5 页详细分析。与 R2 一致的点：新颖性偏工程导向（R2-N2）、Figure 3 统计功效不足（R2-W1）。额外指出 R2 遗漏了 WikiEvents 证据不足的问题。维持 Overall 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2727 · 2026-05-25T21:53:10.787447+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

当前进度：
| 角色 | 初审 | 交叉回应 |
|------|------|----------|
| Reviewer 1 | ✅ 3.5 | ✅ 已完成 |
| Reviewer 2 | ✅ 3.5 | 🔄 等待中 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 207

## Round 207

10 recorded events


### User

_source line 2728 · 2026-05-25T21:57:19.948049+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1 初审

### Must-Fix 回应

**[AGREE with nuance] R1-N1: WikiEvents 证据不足以支撑"结构化 IE 泛化"声称**

同意核心判断，但认为 R1 略微高估了严重性。论文正文 §5.3 标题为 "Event Extraction Validation"，Appendix P 开头明确称其为 "pilot"。Table 47（p38）显示零样本 n=246、微调 n=20，unconstrained EV+RoV 违规率极高（EV 34%、RoV 74.9%），使得 S1 消除效果 trivially observable——R1 判断准确。微调 n=20 下 R-F1 统计效力不足。

但更根本的问题不在 WikiEvents 规模，而在**标题**。"Type-Constrained Information Extraction" 暗示对 IE 的泛化覆盖，但 primary evidence 仅覆盖 RE（SciERC + DocRED），EE 仅是 preliminary pilot。R1 建议"限定 framing 为 RE + 初步 EE 验证"合理，但最关键修改点是**标题和 abstract 措辞**——应明确以 RE 为主、EE 为探索性验证，而非并列为"三个验证轴之一"。

**严重性评估**：同意影响接收决定，但更偏向 should-fix。论文内部 hedging 到位（§5.3 标题、Limitations），修改标题和 abstract 措辞即可解决，无需扩大 WikiEvents 规模。

---

**[AGREE with downgrade] R1-N2: 缺乏与现有语义约束 IE 系统的直接对比**

同意是真实缺陷，但不同意 critical 定级，建议降为 **should-fix**。

R1 指出缺少与 EnriCo（ASP 约束）、SPIRES/OntoGPT（post-hoc validation）的 head-to-head。Appendix S（p39）仅以 "orthogonal approaches" 概述 GoLLIE vs. OntoCoDec，未做数值比较。R1 论证 post-hoc validation 可直接在相同 unconstrained 输出上运行——逻辑成立。

降级理由：
1. 论文核心贡献是 **decoding-time 约束机制**的形式化和实现，非声称优于所有已有方法。Table 16（p25）已与 GCD/BoostedCD 做分析等价性论证。
2. SPIRES/OntoGPT 工作在生物医学领域（OBO ontologies），与 SciERC/DocRED 的 schema 不直接兼容——需重新实现 ontology lookup 模块，非 trivial 工程。
3. EnriCo 使用 ASP solver，约束表达能力与 CFG+semantic layer 形式化层面不同，需仔细设计 fair evaluation protocol。

**建议**：在 Appendix S 增加定性对比表（约束类型、运行时开销、是否需重训练），明确 post-hoc vs. decoding-time 的 trade-off。

---

### Should-Fix 回应

**[AGREE] R1-W1: Figure 3 n=4 + p=0.058 不显著，位置过突出**

完全同意。Figure 3（p5）在正文 §4 占据显著位置，但 n=4 线性拟合（R²=0.886, p=0.058）统计效力不足。尽管 caption 标注 "descriptive only"，读者仍会产生强于作者意图的因果推断。建议移至附录或仅以文字简述趋势。

---

**[AGREE] R1-W2: 70B 验证仅一个模型**

同意。Scale-dependent interaction 是核心发现之一（Figure 6, §5.1），但 70B 仅 Llama-3.1-70B-Instruct AWQ INT4。两个额外顾虑：(1) INT4 量化可能与 constrained decoding mask 机制产生非平凡交互，Appendix R 仅验证约束保持有效，未验证 FP16 vs. INT4 下 DR/F1 差异；(2) 8B 层面验证三个家族，70B 仅一个，scale 效应泛化性未经检验。但属于 should-fix——单一 70B 是资源限制下的合理选择，需在 Limitations 明确声明。

---

**[AGREE and ELEVATE to must-fix] R1-W3: 约束表源于训练数据 vs. "compile from IE ontologies" 声称**

同意，且认为**严重性应高于 R1 定级**，建议升级为 must-fix。

具体矛盾：
- Abstract（p1）："OntoCoDec compiles constraints automatically from IE ontologies"
- 系统名："OntoCoDec" = Ontology-Compiled Decoding
- Section 5 Setup（p6）："RE type constraints are extracted from observed type pairs in training data (neither dataset provides a standalone ontology specification)"
- Appendix C（p21）：33% residual DR 来自 "schema coverage gaps"——频率统计遗漏的长尾 valid type pairs

这不仅是表述问题，而是**方法论诚信问题**。训练集共现统计 ≠ 形式化本体编译。前者受数据分布偏差影响（长尾缺失），后者是完备的。理论框架（Proposition 1, §3 decidability analysis）基于"给定完备 ontology"假设，但实验使用不完备的统计近似。

建议：(1) abstract 中 "from IE ontologies" 改为 "from IE schema specifications or training-set statistics"；(2) §3.3 或 §5 明确讨论两条路径的 completeness 差异；(3) 至少在论文中说明 "Onto" 指 ontology-style constraints 而非要求完备本体输入。

---

**[REBUT] R1-W4: S2 在 70B 上 R-F1 退化分析不足**

部分反驳。论文确实提供了分析，虽然分散在多处：

1. Appendix F（p24）明确归因："at 70B, the repair layer over-constraints relation production where baseline DR is already near-zero (0.22%); CF increases from 0.85% (S1) to 0.34% (S2), confirming that over-constraining induces cascading inconsistencies across datasets."
2. §4（p5）讨论了 CF-DR trade-off 的一般机制。
3. §5.1（p7）CF-DR Trade-off Analysis 及 Table 5（p18）量化了 precision-recall 权衡。

R1 问"over-constraining 还是 entity extraction 质量下降"——Appendix F 数据已回答：baseline DR 近零 + S2 导致 CF 变化 + R-F1 下降 7.5pp，明确指向 over-constraining 而非 entity extraction 退化。

但承认分析**分散**——读者需跨 §4、§5.1、Appendix F 才能拼凑完整图景。建议在 §5.1 的 70B 讨论处增加 1-2 句直接归因总结。

---

### Reviewer 1 遗漏但我认为重要的问题

**R2-Additional-1 [warning]: 200-document DocRED 子集的代表性**

70B 实验和部分消融使用 DocRED 200-doc 子集（Appendix G, p29）。DocRED 全集 998 docs、96 relation types，子集是否覆盖足够 relation type 多样性未讨论。Table 29 仅验证 zero-shot 方向一致性，未验证微调场景下子集与全集的 relation-level DR 分布匹配。DocRED 96 个 relation types 长尾分布严重，200-doc 子集可能系统性遗漏低频 relation types。

**R2-Additional-2 [warning]: Beam search 延迟 scaling 未报告**

Appendix F（p26-28）beam search 实现需每个 beam step 独立维护 entity registry 和 semantic state，per-step 从头重建（"reconstructing all entity/relation state from scratch for each beam independently, 61 lines of code"）。这个 O(n) 重建开销在长文档上可能显著增长，但 Table 40 仅报告 greedy decoding 延迟，beam search wall-clock latency scaling 缺失。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2729 · 2026-05-25T21:57:57.830877+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 2730 · 2026-05-25T21:57:59.287383+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 2731 · 2026-05-25T21:57:59.438456+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2732 · 2026-05-25T21:57:59.440560+00:00_

1	# Review Issues Tracker — schema_semantic_constrained_ie
2	# Updated: R26 fixes verified by Reviewer, 2026-05-23
3	
4	# ============================================================
5	# Round 26 — Resolved after Reviewer verification
6	# ============================================================
7	
8	- id: "R26-W1"
9	  summary: "DR→CF trade-off 在 Abstract/正文中 framing 不平衡"
10	  category: framing
11	  severity: critical
12	  status: resolved
13	  first_raised_round: 25
14	  last_seen_round: 26
15	  action_items:
16	    - round: 26
17	      action: "Abstract severity-framing + §7 L16 修正 >90%→26-52%"
18	      assigned_to: paper_agent
19	      status: resolved
20	  resolution: "Abstract 改用 severity-framing (irrecoverable→correctable)，§7 L16 修正为 '26-52% under fine-tuned greedy S1; beam k=4 eliminates all'。Reviewer 独立验证 26-52% 与 Table 2 一致。"
21	  resolution_round: 26
22	
23	- id: "R26-W2"
24	  summary: "WikiEvents n=20 不足以支撑 task generalization claim"
25	  category: experiment
26	  severity: warning
27	  status: resolved
28	  first_raised_round: 23
29	  last_seen_round: 26
30	  action_items:
31	    - round: 26
32	      action: "§7 '3 datasets' → '2 RE datasets + preliminary pilot'"
33	      assigned_to: paper_agent
34	      status: resolved
35	  resolution: "§7 修正为 '2 RE datasets (SciERC, DocRED) and 3 model families, with a preliminary event extraction pilot'。Reviewer spot-check 通过。"
36	  resolution_round: 26
37	
38	- id: "R26-W3"
39	  summary: "70B scale-dependent findings 仅基于单一模型族，vocabulary calibration hypothesis 缺因果证据"
40	  category: experiment
41	  severity: warning
42	  status: resolved
43	  first_raised_round: 23
44	  last_seen_round: 26
45	  action_items:
46	    - round: 26
47	      action: "§7 vocabulary calibration hypothesis 标注 speculative"
48	      assigned_to: paper_agent
49	      status: resolved
50	  resolution: "§7 改为 'speculative hypothesis' + 'confirming this causal mechanism requires cross-family verification beyond our current scope'。Reviewer 确认适当弱化
…[truncated 7570 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---


### Tool call

_source line 2733 · 2026-05-25T21:59:59.284079+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: R27 fresh review, 2026-05-25\n\n# ============================================================\n# Round 27 — New / Recurred Issues\n# ============================================================\n\n- id: \"R27-N1\"\n  summary: \"Ontology-Compiled framing 与 RE 实验约束来源不一致——abstract 承诺 'compile from IE ontologies' 但 SciERC/DocRED 约束从训练数据提取\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R2 升级为 must-fix（方法论诚信），R1 认为 should-fix（framing 而非结构性问题）。Director 裁决 must-fix。\"\n  action_items:\n    - round: 27\n      action: \"Abstract 'from IE ontologies' → 'from IE schema specifications or training-set statistics'；§5 明确标注约束来源；讨论 completeness 差异\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-N2\"\n  summary: \"WikiEvents EE 验证（ZS n=246, FT n=20）不足以支撑标题 'Information Extraction' 的广泛声称——标题/abstract 应以 RE 为主\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1 critical, R2 agree-with-nuance (should-fix). Director 裁决 must-fix——标题 claim 与证据规模不匹配，但修改 framing 即可。R26-W2 修复了 §7 但标题/abstract 仍过宽。\"\n  action_items:\n    - round: 27\n      action: \"标题考虑限定为 RE 或弱化 EE claim；abstract 不将 EE 与 RE 并列为同等验证轴\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-W1\"\n  summary: \"缺乏与现有语义约束 IE 系统（EnriCo/SPIRES/OntoGPT）的 head-to-head 对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1 critical, R2 降级 should-fix（跨领域复现非 trivial）。Director 裁决 should-fix (elevated)。\"\n  action_items:\n    - round: 27\n      action: \"Appendix S 增加定性对比表（约束类型、运行时开销、是否需重训练），明确 post-hoc vs decoding-time trade-off；可选：与 SPIRES validate-then-correct 在 SciERC 上做简单对比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-W2\"\n  summary: \"Figure 3 线性拟合基于 n=4 数据点（R²=0.886, p=0.058），统计效力不足，在正文中位置过突出\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 完全一致 [AGREE]。\"\n  action_items:\n    - round: 27\n      action: \"Figure 3 caption 标注 n=4 和 p>0.05；或移至附录，正文用文字简述趋势\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-W3\"\n  summary: \"70B 验证仅覆盖 Llama-3.1-70B AWQ INT4 一个模型，scale-dependent 结论泛化性不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 一致。R2 额外指出 INT4 量化可能与 mask 机制有非平凡交互。\"\n  action_items:\n    - round: 27\n      action: \"Limitations 明确声明 70B 验证仅限单一模型族+量化；可选：补充 Qwen-72B 或非量化模型消融\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-W4\"\n  summary: \"核心新颖性偏工程导向——各组件（XGrammar + logit masking + bitwise AND）为已有技术组合\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R2 Excitement 2.5/5, R1 Excitement 3/5。两位均同意主要贡献是系统+实证。R1 认为 non-additive interaction 和 Proposition 1 有独立价值。\"\n  action_items:\n    - round: 27\n      action: \"贡献定位更明确为系统贡献+实证发现；强化 Proposition 1 和 non-additive interaction 的独立意义\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-W5\"\n  summary: \"CF violations 在主文讨论不足——附录有 5+ 页分析但主文缺少 forward pointer\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R2 raised, R1 rebutted（附录充分）。Director 判断：附录分析确实充分，但主文应增加 forward pointer。\"\n  action_items:\n    - round: 27\n      action: \"§3.3 或 Limitations 增加 1-2 句 CF failure mode 讨论 + forward pointer 到 Appendix C\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-W6\"\n  summary: \"Entity registry first-seen 语义可能引入系统性偏差——58.1% CF 来自 hallucinated entity\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [2]\n      note: \"R1 同意观察准确但 Appendix C 已有分析、fine-tuning 后 cascade errors 消除。\"\n  action_items:\n    - round: 27\n      action: \"§3.3 增加 1-2 句 first-seen failure mode 风险说明，引导读者至 Appendix C\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-W7\"\n  summary: \"S2 在 70B 上 R-F1 退化 8.25pp 但分析分散——需在正文集中归因\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1 raised, R2 rebutted（Appendix F 已有分析但分散）。Director 判断 should-fix——增加正文集中归因。\"\n  action_items:\n    - round: 27\n      action: \"§5.1 70B 讨论处增加 1-2 句直接归因（over-constraining when baseline DR near zero）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-M1\"\n  summary: \"评估覆盖范围有限——缺乏非英语语言、大规模 schema（>1000 relations）、小模型（<8B）评估\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"两位均同意。R1 补充 Table 40 scalability 验证到 1000 relations 可在主文引用。\"\n  action_items:\n    - round: 27\n      action: \"主文引用 Appendix K scalability 结果；Limitations 更明确讨论覆盖范围限制\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-M2\"\n  summary: \"200-doc DocRED 子集代表性——是否覆盖足够 relation type 多样性未讨论\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [2]\n      note: \"R2 交叉回应新增。96 relation types 长尾分布下 200-doc 子集可能遗漏低频 types。\"\n  action_items:\n    - round: 27\n      action: \"补充 200-doc 子集的 relation type coverage 统计\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-M3\"\n  summary: \"Beam search wall-clock latency scaling 未报告——Table 40 仅覆盖 greedy\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [2]\n      note: \"R2 交叉回应新增。Beam search per-step entity registry 重建 O(n) 开销在长文档上可能显著。\"\n  action_items:\n    - round: 27\n      action: \"补充 beam search latency 数据或在 Limitations 讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 27 — Carried from R26 (status unchanged)\n# ============================================================\n\n- id: \"R26-M2\"\n  summary: \"CF increase 缺少统计检验\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 27\n  action_items:\n    - round: 26\n      action: \"低优先级，DDL 后可补\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M4\"\n  summary: \"正文视觉密度不足\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 27\n  action_items:\n    - round: 26\n      action: \"低优先级——页面紧张\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 26 and earlier — Resolved\n# ============================================================\n\n- id: \"R26-W1\"\n  summary: \"DR→CF trade-off 在 Abstract/正文中 framing 不平衡\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 26\n  resolution: \"Abstract 改用 severity-framing，§7 修正。\"\n  resolution_round: 26\n\n- id: \"R26-W2\"\n  summary: \"WikiEvents n=20 不足以支撑 task generalization claim\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 27\n  resolution: \"§7 已修正。但 R27 发现标题/abstract 仍过宽——升级为 R27-N2。\"\n  resolution_round: 26\n\n- id: \"R26-W3\"\n  summary: \"70B scale-dependent findings 仅基于单一模型族\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 26\n  resolution: \"§7 vocabulary calibration hypothesis 标注 speculative。\"\n  resolution_round: 26\n\n- id: \"R26-W4\"\n  summary: \"Proposition 1 position-based proof vs name-based implementation gap\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 26\n  resolution: \"Appendix O 补充。\"\n  resolution_round: 26\n\n- id: \"R26-W5\"\n  summary: \"绝对 F1 低且缺失监督 baseline 参照\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 26\n  resolution: \"§5 添加 PL-Marker/PURE 参照。\"\n  resolution_round: 26\n\n- id: \"R26-W6\"\n  summary: \"GoLLIE 缺少 F1 参考数字\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 26\n  resolution: \"§6 已添加。\"\n  resolution_round: 26\n\n- id: \"R26-W7\"\n  summary: \"Contribution 1 Mistral coverage overclaim\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 26\n  resolution: \"C1 修正。\"\n  resolution_round: 26\n\n- id: \"R26-W8\"\n  summary: \"Proposition 1 新颖性争议——PL theory known-ness\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 26\n  resolution: \"§3 添加 PL theory acknowledge。\"\n  resolution_round: 26\n\n- id: \"R26-M1\"\n  summary: \"Abstract F1 范围 '40-46%' 验证\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 26\n  resolution: \"Table 2 验证准确。\"\n  resolution_round: 26\n\n- id: \"R26-M3\"\n  summary: \"LoRA 超参迁移 caveat\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 24\n  last_seen_round: 26\n  resolution: \"§5 Setup 已含 caveat。\"\n  resolution_round: 26\n\n- id: \"R16-W5\"\n  summary: \"Proposition 1 定位过高\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 25\n  resolution: \"R26 未复发。\"\n  resolution_round: 25\n\n- id: \"R16-W1\"\n  summary: \"κ-DR 相关性 n=3 呈现不当\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 26\n  resolution: \"R26 未复发。\"\n  resolution_round: 26\n\n- id: \"R23-W4\"\n  summary: \"WikiEvents overclaim\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 26\n  resolution: \"合并到 R26-W2。\"\n  resolution_round: 26\n\n- id: \"R25-N2\"\n  summary: \"GoLLIE 比较不公平\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 26\n  resolution: \"合并到 R26-W6。\"\n  resolution_round: 26\n\n- id: \"R25-W1\"\n  summary: \"DR↔CF trade-off framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 26\n  resolution: \"合并到 R26-W1。\"\n  resolution_round: 26\n\n- id: \"R23-W5\"\n  summary: \"70B overclaim\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 26\n  resolution: \"合并到 R26-W3。\"\n  resolution_round: 26\n\n- id: \"R25-W2\"\n  summary: \"Scale-dependent 缺因果解释\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 26\n  resolution: \"合并到 R26-W3。\"\n  resolution_round: 26\n\n- id: \"R25-W3\"\n  summary: \"S1 vs S2 对比\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 26\n  resolution: \"R26 未复发。\"\n  resolution_round: 26\n\n- id: \"R25-M4\"\n  summary: \"Figure 1 running example\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"空间限制。\"\n  resolution_round: 25\n\n- id: \"R25-M5\"\n  summary: \"Schema evolution 讨论\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 26\n  resolution: \"Limitations 已覆盖。\"\n  resolution_round: 26\n\n- id: \"R23-W1\"\n  summary: \"CF 占残余违规 64%\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R26 未复发。\"\n  resolution_round: 24\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出第 9 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  resolution: \"主文 8 页内。\"\n  resolution_round: 22\n\n- id: \"R16-MF3\"\n  summary: \"Abstract CF framing 偏乐观\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  resolution: \"已分层报告。\"\n  resolution_round: 22\n\n- id: \"R16-W4\"\n  summary: \"70B quantization 影响未隔离\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 21\n  resolution: \"Appendix R 验证。\"\n  resolution_round: 22"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: R27 fresh review, 2026-05-25\n\n# ============================================================\n# Round 27 — New / Recurred Issues\n# ============================================================\n\n- id: \"R27-N1\"\n  summary: \"Ontology-Compiled framing 与 RE 实验约束来源不一致——abstract 承诺 'compile from IE ontologies' 但 SciERC/DocRED 约束从训练数据提取\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R2 升级为 must-fix（方法论诚信），R1 认为 should-fix（framing 而非结构性问题）。Director 裁决 must-fix。\"\n  action_items:\n    - round: 27\n      action: \"Abstract 'from IE ontologies' → 'from IE schema specifications or training-set statistics'；§5 明确标注约束来源；讨论 completeness 差异\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-N2\"\n  summary: \"WikiEvents EE 验证（ZS n=246, FT n=20）不足以支撑标题 'Information Extraction' 的广泛声称——标题/abstract 应以 RE 为主\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1 critical, R2 agree-with-nuance (should-fix). Director 裁决 must-fix——标题 claim 与证据规模不匹配，但修改 framing 即可。R26-W2 修复了 §7 但标题/abstract 仍过宽。\"\n  action_items:\n    - round: 27\n      action: \"标题考虑限定为 RE 或弱化 EE claim；abstract 不将 EE 与 RE 并列为同等验证轴\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-W1\"\n  summary: \"缺乏与现有语义约束 IE 系统（EnriCo/SPIRES/OntoGPT）的 head-to-head 对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1 critical, R2 降级 should-fix（跨领域复现非 trivial）。Director 裁决 should-fix (elevated)。\"\n  action_items:\n    - round: 27\n      action: \"Appendix S 增加定性对比表（约束类型、运行时开销、是否需重训练），明确 post-hoc vs decoding-time trade-off；可选：与 SPIRES validate-then-correct 在 SciERC 上做简单对比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-W2\"\n  summary: \"Figure 3 线性拟合基于 n=4 数据点（R²=0.886, p=0.058），统计效力不足，在正文中位置过突出\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 完全一致 [AGREE]。\"\n  action_items:\n    - round: 27\n      action: \"Figure 3 caption 标注 n=4 和 p>0.05；或移至附录，正文用文字简述趋势\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-W3\"\n  summary: \"70B 验证仅覆盖 Llama-3.1-70B AWQ INT4 一个模型，scale-dependent 结论泛化性不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 一致。R2 额外指出 INT4 量化可能与 mask 机制有非平凡交互。\"\n  action_items:\n    - round: 27\n      action: \"Limitations 明确声明 70B 验证仅限单一模型族+量化；可选：补充 Qwen-72B 或非量化模型消融\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-W4\"\n  summary: \"核心新颖性偏工程导向——各组件（XGrammar + logit masking + bitwise AND）为已有技术组合\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R2 Excitement 2.5/5, R1 Excitement 3/5。两位均同意主要贡献是系统+实证。R1 认为 non-additive interaction 和 Proposition 1 有独立价值。\"\n  action_items:\n    - round: 27\n      action: \"贡献定位更明确为系统贡献+实证发现；强化 Proposition 1 和 non-additive interaction 的独立意义\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-W5\"\n  summary: \"CF violations 在主文讨论不足——附录有 5+ 页分析但主文缺少 forward pointer\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R2 raised, R1 rebutted（附录充分）。Director 判断：附录分析确实充分，但主文应增加 forward pointer。\"\n  action_items:\n    - round: 27\n      action: \"§3.3 或 Limitations 增加 1-2 句 CF failure mode 讨论 + forward pointer 到 Appendix C\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-W6\"\n  summary: \"Entity registry first-seen 语义可能引入系统性偏差——58.1% CF 来自 hallucinated entity\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [2]\n      note: \"R1 同意观察准确但 Appendix C 已有分析、fine-tuning 后 cascade errors 消除。\"\n  action_items:\n    - round: 27\n      action: \"§3.3 增加 1-2 句 first-seen failure mode 风险说明，引导读者至 Appendix C\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-W7\"\n  summary: \"S2 在 70B 上 R-F1 退化 8.25pp 但分析分散——需在正文集中归因\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"R1 raised, R2 rebutted（Appendix F 已有分析但分散）。Director 判断 should-fix——增加正文集中归因。\"\n  action_items:\n    - round: 27\n      action: \"§5.1 70B 讨论处增加 1-2 句直接归因（over-constraining when baseline DR near zero）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-M1\"\n  summary: \"评估覆盖范围有限——缺乏非英语语言、大规模 schema（>1000 relations）、小模型（<8B）评估\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [1, 2]\n      note: \"两位均同意。R1 补充 Table 40 scalability 验证到 1000 relations 可在主文引用。\"\n  action_items:\n    - round: 27\n      action: \"主文引用 Appendix K scalability 结果；Limitations 更明确讨论覆盖范围限制\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-M2\"\n  summary: \"200-doc DocRED 子集代表性——是否覆盖足够 relation type 多样性未讨论\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [2]\n      note: \"R2 交叉回应新增。96 relation types 长尾分布下 200-doc 子集可能遗漏低频 types。\"\n  action_items:\n    - round: 27\n      action: \"补充 200-doc 子集的 relation type coverage 统计\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R27-M3\"\n  summary: \"Beam search wall-clock latency scaling 未报告——Table 40 仅覆盖 greedy\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n    - round: 27\n      reviewers: [2]\n      note: \"R2 交叉回应新增。Beam search per-step entity registry 重建 O(n) 开销在长文档上可能显著。\"\n  action_items:\n    - round: 27\n      action: \"补充 beam search latency 数据或在 Limitations 讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 27 — Carried from R26 (status unchanged)\n# ============================================================\n\n- id: \"R26-M2\"\n  summary: \"CF increase 缺少统计检验\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 27\n  action_items:\n    - round: 26\n      action: \"低优先级，DDL 后可补\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M4\"\n  summary: \"正文视觉密度不足\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 26\n  last_seen_round: 27\n  action_items:\n    - round: 26\n      action: \"低优先级——页面紧张\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 26 and earlier — Resolved\n# ============================================================\n\n- id: \"R26-W1\"\n  summary: \"DR→CF trade-off 在 Abstract/正文中 framing 不平衡\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 26\n  resolution: \"Abstract 改用 severity-framing，§7 修正。\"\n  resolution_round: 26\n\n- id: \"R26-W2\"\n  summary: \"WikiEvents n=20 不足以支撑 task generalization claim\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 27\n  resolution: \"§7 已修正。但 R27 发现标题/abstract 仍过宽——升级为 R27-N2。\"\n  resolution_round: 26\n\n- id: \"R26-W3\"\n  summary: \"70B scale-dependent findings 仅基于单一模型族\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 26\n  resolution: \"§7 vocabulary calibration hypothesis 标注 speculative。\"\n  resolution_round: 26\n\n- id: \"R26-W4\"\n  summary: \"Proposition 1 position-based proof vs name-based implementation gap\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 26\n  resolution: \"Appendix O 补充。\"\n  resolution_round: 26\n\n- id: \"R26-W5\"\n  summary: \"绝对 F1 低且缺失监督 baseline 参照\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 26\n  resolution: \"§5 添加 PL-Marker/PURE 参照。\"\n  resolution_round: 26\n\n- id: \"R26-W6\"\n  summary: \"GoLLIE 缺少 F1 参考数字\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 26\n  resolution: \"§6 已添加。\"\n  resolution_round: 26\n\n- id: \"R26-W7\"\n  summary: \"Contribution 1 Mistral coverage overclaim\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 26\n  resolution: \"C1 修正。\"\n  resolution_round: 26\n\n- id: \"R26-W8\"\n  summary: \"Proposition 1 新颖性争议——PL theory known-ness\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 26\n  last_seen_round: 26\n  resolution: \"§3 添加 PL theory acknowledge。\"\n  resolution_round: 26\n\n- id: \"R26-M1\"\n  summary: \"Abstract F1 范围 '40-46%' 验证\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 26\n  resolution: \"Table 2 验证准确。\"\n  resolution_round: 26\n\n- id: \"R26-M3\"\n  summary: \"LoRA 超参迁移 caveat\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 24\n  last_seen_round: 26\n  resolution: \"§5 Setup 已含 caveat。\"\n  resolution_round: 26\n\n- id: \"R16-W5\"\n  summary: \"Proposition 1 定位过高\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 25\n  resolution: \"R26 未复发。\"\n  resolution_round: 25\n\n- id: \"R16-W1\"\n  summary: \"κ-DR 相关性 n=3 呈现不当\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 26\n  resolution: \"R26 未复发。\"\n  resolution_round: 26\n\n- id: \"R23-W4\"\n  summary: \"WikiEvents overclaim\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 26\n  resolution: \"合并到 R26-W2。\"\n  resolution_round: 26\n\n- id: \"R25-N2\"\n  summary: \"GoLLIE 比较不公平\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 26\n  resolution: \"合并到 R26-W6。\"\n  resolution_round: 26\n\n- id: \"R25-W1\"\n  summary: \"DR↔CF trade-off framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 26\n  resolution: \"合并到 R26-W1。\"\n  resolution_round: 26\n\n- id: \"R23-W5\"\n  summary: \"70B overclaim\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 26\n  resolution: \"合并到 R26-W3。\"\n  resolution_round: 26\n\n- id: \"R25-W2\"\n  summary: \"Scale-dependent 缺因果解释\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 26\n  resolution: \"合并到 R26-W3。\"\n  resolution_round: 26\n\n- id: \"R25-W3\"\n  summary: \"S1 vs S2 对比\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 26\n  resolution: \"R26 未复发。\"\n  resolution_round: 26\n\n- id: \"R25-M4\"\n  summary: \"Figure 1 running example\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"空间限制。\"\n  resolution_round: 25\n\n- id: \"R25-M5\"\n  summary: \"Schema evolution 讨论\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 26\n  resolution: \"Limitations 已覆盖。\"\n  resolution_round: 26\n\n- id: \"R23-W1\"\n  summary: \"CF 占残余违规 64%\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R26 未复发。\"\n  resolution_round: 24\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出第 9 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  resolution: \"主文 8 页内。\"\n  resolution_round: 22\n\n- id: \"R16-MF3\"\n  summary: \"Abstract CF framing 偏乐观\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  resolution: \"已分层报告。\"\n  resolution_round: 22\n\n- id: \"R16-W4\"\n  summary: \"70B quantization 影响未隔离\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 21\n  resolution: \"Appendix R 验证。\"\n  resolution_round: 22"
  }
}
```

</details>

---


### Tool result

_source line 2734 · 2026-05-25T21:59:59.335146+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml\", \"bytes\": 12936}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2735 · 2026-05-25T22:02:34.934999+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 27 审稿报告 — OntoCoDec: Compiled Schema Constraints for Structured IE\n\n**Venue**: EMNLP 2026 (ARR)  \n**审稿模式**: Fresh（重新审稿）  \n**Reviewer 编排**: 2 人（R1 方法严谨性+实验设计 / R2 新颖性+framing+完整性）  \n**轮次**: 1 轮初审 + 交叉分享 → 收敛\n\n---\n\n## Summary\n\n论文提出 OntoCoDec，一个两层约束解码框架（Grammar layer via XGrammar + Semantic layer via dynamic logit masking），将 IE schema 约束编译为 token-level masks，在生成时 enforce domain/range type constraints。Proposition 1 通过 pumping lemma 证明 domain/range 约束超出 CFG 表达能力，为两层设计提供原则性动机。在 SciERC（7 relations）和 DocRED（96 relations）上验证，zero-shot DR 违规减少 94%+，fine-tuning 后 DR→0%，F1 中性或微升。附带 WikiEvents 事件抽取初步验证和 70B 规模实验。\n\n---\n\n## Strengths\n\n**S1. 形式化分析扎实**  \nProposition 1 通过 pumping lemma 严谨证明 domain/range 约束超出 context-free 表达能力。Appendix O 覆盖 position-based 和 name-based 两种情况。此前未有 IE type constraint 非 context-free 的形式化证明，为两层架构提供不可替代的理论动机。[R1 AGREE, R2 AGREE]\n\n**S2. 实验深度罕见**  \n39 页、49 个表格、8 张图。五路消融（Table 1）、跨模型验证（3 model families × 3 datasets）、微调 composability（Table 2）、beam search 分析、fallback causal tracing（Table 4）、CF-DR trade-off 分析（Table 5）、prompt sensitivity（Table 34）、document length 分析、量化鲁棒性（Appendix R）、nucleus sampling 鲁棒性、order invariance（Appendix N）、lucky violation 分析（Table 39）、ontology scalability（Table 40）。[R1 highlight, R2 highlight]\n\n**S3. 统计方法规范**  \nBonferroni 校正 bootstrap CIs（10,000 iterations，document-level resampling）、Cohen's d 效应量、跨种子确定性验证（Table 29）、200-doc 子集功效分析。在 NLP 论文中显著高于平均水平。[R1 5/5 Reproducibility, R2 5/5 Reproducibility]\n\n**S4. Non-additive layer interaction**  \nGrammar-only 3% DR reduction + Semantic-only 24% → Combined 94%。这一超加性效应的定量刻画（含 fallback causal tracing）是有洞察力的实证发现，展示 grammar 层作为 semantic 层 enabling prerequisite 的机制。[R1 acknowledge, R2 acknowledge]\n\n**S5. 诚实的 limitation 分析**  \nCF-DR trade-off、residual error breakdown、fallback 机制量化、lucky violation 分析均透明展示系统真实边界。[R1 highlight]\n\n**S6. 实用部署考量**  \n无需 constraint-specific training，可组合任何有 logits 接口的 autoregressive LM。三级部署方案（greedy S1 / beam k=2 / beam k=4），runtime overhead 2-3%。[R1 highlight, R2 acknowledge]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. \"Ontology-Compiled\" framing 与 RE 实验约束来源不一致** [R27-N1]  \n- Abstract 承诺 \"compiles constraints automatically from IE ontologies\"，系统名 \"OntoCoDec = Ontology-Compiled Decoding\"\n- 但 SciERC/DocRED 的约束实际从训练数据共现统计提取（§5 lines 419-423），非形式化本体编译\n- 仅 WikiEvents 使用了真正的 KAIROS ontology\n- Appendix C 显示 33% residual DR 来自 schema coverage gaps——频率统计遗漏的长尾 valid type pairs\n- 这不仅是表述问题：理论框架（Proposition 1）基于\"给定完备 ontology\"假设，但 RE 实验使用不完备的统计近似\n- **Reviewer 共识**: R2 升级为 must-fix（方法论诚信），R1 认同问题存在但降级为 should-fix。Director 裁决 must-fix。\n- **建议**: (1) Abstract \"from IE ontologies\" → \"from IE schema specifications or training-set statistics\"；(2) §3 或 §5 明确讨论两条路径（完备 ontology vs 经验性统计）的 completeness 差异；(3) 说明 \"Onto\" 指 ontology-style constraints 而非要求完备本体输入\n\n**MF2. WikiEvents 证据不足以支撑\"Structured IE\"标题声称** [R27-N2]  \n- 标题 \"Information Extraction\" 暗示对 IE 的广泛覆盖，abstract 将 EE 列为三个验证轴之一\n- 但 WikiEvents ZS n=246、FT n=20。unconstrained baseline EV+RoV 违规 >85%，使约束有效性 trivially observable\n- n=20 下 F1 影响无法可靠评估\n- 注：R26-W2 已修复 §7 表述（\"2 RE datasets + preliminary pilot\"），但标题/abstract 仍过宽\n- **Reviewer 共识**: R1 critical, R2 agree-with-nuance。Director 裁决 must-fix，但修改 framing 即可解决，无需扩大实验。\n- **建议**: (1) 标题考虑限定为 \"Relation Extraction\" 或添加限定语；(2) Abstract 不将 EE 与 RE 并列为同等验证轴，明确为 \"preliminary pilot\"\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. 缺乏与现有语义约束 IE 系统的直接对比** [R27-W1]  \n- 仅与 grammar-only baselines（GCD/BoostedCD/vLLM guided_json）和自身消融对比\n- 缺少与 EnriCo（ASP 约束）、SPIRES/OntoGPT（post-hoc validation）的 head-to-head\n- Appendix S 以 \"incompatible evaluation settings\" 回避，但 post-hoc validation 可在相同 unconstrained 输出上运行\n- Table 12 的 post-hoc filtering 实现过于简单（直接删除违规 triple），不代表 post-hoc 方法最优表现\n- **Reviewer 分歧**: R1 critical, R2 降级 should-fix（跨领域复现非 trivial）。Director 裁决 should-fix (elevated)。\n- **建议**: Appendix S 增加定性对比表（约束类型、运行时开销、是否需重训练、completeness guarantee），明确 post-hoc vs decoding-time trade-off\n\n**SF2. Figure 3 线性拟合 n=4 统计效力不足** [R27-W2]  \n- R²=0.886, p=0.058（不显著于 α=0.05），仅 4 个数据点\n- 虽标注 \"descriptive only\"，但 Figure 3 在正文 §4 位置突出，给读者过强的因果暗示\n- **Reviewer 共识**: 两位完全一致 [AGREE]\n- **建议**: Caption 明确标注 n=4 和 p>0.05；或移至附录\n\n**SF3. 70B 验证仅一个模型（Llama-3.1-70B AWQ INT4）** [R27-W3]  \n- Scale-dependent interaction 是核心发现之一（Contribution 3），但 70B 仅单一模型+量化\n- 8B 层面验证 3 个家族，70B 仅 1 个，scale 效应泛化性未经检验\n- INT4 量化可能与 constrained decoding mask 机制有非平凡交互\n- **Reviewer 共识**: 两位一致。属资源限制下的合理选择，需明确声明。\n- **建议**: Limitations 明确声明；可选补充 Qwen-72B 或非量化验证\n\n**SF4. 核心新颖性偏工程导向** [R27-W4]  \n- Grammar layer = XGrammar 直接应用，Semantic layer = constrained beam search + type-based filtering 的自然延伸，组合方式（bitwise AND）为标准做法\n- Proposition 1 的 pumping lemma 证明思路在 PL theory 中是标准技术\n- **Reviewer 分歧**: R2 Excitement 2.5/5, R1 Excitement 3/5。R1 认为 non-additive interaction 和 Proposition 1 对 IE 领域有独立价值。\n- **建议**: 贡献定位更明确为\"系统贡献+实证发现\"；强化 Proposition 1 在 IE 约束解码社区的意义论述\n\n**SF5. CF violations 主文讨论不足** [R27-W5]  \n- 附录有 5+ 页详细分析（Tables 4/5/7/8, Appendix C/M），但主文 Limitations 仅一句\n- **Reviewer 分歧**: R2 raised, R1 rebutted（附录充分）。Director 判断：增加主文 forward pointer。\n- **建议**: §3.3 或 Limitations 增加 1-2 句 CF failure mode 讨论 + forward pointer\n\n**SF6. Entity registry first-seen 语义的系统性偏差** [R27-W6]  \n- Table 8: 58.1% CF violations 来自 hallucinated entity，first-seen lock 传播错误类型\n- Fine-tuning 后 cascade errors 完全消除（0/22），但 zero-shot 下是系统性问题\n- Appendix C 有详细分析但主文不足\n- **建议**: §3.3 增加 failure mode 风险说明\n\n**SF7. S2 70B R-F1 退化分析分散** [R27-W7]  \n- S2 70B R-F1 36.28 vs S1 44.53（-8.25pp），原因分析分散在 §4、§5.1、Appendix F\n- Appendix F 数据已回答是 over-constraining 而非 entity extraction 退化，但读者需跨多处才能拼凑\n- **Reviewer 分歧**: R1 raised, R2 rebutted（分析存在但分散）。\n- **建议**: §5.1 增加 1-2 句直接归因总结\n\n### Minor（不影响接收）\n\n**M1.** 评估覆盖范围有限——缺乏非英语语言、超大规模 schema（>1000 relations）、小模型（<8B）评估 [R27-M1]  \n**M2.** 200-doc DocRED 子集的 relation type coverage 代表性未讨论 [R27-M2]  \n**M3.** Beam search wall-clock latency scaling 未报告（Table 40 仅覆盖 greedy） [R27-M3]  \n**M4.** κ(r) 公式中 |E|² 应写为 |E × E| 避免符号混淆 [R2]  \n**M5.** S1/S2 命名不直观，建议改为 \"joint\" / \"pipeline\" [R2]  \n**M6.** Figure 5 x 轴 relation 标签角度使部分名称难辨认 [R2]  \n**M7.** Figure 2 \"Additive prediction (27%)\" 虚线对比度不足 [R1]  \n**M8.** 正文缩写密度高（DR, CF, RV, ET, OOV, BPE），建议表格标题展开关键缩写 [R2]\n\n---\n\n## Reviewer Consensus（两位 AGREE）\n\n1. **Figure 3 统计效力不足**（n=4, p=0.058）——正文位置过突出\n2. **70B 验证范围有限**——单一模型+量化，scale 结论泛化性受限\n3. **约束来源 framing 需修正**——从训练数据提取 ≠ 从形式化 ontology 编译\n4. **WikiEvents 证据不足以支撑标题级别 claim**\n5. **新颖性偏工程导向**——系统贡献而非算法创新\n6. **实验深度和统计规范性极高**（Reproducibility 均 5/5）\n7. **Proposition 1 证明正确**，为两层设计提供原则性动机\n\n## Reviewer Divergence（存在 REBUT）\n\n| Issue | R1 | R2 | Director 裁决 |\n|-------|----|----|--------------|\n| Ontology framing 严重性 | should-fix | **must-fix** | must-fix |\n| Head-to-head baselines | **critical** | should-fix | should-fix (elevated) |\n| CF 讨论是否充分 | 充分（附录 5+ 页） | 不充分（主文不够） | 增加 forward pointer |\n| S2 70B 分析 | 分析不足 | 分析存在但分散 | 集中归因 |\n| Excitement | 3/5 | 2.5/5 | — |\n\n---\n\n## Questions to Authors\n\n1. **RE 约束忠实性**: 从训练数据提取的 type constraints 与\"真正的\"ontology constraints 的一致性如何量化？是否有 ground truth 对比？\n2. **First-seen 替代方案**: 是否考虑过 soft/probabilistic entity registry（如 weighted type distribution masking）？\n3. **CF 下游影响**: DR→CF 转换被描述为 \"severity downgrade\"——是否有定量的下游任务评估支持？\n4. **大规模 schema**: Wikidata-scale（~10K+ relations）下编译和运行时表现？Entity registry 查询复杂度是否成为瓶颈？\n5. **Post-hoc comparison**: 是否可在相同 unconstrained 输出上运行 SPIRES 的 validate-then-correct 流程作为对比？\n\n---\n\n## Missing References\n\nRelated work 覆盖极为全面（主文 2 页 + 附录 4+ 页），未发现重大遗漏。供参考：\n- Josifoski et al. (2023) \"Language Model Decoding as Direct Metrics Optimization\" — 约束解码与度量优化的关系\n- 若能与 SPIRES/OntoGPT 做定性对比，应正式引用 Caufield et al. (2024)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求。本轮未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 已完成（2026-05-25 21:16 → 21:20, ~4 分钟）\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ warning | Page 1-2 | 连续 2 页纯文本无 display item，首个视觉锚点（Figure 1）到 page 3 才出现。实证贡献为主的论文建议在 page 1-2 加 teaser figure |\n| ℹ️ info | Page 7 | Figure 5 x 轴 relation type 标签旋转后字号偏小（约正文 60-70%） |\n| ℹ️ info | Page 5 | Figure 2/3 红绿色组合对 deuteranopia 色盲有风险，建议改用 blue+orange |\n| ℹ️ info | Page 12-16 | Appendix B+C 连续 5 页纯文本，附录可接受但密度极高 |\n| ℹ️ info | Page 39 | 末页内容约 80%，AI 辅助声明列表简短，整体可接受 |\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 — Borderline Conference  \n**置信度**: 4/5（两位 Reviewer 均熟悉约束解码和结构化 IE 领域）\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 4/5 | 4/5 | 4/5 |\n| Excitement | 3/5 | 2.5/5 | 2.75/5 |\n| Reproducibility | 5/5 | 5/5 | 5/5 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**综合判断**:\n\n论文执行质量达到主会议水准——形式化分析正确、实验深度罕见、统计方法规范、附录极其详尽。两个 Must-Fix 问题（ontology framing 偏差 + WikiEvents 泛化 overclaim）均可通过 framing 调整解决，不需要新实验。\n\n主要隐忧是**新颖性**：核心技术是已有组件的工程整合（XGrammar + logit masking + bitwise AND），non-additive interaction 和 Proposition 1 提供了一定的学术增量，但不足以构成强 novelty。Excitement 综合 2.75/5 在 ARR 中偏低。\n\n**定位建议**: 修复两个 Must-Fix 后，论文更适合 Findings 接收（Overall 3.0-3.5 区间）。若要冲主会议（4.0），需要：(1) 至少一个 head-to-head baseline 对比显示显著优势；(2) 更强的 novelty 论证（如 non-additive interaction 的理论解释而非仅实证观察）。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"three distinct IE tasks\" (line 075-076) 过宽——实际仅深入验证 RE，EE 为 pilot\n- Contribution list 准确反映了系统+实证贡献定位\n\n### §3 Method\n- Proposition 1 证明正确，position-based + name-based 两种情况均有覆盖\n- §3.3 Entity registry 的 first-seen 语义缺少 failure mode 警告\n- S1/S2 命名不直观\n\n### §4 Constraint Tightness Analysis\n- Figure 3 线性拟合应弱化展示（n=4, p>0.05）\n- κ(r) 公式 |E|² 符号可优化\n\n### §5 Experiments\n- 消融设计严谨（五路），统计方法规范\n- §5 应更明确标注 SciERC/DocRED 约束来源（训练数据 vs 本体）\n- §5.1 70B 讨论应集中归因 S2 退化原因\n- §5.3 WikiEvents 内部 hedging 到位（\"preliminary pilot\"），但标题/abstract 不匹配\n\n### §6 Related Work\n- 覆盖极为全面\n- 缺少与 post-hoc validation 系统的系统性对比论述\n\n### §7 Conclusion\n- R26-W2 修复后表述已改善（\"2 RE datasets + preliminary pilot\"）\n- 仍需与标题/abstract 对齐\n\n### Appendix\n- 质量极高，覆盖了几乎所有可能的 reviewer 疑问\n- Appendix S (Related Methods Comparison) 应强化为定性对比表",
  "project": "schema_semantic_constrained_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 — Borderline Conference",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 27 审稿报告 — OntoCoDec: Compiled Schema Constraints for Structured IE\n\n**Venue**: EMNLP 2026 (ARR)  \n**审稿模式**: Fresh（重新审稿）  \n**Reviewer 编排**: 2 人（R1 方法严谨性+实验设计 / R2 新颖性+framing+完整性）  \n**轮次**: 1 轮初审 + 交叉分享 → 收敛\n\n---\n\n## Summary\n\n论文提出 OntoCoDec，一个两层约束解码框架（Grammar layer via XGrammar + Semantic layer via dynamic logit masking），将 IE schema 约束编译为 token-level masks，在生成时 enforce domain/range type constraints。Proposition 1 通过 pumping lemma 证明 domain/range 约束超出 CFG 表达能力，为两层设计提供原则性动机。在 SciERC（7 relations）和 DocRED（96 relations）上验证，zero-shot DR 违规减少 94%+，fine-tuning 后 DR→0%，F1 中性或微升。附带 WikiEvents 事件抽取初步验证和 70B 规模实验。\n\n---\n\n## Strengths\n\n**S1. 形式化分析扎实**  \nProposition 1 通过 pumping lemma 严谨证明 domain/range 约束超出 context-free 表达能力。Appendix O 覆盖 position-based 和 name-based 两种情况。此前未有 IE type constraint 非 context-free 的形式化证明，为两层架构提供不可替代的理论动机。[R1 AGREE, R2 AGREE]\n\n**S2. 实验深度罕见**  \n39 页、49 个表格、8 张图。五路消融（Table 1）、跨模型验证（3 model families × 3 datasets）、微调 composability（Table 2）、beam search 分析、fallback causal tracing（Table 4）、CF-DR trade-off 分析（Table 5）、prompt sensitivity（Table 34）、document length 分析、量化鲁棒性（Appendix R）、nucleus sampling 鲁棒性、order invariance（Appendix N）、lucky violation 分析（Table 39）、ontology scalability（Table 40）。[R1 highlight, R2 highlight]\n\n**S3. 统计方法规范**  \nBonferroni 校正 bootstrap CIs（10,000 iterations，document-level resampling）、Cohen's d 效应量、跨种子确定性验证（Table 29）、200-doc 子集功效分析。在 NLP 论文中显著高于平均水平。[R1 5/5 Reproducibility, R2 5/5 Reproducibility]\n\n**S4. Non-additive layer interaction**  \nGrammar-only 3% DR reduction + Semantic-only 24% → Combined 94%。这一超加性效应的定量刻画（含 fallback causal tracing）是有洞察力的实证发现，展示 grammar 层作为 semantic 层 enabling prerequisite 的机制。[R1 acknowledge, R2 acknowledge]\n\n**S5. 诚实的 limitation 分析**  \nCF-DR trade-off、residual error breakdown、fallback 机制量化、lucky violation 分析均透明展示系统真实边界。[R1 highlight]\n\n**S6. 实用部署考量**  \n无需 constraint-specific training，可组合任何有 logits 接口的 autoregressive LM。三级部署方案（greedy S1 / beam k=2 / beam k=4），runtime overhead 2-3%。[R1 highlight, R2 acknowledge]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. \"Ontology-Compiled\" framing 与 RE 实验约束来源不一致** [R27-N1]  \n- Abstract 承诺 \"compiles constraints automatically from IE ontologies\"，系统名 \"OntoCoDec = Ontology-Compiled Decoding\"\n- 但 SciERC/DocRED 的约束实际从训练数据共现统计提取（§5 lines 419-423），非形式化本体编译\n- 仅 WikiEvents 使用了真正的 KAIROS ontology\n- Appendix C 显示 33% residual DR 来自 schema coverage gaps——频率统计遗漏的长尾 valid type pairs\n- 这不仅是表述问题：理论框架（Proposition 1）基于\"给定完备 ontology\"假设，但 RE 实验使用不完备的统计近似\n- **Reviewer 共识**: R2 升级为 must-fix（方法论诚信），R1 认同问题存在但降级为 should-fix。Director 裁决 must-fix。\n- **建议**: (1) Abstract \"from IE ontologies\" → \"from IE schema specifications or training-set statistics\"；(2) §3 或 §5 明确讨论两条路径（完备 ontology vs 经验性统计）的 completeness 差异；(3) 说明 \"Onto\" 指 ontology-style constraints 而非要求完备本体输入\n\n**MF2. WikiEvents 证据不足以支撑\"Structured IE\"标题声称** [R27-N2]  \n- 标题 \"Information Extraction\" 暗示对 IE 的广泛覆盖，abstract 将 EE 列为三个验证轴之一\n- 但 WikiEvents ZS n=246、FT n=20。unconstrained baseline EV+RoV 违规 >85%，使约束有效性 trivially observable\n- n=20 下 F1 影响无法可靠评估\n- 注：R26-W2 已修复 §7 表述（\"2 RE datasets + preliminary pilot\"），但标题/abstract 仍过宽\n- **Reviewer 共识**: R1 critical, R2 agree-with-nuance。Director 裁决 must-fix，但修改 framing 即可解决，无需扩大实验。\n- **建议**: (1) 标题考虑限定为 \"Relation Extraction\" 或添加限定语；(2) Abstract 不将 EE 与 RE 并列为同等验证轴，明确为 \"preliminary pilot\"\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. 缺乏与现有语义约束 IE 系统的直接对比** [R27-W1]  \n- 仅与 grammar-only baselines（GCD/BoostedCD/vLLM guided_json）和自身消融对比\n- 缺少与 EnriCo（ASP 约束）、SPIRES/OntoGPT（post-hoc validation）的 head-to-head\n- Appendix S 以 \"incompatible evaluation settings\" 回避，但 post-hoc validation 可在相同 unconstrained 输出上运行\n- Table 12 的 post-hoc filtering 实现过于简单（直接删除违规 triple），不代表 post-hoc 方法最优表现\n- **Reviewer 分歧**: R1 critical, R2 降级 should-fix（跨领域复现非 trivial）。Director 裁决 should-fix (elevated)。\n- **建议**: Appendix S 增加定性对比表（约束类型、运行时开销、是否需重训练、completeness guarantee），明确 post-hoc vs decoding-time trade-off\n\n**SF2. Figure 3 线性拟合 n=4 统计效力不足** [R27-W2]  \n- R²=0.886, p=0.058（不显著于 α=0.05），仅 4 个数据点\n- 虽标注 \"descriptive only\"，但 Figure 3 在正文 §4 位置突出，给读者过强的因果暗示\n- **Reviewer 共识**: 两位完全一致 [AGREE]\n- **建议**: Caption 明确标注 n=4 和 p>0.05；或移至附录\n\n**SF3. 70B 验证仅一个模型（Llama-3.1-70B AWQ INT4）** [R27-W3]  \n- Scale-dependent interaction 是核心发现之一（Contribution 3），但 70B 仅单一模型+量化\n- 8B 层面验证 3 个家族，70B 仅 1 个，scale 效应泛化性未经检验\n- INT4 量化可能与 constrained decoding mask 机制有非平凡交互\n- **Reviewer 共识**: 两位一致。属资源限制下的合理选择，需明确声明。\n- **建议**: Limitations 明确声明；可选补充 Qwen-72B 或非量化验证\n\n**SF4. 核心新颖性偏工程导向** [R27-W4]  \n- Grammar layer = XGrammar 直接应用，Semantic layer = constrained beam search + type-based filtering 的自然延伸，组合方式（bitwise AND）为标准做法\n- Proposition 1 的 pumping lemma 证明思路在 PL theory 中是标准技术\n- **Reviewer 分歧**: R2 Excitement 2.5/5, R1 Excitement 3/5。R1 认为 non-additive interaction 和 Proposition 1 对 IE 领域有独立价值。\n- **建议**: 贡献定位更明确为\"系统贡献+实证发现\"；强化 Proposition 1 在 IE 约束解码社区的意义论述\n\n**SF5. CF violations 主文讨论不足** [R27-W5]  \n- 附录有 5+ 页详细分析（Tables 4/5/7/8, Appendix C/M），但主文 Limitations 仅一句\n- **Reviewer 分歧**: R2 raised, R1 rebutted（附录充分）。Director 判断：增加主文 forward pointer。\n- **建议**: §3.3 或 Limitations 增加 1-2 句 CF failure mode 讨论 + forward pointer\n\n**SF6. Entity registry first-seen 语义的系统性偏差** [R27-W6]  \n- Table 8: 58.1% CF violations 来自 hallucinated entity，first-seen lock 传播错误类型\n- Fine-tuning 后 cascade errors 完全消除（0/22），但 zero-shot 下是系统性问题\n- Appendix C 有详细分析但主文不足\n- **建议**: §3.3 增加 failure mode 风险说明\n\n**SF7. S2 70B R-F1 退化分析分散** [R27-W7]  \n- S2 70B R-F1 36.28 vs S1 44.53（-8.25pp），原因分析分散在 §4、§5.1、Appendix F\n- Appendix F 数据已回答是 over-constraining 而非 entity extraction 退化，但读者需跨多处才能拼凑\n- **Reviewer 分歧**: R1 raised, R2 rebutted（分析存在但分散）。\n- **建议**: §5.1 增加 1-2 句直接归因总结\n\n### Minor（不影响接收）\n\n**M1.** 评估覆盖范围有限——缺乏非英语语言、超大规模 schema（>1000 relations）、小模型（<8B）评估 [R27-M1]  \n**M2.** 200-doc DocRED 子集的 relation type coverage 代表性未讨论 [R27-M2]  \n**M3.** Beam search wall-clock latency scaling 未报告（Table 40 仅覆盖 greedy） [R27-M3]  \n**M4.** κ(r) 公式中 |E|² 应写为 |E × E| 避免符号混淆 [R2]  \n**M5.** S1/S2 命名不直观，建议改为 \"joint\" / \"pipeline\" [R2]  \n**M6.** Figure 5 x 轴 relation 标签角度使部分名称难辨认 [R2]  \n**M7.** Figure 2 \"Additive prediction (27%)\" 虚线对比度不足 [R1]  \n**M8.** 正文缩写密度高（DR, CF, RV, ET, OOV, BPE），建议表格标题展开关键缩写 [R2]\n\n---\n\n## Reviewer Consensus（两位 AGREE）\n\n1. **Figure 3 统计效力不足**（n=4, p=0.058）——正文位置过突出\n2. **70B 验证范围有限**——单一模型+量化，scale 结论泛化性受限\n3. **约束来源 framing 需修正**——从训练数据提取 ≠ 从形式化 ontology 编译\n4. **WikiEvents 证据不足以支撑标题级别 claim**\n5. **新颖性偏工程导向**——系统贡献而非算法创新\n6. **实验深度和统计规范性极高**（Reproducibility 均 5/5）\n7. **Proposition 1 证明正确**，为两层设计提供原则性动机\n\n## Reviewer Divergence（存在 REBUT）\n\n| Issue | R1 | R2 | Director 裁决 |\n|-------|----|----|--------------|\n| Ontology framing 严重性 | should-fix | **must-fix** | must-fix |\n| Head-to-head baselines | **critical** | should-fix | should-fix (elevated) |\n| CF 讨论是否充分 | 充分（附录 5+ 页） | 不充分（主文不够） | 增加 forward pointer |\n| S2 70B 分析 | 分析不足 | 分析存在但分散 | 集中归因 |\n| Excitement | 3/5 | 2.5/5 | — |\n\n---\n\n## Questions to Authors\n\n1. **RE 约束忠实性**: 从训练数据提取的 type constraints 与\"真正的\"ontology constraints 的一致性如何量化？是否有 ground truth 对比？\n2. **First-seen 替代方案**: 是否考虑过 soft/probabilistic entity registry（如 weighted type distribution masking）？\n3. **CF 下游影响**: DR→CF 转换被描述为 \"severity downgrade\"——是否有定量的下游任务评估支持？\n4. **大规模 schema**: Wikidata-scale（~10K+ relations）下编译和运行时表现？Entity registry 查询复杂度是否成为瓶颈？\n5. **Post-hoc comparison**: 是否可在相同 unconstrained 输出上运行 SPIRES 的 validate-then-correct 流程作为对比？\n\n---\n\n## Missing References\n\nRelated work 覆盖极为全面（主文 2 页 + 附录 4+ 页），未发现重大遗漏。供参考：\n- Josifoski et al. (2023) \"Language Model Decoding as Direct Metrics Optimization\" — 约束解码与度量优化的关系\n- 若能与 SPIRES/OntoGPT 做定性对比，应正式引用 Caufield et al. (2024)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求。本轮未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 已完成（2026-05-25 21:16 → 21:20, ~4 分钟）\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ warning | Page 1-2 | 连续 2 页纯文本无 display item，首个视觉锚点（Figure 1）到 page 3 才出现。实证贡献为主的论文建议在 page 1-2 加 teaser figure |\n| ℹ️ info | Page 7 | Figure 5 x 轴 relation type 标签旋转后字号偏小（约正文 60-70%） |\n| ℹ️ info | Page 5 | Figure 2/3 红绿色组合对 deuteranopia 色盲有风险，建议改用 blue+orange |\n| ℹ️ info | Page 12-16 | Appendix B+C 连续 5 页纯文本，附录可接受但密度极高 |\n| ℹ️ info | Page 39 | 末页内容约 80%，AI 辅助声明列表简短，整体可接受 |\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 — Borderline Conference  \n**置信度**: 4/5（两位 Reviewer 均熟悉约束解码和结构化 IE 领域）\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 4/5 | 4/5 | 4/5 |\n| Excitement | 3/5 | 2.5/5 | 2.75/5 |\n| Reproducibility | 5/5 | 5/5 | 5/5 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**综合判断**:\n\n论文执行质量达到主会议水准——形式化分析正确、实验深度罕见、统计方法规范、附录极其详尽。两个 Must-Fix 问题（ontology framing 偏差 + WikiEvents 泛化 overclaim）均可通过 framing 调整解决，不需要新实验。\n\n主要隐忧是**新颖性**：核心技术是已有组件的工程整合（XGrammar + logit masking + bitwise AND），non-additive interaction 和 Proposition 1 提供了一定的学术增量，但不足以构成强 novelty。Excitement 综合 2.75/5 在 ARR 中偏低。\n\n**定位建议**: 修复两个 Must-Fix 后，论文更适合 Findings 接收（Overall 3.0-3.5 区间）。若要冲主会议（4.0），需要：(1) 至少一个 head-to-head baseline 对比显示显著优势；(2) 更强的 novelty 论证（如 non-additive interaction 的理论解释而非仅实证观察）。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"three distinct IE tasks\" (line 075-076) 过宽——实际仅深入验证 RE，EE 为 pilot\n- Contribution list 准确反映了系统+实证贡献定位\n\n### §3 Method\n- Proposition 1 证明正确，position-based + name-based 两种情况均有覆盖\n- §3.3 Entity registry 的 first-seen 语义缺少 failure mode 警告\n- S1/S2 命名不直观\n\n### §4 Constraint Tightness Analysis\n- Figure 3 线性拟合应弱化展示（n=4, p>0.05）\n- κ(r) 公式 |E|² 符号可优化\n\n### §5 Experiments\n- 消融设计严谨（五路），统计方法规范\n- §5 应更明确标注 SciERC/DocRED 约束来源（训练数据 vs 本体）\n- §5.1 70B 讨论应集中归因 S2 退化原因\n- §5.3 WikiEvents 内部 hedging 到位（\"preliminary pilot\"），但标题/abstract 不匹配\n\n### §6 Related Work\n- 覆盖极为全面\n- 缺少与 post-hoc validation 系统的系统性对比论述\n\n### §7 Conclusion\n- R26-W2 修复后表述已改善（\"2 RE datasets + preliminary pilot\"）\n- 仍需与标题/abstract 对齐\n\n### Appendix\n- 质量极高，覆盖了几乎所有可能的 reviewer 疑问\n- Appendix S (Related Methods Comparison) 应强化为定性对比表",
    "project": "schema_semantic_constrained_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 — Borderline Conference",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 2736 · 2026-05-25T22:02:39.097007+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2216d5b8b87a9472ce204aba11481390:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4162
}
```

</details>

---


### Assistant

_source line 2737 · 2026-05-25T22:02:48.080515+00:00_

Round 27 审稿报告已投递。

**结果汇总**：
- **Overall**: 3.5 Borderline Conference（两位 Reviewer 一致）
- **2 个 Must-Fix**: Ontology framing 偏差 + WikiEvents 泛化 overclaim（均可通过 framing 调整解决，无需新实验）
- **7 个 Should-Fix**: 缺 head-to-head baseline、Figure 3 统计效力、70B 单模型、新颖性定位、CF 主文 pointer、first-seen 偏差、S2 归因分散
- **3 个 Info**: 评估覆盖、DocRED 子集代表性、beam latency
- **Issue Tracker**: 已同步更新 `review_issues.yaml`（13 个 open issues）
- **定位建议**: 修复 Must-Fix 后更适合 Findings 接收；冲主会议需补 head-to-head baseline + 强化 novelty 论证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 208

## Round 208

2 recorded events


### User

_source line 2738 · 2026-05-25T22:02:50.613051+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 全部 Must-Fix 和 Should-Fix 的逐条交叉回应，并汇报给 Review Director。

总结：
- **R1-N1**（WikiEvents 泛化）：AGREE，但降低严重性——修改标题/abstract 措辞即可
- **R1-N2**（缺少 head-to-head 对比）：AGREE，但从 critical 降为 should-fix
- **R1-W1**（Figure 3 不显著）：AGREE
- **R1-W2**（70B 仅一个模型）：AGREE
- **R1-W3**（训练数据 vs. ontology framing gap）：AGREE 并升级为 must-fix——abstract/系统名与实际实现存在方法论诚信问题
- **R1-W4**（S2 70B 退化分析）：REBUT——论文已在 Appendix F 给出归因，但分析分散，需集中呈现
- 额外提出两个 R1 遗漏问题：DocRED 200-doc 子集代表性、beam search 延迟 scaling 缺失

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2739 · 2026-05-25T22:02:59.561237+00:00_

Round 27 审稿报告已投递完成。

**最终结果**: 3.5 Borderline Conference（R1: 3.5, R2: 3.5）

**关键行动项**:
- 2 个 Must-Fix：Ontology framing 修正 + WikiEvents 标题/abstract 限定
- 7 个 Should-Fix：head-to-head 对比表、Figure 3 弱化、70B 声明、novelty 定位、CF forward pointer、first-seen 风险说明、S2 归因集中
- 3 个 Minor info 项

报告和 Issue Tracker（`review_issues.yaml`）均已同步更新并投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---
