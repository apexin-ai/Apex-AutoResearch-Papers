---
round: 5
overall_score: weak accept
timestamp: 2026-05-17T10:33:03.218829+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 4 审稿报告 — OntoCoDec: Type-Constrained IE via Compiled Ontology Constraints

**目标 Venue**: EMNLP 2026 Findings (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**审稿编排**: 2 名 Reviewer（R1: 方法/实验严谨性; R2: 新颖性/写作/格式）
**交叉验证**: 完成（双向 [AGREE]/[REBUT] 回应）

---

## Summary

OntoCoDec 将 IE 本体模式编译为两层可组合的 token 级解码约束：grammar 层（基于 XGrammar CFG）保证 JSON 结构有效性和实体/关系词汇成员资格，semantic 层通过有状态实体注册表和动态 logit masking 保证逐三元组的 domain/range 类型合规。在 3 个 7-8B 模型和 2 个数据集（SciERC 7 关系, DocRED 96 关系）上，DR 违规降低 42-99%，F1 无显著损失。与 LoRA fine-tuning 组合后 DR≤0.20%。论文同时报告了 CF↔DR 权衡（ZS 下 CF 可达 12%，FT 下降至≤1.2%）和 dual-factor 残差模式的描述性分析。

---

## Strengths

**S1** [共识] 实验设计严谨且覆盖面广：3 模型 × 2 数据集 × 多种消融（grammar-only / semantic-only / full / S1 vs S2）+ fine-tuning composability 验证（4-way ablation 覆盖 4 个 model×dataset 设定）+ runtime 分析 + sampling/beam search 兼容性。数据一致性好，交叉验证 Abstract/§5/Appendix 数字无不匹配。

**S2** [共识] 方法设计扎实：pair-based sequential masking 相对于 independent enforcement 的优势有具体量化支撑（SciERC 33.3%、DocRED 36.8% spurious type pairs），non-rectangularity 分析为设计选择提供了定量基础。两层约束的 enabling dependency（grammar → semantic）有清晰的理论动机和实验验证（semantic-only 仅降 DR 24-25%，full 降 45-94%）。

**S3** [共识] 诚实的局限性讨论：CF↔DR trade-off 通过 Pareto ablation 分析，Mistral 明确定位为 boundary condition，parse failure 的 denominator 处理有说明，dual-factor 的 n=4 限制明确声明为 "descriptive characterization"。

**S4** [共识] Runtime overhead 极低：Full S1 在 DocRED (96 relations) 上仅 +5.4%，FT regime 下 +2.3%，增强了实用性。

**S5** [共识] Reproducibility 基础好：每个实验有 exp_id 可追溯，prompt templates 完整（Appendix A），greedy 实验完全确定性。

---

## Weaknesses（按严重程度排序）

### Must-Fix（影响接收决定）

**MF1** [critical, 共识] **Abstract R²=0.886 (n=4) 统计不充分且过度突出**
- Abstract 第 11 行将 R²=0.886 (n=4) 作为独立句子呈现，给读者以核心贡献的印象。
- 统计问题：n=4 数据点拟合 2 参数线性模型，自由度仅 2；F(1,2)≈15.54，p≈0.058，在 α=0.05 下不显著。
- Mistral 被 post-hoc 排除（"mechanistically distinct error source"），但排除标准是在观察到不符合模型后确定的，构成数据筛选偏差。
- §7 已降级为 "descriptive characterization"，但 Abstract 的定量呈现与定性 disclaimer 矛盾。
- **建议**：(1) Abstract 移除 R² 具体值，改为 "residual DR correlates with the product of schema tightness and baseline violation rate"；(2) Appendix 报告 F 统计量和 p≈0.058；(3) 对 Mistral 排除提供先验标准（如基于 RV=0% 的客观阈值）。

**MF2** [critical, 共识] **Abstract 缩写未展开违反 ARR 规范**
- LLM、IE、CFG、DR、ET、RV、CF、LoRA 均在 Abstract 内使用但未展开。ARR 要求 Abstract 独立可读。
- **建议**：至少展开 LLM（Large Language Model）、IE（Information Extraction）、DR（domain/range）、CF（cross-field consistency）。ET/RV/CFG 可用描述性文字替代。

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, 共识] **Beam search 结果重大但被降级到 Appendix**
- Beam k=4 在 SciERC 全集 551 docs 上实现 DR=0%、CF 0.53%（greedy: DR=0.93%, CF=9.90%），同时解决了主实验两个最大局限。
- 将 greedy 作为 "recommended strategy"（§3.5）缺乏充分理由：SciERC 全集结果 beam strictly dominates greedy。
- DocRED beam 仅 50 docs，且 greedy baseline 来自 998 docs（"Not a matched comparison"），可比性存疑。
- R1 标记 critical，R2 同意重要性但降级（核心贡献是 framework 本身，decoding config 是 deployment 选择）。
- **建议**：(1) §5/§7 讨论 beam 全集结果；(2) 报告 beam runtime 开销；(3) 明确 greedy 为实用推荐、beam 为质量最优；(4) DocRED beam 用匹配的 50-doc subset greedy baseline。

**SF2** [warning, 共识] **Em-dash 过度使用（AI 写作标志）**
- 正文 8-10 处解释性 em-dash（§1, §2, §3, §4, §5, §6）。§3 有 2 处 Unicode em-dash（U+2014）格式不一致。
- R2 标记 critical，R1 降级为 should-fix（camera-ready 可修复）。共识：should-fix。
- 表格数据占位符 `---` 为标准用法，不计入。
- **建议**：逐一替换为逗号、括号或拆分句子。保留至多 2-3 处。Unicode em-dash 必须消除。

**SF3** [warning, 共识] **-ing 分词短语过密（AI 写作标志）**
- 正文约 10 处 -ing 分词短语结尾（"confirming that...", "enabling...", "indicating...", "reflecting...", "showing that..."），Appendix 更密集。
- **建议**：正文中选择性改写为独立句或 which-clauses。

**SF4** [warning, 共识] **Code-gen 新颖性区分未在 §1 Introduction 出现**
- §3 line 9 清楚列出了 IE vs code-gen 的三个技术区别，但 §1 完全未提及 code-gen constrained decoding。审稿人读完 §1 可能质疑 novelty 仅是 "trivial migration"。
- **建议**：§1 第二段或 Contribution #2 附近添加一句简述 IE 与 code-gen type-constrained decoding 的本质区别。

**SF5** [warning, 共识] **Llama DocRED parse failure confounding 未充分分析**
- Llama DocRED parse failure +34%（68→91），且 CF=12.02%（全文最高）恰在此配置。
- Qwen DocRED 提供了 parse-failure-excluded 分析，Llama DocRED 未提供。
- **建议**：提供 Llama DocRED ZS 的 parse-failure-excluded violation rates 和 F1。

**SF6** [warning, 共识] **Post-hoc filtering 在 §1 中 framing 仍有选择性**
- Post-hoc 在 5/6 ZS 配置中 F1 高于 OntoCoDec，但 §1 仅在极端情况下否定 post-hoc。
- R1 标记 should-fix，R2 部分反驳（§1 论点合理但可更平衡）。共识：添加一句平衡表述。
- **建议**：§1 或 §5 添加 "Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48% of predictions including true positives; OntoCoDec's advantage is recall preservation."

**SF7** [warning, 共识] **DocRED fallback coverage 未报告**
- SciERC effective semantic constraint coverage 63.4%（Appendix），DocRED 未报告。
- DocRED fallback rate 10.2% 暗示 coverage ~89.8% 但未显式呈现。
- **建议**：报告 DocRED effective semantic constraint coverage 并与 SciERC 对比。

**SF8** [warning, 共识] **Reproducibility 信息不充分**
- LoRA 超参数（rank, alpha, LR, epochs, batch size）未报告。GPU 型号仅出现一次（Appendix）。Random seeds 对 LoRA training 的影响未讨论。无独立 Reproducibility Statement。
- **建议**：Appendix 添加 Experimental Details 表格（GPU, LoRA 配置, training details）。

**SF9** [warning, 共识] **§4 DR reduction 范围与 Abstract 不一致**
- §4: "SciERC achieves 94-99% DR reduction" 仅 Qwen+Llama（排除 Mistral 76%）。Abstract: "42-99% across three model families"。scope 不同但未标注。
- **建议**：§4 加 "for calibrated models (Qwen, Llama)" 或用全范围 76-99%。

### Minor Issues（不影响接收）

**M1** [info, 共识] RV=0.03% 解释不一致：§5.3 说 "partial JSON recovery"，rebuttal draft 说 "XGrammar enum compilation bug"。需统一。

**M2** [info, 共识] Grammar-only 行未显式标识为 GCD (Geng et al., 2023) 能力上限。建议在 §5 或 §6 添加一句。

**M3** [info, 共识] Semantic-only DocRED ET 增加 +70%（2.48%→4.22%）的机制未针对 DocRED 解释（SciERC 有解释）。

**M4** [info, 共识] DocRED composability 数据散落在文字和 Table 2 caption 中。§5.2 标题 "Results on SciERC" 但包含 DocRED FT 讨论。建议重命名或添加子段落。

**M5** [info, 共识] JSON field ordering 是 sequential masking 的隐含前提。论文应明确说明 grammar layer (JSON Schema) 是否强制 field order。

**M6** [info, 共识] CF-DR trade-off ablation 仅在 SciERC/Qwen 上进行。Llama DocRED（CF=12.02% 最高）缺乏对应 ablation。

**M7** [info, 共识] Design Assumption（first-subword uniqueness）应前置到 §2 Problem Statement。

**M8** [info, R1] Table 1 caption "CF excluded---see text" 的讨论实际在 §5.2；caption 中的 em-dash 应替换。

**M9** [info, 共识] bib 条目 vukovic2024dore 缺少 pages/url。

**M10** [info, 共识] §2 中 $\mathcal{T} = \mathcal{E}$ 同义重复，直接用 $\mathcal{E}$ 即可。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成一致 [AGREE]：
1. R²=0.886 必须从 Abstract 移除（MF1）
2. Abstract 缩写必须展开（MF2）
3. Beam search 应在正文讨论（SF1）
4. Em-dash 和 -ing 模式需清理（SF2, SF3）
5. Code-gen 区分应出现在 §1（SF4）
6. Llama DocRED parse failure 需 excluded 分析（SF5）
7. DocRED fallback coverage 应显式报告（SF7）
8. Reproducibility 信息需补充（SF8）
9. §4 DR 范围应与 Abstract 一致（SF9）
10. RV=0.03% 解释需统一（M1）
11. JSON field ordering 需显式声明（M5）

## Reviewer Divergence

以下问题存在分歧（已记录各方理由）：

**D1** Post-hoc framing 严重性
- R1 [should-fix]：Introduction 未提及 post-hoc 在 5/6 ZS 中 F1 更高，选择性呈现。
- R2 [REBUT]：§1 论点合理（指出 failure mode 而非全面否定），但同意可加一句平衡。
- **Director 判断**：采纳 R2 折中方案——§1 framing 基本合理，但应添加一句承认 post-hoc precision 优势。归入 SF6。

**D2** Em-dash 严重程度
- R2 [critical]：高密度 em-dash 是 AI 生成显著标志，可能引发原创性质疑。
- R1 [should-fix]：不应构成接收障碍，属 camera-ready 修订问题。表格数据占位符是标准用法。
- **Director 判断**：采纳 R1 降级至 should-fix。em-dash 密度确需修复但不影响技术贡献评价。归入 SF2。

**D3** DocRED RE 文献引用
- R2 [should-fix]：缺少 DREEAM、DocGNRE、GLiNER 引用。
- R1 [REBUT]：论文不以 DocRED SOTA 为目标，DREEAM/DocGNRE 与 constraint enforcement 正交。GLiNER 值得提及。
- **Director 判断**：采纳 R1 立场。不作为 should-fix。GLiNER 可选择性引用。

---

## Questions to Authors

**Q1** [共识] JSON Schema 是否强制了 relation triple 中的 field 生成顺序（head → head_type → tail → tail_type）？若 XGrammar 允许任意 key ordering，sequential masking 可能失效。

**Q2** [共识] Beam search + fine-tuning 的组合是否被考虑过？Beam k=4 ZS 的 CF=0.53% 优于 LoRA+S1 的 CF=1.18%。

**Q3** [共识] Semantic-only 在 DocRED 上 ET 增加 +70%（2.48%→4.22%），SciERC 上不变。DocRED 恶化更严重的具体原因是什么？是否因为 96 关系的更复杂 domain/range 组合导致 semantic mask 更频繁排除 preferred types？

**Q4** [共识] CF-DR trade-off ablation（Appendix Table 5）仅在 SciERC/Qwen 上进行。Llama DocRED 有全文最高 CF (12.02%)。是否有理由认为 SciERC 的 trade-off 结论可迁移？

---

## Missing References

- BoostCD (Sakota et al., 2025)：§6 仅一句话提及，考虑到其与 OntoCoDec 的互补性（training-time boosting + decoding-time constraint），值得更详细讨论。
- GLiNER (Zaratiana et al., 2023)：作为 generalist NER 模型，与 OntoCoDec 的 "任何 autoregressive LM 均适用" 定位有对比价值（R1 建议可选引用）。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目配置中 `external_review.paperreview_ai.enabled` 未启用）。

---

## Prior Issues Resolution Summary（Round 1-3 遗留问题）

| Issue | Round 1-3 Status | Round 4 Verdict |
|-------|-----------------|-----------------|
| W1: CF framing bias | in_progress | ✅ **Resolved** — Abstract/Intro 现已显式报告 CF trade-off |
| W8: 'first' claim + DORE | in_progress | ✅ **Resolved** — Narrowed + DORE/GenIE/EnriCo in §6 |
| W9: Design assumption | in_progress | ✅ **Resolved** — §3.3 bold "Design Assumption" |
| R2-N4: ZS F1 context | in_progress | ✅ **Resolved** — §5 DocRED has context paragraph |
| R2-N7: DocRED S2 omission | in_progress | ✅ **Resolved** — §5.3 explicitly explains |
| R2-N8: τ→κ symbol | in_progress | ✅ **Resolved** — κ(r) used throughout |
| R2-N9: DORE/GenIE/EnriCo | in_progress | ✅ **Resolved** — All in §6 main text |
| GC-N2: DR range clarify | in_progress | ✅ **Resolved** — "across three model families" |
| GC-N3: Greedy limitation | in_progress | ✅ **Resolved** — Limitations + beam/sampling appendix |
| R2-N1: R² overclaim | in_progress | ⚠️ **Partially fixed** — §7 downgraded, Abstract still prominent |
| W3: Post-hoc framing | in_progress | ⚠️ **Partially fixed** — Softened but still selective |
| R2-N2: Code-gen in §1 | in_progress | ⚠️ **Partially fixed** — §3 yes, §1 no |
| R2-N3: Parse failure | in_progress | ⚠️ **Partially fixed** — Qwen done, Llama missing |
| R2-N5: Reproducibility | in_progress | ⚠️ **Partially fixed** — Minimal statement only |
| R2-N6: Semantic-only ET | in_progress | ⚠️ **Partially fixed** — SciERC explained, DocRED not |
| R2-N10: RV=0.03% | in_progress | ⚠️ **Inconsistent** — Paper vs rebuttal contradictory |
| GC-N1: GCD ceiling | in_progress | ❌ **Not fixed** |

**总结**: 9/17 已解决，7/17 部分修复，1/17 未修复。

---

## Overall Assessment

**评分**: **Weak Accept** (Findings)
**置信度**: 4/5

**理由**：
论文在方法设计和实验执行上达到 EMNLP Findings 水准。核心贡献（将 IE 本体约束编译为可组合的 token 级 semantic masks）有清晰的技术价值，pair-based sequential masking 的正确性论证充分，实验覆盖面在 constrained decoding 论文中属上乘。CF↔DR trade-off 和 Mistral boundary condition 的诚实处理体现了良好的学术规范。

主要不足：(1) Abstract 中 R²=0.886 (n=4) 统计不充分且过度突出，需移除具体数值；(2) beam search 在 SciERC 全集上同时解决了 DR 和 CF 问题，但被降级到 Appendix，影响了 contribution 的完整呈现；(3) 写作存在 AI 痕迹（em-dash 密度、-ing 模式）；(4) 若干实验覆盖缺口（Llama DocRED parse failure、DocRED fallback coverage、CF-DR ablation 仅 SciERC/Qwen）。

核心 excitement 有限——本质是将 type-constrained decoding 从 code-gen 迁移到 IE，增量贡献清晰但不构成 paradigm shift。适合 Findings 但 Conference 偏弱。

**修复优先级**：
1. [提交前必做] MF1: 移除 Abstract R² 数值 + MF2: 展开 Abstract 缩写
2. [强烈建议] SF1: 正文讨论 beam search 结果 + SF2/SF3: 清理 AI 写作痕迹
3. [建议] SF4-SF9: Code-gen §1 区分、parse failure 分析、post-hoc 平衡、fallback coverage、reproducibility、§4 范围一致性
4. [可选] M1-M10: 统一 RV 解释、GCD 标注、DocRED ET 解释等

---

## Detailed Comments

### Abstract
- 缩写堆积严重（LLM/IE/CFG/DR/ET/RV/CF/LoRA 均未展开），独立可读性差
- R²=0.886 作为独立句子过于突出，应降级为定性描述
- CF trade-off 已正确呈现（较 Round 1-3 显著改善）
- 结构完整（问题→方法→结果→局限），但信息密度过高

### §1 Introduction
- 叙事线清晰：问题（DR violations 15-18%）→ 现有方法不足 → OntoCoDec → 贡献
- 缺失：未提及 code-gen type-constrained decoding（Synchromesh/PICARD/MGD），审稿人无法在 §1 判断 novelty 增量
- Post-hoc framing 可更平衡（添加一句 precision vs recall trade-off）
- Contribution 列表结构化好，但 #3 过长

### §2 Background
- 简洁有效
- $\mathcal{T} = \mathcal{E}$ 冗余

### §3 Method
- 形式化严谨，pair-based sequential masking 论证充分
- Design Assumption 已正确标注（Round 3 issue 已修复）
- 缺失：未显式声明 JSON Schema 是否强制 field ordering（Q1）
- 2 处 Unicode em-dash 需修复

### §4 Constraint Composition
- Decidability taxonomy 有价值
- Tightness 公式和 non-rectangularity 分析有力
- DR reduction 范围 (94-99%) 与 Abstract (42-99%) 不一致

### §5 Experiments
- 覆盖面广，数据一致
- DocRED fallback coverage 未显式报告
- Llama DocRED parse failure excluded 分析缺失
- Semantic-only DocRED ET 增加未解释
- §5.2 标题与内容不匹配

### §6 Related Work
- DORE/GenIE/EnriCo 已在主文本（Round 3 issue 已修复）
- Grammar-only 行未标识为 GCD 上限
- BoostCD 讨论过简

### §7 Discussion and Conclusion
- "Descriptive characterization" 措辞已恰当
- 缺乏对 beam search 全集结果的讨论

### Limitations
- 覆盖面广且诚实
- Greedy decoding limitation 已添加（Round 3 issue 已修复）

### Appendix
- Beam search 结果（Table 7, 8）质量高但应在正文体现
- Sampling robustness（Table 9）验证了 framework 的解码策略无关性