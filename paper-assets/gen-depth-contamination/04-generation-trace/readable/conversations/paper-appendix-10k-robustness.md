# paper appendix 10k robustness

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_paper_appendix_10k_robustness_20260522T141751.jsonl`
- **Structured JSON:** [`3ef9caf41c380a2aaa8d.json`](../../sessions/3e/3ef9caf41c380a2aaa8d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-22T14:18:41.270930+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix_10k_robustness_20260522T141751",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T14:18:41.271251+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix_10k_robustness_20260522T141751",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T14:18:41.271421+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix_10k_robustness_20260522T141751",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T14:18:41.271832+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Extended Discussion}\\n\\\\label{sec:extended_discussion}\\n\\n\\\\subsection{Theoretical Implications of $\\\\Kempirical = 2$}\\n\\nThe DPI guarantees a finite $\\\\Ktheory$; for general web text, $\\\\Kempirical \\\\leq 2$ across all 10 configurations (1B--8B, 6 families), while structured domains (arXiv) yield $\\\\Kempirical{=}3$, aligning with model collapse convergence~\\\\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.\\nDecoding strategy modestly affects signal strength (1v2 $\\\\auc \\\\in [0.6866, 0.7039]$) but does not shift the boundary.\\n\\n\\\\subsection{Cross-Model Transfer Implications}\\n\\nCross-model classification retains 80--100\\\\% accuracy with scorer-invariant feature rankings ($\\\\rho > 0.90$), enabling single-classifier deployment across generators.\\nAbsolute discriminability at the $\\\\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\\\\Kempirical$ from 2 to 1, while rewrite-mode $\\\\Kempirical = 2$ is preserved.\\nModel family similarity modulates transfer (Pythia$\\\\leftrightarrow$OLMo: 90--92\\\\% vs.\\\\ Qwen-cont$\\\\leftrightarrow$OLMo: 80--85\\\\%).\\n\\n\\\\begin{minipage}{\\\\columnwidth}\\n\\\\centering\\n\\\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\\\rho > 0.90$) and rewrite-mode $\\\\Kempirical = 2$, but reduce continuation-mode $\\\\Kempirical$ from 2 to 1.}\\n\\\\label{tab:crossscorer}\\n\\\\resizebox{\\\\columnwidth}{!}{\\\\input{tables/tab_crossscorer}}\\n\\\\end{minipage}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\small\\n\\\\caption{Three-way ANOVA (Generator $\\\\times$ Scorer $\\\\times$ Depth-Pair) on per-fold pairwise $\\\\auc$ values. DV = per-fold AUC; $N{=}300$ (12 cells $\\\\times$ 5 folds $\\\\times$ 5 depth-pairs). Scorer is statistically significant but explains modest v
…[truncated 7256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix_10k_robustness_20260522T141751",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T14:18:41.272065+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat >> /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix_extended.tex << 'ENDOFAPPEND'\n\n\\subsection{Cross-Sample Robustness: 5K vs.\\ 10K}\n\\label{sec:robustness_10k}\n\nThe preceding analyses fix the sample pool at $N{=}5{,}000$ passages per depth.\nTo assess between-sample variability, we re-draw an independent $N{=}10{,}000$ sample from C4 using a different random seed and repeat the full OBD pipeline.\nIf $\\Kempirical$ and the boundary AUC are driven by the underlying distributional shift rather than by idiosyncrasies of a particular sample, both quantities should remain stable across draws.\n\nTable~\\ref{tab:robustness_10k} reports the results.\nFor Pythia-1.4B (continuation, C4), the 5K and 10K samples agree on $\\Kempirical{=}2$: the 0v1 AUC is nearly identical ($0.9700$ vs.\\ $0.9712$), while the boundary 1v2 AUC decreases from $0.6539$ to $0.6175$ ($\\Delta = -0.036$).\nThis shift is consistent with natural sampling variability across C4 subsets and does not alter the qualitative depth boundary.\nThe 2v3 pair remains near chance in both draws ($0.54$, $0.54$), confirming that depths $\\geq 2$ are indistinguishable regardless of sample.\nResults for Qwen-1.5B and LLaMA-3.1-8B (continuation, C4) are pending; once available, they will allow a more comprehensive assessment of cross-sample stability across model scales.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Cross-sample robustness: pairwise AUC and $\\Kempirical$ under 5K and 10K C4 samples drawn with different random seeds. All configurations use continuation mode. $\\Kempirical$ is determined by the $\\theta{=}0.60$ threshold on 1v2 AUC.}\n\\label{tab:robustness_10k}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & $N$ & \\textbf{AUC(0v1)} & \\textbf{AUC(1v2)} & \\textbf{AUC(2v3)} & $\\Kempirical$ \\\\\n\\midrule\nPythia-1.4B cont & 5K  & 0.9700 & 0.6539 & 0.5400 & 2 \\\\\nPythia-1.4B cont & 10K & 0.9712 & 0.6175 & 0.5364 & 2 \\\\\n\\midrule\nQwen-1.5B cont  & 5K  & \\multicolumn{3}{c}{(see Table~\\ref{tab:bonferroni_ci})} & 2 \\\\\nQwen-1.5B cont  & 10K & \\multicolumn{4}{c}{\\textit{pending}} \\\\\n\\midrule\nLLaMA-8B cont   & 5K  & \\multicolumn{3}{c}{(see Table~\\ref{tab:bonferroni_ci})} & 2 \\\\\nLLaMA-8B cont   & 10K & \\multicolumn{4}{c}{\\textit{pending}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\nENDOFAPPEND",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix_10k_robustness_20260522T141751",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat >> /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix_extended.tex << 'ENDOFAPPEND'\n\n\\subsection{Cross-Sample Robustness: 5K vs.\\ 10K}\n\\label{sec:robustness_10k}\n\nThe preceding analyses fix the sample pool at $N{=}5{,}000$ passages per depth.\nTo assess between-sample variability, we re-draw an independent $N{=}10{,}000$ sample from C4 using a different random seed and repeat the full OBD pipeline.\nIf $\\Kempirical$ and the boundary AUC are driven by the underlying distributional shift rather than by idiosyncrasies of a particular sample, both quantities should remain stable across draws.\n\nTable~\\ref{tab:robustness_10k} reports the results.\nFor Pythia-1.4B (continuation, C4), the 5K and 10K samples agree on $\\Kempirical{=}2$: the 0v1 AUC is nearly identical ($0.9700$ vs.\\ $0.9712$), while the boundary 1v2 AUC decreases from $0.6539$ to $0.6175$ ($\\Delta = -0.036$).\nThis shift is consistent with natural sampling variability across C4 subsets and does not alter the qualitative depth boundary.\nThe 2v3 pair remains near chance in both draws ($0.54$, $0.54$), confirming that depths $\\geq 2$ are indistinguishable regardless of sample.\nResults for Qwen-1.5B and LLaMA-3.1-8B (continuation, C4) are pending; once available, they will allow a more comprehensive assessment of cross-sample stability across model scales.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Cross-sample robustness: pairwise AUC and $\\Kempirical$ under 5K and 10K C4 samples drawn with different random seeds. All configurations use continuation mode. $\\Kempirical$ is determined by the $\\theta{=}0.60$ threshold on 1v2 AUC.}\n\\label{tab:robustness_10k}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & $N$ & \\textbf{AUC(0v1)} & \\textbf{AUC(1v2)} & \\textbf{AUC(2v3)} & $\\Kempirical$ \\\\\n\\midrule\nPythia-1.4B cont & 5K  & 0.9700 & 0.6539 & 0.5400 & 2 \\\\\nPythia-1.4B cont & 10K & 0.9712 & 0.6175 & 0.5364 & 2 \\\\\n\\midrule\nQwen-1.5B cont  & 5K  & \\multicolumn{3}{c}{(see Table~\\ref{tab:bonferroni_ci})} & 2 \\\\\nQwen-1.5B cont  & 10K & \\multicolumn{4}{c}{\\textit{pending}} \\\\\n\\midrule\nLLaMA-8B cont   & 5K  & \\multicolumn{3}{c}{(see Table~\\ref{tab:bonferroni_ci})} & 2 \\\\\nLLaMA-8B cont   & 10K & \\multicolumn{4}{c}{\\textit{pending}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\nENDOFAPPEND",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T14:18:41.272328+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix_10k_robustness_20260522T141751",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T14:18:41.272550+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -45 /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix_10k_robustness_20260522T141751",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -45 /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T14:18:41.272833+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\multicolumn{6}{l}{\\\\textit{$\\\\Kempirical = 1$ configurations}} \\\\\\\\\\nOLMo-1B                   & 0v1 & .9860 & .0009 & $[.983,\\\\,.989]$ & \\\\checkmark \\\\\\\\\\nMistral-7B                & 0v1 & .9842 & .0009 & $[.982,\\\\,.987]$ & \\\\checkmark \\\\\\\\\\nPythia-6.9B$^\\\\S$          & 0v1 & .9599 & .0015$^\\\\dagger$ & $[.956,\\\\,.964]$ & \\\\checkmark \\\\\\\\\\nGemma-2-2B                & 0v1 & .9530 & .0018 & $[.948,\\\\,.958]$ & \\\\checkmark \\\\\\\\\\n\\\\bottomrule\\n\\\\multicolumn{6}{l}{\\\\footnotesize $^\\\\ddagger$Generator: Qwen2.5-7B; scorer: Qwen2.5-1.5B.} \\\\\\\\\\n\\\\multicolumn{6}{l}{\\\\footnotesize $^\\\\S$Nucleus sampling ($p{=}0.95$, $T{=}1.0$).} \\\\\\\\\\n\\\\multicolumn{6}{l}{\\\\footnotesize $^\\\\dagger$Estimated from analogous configurations (no separate bootstrap JSON).}\\n\\\\end{tabular}}\\n\\\\end{table}\\n\\n\\\\subsection{Cross-Sample Robustness: 5K vs.\\\\ 10K}\\n\\\\label{sec:robustness_10k}\\n\\nThe preceding analyses fix the sample pool at $N{=}5{,}000$ passages per depth.\\nTo assess between-sample variability, we re-draw an independent $N{=}10{,}000$ sample from C4 using a different random seed and repeat the full OBD pipeline.\\nIf $\\\\Kempirical$ and the boundary AUC are driven by the underlying distributional shift rather than by idiosyncrasies of a particular sample, both quantities should remain stable across draws.\\n\\nTable~\\\\ref{tab:robustness_10k} reports the results.\\nFor Pythia-1.4B (continuation, C4), the 5K and 10K samples agree on $\\\\Kempirical{=}2$: the 0v1 AUC is nearly identical ($0.9700$ vs.\\\\ $0.9712$), while the boundary 1v2 AUC decreases from $0.6539$ to $0.6175$ ($\\\\Delta = -0.036$).\\nThis shift is consistent with natural sampling variability across C4 subsets and does not alter the qualitative depth boundary.\\nThe 2v3 pair remains near chance in both draws ($0.54$, $0.54$), confirming that depths $\\\\geq 2$ are in
…[truncated 1427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix_10k_robustness_20260522T141751",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-22T14:18:41.273124+00:00_

已完成。

**插入位置**：文件末尾，紧接 `\subsection{Bonferroni-Corrected Confidence Intervals}` 及其表格之后。

**添加内容**：
- `\subsection{Cross-Sample Robustness: 5K vs.\ 10K}`（`\label{sec:robustness_10k}`）
- 两段说明文字：第一段交代实验动机（between-sample variability），第二段报告 Pythia-1.4B 结果（K\*=2 一致，1v2 AUC Δ=-0.036，2v3 near chance），末尾留 pending 占位句
- `Table~\ref{tab:robustness_10k}`：6 行表格，Pythia 行填入完整数据，Qwen/LLaMA 5K 行交叉引用 Bonferroni CI 表，10K 行标 *pending*

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_appendix_10k_robustness_20260522T141751"
}
```

</details>

---
