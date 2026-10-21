# paper fix appendix v1 stats

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/chats/worker_paper_fix-appendix-v1-stats_20260527T042745.jsonl`
- **Structured JSON:** [`5921037537bccbaa290a.json`](../../sessions/59/5921037537bccbaa290a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

5 recorded events

### Tool call

_source line 1 · 2026-05-27T04:28:07.447185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "offset": "60",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-appendix-v1-stats_20260527T042745",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "offset": "60",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-27T04:28:07.447527+00:00_

60	Aux.\ head parameters & 1.2M \\
61	Hardware & NVIDIA RTX PRO 6000 (98\,GB) \\
62	Wall time per run & $\sim$12.9 hours \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \texttt{body\_xpos} exceeds $10^{-3}$. Bootstrap 95\% CIs are computed via 10{,}000 resamples (percentile method).
68	
69	\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed paired $t$-tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency. Detach OCC shows negligible difference from Vanilla ($d \approx -0.04$, $p = 0.91$), confirming that gradient-detached auxiliary supervision does not harm collision avoidance; all gradient-flow conditions also show $p > 0.35$.
70	
71	\textbf{CKA analysis.} Centered Kernel Alignment~\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.
72	
73	\textbf{Cutoff implementation.} As described in Section~\ref{sec:ablation}, setting $\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).
74	
75	\section{Extended Analysis}
76	
77	\begin{figure}[h]
78	\centering
79	\includegraphics[width=\textwidth]{figures/gradient_analysis_combined.pdf}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-appendix-v1-stats_20260527T042745",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T04:28:07.447765+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "old_string": "Detach OCC shows negligible difference from Vanilla ($d \\approx -0.04$, $p = 0.91$), confirming that gradient-detached auxiliary supervision does not harm collision avoidance; all gradient-flow conditions also show $p > 0.35$.",
  "new_string": "Under the v1 codebase, Detach OCC shows negligible difference from Vanilla ($d \\approx -0.04$, $p = 0.91$); under v2 (Table~\\ref{tab:main_results}), the effect reverses in sign ($\\Delta{=}+2.2$\\,pp, $p = 0.28$) but remains statistically indistinguishable from Vanilla, confirming that gradient-detached auxiliary supervision does not harm collision avoidance regardless of codebase version. Under v1, all gradient-flow conditions also show $p > 0.35$."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fix-appendix-v1-stats_20260527T042745",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "old_string": "Detach OCC shows negligible difference from Vanilla ($d \\approx -0.04$, $p = 0.91$), confirming that gradient-detached auxiliary supervision does not harm collision avoidance; all gradient-flow conditions also show $p > 0.35$.",
    "new_string": "Under the v1 codebase, Detach OCC shows negligible difference from Vanilla ($d \\approx -0.04$, $p = 0.91$); under v2 (Table~\\ref{tab:main_results}), the effect reverses in sign ($\\Delta{=}+2.2$\\,pp, $p = 0.28$) but remains statistically indistinguishable from Vanilla, confirming that gradient-detached auxiliary supervision does not harm collision avoidance regardless of codebase version. Under v1, all gradient-flow conditions also show $p > 0.35$."
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T04:28:07.448122+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fix-appendix-v1-stats_20260527T042745",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-27T04:28:07.448392+00:00_

修改完成。v1 统计数据已标注来源，v2 主文结果已交叉引用，核心结论保持不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_fix-appendix-v1-stats_20260527T042745"
}
```

</details>

---
