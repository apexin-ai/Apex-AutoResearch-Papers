# writing related work snapkv nacl

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_writing_related-work-snapkv-nacl_20260514T055834.jsonl`
- **Structured JSON:** [`805327fbfee8fbcd2c37.json`](../../sessions/80/805327fbfee8fbcd2c37.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-14T06:00:12.072567+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T06:00:12.074028+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Compound and Joint Compression}
5	
6	Combining multiple compression axes produces non-additive errors.
7	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction, with up to 65\% quality loss exceeding individual component effects---the first explicit measurement of this phenomenon in KV cache sparsity.
8	\cite{slim-icml2025} formalize compound error for quantization and sparsity, deriving an invertible saliency function for low-rank compensation and confirming that aggregated error is strictly non-additive.
9	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning and multilingual capabilities degrade disproportionately relative to factual recall.
10	The order of compression stages is itself consequential: \cite{compression-ordering-2025} show that early quantization causes irreversible information loss, making P$\to$KD$\to$Q strictly preferable.
11	At a more fundamental level, \cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying that the joint safe region is the intersection---not the union---of per-dimension safe zones.
12	On the structural side, GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates to jointly prune FFN channels and attention heads, but treats the pruning decision as static across generation.
13	These works share a common assumption: compound interaction is either uniform across the generation process or varies only by task.
14	None examines how the interaction shifts across reasoning phases within a single generation.
15	
16	\subsection{KV Cache Eviction}
17	
18	Most eviction methods rely on importance scoring, yet accumulating evidence questions its reliability.
19	Ada-KV~\cite{adakv-neurips2025} introduce per-head adaptive budget allocation, outperforming uniform distribution but assuming stable impo
…[truncated 3018 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T06:00:12.074374+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T06:00:12.074632+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T06:00:12.074866+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SnapKV KV cache compression eviction paper 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SnapKV KV cache compression eviction paper 2024"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T06:00:12.075082+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NACL KV cache eviction paper 2024 LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NACL KV cache eviction paper 2024 LLM"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T06:00:12.075354+00:00_

Web search results for query: "SnapKV KV cache compression eviction paper 2024"

Links: [{"title":"SnapKV: LLM Knows What You Are Looking for before Generation Yuhong Li1∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/28ab418242603e0f7323e54185d19bde-Paper-Conference.pdf"},{"title":"SnapKV: LLM Knows What You are Looking for Before Generation Yuhong Li1∗","url":"https://arxiv.org/pdf/2404.14469"},{"title":"SnapKV : LLM Knows What You are Looking for Before Generation","url":"https://arxiv.org/html/2404.14469v1"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget ...","url":"https://arxiv.org/pdf/2407.11550"},{"title":"SnapKV: LLM Knows What You are Looking for Before Generation | OpenReview","url":"https://openreview.net/forum?id=poE54GOq2l"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Preprint THE PITFALLS OF KV CACHE COMPRESSION","url":"https://arxiv.org/pdf/2510.00231"},{"title":"KV Cache Compression, But What Must We Give in Return ...","url":"https://aclanthology.org/2024.findings-emnlp.266.pdf"},{"title":"Published as preprint paper G-KV: DECODING-TIME KV CACHE EVICTION WITH","url":"https://arxiv.org/pdf/2512.00504"},{"title":"Paper page - SnapKV: LLM Knows What You are Looking for Before Generation","url":"https://huggingface.co/papers/2404.14469"}]

Based on the search results, I found comprehensive information about the SnapKV paper on KV cache compression and eviction from 2024.

## SnapKV: LLM Knows What You are Looking for Before Generation

SnapKV is an innovative and fine-tuning-free approach that efficiently minimizes KV cache size while still delivering comparable performance in real-world applications.

### Key
…[truncated 1341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T06:00:12.078893+00:00_

Web search results for query: "NACL KV cache eviction paper 2024 LLM"

Links: [{"title":"NACL: A General and Effective KV Cache Eviction Framework for LLM at Inference Time - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.428/"},{"title":"NACL: A General and Effective KV Cache Eviction ...","url":"https://aclanthology.org/2024.acl-long.428.pdf"},{"title":"[2408.03675] NACL: A General and Effective KV Cache Eviction Framework for LLMs at Inference Time","url":"https://arxiv.org/abs/2408.03675"},{"title":"NaCl: A General and Effective KV Cache Eviction Framework for LLMs at Inference Time","url":"https://arxiv.org/html/2408.03675v1"},{"title":"NACL: A General and Effective KV Cache Eviction Framework for LLMs at Inference Time | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/nacl-general-effective-kv-cache-eviction-framework"},{"title":"NACL: A General and Effective KV Cache Eviction ...","url":"https://www.emergentmind.com/papers/2408.03675"},{"title":"Paper page - NACL: A General and Effective KV Cache Eviction Framework for LLMs at Inference Time","url":"https://huggingface.co/papers/2408.03675"},{"title":"NACL: A Robust KV Cache Eviction Framework for Efficient Long-Text Processing in LLMs - MarkTechPost","url":"https://www.marktechpost.com/2024/08/12/nacl-a-robust-kv-cache-eviction-framework-for-efficient-long-text-processing-in-llms/"},{"title":"NACL: A General and Effective KV Cache Eviction Framework for LLM at Inference Time | Request PDF","url":"https://www.researchgate.net/publication/384207931_NACL_A_General_and_Effective_KV_Cache_Eviction_Framework_for_LLM_at_Inference_Time"},{"title":"(PDF) NACL: A General and Effective KV Cache Eviction Framework for LLMs at Inference Time","url":"https://www.researchgate.net/publication/382943980_NACL_A_General_and_Effective_KV_Cache_Eviction_Framework_for_LLMs_at_Inference_Time"}]

Based on the search results, here's what I found about the NACL KV cache eviction paper:

## NACL: 
…[truncated 1295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T06:00:12.079226+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SnapKV paper authors full list Yuhong Li NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SnapKV paper authors full list Yuhong Li NeurIPS 2024"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T06:00:12.079537+00:00_

Web search results for query: "SnapKV paper authors full list Yuhong Li NeurIPS 2024"

Links: [{"title":"SnapKV: LLM Knows What You Are Looking for before Generation Yuhong Li1∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/28ab418242603e0f7323e54185d19bde-Paper-Conference.pdf"},{"title":"SnapKV: LLM Knows What You are Looking for Before Generation","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/28ab418242603e0f7323e54185d19bde-Abstract-Conference.html"},{"title":"NeurIPS Poster SnapKV: LLM Knows What You are Looking for Before Generation","url":"https://neurips.cc/virtual/2024/poster/93531"},{"title":"SnapKV: LLM Knows What You are Looking for Before Generation [Quick Review]","url":"https://liner.com/review/snapkv-llm-knows-what-you-are-looking-for-before-generation"},{"title":"[PDF] SnapKV: LLM Knows What You are Looking for Before Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SnapKV:-LLM-Knows-What-You-are-Looking-for-Before-Li-Huang/1784c987e681d60c634765fe64c8d9c26f73d5ff"},{"title":"NeurIPS 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/neurips-paper-list/neurips-2024-paper-list/"},{"title":"NeurIPS 2024 Accepted Paper List: Datasets & Benchmarks Track - Paper Copilot","url":"https://papercopilot.com/paper-list/neurips-paper-list/neurips-2024-paper-list-datasets-benchmarks-track/"},{"title":"Paper Digest: NeurIPS 2024 Papers & Highlights – Resources | Paper Digest","url":"https://resources.paperdigest.org/2024/10/neurips-2024-highlights/"},{"title":"Yuhong Li","url":"https://scholar.google.com/citations?user=Qh-6mV8AAAAJ&hl=en"},{"title":"NeurIPS 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/neurips-paper-list/neurips-2025-paper-list/"}]

Based on the search results, I found the full author list for the SnapKV paper at NeurIPS 2024. The authors are: Yuhong Li, Yingbing Huang, Bowen Yang, Bharat Venkitesh, Acyr F. L
…[truncated 168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T06:00:12.079910+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex",
  "old_string": "Ada-KV~\\cite{adakv-neurips2025} introduce per-head adaptive budget allocation, outperforming uniform distribution but assuming stable importance across generation.\n\\cite{defensivekv-iclr2026} show",
  "new_string": "Ada-KV~\\cite{adakv-neurips2025} introduce per-head adaptive budget allocation, outperforming uniform distribution but assuming stable importance across generation.\nSnapKV~\\cite{snapkv-neurips2024} identifies important KV positions per head from an observation window at the end of the prompt, compressing the cache before generation begins---effective for long contexts but committing to a fixed importance snapshot that cannot adapt across reasoning phases.\n\\cite{defensivekv-iclr2026} show"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex",
    "old_string": "Ada-KV~\\cite{adakv-neurips2025} introduce per-head adaptive budget allocation, outperforming uniform distribution but assuming stable importance across generation.\n\\cite{defensivekv-iclr2026} show",
    "new_string": "Ada-KV~\\cite{adakv-neurips2025} introduce per-head adaptive budget allocation, outperforming uniform distribution but assuming stable importance across generation.\nSnapKV~\\cite{snapkv-neurips2024} identifies important KV positions per head from an observation window at the end of the prompt, compressing the cache before generation begins---effective for long contexts but committing to a fixed importance snapshot that cannot adapt across reasoning phases.\n\\cite{defensivekv-iclr2026} show"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T06:00:12.080192+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T06:00:12.082468+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex",
  "old_string": "\\cite{defensivekv-iclr2026} show that standard mean-based importance aggregation is fragile, with worst-case quality loss 2.3--4.3$\\times$ higher than expected; their defensive aggregation mitigates but does not eliminate the instability.\n\\cite{obcache-2025}",
  "new_string": "\\cite{defensivekv-iclr2026} show that standard mean-based importance aggregation is fragile, with worst-case quality loss 2.3--4.3$\\times$ higher than expected; their defensive aggregation mitigates but does not eliminate the instability.\n\\cite{nacl-acl2024} combine proxy-token eviction with random eviction to counteract attention bias, improving robustness over pure importance-based methods; yet the eviction policy remains uniform throughout generation.\n\\cite{obcache-2025}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex",
    "old_string": "\\cite{defensivekv-iclr2026} show that standard mean-based importance aggregation is fragile, with worst-case quality loss 2.3--4.3$\\times$ higher than expected; their defensive aggregation mitigates but does not eliminate the instability.\n\\cite{obcache-2025}",
    "new_string": "\\cite{defensivekv-iclr2026} show that standard mean-based importance aggregation is fragile, with worst-case quality loss 2.3--4.3$\\times$ higher than expected; their defensive aggregation mitigates but does not eliminate the instability.\n\\cite{nacl-acl2024} combine proxy-token eviction with random eviction to counteract attention bias, improving robustness over pure importance-based methods; yet the eviction policy remains uniform throughout generation.\n\\cite{obcache-2025}"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T06:00:12.082859+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T06:00:12.083090+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex",
  "old_string": "No prior work examines the interaction between eviction \\emph{strategy} and reasoning phase in compound sparsity settings---the gap our study addresses.",
  "new_string": "To our knowledge, no prior work examines the interaction between eviction \\emph{strategy} and reasoning phase in compound sparsity settings---the gap our study addresses."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex",
    "old_string": "No prior work examines the interaction between eviction \\emph{strategy} and reasoning phase in compound sparsity settings---the gap our study addresses.",
    "new_string": "To our knowledge, no prior work examines the interaction between eviction \\emph{strategy} and reasoning phase in compound sparsity settings---the gap our study addresses."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T06:00:12.083316+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T06:00:12.083660+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T06:00:12.083934+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Compound and Joint Compression}
5	
6	Combining multiple compression axes produces non-additive errors.
7	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction, with up to 65\% quality loss exceeding individual component effects---the first explicit measurement of this phenomenon in KV cache sparsity.
8	\cite{slim-icml2025} formalize compound error for quantization and sparsity, deriving an invertible saliency function for low-rank compensation and confirming that aggregated error is strictly non-additive.
9	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning and multilingual capabilities degrade disproportionately relative to factual recall.
10	The order of compression stages is itself consequential: \cite{compression-ordering-2025} show that early quantization causes irreversible information loss, making P$\to$KD$\to$Q strictly preferable.
11	At a more fundamental level, \cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying that the joint safe region is the intersection---not the union---of per-dimension safe zones.
12	On the structural side, GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates to jointly prune FFN channels and attention heads, but treats the pruning decision as static across generation.
13	These works share a common assumption: compound interaction is either uniform across the generation process or varies only by task.
14	None examines how the interaction shifts across reasoning phases within a single generation.
15	
16	\subsection{KV Cache Eviction}
17	
18	Most eviction methods rely on importance scoring, yet accumulating evidence questions its reliability.
19	Ada-KV~\cite{adakv-neurips2025} introduce per-head adaptive budget allocation, outperforming uniform distribution but assuming stable impo
…[truncated 3557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-14T06:00:12.084242+00:00_

文件已更新完毕。以下是修改总结和 BibTeX 条目：

**修改内容：**
- L20: 插入 SnapKV（NeurIPS 2024）——基于 observation window 的 per-head KV 选择，一次性快照无法跨 phase 调整
- L22: 插入 NACL（ACL 2024）——proxy-token + random eviction 对抗 attention bias，但 policy 全程不变
- L39: gap statement 从 "No prior work" 软化为 "To our knowledge, no prior work"

**BibTeX 条目：**

```bibtex
@inproceedings{snapkv-neurips2024,
  title     = {{SnapKV}: {LLM} Knows What You Are Looking for Before Generation},
  author    = {Li, Yuhong and Huang, Yingbing and Yang, Bowen and Venkitesh, Bharat and Locatelli, Acyr and Ye, Hanchen and Cai, Tianle and Lewis, Patrick and Chen, Deming},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2024}
}

@inproceedings{nacl-acl2024,
  title     = {{NACL}: A General and Effective {KV} Cache Eviction Framework for {LLMs} at Inference Time},
  author    = {Chen, Yilong and Wang, Guoxia and Shang, Junyuan and Cui, Shiyao and Zhang, Zhenyu and Liu, Tingwen and Wang, Shuohuan and Sun, Yu and Yu, Dianhai and Wu, Hua},
  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},
  year      = {2024}
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_related-work-snapkv-nacl_20260514T055834"
}
```

</details>

---
