# Full-Text Consistency Audit — 2026-05-14

## Critical（必须修复）

| # | 文件:行 | 问题 | 建议修复 |
|---|---------|------|----------|
| 1 | related_work.tex:36 | OBD 名称不一致：此处写 "Ordinal **Boundary** Detection (OBD)"，但 method.tex:90/94 和 conclusion.tex:28-29 写 "Ordinal **Binary** Decomposition (OBD)" | 统一为 "Ordinal Binary Decomposition"（method 中的定义为准） |
| 2 | discussion.tex:13 | 2v3 AUC 范围写 "0.5496--0.5917"，但 Table 3 四组 model-mode 的 2v3 点估计最大值为 0.5893（Qwen-rw），0.5917 无法从已报告数据追溯 | 若只覆盖 4 model-mode 条件，改为 "0.5496--0.5893"；若覆盖全部 8 条件（含 decoding），需在 experiments 中补报 decoding configs 的 2v3 数据 |
| 3 | discussion.tex:110 | 阈值敏感性与 method.tex:124-126 矛盾。Discussion 写 "$K^*_{\text{empirical}}=3$ at $\theta=0.55$"，但 method 写 "ranges from 2 to 3 depending on the configuration"。Discussion 写 "$K^*_{\text{empirical}}=2$ for $\theta \in [0.60,0.65]$"，但 method 写 "at $\theta=0.65$, only rewrite retains $K^*_{\text{empirical}}=2$; continuation-mode configurations yield $K^*_{\text{empirical}}=1$" | 将 discussion 的表述与 method 对齐，保留 configuration-dependent 的精确描述 |
| 4 | discussion.tex:133-134 | `\paragraph{Graduated Filtering.}` 后仅有 TODO 注释，渲染输出为一个没有内容的悬空标题 | 删除该 paragraph 或填充内容；当前状态会在 PDF 中生成空段落标题 |

## Warning（建议修复）

| # | 文件:行 | 问题 | 建议修复 |
|---|---------|------|----------|
| 5 | discussion.tex:32 | Neural probe 对比中 LightGBM 1v2 AUC 写 "0.6114"，但 Table 3 (experiments_c1.tex:37) Qwen-cont 1v2 点估计为 0.6112 | 统一为 0.6112 |
| 6 | discussion.tex:34 | 使用 "discriminable depth horizon" 一次性变体术语，全文其他地方（8 处）统一使用 "discrimination boundary" | 改为 "discrimination boundary" |
| 7 | appendix.tex:8 | Caption 写 "500 bootstrap resamples"，但 method.tex:40 和 experiments_c1.tex:19-20 统一写 "1,000 resamples" | 统一为 1,000 resamples（或确认 appendix 图确实用了 500 次，则需在 caption 中解释差异） |
| 8 | appendix.tex:7-8 | 使用裸文本 "AUC"（2 处），主文全文使用 `$\auc$` macro | 改为 `$\auc$` |
| 9 | appendix.tex:8 | 硬编码 "Figure~2" 而非 `Figure~\ref{fig:auc_decay}` | 改为 `Figure~\ref{fig:auc_decay}` |
| 10 | discussion.tex:76 | LLM baseline 使用 "5 depth classes (depths 0--4)"，但主实验使用 depths 0--5（6 classes）。OBD-LightGBM 的 38.6% 未说明是 5-class 还是 6-class 对比基准 | 明确说明 LLM baseline 和 OBD-LightGBM 的对比是在相同的 5-class 设置下，或解释类别数差异 |

## Info（可选）

| # | 文件:行 | 问题 | 建议修复 |
|---|---------|------|----------|
| 11 | method.tex:40, 160 | 使用 `\S\ref{}` 格式，其他文件统一使用 `Section~\ref{}` | 风格统一选择一种；`\S` 更紧凑适合期刊，`Section~` 更适合会议 |
| 12 | 多文件 | 10 个 `\label{}` 定义后从未被 `\ref{}` 引用：eq:markov, eq:dpi, sec:classifier, sec:experimental_setup, sec:generation_mode_method, sec:discuss_transfer, sec:discuss_features, sec:discuss_llm, sec:limitations, sec:broader_impact | 非错误（部分可能为预留），但可审查是否有遗漏的交叉引用 |
| 13 | main.tex:32-35 | Abstract 被注释掉（含 TODO），提交前需填充 | 预期状态，确保提交前完成 |
| 14 | method.tex:4-10 | Pipeline figure placeholder 被注释掉 | 确认是否需要补图 |
| 15 | conclusion.tex:49-53 | Graduated filtering TODO 注释（不影响渲染输出，但提交前需清理或填充） | 填充 exp-006 结果或删除预留注释 |

## 验证通过项

以下方面检查未发现问题：

- **Notation macros**：`\Kstar`、`\Kempirical`、`\Ktheory`、`\Kempirical^{\text{neural}}`、`\auc` 全文统一使用 macro，无裸写 `$K^*$`（除 appendix AUC 问题外）
- **θ 阈值**：全文统一写 `$\theta = 0.60$`，无 0.6 或 60% 变体
- **模型名称**：Tables 用短名（Qwen-rw/Qwen-cont/Pythia/OLMo），running text 用全名（Qwen-rewrite/Qwen-continuation/Pythia-1.4B/OLMo-1B），首次出现用完整名（Qwen2.5-1.5B-Instruct），模式一致
- **Transfer retention 数值**：80--92%（全 cont-mode pairs）、90--92%（Pythia↔OLMo）、61--63%（Qwen-rw→Pythia/OLMo）均可从 Table 4 计算验证，全文一致
- **0v1 AUC**：within-model "> 0.99"、cross-model "> 0.96"——全文一致
- **Spearman ρ ≥ 0.85**：与 experiments 报告的最小值（OLMo--Qwen-cont: 0.85）一致
- **1v2 AUC range**：0.6112--0.7039（across all 8 conditions）——introduction/conclusion/discussion 一致
- **hand-crafted**：全文统一使用连字符形式，无 "handcrafted"
- **generational depth**：统一使用此术语，未出现 "generation depth" 或 "recursive depth" 变体
- **\cite{} 完整性**：全部 22 个 cite key 在 references.bib 中有对应条目
- **百分比格式**：transfer retention 全文统一用 "80--92\%" 百分比形式
- **Marginal case 数值**：0.6015 CI lower bound、+0.15 pp margin——introduction/experiments/discussion/conclusion 四处一致
