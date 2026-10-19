# AdvBench Layer Selection Bias — Paper Integration Template

> 预写模板，数字留 `[TBD]`。结果出来后替换数字并 apply。
> 实验：R1-8B 在 AdvBench 520 prompts 上的 5-metric layer selection bias (binary jailbreak/safe labels, NOT CP annotations)
> 关键区别：测试的是 C1 (layer selection bias pattern) 在不同数据集+不同标签语义下是否复现

---

## A) Intro (introduction.tex)

### A1. Line 30 C1 bullet — 加入 cross-dataset evidence

**当前文本** (introduction.tex line 30):
```latex
\item \textbf{Metric-induced layer selection bias.} Prior work has noted metric sensitivity in probing~\citep{belinkov2022probing}; our contribution is demonstrating a qualitative reversal (significant to non-significant) in a safety-critical application, where the stakes of metric choice are higher than in typical linguistic probing. Crossing-rate composite metrics systematically select shallow layers across all four models (including Llama), reversing HS probe conclusions at 32B scale. The divergence is not gradual: ...
```

**修改**：在 "across all four models (including Llama)" 后加一句 AdvBench cross-dataset evidence。

**替换为**:
```latex
\item \textbf{Metric-induced layer selection bias.} Prior work has noted metric sensitivity in probing~\citep{belinkov2022probing}; our contribution is demonstrating a qualitative reversal (significant to non-significant) in a safety-critical application, where the stakes of metric choice are higher than in typical linguistic probing. Crossing-rate composite metrics systematically select shallow layers across all four models (including Llama) and across datasets (HarmThoughts step-level CP labels and AdvBench binary jailbreak classification; \cref{app:advbench_layer_bias}), reversing HS probe conclusions at 32B scale. The divergence is not gradual: ...
```

### A2. Line 7 — 研究空白定位（novelty positioning）

**当前文本** (introduction.tex line 5, 第二段末尾):
```latex
More broadly, no prior work tracks how safety signals evolve step-by-step during extended reasoning; existing hidden-state analyses operate across layers (spatial) rather than across generation steps (temporal).\looseness=-1
```

**考虑追加 1 句**（定位两个高置信度空白：隐状态×推理模型 + 跨层一致性）:
```latex
More broadly, no prior work tracks how safety signals evolve step-by-step during extended reasoning; existing hidden-state analyses operate across layers (spatial) rather than across generation steps (temporal). This temporal gap is compounded by the absence of cross-layer consistency analysis: layer selection in probing is treated as a tuning detail, yet we show it constitutes an uncontrolled confound.\looseness=-1
```

---

## B) Experiments (experiments.tex)

### B1. 新段落：在 ensemble paragraph (line 42) 之后，\subsection{HS vs.\ Text Comparison} 之前

**插入位置**: experiments.tex line 43 (在 ensemble paragraph 末尾 `\looseness=-1` 之后)

```latex
\paragraph{Cross-dataset replication (AdvBench).} To test whether metric-induced layer selection bias generalizes beyond HarmThoughts CP labels, we replicate the five-metric layer sweep on AdvBench~\citep{advbench} ([TBD] traces, [TBD] jailbreaks) using R1-8B with binary jailbreak/safe labels instead of step-level CP annotations. The CR-composite selects L[TBD] ([TBD]\% depth) while threshold-based metrics converge on L[TBD] ([TBD]\% depth), a [TBD]-layer divergence ([TBD]\% of model depth) consistent with HarmThoughts (L0 vs.\ L14). This confirms that the layer selection bias is driven by representational geometry, not label semantics (\cref{app:advbench_layer_bias}).\looseness=-1
```

---

## C) Appendix — 新 subsection

### C1. 位置：appendix.tex，在现有 "AdvBench Boundary Condition" (app:advbench_cp) 之后

**Label**: `\label{app:advbench_layer_bias}`

```latex
\subsection{AdvBench Layer Selection Bias Replication}
\label{app:advbench_layer_bias}

We replicate the five-metric layer selection analysis on AdvBench~\citep{advbench} to test whether metric-induced layer divergence depends on HarmThoughts-specific CP annotations or generalizes to simpler binary supervision. Using R1-8B, we generate reasoning traces for all 520 AdvBench prompts, classify each as jailbreak or safe via keyword matching, and evaluate logistic regression probes across all 32 layers (L0--L31) with windows $W \in \{1, 3, 5, 15\}$. The 60/20/20 train/val/test split matches HarmThoughts protocol.

\paragraph{Data distribution.} Of [TBD] traces, [TBD] ([TBD]\%) are classified as jailbreak and [TBD] ([TBD]\%) as safe. Mean steps per trace: [TBD].

\begin{table}[h]
\centering
\small
\caption{AdvBench layer selection (R1-8B, 32 layers). CR-composite selects shallow layers; threshold-based metrics select deep layers, consistent with HarmThoughts (\cref{tab:layer_selection}).}
\label{tab:advbench_layer_selection}
\begin{tabular}{lccc}
\toprule
\textbf{Metric} & \textbf{Best Layer} & \textbf{Depth (\%)} & \textbf{Best $W$} \\
\midrule
CR-composite (BA $\times$ CR) & L[TBD] & [TBD]\% & [TBD] \\
Precision & L[TBD] & [TBD]\% & [TBD] \\
Inverse FPR & L[TBD] & [TBD]\% & [TBD] \\
Balanced accuracy & L[TBD] & [TBD]\% & [TBD] \\
AUROC & L[TBD] & [TBD]\% & [TBD] \\
\bottomrule
\end{tabular}
\end{table}

\paragraph{Crossing rate pattern.} Mean crossing rate at shallow layers (L0--L5): [TBD]; at deep layers (L20--L31): [TBD]. The [TBD]$\times$ ratio is consistent with the 1.4--2.7$\times$ cosine compression range observed on HarmThoughts (\cref{tab:cosine_volatility}).

\paragraph{Per-window consistency.} CR-composite selects shallow layers across all windows: W1$=$L[TBD], W3$=$L[TBD], W5$=$L[TBD], W15$=$L[TBD]. Threshold-based metrics consistently select deep layers regardless of window size.

The [TBD]-layer divergence ([TBD]\% of model depth) between CR-composite and threshold-based selection replicates the HarmThoughts pattern (L0 vs.\ L14, 56\% divergence) under different label semantics (binary jailbreak/safe vs.\ step-level CP). This confirms that the bias arises from representational geometry (shallow-layer cosine compression) rather than task-specific label structure.
```

---

## D) Conclusion (conclusion.tex)

### D1. Line 3 — 移除 "beyond HarmThoughts" 限制语

**当前文本**:
```latex
Layer selection metric choice can reverse a safety study's central conclusion: for QwQ-32B, the same data yield $p{=}0.83$ or $p{<}0.005$ depending solely on metric. The HS advantage is validated at 7--8B (+20--22pp, nested CV) and exploratory$^\dagger$ at 32B (+15--19pp) against 384d encoders, but conditional on encoder quality and position (partially correlated); generalization beyond HarmThoughts and Qwen (3/4) requires causal validation. Until layer selection is controlled, probe-based safety conclusions from any single metric should be treated as provisional.\looseness=-1
```

**替换为**:
```latex
Layer selection metric choice can reverse a safety study's central conclusion: for QwQ-32B, the same data yield $p{=}0.83$ or $p{<}0.005$ depending solely on metric. The layer selection bias replicates on AdvBench with binary jailbreak/safe labels (\cref{app:advbench_layer_bias}), confirming it arises from representational geometry rather than dataset-specific annotations. The HS advantage is validated at 7--8B (+20--22pp, nested CV) and exploratory$^\dagger$ at 32B (+15--19pp) against 384d encoders, but conditional on encoder quality and position (partially correlated); generalization beyond Qwen (3/4 models) requires causal validation. Until layer selection is controlled, probe-based safety conclusions from any single metric should be treated as provisional.\looseness=-1
```

**关键变化**：
- 加入 AdvBench replication 一句
- "beyond HarmThoughts and Qwen (3/4)" → "beyond Qwen (3/4 models)"（HarmThoughts 限制已被 AdvBench 部分解除）

---

## E) Limitations (limitations.tex)

### E1. Line 4-5 — 将单数据集限制改为已部分验证的版本

**当前文本**:
```latex
\paragraph{Single dataset and annotation quality.}
All CP-dependent claims rely on one dataset (HarmThoughts~\citep{harmthoughts}), the only publicly available dataset providing step-level CP annotations for reasoning model traces, with annotations lacking formal inter-annotator agreement; an LLM-based proxy on AdvBench achieved $\kappa{=}0.606$ (\cref{app:iaa}). The geometric precondition (shallow-layer compression) is confirmed on AdvBench (\cref{app:cosine_volatility,app:advbench_cp}), but generalization to other jailbreak datasets, attack taxonomies, or multilingual settings is untested.
```

**替换为**:
```latex
\paragraph{Dataset scope and annotation quality.}
CP-dependent claims (C2, HS vs.\ text advantage) rely on one dataset (HarmThoughts~\citep{harmthoughts}), the only publicly available dataset providing step-level CP annotations for reasoning model traces, with annotations lacking formal inter-annotator agreement; an LLM-based proxy on AdvBench achieved $\kappa{=}0.606$ (\cref{app:iaa}). The methodological finding (C1, layer selection bias) is replicated on AdvBench with binary jailbreak/safe labels (\cref{app:advbench_layer_bias}), and the geometric precondition (shallow-layer compression) is confirmed cross-dataset (\cref{app:cosine_volatility,app:advbench_cp}), but generalization to other jailbreak datasets, attack taxonomies, or multilingual settings is untested.
```

**关键变化**：
- 标题从 "Single dataset" → "Dataset scope"
- 区分 C1 (已跨数据集验证) 和 C2 (仍单数据集)
- 保留其余 limitation 内容不变

---

## Discussion (discussion.tex) — 可选更新

### F1. Line 3 — Discussion 已有 "C1 generalizes across all four models (cross-dataset: ...)" 引用 cosine_volatility

**当前文本**:
```latex
C1 generalizes across all four models (cross-dataset: \cref{app:cosine_volatility}; split-half: \cref{app:split_half})
```

**替换为**:
```latex
C1 generalizes across all four models (cross-dataset layer selection: \cref{app:advbench_layer_bias}; geometric: \cref{app:cosine_volatility}; split-half: \cref{app:split_half})
```

---

## 整合清单（结果出来后执行）

1. 从 `advbench_layer_bias_results.json` 提取所有 `[TBD]` 数值
2. 判断属于哪个场景：
   - **场景 A (full)**: CR-composite 选浅层 (depth < 20%), threshold 选深层 (depth > 50%), divergence > 15%
   - **场景 B (partial)**: CR-composite 选浅层但 divergence < 15%, 或某些 threshold metrics 不一致
   - **场景 C (fail)**: CR-composite 不选浅层
3. 场景 A → apply 以上所有模板 (A-F)
4. 场景 B → 仅 apply Appendix (C) + Discussion (F), Intro/Conclusion/Limitations 保持原样
5. 场景 C → 不修改论文，在 Discussion 加一句 "did not replicate"
6. 替换所有 `[TBD]` 为实际数值
7. `check_paper_consistency` 检查数字一致性
8. 编译确认 ≤ 8 页
9. Commit + report to Director
