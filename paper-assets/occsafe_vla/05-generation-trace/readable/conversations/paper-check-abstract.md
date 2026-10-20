# paper check abstract

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_paper_check_abstract_20260524T212524.jsonl`
- **Structured JSON:** [`bf0ece1c9161e1b96395.json`](../../sessions/bf/bf0ece1c9161e1b96395.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-24T21:26:48.801072+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/abstract.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_check_abstract_20260524T212524",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/abstract.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T21:26:48.801407+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_check_abstract_20260524T212524",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T21:26:48.801579+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_check_abstract_20260524T212524",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-24T21:26:48.801744+00:00_

docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_check_abstract_20260524T212524",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T21:26:48.801878+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_check_abstract_20260524T212524",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T21:26:48.802007+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_check_abstract_20260524T212524",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T21:26:48.802145+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_check_abstract_20260524T212524",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T21:26:48.802307+00:00_

1	% OccSafe-VLA: Occupancy-Aware Safety for Vision-Language-Action Models
2	% Target: CoRL 2026
3	\documentclass{article}
4	
5	\usepackage[dvipsnames]{xcolor}
6	\usepackage{corl_2026}
7	
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb}
10	\usepackage{booktabs}
11	\usepackage{enumitem}
12	\usepackage{subcaption}
13	
14	\newcommand{\todo}[1]{\textcolor{red}{[TODO: #1]}}
15	
16	\title{Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer?\\ An Empirical Investigation}
17	
18	\author{
19	Anonymous Author(s)
20	}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	Fine-tuned Vision-Language-Action (VLA) models can achieve high task success rates yet remain behaviorally unsafe: on SafeLIBERO Level~I, OpenVLA attains 90.7\% task success but only 78.0\% collision avoidance.
27	This paper presents the first factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance.
28	Multiple conditions on OpenVLA-OFT with LoRA vary gradient flow, label content, spatial reference frame, and temporal extent: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth labels), Random OCC (random binary labels), Detach OCC (encoder gradients blocked), Detach+LN (LayerNorm replacing BatchNorm), Depth (egocentric depth prediction), Cutoff@\{15K--45K\} (gradient flow for the first $N$ of 50K steps), and Reverse Cutoff (gradient flow for the last 15K steps only).
29	The central finding is that the Detach OCC degradation ($-$3.4\,pp CAR vs.\ Vanilla) decomposes into two mechanistically distinct pathways: BatchNorm interference accounts for all representational drift (replacing BN with LayerNorm recovers pretrained CKA to Vanilla level and 1.9\,pp CAR; Detach+LN 0.765), while gradient flow absence costs a modest additional 1.5\,pp (within statistical uncertainty) through behavioral regularization beyond representation preservation. Gradient norms fall to 1--13\% of baseline under gradient detachme
…[truncated 1603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_check_abstract_20260524T212524",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-24T21:26:48.802605+00:00_

## Abstract 全文

```latex
Fine-tuned Vision-Language-Action (VLA) models can achieve high task success rates yet remain
behaviorally unsafe: on SafeLIBERO Level~I, OpenVLA attains 90.7\% task success but only 78.0\%
collision avoidance.
This paper presents the first factorial study isolating how auxiliary spatial supervision during
VLA fine-tuning affects collision avoidance.
Multiple conditions on OpenVLA-OFT with LoRA vary gradient flow, label content, spatial reference
frame, and temporal extent: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth
labels), Random OCC (random binary labels), Detach OCC (encoder gradients blocked), Detach+LN
(LayerNorm replacing BatchNorm), Depth (egocentric depth prediction), Cutoff@\{15K--45K\}
(gradient flow for the first $N$ of 50K steps), and Reverse Cutoff (gradient flow for the last
15K steps only).
The central finding is that the Detach OCC degradation ($-$3.4\,pp CAR vs.\ Vanilla) decomposes
into two mechanistically distinct pathways: BatchNorm interference accounts for all
representational drift (replacing BN with LayerNorm recovers pretrained CKA to Vanilla level and
1.9\,pp CAR; Detach+LN 0.765), while gradient flow absence costs a modest additional 1.5\,pp
(within statistical uncertainty) through behavioral regularization beyond representation
preservation. Gradient norms fall to 1--13\% of baseline under gradient detachment; BatchNorm
interference drives representations away from pretrained features (CKA dropping to 0.31--0.54),
while Detach+LN (LayerNorm substitution) fully recovers pretrained CKA despite retaining
\texttt{stop\_gradient}. Full OCC and Random OCC maintain encoder gradient norms at
0.87--1.14$\times$ baseline, preserve pretrained representations (CKA $\geq$ 0.95), and CAR
within 1.7\,pp of Vanilla (78.0--79.7\%).
Within the variance of our experiments, label content type does not significantly affect downstream
safety metrics: structured occupancy, random binary maps, and egocentric depth yield comparable
collision avoidance when gradient flow is maintained.
Cutoff@35K retains high task success (93.3\%) with CAR statistically indistinguishable from Vanilla
($-$0.1\,pp); preliminary cutoff experiments suggest that gradient flow \emph{continuity} matters
more than mere existence---mid-training transitions between gradient-flow and Detach modes
introduce seed-dependent outcome variability not observed under consistent training regimes.
Because the auxiliary head is discarded after training, these spatial losses add zero inference
cost and require no ground-truth spatial labels at deployment.
```

---

## 检查点评估

### a) Dual mechanism (BN interference + gradient flow absence)
**一致。** 明确描述了"two mechanistically distinct pathways"：BN interference 贡献 1.9pp，gradient flow absence 贡献 1.5pp，合计 3.4pp。比例 56%/44% 未显式给出，但数字可推算（1.9/3.4=56%, 1.5/3.4=44%）。

### b) Representation-behavior dissociation (CKA 恢复但 CAR 仍低)
**一致。** "Detach+LN (LayerNorm substitution) fully recovers pretrained CKA despite retaining `stop_gradient`"，同时 Detach+LN CAR = 0.765 仍低于 Vanilla 0.780。CKA 恢复 + CAR 仍有 1.5pp gap = dissociation 概念在。但 abstract 未使用 "representation-behavior dissociation" 这一术语。

### c) Existence regularization
**部分缺失。** "existence regularization" 一词未出现。概念通过 Random OCC ≈ Full OCC 的结果和"label content type does not significantly affect"间接传达，但未提炼为明确的 framing term。Abstract 更侧重 "gradient flow continuity" 而非 "existence regularization"。

### d) 数字核查

| 指标 | Abstract 值 | 参考值 | 判定 |
|------|------------|--------|------|
| Full OCC CAR | 范围 78.0–79.7% 中的上界 → 0.797 | 0.797 | **一致** |
| Detach CAR | 78.0% − 3.4pp = 74.6% → 0.746 | 0.746 | **一致** |
| Vanilla CAR | 78.0% | 0.780 | **一致** |
| Random OCC CAR | 范围 78.0–79.7% 内（隐含） | 0.789 | **一致**（未单独列出） |
| Detach+LN CAR | 0.765 | 0.765 | **一致** |

所有数字与参考值吻合。

### e) 过时或不准确的 claim
未发现明显不准确的 claim。

---

## 建议修改

1. **引入 "existence regularization" 术语。** 这是当前核心叙事的关键概念，但 abstract 中完全缺失。建议在描述 Random OCC ≈ Full OCC 发现处加入，例如将 "behavioral regularization beyond representation preservation" 改为更明确的 "existence regularization — the mere presence of auxiliary gradient flow, regardless of label content, regularizes encoder training"。

2. **显式点出 representation-behavior dissociation。** 目前 CKA 恢复与 CAR 仍低的对比分散在两处，读者需自行拼接。建议用一句话明确："This reveals a representation-behavior dissociation: recovering pretrained representations (CKA) is necessary but not sufficient for recovering safety behavior (CAR)."

3. **Abstract 偏长。** 当前约 280 词，CoRL 通常建议 150–200 词。Cutoff 实验细节（Cutoff@35K 的具体数字、continuity vs. existence 的讨论）可压缩或移至正文，为核心 message 留出空间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_check_abstract_20260524T212524"
}
```

</details>

---
