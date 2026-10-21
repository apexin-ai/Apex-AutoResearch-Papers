# paper section3 method warnings fix

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_paper_section3_method_warnings_fix_20260514T055617.jsonl`
- **Structured JSON:** [`5e58393b8d95a51ff607.json`](../../sessions/5e/5e58393b8d95a51ff607.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-14T05:57:55.485793+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T05:57:55.486213+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Near-Complete Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity—well-formed JSON with ontology-vocabulary membership—while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
10	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and the two decoding strategies (\S\ref{sec:strategies}).
11	Formal analysis of constraint composition and the grammar-first invariant is deferred to Section~\ref{sec:composition}.
12	
13	
14	\subsection{Problem Formulation}
15	\label{sec:formulation}
16	
17	\paragraph{IE as structured generation.}
18	Given an input text $x$, a language model generates a structured JSON output $y$ encoding the extracted information:
19	%
20	\begin{equation}\label{eq:output-schema}
21	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\},
22	\end{equation}
23	%
24	where each entity has a name $n_i$ and type $\tau_i$, and each relation triple specifies a head entity $h_j$, tail entity $t_j$, relation type $r_j$, and the corresponding head and tail entity types $\tau^h_j$ and $\tau^t_j$.
25	
26	\paragraph{Ontology schema.}
27	An ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \operatorname{dom}, \operatorname{range})$ defines the set of entity types $\mathcal{E}$, the set of relation types $\mathcal{R}$, and two functions $\operatorname{dom}: \mathcal{R} \to 2^{\mathcal{E}}$ and $\operatorname{range}: \mathcal{R} \to 2^{\mathcal{E}}$ that specify, for each relation, the entity types permitted as head and tail respectively.
28	
29	\paragraph{Ontology compliance.}
30	
…[truncated 11226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T05:57:55.486453+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex",
  "old_string": "Formal analysis of constraint composition and the grammar-first invariant is deferred to Section~\\ref{sec:composition}.",
  "new_string": "Further discussion of constraint composition and the grammar-first fallback mechanism appears in Section~\\ref{sec:composition}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex",
    "old_string": "Formal analysis of constraint composition and the grammar-first invariant is deferred to Section~\\ref{sec:composition}.",
    "new_string": "Further discussion of constraint composition and the grammar-first fallback mechanism appears in Section~\\ref{sec:composition}."
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T05:57:55.486654+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T05:57:55.486842+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex",
  "old_string": "OntoCoDec's two-layer design covers the first two classes: the grammar layer handles local constraints, and the semantic layer handles prefix-decidable constraints.\nWe revisit this taxonomy in Section~\\ref{sec:composition} to formalize constraint composition properties.",
  "new_string": "OntoCoDec's two-layer design covers the first two classes: the grammar layer handles local constraints, and the semantic layer handles prefix-decidable constraints."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex",
    "old_string": "OntoCoDec's two-layer design covers the first two classes: the grammar layer handles local constraints, and the semantic layer handles prefix-decidable constraints.\nWe revisit this taxonomy in Section~\\ref{sec:composition} to formalize constraint composition properties.",
    "new_string": "OntoCoDec's two-layer design covers the first two classes: the grammar layer handles local constraints, and the semantic layer handles prefix-decidable constraints."
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T05:57:55.487036+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T05:57:55.487175+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex",
  "old_string": "\\paragraph{Head type masking.}\nAt a \\textsc{HeadType} position within a relation triple, the processor considers two information sources: the entity registry $\\mathcal{D}$ and the current relation type $r_j$ (if already generated).\nIf $h_j \\in \\mathcal{D}$ and the registered type $\\mathcal{D}[h_j] \\in \\operatorname{dom}(r_j)$, the mask allows only that type: $S(t) = \\{\\operatorname{tok}(\\mathcal{D}[h_j])\\}$, ensuring consistency with both the entity list and domain constraints.\nOtherwise, if $r_j$ is known, the mask falls back to all domain-valid head types: $S(t) = \\{\\operatorname{tok}(\\tau) : \\tau \\in \\operatorname{dom}(r_j)\\}$.\nIf $r_j$ is not yet available, no semantic mask is applied and the grammar layer's entity-type membership constraint remains the sole guard.",
  "new_string": "\\paragraph{Head type masking.}\nAt a \\textsc{HeadType} position within a relation triple, the processor considers two information sources: the entity registry $\\mathcal{D}$ and the current relation type $r_j$ (if already generated).\nThree cases arise:\n(1)~\\emph{Match}: $h_j \\in \\mathcal{D}$ and $\\mathcal{D}[h_j] \\in \\operatorname{dom}(r_j)$---the registered type is domain-valid, so the mask allows only that type: $S(t) = \\{\\operatorname{tok}(\\mathcal{D}[h_j])\\}$, ensuring consistency with both the entity list and domain constraints.\n(2)~\\emph{Conflict}: $h_j \\in \\mathcal{D}$ but $\\mathcal{D}[h_j] \\notin \\operatorname{dom}(r_j)$---the entity registry and the relation's domain constraint disagree. This indicates an inconsistency between the entity list and the relation being generated. In this case, the processor prioritizes the ontology's domain constraint and falls back to $S(t) = \\{\\operatorname{tok}(\\tau) : \\tau \\in \\operatorname{dom}(r_j)\\}$, the full set of domain-valid head types.\n(3)~\\emph{Unknown}: $r_j$ is not yet available---no semantic mask is applied and the grammar layer's entity-type membership constraint remains the sole guard."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex",
    "old_string": "\\paragraph{Head type masking.}\nAt a \\textsc{HeadType} position within a relation triple, the processor considers two information sources: the entity registry $\\mathcal{D}$ and the current relation type $r_j$ (if already generated).\nIf $h_j \\in \\mathcal{D}$ and the registered type $\\mathcal{D}[h_j] \\in \\operatorname{dom}(r_j)$, the mask allows only that type: $S(t) = \\{\\operatorname{tok}(\\mathcal{D}[h_j])\\}$, ensuring consistency with both the entity list and domain constraints.\nOtherwise, if $r_j$ is known, the mask falls back to all domain-valid head types: $S(t) = \\{\\operatorname{tok}(\\tau) : \\tau \\in \\operatorname{dom}(r_j)\\}$.\nIf $r_j$ is not yet available, no semantic mask is applied and the grammar layer's entity-type membership constraint remains the sole guard.",
    "new_string": "\\paragraph{Head type masking.}\nAt a \\textsc{HeadType} position within a relation triple, the processor considers two information sources: the entity registry $\\mathcal{D}$ and the current relation type $r_j$ (if already generated).\nThree cases arise:\n(1)~\\emph{Match}: $h_j \\in \\mathcal{D}$ and $\\mathcal{D}[h_j] \\in \\operatorname{dom}(r_j)$---the registered type is domain-valid, so the mask allows only that type: $S(t) = \\{\\operatorname{tok}(\\mathcal{D}[h_j])\\}$, ensuring consistency with both the entity list and domain constraints.\n(2)~\\emph{Conflict}: $h_j \\in \\mathcal{D}$ but $\\mathcal{D}[h_j] \\notin \\operatorname{dom}(r_j)$---the entity registry and the relation's domain constraint disagree. This indicates an inconsistency between the entity list and the relation being generated. In this case, the processor prioritizes the ontology's domain constraint and falls back to $S(t) = \\{\\operatorname{tok}(\\tau) : \\tau \\in \\operatorname{dom}(r_j)\\}$, the full set of domain-valid head types.\n(3)~\\emph{Unknown}: $r_j$ is not yet available---no semantic mask is applied and the grammar layer's entity-type membership constraint remains the sole guard."
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T05:57:55.487382+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T05:57:55.487517+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex",
  "old_string": "When $S(t) \\cap G(t) = \\emptyset$---the semantic layer would mask out all grammar-valid tokens---the system falls back to grammar-only control, preserving structural validity at the cost of a potential type violation.\nThis \\emph{grammar-first invariant} reflects a deliberate priority ordering: structural integrity is a hard constraint, while a type violation is a soft error detectable by downstream validation.\nWe formalize this invariant and analyze constraint composition in detail in Section~\\ref{sec:composition}.",
  "new_string": "When $S(t) \\cap G(t) = \\emptyset$---the semantic layer would mask out all grammar-valid tokens---the system falls back to grammar-only control, preserving structural validity at the cost of a potential type violation.\nThis \\emph{grammar-first fallback} reflects a deliberate priority ordering: structural integrity is a hard constraint, while a type violation is a soft error detectable by downstream validation.\nThis is an engineering robustness mechanism (error recovery), not a formal guarantee: it ensures that tighter semantic constraints never cause the decoder to deadlock, gracefully degrading to grammar-only control when the two layers conflict.\nIn practice, this fallback is rarely triggered: on SciERC (551 sentences) it never activates; on DocRED (998 documents) it triggers once (0.1\\%), consistent with the expectation that tighter constraints increase the probability of empty intersections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex",
    "old_string": "When $S(t) \\cap G(t) = \\emptyset$---the semantic layer would mask out all grammar-valid tokens---the system falls back to grammar-only control, preserving structural validity at the cost of a potential type violation.\nThis \\emph{grammar-first invariant} reflects a deliberate priority ordering: structural integrity is a hard constraint, while a type violation is a soft error detectable by downstream validation.\nWe formalize this invariant and analyze constraint composition in detail in Section~\\ref{sec:composition}.",
    "new_string": "When $S(t) \\cap G(t) = \\emptyset$---the semantic layer would mask out all grammar-valid tokens---the system falls back to grammar-only control, preserving structural validity at the cost of a potential type violation.\nThis \\emph{grammar-first fallback} reflects a deliberate priority ordering: structural integrity is a hard constraint, while a type violation is a soft error detectable by downstream validation.\nThis is an engineering robustness mechanism (error recovery), not a formal guarantee: it ensures that tighter semantic constraints never cause the decoder to deadlock, gracefully degrading to grammar-only control when the two layers conflict.\nIn practice, this fallback is rarely triggered: on SciERC (551 sentences) it never activates; on DocRED (998 documents) it triggers once (0.1\\%), consistent with the expectation that tighter constraints increase the probability of empty intersections."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T05:57:55.487746+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T05:57:55.487917+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "invariant",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "Grep",
  "tool_args": {
    "pattern": "invariant",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T05:57:55.488045+00:00_

&lt;tool_use_error>InputValidationError: Grep failed due to the following issue:
An unexpected parameter `file_path` was provided&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T05:57:55.488164+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "invariant",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "Grep",
  "tool_args": {
    "pattern": "invariant",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T05:57:55.488276+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T05:57:55.488386+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "formalize|revisit this taxonomy",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "Grep",
  "tool_args": {
    "pattern": "formalize|revisit this taxonomy",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/section3_method_draft.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T05:57:55.488536+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T05:57:55.488664+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T05:57:55.488802+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T05:57:55.488929+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T05:57:55.489038+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T05:57:55.489154+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T05:57:55.489263+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T05:57:55.489411+00:00_

`register_artifact` 不在可用工具列表中，跳过注册步骤。

验证结果：

1. **"invariant" 已清除** — 文件中不再出现该词（grep 零匹配）
2. **Head type masking 三路径已覆盖** — Match（registry 与 domain 一致 → 单一类型）、Conflict（registry 与 domain 冲突 → fallback 到 dom(r_j) 全集，优先 ontology）、Unknown（r_j 未知 → 仅 grammar 层）
3. **无 formalize/revisit taxonomy 的承诺** — 第 55 行的 forward reference 已删除；第 11 行改为 "Further discussion...appears in" 而非 "Formal analysis...deferred to"
4. **Fallback 定位为 engineering robustness** — "grammar-first fallback"，明确标注为 error recovery 而非 formal guarantee，附 SciERC/DocRED 触发率数据

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_section3_method_warnings_fix_20260514T055617"
}
```

</details>

---
