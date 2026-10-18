# research wang fla version

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 230
- **Recorded user turns:** 0
- **Tool calls:** 114
- **Original source:** `logs/chats/worker_research_wang-fla-version_20260518T122417.jsonl`
- **Structured JSON:** [`ce368333aa8e1b4fde00.json`](../../sessions/ce/ce368333aa8e1b4fde00.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

230 recorded events

### Tool call

_source line 1 · 2026-05-18T12:29:38.867364+00:00_

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
  "session": "worker_research_wang-fla-version_20260518T122417",
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

_source line 2 · 2026-05-18T12:29:38.867721+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T12:29:38.867906+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang et al \"Systematic Analysis of Hybrid Linear Attention\" github requirements flash-linear-attention version"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang et al \"Systematic Analysis of Hybrid Linear Attention\" github requirements flash-linear-attention version"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T12:29:38.868040+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com fla-org flash-linear-attention releases tags"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com fla-org flash-linear-attention releases tags"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T12:29:38.868159+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:huggingface.co m-a-p hybrid linear attention 1.3B flash-linear-attention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:huggingface.co m-a-p hybrid linear attention 1.3B flash-linear-attention"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T12:29:38.868274+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "pypi flash-linear-attention version history"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "pypi flash-linear-attention version history"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T12:29:38.868445+00:00_

Web search results for query: "Wang et al "Systematic Analysis of Hybrid Linear Attention" github requirements flash-linear-attention version"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/html/2507.06457v1"},{"title":"[2507.06457] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457"},{"title":"[PDF] A Systematic Analysis of Hybrid Linear Attention | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Systematic-Analysis-of-Hybrid-Linear-Attention-Wang-Zhu/f7ad9ebc481e23ae7fa90d98d3814518e94adcd1"},{"title":"[2507.06457v1] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457v1"},{"title":"Paper page - A Systematic Analysis of Hybrid Linear Attention","url":"https://huggingface.co/papers/2507.06457"},{"title":"Linear Attention Fundamentals | Hailey Schoelkopf","url":"https://haileyschoelkopf.github.io/blog/2024/linear-attn/"},{"title":"(PDF) A Systematic Analysis of Hybrid Linear Attention","url":"https://www.researchgate.net/publication/393538945_A_Systematic_Analysis_of_Hybrid_Linear_Attention"},{"title":"Linear Attention Variants Overview","url":"https://www.emergentmind.com/topics/linear-attention-variants"},{"title":"A Systematic Analysis of Hybrid Linear Attention | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/systematic-analysis-hybrid-linear-attention"}]

Based on the search results, I found information about the Wang et al. paper on "A Systematic Analysis of Hybrid Linear Attention" and its connection to the flash-linear-attention library.

## Key Findings:

**Paper Details:**
The paper trained and open-sourced 72 models: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention var
…[truncated 889 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T12:29:38.868670+00:00_

Web search results for query: "site:github.com fla-org flash-linear-attention releases tags"

Links: [{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"},{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"GitHub - Fzkuji/flash-linear: 🚀 Efficient implementations of state-of-the-art linear attention models in Pytorch and Triton","url":"https://github.com/Fzkuji/flash-linear-attention"},{"title":"Home · fla-org/flash-linear-attention Wiki · GitHub","url":"https://github.com/fla-org/flash-linear-attention/wiki"},{"title":"flash-linear-attention/README.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/README.md"},{"title":"flash-linear-attention/fla/ops/cp/README.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/fla/ops/cp/README.md"},{"title":"GitHub - fla-org/fla-zoo: Flash-Linear-Attention models beyond language · GitHub","url":"https://github.com/fla-org/fla-zoo"},{"title":"release · Workflow runs · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/actions/workflows/release.yml"},{"title":"Activity · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/activity"},{"title":"flash-linear-attention/FAQs.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/FAQs.md"}]

I found the search results for the `fla-org/flash-linear-attention` repository's releases and tags. Here's what I discovered:

**Latest Release:**
The latest release is v0.5.0, with the main new model being MoBA / FlashMoBA, which brings Moonshot's Mixture of Block Attention into the fla family. This release was published on April 21, 2025.

**Key Features 
…[truncated 806 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T12:29:38.868911+00:00_

Web search results for query: "pypi flash-linear-attention version history"

Links: [{"title":"flash-linear-attention · PyPI","url":"https://pypi.org/project/flash-linear-attention/"},{"title":"piwheels - flash-linear-attention","url":"https://www.piwheels.org/project/flash-linear-attention/"},{"title":"flash-attn · PyPI","url":"https://pypi.org/project/flash-attn/"},{"title":"flash-linear-attention Changelog","url":"https://data.safetycli.com/packages/pypi/flash-linear-attention/changelog"},{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"RWKV-FLA User Guide","url":"https://wiki.rwkv.com/advance/RWKV-FLA.html"},{"title":"piwheels - fla-core","url":"https://www.piwheels.org/project/fla-core/"},{"title":"flash-linear-attention/FAQs.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/FAQs.md"},{"title":"FLASH-pytorch · PyPI","url":"https://pypi.org/project/FLASH-pytorch/"},{"title":"flash-attn-4 · PyPI","url":"https://pypi.org/project/flash-attn-4/"}]

Based on the search results, here's information about the flash-linear-attention PyPI package version history:

## Package Overview
The repository provides efficient implementations for emerging model architectures, with a focus on efficient sequence modeling (e.g., linear attention, state space models, and their hybrids).

## Package Structure
Starting from v0.3.2, the packages published on PyPI are fla-core and flash-linear-attention. The former contains all customized kernels and only depends on PyTorch, Triton, and einops. The latter is an extension package of the former, containing fla/layers and fla/models, and depends on transformers.

## Recent Updates
The search results show several recent features and updates, including:
- MoBA (Mixture of Block Attention) implementation with FlashMoBA backend support (2026-04)
- Context
…[truncated 637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T12:29:38.869111+00:00_

Web search results for query: "site:huggingface.co m-a-p hybrid linear attention 1.3B flash-linear-attention"

Links: [{"title":"Hybrid Linear Attention Research - a m-a-p Collection","url":"https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research"},{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"Paper page - A Systematic Analysis of Hybrid Linear Attention","url":"https://huggingface.co/papers/2507.06457"},{"title":"(PDF) A Systematic Analysis of Hybrid Linear Attention","url":"https://www.researchgate.net/publication/393538945_A_Systematic_Analysis_of_Hybrid_Linear_Attention"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/html/2507.06457v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=linear+attention"},{"title":"m-a-p/transformer_340M_baseline · Hugging Face","url":"https://huggingface.co/m-a-p/transformer_340M_baseline"},{"title":"ByteDance conducted the Hybrid Linear Attention Research They systematically evaluated various linear attention models within hybrid architectures, revealing that superior standalone linear models do not necessarily lead to better performance in hybrid configurations.","url":"https://www.threads.com/@sung.kim.mw/post/DOJBMCIkVWH/bytedance-conducted-the-hybrid-linear-attention-researchthey-systematically-eval"},{"title":"hustvl/InfiniteVL · Hugging Face","url":"https://huggingface.co/hustvl/InfiniteVL"},{"title":"inclusionAI/Ling-2.5-1T · Hugging Face","url":"https://huggingface.co/inclusionAI/Ling-2.5-1T"}]

Based on the search results, I found relevant information about the m-a-p hybrid linear attention research with 1.3B models using flash-linear-attention:

The m-a-p collection includes all 1.3B & 340M hybrid linear-attention experiments. This research represents a comprehensive study on hybrid linear attention a
…[truncated 928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T12:29:38.869295+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com m-a-p \"hybrid-linear-attention\" OR \"hybrid_linear_attention\" training code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com m-a-p \"hybrid-linear-attention\" OR \"hybrid_linear_attention\" training code"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T12:29:38.869422+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "flash-linear-attention 0.5.0 breaking changes GatedDeltaNet \"attn.D\" migration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "flash-linear-attention 0.5.0 breaking changes GatedDeltaNet \"attn.D\" migration"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T12:29:38.869540+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com fla-org flash-linear-attention \"0.4\" OR \"v0.4\" release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com fla-org flash-linear-attention \"0.4\" OR \"v0.4\" release"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T12:29:38.869735+00:00_

Web search results for query: "site:github.com fla-org flash-linear-attention "0.4" OR "v0.4" release"

Links: [{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"},{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"release · Workflow runs · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/actions/workflows/release.yml"},{"title":"Home · fla-org/flash-linear-attention Wiki · GitHub","url":"https://github.com/fla-org/flash-linear-attention/wiki"},{"title":"Commits · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/commits/main"},{"title":"flash-linear-attention/README.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/README.md"},{"title":"GitHub - Fzkuji/flash-linear: 🚀 Efficient implementations of state-of-the-art linear attention models in Pytorch and Triton","url":"https://github.com/Fzkuji/flash-linear-attention"},{"title":"flash-linear-attention/fla/layers/gla.py at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/fla/layers/gla.py"},{"title":"FLA-org","url":"https://github.com/fla-org"},{"title":"flash-linear-attention/fla/ops/cp/README.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/fla/ops/cp/README.md"}]

Based on the search results, I found information about the v0.4.0 release of the flash-linear-attention project:

v0.4.0 includes improvements such as Kimi Delta Attention, fixes for GDN tiling bugs, comprehensive docstrings for Conv operations with a change to Triton as the default backend, cumsum dimension correction in normalize_output, autotune caching support for Triton kernels, the addition of a De
…[truncated 287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T12:29:38.869946+00:00_

Web search results for query: "flash-linear-attention 0.5.0 breaking changes GatedDeltaNet "attn.D" migration"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"},{"title":"[Bug] Flash Attention crashes with `illegal memory access` on Qwen3.5 due to 3D `position_ids` being misinterpreted as packed sequence · Issue #104 · QwenLM/Qwen3.6","url":"https://github.com/QwenLM/Qwen3.6/issues/104"},{"title":"[Bug]: Gated DeltaNet Recurrence with constant Gate at 1 vs. DeltaNet Recurrence · Issue #104 · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/issues/104"},{"title":"[Bug] GatedDeltaNet backward error on Blackwell · Issue #607 · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/issues/607"},{"title":"Releases · Dao-AILab/flash-attention","url":"https://github.com/Dao-AILab/flash-attention/releases"},{"title":"Flash Attention Explained: A Comprehensive Guide | DataCamp","url":"https://www.datacamp.com/blog/flash-attention"},{"title":"GitHub - Fzkuji/flash-linear: 🚀 Efficient implementations of state-of-the-art linear attention models in Pytorch and Triton","url":"https://github.com/Fzkuji/flash-linear-attention"},{"title":"Gated DeltaNet: Adaptive Fast-Weight Model","url":"https://www.emergentmind.com/topics/gated-deltanet"},{"title":"Gated DeltaNet | Sebastian Raschka, PhD","url":"https://sebastianraschka.com/llms-from-scratch/ch04/08_deltanet/"}]

Based on the search results, I found some relevant information about flash-linear-attention and GatedDeltaNet, though the specific details about version 0.5.0 breaking changes and "attn.D" migration aren't fully detailed in these results.

Here's what I found:

Gated DeltaNet implementation was added t
…[truncated 992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T12:29:38.870143+00:00_

Web search results for query: "site:github.com m-a-p "hybrid-linear-attention" OR "hybrid_linear_attention" training code"

Links: [{"title":"GitHub - thunlp/hybrid-linear-attention: Code and models for the paper: Hybrid Linear Attention Done Right: Efficient Distillation and Effective Architectures for Extremely Long Contexts · GitHub","url":"https://github.com/thunlp/hybrid-linear-attention"},{"title":"GitHub - MoonshotAI/Kimi-Linear · GitHub","url":"https://github.com/MoonshotAI/Kimi-Linear"},{"title":"GitHub - idiap/hybrid-linear-sparse-attention: Alleviating Forgetfulness of Linear Attention by Hybrid Sparse Attention and Contextualized Learnable Token Eviction.","url":"https://github.com/idiap/hybrid-linear-sparse-attention"},{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"GitHub - mrlonely426/ECTTrack: Efficient Hybrid Linear Self-Attention based Visual Object Tracking with LoRA · GitHub","url":"https://github.com/mrlonely426/ECTTrack"},{"title":"GitHub - yedizhang/linattn-icl: [ICML 2025 Spotlight] Training Dynamics of In-Context Learning in Linear Attention.","url":"https://github.com/yedizhang/linattn-icl"},{"title":"GitHub - OpenNLPLab/LASP: Linear Attention Sequence Parallelism (LASP) · GitHub","url":"https://github.com/OpenNLPLab/LASP"},{"title":"GitHub - HazyResearch/based: Code for exploring Based models from \"Simple linear attention language models balance the recall-throughput tradeoff\" · GitHub","url":"https://github.com/HazyResearch/based"},{"title":"Gated DeltaNet for Linear Attention - rasbt/LLMs-from-scratch","url":"https://github.com/rasbt/LLMs-from-scratch/blob/main/ch04/08_deltanet/README.md"},{"title":"GitHub - lucidrains/linear-attention-transformer: Transformer based on a variant of attention that is linear complexity in respect to sequence length · GitHub","url":"https://github.com/lucidrains/linear-atte
…[truncated 2003 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T12:29:38.870329+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "github.com fla-org flash-linear-attention releases v0.4.0 v0.4.1 v0.4.2 changelog"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "github.com fla-org flash-linear-attention releases v0.4.0 v0.4.1 v0.4.2 changelog"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T12:29:38.870455+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2507.06457 \"hybrid linear attention\" github code repository training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2507.06457 \"hybrid linear attention\" github code repository training"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T12:29:38.870571+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com fla-org flash-linear-attention GatedDeltaNet \"A_log\" OR \"attn.D\" rename parameter change"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com fla-org flash-linear-attention GatedDeltaNet \"A_log\" OR \"attn.D\" rename parameter change"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T12:29:38.870739+00:00_

Web search results for query: "github.com fla-org flash-linear-attention releases v0.4.0 v0.4.1 v0.4.2 changelog"

Links: [{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"},{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"Releases · Dao-AILab/flash-attention","url":"https://github.com/Dao-AILab/flash-attention/releases"},{"title":"flash-linear-attention Changelog","url":"https://data.safetycli.com/packages/pypi/flash-linear-attention/changelog"},{"title":"GitHub - Fzkuji/flash-linear: 🚀 Efficient implementations of state-of-the-art linear attention models in Pytorch and Triton","url":"https://github.com/Fzkuji/flash-linear-attention"},{"title":"Commits · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/commits/main"},{"title":"flash-linear-attention · PyPI","url":"https://pypi.org/project/flash-linear-attention/"},{"title":"Releases · mjun0812/flash-attention-prebuild-wheels","url":"https://github.com/mjun0812/flash-attention-prebuild-wheels/releases"},{"title":"Releases · loscrossos/lib_flashattention","url":"https://github.com/loscrossos/lib_flashattention/releases"},{"title":"flash-linear-attention/FAQs.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/FAQs.md"}]

Based on the search results from the fla-org/flash-linear-attention GitHub releases page, I found information about the versions you requested:

## v0.4.2

The v0.4.2 release includes: [Misc] Use autopep8 to keep style, [Misc] Reduce D2H/H2D Sync, [Conv]: Support mix mode(Triton fwd and CUDA bwd), [Test] Add memory guard fixtures for CUDA memory safety testing, [KDA] Add lowerbound gate function, and [KDA] Remove deprecated head_first in kda gate func.

## v0.4.0 and v0.4.1

The search results mention t
…[truncated 467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T12:29:38.870921+00:00_

Web search results for query: "arXiv 2507.06457 "hybrid linear attention" github code repository training"

Links: [{"title":"[2507.06457] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/html/2507.06457"},{"title":"[2507.06457v1] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457v1"},{"title":"Paper page - A Systematic Analysis of Hybrid Linear Attention","url":"https://huggingface.co/papers/2507.06457"},{"title":"Hybrid Linear Attention Done Right: Efficient Distillation ...","url":"https://arxiv.org/pdf/2601.22156"},{"title":"(PDF) A Systematic Analysis of Hybrid Linear Attention","url":"https://www.researchgate.net/publication/393538945_A_Systematic_Analysis_of_Hybrid_Linear_Attention"},{"title":"Alleviating Forgetfulness of Linear Attention by Hybrid ...","url":"https://arxiv.org/pdf/2510.20787"},{"title":"A Systematic Analysis of Hybrid Linear Attention | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/systematic-analysis-hybrid-linear-attention"},{"title":"Alleviating Forgetfulness of Linear Attention by Hybrid Sparse Attention and Contextualized Learnable Token Eviction","url":"https://arxiv.org/html/2510.20787v2"},{"title":"Hybrid Linear Attention Done Right: Efficient Distillation and Effective Architectures for Extremely Long Contexts","url":"https://arxiv.org/html/2601.22156v1"}]

Based on the search results, I found information about arXiv paper 2507.06457 titled "A Systematic Analysis of Hybrid Linear Attention."

## Overview

The paper systematically evaluates various linear attention models across generations both standalone and hybridized, and trained and open-sourced 72 models: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios.

## Key Findings

Benchmarking on sta
…[truncated 1087 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T12:29:38.871144+00:00_

Web search results for query: "site:github.com fla-org flash-linear-attention GatedDeltaNet "A_log" OR "attn.D" rename parameter change"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"},{"title":"GitHub - Fzkuji/flash-linear: 🚀 Efficient implementations of state-of-the-art linear attention models in Pytorch and Triton","url":"https://github.com/Fzkuji/flash-linear-attention"},{"title":"Linear Attention Models (GLA, Delta Net) | fla-org/flame | DeepWiki","url":"https://deepwiki.com/fla-org/flame/7.3-linear-attention-models-(gla-delta-net)"},{"title":"flash-linear-attention · PyPI","url":"https://pypi.org/project/flash-linear-attention/"},{"title":"flash-linear-attention/fla/layers/delta_net.py at main · fla-org/flash-linear-attention","url":"https://github.com/sustcsonglin/flash-linear-attention/blob/main/fla/layers/delta_net.py"},{"title":"GitHub - NVlabs/GatedDeltaNet: [ICLR 2025] Official PyTorch Implementation of Gated Delta Networks: Improving Mamba2 with Delta Rule · GitHub","url":"https://github.com/NVlabs/GatedDeltaNet"},{"title":"Home · fla-org/flash-linear-attention Wiki · GitHub","url":"https://github.com/fla-org/flash-linear-attention/wiki"},{"title":"flash-linear-attention/fla/ops/cp/README.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/fla/ops/cp/README.md"},{"title":"GitHub - fla-org/fla-zoo: Flash-Linear-Attention models beyond language · GitHub","url":"https://github.com/fla-org/fla-zoo"}]

The search results show information about the flash-linear-attention repository and GatedDeltaNet implementations, but don't contain specific details about the parameter rename you're asking about. Let me search more specifically for parameter name cha
…[truncated 4495 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T12:29:38.871336+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:pypi.org \"flash-linear-attention\" release history"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:pypi.org \"flash-linear-attention\" release history"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-18T12:29:38.871476+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com fla-org flash-linear-attention \"A_log\" OR \"dt_bias\" commit rename refactor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com fla-org flash-linear-attention \"A_log\" OR \"dt_bias\" commit rename refactor"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T12:29:38.871594+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"m-a-p\" \"gated_deltanet\" OR \"GatedDeltaNet\" huggingface model config flash-linear-attention version"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"m-a-p\" \"gated_deltanet\" OR \"GatedDeltaNet\" huggingface model config flash-linear-attention version"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T12:29:38.871746+00:00_

Web search results for query: "site:pypi.org "flash-linear-attention" release history"

Links: [{"title":"flash-linear-attention · PyPI","url":"https://pypi.org/project/flash-linear-attention/"},{"title":"rwkv-simple · PyPI","url":"https://pypi.org/project/rwkv-simple/"},{"title":"rwkv-fla · PyPI","url":"https://pypi.org/project/rwkv-fla/"},{"title":"cuda-linear-attention · PyPI","url":"https://pypi.org/project/cuda-linear-attention/"}]

Based on the web search results, I found the PyPI page for flash-linear-attention. Starting from v0.3.2, the packages published on PyPI are fla-core and flash-linear-attention.

However, the search results don't contain detailed release history information. The first search result is from the PyPI project page for flash-linear-attention, but it doesn't display the full release history section in the excerpt provided. 

To view the complete release history for the flash-linear-attention package, you would need to visit the PyPI page directly at https://pypi.org/project/flash-linear-attention/ and scroll to the "Release history" section, which should list all available versions and their release dates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-18T12:29:38.871892+00:00_

Web search results for query: "site:github.com fla-org flash-linear-attention "A_log" OR "dt_bias" commit rename refactor"

Links: [{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"},{"title":"flash-linear-attention/fla/layers/gated_deltaproduct.py at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/fla/layers/gated_deltaproduct.py"},{"title":"GitHub - MoonshotAI/FlashKDA: FlashKDA: high-performance Kimi Delta Attention kernels · GitHub","url":"https://github.com/MoonshotAI/FlashKDA"},{"title":"GitHub - inclusionAI/cuLA: CUDA kernels for linear attention variants, written in CuTe DSL and CUTLASS C++. · GitHub","url":"https://github.com/inclusionAI/cuLA"},{"title":"qwen3.5-gated-deltanet-analysis · GitHub","url":"https://gist.github.com/justinchuby/0213aa253664fb72e9adb0089816de15"}]

Based on the search results, I found relevant information about `A_log` and `dt_bias` in the fla-org/flash-linear-attention repository:

A recent commit fix guards `A_log` and `dt_bias` re-initialization against loaded checkpoint values in GatedDeltaNet, Comba, and KDA (pull request #754).

The search results also show that in the codebase, `dt_bias` is handled specially to not receive weight decay because of a check for parameters ending with "bias", and both `A_log` and `dt_bias` are used together in calculations in the gated delta product operations.

Additionally, there was a rename refactor involving removing `head_first` and renaming `offsets` to `cu_seqlens` (pull request #345), which demonstrates the type of naming/refactoring work that occurs in the repository.

The search results indicate these are parameters used in linear attention implementations within the flash-linear-attention framework, particularly for delta rule-based attention mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T12:29:38.872068+00:00_

Web search results for query: ""m-a-p" "gated_deltanet" OR "GatedDeltaNet" huggingface model config flash-linear-attention version"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"GitHub - NVlabs/GatedDeltaNet: [ICLR 2025] Official PyTorch Implementation of Gated Delta Networks: Improving Mamba2 with Delta Rule · GitHub","url":"https://github.com/NVlabs/GatedDeltaNet"},{"title":"Gated DeltaNet | Sebastian Raschka, PhD","url":"https://sebastianraschka.com/llms-from-scratch/ch04/08_deltanet/"},{"title":"Idiap/gated-deltanet-attn-1.4B-30B · Hugging Face","url":"https://huggingface.co/Idiap/gated-deltanet-attn-1.4B-30B"},{"title":"Gated DeltaNet for Linear Attention - rasbt/LLMs-from-scratch","url":"https://github.com/rasbt/LLMs-from-scratch/blob/main/ch04/08_deltanet/README.md"},{"title":"qwen3.5-gated-deltanet-analysis · GitHub","url":"https://gist.github.com/justinchuby/0213aa253664fb72e9adb0089816de15"},{"title":"linear-moe-hub/Gated-Deltanet-1.3B · Hugging Face","url":"https://huggingface.co/linear-moe-hub/Gated-Deltanet-1.3B"},{"title":"Qwen/Qwen3-Next-80B-A3B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct"},{"title":"NVlabs/GatedDeltaNet | DeepWiki","url":"https://deepwiki.com/NVlabs/GatedDeltaNet"},{"title":"DeltaNet Explained (Part I) | Songlin Yang","url":"https://sustcsonglin.github.io/blog/2024/deltanet-1/"}]

Based on the search results, I found relevant information about GatedDeltaNet in the flash-linear-attention repository and related implementations:

Gated DeltaNet implementation was added to fla (flash-linear-attention) in December 2024. 

Optimized FLA Gated DeltaNet kernels are available in the repository, and you can import the Gated DeltaNet block directly from FLA using `from fla.layers import GatedDeltaNet`.

For Hugging Face model configurations, the model `Idiap/
…[truncated 691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T12:29:38.872259+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Fetch fla PyPI and releases",
  "subagent_type": "general-purpose",
  "prompt": "I need to find the exact version history of the flash-linear-attention Python package. Please:\n\n1. Use WebFetch to get https://pypi.org/project/flash-linear-attention/#history — look for all version numbers and release dates\n2. Use WebFetch to get https://github.com/fla-org/flash-linear-attention/releases — look for all release tags, dates, and changelogs (especially v0.4.x and v0.5.0)\n3. Use WebFetch to get https://data.safetycli.com/packages/pypi/flash-linear-attention/changelog — for the changelog\n\nReport every version number you find with its release date."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Agent",
  "tool_args": {
    "description": "Fetch fla PyPI and releases",
    "subagent_type": "general-purpose",
    "prompt": "I need to find the exact version history of the flash-linear-attention Python package. Please:\n\n1. Use WebFetch to get https://pypi.org/project/flash-linear-attention/#history — look for all version numbers and release dates\n2. Use WebFetch to get https://github.com/fla-org/flash-linear-attention/releases — look for all release tags, dates, and changelogs (especially v0.4.x and v0.5.0)\n3. Use WebFetch to get https://data.safetycli.com/packages/pypi/flash-linear-attention/changelog — for the changelog\n\nReport every version number you find with its release date."
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-18T12:29:38.872421+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-18T12:29:38.872542+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-18T12:29:38.872679+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Fetch paper and model cards",
  "subagent_type": "general-purpose",
  "prompt": "I need to find which version of flash-linear-attention was used by Wang et al. in their paper \"A Systematic Analysis of Hybrid Linear Attention\" (arXiv 2507.06457). Please:\n\n1. Use WebFetch to get https://arxiv.org/abs/2507.06457 — look for any GitHub repo link, code availability section, or version information\n2. Use WebFetch to get https://huggingface.co/m-a-p/transformer_340M_baseline — look for model card info, requirements, or fla version\n3. Use WebFetch to get https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research — look for all model links and any version info mentioned\n4. Try WebSearch for \"m-a-p gated_deltanet_1.3B_hybrid\" or similar model names on huggingface to find a model card that might mention fla version\n\nReport any version numbers, commit hashes, or requirements files you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Agent",
  "tool_args": {
    "description": "Fetch paper and model cards",
    "subagent_type": "general-purpose",
    "prompt": "I need to find which version of flash-linear-attention was used by Wang et al. in their paper \"A Systematic Analysis of Hybrid Linear Attention\" (arXiv 2507.06457). Please:\n\n1. Use WebFetch to get https://arxiv.org/abs/2507.06457 — look for any GitHub repo link, code availability section, or version information\n2. Use WebFetch to get https://huggingface.co/m-a-p/transformer_340M_baseline — look for model card info, requirements, or fla version\n3. Use WebFetch to get https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research — look for all model links and any version info mentioned\n4. Try WebSearch for \"m-a-p gated_deltanet_1.3B_hybrid\" or similar model names on huggingface to find a model card that might mention fla version\n\nReport any version numbers, commit hashes, or requirements files you find."
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T12:29:38.872852+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://pypi.org/project/flash-linear-attention/#history",
  "prompt": "List every version number and its release date for the flash-linear-attention package. Include ALL versions you can find on this page, from earliest to latest. Format each as: version - date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://pypi.org/project/flash-linear-attention/#history",
    "prompt": "List every version number and its release date for the flash-linear-attention package. Include ALL versions you can find on this page, from earliest to latest. Format each as: version - date"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-18T12:29:38.872975+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-18T12:29:38.873088+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-18T12:29:38.873207+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/releases",
  "prompt": "List every release tag, its release date, and any changelog or release notes content. Include ALL releases visible on this page, especially v0.4.x and v0.5.0 versions. Format each as: tag - date - changelog summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/releases",
    "prompt": "List every release tag, its release date, and any changelog or release notes content. Include ALL releases visible on this page, especially v0.4.x and v0.5.0 versions. Format each as: tag - date - changelog summary"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T12:29:38.873338+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Fetch fla GatedDeltaNet changes",
  "subagent_type": "general-purpose",
  "prompt": "I need to understand what breaking changes happened in flash-linear-attention (fla) around GatedDeltaNet, specifically regarding the parameter \"A_log\" or \"attn.D\". Please:\n\n1. Use WebFetch to get https://github.com/fla-org/flash-linear-attention/blob/main/fla/layers/gated_delta_net.py — look for any parameter named A_log, D, dt_bias, or attn\n2. Use WebFetch to get https://github.com/fla-org/flash-linear-attention/releases/tag/v0.5.0 — look for the full changelog and breaking changes\n3. Use WebFetch to get https://github.com/fla-org/flash-linear-attention/releases/tag/v0.4.0 — look for changelog\n4. Use WebSearch for: github fla-org flash-linear-attention pull request \"A_log\" OR \"rename\" GatedDeltaNet parameter\n5. Use WebFetch to get https://github.com/fla-org/flash-linear-attention/pulls?q=GatedDeltaNet+A_log — to find relevant PRs\n\nReport all parameter changes and breaking changes you find, especially anything that would cause checkpoint loading failures."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Agent",
  "tool_args": {
    "description": "Fetch fla GatedDeltaNet changes",
    "subagent_type": "general-purpose",
    "prompt": "I need to understand what breaking changes happened in flash-linear-attention (fla) around GatedDeltaNet, specifically regarding the parameter \"A_log\" or \"attn.D\". Please:\n\n1. Use WebFetch to get https://github.com/fla-org/flash-linear-attention/blob/main/fla/layers/gated_delta_net.py — look for any parameter named A_log, D, dt_bias, or attn\n2. Use WebFetch to get https://github.com/fla-org/flash-linear-attention/releases/tag/v0.5.0 — look for the full changelog and breaking changes\n3. Use WebFetch to get https://github.com/fla-org/flash-linear-attention/releases/tag/v0.4.0 — look for changelog\n4. Use WebSearch for: github fla-org flash-linear-attention pull request \"A_log\" OR \"rename\" GatedDeltaNet parameter\n5. Use WebFetch to get https://github.com/fla-org/flash-linear-attention/pulls?q=GatedDeltaNet+A_log — to find relevant PRs\n\nReport all parameter changes and breaking changes you find, especially anything that would cause checkpoint loading failures."
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-18T12:29:38.873499+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://data.safetycli.com/packages/pypi/flash-linear-attention/changelog",
  "prompt": "List every version number and its release date for the flash-linear-attention package. Include ALL versions and any changelog details. Format each as: version - date - changes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://data.safetycli.com/packages/pypi/flash-linear-attention/changelog",
    "prompt": "List every version number and its release date for the flash-linear-attention package. Include ALL versions and any changelog details. Format each as: version - date - changes"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-18T12:29:38.873618+00:00_

# Flash-Linear-Attention Package Versions

Based on the PyPI page, here are all available versions from earliest to latest:

- 0.1 - Mar 20, 2025
- 0.1.1 - Mar 24, 2025
- 0.1.2 - Mar 31, 2025
- 0.2.0 - Apr 11, 2025
- 0.2.1 - Apr 23, 2025
- 0.2.2 - Jun 5, 2025
- 0.3.0 - Jul 14, 2025
- 0.3.1 - Aug 26, 2025
- 0.3.2 - Sep 10, 2025
- 0.4.0 - Oct 27, 2025
- 0.4.1 - Dec 24, 2025
- 0.4.2 - Mar 12, 2026
- 0.5.0 - Apr 21, 2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-18T12:29:38.873763+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.06457",
  "prompt": "Find any information about: 1) GitHub repository links or code availability, 2) flash-linear-attention (fla) version or commit hash, 3) software dependencies or requirements, 4) any mention of specific library versions used. Extract all URLs, version numbers, and commit hashes mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2507.06457",
    "prompt": "Find any information about: 1) GitHub repository links or code availability, 2) flash-linear-attention (fla) version or commit hash, 3) software dependencies or requirements, 4) any mention of specific library versions used. Extract all URLs, version numbers, and commit hashes mentioned."
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-18T12:29:38.873884+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T12:29:38.873992+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-18T12:29:38.874112+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/transformer_340M_baseline",
  "prompt": "Find any information about: 1) flash-linear-attention (fla) version or commit hash, 2) software dependencies or requirements, 3) training configuration or library versions, 4) any links to GitHub repos or requirements files. Extract all version numbers and dependency information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/transformer_340M_baseline",
    "prompt": "Find any information about: 1) flash-linear-attention (fla) version or commit hash, 2) software dependencies or requirements, 3) training configuration or library versions, 4) any links to GitHub repos or requirements files. Extract all version numbers and dependency information."
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-18T12:29:38.874238+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research",
  "prompt": "List ALL model names/links in this collection. For each, note any version information, fla version, flash-linear-attention version, commit hash, or dependency information mentioned. Extract everything related to software versions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research",
    "prompt": "List ALL model names/links in this collection. For each, note any version information, fla version, flash-linear-attention version, commit hash, or dependency information mentioned. Extract everything related to software versions."
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-18T12:29:38.874360+00:00_

# Flash-Linear-Attention Version History

Based on the changelog provided, here are the documented releases:

**0.5.0** - Date not specified
"MoBA / FlashMoBA" integration, multi-backend support with FlashKDA and TileLang, various bug fixes and optimizations across GDN, KDA, and attention kernels.

**0.4.2** - Date not specified
Performance improvements including reduced sync operations, convolution enhancements, KDA speedups via lower-bound gating, and backend dispatch system introduction.

**0.4.1** - Date not specified
KDA optimization with token-parallel intra-chunk attention, NSA and GDN fixes, softplus PTX support, and various kernel improvements.

**0.4.0** - Date not specified
Introduction of Kimi Delta Attention (KDA) as new model, DeltaFormer addition, autotune caching for Triton kernels, and dependency minimization.

**0.3.2** - Date not specified
Log Linear Attention model addition, minimal-dependency fla-core package launch, and causal convolution enhancements.

**0.3.1** - Date not specified
RWKV7 optimizations, TokenShift support for cache, Log-Linear Attention testing, and TMA descriptor acceleration for solve_tril.

The page indicates "Page 1 of 3," suggesting additional older versions exist on subsequent pages, but specific release dates are not provided in this excerpt.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-18T12:29:38.874492+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "m-a-p gated_deltanet hybrid flash-linear-attention fla version huggingface model card"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "m-a-p gated_deltanet hybrid flash-linear-attention fla version huggingface model card"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-18T12:29:38.874606+00:00_

# Search Results Summary

Based on the provided content, here's what I found:

## Code/Repository Availability
The paper mentions open-sourced models with this reference: **"Our models are open-sourced at [this https URL]"** - however, the actual URL is not fully displayed in the extracted text, only a placeholder link to a Hugging Face collection about "hybrid-linear-attention-research."

## Flash-Linear-Attention (FLA)
No mention of flash-linear-attention, version numbers, or commit hashes appears in this document.

## Software Dependencies
No specific library versions, dependency lists, or software requirements are detailed in the provided content.

## URLs Found
- Hugging Face collection reference: `https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e`
- DOI: `https://doi.org/10.48550/arXiv.2507.06457`

## Conclusion
The abstract references open-sourced models but does not provide detailed technical setup information, version specifics, or GitHub repository links within this landing page content. For complete implementation details, accessing the full PDF or HTML paper version would be necessary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-18T12:29:38.874751+00:00_

# Flash-Linear-Attention Release Tags and Dates

**v0.5.0** - April 21, 2024
Key additions include "Mixture of Block Attention (MoBA/FlashMoBA)" and multi-backend support with "FlashKDA as a new backend for KDA" and TileLang introduction for various kernels.

**v0.4.2** - March 12, 2024
Focused on performance improvements through "lowerbound gate function" enhancements and backend dispatch system implementation for selecting "available backends based on priority order."

**v0.4.1** - December 24, 2023
Performance optimizations centered on KDA with "token-parallel intra-chunk attention" implementation and fused kernel improvements across multiple operations.

**v0.4.0** - October 27, 2023
Major release introducing "Kimi Delta Attention" as the primary new model contribution alongside various kernel optimizations and infrastructure updates.

**v0.3.2** - September 10, 2023
Introduced "Log Linear Attention" model with backward pass support and split package distribution for a "minimal-dependency subset of the main repo."

**v0.3.1** - August 26, 2023
Added "Log-Linear Attention" model implementation and various performance enhancements for existing architectures including "TMA acceleration" improvements.

**v0.3.0** - July 14, 2023
Expanded model library with four architectures: MesaNet, PaTH, Comba, and MLA, representing substantial architectural diversification.

**v0.2.2** - June 5, 2023
Added PaTH attention model and introduced performance optimizations achieving "1.1x speedup" for DeltaNet through "fused LayerNormGated layer" enhancements.

**v0.2.1** - April 23, 2023
Optimization release delivering "1.1x speedup" primarily through normalization kernel improvements for small dimension parameters.

**v0.2.0** - April 11, 2023
Major API refactoring removing "head_first option" and renaming parameters like "offsets to cu_seqlens" alongside FoX model introduction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-18T12:29:38.874885+00:00_

# Analysis of Model Page Content

Based on the provided web page content for `m-a-p/transformer_340M_baseline`, here's what I found:

## Information Available:

1. **Model Specifications:**
   - Model size: 0.3B params
   - Tensor type: F32
   - Format: Safetensors

2. **Collection Reference:**
   - Part of "Hybrid Linear Attention Research" collection
   - Updated Sep 11, 2025
   - Contains 62 items focused on "1.3B & 340M hybrid linear-attention experiments"

## Information NOT Available:

❌ **Flash-Linear-Attention (FLA) version or commit hash** - Not provided on this page

❌ **Software dependencies or requirements** - Not listed (page notes "No model card")

❌ **Training configuration or library versions** - Not specified

❌ **GitHub repo links or requirements files** - Not included in the content provided

## Recommendation:

To find the missing technical details, you would need to:
- Check the actual **model card** (if one exists beyond what's shown)
- Visit the **Files section** (indicated by "xet" link)
- Check the associated **GitHub repository** for the m-a-p organization
- Review the **Hybrid Linear Attention Research collection** page for documentation
- Contact the model creators (Multimodal Art Projection organization)

The provided web page is primarily a landing/overview page without detailed technical specifications.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-18T12:29:38.875024+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/blob/main/fla/layers/gated_delta_net.py",
  "prompt": "Extract the full source code of the GatedDeltaNet class. Focus on: 1) All __init__ parameters, especially anything named A_log, D, dt_bias, attn, a_log, or similar. 2) The full parameter list and any nn.Parameter definitions. 3) Any comments about parameter naming or backward compatibility. 4) The state_dict_from_pretrained or any weight loading/conversion methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/blob/main/fla/layers/gated_delta_net.py",
    "prompt": "Extract the full source code of the GatedDeltaNet class. Focus on: 1) All __init__ parameters, especially anything named A_log, D, dt_bias, attn, a_log, or similar. 2) The full parameter list and any nn.Parameter definitions. 3) Any comments about parameter naming or backward compatibility. 4) The state_dict_from_pretrained or any weight loading/conversion methods."
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-18T12:29:38.875150+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/releases/tag/v0.5.0",
  "prompt": "Extract the full changelog and release notes for v0.5.0. Focus on: 1) Any breaking changes listed. 2) Any parameter renames or API changes. 3) Any mentions of GatedDeltaNet, A_log, D, dt_bias, or checkpoint compatibility. 4) All bullet points of changes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/releases/tag/v0.5.0",
    "prompt": "Extract the full changelog and release notes for v0.5.0. Focus on: 1) Any breaking changes listed. 2) Any parameter renames or API changes. 3) Any mentions of GatedDeltaNet, A_log, D, dt_bias, or checkpoint compatibility. 4) All bullet points of changes."
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-18T12:29:38.875265+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-18T12:29:38.875395+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/releases/tag/v0.4.0",
  "prompt": "Extract the full changelog and release notes for v0.4.0. Focus on: 1) Any breaking changes listed. 2) Any parameter renames or API changes. 3) Any mentions of GatedDeltaNet, A_log, D, dt_bias, or checkpoint compatibility. 4) All bullet points of changes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/releases/tag/v0.4.0",
    "prompt": "Extract the full changelog and release notes for v0.4.0. Focus on: 1) Any breaking changes listed. 2) Any parameter renames or API changes. 3) Any mentions of GatedDeltaNet, A_log, D, dt_bias, or checkpoint compatibility. 4) All bullet points of changes."
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-18T12:29:38.875521+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://data.safetycli.com/packages/pypi/flash-linear-attention/changelog?page=2",
  "prompt": "List every version number, release date, and changelog details for the flash-linear-attention package on this page. Format each as: version - date - changes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://data.safetycli.com/packages/pypi/flash-linear-attention/changelog?page=2",
    "prompt": "List every version number, release date, and changelog details for the flash-linear-attention package on this page. Format each as: version - date - changes"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-18T12:29:38.875658+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "github fla-org flash-linear-attention pull request \"A_log\" OR \"rename\" GatedDeltaNet parameter",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "github fla-org flash-linear-attention pull request \"A_log\" OR \"rename\" GatedDeltaNet parameter",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-18T12:29:38.875788+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://data.safetycli.com/packages/pypi/flash-linear-attention/changelog?page=3",
  "prompt": "List every version number, release date, and changelog details for the flash-linear-attention package on this page. Format each as: version - date - changes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://data.safetycli.com/packages/pypi/flash-linear-attention/changelog?page=3",
    "prompt": "List every version number, release date, and changelog details for the flash-linear-attention package on this page. Format each as: version - date - changes"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-18T12:29:38.875925+00:00_

Web search results for query: "m-a-p gated_deltanet hybrid flash-linear-attention fla version huggingface model card"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"Idiap/gated-deltanet-attn-1.4B-30B · Hugging Face","url":"https://huggingface.co/Idiap/gated-deltanet-attn-1.4B-30B"},{"title":"m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1"},{"title":"GitHub - NVlabs/GatedDeltaNet: [ICLR 2025] Official PyTorch Implementation of Gated Delta Networks: Improving Mamba2 with Delta Rule · GitHub","url":"https://github.com/NVlabs/GatedDeltaNet"},{"title":"Qwen/Qwen3-Next-80B-A3B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct"},{"title":"Gated DeltaNet | Sebastian Raschka, PhD","url":"https://sebastianraschka.com/llms-from-scratch/ch04/08_deltanet/"},{"title":"DeltaNet Explained (Part I) | Songlin Yang","url":"https://sustcsonglin.github.io/blog/2024/deltanet-1/"},{"title":"hustvl/InfiniteVL · Hugging Face","url":"https://huggingface.co/hustvl/InfiniteVL"},{"title":"Hybrid Linear Attention Research - a m-a-p Collection","url":"https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e"},{"title":"Linear Attention Models (GLA, Delta Net) | fla-org/flame | DeepWiki","url":"https://deepwiki.com/fla-org/flame/7.3-linear-attention-models-(gla-delta-net)"}]

Based on the web search results, I found relevant information about the m-a-p gated_deltanet hybrid flash-linear-attention model:

The m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1 model is a gated_deltanet architecture with 0.4B parameters that is part of a collection for "All 1.3B & 340M hybrid linear-attention experiments".

Gated DeltaNet was added to the flash-linear-attention (FLA) library in December 2024. The FL
…[truncated 702 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-18T12:29:38.876084+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/pulls?q=GatedDeltaNet+A_log",
  "prompt": "List all pull requests shown on this page. For each PR, extract: title, number, author, date, and any description text. Focus on PRs that mention A_log, parameter renames, GatedDeltaNet changes, or breaking changes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/pulls?q=GatedDeltaNet+A_log",
    "prompt": "List all pull requests shown on this page. For each PR, extract: title, number, author, date, and any description text. Focus on PRs that mention A_log, parameter renames, GatedDeltaNet changes, or breaking changes."
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-18T12:29:38.876220+00:00_

Web search results for query: "github fla-org flash-linear-attention pull request "A_log" OR "rename" GatedDeltaNet parameter"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"},{"title":"GitHub - Fzkuji/flash-linear: 🚀 Efficient implementations of state-of-the-art linear attention models in Pytorch and Triton","url":"https://github.com/Fzkuji/flash-linear-attention"},{"title":"Pull requests · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/pulls"},{"title":"flash-linear-attention/README.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/README.md"},{"title":"GitHub - fla-org/fla-zoo: Flash-Linear-Attention models beyond language · GitHub","url":"https://github.com/fla-org/fla-zoo"},{"title":"[Stick-Breaking Attention] Add Model by Nathancgy · Pull Request #599 · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/pull/599"},{"title":"GitHub - YJMSTR/cutile-flash-linear-attention: FLA but cuTile","url":"https://github.com/YJMSTR/cutile-flash-linear-attention"},{"title":"Home · fla-org/flash-linear-attention Wiki · GitHub","url":"https://github.com/fla-org/flash-linear-attention/wiki"},{"title":"[Bug] GatedDeltaNet backward error on Blackwell · Issue #607 · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/issues/607"}]

Based on the search results, I found relevant information about a pull request related to your query. There was a fix that guards A_log and dt_bias re-initialization against loaded checkpoint values in GatedDeltaNet, Comba, and KDA by @ljxw88 in #754. This appears to be the pull request you're looking for, which addresses the `A_
…[truncated 194 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-18T12:29:38.876356+00:00_

# flash-linear-attention Package Versions

Based on the changelog page provided, here are the version numbers listed:

**Version 0.1.0** - No release date provided on this page

The changelog for this version includes numerous updates across multiple areas:

- "Update README.md" and fixes to gradient calculations
- Implementations of RWKV-v4, Mamba 2, and BitNet models
- Bug fixes for "backward if h0 not passed" and cache management issues
- Torch 2.4.0 compatibility updates
- Enhancements to precision in fused LayerNorm operations
- Support for variable-length training and conversion scripts for RWKV7 models

**Additional versions visible** (without detailed changelog on this page):
0.1.1, 0.1.2, 0.2.0, 0.2.1, 0.2.2, 0.3.0, 0.3.1, 0.3.2, 0.4.0, 0.4.1, 0.4.2, and 0.5.0 (latest)

Note: The webpage displays "Page 3 of 3," showing only version 0.1.0 details. Release dates are not included in the provided content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-18T12:29:38.876480+00:00_

# Flash Linear Attention v0.4.0 Release Notes

## Breaking Changes & API Modifications
No explicit breaking changes are documented. However, several structural updates occurred:
- "Replace GenerationMixin with FLAGenerationMixin" suggests API modifications for model generation
- "Make pytest an optional dependency" and "Minimize deps" indicate dependency adjustments

## Parameter/API Changes
The release notes don't specifically mention renaming of parameters like `A_log`, `D`, `dt_bias`, or checkpoint compatibility issues.

## All Changes

**New Features:**
- "Kimi Delta Attention" model implementation added

**Bug Fixes & Improvements:**
- Resolved tiling issues in GDN when gradient variation applied
- Enhanced Conv module with comprehensive documentation; switched default backend to Triton
- Corrected cumsum dimension in normalize_output function
- Fixed potential out-of-bounds problems in Conv operations
- Resolved cache compatibility with from_legacy_cache
- Fixed DeltaFormer testing operation errors
- Implemented autotune caching for Triton kernels
- Chunk size now determined at kernel entry point

**Infrastructure:**
- Migrated linting from flake8/isort to Ruff
- Reduced dependency footprint

**Contributors:** 7 contributors including 4 first-time contributors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-18T12:29:38.876599+00:00_

# Flash-Linear-Attention v0.5.0 Release Notes

## Breaking Changes & API Modifications

**Parameter Removal:** "Cleanup: Remove deprecated head_first parameter from public ops" (#853) indicates the `head_first` parameter has been eliminated from public operations.

**Minimum PyTorch Upgrade:** "Upgrade minimum PyTorch requirement to 2.7.0" (#801) represents a significant dependency change.

## GatedDeltaNet & Related Mentions

The changelog does not explicitly reference GatedDeltaNet, A_log, D, dt_bias, or checkpoint compatibility issues. However, one change permits negative eigenvalues for delta-net (#832), suggesting performance or stability improvements for delta-net architectures.

## Complete Changes Summary

**Major Features:**
- MoBA/FlashMoBA integration (Moonshot's Mixture of Block Attention)
- Multi-backend architecture expansion beyond Triton
- FlashKDA backend for KDA support
- TileLang backend introduction for GDN, KDA, and parallel attention

**Key Improvements:**
- 54 merged pull requests addressing bugs, optimizations, and new features
- Grouped Value Attention (GVA) support for GDN and KDA
- Sliding window and attention sink support additions
- Fused kernel implementations reducing computational overhead
- Logit softcapping in cross entropy operations

**Critical Bug Fixes:**
- Memory access violations and overflow issues in conv kernels
- FSDP meta device compatibility fixes
- Varlen mode batch-size enforcement across operations

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-18T12:29:38.876749+00:00_

# Hybrid Linear Attention Research Collection - Model List

## All Models in Collection

### 340M Parameter Models (20B Tokens)

1. **m-a-p/340M-20B-GatedDeltaNet-hybrid-3-1** - 0.4B | Updated Mar 3, 2025
2. **m-a-p/340M-20B-GatedDeltaNet-hybrid-6-1** - 0.4B | Updated Mar 3, 2025
3. **m-a-p/340M-20B-GLA-hybrid-6-1** - 0.3B | Updated Mar 3, 2025
4. **m-a-p/340M-20B-GLA-hybrid-3-1** - 0.3B | Updated Mar 3, 2025
5. **m-a-p/340M-20B-GLA-hybrid-12-1** - 0.3B | Updated Mar 3, 2025
6. **m-a-p/340M-20B-GLA-hybrid-24-1** - 0.3B | Updated Mar 3, 2025
7. **m-a-p/340M-20B-HGRN2-pure-baseline** - 0.3B | Updated Mar 3, 2025
8. **m-a-p/340M-20B-HGRN2-hybrid-6-1** - 0.3B | Updated Mar 3, 2025
9. **m-a-p/340M-20B-HGRN2-hybrid-3-1** - 0.3B | Updated Mar 3, 2025
10. **m-a-p/340M-20B-HGRN2-hybrid-12-1** - 0.3B | Updated Mar 4, 2025
11. **m-a-p/340M-20B-HGRN2-hybrid-24-1** - 0.3B | Updated Mar 4, 2025
12. **m-a-p/340M-20B-DeltaNet-hybrid-3-1** - 0.3B | Updated Mar 4, 2025
13. **m-a-p/340M-20B-DeltaNet-pure** - 0.3B | Updated Mar 4, 2025
14. **m-a-p/340M-20B-DeltaNet-hybrid-6-1** - 0.3B | Updated Mar 4, 2025
15. **m-a-p/340M-20B-DeltaNet-hybrid-12-1** - 0.3B | Updated Mar 4, 2025
16. **m-a-p/340M-20B-DeltaNet-hybrid-24-1** - 0.3B | Updated Mar 4, 2025
17. **m-a-p/340M-20B-RetNet-hybrid-24-1** - 0.3B | Updated Mar 4, 2025
18. **m-a-p/340M-20B-RetNet-hybrid-12-1** - 0.3B | Updated Mar 4, 2025
19. **m-a-p/340M-20B-RetNet-hybrid-6-1** - 0.3B | Updated Mar 4, 2025
20. **m-a-p/340M-20B-RetNet-hybrid-3-1** - 0.3B | Updated Mar 4, 2025
21. **m-a-p/340M-20B-RetNet-pure** - 0.3B | Updated Mar 4, 2025
22. **m-a-p/340M-20B-HGRN-hybrid-3-1** - 0.3B | Updated Apr 20, 2025
23. **m-a-p/340M-20B-HGRN-hybrid-6-1** - 0.3B | Updated Apr 20, 2025
24. **m-a-p/340M-20B-HGRN-hybrid-12-1** - 0.3B | Updated Apr 20, 2025
25. **m-a-p/340M-20B-HGRN-hybrid-24-1** - 0.3B | Updated Apr 20, 2025
26. **m-a-p/340M-20B-HGRN-pure-baseline** - 0.3B | Updated Apr 20, 2025
27. **m-a-p/340M-20B-GLA-pure-baseline** - 0.3B | Upda
…[truncated 2745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-18T12:29:38.876885+00:00_

# Flash-Linear-Attention Package Versions

Based on the changelog page provided, here are the versions displayed:

**0.3.0** - No date listed - Added four new model architectures (MesaNet, PaTH, Comba, MLA). Notable changes include kernel implementations, support for inference modes, precision enhancements with L2Warp, CI upgrades to torch~=2.7.0, and various bug fixes across multiple components.

**0.2.2** - No date listed - Introduced TokenShift support with varlen, official Mamba initialization strategies, new Mamba2 and Mamba attention layers, PaTH attention model and kernel, fused pack/unpack utilities, and RWKV7 initialization updates aligned with official RWKV-LM.

**0.2.1** - No date listed - Featured performance optimization for DeltaNet models achieving "1.1x speedup," optimized LayerNormGated layer for small headdims, RWKV7 initialization updates, and various norm and GroupNorm speed improvements.

**0.2.0** - No date listed - Introduced FoX model/layer/kernel implementations with varlen support, renamed "fox" to "forgetting_attn," optimized WY representation for DeltaNet, enhanced GroupNorm with RMS norm argument, removed "head_first" parameter throughout codebase.

**0.1.2** - No date listed - Fixed RWKV7Attention initialization, corrected triton kernel issues on H100 GPUs, added triton implementations for MHA/GQA, enhanced Hopper GPU support.

**0.1.1** - No date listed - Improved DeltaNet kernel speed through fine-grained autotuning, added fused norm/gate operations, fixed various bugs in RWKV7 and other components.

*Note: Specific release dates are not provided on this changelog page.*

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-18T12:29:38.877006+00:00_

# Pull Requests Related to GatedDeltaNet and A_log

Based on the GitHub page for fla-org/flash-linear-attention, here are the relevant PRs:

## Key PRs Mentioning A_log or GatedDeltaNet:

1. **#848** - "[GDN/KDA] Fuse gate activation into fused_recurrent kernels"
   - Author: yzhangcs (Member)
   - Merged: Apr 18, 2026

2. **#820** - "[Fix] Guard checkpoint weight re-initialization in RWKV-7, Mamba, Mamba2, and LogLinearMamba2"
   - Author: puigde (Contributor)
   - Merged: Apr 12, 2026

3. **#813** - "[GDN] Add fused gate kernel with use_gate_in_kernel support"
   - Author: yzhangcs (Member)
   - Merged: Apr 6, 2026

4. **#754** - "[Fix] Guard A_log and dt_bias re-initialization against loaded checkpoint values..."
   - Author: ljxw88 (Contributor)
   - Merged: Feb 25, 2026
   - *Directly addresses A_log parameter handling*

5. **#380** - "[GDN]: initializing `A_log` and `dt_bias` in `_init_weights`"
   - Author: HanGuo97 (Contributor)
   - Merged: May 1, 2025
   - *Core initialization changes for A_log parameter*

The page shows 9 closed PRs matching the search "GatedDeltaNet A_log" with no currently open PRs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-18T12:29:38.877140+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/fla-org/flash-linear-attention/main/fla/layers/gated_delta_net.py",
  "prompt": "Extract the COMPLETE source code. Show every class definition, every __init__ method, every nn.Parameter, every reference to A_log, D, dt_bias, a_log, attn. Show all parameter names used in the class."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/fla-org/flash-linear-attention/main/fla/layers/gated_delta_net.py",
    "prompt": "Extract the COMPLETE source code. Show every class definition, every __init__ method, every nn.Parameter, every reference to A_log, D, dt_bias, a_log, attn. Show all parameter names used in the class."
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-18T12:29:38.877265+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2507.06457",
  "prompt": "Find ANY mention of: 1) flash-linear-attention or fla library version, commit hash, or installation instructions, 2) GitHub repository URL for code, 3) software dependencies, requirements, or environment setup, 4) any pip install commands or package versions. Look in the entire paper including appendix, footnotes, and supplementary sections. Extract all version numbers and URLs found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2507.06457",
    "prompt": "Find ANY mention of: 1) flash-linear-attention or fla library version, commit hash, or installation instructions, 2) GitHub repository URL for code, 3) software dependencies, requirements, or environment setup, 4) any pip install commands or package versions. Look in the entire paper including appendix, footnotes, and supplementary sections. Extract all version numbers and URLs found."
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-18T12:29:38.877375+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-18T12:29:38.877492+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/pull/380",
  "prompt": "Extract the full PR description, all code changes (diffs), and all comments. This PR is about initializing A_log and dt_bias in _init_weights. I need to understand what parameters existed before and after this change."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/pull/380",
    "prompt": "Extract the full PR description, all code changes (diffs), and all comments. This PR is about initializing A_log and dt_bias in _init_weights. I need to understand what parameters existed before and after this change."
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-18T12:29:38.877614+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1",
  "prompt": "Find any information about: 1) flash-linear-attention (fla) version, commit hash, or package version, 2) training configuration, software dependencies, requirements, 3) any config.json contents showing library versions, 4) any README or model card content. Extract all technical details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1",
    "prompt": "Find any information about: 1) flash-linear-attention (fla) version, commit hash, or package version, 2) training configuration, software dependencies, requirements, 3) any config.json contents showing library versions, 4) any README or model card content. Extract all technical details."
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-18T12:29:38.877758+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/pull/754",
  "prompt": "Extract the full PR description, all code changes (diffs), and all comments. This PR is about guarding A_log and dt_bias re-initialization against loaded checkpoint values. I need to understand the exact parameter names and the fix applied."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/pull/754",
    "prompt": "Extract the full PR description, all code changes (diffs), and all comments. This PR is about guarding A_log and dt_bias re-initialization against loaded checkpoint values. I need to understand the exact parameter names and the fix applied."
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-18T12:29:38.877883+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "github fla-org flash-linear-attention GatedDeltaNet \"A_log\" renamed \"a_log\" OR \"attn.A\" checkpoint breaking change",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "github fla-org flash-linear-attention GatedDeltaNet \"A_log\" renamed \"a_log\" OR \"attn.A\" checkpoint breaking change",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-18T12:29:38.878005+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1/tree/main",
  "prompt": "List ALL files in this model repository. I'm looking for config.json, requirements.txt, README.md, or any file that might contain version information about flash-linear-attention or other dependencies."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1/tree/main",
    "prompt": "List ALL files in this model repository. I'm looking for config.json, requirements.txt, README.md, or any file that might contain version information about flash-linear-attention or other dependencies."
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-18T12:29:38.878132+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1",
  "prompt": "Find any information about: 1) flash-linear-attention (fla) version, commit hash, or package version, 2) training configuration, software dependencies, 3) any model card or README content, 4) any config.json or requirements. Extract all technical details and version numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1",
    "prompt": "Find any information about: 1) flash-linear-attention (fla) version, commit hash, or package version, 2) training configuration, software dependencies, 3) any model card or README content, 4) any config.json or requirements. Extract all technical details and version numbers."
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-18T12:29:38.878248+00:00_

# Software Dependencies and Installation Information

After thoroughly reviewing the entire paper, I found **minimal technical setup information**:

## Found References

1. **Library Mention**: The paper states models are "implemented using the [flash-linear-attention](https://github.com/fla-org/flash-linear-attention) library" but provides **no version number, commit hash, or installation instructions**.

2. **GitHub URL**: Only one repository link appears: `https://github.com/fla-org/flash-linear-attention`

3. **No Dependency Details**: The paper contains **no pip install commands, requirements files, or environment specifications**.

4. **Training Framework**: The work uses "AdamW optimizer with a cosine learning rate schedule" but doesn't specify which framework (PyTorch, etc.) or versions.

5. **Dataset Reference**: Mentions "fineweb-edu" dataset but without specific version or access instructions.

## Key Limitation

The authors note: "Our model training and inference are both implemented using the flash-linear-attention library" but unfortunately do not include reproducibility details such as specific versions, dependency lists, or setup procedures in this document.

For implementation details, readers would need to consult the linked GitHub repository or contact the authors directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-18T12:29:38.878372+00:00_

# Analysis of Available Technical Information

Based on the provided web page content, **very limited technical details are available**. Here's what can be extracted:

## Available Information

### Model Metadata
- **Model Name**: `m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1`
- **Organization**: Multimodal Art Projection (m-a-p)
- **Model Size**: 1B params
- **Tensor Type**: F32
- **Format**: Safetensors
- **Downloads (last month)**: 14

### Associated Collection
- **Collection**: "Hybrid Linear Attention Research"
- **Description**: "All 1.3B & 340M hybrid linear-attention experiments"
- **Items**: 62
- **Updated**: Sep 11, 2025

## Missing Information

❌ **No config.json contents** - Not displayed on page  
❌ **No README or model card** - Page explicitly states "No model card"  
❌ **No flash-linear-attention (fla) version/commit hash** - Not provided  
❌ **No training configuration details** - Not available  
❌ **No software dependencies/requirements** - Not specified  
❌ **No package versions** - Not listed  

## Recommendation

To access the complete technical specifications, you would need to:
1. Visit the model's [Files section](https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1/tree/main)
2. Download and review the `config.json` file directly
3. Check for any README.md files in the repository

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-18T12:29:38.878550+00:00_

Here is the complete version history of the **flash-linear-attention** Python package, compiled from PyPI, GitHub Releases, and the SafetyCLI changelog:

| Version | Release Date | Key Changes |
|---------|-------------|-------------|
| **0.1** (0.1.0) | Mar 20, 2025 | Initial release. RWKV-v4, Mamba 2, BitNet models; variable-length training support; torch 2.4.0 compatibility; fused LayerNorm precision enhancements. |
| **0.1.1** | Mar 24, 2025 | DeltaNet kernel speed improvements via fine-grained autotuning; fused norm/gate operations; RWKV7 bug fixes. |
| **0.1.2** | Mar 31, 2025 | Fixed RWKV7Attention initialization; corrected Triton kernel issues on H100 GPUs; added Triton implementations for MHA/GQA; enhanced Hopper GPU support. |
| **0.2.0** | Apr 11, 2025 | Major API refactoring: removed `head_first` parameter, renamed `offsets` to `cu_seqlens`. Introduced FoX (Forgetting Attention) model/layer/kernel with varlen support. Optimized WY representation for DeltaNet. |
| **0.2.1** | Apr 23, 2025 | Performance optimization: 1.1x speedup for DeltaNet through optimized LayerNormGated layer for small headdims. RWKV7 initialization updates; GroupNorm speed improvements. |
| **0.2.2** | Jun 5, 2025 | Added PaTH attention model and kernel. TokenShift support with varlen. Official Mamba initialization strategies, new Mamba2/Mamba attention layers. Fused pack/unpack utilities. Fused LayerNormGated layer giving 1.1x speedup for DeltaNet. |
| **0.3.0** | Jul 14, 2025 | Four new model architectures: MesaNet, PaTH, Comba, MLA. L2Warp precision enhancements. CI upgraded to torch~=2.7.0. |
| **0.3.1** | Aug 26, 2025 | Log-Linear Attention model implementation. RWKV7 optimizations. TokenShift support for cache. TMA descriptor acceleration for solve_tril. |
| **0.3.2** | Sep 10, 2025 | Log Linear Attention with backward pass support. Split package distribution: launched minimal-dependency `fla-core` package. Causal convolution enhancements. |
| **0.4.0** | Oct 27, 2025 | Major r
…[truncated 1013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Agent",
  "elapsed_ms": 6
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-18T12:29:38.878717+00:00_

# Files in the Model Repository

Based on the web page content, here are **ALL files** listed in this model repository:

1. **.gitattributes** (1.52 kB)
2. **config.json** (1.16 kB) ✓
3. **generation_config.json** (111 Bytes)
4. **model-00001-of-00002.safetensors** (4.99 GB)
5. **model-00002-of-00002.safetensors** (606 MB)
6. **model.safetensors.index.json** (29.1 kB)
7. **special_tokens_map.json** (414 Bytes)
8. **tokenizer.json** (3.51 MB)
9. **tokenizer_config.json** (1.03 kB)

## Key Findings:

- **config.json** is present (1.16 kB) - likely contains model architecture and dependency information
- **No requirements.txt** file is listed
- **No README.md** file is visible in the provided content
- **No flash-linear-attention version info** is shown in the file listing

To find version information about dependencies like flash-linear-attention, you would need to examine the **config.json** file directly, as it's the most likely location for such metadata in this model repository.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-18T12:29:38.878851+00:00_

# Technical Details Analysis

Based on the provided web page content, here's what I found:

## Available Information:

1. **Model Specifications:**
   - Model size: 0.4B params
   - Tensor type: F32
   - Format: Safetensors
   - Architecture: gated_deltanet (hybrid linear-attention based)

2. **Model Identity:**
   - Model name: `340M-20B-GatedDeltaNet-New-hybrid-24-1`
   - Organization: m-a-p (Multimodal Art Projection)
   - HuggingFace URL: `/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1`

## Missing Information:

❌ **No model card or README content** - The page explicitly states "No model card"

❌ **Flash-Linear-Attention (FLA) version** - Not mentioned in the provided content

❌ **Commit hash** - Not visible in this page excerpt

❌ **Training configuration** - Not documented

❌ **Software dependencies/requirements** - Not specified

❌ **config.json details** - Not shown

❌ **Package versions** - Not provided

## Recommendation:

To obtain complete technical details, you would need to:
1. Visit the full model repository page directly
2. Check the "Files and versions" section (linked as `/tree/main`)
3. Look for `config.json`, `requirements.txt`, or `README.md` files in the repository
4. Review the model card section which appears to be empty

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-18T12:29:38.878982+00:00_

# PR #380: GDN Parameter Initialization Analysis

## Overview
This merged PR (#380) addresses proper initialization of `A_log` and `dt_bias` parameters in the GatedDeltaNet model's `_init_weights` function.

## Key Problem Statement
The contributor noted: "When training GDN using `flame` framework, the initializations of `A_log` and `dt_bias` need to handled inside `_init_weights` function. Otherwise, the initialization would be overwritten."

## Parameters Modified

**Before:** These parameters lacked specialized initialization handling and could be overwritten during distributed training setup.

**After:** The `_init_weights` method now includes dedicated logic for GatedDeltaNet modules with:

- **A_log initialization**: Populated with `torch.log(A)` where A is uniformly distributed between 0-16
- **dt_bias initialization**: Set using inverse softplus transformation with parameters dt_min=0.001, dt_max=0.1, dt_init_floor=1e-4

Both parameters include safeguards:
- Detection of distributed tensor types (DTensor) with warning fallback
- Explicit flags: `_no_weight_decay = True` and `_no_reinit = True`

## Important Caveat
The PR includes a critical footnote: training GDN with the `flame` framework requires explicitly creating a seed checkpoint beforehand, as initialization might not work correctly otherwise.

## Code Path
File modified: `fla/models/gated_deltanet/modeling_gated_deltanet.py` (lines 124-157)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-18T12:29:38.879123+00:00_

Web search results for query: "github fla-org flash-linear-attention GatedDeltaNet "A_log" renamed "a_log" OR "attn.A" checkpoint breaking change"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"},{"title":"GitHub - Fzkuji/flash-linear: 🚀 Efficient implementations of state-of-the-art linear attention models in Pytorch and Triton","url":"https://github.com/Fzkuji/flash-linear-attention"},{"title":"flash-linear-attention/README.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/README.md"},{"title":"Home · fla-org/flash-linear-attention Wiki · GitHub","url":"https://github.com/fla-org/flash-linear-attention/wiki"},{"title":"[Bug] GatedDeltaNet backward error on Blackwell · Issue #607 · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/issues/607"},{"title":"flash-linear-attention/fla/ops/cp/README.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/fla/ops/cp/README.md"},{"title":"FLA · GitHub","url":"https://github.com/fla-org"},{"title":"GitHub - YJMSTR/cutile-flash-linear-attention: FLA but cuTile","url":"https://github.com/YJMSTR/cutile-flash-linear-attention"},{"title":"flash-linear-attention/examples/training.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/examples/training.md"}]

Based on my web search, I found relevant information about the GatedDeltaNet parameter renaming in the flash-linear-attention repository.

[Fix] Guard A_log and dt_bias re-initialization against loaded checkpoint values in GatedDeltaNet, Comba, and KDA by @ljxw88 in #754 appears in the release notes for the fla-org/fla
…[truncated 893 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-18T12:29:38.879269+00:00_

# PR #754 Summary: Guard A_log and dt_bias Re-initialization

## Problem Statement

Loading `GatedDeltaNet`, `Comba`, or `KimiDeltaAttention` checkpoints with transformers >= 5.0 caused "NaN outputs, causing the model to generate only padding/EOS tokens."

**Root cause:** The transformers 5.x library loads models on a meta device first. When `_init_weights` is called during checkpoint loading, the `_is_hf_initialized` flag is absent, causing parameters already loaded from the checkpoint to be re-initialized incorrectly:

- For `A_log`: Taking the logarithm of already-loaded negative values produces NaN
- For `dt_bias`: Re-applying transformations to loaded large negative values creates incorrect near-zero results

## Solution

Add `_is_hf_initialized` guards before initialization blocks:

```python
# Before
module.A_log.copy_(nn.init.uniform_(module.A_log, a=0, b=16).log())

# After
if not getattr(module.A_log, '_is_hf_initialized', False):
    module.A_log.copy_(nn.init.uniform_(module.A_log, a=0, b=16).log())
```

Same pattern applied to `dt_bias` across three model files:
- `fla/models/comba/modeling_comba.py`
- `fla/models/gated_deltanet/modeling_gated_deltanet.py`
- `fla/models/kda/modeling_kda.py`

## Status

**Merged** by sustcsonglin on Feb 25, 2026. The fix prevents unintended parameter reinitialization while preserving checkpoint-loaded values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-18T12:29:38.879419+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1/raw/main/config.json",
  "prompt": "Show the COMPLETE contents of this config.json file. I need to see every field, especially any field related to: auto_map, transformers_version, fla version, or any version/library references."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1/raw/main/config.json",
    "prompt": "Show the COMPLETE contents of this config.json file. I need to see every field, especially any field related to: auto_map, transformers_version, fla version, or any version/library references."
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-18T12:29:38.879552+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1/raw/main/config.json",
  "prompt": "Show the COMPLETE contents of this config.json file. I need every field, especially auto_map, transformers_version, fla version, or any version/library references."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1/raw/main/config.json",
    "prompt": "Show the COMPLETE contents of this config.json file. I need every field, especially auto_map, transformers_version, fla version, or any version/library references."
  }
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-18T12:29:38.879695+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/fla-org/flash-linear-attention/v0.5.0/fla/layers/gated_delta_net.py",
  "prompt": "Extract the COMPLETE source code. Show every parameter definition (nn.Parameter), every __init__ parameter, every reference to A_log, D, dt_bias, a_log, attn. Show the full class."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/fla-org/flash-linear-attention/v0.5.0/fla/layers/gated_delta_net.py",
    "prompt": "Extract the COMPLETE source code. Show every parameter definition (nn.Parameter), every __init__ parameter, every reference to A_log, D, dt_bias, a_log, attn. Show the full class."
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-18T12:29:38.879813+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-18T12:29:38.879933+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/fla-org/flash-linear-attention/v0.4.0/fla/layers/gated_delta_net.py",
  "prompt": "Extract the COMPLETE source code. Show every parameter definition (nn.Parameter), every __init__ parameter, every reference to A_log, D, dt_bias, a_log, attn. Show the full class."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/fla-org/flash-linear-attention/v0.4.0/fla/layers/gated_delta_net.py",
    "prompt": "Extract the COMPLETE source code. Show every parameter definition (nn.Parameter), every __init__ parameter, every reference to A_log, D, dt_bias, a_log, attn. Show the full class."
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-18T12:29:38.880060+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention",
  "prompt": "Find: 1) The latest release version or tag, 2) Any releases listed on the page, 3) The version number in setup.py or pyproject.toml if shown, 4) Recent commits or tags. List all version numbers visible on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention",
    "prompt": "Find: 1) The latest release version or tag, 2) Any releases listed on the page, 3) The version number in setup.py or pyproject.toml if shown, 4) Recent commits or tags. List all version numbers visible on this page."
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-18T12:29:38.880186+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"flash-linear-attention\" \"fla\" version pypi pip install site:github.com/fla-org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"flash-linear-attention\" \"fla\" version pypi pip install site:github.com/fla-org"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-18T12:29:38.880294+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-18T12:29:38.880411+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com/fla-org/flash-linear-attention GatedDeltaNet parameter rename commit \"A_log\" OR \"a_log\" OR \"attn.D\"",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com/fla-org/flash-linear-attention GatedDeltaNet parameter rename commit \"A_log\" OR \"a_log\" OR \"attn.D\"",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-18T12:29:38.880541+00:00_

# Complete Config.json Contents

Here is the **complete and entire** contents of the config.json file:

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/GatedDeltaNet/gated_deltanet_1.3B_3.json",
  "architectures": [
    "GatedDeltaNetForCausalLM"
  ],
  "attn": {
    "layers": [
      2,
      5,
      8,
      11,
      14,
      17,
      20,
      23
    ],
    "num_heads": 16,
    "num_kv_heads": 8,
    "qkv_bias": false,
    "rope_theta": 10000.0,
    "window_size": null
  },
  "attn_mode": "chunk",
  "bos_token_id": 1,
  "conv_size": 4,
  "eos_token_id": 2,
  "expand_k": 1,
  "expand_v": 1,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "head_dim": 256,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 2048,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "gated_deltanet",
  "norm_eps": 1e-06,
  "norm_first": false,
  "num_heads": 8,
  "num_hidden_layers": 24,
  "qk_activation": "silu",
  "qk_norm": "l2",
  "tie_word_embeddings": false,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_beta": true,
  "use_cache": true,
  "use_gate": true,
  "use_output_norm": true,
  "use_short_conv": true,
  "vocab_size": 32000
}
```

## Key Findings:

**Version/Library References Found:**
- **`transformers_version`**: `"4.49.0"` ✓

**NOT Present in this config:**
- `auto_map` - **Not included**
- `fla_version` - **Not included**
- Any other library/framework version references

This is a **GatedDeltaNet** 1.3B parameter model configuration with 24 hidden layers, using hybrid attention-convolution architecture with gating mechanisms.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-18T12:29:38.880696+00:00_

# Complete Config.json Contents

Here is the **complete and exhaustive** contents of the configuration file:

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/GatedDeltaNet/gated_deltanet_340M_24.json",
  "architectures": [
    "GatedDeltaNetForCausalLM"
  ],
  "attn": {
    "layers": [
      23
    ],
    "num_heads": 32,
    "num_kv_heads": 8,
    "qkv_bias": false,
    "rope_theta": 10000.0,
    "window_size": null
  },
  "attn_mode": "chunk",
  "bos_token_id": 1,
  "conv_size": 4,
  "eos_token_id": 2,
  "expand_k": 1,
  "expand_v": 1,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "head_dim": 256,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "gated_deltanet",
  "norm_eps": 1e-06,
  "norm_first": false,
  "num_heads": 4,
  "num_hidden_layers": 24,
  "qk_activation": "silu",
  "qk_norm": "l2",
  "tie_word_embeddings": false,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_beta": true,
  "use_cache": true,
  "use_gate": true,
  "use_output_norm": true,
  "use_short_conv": true,
  "vocab_size": 32000
}
```

## Key Version/Library References Found:
- **transformers_version**: `4.49.0`
- **torch_dtype**: `float32`
- **No auto_map field** present in this configuration
- **No fla_version field** present in this configuration

The config contains **31 fields total**. There are no additional version or library references beyond what is listed above.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-18T12:29:38.880831+00:00_

# Version Information from Flash Linear Attention Repository

## Latest Release
The latest release version is **v0.5.0**, dated April 21, 2026.

## All Listed Releases
The page indicates there are **13 total releases** available, with v0.5.0 being the most recent.

## Version Numbers Found

1. **v0.5.0** (Latest - April 21, 2026)
2. **v0.3.2** (mentioned in installation notes as a milestone for package split)
3. **v0.1** (mentioned in news section from May 2024)

## Additional Technical Requirements
The documentation specifies minimum dependencies including "PyTorch >= 2.7.0" and "Triton >= 3.3," though these are not release versions for the FLA project itself.

The page notes that 12 additional releases exist beyond v0.5.0, though specific version numbers for those earlier releases are not displayed in the provided content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-18T12:29:38.880969+00:00_

Web search results for query: ""flash-linear-attention" "fla" version pypi pip install site:github.com/fla-org"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"flash-linear-attention/FAQs.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/FAQs.md"},{"title":"flash-linear-attention/README.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/README.md"},{"title":"GitHub - fla-org/flash-bidirectional-linear-attention: Triton implement of bi-directional (non-causal) linear attention · GitHub","url":"https://github.com/fla-org/flash-bidirectional-linear-attention"},{"title":"GitHub - fla-org/flame: 🔥 A minimal training framework for scaling FLA models","url":"https://github.com/fla-org/flame"},{"title":"flash-linear-attention/setup.py at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/setup.py"},{"title":"flash-linear-attention/examples/training.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/examples/training.md"},{"title":"GitHub - fla-org/fla-zoo: Flash-Linear-Attention models beyond language · GitHub","url":"https://github.com/fla-org/fla-zoo"},{"title":"flash-linear-attention/fla/layers/linear_attn.py at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/fla/layers/linear_attn.py"},{"title":"flash-linear-attention/pyproject.toml at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/pyproject.toml"}]

Based on the search results, here's the information about flash-linear-attention (FLA):

## Installation

You can install fla with pip: `pip install flash-linear-attention`. Alternati
…[truncated 914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-18T12:29:38.881129+00:00_

Web search results for query: "site:github.com/fla-org/flash-linear-attention GatedDeltaNet parameter rename commit "A_log" OR "a_log" OR "attn.D""

Links: [{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"},{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"[Bug] triton error when run chunk gated deltanet op · Issue #196 · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/issues/196"},{"title":"[Bug]: Gated DeltaNet Recurrence with constant Gate at 1 vs. DeltaNet Recurrence · Issue #104 · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/issues/104"},{"title":"Commits · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/commits/main"},{"title":"flash-linear-attention/fla/layers/gla.py at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/fla/layers/gla.py"},{"title":"Home · fla-org/flash-linear-attention Wiki","url":"https://github.com/fla-org/flash-linear-attention/wiki"},{"title":"flash-linear-attention/fla/ops/ttt at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/tree/main/fla/ops/ttt"},{"title":"flash-linear-attention/FAQs.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/FAQs.md"},{"title":"[Linear Attention] Update fused_recurrent.py for inference with nomalization=true by yiyousong · Pull Request #268 · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/pull/268"}]

I found information about GatedDeltaNet in the releases page, including a mention of "A_log" in a fix commit. Let me search for more specific information about the parameter rename com
…[truncated 1536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-18T12:29:38.881279+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "gh api repos/fla-org/flash-linear-attention/contents/fla/layers/gated_delta_net.py --jq '.download_url' 2>/dev/null || echo \"gh not authenticated for this repo\"",
  "description": "Get download URL for gated_delta_net.py via GitHub API"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "gh api repos/fla-org/flash-linear-attention/contents/fla/layers/gated_delta_net.py --jq '.download_url' 2>/dev/null || echo \"gh not authenticated for this repo\"",
    "description": "Get download URL for gated_delta_net.py via GitHub API"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-18T12:29:38.881443+00:00_

gh not authenticated for this repo

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-18T12:29:38.881582+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/releases",
  "prompt": "List ALL release versions with their dates. I need to find which version would have been current around March-June 2025 when the m-a-p models were trained. List every release tag and date visible on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/releases",
    "prompt": "List ALL release versions with their dates. I need to find which version would have been current around March-June 2025 when the m-a-p models were trained. List every release tag and date visible on this page."
  }
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-18T12:29:38.881750+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/blob/main/fla/layers/gated_delta_net.py",
  "prompt": "Show ALL parameter definitions in this file. Look for nn.Parameter, self.A_log, self.a_log, self.D, self.dt_bias, or any parameter with 'log' or 'bias' in the name. Show the complete __init__ method of GatedDeltaNet class."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/blob/main/fla/layers/gated_delta_net.py",
    "prompt": "Show ALL parameter definitions in this file. Look for nn.Parameter, self.A_log, self.a_log, self.D, self.dt_bias, or any parameter with 'log' or 'bias' in the name. Show the complete __init__ method of GatedDeltaNet class."
  }
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-18T12:29:38.881889+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flame",
  "prompt": "Find: 1) Any requirements.txt, setup.py, or pyproject.toml that pins the flash-linear-attention version, 2) Any mention of fla version requirements, 3) Installation instructions that specify a version. Look for dependency specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flame",
    "prompt": "Find: 1) Any requirements.txt, setup.py, or pyproject.toml that pins the flash-linear-attention version, 2) Any mention of fla version requirements, 3) Installation instructions that specify a version. Look for dependency specifications."
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-18T12:29:38.882006+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-18T12:29:38.882130+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "fla-org flash-linear-attention \"GatedDeltaNet\" checkpoint loading error \"unexpected key\" OR \"missing key\" A_log state_dict",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "fla-org flash-linear-attention \"GatedDeltaNet\" checkpoint loading error \"unexpected key\" OR \"missing key\" A_log state_dict",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-18T12:29:38.882257+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2507.06457 \"systematic analysis hybrid linear attention\" Wang flash-linear-attention version code github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2507.06457 \"systematic analysis hybrid linear attention\" Wang flash-linear-attention version code github"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-18T12:29:38.882371+00:00_

# Flash-Linear-Attention Release Versions and Dates

Based on the GitHub releases page, here are all visible release versions with their dates:

1. **v0.5.0** - April 21, 2025
2. **v0.4.2** - March 12, 2025
3. **v0.4.1** - December 24, 2024
4. **v0.4.0** - October 27, 2024
5. **v0.3.2** - September 10, 2024
6. **v0.3.1** - August 26, 2024
7. **v0.3.0** - July 14, 2024
8. **v0.2.2** - June 5, 2024
9. **v0.2.1** - April 23, 2024
10. **v0.2.0** - April 11, 2024

## For March-June 2025 Training Timeline

If the m-a-p models were trained during March-June 2025, the current versions would have been:
- **v0.4.2** (March 12, 2025) through **v0.5.0** (April 21, 2025)

The v0.5.0 release represents "the main new model this release is MoBA / FlashMoBA" and introduces multi-backend support moving beyond Triton-only infrastructure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-18T12:29:38.882487+00:00_

# Flash-Linear-Attention Version Requirements

Based on the GitHub repository content, here are the relevant dependency specifications:

## Installation Instructions

The setup guide includes this specific instruction:

> "pip uninstall flash-linear-attention && pip install -U --no-use-pep517 git+https://github.com/fla-org/flash-linear-attention"

This command installs the latest development version from the GitHub repository without pinning to a specific release version.

## Related Dependencies

The framework also requires a specific torchtitan version:

> "pip install git+https://github.com/pytorch/torchtitan.git@0b44d4c"

## Additional Notes

- No explicit version pin (like `flash-linear-attention==X.Y.Z`) appears in the provided content
- The installation uses the `-U` flag to upgrade to the newest available version
- The `--no-use-pep517` flag suggests building directly from source
- While `pyproject.toml` and `setup.py` files are mentioned in the repository structure, their specific contents are not shown in the provided material

The developers recommend using recent versions: **torch>=2.6** and **triton>=3.0** for optimal compatibility with torch.compile features.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-18T12:29:38.882630+00:00_

Web search results for query: "fla-org flash-linear-attention "GatedDeltaNet" checkpoint loading error "unexpected key" OR "missing key" A_log state_dict"

Links: [{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"},{"title":"[Bug] GatedDeltaNet backward error on Blackwell · Issue #607 · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/issues/607"},{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"[Bug] triton error when run chunk gated deltanet op · Issue #196 · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/issues/196"},{"title":"Unexpected key(s) in state_dict Error when calling `load_from_checkpoint` · Issue #3629 · Lightning-AI/pytorch-lightning","url":"https://github.com/PyTorchLightning/pytorch-lightning/issues/3629"},{"title":"[BUG]\"Unexpected key(s) in state_dict\" while loading Llama-megatron checkpoint. · Issue #1132 · NVIDIA/Megatron-LM","url":"https://github.com/NVIDIA/Megatron-LM/issues/1132"},{"title":"RunTimeError Missing keys while resuming training and cannot load checkpoint · Issue #1453 · huggingface/peft","url":"https://github.com/huggingface/peft/issues/1453"},{"title":"[modeling] keys to ignore revisited · Issue #16719 · huggingface/transformers","url":"https://github.com/huggingface/transformers/issues/16719"},{"title":"Unexpected key(s) in state_dict Error when calling `load_from_checkpoint` · Issue #3629 · Lightning-AI/lightning","url":"https://github.com/Lightning-AI/lightning/issues/3629"},{"title":"SAM 2.1 Model Loading Error (Unexpected key(s) in state_dict) · Issue #337 · facebookresearch/sam2","url":"https://github.com/facebookresearch/sam2/issues/337"}]

Based on the search results, I found relevant information about your query:

There was a fix that guar
…[truncated 948 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-18T12:29:38.882806+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "gh api repos/fla-org/flash-linear-attention/contents/fla/layers/gated_delta_net.py -H \"Accept: application/vnd.github.raw+json\" 2>&1 | head -200",
  "description": "Fetch raw gated_delta_net.py source via GitHub API"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "gh api repos/fla-org/flash-linear-attention/contents/fla/layers/gated_delta_net.py -H \"Accept: application/vnd.github.raw+json\" 2>&1 | head -200",
    "description": "Fetch raw gated_delta_net.py source via GitHub API"
  }
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-18T12:29:38.882921+00:00_

/bin/bash: line 1: gh: command not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-18T12:29:38.883038+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers/gated_delta_net.py\" -H \"Accept: application/vnd.github.raw+json\" 2>&1 | head -300",
  "description": "Fetch raw gated_delta_net.py source via curl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers/gated_delta_net.py\" -H \"Accept: application/vnd.github.raw+json\" 2>&1 | head -300",
    "description": "Fetch raw gated_delta_net.py source via curl"
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-18T12:29:38.883146+00:00_

{
  "message": "Not Found",
  "documentation_url": "https://docs.github.com/rest/repos/contents#get-repository-content",
  "status": "404"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-18T12:29:38.883295+00:00_

Web search results for query: "arxiv 2507.06457 "systematic analysis hybrid linear attention" Wang flash-linear-attention version code github"

Links: [{"title":"[2507.06457] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457"},{"title":"[2507.06457v1] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457v1"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/pdf/2507.06457"},{"title":"[PDF] A Systematic Analysis of Hybrid Linear Attention | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Systematic-Analysis-of-Hybrid-Linear-Attention-Wang-Zhu/f7ad9ebc481e23ae7fa90d98d3814518e94adcd1"},{"title":"(PDF) A Systematic Analysis of Hybrid Linear Attention","url":"https://www.researchgate.net/publication/393538945_A_Systematic_Analysis_of_Hybrid_Linear_Attention"},{"title":"Paper page - A Systematic Analysis of Hybrid Linear Attention","url":"https://huggingface.co/papers/2507.06457"},{"title":"A Systematic Analysis of Hybrid Linear Attention | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/systematic-analysis-hybrid-linear-attention"},{"title":"Alphaxiv","url":"https://www.alphaxiv.org/overview/2507.06457v1"},{"title":"Hybrid Linear Attention Done Right: Efficient Distillation ...","url":"https://arxiv.org/pdf/2601.22156"},{"title":"Hybrid Architectures for Language Models: Systematic Analysis and Design Insights","url":"https://arxiv.org/html/2510.04800v1"}]

Now let me search for the GitHub code repository related to this paper:

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"GitHub - Fzkuji/flash-linear: 🚀 Efficient implementations of state-of-the-art linear attention models in Pytorch and Triton","url":"https://github.com/Fzkuji/flash-linear-attention"},{"title":"Releases · fla-o
…[truncated 4674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-18T12:29:38.883485+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers/gated_delta_net.py\" -H \"Accept: application/vnd.github.raw+json\" 2>&1 | tail -n +300 | head -200",
  "description": "Fetch remaining lines of gated_delta_net.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers/gated_delta_net.py\" -H \"Accept: application/vnd.github.raw+json\" 2>&1 | tail -n +300 | head -200",
    "description": "Fetch remaining lines of gated_delta_net.py"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-18T12:29:38.883607+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-18T12:29:38.883747+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers\" -H \"Accept: application/json\" 2>&1 | python3 -c \"import sys,json; data=json.load(sys.stdin); [print(x['name']) for x in data if 'delta' in x['name'].lower() or 'gdn' in x['name'].lower() or 'gated' in x['name'].lower()]\" 2>&1",
  "description": "List files with delta/gdn/gated in fla/layers directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers\" -H \"Accept: application/json\" 2>&1 | python3 -c \"import sys,json; data=json.load(sys.stdin); [print(x['name']) for x in data if 'delta' in x['name'].lower() or 'gdn' in x['name'].lower() or 'gated' in x['name'].lower()]\" 2>&1",
    "description": "List files with delta/gdn/gated in fla/layers directory"
  }
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-18T12:29:38.883877+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flame/blob/main/pyproject.toml",
  "prompt": "Show the COMPLETE contents of this pyproject.toml. I need to see all dependency specifications, especially any flash-linear-attention or fla version pins."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flame/blob/main/pyproject.toml",
    "prompt": "Show the COMPLETE contents of this pyproject.toml. I need to see all dependency specifications, especially any flash-linear-attention or fla version pins."
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-18T12:29:38.883987+00:00_

delta_net.py
deltaformer.py
gated_deltanet.py
gated_deltaproduct.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-18T12:29:38.884102+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/papers/2507.06457",
  "prompt": "Find any discussion comments, author responses, or additional information about the paper. Look for any mention of flash-linear-attention version, code repository, or implementation details shared in comments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/papers/2507.06457",
    "prompt": "Find any discussion comments, author responses, or additional information about the paper. Look for any mention of flash-linear-attention version, code repository, or implementation details shared in comments."
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-18T12:29:38.884229+00:00_

&lt;persisted-output>
Output too large (63.9KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft/862a51fb-ad20-4c48-8de6-4985ffc65890/tool-results/toolu_01Nx4h9kyXz4ELf6tJzTqbja.txt

Preview (first 2KB):
Title: A Systematic Analysis of Hybrid Linear Attention

URL Source: https://arxiv.org/html/2507.06457

Markdown Content:
1]UC Santa Cruz 2]ByteDance Seed 3]University of Groningen 4]CASIA 5]PolyU 6]M-A-P \contribution[*]Equal Contribution \contribution[†]Corresponding authors

Rui-Jie Zhu 

Steven Abreu Yong Shan Taylor Kergan Yuqi Pan Yuhong Chou Zheng Li Ge Zhang Wenhao Huang Jason Eshraghian [ [ [ [ [ [ [zhangge.eli@bytedance.com](mailto:zhangge.eli@bytedance.com)[jsn@ucsc.edu](mailto:jsn@ucsc.edu)

(July 8, 2025)

###### Abstract

Transformers face quadratic complexity and memory issues with long sequences, prompting the adoption of linear attention mechanisms using fixed-size hidden states. However, linear models often suffer from limited recall performance, leading to hybrid architectures that combine linear and full attention layers. Despite extensive hybrid architecture research, the choice of linear attention component has not been deeply explored. We systematically evaluate various linear attention models across generations—vector recurrences to advanced gating mechanisms—both standalone and hybridized. To enable this comprehensive analysis, we trained and open-sourced 72 models***Our model training and inference are both implemented using the [flash-linear-attention](https://github.com/fla-org/flash-linear-attention) library.: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios. Benchmarking on standard language modeling and recall tasks reveals that superior standalone linear models do not necessarily excel in hybrids. While language modeling remains stable across linear-
…[truncated 317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-18T12:29:38.884372+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/blob/main/setup.py",
  "prompt": "Show the COMPLETE contents of setup.py. I need the version number defined in this file."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/blob/main/setup.py",
    "prompt": "Show the COMPLETE contents of setup.py. I need the version number defined in this file."
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-18T12:29:38.884499+00:00_

# FLAME pyproject.toml Contents

Based on the GitHub page content provided, here is the complete pyproject.toml file:

```toml
[project]
name = "flame"
dynamic = ["version"]
description = "A minimal training framework for scaling FLA models"
readme = "README.md"
authors = [
{ name = "Songlin Yang", email = "yangsl66@mit.edu" },
{ name = "Yu Zhang", email = "yzhang.cs@outlook.com" },
]
license = { file = "LICENSE" }
classifiers = [
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
"Topic :: Scientific/Engineering :: Artificial Intelligence",
]
requires-python = ">=3.10"
dependencies = [
'flash-linear-attention',
'torch>=2.5',
'torchdata',
'transformers>=4.45.0',
'triton>=3.0',
'datasets>=3.3.0',
'einops',
'ninja',
'wandb',
'tiktoken',
'tensorboard',
]

[project.optional-dependencies]
dev = ["pytest"]

[project.urls]
Homepage = "https://github.com/fla-org/flame"

[build-system]
requires = ["setuptools>=45", "wheel", "ninja", "torch"]

[tool.isort]
line_length = 127
multi_line_output = 3
```

**Key Finding:** The `flash-linear-attention` dependency has **no version pin specified**—it will install the latest available version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-18T12:29:38.884655+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://pypi.org/project/flash-linear-attention/",
  "prompt": "List ALL release versions with dates available on PyPI. I need the complete version history to determine which version was current in early 2025."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://pypi.org/project/flash-linear-attention/",
    "prompt": "List ALL release versions with dates available on PyPI. I need the complete version history to determine which version was current in early 2025."
  }
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-18T12:29:38.884788+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers/gated_deltanet.py\" -H \"Accept: application/vnd.github.raw+json\" 2>&1",
  "description": "Fetch raw gated_deltanet.py source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers/gated_deltanet.py\" -H \"Accept: application/vnd.github.raw+json\" 2>&1",
    "description": "Fetch raw gated_deltanet.py source"
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-18T12:29:38.884940+00:00_

# Copyright (c) 2023-2026, Songlin Yang, Yu Zhang, Zhiyuan Li
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
# For a list of all contributors, visit:
#   https://github.com/fla-org/flash-linear-attention/graphs/contributors

from __future__ import annotations

import math
import warnings
from typing import TYPE_CHECKING

import torch
import torch.nn as nn
from einops import rearrange
from torch.nn import functional as F

from fla.layers.utils import get_layer_cache, get_unpad_data, index_first_axis, pad_input, update_layer_cache
from fla.modules import FusedRMSNormGated, RMSNorm, ShortConvolution
from fla.ops.gated_delta_rule import chunk_gated_delta_rule, fused_recurrent_gated_delta_rule

if TYPE_CHECKING:
    from transformers.processing_utils import Unpack

    from fla.models.utils import Cache


class GatedDeltaNet(nn.Module):
    """
    Gated Delta Networks (GDN) layer implementation.

    Reference: `Gated Delta Networks: Improving Mamba2 with Delta Rule &lt;https://arxiv.org/abs/2412.06464>`_

    Similar to Mamba2, each layer contains around 6*hidden_size*hidden_size parameters.

    Parameter allocation when use_gate=True:
        - 0.75 * hidden_size * hidden_size for the q_proj and k_proj each
        - 1.5 * hidden_size * hidden_size for the v_proj, g_proj and o_proj each
        - Others are ignorably small.
        - In total = 0.75 * 2 + 1.5 * 3 = 6 * hidden_size * hidden_size
    NOTE: num_heads * head_dim = 0.75 * hidden_size, please make sure to set the correct num_heads and head_dim.

    Parameter allocation when use_gate=False:
        - 1 * hidden_size * hidden_size for the q_proj and k_proj each
        - 2 * hidden_size * hidden_size for the v_proj and o_proj each
        - Others are ignorably small.
        - In total = 1 * 2 + 2 * 2 = 6 * hidden_size * hidden_size

    Args:
        hidden_size (int, Optional):
            The hidden size of the input. Default: 2
…[truncated 11413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-18T12:29:38.885075+00:00_

# Setup.py Contents

The setup.py file shown is complete. However, **the actual version number is not hardcoded in this file**. Instead, it's dynamically retrieved from the package's `__init__.py`:

```python
def get_package_version():
    init_file = Path(os.path.dirname(os.path.abspath(__file__))) / 'fla' / '__init__.py'
    with open(init_file) as f:
        version_match = re.search(r"^__version__\s*=\s*(.*)", f.read(), re.MULTILINE)
```

The version is "extracted from the `fla/__init__.py` file at package initialization time." To find the actual version number, you would need to check that `__init__.py` file, which is not displayed in the provided content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-18T12:29:38.885201+00:00_

# Flash Linear Attention Release History

Based on the PyPI page, here is the complete version history with release dates:

| Version | Release Date |
|---------|--------------|
| 0.5.0 | Apr 21, 2026 |
| 0.4.2 | Mar 12, 2026 |
| 0.4.1 | Dec 24, 2025 |
| 0.4.0 | Oct 27, 2025 |
| 0.3.2 | Sep 10, 2025 |
| 0.3.1 | Aug 26, 2025 |
| 0.3.0 | Jul 14, 2025 |
| 0.2.2 | Jun 5, 2025 |
| 0.2.1 | Apr 23, 2025 |
| 0.2.0 | Apr 11, 2025 |
| 0.1.2 | Mar 31, 2025 |
| 0.1.1 | Mar 24, 2025 |
| 0.1 | Mar 20, 2025 |

## Early 2025 Status

In early 2025 (January-February), version 0.1 would have been the current release, having launched on March 20, 2025. The package was in its initial stages, offering "a collection of implementations for state-of-the-art linear attention models."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-18T12:29:38.885328+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/tags?per_page=20\" | python3 -c \"import sys,json; [print(t['name']) for t in json.load(sys.stdin)]\" 2>&1",
  "description": "List all tags in the fla repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/tags?per_page=20\" | python3 -c \"import sys,json; [print(t['name']) for t in json.load(sys.stdin)]\" 2>&1",
    "description": "List all tags in the fla repo"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-18T12:29:38.885440+00:00_

v0.5.0
v0.4.2
v0.4.1
v0.4.0
v0.3.2
v0.3.1
v0.3.0
v0.2.2
v0.2.1
v0.2.0
v0.1.2
v0.1.1
v0.1.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-18T12:29:38.885559+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft/862a51fb-ad20-4c48-8de6-4985ffc65890/tool-results/toolu_01Nx4h9kyXz4ELf6tJzTqbja.txt",
  "limit": "200",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft/862a51fb-ad20-4c48-8de6-4985ffc65890/tool-results/toolu_01Nx4h9kyXz4ELf6tJzTqbja.txt",
    "limit": "200",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-18T12:29:38.885836+00:00_

0	Title: A Systematic Analysis of Hybrid Linear Attention
1	
2	URL Source: https://arxiv.org/html/2507.06457
3	
4	Markdown Content:
5	1]UC Santa Cruz 2]ByteDance Seed 3]University of Groningen 4]CASIA 5]PolyU 6]M-A-P \contribution[*]Equal Contribution \contribution[†]Corresponding authors
6	
7	Rui-Jie Zhu 
8	
9	Steven Abreu Yong Shan Taylor Kergan Yuqi Pan Yuhong Chou Zheng Li Ge Zhang Wenhao Huang Jason Eshraghian [ [ [ [ [ [ [zhangge.eli@bytedance.com](mailto:zhangge.eli@bytedance.com)[jsn@ucsc.edu](mailto:jsn@ucsc.edu)
10	
11	(July 8, 2025)
12	
13	###### Abstract
14	
15	Transformers face quadratic complexity and memory issues with long sequences, prompting the adoption of linear attention mechanisms using fixed-size hidden states. However, linear models often suffer from limited recall performance, leading to hybrid architectures that combine linear and full attention layers. Despite extensive hybrid architecture research, the choice of linear attention component has not been deeply explored. We systematically evaluate various linear attention models across generations—vector recurrences to advanced gating mechanisms—both standalone and hybridized. To enable this comprehensive analysis, we trained and open-sourced 72 models***Our model training and inference are both implemented using the [flash-linear-attention](https://github.com/fla-org/flash-linear-attention) library.: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios. Benchmarking on standard language modeling and recall tasks reveals that superior standalone linear models do not necessarily excel in hybrids. While language modeling remains stable across linear-to-full attention ratios, recall significantly improves with increased full attention layers, particularly below a 3:1 ratio. Our study highlights selective gating, hierarchical recurrence, and controlled forgetting as critical for effective hybrid models
…[truncated 40589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-18T12:29:38.886016+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers/gated_deltanet.py?ref=v0.3.2\" -H \"Accept: application/vnd.github.raw+json\" 2>&1",
  "description": "Fetch gated_deltanet.py at v0.3.2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers/gated_deltanet.py?ref=v0.3.2\" -H \"Accept: application/vnd.github.raw+json\" 2>&1",
    "description": "Fetch gated_deltanet.py at v0.3.2"
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-18T12:29:38.886183+00:00_

# -*- coding: utf-8 -*-
# Copyright (c) 2023-2025, Songlin Yang, Yu Zhang

from __future__ import annotations

import math
import warnings
from typing import TYPE_CHECKING, Dict, Optional, Tuple

import torch
import torch.nn as nn
from einops import rearrange, repeat
from torch.nn import functional as F

from fla.layers.utils import get_unpad_data, index_first_axis, pad_input
from fla.modules import FusedRMSNormGated, RMSNorm, ShortConvolution
from fla.ops.gated_delta_rule import chunk_gated_delta_rule, fused_recurrent_gated_delta_rule

if TYPE_CHECKING:
    from transformers.processing_utils import Unpack

    from fla.models.utils import Cache


@torch.compile
def elu_p1(x):
    return (F.elu(x, 1., False) + 1.).to(x)


@torch.compile
def sum_norm(x):
    return (x / x.sum(-1, keepdim=True)).to(x)


class GatedDeltaNet(nn.Module):
    """
    The layer implementaion for [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://arxiv.org/abs/2412.06464).  # noqa

    Similar to Mamba2, each layer contains around 6*hidden_size*hidden_size parameters.

    Parameter alloation when use_gate=True:
        - 0.75 * hidden_size * hidden_size for the q_proj and k_proj each
        - 1.5 * hidden_size * hidden_size for the v_proj, g_proj and o_proj each
        - Others are ignorably small.
        - In total = 0.75 * 2 + 1.5 * 3 = 6 * hidden_size * hidden_size
    NOTE: num_heads * head_dim = 0.75 * hidden_size, please make sure to set the correct num_heads and head_dim.

    Parameter allocation when use_gate=False:
        - 1 * hidden_size * hidden_size for the q_proj and k_proj each
        - 2 * hidden_size * hidden_size for the v_proj and o_proj each
        - Others are ignorably small.
        - In total = 1 * 2 + 2 * 2 = 6 * hidden_size * hidden_size

    Args:
        hidden_size (int, Optional):
            The hidden size of the input. Default: 2048.
        expand_v (float, Optional):
            The expansion ratio for the value dim. Default: 2.0.
   
…[truncated 11186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-18T12:29:38.886335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft/862a51fb-ad20-4c48-8de6-4985ffc65890/tool-results/toolu_01Nx4h9kyXz4ELf6tJzTqbja.txt",
  "limit": "200",
  "offset": "199"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft/862a51fb-ad20-4c48-8de6-4985ffc65890/tool-results/toolu_01Nx4h9kyXz4ELf6tJzTqbja.txt",
    "limit": "200",
    "offset": "199"
  }
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-18T12:29:38.886551+00:00_

199	Table 5: Recall performance results from each linear attention variant and ratio are averaged. Total average represents the aggregate score for each ratio.
200	
201	### 4.4 Performance-Efficiency Pareto Front
202	
203	We further explore the Pareto Front of performance and efficiency for all hybrid models considered herein. We relate the FLOPs of the token mixers to the language modeling performance for each model and hybridization setting (averaged over all benchmarks and both model sizes). Details for the FLOP calculation are presented in Appendix [A](https://arxiv.org/html/2507.06457v1#A1 "Appendix A Forward-Pass FLOP Analysis of Token Mixers ‣ A Systematic Analysis of Hybrid Linear Attention"). Figure [5(a)](https://arxiv.org/html/2507.06457v1#S4.F5.sf1 "Figure 5(a) ‣ Figure 5 ‣ 4.4 Performance-Efficiency Pareto Front ‣ 4 Empirical Study ‣ A Systematic Analysis of Hybrid Linear Attention") shows this Pareto Front with the FLOPs calculated for the 1.3B parameter models and a sequence length of 4,096. The Pareto Front of optimality is shown with a dashed line. It is immediately evident that the pure HGRN model, due to its vector-sized state, uses orders of magnitude fewer FLOPs than all other models. The full transformer model is on the opposite end of the Pareto Front, representing the highest performance and lowest efficiency. The middle of the Pareto Front is occupied by the HGRN 24:1 model and the HGRN2 6:1 model.
204	
205	![Image 5: Refer to caption](https://arxiv.org/html/2507.06457v1/x3.png)
206	
207	(a)Sequence length L=4096 𝐿 4096 L=4096 italic_L = 4096.
208	
209	![Image 6: Refer to caption](https://arxiv.org/html/2507.06457v1/x4.png)
210	
211	(b)Sequence length L=32768 𝐿 32768 L=32768 italic_L = 32768.
212	
213	Figure 5: Performance-Efficiency Pareto Front where FLOPs are calculated for the 1.3B parameter models with two different sequence lengths. Note that the y-axis is inverted so that the Pareto Front can be clearly seen towards the top-right.
214
…[truncated 22104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-18T12:29:38.886752+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers/gated_deltanet.py?ref=v0.4.0\" -H \"Accept: application/vnd.github.raw+json\" 2>&1 | head -200",
  "description": "Fetch gated_deltanet.py at v0.4.0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers/gated_deltanet.py?ref=v0.4.0\" -H \"Accept: application/vnd.github.raw+json\" 2>&1 | head -200",
    "description": "Fetch gated_deltanet.py at v0.4.0"
  }
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-18T12:29:38.886888+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers/gated_deltanet.py?ref=v0.2.0\" -H \"Accept: application/vnd.github.raw+json\" 2>&1",
  "description": "Fetch gated_deltanet.py at v0.2.0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers/gated_deltanet.py?ref=v0.2.0\" -H \"Accept: application/vnd.github.raw+json\" 2>&1",
    "description": "Fetch gated_deltanet.py at v0.2.0"
  }
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-18T12:29:38.887031+00:00_

# -*- coding: utf-8 -*-
# Copyright (c) 2023-2025, Songlin Yang, Yu Zhang

from __future__ import annotations

import math
import warnings
from typing import TYPE_CHECKING, Dict, Optional, Tuple

import torch
import torch.nn as nn
from einops import rearrange, repeat
from torch.nn import functional as F

from fla.layers.utils import get_unpad_data, index_first_axis, pad_input
from fla.modules import FusedRMSNormGated, RMSNorm, ShortConvolution
from fla.ops.gated_delta_rule import chunk_gated_delta_rule, fused_recurrent_gated_delta_rule

if TYPE_CHECKING:
    from transformers.processing_utils import Unpack

    from fla.models.utils import Cache


@torch.compile
def elu_p1(x):
    return (F.elu(x, 1., False) + 1.).to(x)


@torch.compile
def sum_norm(x):
    return (x / x.sum(-1, keepdim=True)).to(x)


class GatedDeltaNet(nn.Module):
    """
    The layer implementaion for [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://arxiv.org/abs/2412.06464).  # noqa

    Similar to Mamba2, each layer contains around 6*hidden_size*hidden_size parameters.

    Parameter alloation when use_gate=True:
        - 0.75 * hidden_size * hidden_size for the q_proj and k_proj each
        - 1.5 * hidden_size * hidden_size for the v_proj, g_proj and o_proj each
        - Others are ignorably small.
        - In total = 0.75 * 2 + 1.5 * 3 = 6 * hidden_size * hidden_size
    NOTE: num_heads * head_dim = 0.75 * hidden_size, please make sure to set the correct num_heads and head_dim.

    Parameter allocation when use_gate=False:
        - 1 * hidden_size * hidden_size for the q_proj and k_proj each
        - 2 * hidden_size * hidden_size for the v_proj and o_proj each
        - Others are ignorably small.
        - In total = 1 * 2 + 2 * 2 = 6 * hidden_size * hidden_size

    Args:
        hidden_size (int, Optional):
            The hidden size of the input. Default: 2048.
        expand_v (float, Optional):
            The expansion ratio for the value dim. Default: 2.0.
   
…[truncated 6338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-18T12:29:38.887210+00:00_

# -*- coding: utf-8 -*-
# Copyright (c) 2023-2025, Songlin Yang, Yu Zhang

from __future__ import annotations

import math
from typing import TYPE_CHECKING, Dict, Optional, Tuple

import torch
import torch.nn as nn
from einops import rearrange
from torch.nn import functional as F

from fla.layers.utils import get_unpad_data, index_first_axis, pad_input
from fla.modules import FusedRMSNormGated, RMSNorm, ShortConvolution
from fla.ops.gated_delta_rule import chunk_gated_delta_rule, fused_recurrent_gated_delta_rule

if TYPE_CHECKING:
    from transformers.processing_utils import Unpack

    from fla.models.utils import Cache


@torch.compile
def elu_p1(x):
    return (F.elu(x, 1., False) + 1.).to(x)


@torch.compile
def sum_norm(x):
    return (x / x.sum(-1, keepdim=True)).to(x)


class GatedDeltaNet(nn.Module):
    """
    The layer implementaion for [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://arxiv.org/abs/2412.06464).  # noqa

    Similar to Mamba2, each layer contains around 6*hidden_size*hidden_size parameters.

    Parameter alloation when use_gate=True:
        - 0.75 * hidden_size * hidden_size for the q_proj and k_proj each
        - 1.5 * hidden_size * hidden_size for the v_proj, g_proj and o_proj each
        - Others are ignorably small.
        - In total = 0.75 * 2 + 1.5 * 3 = 6 * hidden_size * hidden_size
    NOTE: num_heads * head_dim = 0.75 * hidden_size, please make sure to set the correct num_heads and head_dim.

    Parameter allocation when use_gate=False:
        - 1 * hidden_size * hidden_size for the q_proj and k_proj each
        - 2 * hidden_size * hidden_size for the v_proj and o_proj each
        - Others are ignorably small.
        - In total = 1 * 2 + 2 * 2 = 6 * hidden_size * hidden_size

    Args:
        hidden_size (int, Optional):
            The hidden size of the input. Default: 2048.
        expand_v (float, Optional):
            The expansion ratio for the value dim. Default: 2.0.
        head_dim (int, Opti
…[truncated 9859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-18T12:29:38.887380+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://pypi.org/project/flash-linear-attention/#history",
  "prompt": "List ALL versions with their exact release dates. I need the complete version history table."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://pypi.org/project/flash-linear-attention/#history",
    "prompt": "List ALL versions with their exact release dates. I need the complete version history table."
  }
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-18T12:29:38.887528+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/releases/tag/v0.4.2",
  "prompt": "Show the release notes for v0.4.2. What changes were included? What was the date? Any breaking changes or new model support mentioned?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/releases/tag/v0.4.2",
    "prompt": "Show the release notes for v0.4.2. What changes were included? What was the date? Any breaking changes or new model support mentioned?"
  }
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-18T12:29:38.887692+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/releases/tag/v0.4.1",
  "prompt": "Show the release notes for v0.4.1. What changes were included? What was the date? List all details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/releases/tag/v0.4.1",
    "prompt": "Show the release notes for v0.4.1. What changes were included? What was the date? List all details."
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-18T12:29:38.887827+00:00_

# Flash Linear Attention - Complete Version History

Based on the PyPI page, here is the complete release history with dates:

| Version | Release Date |
|---------|---|
| 0.5.0 | Apr 21, 2026 |
| 0.4.2 | Mar 12, 2026 |
| 0.4.1 | Dec 24, 2025 |
| 0.4.0 | Oct 27, 2025 |
| 0.3.2 | Sep 10, 2025 |
| 0.3.1 | Aug 26, 2025 |
| 0.3.0 | Jul 14, 2025 |
| 0.2.2 | Jun 5, 2025 |
| 0.2.1 | Apr 23, 2025 |
| 0.2.0 | Apr 11, 2025 |
| 0.1.2 | Mar 31, 2025 |
| 0.1.1 | Mar 24, 2025 |
| 0.1 | Mar 20, 2025 |

The current stable release is **0.5.0** (April 2026), which provides "efficient implementations for emerging model architectures, with a focus on efficient sequence modeling."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-18T12:29:38.887962+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "A_log|dt_bias|a_log|attn\\.D",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Grep",
  "tool_args": {
    "pattern": "A_log|dt_bias|a_log|attn\\.D",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-18T12:29:38.888112+00:00_

mistakes.yaml:57:  summary: fla 0.5.0 与 Wang et al. 模型不兼容（训练时用 ~0.4.x），GatedDeltaNet 的 attn.D 参数被丢弃导致输出随机噪声
mistakes.yaml:59:    版本。fla 0.5.0 的 GatedDeltaNet 架构变更导致 checkpoint 参数不匹配（attn.D 被标记为 UNEXPECTED 并丢弃）。
logs/chats/feishu_group_oc_40962fa57a434c0fa984bdc62b106f2e_reviewer.jsonl:512:[Omitted long matching line]
logs/chats/feishu_group_oc_40962fa57a434c0fa984bdc62b106f2e_reviewer.jsonl:682:{"ts": "2026-05-18T12:19:45.023966+00:00", "role": "tool", "session": "feishu:group:oc_40962fa57a434c0fa984bdc62b106f2e:reviewer", "text": "called mcp__agent-ml-research__ssh_read_only", "tool": "mcp__agent-ml-research__ssh_read_only", "tool_args": {"server": "westb-48145", "command": "grep -n \"self.D\\|self\\.A_log\\|attn.D\" /root/miniconda3/lib/python3.12/site-packages/fla/layers/gated_deltanet.py"}}
logs/chats/feishu_group_oc_40962fa57a434c0fa984bdc62b106f2e_reviewer.jsonl:700:[Omitted long matching line]
logs/chats/feishu_group_oc_1f8f0d6d9482071694045c30143bb993_director.jsonl:320:[Omitted long matching line]
logs/chats/feishu_group_oc_1f8f0d6d9482071694045c30143bb993_director.jsonl:321:[Omitted long matching line]
logs/chats/feishu_group_oc_1f8f0d6d9482071694045c30143bb993_director.jsonl:323:[Omitted long matching line]
logs/chats/feishu_group_oc_1f8f0d6d9482071694045c30143bb993_director.jsonl:326:[Omitted long matching line]
logs/chats/feishu_group_oc_1f8f0d6d9482071694045c30143bb993_director.jsonl:327:[Omitted long matching line]
logs/chats/feishu_group_oc_1f8f0d6d9482071694045c30143bb993_director.jsonl:328:[Omitted long matching line]
logs/chats/feishu_group_oc_40962fa57a434c0fa984bdc62b106f2e.jsonl:483:[Omitted long matching line]
logs/chats/feishu_group_oc_40962fa57a434c0fa984bdc62b106f2e.jsonl:486:[Omitted long matching line]
logs/chats/feishu_group_oc_40962fa57a434c0fa984bdc62b106f2e.jsonl:488:[Omitted long matching line]
logs/workers/worker_code_logprob-eval_20260518T072542.log:24:[Omitted long matching line]
logs/workers/worker_code_logprob-eval_20260518T0725
…[truncated 7963 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-18T12:29:38.888248+00:00_

# Release Notes for v0.4.1

**Release Date:** December 24

**Notable Changes:**

The v0.4.1 release included 30+ commits addressing performance optimizations and bug fixes across multiple components:

**Key Improvements:**
- "Fix oom on A6000" memory issue resolution
- KDA (kernel) optimizations including fused gate operations and intra-chunk attention improvements
- Precision fixes for RMSNorm dtype handling
- L2Norm recompilation avoidance for variable-length inputs
- NSA layer enhancements with head_dim parameter support
- GDN out-of-bounds bug corrections

**Bug Fixes:**
- Fixed weight decay term in KDA
- Corrected K/V dimension mismatches in attention backward kernels
- Resolved contiguous memory layout enforcement in KDA gate
- Fixed docstring parameter documentation

**Performance Features:**
- Added chunk_indices parameter to reduce redundant computation
- Implemented token-parallel intra-chunk attention
- Enabled precision autotune capabilities
- Added PTX softplus support for AMD/Intel devices

The release attracted 7 new contributors and included 160 subsequent commits to the main branch, indicating active ongoing development.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-18T12:29:38.888386+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/mistakes.yaml",
  "offset": "50",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/mistakes.yaml",
    "offset": "50",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-18T12:29:38.888509+00:00_

50	  prevention: 修复模型加载问题时必须先检查 checkpoint 的实际 key 名（safetensors header 或 state_dict().keys()），不假设属性名与
51	    HuggingFace 标准一致。
52	  status: active
53	- id: M005
54	  date: '2026-05-18'
55	  category: code_bug
56	  severity: high
57	  summary: fla 0.5.0 与 Wang et al. 模型不兼容（训练时用 ~0.4.x），GatedDeltaNet 的 attn.D 参数被丢弃导致输出随机噪声
58	  root_cause: 安装了 fla 最新版 0.5.0，但 Wang et al. 模型训练时用 transformers 4.49.0 + 更早的 fla
59	    版本。fla 0.5.0 的 GatedDeltaNet 架构变更导致 checkpoint 参数不匹配（attn.D 被标记为 UNEXPECTED 并丢弃）。
60	  prevention: 使用第三方开源模型前，必须检查其训练环境版本（看 config.json 的 transformers_version 和 repo 的
61	    requirements.txt），安装匹配的库版本。不假设最新版兼容旧 checkpoint。
62	  status: active
63	  related_decisions:
64	  - D002
65	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-18T12:29:38.888631+00:00_

# Flash-Linear-Attention v0.4.2 Release Notes

**Release Date:** March 12, 2024

## Key Changes

This release included 41 merged pull requests with improvements across multiple components:

**Performance & Optimization:**
- Introduced a backend dispatch system for better flexibility
- Reduced device-to-host/host-to-device synchronization overhead
- Added lowerbound gate function to speed up KDA and DPLR operations
- Optimized convolution operations with mixed Triton forward and CUDA backward support

**Bug Fixes & Compatibility:**
- Fixed memory access issues in convolution kernels
- Corrected varlen-related logic in NSA dkv kernel
- Enhanced compatibility with Triton 3.2 and AMD RDNA GPUs
- Fixed initialization issues for Mamba2 with FSDP-2 DTensors
- Prevented int32 index overflow for long sequences

**Architectural Improvements:**
- Refactored convolution code into organized packages
- Centralized reference implementations
- Added cache support for intra-card context parallelism
- Removed deprecated torch.jit.script decorators

## Breaking Changes or New Models

The release notes do not explicitly mention breaking changes or new model support, focusing instead on internal improvements and optimizations to existing implementations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-18T12:29:38.888794+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "fla-org flash-linear-attention GatedDeltaNet \"attn.D\" parameter removed v0.5",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "fla-org flash-linear-attention GatedDeltaNet \"attn.D\" parameter removed v0.5",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-18T12:29:38.888927+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Songlin Yang\" \"Yu Zhang\" flash-linear-attention \"Wang\" \"hybrid linear attention\" fla version"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Songlin Yang\" \"Yu Zhang\" flash-linear-attention \"Wang\" \"hybrid linear attention\" fla version"
  }
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-18T12:29:38.889057+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/blob/main/fla/__init__.py",
  "prompt": "Show the complete contents of this __init__.py file. I need to see the __version__ variable."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/blob/main/fla/__init__.py",
    "prompt": "Show the complete contents of this __init__.py file. I need to see the __version__ variable."
  }
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-18T12:29:38.889181+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers/gated_deltanet.py?ref=v0.4.2\" -H \"Accept: application/vnd.github.raw+json\" 2>&1 | grep -n \"self\\.D\\|class Gated\\|nn\\.Parameter\\|A_log\\|dt_bias\\|a_proj\\|b_proj\"",
  "description": "Check for self.D parameter in v0.4.2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers/gated_deltanet.py?ref=v0.4.2\" -H \"Accept: application/vnd.github.raw+json\" 2>&1 | grep -n \"self\\.D\\|class Gated\\|nn\\.Parameter\\|A_log\\|dt_bias\\|a_proj\\|b_proj\"",
    "description": "Check for self.D parameter in v0.4.2"
  }
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-18T12:29:38.889300+00:00_

Based on the webpage content provided, here is the complete `__init__.py` file:

```python
# Copyright (c) 2023-2026, Songlin Yang, Yu Zhang, Zhiyuan Li
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
# For a list of all contributors, visit:
# https://github.com/fla-org/flash-linear-attention/graphs/contributors

import importlib
from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)

__version__ = "0.5.1"

__all__: list[str] = []

def _export_optional_public_api(module_name: str) -> None:
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError as exc:
        if exc.name == module_name:
            return
        raise

    globals()[module_name.rsplit(".", maxsplit=1)[-1]] = module

    for name in module.__all__:
        if name.endswith("Config"):
            continue
        globals()[name] = getattr(module, name)
        __all__.append(name)

_export_optional_public_api("fla.layers")
_export_optional_public_api("fla.models")

del _export_optional_public_api
```

The `__version__` variable is set to **"0.5.1"**.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-18T12:29:38.889477+00:00_

Web search results for query: "fla-org flash-linear-attention GatedDeltaNet "attn.D" parameter removed v0.5"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"},{"title":"GitHub - Fzkuji/flash-linear: 🚀 Efficient implementations of state-of-the-art linear attention models in Pytorch and Triton","url":"https://github.com/Fzkuji/flash-linear-attention"},{"title":"flash-linear-attention/README.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/README.md"},{"title":"[Bug] GatedDeltaNet backward error on Blackwell · Issue #607 · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/issues/607"},{"title":"flash-linear-attention/FAQs.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/FAQs.md"},{"title":"flash-linear-attention/fla/layers/path_attn.py at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/fla/layers/path_attn.py"},{"title":"GatedDeltaNet backward error on B200 · Issue #8459 · triton-lang/triton","url":"https://github.com/triton-lang/triton/issues/8459"},{"title":"[Bug]: Gated DeltaNet Recurrence with constant Gate at 1 vs. DeltaNet Recurrence · Issue #104 · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/issues/104"},{"title":"Home · fla-org/flash-linear-attention Wiki · GitHub","url":"https://github.com/fla-org/flash-linear-attention/wiki"}]

Let me search more specifically for information about the v0.5 release and the "attn.D" parameter removal:

Links: [{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/
…[truncated 4546 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-18T12:29:38.889693+00:00_

34:class GatedDeltaNet(nn.Module):
148:        self.a_proj = nn.Linear(hidden_size, self.num_v_heads, bias=False)
149:        self.b_proj = nn.Linear(hidden_size, self.num_v_heads, bias=False)
152:        self.A_log = nn.Parameter(torch.log(A))
153:        self.A_log._no_weight_decay = True
165:        self.dt_bias = nn.Parameter(inv_dt)
166:        # Just to be explicit. Without this we already don't put wd on dt_bias because of the check
168:        self.dt_bias._no_weight_decay = True
264:        beta = self.b_proj(hidden_states).sigmoid()
268:        g = -self.A_log.float().exp() * F.softplus(self.a_proj(hidden_states).float() + self.dt_bias)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-18T12:29:38.889848+00:00_

Web search results for query: ""Songlin Yang" "Yu Zhang" flash-linear-attention "Wang" "hybrid linear attention" fla version"

Links: [{"title":"Songlin Yang","url":"https://sustcsonglin.github.io/"},{"title":"publications | Songlin Yang - GitHub Pages","url":"https://sustcsonglin.github.io/publications/"},{"title":"[PDF] Gated Linear Attention Transformers with Hardware-Efficient Training | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Gated-Linear-Attention-Transformers-with-Training-Yang-Wang/62b18cc55dcc7ffe52c28e1086aee893b7bc4334"},{"title":"Linear Transformers for Eﬃcient Sequence Modeling Songlin Yang MIT CSAIL","url":"https://sustcsonglin.github.io/assets/pdf/talk_linear_transformer.pdf"},{"title":"Published as a conference paper at ICLR 2026 LOG-LINEAR ATTENTION Han Guo1∗","url":"https://arxiv.org/pdf/2506.04761"},{"title":"Gated Slot Attention for Efficient Linear-Time Sequence Modeling Yu Zhang1∗","url":"https://arxiv.org/pdf/2409.07146"},{"title":"Songlin Yang","url":"https://www.catalyzex.com/author/Songlin%20Yang"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/html/2507.06457v1"},{"title":"Parallelizing Linear Transformers with the Delta Rule over Sequence Length","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d13a3eae72366e61dfdc7eea82eeb685-Paper-Conference.pdf"},{"title":"DeltaNet Explained (Part II) | Songlin Yang - GitHub Pages","url":"https://sustcsonglin.github.io/blog/2024/deltanet-2/"}]

I found relevant information about the research you're asking about. Here are the key findings:

## Flash Linear Attention (FLA) Library

Songlin Yang and Yu Zhang developed FLA: A Triton-based library for hardware-efficient implementations of linear attention mechanism (2024).

## Key Papers and Research

Songlin Yang, Bailin Wang, Yu Zhang, Yikang Shen, and Yoon Kim published work on Gated Linear Attention Transformers with Hardware-Efficient Training at NeurIPS 2024, with an impleme
…[truncated 905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-18T12:29:38.890002+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/models/gated_deltanet/modeling_gated_deltanet.py?ref=v0.4.2\" -H \"Accept: application/vnd.github.raw+json\" 2>&1 | grep -n \"self\\.D\\|attn\\.D\\|class Gated\\|_keys_to_ignore\\|UNEXPECTED\\|ignore_keys\\|_init_weights\\|A_log\\|dt_bias\" | head -30",
  "description": "Check model-level code for attn.D in v0.4.2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/models/gated_deltanet/modeling_gated_deltanet.py?ref=v0.4.2\" -H \"Accept: application/vnd.github.raw+json\" 2>&1 | grep -n \"self\\.D\\|attn\\.D\\|class Gated\\|_keys_to_ignore\\|UNEXPECTED\\|ignore_keys\\|_init_weights\\|A_log\\|dt_bias\" | head -30",
    "description": "Check model-level code for attn.D in v0.4.2"
  }
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-18T12:29:38.890132+00:00_

34:class GatedDeltaNetBlock(GradientCheckpointingLayer):
111:class GatedDeltaNetPreTrainedModel(PreTrainedModel):
122:    def _init_weights(
130:                if not getattr(module.A_log, '_is_hf_initialized', False):
131:                    module.A_log.copy_(nn.init.uniform_(module.A_log, a=0, b=16).log())
132:                module.A_log._no_weight_decay = True
133:                if not getattr(module.dt_bias, '_is_hf_initialized', False):
135:                        nn.init.uniform_(module.dt_bias) * (math.log(0.1) - math.log(0.001)) + math.log(0.001),
139:                    module.dt_bias.copy_(inv_dt)
140:                module.dt_bias._no_weight_decay = True
180:class GatedDeltaNetModel(GatedDeltaNetPreTrainedModel):
268:class GatedDeltaNetForCausalLM(GatedDeltaNetPreTrainedModel, FLAGenerationMixin):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-18T12:29:38.890263+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/models/gated_deltanet/modeling_gated_deltanet.py\" -H \"Accept: application/vnd.github.raw+json\" 2>&1 | grep -n \"self\\.D\\|attn\\.D\\|class Gated\\|_keys_to_ignore\\|UNEXPECTED\\|ignore_keys\\|_init_weights\\|A_log\\|dt_bias\" | head -30",
  "description": "Check model-level code for attn.D in main/v0.5.0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/models/gated_deltanet/modeling_gated_deltanet.py\" -H \"Accept: application/vnd.github.raw+json\" 2>&1 | grep -n \"self\\.D\\|attn\\.D\\|class Gated\\|_keys_to_ignore\\|UNEXPECTED\\|ignore_keys\\|_init_weights\\|A_log\\|dt_bias\" | head -30",
    "description": "Check model-level code for attn.D in main/v0.5.0"
  }
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-18T12:29:38.890381+00:00_

42:class GatedDeltaNetBlock(GradientCheckpointingLayer):
173:class GatedDeltaNetPreTrainedModel(PreTrainedModel):
184:    def _init_weights(
192:                if not getattr(module.A_log, '_is_hf_initialized', False):
193:                    module.A_log.copy_(nn.init.uniform_(module.A_log, a=0, b=16).log())
194:                module.A_log._no_weight_decay = True
195:                if not getattr(module.dt_bias, '_is_hf_initialized', False):
197:                        nn.init.uniform_(module.dt_bias) * (math.log(0.1) - math.log(0.001)) + math.log(0.001),
201:                    module.dt_bias.copy_(inv_dt)
202:                module.dt_bias._no_weight_decay = True
245:class GatedDeltaNetModel(GatedDeltaNetPreTrainedModel):
354:class GatedDeltaNetForCausalLM(GatedDeltaNetPreTrainedModel, FLAGenerationMixin):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-18T12:29:38.890522+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/releases/tag/v0.1",
  "prompt": "Show the release notes for v0.1. What was the exact date? What features and models were supported? List all details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/releases/tag/v0.1",
    "prompt": "Show the release notes for v0.1. What was the exact date? What features and models were supported? List all details."
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-18T12:29:38.890722+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-18T12:29:38.890868+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:huggingface.co m-a-p \"1.3B-100B\" OR \"340M-20B\" \"fla\" OR \"flash-linear-attention\" version requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:huggingface.co m-a-p \"1.3B-100B\" OR \"340M-20B\" \"fla\" OR \"flash-linear-attention\" version requirements"
  }
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-18T12:29:38.890997+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers/gated_deltanet.py?ref=v0.5.0\" -H \"Accept: application/vnd.github.raw+json\" 2>&1 | grep -n \"self\\.D\\|A_log\\|dt_bias\\|a_proj\\|b_proj\\|use_gate_in_kernel\\|state_v_first\"",
  "description": "Check v0.5.0 tag layer parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sL \"https://api.github.com/repos/fla-org/flash-linear-attention/contents/fla/layers/gated_deltanet.py?ref=v0.5.0\" -H \"Accept: application/vnd.github.raw+json\" 2>&1 | grep -n \"self\\.D\\|A_log\\|dt_bias\\|a_proj\\|b_proj\\|use_gate_in_kernel\\|state_v_first\"",
    "description": "Check v0.5.0 tag layer parameters"
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-18T12:29:38.891123+00:00_

147:        self.a_proj = nn.Linear(hidden_size, self.num_v_heads, bias=False)
148:        self.b_proj = nn.Linear(hidden_size, self.num_v_heads, bias=False)
151:        self.A_log = nn.Parameter(torch.log(A))
152:        self.A_log._no_weight_decay = True
164:        self.dt_bias = nn.Parameter(inv_dt)
165:        # Just to be explicit. Without this we already don't put wd on dt_bias because of the check
167:        self.dt_bias._no_weight_decay = True
260:        beta = self.b_proj(hidden_states).sigmoid()
270:                g=self.a_proj(hidden_states),
276:                use_gate_in_kernel=True,
277:                A_log=self.A_log,
278:                dt_bias=self.dt_bias,
285:                g=self.a_proj(hidden_states),
291:                use_gate_in_kernel=True,
292:                A_log=self.A_log,
293:                dt_bias=self.dt_bias,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-18T12:29:38.891266+00:00_

Web search results for query: "site:huggingface.co m-a-p "1.3B-100B" OR "340M-20B" "fla" OR "flash-linear-attention" version requirements"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1"},{"title":"flash-linear-attention/examples/training.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/examples/training.md"},{"title":"flash-linear-attention/README.md at main · fla-org/flash-linear-attention","url":"https://github.com/sustcsonglin/flash-linear-attention/blob/main/README.md"},{"title":"m-a-p/transformer_340M_baseline · Hugging Face","url":"https://huggingface.co/m-a-p/transformer_340M_baseline"},{"title":"m-a-p/1.3B-100B-DeltaNet-hybrid-6-1 · Hugging Face","url":"https://huggingface.co/m-a-p/1.3B-100B-DeltaNet-hybrid-6-1"},{"title":"Hybrid Linear Attention Research - a m-a-p Collection","url":"https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research"},{"title":"m-a-p/340M-20B-DeltaNet-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-DeltaNet-hybrid-24-1"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/html/2507.06457v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=linear+attention"}]

Based on the search results, I found information about the m-a-p models with the model sizes you specified (340M-20B and 1.3B-100B) related to flash-linear-attention (fla).

The m-a-p team trained and open-sourced 72 models: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios. All models are pretrained on the fineweb-edu dataset and using flash-
…[truncated 787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-18T12:29:38.891450+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/releases/tag/0.1",
  "prompt": "Show the release notes for v0.1 (tag 0.1). What was the exact date? What features were supported?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/releases/tag/0.1",
    "prompt": "Show the release notes for v0.1 (tag 0.1). What was the exact date? What features were supported?"
  }
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-18T12:29:38.891575+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-18T12:29:38.891722+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pip show flash-linear-attention 2>/dev/null || echo \"flash-linear-attention not installed locally\"",
  "description": "Check if flash-linear-attention is installed locally"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "pip show flash-linear-attention 2>/dev/null || echo \"flash-linear-attention not installed locally\"",
    "description": "Check if flash-linear-attention is installed locally"
  }
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-18T12:29:38.891841+00:00_

flash-linear-attention not installed locally

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-18T12:29:38.891965+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/NVlabs/GatedDeltaNet/main/gated_delta_net/model/gated_delta_net_layer.py",
  "prompt": "Show the full source code. Focus on all nn.Parameter definitions, especially anything named D, A_log, dt_bias. Show the complete __init__ method."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/NVlabs/GatedDeltaNet/main/gated_delta_net/model/gated_delta_net_layer.py",
    "prompt": "Show the full source code. Focus on all nn.Parameter definitions, especially anything named D, A_log, dt_bias. Show the complete __init__ method."
  }
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-18T12:29:38.892078+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 173 · 2026-05-18T12:29:38.892196+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sL \"https://api.github.com/repos/NVlabs/GatedDeltaNet/contents\" | python3 -c \"import sys,json; data=json.load(sys.stdin); [print(x['name'], x['type']) for x in data]\" 2>&1",
  "description": "List files in NVlabs/GatedDeltaNet repo root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sL \"https://api.github.com/repos/NVlabs/GatedDeltaNet/contents\" | python3 -c \"import sys,json; data=json.load(sys.stdin); [print(x['name'], x['type']) for x in data]\" 2>&1",
    "description": "List files in NVlabs/GatedDeltaNet repo root"
  }
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-18T12:29:38.892307+00:00_

Dockerfile file
LICENSE file
README.md file
cache.py file
lit_gpt dir
pretrain.py file
scripts dir

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-18T12:29:38.892430+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "pypi flash-linear-attention 0.1 \"Mar 2025\" release history versions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "pypi flash-linear-attention 0.1 \"Mar 2025\" release history versions"
  }
}
```

</details>

---

### Tool call

_source line 176 · 2026-05-18T12:29:38.892551+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sL \"https://api.github.com/repos/NVlabs/GatedDeltaNet/contents/lit_gpt\" | python3 -c \"import sys,json; data=json.load(sys.stdin); [print(x['name'], x['type']) for x in data]\" 2>&1",
  "description": "List files in NVlabs/GatedDeltaNet lit_gpt directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sL \"https://api.github.com/repos/NVlabs/GatedDeltaNet/contents/lit_gpt\" | python3 -c \"import sys,json; data=json.load(sys.stdin); [print(x['name'], x['type']) for x in data]\" 2>&1",
    "description": "List files in NVlabs/GatedDeltaNet lit_gpt directory"
  }
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-18T12:29:38.892682+00:00_

__init__.py file
config.py file
fused_cross_entropy.py file
fused_rotary_embedding.py file
gated_delta_net.py file
gated_delta_rule_ops dir
model.py file
packed_dataset.py file
rmsnorm.py file
rotary.py file
speed_monitor.py file
tokenizer.py file
utils.py file

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-18T12:29:38.892812+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://pypi.org/project/flash-linear-attention/0.1/",
  "prompt": "Show the exact release date and metadata for flash-linear-attention version 0.1. What Python version is required? What are the dependencies?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://pypi.org/project/flash-linear-attention/0.1/",
    "prompt": "Show the exact release date and metadata for flash-linear-attention version 0.1. What Python version is required? What are the dependencies?"
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-18T12:29:38.892924+00:00_

I cannot provide the requested information about flash-linear-attention version 0.1 based on the content provided. The web page shows only an error message stating that "A required part of this site couldn't load," which prevents access to the package metadata, release date, Python version requirements, and dependency information you're asking about.

To find this information, you would need to:
- Resolve the loading issue (check connection, disable ad blockers, try another browser)
- Visit a package repository like PyPI directly
- Check the project's GitHub releases page

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 180 · 2026-05-18T12:29:38.893054+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sL \"https://api.github.com/repos/NVlabs/GatedDeltaNet/contents/lit_gpt/gated_delta_net.py\" -H \"Accept: application/vnd.github.raw+json\" 2>&1",
  "description": "Fetch NVlabs GatedDeltaNet layer implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sL \"https://api.github.com/repos/NVlabs/GatedDeltaNet/contents/lit_gpt/gated_delta_net.py\" -H \"Accept: application/vnd.github.raw+json\" 2>&1",
    "description": "Fetch NVlabs GatedDeltaNet layer implementation"
  }
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-18T12:29:38.893197+00:00_

# Copyright (c) 2024, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.


from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F
from einops import rearrange, repeat

from fla.modules import FusedRMSNormSwishGate, RMSNorm, ShortConvolution
from fla.modules.activations import ACT2FN
from fla.ops.simple_gla import chunk_simple_gla
from .gated_delta_rule_ops import chunk_gated_delta_rule
import math 

if TYPE_CHECKING:
    from fla.models.utils import Cache

try:
    from fla.modules.l2norm import l2_norm as l2_norm_fn
except:
    from fla.modules.l2norm import l2_norm_fn

class GatedDeltaNet(nn.Module):
    def __init__(
        self,
        mode: str = 'chunk',
        hidden_size: int = 1024,
        expand_k: float = 0.75,
        expand_v: float = 1.5,
        num_heads: int = 9,
        num_kv_heads: Optional[int] = None,
        qk_norm: str = 'l2',
        conv_size: int = 4,
        conv_bias: bool = False,
        gate_fn: str = 'swish',
        elementwise_affine: Optional[bool] = True,
        norm_eps: float = 1e-5,
        gate_logit_normalizer: int = 16,
        fuse_norm: bool = True,
        layer_idx: int = None,
        use_mamba_gate: bool = True,
        use_mva: bool = False,
        use_residual: bool = False, # residual as in Mamba2,
        use_input_gate: bool = False,
    ) -> GatedDeltaNet:
        super().__init__()
        self.qk_norm = qk_norm
        assert self.qk_norm in ['l2', 'longhorn', 'softmax']

        self.use_mva = use_mva

        self.mode = mode
        self.hidden_size = hidde
…[truncated 7513 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 182 · 2026-05-18T12:29:38.893344+00:00_

Web search results for query: "pypi flash-linear-attention 0.1 "Mar 2025" release history versions"

Links: [{"title":"flash-linear-attention · PyPI","url":"https://pypi.org/project/flash-linear-attention/"},{"title":"piwheels - flash-linear-attention","url":"https://www.piwheels.org/project/flash-linear-attention/"},{"title":"flash-attn · PyPI","url":"https://pypi.org/project/flash-attn/"},{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"flash-linear-attention/FAQs.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/FAQs.md"},{"title":"jax-flash-attn2 · PyPI","url":"https://pypi.org/project/jax-flash-attn2/"},{"title":"Releases · Dao-AILab/flash-attention","url":"https://github.com/Dao-AILab/flash-attention/releases"},{"title":"flash-sparse-attn · PyPI","url":"https://pypi.org/project/flash-sparse-attn/"},{"title":"flash-attn 0.2.1","url":"https://pypi.org/project/flash-attn/0.2.1/"},{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"}]

Based on the search results, I found the release history information for the `flash-linear-attention` package on PyPI.

The flash-linear-attention package has version 0.1 released on Mar 20, 2025, with version 0.1.1 released on Mar 24, 2025, and version 0.1.2 released on Mar 31, 2025.

The complete release timeline from the PyPI page shows these March 2025 releases in the context of the broader version history, which includes earlier and later versions spanning from March 2025 through March 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 183 · 2026-05-18T12:29:38.893500+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flame/blob/main/requirements.txt",
  "prompt": "Show all contents of requirements.txt if it exists."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flame/blob/main/requirements.txt",
    "prompt": "Show all contents of requirements.txt if it exists."
  }
}
```

</details>

---

### Tool call

_source line 184 · 2026-05-18T12:29:38.893629+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "curl -sL \"https://api.github.com/repos/NVlabs/GatedDeltaNet/contents/lit_gpt/model.py\" -H \"Accept: application/vnd.github.raw+json\" 2>&1 | grep -n \"attn\\|GatedDeltaNet\\|self\\.D\\|class \" | head -30",
  "description": "Check how GatedDeltaNet is used in NVlabs model.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "tool_args": {
    "command": "curl -sL \"https://api.github.com/repos/NVlabs/GatedDeltaNet/contents/lit_gpt/model.py\" -H \"Accept: application/vnd.github.raw+json\" 2>&1 | grep -n \"attn\\|GatedDeltaNet\\|self\\.D\\|class \" | head -30",
    "description": "Check how GatedDeltaNet is used in NVlabs model.py"
  }
}
```

</details>

---

### Tool call

_source line 185 · 2026-05-18T12:29:38.893781+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"2507.06457\" \"flash-linear-attention\" version commit OR \"v0.\" reproducibility"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"2507.06457\" \"flash-linear-attention\" version commit OR \"v0.\" reproducibility"
  }
}
```

</details>

---

### Tool result

_source line 186 · 2026-05-18T12:29:38.893899+00:00_

15:from .gated_delta_net import GatedDeltaNet
33:FlashAttention2Available = RequirementCache("flash-attn>=2.0.0.post1")
63:class GPT(nn.Module):
202:        # passing `attn_mask` to SDPA downgrades it to use the inefficient implementation. since we only need the mask
282:class Block(nn.Module):
288:            self.attn = GatedDeltaNet(hidden_size=config.n_embd)      
290:            self.attn = CausalSelfAttention(config, n_embd= config.n_embd, layer_idx= layer_idx, )
310:            h, _ , new_kv_cache = self.attn(n_1, attention_mask=mask)
312:            h, new_kv_cache = self.attn(n_1, rope, max_seq_length, mask, input_pos, kv_cache)   
327:class MBlock(nn.Module):
332:        Simple block wrapping a mixer class with LayerNorm/RMSNorm and residual connection"
386:class CausalSelfAttention(nn.Module):
400:        self.attn = nn.Linear(n_embd, shape, bias=config.bias)
404:        self.sc = config.sc_attn
445:        qkv = self.attn(x)
521:            from flash_attn import flash_attn_func
526:            return flash_attn_func(q, k, v, dropout_p=0.0, softmax_scale=scale, causal=True, window_size=win_tuple)
534:            q, k, v, attn_mask=mask, dropout_p=0.0, scale=scale, is_causal=mask is None
539:class LLaMAMLP(nn.Module):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-18T12:29:38.894017+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-18T12:29:38.894142+00:00_

Web search results for query: ""2507.06457" "flash-linear-attention" version commit OR "v0." reproducibility"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"},{"title":"Releases · Dao-AILab/flash-attention","url":"https://github.com/Dao-AILab/flash-attention/releases"},{"title":"[2507.06457] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457"},{"title":"Commits · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/commits/main"},{"title":"GitHub - Fzkuji/flash-linear: 🚀 Efficient implementations of state-of-the-art linear attention models in Pytorch and Triton","url":"https://github.com/Fzkuji/flash-linear-attention"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/pdf/2507.06457"},{"title":"Home · fla-org/flash-linear-attention Wiki · GitHub","url":"https://github.com/fla-org/flash-linear-attention/wiki"},{"title":"FLA · GitHub","url":"https://github.com/fla-org"},{"title":"flash-linear-attention · PyPI","url":"https://pypi.org/project/flash-linear-attention/"}]

I found results related to the arXiv paper 2507.06457 "A Systematic Analysis of Hybrid Linear Attention" and the flash-linear-attention repository. The paper trained and open-sourced 72 models: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios.

The search returned information about the flash-linear-attention GitHub repository and its releases, but the specific version, commit hash, or "v0." version information related to this paper's reproducibility wasn't clearly displayed in the search results. You may need to check the paper itself or the GitHub r
…[truncated 224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-18T12:29:38.894342+00:00_

Here is a comprehensive summary of findings.

## Results

**The paper does not specify an exact flash-linear-attention version or commit hash.** Wang et al. (arXiv 2507.06457) only state: "Our model training and inference are both implemented using the flash-linear-attention library" with a link to `https://github.com/fla-org/flash-linear-attention` (reference [45]). No version number, commit hash, requirements file, or reproducibility details are provided in the paper text, appendices, or model cards.

### What I checked:

1. **Full paper HTML** (`https://arxiv.org/html/2507.06457v1`) -- searched every section including appendix. Only mentions "flash-linear-attention library" with the GitHub link. No version specified.

2. **HuggingFace model cards** -- All 62 models in the collection (`https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e`) have "No model card." No README, no requirements.txt.

3. **Model config.json files** (checked `m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1` and `m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1`) -- contain `"transformers_version": "4.49.0"` but no fla version field. The `_name_or_path` field shows `/mnt/bn/ridger1/flame/configs/...`, confirming they used the `fla-org/flame` training framework.

4. **flame training framework** (`https://github.com/fla-org/flame`) -- `pyproject.toml` lists `flash-linear-attention` as a dependency **with no version pin** (just bare `'flash-linear-attention'`). Installs from source via `pip install -U --no-use-pep517 git+https://github.com/fla-org/flash-linear-attention`.

5. **PyPI release history** for `flash-linear-attention`:
   - v0.1: Mar 20, 2025
   - v0.1.1: Mar 24, 2025
   - v0.1.2: Mar 31, 2025
   - v0.2.0: Apr 11, 2025
   - v0.2.1: Apr 23, 2025
   - v0.2.2: Jun 5, 2025
   - v0.3.0: Jul 14, 2025
   - v0.3.1: Aug 26, 2025
   - v0.3.2: Sep 10, 2025
   - v0.4.0: Oct 27, 2025
   - v0.4.1: Dec 24, 2025
   - v0.4.2: Mar 12, 2026
   - v0.5.0: Apr 21, 2026

…[truncated 1082 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Agent",
  "elapsed_ms": 21
}
```

</details>

---

### Tool result

_source line 190 · 2026-05-18T12:29:38.894561+00:00_

There it is. In the NVlabs implementation, line 288: `self.attn = GatedDeltaNet(...)`. So in the checkpoint, the layer's GatedDeltaNet parameters appear under the key prefix `attn.`, meaning the `D` parameter from NVlabs' `GatedDeltaNet` would appear as `attn.D` in the state_dict.

Now I have the complete picture. Here is the comprehensive report:

---

## Breaking Changes in flash-linear-attention (fla) GatedDeltaNet

### 1. The Core Issue: NVlabs vs fla-org Implementations

The NVlabs official GatedDeltaNet implementation (`NVlabs/GatedDeltaNet/lit_gpt/gated_delta_net.py`) and the fla-org implementation (`fla-org/flash-linear-attention/fla/layers/gated_deltanet.py`) have **different parameter sets**. The NVlabs version has a parameter `self.D` (a skip-connection residual parameter, shape `[num_heads]`) that the fla-org version has **never had**.

When NVlabs' `GatedDeltaNet` is stored inside a `Block` as `self.attn = GatedDeltaNet(...)`, the checkpoint key becomes `attn.D`. Loading a checkpoint trained with NVlabs' code into fla-org's `GatedDeltaNet` causes `attn.D` to be an **UNEXPECTED key** and silently dropped, producing random/garbage outputs.

### 2. Parameter Comparison Across Versions

**Parameters that exist in ALL fla-org versions (v0.2.0 through v0.5.0/main):**
- `self.A_log` -- `nn.Parameter`, shape `[num_heads]` (or `[num_v_heads]` in >= v0.3.x)
- `self.dt_bias` -- `nn.Parameter`, shape `[num_heads]` (or `[num_v_heads]`)
- `self.q_proj`, `self.k_proj`, `self.v_proj` -- `nn.Linear`
- `self.a_proj`, `self.b_proj` -- `nn.Linear`
- `self.o_proj` -- `nn.Linear`
- `self.g_proj` (when `use_gate=True`) -- `nn.Linear`
- `self.q_conv1d`, `self.k_conv1d`, `self.v_conv1d` (when `use_short_conv=True`) -- `ShortConvolution`

**Parameter that exists ONLY in NVlabs' implementation:**
- `self.D` -- `nn.Parameter`, shape `[num_heads]`, used for `o = o + self.D * v` residual connection

**The fla-org `GatedDeltaNet` has NEVER had `self.D`.** This is not a rename; it is 
…[truncated 3579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "Agent",
  "elapsed_ms": 21
}
```

</details>

---

### Assistant

_source line 191 · 2026-05-18T12:29:38.894785+00:00_

## 调查结果

### 1. Wang et al. 使用的 fla 版本

**论文和模型卡均未记录具体版本。** 基于时间线推断：

- 340M 模型最早上传日期：**2025-03-03**
- 1.3B 模型最早上传日期：**2025-04-20**
- fla 首个 PyPI 发布 (v0.1)：**2025-03-20**
- 训练框架 `fla-org/flame` 的 `pyproject.toml` 中 `flash-linear-attention` **无版本锁定**，直接从 git main 分支安装

**结论：Wang et al. 大概率使用的是 2025 年 2-3 月 main 分支的源码安装，早于或等同于 v0.1 发布。**

### 2. fla PyPI 版本历史

| 版本 | 发布日期 |
|------|----------|
| 0.1 | 2025-03-20 |
| 0.1.1 | 2025-03-24 |
| 0.1.2 | 2025-03-31 |
| 0.2.0 | 2025-04-11 |
| 0.2.1 | 2025-04-23 |
| 0.2.2 | 2025-06-05 |
| 0.3.0 | 2025-07-14 |
| 0.3.1 | 2025-08-26 |
| 0.3.2 | 2025-09-10 |
| 0.4.0 | 2025-10-27 |
| 0.4.1 | 2025-12-24 |
| 0.4.2 | 2026-03-12 |
| 0.5.0 | 2026-04-21 |

### 3. `attn.D` 问题澄清

**这不是 fla 版本间的 breaking change，而是 NVlabs 实现 vs fla-org 实现的差异：**

- **NVlabs/GatedDeltaNet** 有 `self.D` 参数（skip-connection residual，shape `[num_heads]`，用于 `o = o + self.D * v`）
- **fla-org 的 GatedDeltaNet 从未有过 `self.D`**
- NVlabs 代码中 `self.attn = GatedDeltaNet(...)`，所以 checkpoint 中 key 为 `attn.D`
- 用 fla-org 加载 NVlabs checkpoint 时，`attn.D` 被当作 unexpected key **静默丢弃**，导致输出异常

### 4. fla v0.4.x → v0.5.0 的实际 breaking changes

**GatedDeltaNet forward 方法变化：**

- **v0.2.0~v0.4.2**：gate `g` 在 layer 层计算后传入 kernel
  ```python
  g = -self.A_log.float().exp() * F.softplus(self.a_proj(...) + self.dt_bias)
  chunk_gated_delta_rule(q, k, v, g=g, beta=beta, ...)
  ```
- **v0.5.0**：`A_log`/`dt_bias` 直接传入 kernel，内部融合计算
  ```python
  chunk_gated_delta_rule(q, k, v, g=self.a_proj(...), beta=beta,
      A_log=self.A_log, dt_bias=self.dt_bias,
      use_gate_in_kernel=True, state_v_first=True, ...)
  ```

**Checkpoint 权重兼容性**：v0.2.0~v0.5.0 之间的 fla 参数名一致（`A_log`, `dt_bias`, 各 proj），**权重可互相加载**。变化主要在 forward path 和 kernel API。

另有已知 bug fix：PR #754 修复了 transformers >= 5.0 meta device loading 时 `A_log` 被 `_init_weights` 重新初始化（对已加载的负值取 log 导致 NaN）。

### 5. 降级建议

如果你的项目需要兼容 Wang et al. 的 checkpoint：

```bash
# 安装 v0.4.2（最近的稳定 0.4.x）
pip install flash-linear-attention==0.4.2

# 或者锁定到 Wang et al. 训练时期的 commit（~2025年3月初）
pip install git+https://github.com/fla-org/flash-linear-attention@v0.1
```

如果问题是 NVlabs checkpoint 的 `attn.D` 丢失，降级 fla 版本不能解决——需要手动在 fla 的 `GatedDeltaNet` 中添加 `self.D` 参数，或在加载时做 key mapping。

Sources:
- [fla-org/flash-linear-attention GitHub](https://github.com/fla-org/flash-linear-attention)
- [flash-linear-attention PyPI](https://pypi.org/project/flash-linear-attention/)
- [Releases page](https://github.com/fla-org/flash-linear-attention/releases)
- [arXiv 2507.06457](https://arxiv.org/abs/2507.06457)
- [m-a-p HuggingFace Collection](https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research)
- [NVlabs/GatedDeltaNet](https://github.com/NVlabs/GatedDeltaNet)
- [fla-org/flame training framework](https://github.com/fla-org/flame)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_wang-fla-version_20260518T122417"
}
```

</details>

---

### Tool call

_source line 192 · 2026-05-18T12:32:39.157919+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-18T12:32:39.161819+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "ToolSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 194 · 2026-05-18T12:32:39.162127+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang \"Systematic Analysis of Hybrid Linear Attention\" arXiv 2507.06457 github flash-linear-attention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang \"Systematic Analysis of Hybrid Linear Attention\" arXiv 2507.06457 github flash-linear-attention"
  }
}
```

</details>

---

### Tool call

_source line 195 · 2026-05-18T12:32:39.162366+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "flash-linear-attention pypi version history releases 0.4 0.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "flash-linear-attention pypi version history releases 0.4 0.5"
  }
}
```

</details>

---

### Tool result

_source line 196 · 2026-05-18T12:32:39.163435+00:00_

Web search results for query: "flash-linear-attention pypi version history releases 0.4 0.5"

Links: [{"title":"flash-linear-attention · PyPI","url":"https://pypi.org/project/flash-linear-attention/"},{"title":"piwheels - flash-linear-attention","url":"https://www.piwheels.org/project/flash-linear-attention/"},{"title":"flash-attn · PyPI","url":"https://pypi.org/project/flash-attn/"},{"title":"flash-linear-attention Changelog","url":"https://data.safetycli.com/packages/pypi/flash-linear-attention/changelog"},{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"flash-attn Versions - Latest Release & Version History | Flash Attention Wheel Finder","url":"https://flashattn.dev/versions"},{"title":"flash-attn-jax · PyPI","url":"https://pypi.org/project/flash-attn-jax/"},{"title":"Releases · Dao-AILab/flash-attention","url":"https://github.com/Dao-AILab/flash-attention/releases"},{"title":"flash-attn Prebuilt Wheels - Install Flash Attention in Seconds","url":"https://flashattn.dev/"},{"title":"piwheels - fla-core","url":"https://www.piwheels.org/project/fla-core/"}]

I found information about the flash-linear-attention package on PyPI. Let me search more specifically for versions 0.4 and 0.5:

Links: [{"title":"flash-linear-attention · PyPI","url":"https://pypi.org/project/flash-linear-attention/"},{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"piwheels - flash-linear-attention","url":"https://www.piwheels.org/project/flash-linear-attention/"},{"title":"flash-attn · PyPI","url":"https://pypi.org/project/flash-attn/"},{"title":"piwheels - fla-core","url":"https://www.piwheels.org/project/fla-core/"},{"title":"flash-linear-attention/FAQs.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-o
…[truncated 1054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-18T12:32:39.163899+00:00_

Web search results for query: "Wang "Systematic Analysis of Hybrid Linear Attention" arXiv 2507.06457 github flash-linear-attention"

Links: [{"title":"[2507.06457] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/html/2507.06457v1"},{"title":"[2507.06457v1] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457v1"},{"title":"[PDF] A Systematic Analysis of Hybrid Linear Attention | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Systematic-Analysis-of-Hybrid-Linear-Attention-Wang-Zhu/f7ad9ebc481e23ae7fa90d98d3814518e94adcd1"},{"title":"Paper page - A Systematic Analysis of Hybrid Linear Attention","url":"https://huggingface.co/papers/2507.06457"},{"title":"(PDF) A Systematic Analysis of Hybrid Linear Attention","url":"https://www.researchgate.net/publication/393538945_A_Systematic_Analysis_of_Hybrid_Linear_Attention"},{"title":"A Systematic Analysis of Hybrid Linear Attention | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/systematic-analysis-hybrid-linear-attention"},{"title":"Hybrid Linear Attention Done Right: Efficient Distillation ...","url":"https://arxiv.org/pdf/2601.22156"},{"title":"Hybrid Linear Attention Done Right: Efficient Distillation and Effective Architectures for Extremely Long Contexts","url":"https://arxiv.org/html/2601.22156v1"},{"title":"[QA] A Systematic Analysis of Hybrid Linear Attention - YouTube","url":"https://www.youtube.com/watch?v=Qu3I8nmBpT8"}]

I found the paper you're looking for! Here are the key details:

## "A Systematic Analysis of Hybrid Linear Attention" (arXiv 2507.06457)

**Authors:** Dustin Wang, Rui-Jie Zhu, Steven Abreu, Yong Shan, Taylor Kergan, Yuqi Pan, Yuhong Chou, Zheng Li, Ge Zhang, Wenhao Huang, and Jason Eshraghian

**Published:** July 8, 2025

**Core Research:**

Transformers face quadratic complexity and memor
…[truncated 1202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 198 · 2026-05-18T12:32:39.164225+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"m-a-p\" hybrid linear attention github 1.3B 340M training code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"m-a-p\" hybrid linear attention github 1.3B 340M training code"
  }
}
```

</details>

---

### Tool call

_source line 199 · 2026-05-18T12:32:39.164464+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2507.06457v1",
  "prompt": "Extract any mention of flash-linear-attention library version, fla version, GitHub repository URL, code release, training code, requirements.txt, package versions, and any specific commit hashes used in training. Also extract the GatedDeltaNet configuration details and any model architecture details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2507.06457v1",
    "prompt": "Extract any mention of flash-linear-attention library version, fla version, GitHub repository URL, code release, training code, requirements.txt, package versions, and any specific commit hashes used in training. Also extract the GatedDeltaNet configuration details and any model architecture details."
  }
}
```

</details>

---

### Tool result

_source line 200 · 2026-05-18T12:32:39.164772+00:00_

Web search results for query: ""m-a-p" hybrid linear attention github 1.3B 340M training code"

Links: [{"title":"GitHub - JusenD/NHA: [ACL 2026] Official repo for \"Native Hybrid Attention for Efficient Sequence Modeling\" · GitHub","url":"https://github.com/JusenD/NHA"},{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"flash-linear-attention/examples/training.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/examples/training.md"},{"title":"GitHub - thunlp/hybrid-linear-attention: Code and models for the paper: Hybrid Linear Attention Done Right: Efficient Distillation and Effective Architectures for Extremely Long Contexts · GitHub","url":"https://github.com/thunlp/hybrid-linear-attention"},{"title":"GitHub - HazyResearch/based: Code for exploring Based models from \"Simple linear attention language models balance the recall-throughput tradeoff\" · GitHub","url":"https://github.com/HazyResearch/based"},{"title":"GitHub - MoonshotAI/Kimi-Linear · GitHub","url":"https://github.com/MoonshotAI/Kimi-Linear"},{"title":"m-a-p/transformer_340M_baseline · Hugging Face","url":"https://huggingface.co/m-a-p/transformer_340M_baseline"},{"title":"Songlin Yang","url":"https://sustcsonglin.github.io/"},{"title":"GitHub - idiap/hybrid-linear-sparse-attention: Alleviating Forgetfulness of Linear Attention by Hybrid Sparse Attention and Contextualized Learnable Token Eviction.","url":"https://github.com/idiap/hybrid-linear-sparse-attention"},{"title":"GitHub - fla-org/flame: 🔥 A minimal training framework for scaling FLA models","url":"https://github.com/fla-org/flame"}]

Based on the search results, I found several relevant resources related to hybrid linear attention with 1.3B and 340M models:

## Key Findings:

**Hugging Face Model:** There is an m-a-p model on Hugging Face that includes 
…[truncated 1326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-18T12:32:39.165049+00:00_

# Flash-Linear-Attention Library and Implementation Details

## Library Reference
The paper mentions using the **flash-linear-attention library** for model training and inference, as indicated by the footnote: "Our model training and inference are both implemented using the flash-linear-attention library."

A GitHub repository reference is provided: https://github.com/fla-org/flash-linear-attention

## Specific Version Information
The document does not specify a particular version number, commit hash, or requirements.txt file for the flash-linear-attention library used in this research.

## Training Infrastructure
The researchers trained 72 models across two scales:
- **340M parameters**: trained on 20 billion tokens
- **1.3B parameters**: trained on 100 billion tokens

All models used the **AdamW optimizer** with a **cosine learning rate schedule**.

## Dataset
Models were pretrained on the **fineweb-edu** dataset.

## GatedDeltaNet Architecture
The paper does not provide detailed configuration specifications for GatedDeltaNet. It is identified as a third-generation delta-rule mechanism with per-token gates and is noted as one of the top-performing hybrid configurations, particularly at a 24:1 linear-to-full attention ratio.

## Model Availability
The authors note they "open-sourced 72 models" and reference a Hugging Face collection: https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-18T12:32:39.165319+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e",
  "prompt": "Find any GitHub repository links, training code links, and any mention of flash-linear-attention library version or fla version used. Also look for any GatedDeltaNet specific model card and its config details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e",
    "prompt": "Find any GitHub repository links, training code links, and any mention of flash-linear-attention library version or fla version used. Also look for any GatedDeltaNet specific model card and its config details."
  }
}
```

</details>

---

### Tool call

_source line 203 · 2026-05-18T12:32:39.165536+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://pypi.org/project/flash-linear-attention/",
  "prompt": "List all versions of flash-linear-attention with their release dates, especially versions 0.1.x, 0.2.x, 0.3.x, 0.4.x, and 0.5.0. I need a complete version history with dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://pypi.org/project/flash-linear-attention/",
    "prompt": "List all versions of flash-linear-attention with their release dates, especially versions 0.1.x, 0.2.x, 0.3.x, 0.4.x, and 0.5.0. I need a complete version history with dates."
  }
}
```

</details>

---

### Tool result

_source line 204 · 2026-05-18T12:32:39.166119+00:00_

# Analysis of Hybrid Linear Attention Research Collection

Based on the webpage content provided, I cannot find:

1. **GitHub repository links** - None are visible in the collection page content
2. **Training code links** - Not mentioned in the displayed content
3. **Flash-linear-attention (fla) library version** - No specific version information is provided
4. **GatedDeltaNet specific model card or config details** - The collection lists multiple GatedDeltaNet models but doesn't include detailed config information on this overview page

## What is Available

The collection contains multiple model variants including:
- **GatedDeltaNet models** (340M and 1.3B sizes with various hybrid configurations)
- **DeltaNet models** (pure and hybrid variants)
- **RetNet models** (pure and hybrid variants)
- **GLA (Gated Linear Attention) models** (pure and hybrid variants)
- **HGRN/HGRN2 models** (pure and hybrid variants)

Models are organized by:
- Size (340M, 1.3B)
- Training data (20B, 100B tokens)
- Architecture variant
- Configuration ratios (hybrid-3-1, hybrid-6-1, etc.)

## Recommended Next Steps

To find the specific information you're looking for:
1. **Click individual model cards** (e.g., `m-a-p/1.3B-100B-GatedDeltaNet-pure`) to access detailed config files and model cards
2. **Check the model's repository** link on individual model pages for training code and implementation details
3. **Look for associated papers** in the M-A-P organization's documentation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-18T12:32:39.166360+00:00_

# Flash-Linear-Attention Version History

Based on the PyPI page, here's the complete release timeline:

| Version | Release Date |
|---------|-------------|
| 0.5.0 | Apr 21, 2026 |
| 0.4.2 | Mar 12, 2026 |
| 0.4.1 | Dec 24, 2025 |
| 0.4.0 | Oct 27, 2025 |
| 0.3.2 | Sep 10, 2025 |
| 0.3.1 | Aug 26, 2025 |
| 0.3.0 | Jul 14, 2025 |
| 0.2.2 | Jun 5, 2025 |
| 0.2.1 | Apr 23, 2025 |
| 0.2.0 | Apr 11, 2025 |
| 0.1.2 | Mar 31, 2025 |
| 0.1.1 | Mar 24, 2025 |
| 0.1 | Mar 20, 2025 |

The project represents "efficient implementations for emerging model architectures, with a focus on efficient sequence modeling (e.g., linear attention, state space models, and their hybrids)." All implementations are written in PyTorch and Triton, supporting NVIDIA, AMD, and Intel platforms.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-18T12:32:39.166601+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-pure",
  "prompt": "Find any mention of: flash-linear-attention version, fla version, requirements, github repository, training code, dependencies, package versions, and commit hashes. Also extract any GatedDeltaNet config details including attn parameters (window_size, D, num_heads)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-pure",
    "prompt": "Find any mention of: flash-linear-attention version, fla version, requirements, github repository, training code, dependencies, package versions, and commit hashes. Also extract any GatedDeltaNet config details including attn parameters (window_size, D, num_heads)."
  }
}
```

</details>

---

### Tool call

_source line 207 · 2026-05-18T12:32:39.166861+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"flash-linear-attention\" \"0.3.0\" OR \"0.2.2\" GatedDeltaNet breaking changes attn"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"flash-linear-attention\" \"0.3.0\" OR \"0.2.2\" GatedDeltaNet breaking changes attn"
  }
}
```

</details>

---

### Tool result

_source line 208 · 2026-05-18T12:32:39.167077+00:00_

# Analysis of Web Page Content

Based on the provided web page content, **no mentions were found** of the following:

- Flash-linear-attention version
- FLA version
- Requirements
- GitHub repository
- Training code
- Dependencies
- Package versions
- Commit hashes
- GatedDeltaNet config details (window_size, D, num_heads, attn parameters)

## What the Page Contains

The page is a Hugging Face model card for **m-a-p/1.3B-100B-GatedDeltaNet-pure** with only the following available information:

- **Model Size:** 1B params
- **Tensor Type:** F32
- **Format:** Safetensors
- **Downloads (last month):** 1,574
- **Status:** No model card provided
- **Collection:** Part of "Hybrid Linear Attention Research" collection (62 items)

## Recommendation

To find the technical details you're looking for, you would need to:
1. Check the model's **Files** section on the repository
2. Look for a `README.md` or model configuration files
3. Visit the linked **GitHub repository** (if available in the full model card)
4. Check the model's discussion/community section for additional documentation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-18T12:32:39.167365+00:00_

Web search results for query: ""flash-linear-attention" "0.3.0" OR "0.2.2" GatedDeltaNet breaking changes attn"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"},{"title":"Flash Attention Explained: A Comprehensive Guide | DataCamp","url":"https://www.datacamp.com/blog/flash-attention"},{"title":"GitHub - Fzkuji/flash-linear: 🚀 Efficient implementations of state-of-the-art linear attention models in Pytorch and Triton","url":"https://github.com/Fzkuji/flash-linear-attention"},{"title":"Reimplementing FlashAttention for performance and giggles | AmineDiro","url":"https://aminediro.com/posts/flash_attn/"},{"title":"Attention Is All You Need! — Transformer Engine 2.15.0 documentation","url":"https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/examples/attention/attention.html"},{"title":"FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision – PyTorch","url":"https://pytorch.org/blog/flashattention-3/"},{"title":"Gated DeltaNet | Sebastian Raschka, PhD","url":"https://sebastianraschka.com/llms-from-scratch/ch04/08_deltanet/"},{"title":"ELI5: Flash Attention","url":"https://gordicaleksa.medium.com/eli5-flash-attention-5c44017022ad"},{"title":"A Visual Guide to Flash Attention, Linear Attention, and Efficient Transformers | by Zaina Haider | Medium","url":"https://medium.com/@thekzgroupllc/a-visual-guide-to-flash-attention-linear-attention-and-efficient-transformers-32e4f900d084"}]

Based on the search results, I found relevant information about the flash-linear-attention repository. The flash-linear-attention project includes a fix that guards A_log and dt_bias re-initialization against loaded checkpoint values in GatedDeltaNet, Comba, and KDA. Additionally, there were breaking chang
…[truncated 954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 210 · 2026-05-18T12:32:39.167617+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/releases",
  "prompt": "List all releases with dates and key changes. I'm especially interested in: breaking changes between 0.2.x and 0.3.0, between 0.3.x and 0.4.0, and between 0.4.x and 0.5.0. Focus on any changes to GatedDeltaNet, the attn.D parameter, attention module config schema, and HybridLinearAttention configs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/releases",
    "prompt": "List all releases with dates and key changes. I'm especially interested in: breaking changes between 0.2.x and 0.3.0, between 0.3.x and 0.4.0, and between 0.4.x and 0.5.0. Focus on any changes to GatedDeltaNet, the attn.D parameter, attention module config schema, and HybridLinearAttention configs."
  }
}
```

</details>

---

### Tool call

_source line 211 · 2026-05-18T12:32:39.167882+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-pure/blob/main/config.json",
  "prompt": "Show full config.json contents including all attn-related fields, model architecture fields, and any version hints."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-pure/blob/main/config.json",
    "prompt": "Show full config.json contents including all attn-related fields, model architecture fields, and any version hints."
  }
}
```

</details>

---

### Tool result

_source line 212 · 2026-05-18T12:32:39.168122+00:00_

# GatedDeltaNet Configuration (1.3B-100B-GatedDeltaNet-pure)

## Full Configuration

```json
{
  "architectures": ["GatedDeltaNetForCausalLM"],
  "attn": null,
  "attn_mode": "chunk",
  "bos_token_id": 1,
  "conv_size": 4,
  "eos_token_id": 2,
  "expand_k": 1,
  "expand_v": 1,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "head_dim": 256,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 2048,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "gated_deltanet",
  "norm_eps": 1e-06,
  "norm_first": false,
  "num_heads": 8,
  "num_hidden_layers": 24,
  "qk_activation": "silu",
  "qk_norm": "l2",
  "tie_word_embeddings": false,
  "torch_dtype": "float32",
  "transformers_version": "4.51.3",
  "use_beta": true,
  "use_cache": true,
  "use_gate": true,
  "use_output_norm": true,
  "use_short_conv": true,
  "vocab_size": 32000
}
```

## Key Architecture Details

| Parameter | Value | Purpose |
|-----------|-------|---------|
| **Model Type** | `gated_deltanet` | Alternative to standard Transformer attention |
| **Hidden Size** | 2048 | Embedding dimension |
| **Num Layers** | 24 | Depth of the model |
| **Num Heads** | 8 | Multi-head configuration |
| **Head Dim** | 256 | Per-head dimension (2048/8) |
| **Attn Mode** | `chunk` | Chunked attention mechanism |
| **Conv Size** | 4 | Local convolution window |
| **Max Seq Length** | 2048 | Context window |
| **Vocab Size** | 32000 | Token vocabulary |

## Attention-Related Fields
- `attn`: `null` (not using standard attention)
- `attn_mode`: `"chunk"` (chunked/local attention pattern)
- `qk_activation`: `"silu"` (query-key activation)
- `qk_norm`: `"l2"` (L2 normalization on Q/K)

## Optimization Flags
- `fuse_cross_entropy`: `true`
- `fuse_norm`: `true`
- `fuse_swiglu`: `true`
- `use_cache`: `true`
- `use_gate`: `true`
- `use_short_conv`: `true`

**Framework**: Transformers v4.51.3 | **Dtype**: float32

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-18T12:32:39.168370+00:00_

# Flash-Linear-Attention Release Summary

## v0.2.x → v0.3.0 Breaking Changes

The major API shift removed the `head_first` parameter across multiple operations:
- **[v0.2.0]** "Remove `head_first` option" was implemented progressively through multiple PRs (#337, #338, #339, #342, #345, #347)
- Parameter `offsets` was renamed to `cu_seqlens` in attention operations
- GatedDeltaNet kernel was refactored: "Refactor the kernel to remove one matrix inversion" (#433)

## v0.3.x → v0.4.0 Breaking Changes

**Minimum PyTorch requirement upgraded to 2.7.0** (#801 in v0.5.0, but changes started accumulating in this window)

Key architectural additions:
- **Kimi Delta Attention (KDA)** introduced as primary new model
- Backend system introduced with dispatch mechanism (#741, #742)
- GatedDeltaNet received "native GVA support: remove redundant Q/K repeat" (#812)

## v0.4.x → v0.5.0 Breaking Changes

**Multi-backend migration from Triton-only stack:**
- "moving from a Triton-only stack to a multi-backend one"
- FlashKDA backend added for KDA (#852)
- TileLang backend introduced for GDN, KDA, parallel attention kernels (#827, #846, #854)

**MoBA/FlashMoBA integration** (#840, #845) - Moonshot's Mixture of Block Attention

**Deprecated features removed:**
- "Remove deprecated head_first parameter from public ops" (#853)

## Configuration Schema Notes

- v0.3.0 introduced ShortConv backend parameter replacing `use_fast_conv1d` (#456)
- KDA added `safe_gate` and `lower_bound` support (#814)
- GDN added fused gate kernel with `use_gate_in_kernel` (#813)

No explicit breaking changes documented for HybridLinearAttention configs across these versions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-18T12:32:39.168631+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-6-1/blob/main/config.json",
  "prompt": "Show full config.json contents, especially the \"attn\" field with all its sub-fields (num_heads, num_kv_heads, qkv_bias, window_size, layers, rope_theta, D, etc.). I need every field inside attn:."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-6-1/blob/main/config.json",
    "prompt": "Show full config.json contents, especially the \"attn\" field with all its sub-fields (num_heads, num_kv_heads, qkv_bias, window_size, layers, rope_theta, D, etc.). I need every field inside attn:."
  }
}
```

</details>

---

### Tool call

_source line 215 · 2026-05-18T12:32:39.168869+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/blob/v0.2.2/fla/models/gated_deltanet/configuration_gated_deltanet.py",
  "prompt": "Show the GatedDeltaNetConfig class fields, especially what fields are accepted in the attn dictionary. List all defaults and constructor parameters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/blob/v0.2.2/fla/models/gated_deltanet/configuration_gated_deltanet.py",
    "prompt": "Show the GatedDeltaNetConfig class fields, especially what fields are accepted in the attn dictionary. List all defaults and constructor parameters."
  }
}
```

</details>

---

### Tool result

_source line 216 · 2026-05-18T12:32:39.169081+00:00_

# GatedDeltaNet Attention Configuration

Here's the complete `attn` field from the config.json:

```json
"attn": {
  "layers": [6, 11, 17, 23],
  "num_heads": 32,
  "num_kv_heads": 8,
  "qkv_bias": false,
  "rope_theta": 10000.0,
  "window_size": null
}
```

## Attention Field Breakdown

| Field | Value | Description |
|-------|-------|-------------|
| `layers` | `[6, 11, 17, 23]` | Indices of layers where attention is applied (4 layers total) |
| `num_heads` | `32` | Number of attention heads |
| `num_kv_heads` | `8` | Number of key-value heads (supports grouped query attention) |
| `qkv_bias` | `false` | No bias terms in Q, K, V projections |
| `rope_theta` | `10000.0` | Rotary position embedding base frequency |
| `window_size` | `null` | No local attention window (full attention) |

## Model Context

- **Model Type**: GatedDeltaNet (hybrid architecture)
- **Attention Mode**: `chunk`
- **Total Hidden Layers**: 24 (only 4 use attention)
- **Hidden Size**: 2048
- **Head Dimension**: 256
- **Max Position Embeddings**: 2048

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 217 · 2026-05-18T12:32:39.169311+00:00_

# GatedDeltaNetConfig Class Overview

## Constructor Parameters with Defaults

| Parameter | Default | Type |
|-----------|---------|------|
| `attn_mode` | "chunk" | str |
| `hidden_size` | 2048 | int |
| `expand_v` | 2 | int |
| `use_gate` | True | bool |
| `use_short_conv` | True | bool |
| `conv_size` | 4 | int |
| `head_dim` | 256 | int |
| `num_heads` | 6 | int |
| `num_v_heads` | None | Optional[int] |
| `max_position_embeddings` | 2048 | int |
| `hidden_ratio` | 4 | Optional[int] |
| `intermediate_size` | None | Optional[int] |
| `hidden_act` | "swish" | str |
| `num_hidden_layers` | 21 | int |
| `norm_eps` | 1e-6 | float |
| `attn` | None | Optional[Dict] |
| `use_cache` | True | bool |
| `pad_token_id` | None | int |
| `bos_token_id` | 1 | int |
| `eos_token_id` | 2 | int |
| `tie_word_embeddings` | False | bool |
| `initializer_range` | 0.02 | float |
| `fuse_norm` | True | bool |
| `fuse_swiglu` | True | bool |
| `fuse_cross_entropy` | True | bool |
| `vocab_size` | 32000 | int |

## Attention Dictionary (`attn`) Fields

When provided, the `attn` parameter must include:

- **Required fields:**
  - `layers` — layer indices for hybrid attention
  - `num_heads` — number of attention heads

- **Auto-populated fields** (if not provided):
  - `num_kv_heads` — defaults to `num_heads`
  - `qkv_bias` — defaults to False
  - `window_size` — defaults to None
  - `rope_theta` — defaults to 10000.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 218 · 2026-05-18T12:32:39.169566+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/blob/main/fla/models/gated_deltanet/configuration_gated_deltanet.py",
  "prompt": "Show the latest GatedDeltaNetConfig class. List ALL parameters in the constructor including the contents of the `attn` dict. I'm specifically looking for whether there's a \"D\" field in attn, when it was added, and what it does. Also list the difference vs older versions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/blob/main/fla/models/gated_deltanet/configuration_gated_deltanet.py",
    "prompt": "Show the latest GatedDeltaNetConfig class. List ALL parameters in the constructor including the contents of the `attn` dict. I'm specifically looking for whether there's a \"D\" field in attn, when it was added, and what it does. Also list the difference vs older versions."
  }
}
```

</details>

---

### Tool call

_source line 219 · 2026-05-18T12:32:39.169802+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/blob/v0.3.0/fla/layers/attn.py",
  "prompt": "Show the Attention class __init__ signature and all parameters. I'm looking for whether there's a \"D\" parameter and what fields are read from the attn config dict (e.g., self.D, self.window_size, etc.)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/blob/v0.3.0/fla/layers/attn.py",
    "prompt": "Show the Attention class __init__ signature and all parameters. I'm looking for whether there's a \"D\" parameter and what fields are read from the attn config dict (e.g., self.D, self.window_size, etc.)."
  }
}
```

</details>

---

### Tool result

_source line 220 · 2026-05-18T12:32:39.170012+00:00_

# GatedDeltaNetConfig Constructor Parameters

Based on the provided code, here are **all parameters** in the `__init__` method:

## Main Parameters
- `attn_mode`, `hidden_size`, `expand_v`, `use_gate`, `use_short_conv`, `allow_neg_eigval`, `conv_size`, `head_dim`, `num_heads`, `num_v_heads`, `max_position_embeddings`, `hidden_ratio`, `intermediate_size`, `hidden_act`, `num_hidden_layers`, `norm_eps`, `attn`, `use_cache`, `pad_token_id`, `bos_token_id`, `eos_token_id`, `tie_word_embeddings`, `initializer_range`, `fuse_norm`, `fuse_swiglu`, `fuse_cross_entropy`, `fuse_linear_cross_entropy`, `use_l2warp`, `vocab_size`, `attnres_block_size`

## Attn Dict Contents
When `attn` is provided, it includes:
- `'layers'` (required)
- `'num_heads'` (required)
- `'num_kv_heads'` (optional, defaults to num_heads)
- `'qkv_bias'` (optional, defaults to False)
- `'window_size'` (optional, defaults to None)
- `'rope_theta'` (optional, defaults to 10000)

## Key Finding
**There is no "D" field present** in the `attn` dictionary based on this code snapshot. The file shows 116 lines with no mention of a "D" parameter or field. Without access to historical versions or commit history, I cannot determine when such a field might have been added or removed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-18T12:32:39.170238+00:00_

# Attention Class __init__ Signature

The `__init__` method signature is:

```python
def __init__(
    self,
    hidden_size: int = 2048,
    num_heads: int = 32,
    num_kv_heads: Optional[int] = None,
    qkv_bias: bool = False,
    qk_norm: bool = False,
    window_size: Optional[int] = None,
    rope_theta: Optional[float] = 10000.,
    max_position_embeddings: Optional[int] = None,
    layer_idx: int = None
)
```

## Key Findings

**No "D" parameter exists** in this attention class initialization.

**Fields stored from parameters:**
- `self.hidden_size`
- `self.num_heads`
- `self.num_kv_heads`
- `self.qkv_bias`
- `self.qk_norm`
- `self.window_size`
- `self.rope_theta`
- `self.max_position_embeddings`
- `self.layer_idx`

The class also computes derived fields like `self.head_dim`, `self.kv_dim`, and `self.num_kv_groups` based on the input parameters. There is no configuration dictionary unpacking; all parameters are explicitly defined in the signature.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 222 · 2026-05-18T12:32:39.170490+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"m-a-p\" \"GatedDeltaNet\" github \"flash-linear-attention\" requirements OR install"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"m-a-p\" \"GatedDeltaNet\" github \"flash-linear-attention\" requirements OR install"
  }
}
```

</details>

---

### Tool call

_source line 223 · 2026-05-18T12:32:39.170718+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/blob/v0.2.2/fla/layers/attn.py",
  "prompt": "Show the Attention class __init__ signature including all parameters. Does this version accept a \"D\" parameter? What is the full parameter list?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/blob/v0.2.2/fla/layers/attn.py",
    "prompt": "Show the Attention class __init__ signature including all parameters. Does this version accept a \"D\" parameter? What is the full parameter list?"
  }
}
```

</details>

---

### Tool result

_source line 224 · 2026-05-18T12:32:39.170940+00:00_

# Attention Class __init__ Signature

Based on the code shown, here is the complete parameter list for the `Attention` class initialization:

```python
def __init__(
    self,
    hidden_size: int = 2048,
    num_heads: int = 32,
    num_kv_heads: Optional[int] = None,
    qkv_bias: bool = False,
    qk_norm: bool = False,
    window_size: Optional[int] = None,
    rope_theta: Optional[float] = 10000.,
    max_position_embeddings: Optional[int] = None,
    layer_idx: int = None
):
```

**Does it accept a "D" parameter?**

No, this version does not include a "D" parameter. The dimensional configuration is determined by `hidden_size` and `num_heads` instead, with the head dimension being calculated internally as `hidden_size // num_heads`.

**Full parameter list (9 parameters):**
1. hidden_size
2. num_heads
3. num_kv_heads
4. qkv_bias
5. qk_norm
6. window_size
7. rope_theta
8. max_position_embeddings
9. layer_idx

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 225 · 2026-05-18T12:32:39.171230+00:00_

Web search results for query: ""m-a-p" "GatedDeltaNet" github "flash-linear-attention" requirements OR install"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"},{"title":"GitHub - NVlabs/GatedDeltaNet: [ICLR 2025] Official PyTorch Implementation of Gated Delta Networks: Improving Mamba2 with Delta Rule · GitHub","url":"https://github.com/NVlabs/GatedDeltaNet"},{"title":"GitHub - Fzkuji/flash-linear: 🚀 Efficient implementations of state-of-the-art linear attention models in Pytorch and Triton","url":"https://github.com/Fzkuji/flash-linear-attention"},{"title":"Gated DeltaNet for Linear Attention - rasbt/LLMs-from-scratch","url":"https://github.com/rasbt/LLMs-from-scratch/blob/main/ch04/08_deltanet/README.md"},{"title":"flash-linear-attention/FAQs.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/FAQs.md"},{"title":"GitHub - berlino/gated_linear_attention · GitHub","url":"https://github.com/berlino/gated_linear_attention"},{"title":"DeltaNet Explained (Part I) | Songlin Yang","url":"https://sustcsonglin.github.io/blog/2024/deltanet-1/"},{"title":"flash-linear-attention/fla/ops/cp/README.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/fla/ops/cp/README.md"},{"title":"GitHub - idiap/hybrid-linear-sparse-attention: Alleviating Forgetfulness of Linear Attention by Hybrid Sparse Attention and Contextualized Learnable Token Eviction.","url":"https://github.com/idiap/hybrid-linear-sparse-attention"}]

Based on the search results, I found relevant information about GatedDeltaNet and flash-linear-attention:

## Installation Information

Starting from v0.3.2, the packages published on PyPI are fla-core and
…[truncated 930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 226 · 2026-05-18T12:32:39.171539+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/blob/main/fla/models/gated_deltanet/modeling_gated_deltanet.py",
  "prompt": "Show how the model instantiates the Attention layer from the `attn` config dict. List all the keys it reads from `config.attn` (e.g., config.attn['layers'], config.attn['num_heads'], etc.). Are there any new keys read like 'D' or any required key beyond layers/num_heads/num_kv_heads/qkv_bias/window_size/rope_theta?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/blob/main/fla/models/gated_deltanet/modeling_gated_deltanet.py",
    "prompt": "Show how the model instantiates the Attention layer from the `attn` config dict. List all the keys it reads from `config.attn` (e.g., config.attn['layers'], config.attn['num_heads'], etc.). Are there any new keys read like 'D' or any required key beyond layers/num_heads/num_kv_heads/qkv_bias/window_size/rope_theta?"
  }
}
```

</details>

---

### Tool call

_source line 227 · 2026-05-18T12:32:39.171782+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/blob/v0.5.0/fla/layers/attn.py",
  "prompt": "Show the Attention class __init__ signature and any **kwargs unpacking. Does this version accept \"D\" parameter? What is the full parameter list? Also show any model.from_config or AttentionConfig that may differ from old versions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/fla-org/flash-linear-attention/blob/v0.5.0/fla/layers/attn.py",
    "prompt": "Show the Attention class __init__ signature and any **kwargs unpacking. Does this version accept \"D\" parameter? What is the full parameter list? Also show any model.from_config or AttentionConfig that may differ from old versions."
  }
}
```

</details>

---

### Tool result

_source line 228 · 2026-05-18T12:32:39.172007+00:00_

# Attention Layer Instantiation in GatedDeltaNetBlock

Based on the code, the Attention layer is instantiated conditionally when certain criteria are met. Here's how it works:

## Instantiation Logic

The model checks if `config.attn is not None` and if the current `layer_idx` is in `config.attn['layers']`. When both conditions are true, it creates an Attention instance:

```python
self.attn = Attention(
    hidden_size=config.hidden_size,
    num_heads=config.attn['num_heads'],
    num_kv_heads=config.attn['num_kv_heads'],
    qkv_bias=config.attn['qkv_bias'],
    window_size=config.attn['window_size'],
    rope_theta=config.attn['rope_theta'],
    max_position_embeddings=config.max_position_embeddings,
    layer_idx=layer_idx,
)
```

## Keys Read from config.attn

The implementation reads **exactly five keys** from the `config.attn` dictionary:

1. `'layers'` – specifies which layers use Attention
2. `'num_heads'` – number of attention heads
3. `'num_kv_heads'` – number of key-value heads
4. `'qkv_bias'` – whether to include bias in projections
5. `'window_size'` – attention window constraint
6. `'rope_theta'` – rotary position embedding base

## Additional Parameters

The Attention constructor also receives `max_position_embeddings` and `layer_idx` directly from the config and layer context, not from the `attn` dict.

**No additional keys** like 'D' are referenced in this code snippet.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 229 · 2026-05-18T12:32:39.172245+00:00_

# Attention Class Analysis

## `__init__` Signature

```python
def __init__(
    self,
    hidden_size: int = 2048,
    num_heads: int = 32,
    num_kv_heads: int | None = None,
    qkv_bias: bool = False,
    qk_norm: bool = False,
    window_size: int | None = None,
    rope_theta: float | None = 10000.,
    max_position_embeddings: int | None = None,
    layer_idx: int = None,
):
```

## "D" Parameter

No, this version does **not** accept a "D" parameter.

## Full Parameter List

The complete initialization parameters are:
- `hidden_size` (default: 2048)
- `num_heads` (default: 32)
- `num_kv_heads` (optional)
- `qkv_bias` (default: False)
- `qk_norm` (default: False)
- `window_size` (optional)
- `rope_theta` (default: 10000.0)
- `max_position_embeddings` (optional)
- `layer_idx` (optional)

## Config Methods

The provided code does not include `from_config()` methods or an `AttentionConfig` class definition. The page shows only the core `Attention` class implementation without configuration factory methods.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_wang-fla-version_20260518T122417",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 230 · 2026-05-18T12:32:39.172574+00:00_

## Wang et al. (arXiv 2507.06457) 使用的 fla 版本调查结果

### 1. 版本推断

论文提交日期：**2025-07-08**。模型 config.json 中 `transformers_version: "4.51.3"`。

fla 版本时间线：

| 版本 | 发布日期 | 与论文关系 |
|---|---|---|
| 0.2.0 | 2025-04-11 | 训练前 |
| 0.2.1 | 2025-04-23 | 训练中 |
| **0.2.2** | **2025-06-05** | **✅ 论文提交前最后一个发布版** |
| 0.3.0 | 2025-07-14 | 论文提交后 6 天才发布，**不可能用** |
| 0.3.1 | 2025-08-26 | — |
| 0.4.0 | 2025-10-27 | — |
| 0.5.0 | 2026-04-21 | — |

**结论：Wang et al. 训练时最可能用的是 fla 0.2.2**（或紧邻该版本的 main 分支 commit）。无显式 pin。

### 2. m-a-p config 中的实际 attn 字段

`m-a-p/1.3B-100B-GatedDeltaNet-hybrid-6-1/config.json` 的 `attn`:

```json
{
  "layers": [6, 11, 17, 23],
  "num_heads": 32,
  "num_kv_heads": 8,
  "qkv_bias": false,
  "rope_theta": 10000.0,
  "window_size": null
}
```

**没有 `D` 字段。** 在 0.2.2 / 0.3.0 / 0.5.0 / main 各版本的 `Attention.__init__` 中均无 `D` 参数，`GatedDeltaNetBlock` 从 `config.attn` 只读取上述 6 个 key。

> 你说的 "attn.D parameter" 不是 fla 的真实字段。如果运行报 `unexpected keyword argument 'D'` 或类似错误，应贴出完整 traceback 重新定位 —— 大概率不是 fla 版本问题本身，而是 GatedDeltaNet 层（不是 attn）的某个内部张量 `D`（如 mamba-style skip 项）在新版本被重命名/删除。

### 3. 主要 breaking changes

**0.2.x → 0.3.0**
- 多个 op 删除 `head_first` 参数（#337–#347）
- 注意力相关 op 中 `offsets` 重命名为 `cu_seqlens`
- GatedDeltaNet kernel 重构以去掉一次矩阵求逆（#433）

**0.3.x → 0.4.0**
- 引入 backend 调度系统（#741, #742）
- 引入 KDA (Kimi Delta Attention)
- GDN 增加 native GVA 支持，移除冗余 Q/K repeat（#812）
- GDN 增加 `use_gate_in_kernel` 融合 gate kernel（#813）

**0.4.x → 0.5.0**
- PyTorch 最低 2.7.0
- Triton-only → 多后端（TileLang, FlashKDA），新增 `FlashKDA` 后端
- 公开 op 中彻底删除 deprecated `head_first`（#853）
- MoBA / FlashMoBA 集成

### 4. 降级建议

```bash
pip install flash-linear-attention==0.2.2
```

或固定到论文提交前的 main 分支：

```bash
pip install "git+https://github.com/fla-org/flash-linear-attention.git@v0.2.2"
```

如需更精确复现，可用 2025-06-05 ~ 2025-07-08 之间的 commit。注意 0.3.2 之后 PyPI 拆分成 `fla-core` + `flash-linear-attention` 两个包，0.2.2 仍是单包，安装更简单。

### 5. 下一步建议

如果当前问题是加载 m-a-p checkpoint 失败：
1. 先 `pip install flash-linear-attention==0.2.2` 测试 checkpoint 是否能直接 load
2. 如果仍报 `D` 字段错误，把完整 traceback 贴出来 —— 多半是 GatedDeltaNet 内部 state_dict key 不匹配（如 `A_log`, `D`, `dt_bias` 等 mamba-lineage 张量），而不是 config dict 不匹配
3. 0.2.2 对应 transformers `>=4.45,<=4.51.x` 范围，建议同时 pin `transformers==4.51.3`

Sources:
- [arXiv 2507.06457 - Wang et al.](https://arxiv.org/abs/2507.06457)
- [m-a-p Hybrid Linear Attention collection](https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e)
- [flash-linear-attention PyPI](https://pypi.org/project/flash-linear-attention/)
- [fla-org/flash-linear-attention GitHub](https://github.com/fla-org/flash-linear-attention)
- [fla releases](https://github.com/fla-org/flash-linear-attention/releases)
- [fla FAQs](https://github.com/fla-org/flash-linear-attention/blob/main/FAQs.md)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_wang-fla-version_20260518T122417"
}
```

</details>

---
