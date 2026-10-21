# DocRED Composability Paper Update Checklist

当 DocRED constrained FT 结果（Qwen LoRA+S1, Llama LoRA+S1）到来后，需更新的所有位置。

已有 DocRED unconstrained FT baseline:
- Qwen: DR=0.76%, R-F1=40.86%, E-F1=82.15%, CF=0.12%
- Llama: DR=0.49%, R-F1=43.72%, E-F1=83.93%

编译后 Table 编号映射:
- Table 1 = `tab:prompt_comparison` (Violation Landscape)
- Table 2 = `tab:scierc-ablation` (SciERC 5-way ablation)
- Table 3 = `tab:docred-ablation` (DocRED 4-way ablation)
- Table 4 = `tab:cross-model` (Cross-model validation)
- Table 5 = `tab:composability` (Composability matrix, **当前仅 SciERC**)
- Table 6 = `tab:runtime` (Runtime)

---

## 需更新位置

| # | 文件 | 行号/标签 | 当前内容 | 需要的更新 |
|---|------|-----------|----------|-----------|
| 1 | `abstract.tex` | L14 | "Composed with LoRA fine-tuning **on SciERC**, OntoCoDec achieves DR=0% at R-F1 43.77 (loss <0.1pp)" | 扩展为 SciERC+DocRED composability claim，填入 DocRED constrained FT 的 DR/R-F1 数字 |
| 2 | `section1_introduction_draft.tex` | L27 | "composability with fine-tuning (DR→0% at <0.1pp F1 cost)" | 更新 DR 值（DocRED FT+S1 可能不为 0%）；如 DocRED DR≠0%，改为 "DR≤X% at ≤Y pp F1 cost" |
| 3 | `section5_scierc_draft.tex` | L125-127 | "§composability: composability matrix **on SciERC** for both Qwen3-8B and Llama-3.1-8B" | 扩展标题和描述为 "SciERC and DocRED"；或将 DocRED composability 拆为独立 paragraph |
| 4 | `section5_scierc_draft.tex` | L145-146 | "consistently validating Claim 3 **on SciERC** across two model families... We evaluate on **one dataset** and one fine-tuning method (LoRA), so we do not claim composability holds universally." | 改为 "two datasets"；如 DocRED 结果一致，可加强 composability claim |
| 5 | `section5_scierc_draft.tex` | L159-199, `tab:composability` (=**Table 5**) | 仅含 SciERC 4 行（Qwen ZS/LoRA × Unconstr/S1, Llama ZS/LoRA × Unconstr/S1） | **核心更新**: 添加 DocRED 8 行（Qwen ZS/LoRA × U/S1 + Llama ZS/LoRA × U/S1）。DocRED ZS 行数据已有，LoRA 行待填 |
| 6 | `section5_scierc_draft.tex` | L190-197 | Table caption: "Composability matrix **on SciERC** (551 documents)... Evaluation is limited to **one dataset**" | 改为 "SciERC and DocRED"，删除 "limited to one dataset" |
| 7 | `section5_scierc_draft.tex` | L133-157 | Composability 正文段落仅讨论 SciERC 的 Qwen/Llama 数字 | 添加 DocRED FT 段落：Qwen DocRED LoRA DR/R-F1/E-F1/CF, Llama DocRED LoRA DR/R-F1/E-F1/CF, 对比 unconstrained FT baseline |
| 8 | `main.tex` (Limitations) | L70 | "Composability with fine-tuned models is validated on SciERC... evaluation is limited to **one dataset** and one fine-tuning method (LoRA)" | 改为 "validated on SciERC and DocRED"；删除 "limited to one dataset"，保留 "one fine-tuning method" |
| 9 | `main.tex` (Limitations) | L76 | "Validation with fine-tuned models... remains to be explored." | FT 现已在 DocRED 上验证，需改写此句（仅保留 larger scales / non-English 部分） |
| 10 | `section7_conclusion_compressed.tex` | L13 | "Fine-tuning reduces CF by 88% (+9.82pp→+1.18pp; §composability)" | 添加 DocRED FT CF 变化数据 |
| 11 | `section7_conclusion.tex` | L35 | "integration with fine-tuned models has not been explored" | **严重过时**: FT composability 已在 SciERC 验证、即将在 DocRED 验证。此文件为未编译版本但应保持一致 |
| 12 | `section7_conclusion.tex` | L41 | Future work "(3) Integration with fine-tuned models" | 已部分实现；改为 "further integration" 或具体说明未覆盖的方向 |
| 13 | `appendix_discussion.tex` | L74-76 | "Composing OntoCoDec with LoRA on SciERC reduces CF by 88%... empirically validated on **one dataset** and one fine-tuning method but does not generalize without further evidence." | 添加 DocRED FT CF 数据；"one dataset" 改为 "two datasets"；可加强泛化 claim |
| 14 | `appendix_discussion.tex` | L119 | "even well-prompted models exhibit non-trivial violation rates (15.37% DR on SciERC, 18.46% on DocRED)" | 可补充 FT 后残余 DR（Qwen DocRED FT unconstr DR=0.76%, + S1 后的 DR）作为进一步证据 |
| 15 | `section4_composition_draft.tex` | L28 | "DocRED (τ̄=0.842, 5.68 pairs) achieves 45--90%" | 如 FT+S1 在 DocRED 上 DR 进一步降低，可在此处补充 FT 场景下的 DR 变化 |
| 16 | `paper_tables_draft.tex` | L112, L119 | "DocRED S1 results are pending" / TBD entries | 草稿文件，不编译但应更新以保持参考一致性 |

## 条件更新（取决于具体数字）

| # | 条件 | 文件 | 更新内容 |
|---|------|------|----------|
| C1 | 若 DocRED FT+S1 DR=0% | `abstract.tex` L14, `section1_intro` L27 | 可声明 "DR→0% on both datasets" |
| C2 | 若 DocRED FT+S1 DR>0% | `abstract.tex` L14, `section1_intro` L27 | 改为 "DR≤X%" 或分别报告两个数据集 |
| C3 | 若 DocRED FT CF 大幅下降 | `section7_conclusion_compressed.tex` L13, `appendix_discussion.tex` L74 | 可声明 "FT consistently reduces CF across datasets" |
| C4 | 若 DocRED FT R-F1 loss <0.1pp | `section1_intro` L27 | 保持 "<0.1pp F1 cost" claim |
| C5 | 若 DocRED FT R-F1 loss >0.5pp | 全文 | 需弱化 composability F1 claim，不能再说 "zero cost" |

## 一致性检查点

- [ ] Table 5 (`tab:composability`) DocRED 行数字 与 composability 正文段落 (§5.2) 一致
- [ ] Table 5 DocRED FT+S1 DR 与 Abstract composability claim 一致
- [ ] Table 5 DocRED 行 与 Table 4 (`tab:cross-model`) DocRED zero-shot 行一致（ZS 行应完全相同）
- [ ] Abstract "DR→0% at <0.1pp F1 cost" 与实际 DocRED FT 数字一致（可能需修改）
- [ ] Introduction (L27) composability claim 与 Table 5 一致
- [ ] Limitations (main.tex L70) "one dataset" → "two datasets" 已更新
- [ ] Limitations (main.tex L76) "fine-tuned models remains to be explored" 已删除或修改
- [ ] §7 conclusion compressed (L13) CF reduction claim 覆盖 DocRED
- [ ] §7 conclusion full version (L35, L41) FT 相关描述已更新（即使不编译）
- [ ] Appendix B (appendix_discussion.tex L74-76) "one dataset" → "two datasets"
- [ ] paper_framing.md 中 composability claim 与最终论文一致
- [ ] section5_scierc_draft.tex 的 subsection 名可能需改（不再仅限 SciERC）或将 composability 拆为独立 subsection
- [ ] Bootstrap CI 已对 DocRED FT+S1 结果运行并报告 p-value
- [ ] DocRED FT unconstrained baseline 数字（DR=0.76%/0.49%, R-F1=40.86%/43.72%）与 Table 5 新行一致
