# review paper sections audit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_paper_sections_audit_20260513T215258_result.json`
- **Structured JSON:** [`4f4c4499168a142e7714.json`](../../sessions/4f/4f4c4499168a142e7714.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here is the complete audit.

---

## 审查结果

### A. 数值引用一致性

所有 4 章 tex 文件统一使用 exp-007 bootstrap 值（非原始 pipeline 值），内部一致。以下是发现的问题：

```
[experiments_c1.tex:170] "Pythia→OLMo retains 91--92%" 计算不符 | 0.3531/0.3856=91.6%, 单方向无范围；若含反向 OLMo→Pythia (0.3450/0.3822=90.3%)，范围应为 90--92%
```

```
[experiments_c1.tex:175] "accuracy-based retention of 91--92%" 同上 | 91--92% → 应改为 90--92%
```

```
[introduction.tex:35] "Pythia↔OLMo: 91--92%" 同上 | 91--92% → 90--92%
```

```
[experiments_c1.tex:179] "Qwen-cont↔Pythia also transfers well (83--85% accuracy retention)" 计算不符 | Qwen_cont→Pythia=84.7%, Pythia→Qwen_cont=85.2%，范围 84--85%，不存在 83%
```

其余所有数值与 registry 一致（逐一核对了 tab:kstar_ci 全部 20 个 AUC 值、全部 8 个 CI bound、全部 p-value、tab:transfer_matrix 全部 16 个 cell、tab:top_features 排名、method.tex 的 MAE/mean_pw_auc 值、所有 Δpp 计算）。

### B. 已知修正同步状态

| 修正项 | 状态 |
|--------|------|
| "12 个条件" → "8 个条件" | **未发现** — 4 个 tex 文件中无 "12 conditions" 字样，已修正或在其他文件 |
| D016 universality (非 controllability) | **已正确** — 无 "controllability" 出现 |
| OBD 方向 P(depth ≤ k) vs P(depth > k) | **已正确** — method.tex:95-98 写的是 P(depth > k)（"exceedance probability"），与代码一致 |
| exp-003 config4_t12 数据 | **未引用** — 这些值未出现在当前 4 章中（仅在 intro 中以 rounded 形式引用：0.69→0.70） |
| exp-007 qwen_cont 0v1 CI | **未直接引用** — 表注说 "conservatively inferred"，见下方 C 节第 5 条 |

### C. 图表引用完整性

```
[experiments_c1.tex:75] \includegraphics{figures/fig2_auc_decay.pdf} — figures/ 目录不存在，编译会报错
```

```
[experiments_c1.tex:159] \includegraphics{figures/fig3_transfer_heatmap.pdf} — 同上，文件缺失
```

```
[experiments_c1.tex:157-167] \label{fig:transfer_heatmap} 已定义但全文无 \ref{fig:transfer_heatmap} 引用 — 浮动图无文本锚点
```

```
[introduction.tex:56] \ref{sec:conclusion} 悬空 — conclusion.tex 未写，main.tex 中 \input{conclusion} 被注释
```

```
[experiments_c1.tex:6] 硬编码 "Section~3" | → 应改为 Section~\ref{sec:method}
```

```
[experiments_c1.tex:301] 硬编码 "Section~3" | → 应改为 Section~\ref{sec:method} 或 \S\ref{sec:generation_mode}
```

```
[experiments_c1.tex:30] 表注 "Qwen-cont 0v1 not computed due to AUC > 0.997; conservatively inferred" — registry exp-007 实际有 perm_p=0（已计算，500 次 permutation 均未超过 observed AUC） | 建议修改为 "p < 0.002" 或删除此注
```

所有 `\cite{}` 均在 `references.bib` 中有对应条目，无悬空引用。

### D. 措辞一致性

- **$\Kstar$ vs $\Kempirical$**：experiments_c1.tex:15 节标题用 "$\Kstar = 2$"，而正文建立结论时用 "$\Kempirical = 2$"（line 90）。method.tex 明确区分 $\Kempirical$（经验值）和 $\Ktheory$（理论上界）。节标题用 $\Kstar$ 虽可接受（intro 中 $\Kstar$ 定义为通用 boundary），但可能与 method.tex 的精确区分产生混淆。**建议统一为 $\Kempirical$**。

- CI 格式统一（表内 `[.XXXX,\,.XXXX]`，正文 `$\text{CI}_\text{lower} = X.XXXX$`）✓
- p-value 格式统一（`$p = 0.002$`）✓
- "universality" 叙事一致，无 "controllability" 干扰 ✓

---

**共 10 条需修正项**（4 条数值、6 条格式/引用），无重大数据错误。核心发现 $K^*_{\text{empirical}}=2$ 的所有支撑数据与 registry 完全吻合。

---
