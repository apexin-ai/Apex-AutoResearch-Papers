# Composability 数字更新清单

## 待 DocRED constrained eval 结果后更新

依赖实验：`w5_qwen_docred_lora_constrained_eval` / `w5_llama_docred_lora_constrained_eval`（及对应的 unconstrained baseline `w5_qwen_docred_lora_unconstrained_eval` / `w5_llama_docred_lora_unconstrained_eval`）

---

### 1. [section5_composability.tex:18-51] Table 5 (tab:composability) — 仅含 SciERC，需加 DocRED 行

- **当前值**: 8 行数据（2 models × {ZS, LoRA} × {U, S1}），全部 SciERC
- **需要更新为**: 新增 DocRED 块（至少 4 行：2 models × {LoRA-U, LoRA-S1}；或 8 行含 ZS-DocRED 作对照）
- **需要的数字**: DocRED FT-unconstrained DR/CF/R-F1/E-F1（两模型）、DocRED FT-S1 DR/CF/R-F1/E-F1（两模型）
- **表格 caption (line 45-49)** 也需从 "on SciERC (551 documents)" 改为 "on SciERC (551) and DocRED (998 documents)"
- **占位符**: 无 TBD，但整个 DocRED 块缺失

### 2. [section5_composability.tex:14-16] 实验描述 — SciERC-only 措辞

- **当前值**: `"We test this by LoRA fine-tuning both Qwen3-8B and Llama-3.1-8B on SciERC and then evaluating each fine-tuned model with and without the two-layer constraints"`
- **需要更新为**: "...on SciERC and DocRED..." 或分段描述两个数据集
- **行号**: 14-16

### 3. [section5_composability.tex:53-68] ¶ "Fine-tuning does not eliminate violations" — 所有数字仅 SciERC

- **line 54-56**: `"lifts relation F1 from 8.23 to 43.86 (Qwen) and from 2.68 to 45.45 (Llama)---a 35--43pp gain"` — 需加 DocRED FT F1 数字
- **line 58**: `"residual domain/range violations persist at 1.95% (Qwen) and 1.11% (Llama)"` — 需加 DocRED FT DR baseline
- **line 60-62**: `"Evaluate-for retains 13.1% DR for the fine-tuned Qwen model despite achieving zero on six of the other seven relations"` — SciERC per-relation analysis；DocRED 是否有类似 tight-constraint relation 残留需分析
- **整段策略**: 可扩展为 "On SciERC, ... On DocRED, ..." 两段式；或保留 SciERC 正文 + DocRED 表格引用

### 4. [section5_composability.tex:70-86] ¶ "Constraints compose at no F1 cost" — 所有数字仅 SciERC

- **line 72-73**: `"eliminates residual DR almost entirely (Qwen 1.95%→0.00%, Llama 1.11%→0.09%)"` — 需加 DocRED FT-U→FT-S1 DR 变化
- **line 73-74**: `"relation F1 changes by less than 0.1pp (−0.09pp Qwen, +0.02pp Llama)"` — 需加 DocRED R-F1 delta
- **line 74-75**: `"entity F1 is identical to the fine-tuned unconstrained baseline in both cases"` — 需验证 DocRED 是否同样成立
- **line 81-82**: `"CF rate at the fine-tuned regime is also markedly lower (1.18% Qwen, 0.46% Llama vs. 9.90% and 6.56%)"` — 需加 DocRED FT CF 数字
- **⚠️ 关键判断**: DocRED FT+S1 是否同样 "no F1 cost"？如果 DocRED FT DR 残留更高（类似 ZS 模式），段落 claim 需 nuance

### 5. [section5_composability.tex:88-98] ¶ "Implication" — 定性 claim

- **当前值**: 通用 claim "Fine-tuning and decoding-time enforcement are complementary, not substitutable"
- **无硬数字需替换**，但如果 DocRED FT 消除了大部分 violations（DR→<0.5%），需 nuance "constraints are most needed when FT data does not cover the full relation distribution"
- **优先级**: 看结果再定

### 6. [main.tex:65] Limitations — CF under fine-tuning 数字

- **当前值**: `"this rate falls to $\leq$1.18\% once the base model is LoRA fine-tuned (Table~\ref{tab:composability})"`
- **需要更新为**: 如果 DocRED FT CF 更高，需改为范围如 `"falls to X--Y%"`；如果也很低可保持
- **关键**: 当前 1.18% 是 SciERC Qwen FT S1 的 CF

### 7. [main.tex:69] Limitations — "DocRED fine-tuning is not reported" ⬅️ 必须删除

- **当前值**: `"Results cover two 8B-class models on two datasets, in both zero-shot and LoRA fine-tuned settings on SciERC; DocRED fine-tuning is not reported (the Qwen LoRA run is still in progress at submission time)."`
- **需要更新为**: 删除 "DocRED fine-tuning is not reported..." 半句，改为 "Results cover two 8B-class models on two datasets, in both zero-shot and LoRA fine-tuned settings."
- **这是 Limitations 中最显眼的"缺失实验"声明，有结果后必须第一时间修改**

### 8. [paper_tables_draft.tex:112,119,128] Table 4 (cross-dataset) — TBD 占位符

- **line 119**: `DocRED & 96 & 18.7 & 28.9 & 7.5 & \textit{TBD} & \textit{TBD}`
- **line 112**: caption 写 "DocRED S1 results are pending (experiment in progress)"
- **line 128**: exp ID 注释写 "(RUNNING)"
- **⚠️ 此文件未被 main.tex \input，是独立草稿。** cross-model table (section5_crossmodel_draft.tex) 已有 DocRED ZS S1 数字（Qwen DR=10.21, Llama DR=2.55）。此文件可清理或标注弃用。
- **优先级**: 低（不影响编译产出）

### 9. [appendix_discussion.tex:13-17] ¶ "Practical Significance" — fine-tuning 泛指

- **当前值**: `"When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary"`
- **无硬数字需更新**（引用的是 Phase 0 ZS baseline 15.37%/18.46%）
- **可选**: 添加一句 DocRED FT evidence 强化论点
- **优先级**: 低

### 10. [section6_related_work.tex:20] & [appendix_related_work.tex:65] — "composable" 泛指

- 无数字，无需更新。DocRED FT 结果出来后 evidence base 变强但文本不变。
- **优先级**: 无

---

## 更新优先级

| 优先级 | 项目 | 原因 |
|--------|------|------|
| **P0** | #1 Table 5 加 DocRED 行 | 核心数据表，composability claim 的直接 evidence |
| **P0** | #7 删除 "DocRED not reported" | Limitations 中的 gap 声明，有结果后必须删 |
| P1 | #2 实验描述改 "SciERC and DocRED" | 与 Table 一致性 |
| P1 | #4 "no F1 cost" 段加 DocRED 数字 | 核心 claim 的量化支撑 |
| P1 | #3 "FT does not eliminate violations" 段 | 支持 claim 的 evidence 扩展 |
| P1 | #6 Limitations CF 数字范围 | 准确性 |
| P2 | #5 Implication 段 | 看结果决定是否调整 |
| P2 | #8 paper_tables_draft.tex TBD | 已非编译文件，低优先级 |
| P3 | #9 Appendix discussion | 可选补充 |
| P3 | #10 Related work | 无需改动 |

## 数据需求汇总

从 DocRED FT 实验中需提取的数字（每个模型 × {unconstrained, S1}）：

| 指标 | Qwen FT-U | Qwen FT-S1 | Llama FT-U | Llama FT-S1 |
|------|-----------|------------|------------|-------------|
| DR (%) | ? | ? | ? | ? |
| RV (%) | ? | ? | ? | ? |
| ET (%) | ? | ? | ? | ? |
| CF (%) | ? | ? | ? | ? |
| R-F1 (×100) | ? | ? | ? | ? |
| E-F1 (×100) | ? | ? | ? | ? |
| Parse failures | ? | ? | ? | ? |

## 注意事项

- DocRED ZS 数据已在 cross-model table (section5_crossmodel_draft.tex) 中，composability table 如果要加 ZS-DocRED 行，直接从那里取（Qwen U: DR=18.46, R-F1=7.74, E-F1=58.15; Qwen S1: DR=10.21, R-F1=8.23, E-F1=59.37; Llama U: DR=26.07, R-F1=5.98, E-F1=55.65; Llama S1: DR=2.55, R-F1=6.27, E-F1=55.01）
- DocRED FT 的 DR reduction 可能比 SciERC FT 更复杂：ZS baseline Qwen DR=10.21%（S1）vs SciERC 0.93%，如果 FT baseline DR 也更高，FT+S1 的残留 DR 也可能更高
- DocRED ontology 有 96 relations，FT 可能无法覆盖所有 long-tail relation 的 type constraint，tight-constraint 残留分析需要类似 SciERC Evaluate-for 的 per-relation breakdown
