# paper writing abstract

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_paper_writing_abstract_20260515T191020.jsonl`
- **Structured JSON:** [`be06f4a3c455ef031604.json`](../../sessions/be/be06f4a3c455ef031604.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-15T19:11:29.405831+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260515T191020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T19:11:29.406254+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations---near halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combination---accounts for the observed gains. More broadly, all prior approaches conflate two dis
…[truncated 6382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260515T191020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T19:11:29.406445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260515T191020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T19:11:29.406602+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented a controlled empirical study isolating the factors behind schema-induced degradation in training-free LLM information extraction. Our experiments across NER, RE, and ED reveal that degradation operates through two orthogonal channels: a count channel, where increasing the number of candidate types suppresses recall, and a confusability channel, where semantically similar types trigger intra-batch substitution errors. These channels are mechanistically distinct---the first reflects capacity limitations as types compete for attention, the second reflects semantic indistinguishability regardless of schema size.
5	
6	Pairwise type confusability, quantified by the Schema Confusability Score, is a partial but robust predictor of type confusion. The signal is modest in magnitude ($r^2 \approx 1.3\text{--}1.7\%$), yet it replicates across three tasks, two embedding spaces, and survives bootstrap resampling---making it the first factor to be empirically isolated in controlled zero-shot IE experiments. Entity frequency, prompt position, and type definition quality account for the remaining variance; disentangling these factors is an open problem. We further identify a centrality confound that reverses per-type aggregation on same-domain schemas, a methodological finding relevant to any embedding-based schema analysis.
7	
8	Our Schema-DAG-Guided Decomposition experiments yield an informative negative result: separating confusable types into different batches does not improve extraction, because merge amplification destroys precision across all decomposition strategies. This structural bottleneck applies broadly to decompose-then-merge pipelines.
9	
10	Several limitations bound our findings. All experiments use a single model (Qwen3-32B); multi-model validation is an immediate priority. Future work should address the merge bottleneck directly---calibration-based cross-batch consistency, joint decoding over decomp
…[truncated 134 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260515T191020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T19:11:29.406782+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex 2>/dev/null; echo \"EXIT:$?\"",
  "description": "Check if abstract.tex exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260515T191020",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex 2>/dev/null; echo \"EXIT:$?\"",
    "description": "Check if abstract.tex exists"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T19:11:29.406974+00:00_

EXIT:2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260515T191020",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T19:11:29.407191+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
  "content": "\\begin{abstract}\nTraining-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\\% to 50.4\\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms behind this degradation unclear. We conduct the first controlled empirical study that isolates type confusability from type count across three IE tasks (NER, RE, event detection) and three datasets. We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic overlap between types and design two complementary experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two orthogonal degradation channels: a count channel that suppresses recall in NER and RE as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors. Pairwise SCS predicts type confusion across tasks (Pearson $r = 0.112$--$0.129$, $r^2 \\approx 0.013$--$0.017$)---modest in magnitude but the first factor empirically isolated in controlled zero-shot IE experiments. Confusability effects amplify $3.4\\times$ as schema size grows from 16 to 80 types, with accuracy gaps widening from 9.1 to 31.2 percentage points. We further identify a centrality confound that reverses per-type confusability aggregation on homogeneous schemas while the pairwise signal remains intact. Our confusability-aware decomposition (SDGD) yields an informative negative result: merge amplification destroys precision across all decomposition strategies, revealing a structural bottleneck for decompose-then-merge pipelines. These findings carry practical implications for schema design and identify merge amplification as the key obstacle for decomposition approaches in zero-shot IE.\n\\end{abstract}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_20260515T191020",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
    "content": "\\begin{abstract}\nTraining-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\\% to 50.4\\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms behind this degradation unclear. We conduct the first controlled empirical study that isolates type confusability from type count across three IE tasks (NER, RE, event detection) and three datasets. We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic overlap between types and design two complementary experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two orthogonal degradation channels: a count channel that suppresses recall in NER and RE as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors. Pairwise SCS predicts type confusion across tasks (Pearson $r = 0.112$--$0.129$, $r^2 \\approx 0.013$--$0.017$)---modest in magnitude but the first factor empirically isolated in controlled zero-shot IE experiments. Confusability effects amplify $3.4\\times$ as schema size grows from 16 to 80 types, with accuracy gaps widening from 9.1 to 31.2 percentage points. We further identify a centrality confound that reverses per-type confusability aggregation on homogeneous schemas while the pairwise signal remains intact. Our confusability-aware decomposition (SDGD) yields an informative negative result: merge amplification destroys precision across all decomposition strategies, revealing a structural bottleneck for decompose-then-merge pipelines. These findings carry practical implications for schema design and identify merge amplification as the key obstacle for decomposition approaches in zero-shot IE.\n\\end{abstract}\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T19:11:29.407342+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_20260515T191020",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-15T19:11:29.407523+00:00_

已写入 `abstract.tex`。约 260 words，覆盖全部 5 个元素。数字核对：

| 指标 | Abstract | §1 一致性 |
|------|----------|-----------|
| NER recall 0.72→0.42 | ✓ | ✓ |
| RE accuracy 85.7%→50.4% | ✓ | ✓ |
| r = 0.112–0.129 | ✓ | ✓ |
| r² ≈ 0.013–0.017 | ✓ (DR2 fix) | ✓ |
| 3.4× amplification, 9.1→31.2 pp | ✓ | ✓ |
| Count degradation限定NER and RE | ✓ | ✓ |
| 无 \cite、无禁用词 | ✓ | — |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_abstract_20260515T191020"
}
```

</details>

---
