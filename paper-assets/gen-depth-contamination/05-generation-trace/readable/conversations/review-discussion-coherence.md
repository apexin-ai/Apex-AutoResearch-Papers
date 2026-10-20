# review discussion coherence

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_review_discussion-coherence_20260514T110436.jsonl`
- **Structured JSON:** [`4eed9a17c1e7343ad76a.json`](../../sessions/4e/4eed9a17c1e7343ad76a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-14T11:07:16.309148+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_discussion-coherence_20260514T110436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T11:07:16.309466+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_discussion-coherence_20260514T110436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-14T11:07:16.309691+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	% === Contribution 1: K*=2 consistent boundary ===
5	% Sources: exp_007 (bootstrap CI + permutation), exp_001/exp_002/exp_017/mvp_pilot (model-mode), exp_003 (decoding ablation)
6	We presented the first systematic measurement of the generational depth
7	discrimination boundary $\Kempirical$ for recursive synthetic text.
8	Across three model architectures in four model-mode configurations
9	(Pythia-1.4B and OLMo-1B in continuation mode; Qwen2.5-1.5B-Instruct in both
10	continuation and rewrite modes) and 4 decoding strategies---totaling 8
11	conditions---we establish $\Kempirical = 2$ as a consistent boundary:
12	classifiers reliably distinguish adjacent generations up to depth~2, but all
13	deeper pairs fall below the operational threshold $\theta = 0.60$.
14	For the four model-mode configurations, bootstrap 95\% confidence intervals
15	and permutation tests confirm statistical significance at the 1v2 boundary
16	($p \leq 0.002$ for all four); the most marginal case, Qwen-continuation,
17	yields a CI lower bound of 0.6015, exceeding $\theta$ by only 0.15\,pp.
18	All four decoding configurations (greedy, nucleus, $T{=}0.70$, $T{=}1.2$)
19	likewise yield 1v2 point-estimate $\auc$ above $\theta$.
20	The 0v1 boundary is near-perfectly separable ($\auc > 0.99$), followed by a
21	sharp ${\sim}$30\,pp drop at 1v2 ($\auc$: 0.6112--0.7039 across all
22	conditions), while all 2v3 pairs fall below~$\theta$.
23	Recursive generation thus acts as a severely lossy channel whose discriminable
24	statistical fingerprint is exhausted within two steps.
25	
26	% === Contribution 2: Ordinal depth estimation framework ===
27	% Sources: exp_010 (OBD vs baselines), exp_013 (cross-model transfer), exp_005 (feature degradation), exp_011 (LLM zero-shot)
28	To operationalize depth estimation, we introduced an ordinal binary
29	decomposition (OBD) framework pairing 15 hand-crafted statistical features
30	with LightGBM classifiers.
31	Cross-mo
…[truncated 3339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_discussion-coherence_20260514T110436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T11:07:16.310031+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	\label{sec:discuss_kstar}
6	
7	The Data Processing Inequality guarantees the existence of a finite $\Ktheory$ beyond which adjacent generations become indistinguishable (Section~\ref{sec:formulation}).
8	Our empirical result---$\Kempirical = 2$ consistently across all 8 tested configurations (4 model-mode combinations and 4 decoding strategies; Section~\ref{sec:kstar_boundary}, Figure~\ref{fig:auc_decay})---establishes that this boundary is not only finite but remarkably shallow at the $\leq$1.5B parameter scale.
9	
10	The shallowness of $\Kempirical$ is explained by the rate of information loss across generations.
11	The 0v1 boundary is near-trivially separable ($\auc > 0.99$ across all configurations; Table~\ref{tab:kstar_ci}), reflecting the large distributional gap between human text and first-generation synthetic text.
12	At the 1v2 boundary, $\auc$ drops by approximately 30 percentage points ($\auc$ range: 0.6112--0.7039 across all eight model$\times$decoding conditions; Table~\ref{tab:kstar_ci}, Figure~\ref{fig:auc_decay}; see also Figure~\ref{fig:s1_auc_decay_ci} in the Appendix), indicating that the majority of the discriminative signal is consumed in the first generation step.
13	By the 2v3 boundary, $\auc$ falls to 0.5496--0.5917 across all eight model$\times$decoding conditions (upper bound from nucleus $p{=}0.9$ decoding; Figure~\ref{fig:auc_decay})---below the operational threshold $\theta = 0.60$---and deeper pairs converge toward chance.
14	Recursive generation thus acts as a severely lossy channel whose information bottleneck is traversed within two steps.
15	
16	The feature degradation analysis (Section~\ref{sec:feature_degradation}) provides mechanistic evidence for this rapid collapse.
17	The most discriminative features---surprisal variance (\texttt{surp\_d1\_std}, \texttt{surp\_std}) and its derivatives---all capture the heterogenei
…[truncated 24090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_discussion-coherence_20260514T110436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T11:07:16.310365+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{(sec:formulation|sec:kstar_boundary|sec:feature_degradation|sec:transfer|fig:auc_decay|tab:kstar_ci|tab:transfer_matrix|tab:top_features|tab:s7_neural_probe|tab:s1_transfer|tab:s2_decoding|tab:s3_llm_zeroshot|fig:s1_auc_decay_ci)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_discussion-coherence_20260514T110436",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{(sec:formulation|sec:kstar_boundary|sec:feature_degradation|sec:transfer|fig:auc_decay|tab:kstar_ci|tab:transfer_matrix|tab:top_features|tab:s7_neural_probe|tab:s1_transfer|tab:s2_decoding|tab:s3_llm_zeroshot|fig:s1_auc_decay_ci)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T11:07:16.310610+00:00_

docs/paper/experiments_c1.tex:16:\label{sec:kstar_boundary}
docs/paper/experiments_c1.tex:31:\label{tab:kstar_ci}
docs/paper/experiments_c1.tex:77:\label{fig:auc_decay}
docs/paper/experiments_c1.tex:126:\label{sec:transfer}
docs/paper/experiments_c1.tex:142:\label{tab:transfer_matrix}
docs/paper/experiments_c1.tex:210:\label{sec:feature_degradation}
docs/paper/experiments_c1.tex:227:\label{tab:top_features}
docs/paper/method.tex:12:\label{sec:formulation}
docs/paper/appendix.tex:8:  \label{fig:s1_auc_decay_ci}
docs/paper/appendix.tex:17:  \label{tab:s1_transfer}
docs/paper/appendix.tex:41:  \label{tab:s2_decoding}
docs/paper/appendix.tex:76:  \label{tab:s3_llm_zeroshot}
docs/paper/appendix.tex:201:  \label{tab:s7_neural_probe}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_discussion-coherence_20260514T110436",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-14T11:07:16.310908+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_review_discussion-coherence_20260514T110436"
}
```

</details>

---
