# review discussion coherence

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_discussion-coherence_20260514T110436_result.json`
- **Structured JSON:** [`a211a063ceb06b855eb1.json`](../../sessions/a2/a211a063ceb06b855eb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 13 cross-references resolve. Here's the audit report:

---

## Discussion.tex 连贯性审查报告

### CRITICAL — 事实性错误

**Line 181**: "Since $\Kempirical = 2$ implies that texts at depth~$\geq 2$ are statistically indistinguishable **from depth-1 text**"

这是错误的。$K^*=2$ 表示 1v2 是最后一个可区分的边界，即 depth-1 和 depth-2 **可以**区分。depth $\geq 2$ 的文本是**彼此**不可区分，不是与 depth-1 不可区分。这与 line 173-175 的三级分类法（human / depth-1 / depth $\geq 2$）自相矛盾。

**修复建议**: 改为 "Since $\Kempirical = 2$ implies that texts at depth~$\geq 2$ are statistically indistinguishable **from one another**"

---

### MODERATE — 内容重复

**Issue 2: Neural probe 重复三次 (Limitations §5.6)**
- Lines 148: Boundary marginality 段引用 neural probe
- Lines 154-156: Operational vs theoretical 段详述 neural probe（"frozen-encoder MLP achieves $\Kempirical^{\text{neural}} = 3$, 2v3 AUC = 0.6195 vs 0.5609"）
- Lines 160-162: Feature representation 段再次详述 neural probe（"frozen LLM embeddings (1536 dimensions) paired with a lightweight MLP push $\Kempirical$ from 2 to 3"）

加上 §5.1 lines 28-35 的首次讨论，neural probe 在全文出现了 **4 次**，其中 Limitations 的后两段几乎说的是同一件事。

**修复建议**: 将 "Operational versus theoretical boundary" 和 "Feature representation" 两段合并为一段，避免重复引用相同的 AUC 数字。

**Issue 3: Model collapse 文献重复引用**
- §5.1 lines 22-26: Shumailov + Dohmatob + Alemohammad
- §5.4 line 83: Shumailov + Alemohammad（几乎同样的论点）
- §5.7 lines 185-188: Shumailov + Alemohammad（再次重复）

三处都在说 "tail-mode collapse / fixed-point convergence"，论点高度重叠。

**修复建议**: §5.4 line 83 可简化为 "consistent with model collapse findings discussed in Section~\ref{sec:discuss_kstar}"，避免重述。

**Issue 4: Prompt-chain vs retrain-chain 重复**
- §5.6 lines 120-126 (Limitations): 详细讨论 prompt-chain upper bound 及 monotonic-degradation assumption
- §5.7 lines 185-189 (Broader Impact): 再次讨论同一关系

两处都提到 $K^*_{\text{retrain}} \leq K^*_{\text{prompt}}$ 和 monotonic-degradation assumption。

**修复建议**: §5.7 可交叉引用 Section~\ref{sec:limitations} 而非重述。

---

### MINOR

**Issue 5: §5.1 内部过渡突兀 (line 37)**
Lines 28-35 讨论 neural probe，line 37 突然跳到 "The consistency of $\Kempirical = 2$ across decoding strategies merits emphasis"。缺少连接句。

**修复建议**: 在 line 36 后加一句过渡，如 "Returning to the hand-crafted feature setting, ..."

**Issue 6: Line 165 — Graduated Filtering 占位符**
"Results for graduated filtering will be added upon completion of ongoing experiments." 作为 Limitations 的一个 `\paragraph` 存在，内容空洞。发表前需要填充或删除。

**Issue 7: Line 93 — "depths $\geq 3$ are mutually indistinguishable" 措辞不精确**
$K^*=2$ 意味着 2v3 已低于阈值，所以 depths $\geq 2$（不是 $\geq 3$）才是互不可分的。当前措辞虽不算错（3v4, 4v5 确实也不可分），但遗漏了 2v3 这个关键边界。

**修复建议**: 改为 "since depths $\geq 2$ are mutually indistinguishable ($\Kempirical = 2$)"

**Issue 8: "80--92\%" 统计重复**
Cross-model transfer 的 "80--92%" 在 lines 46, 53, 77 出现三次。不影响正确性，但显得冗余。

---

### Dangling References

所有 13 个 `\ref` 和 6 个 `\cite` 均有对应 `\label` / bib entry。**无断裂引用。**

---

### Conclusion.tex 对齐检查

Conclusion 与 Discussion 的核心论点对齐良好：$K^*=2$、cross-model transfer、feature degradation、LLM baseline、neural probe、limitations 均覆盖。两个小遗漏（不影响论文质量）：

- Discussion §5.7 提出的 **$K^*$ corpus audit metric** 概念未在 conclusion 中提及
- Discussion §5.5 的 **DetectGPT/Binoculars 不适用于 depth estimation** 论点未在 conclusion 中回应

Conclusion line 51-53 的 graduated filtering TODO 注释是已知的待填充项。

---

### 总结

| 级别 | 数量 | 需要立即修复 |
|------|------|-------------|
| Critical | 1 | Line 181 事实性错误 |
| Moderate | 3 | 内容重复（neural probe ×4, model collapse ×3, prompt-chain ×2） |
| Minor | 4 | 过渡、占位符、措辞 |
| Dangling ref | 0 | — |

最优先修复 line 181 的 "from depth-1 text" → "from one another"。

---
