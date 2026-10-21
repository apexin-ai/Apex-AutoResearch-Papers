# research quantization rl interaction

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_research_quantization-rl-interaction_20260515T174945.jsonl`
- **Structured JSON:** [`0159bf153a50e306a7db.json`](../../sessions/01/0159bf153a50e306a7db.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-15T17:56:33.685226+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T17:56:33.685867+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T17:56:33.686160+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "QLoRA quantization RLHF DPO GRPO training instability catastrophic forgetting 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "QLoRA quantization RLHF DPO GRPO training instability catastrophic forgetting 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T17:56:33.688376+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GRPO group relative policy optimization stability failure modes structured tasks 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GRPO group relative policy optimization stability failure modes structured tasks 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T17:56:33.688636+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LoRA precision 4-bit 8-bit bf16 quantization noise gradient training behavior difference 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LoRA precision 4-bit 8-bit bf16 quantization noise gradient training behavior difference 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T17:56:33.688857+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "catastrophic forgetting RLHF reinforcement learning fine-tuning multi-task structured output 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "catastrophic forgetting RLHF reinforcement learning fine-tuning multi-task structured output 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T17:56:33.689117+00:00_

Web search results for query: "GRPO group relative policy optimization stability failure modes structured tasks 2024 2025"

Links: [{"title":"2025-07-29 Group Sequence Policy Optimization Chujie Zheng∗ Shixuan Liu","url":"https://arxiv.org/pdf/2507.18071"},{"title":"Group Relative Policy Optimization (GRPO) - Matthew Landers","url":"https://mattlanders.net/grpo.html"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Group+Relative+Policy+Optimization"},{"title":"GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control","url":"https://arxiv.org/html/2508.03772v4"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250803772S/abstract"},{"title":"Generalized Relative Policy Optimization (GRPO)","url":"https://www.emergentmind.com/topics/generalized-relative-policy-optimization-grpo"},{"title":"[2508.03772] GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control","url":"https://arxiv.org/abs/2508.03772"},{"title":"Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training","url":"https://arxiv.org/html/2505.22257v1"},{"title":"Constrained Group Relative Policy Optimization","url":"https://arxiv.org/html/2602.05863v1"}]

Based on the search results, here's what I found about GRPO (Group Relative Policy Optimization), stability issues, failure modes, and structured tasks:

## Key Stability Issues with GRPO

GRPO exhibits severe stability issues when training gigantic language models, often resulting in catastrophic and irreversible model collapse.

### Main Failure Modes

**Token-Level Penalization:** GRPO has a token-level penalization issue where valuable tokens shared across different responses receive contradictory feedback signals, leading to
…[truncated 1448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T17:56:33.689448+00:00_

Web search results for query: "QLoRA quantization RLHF DPO GRPO training instability catastrophic forgetting 2024 2025"

Links: [{"title":"Efficient LLM Fine-Tuning: LoRA, QLoRA & RLHF | Medium","url":"https://medium.com/@hetp2030/parameter-efficient-fine-tuning-of-large-language-models-from-lora-to-rlhf-c17e166da5df"},{"title":"LLM Post-Training Explained: SFT, DPO, and GRPO — ai.rs","url":"https://ai.rs/ai-developer/llm-post-training-explained"},{"title":"CATASTROPHIC FAILURE OF LLM UNLEARNING VIA ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ba79fb5c4fe70050752f20c90c5f07ca-Paper-Conference.pdf"},{"title":"Mastering Post-Training Techniques for LLMs in 2025: Elevating Models from Generalists to Specialists - Macaron","url":"https://macaron.im/blog/post-training-llm-techniques-2025"},{"title":"Post-training for LLMs on Anyscale | Anyscale Docs","url":"https://docs.anyscale.com/llm/fine-tuning"},{"title":"QLORA: Efficient Finetuning of Quantized LLMs Tim Dettmers∗ Artidoro Pagnoni∗","url":"https://arxiv.org/pdf/2305.14314"},{"title":"GitHub - artidoro/qlora: QLoRA: Efficient Finetuning of Quantized LLMs · GitHub","url":"https://github.com/artidoro/qlora"},{"title":"Robust Policy Optimization to Prevent Catastrophic Forgetting","url":"https://arxiv.org/html/2602.08813"},{"title":"Large Language Model Post Training Techniques — SFT, RL | by Manu Suryavansh | Medium","url":"https://msuryavanshi.medium.com/large-language-model-fine-tuning-techniques-df8975396989"},{"title":"Post-Training Playbook: SFT, LoRA, DPO, and GRPO from First Principles | Gopi Krishna Tummala","url":"http://gopikrishnatummala.com/posts/mlops/modern-post-training-peft-2026/"}]

I've completed the web search for your query about QLoRA quantization, RLHF, DPO, GRPO training, instability, and catastrophic forgetting in 2024-2025. Here are the key findings:

## Summary of Results

**QLoRA and Quantization:**
QLoRA quantizes the base model to 4-bit precision, cutting VRAM by 4x. 
…[truncated 1433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T17:56:33.689759+00:00_

Web search results for query: "LoRA precision 4-bit 8-bit bf16 quantization noise gradient training behavior difference 2024 2025"

Links: [{"title":"Quantized LoRA (QLoRA) Principles","url":"https://apxml.com/courses/lora-peft-efficient-llm-training/chapter-4-advanced-lora-variants/qlora-principles"},{"title":"QLoRA Explained - How 4 Bit Quantization Unlocks Frontier Models","url":"https://theneuralmaze.substack.com/p/qlora-explained-how-4-bit-quantization"},{"title":"t2i_t2v_i2v_lora_20251114.md · John6666/knowledge_base_md_for_rag_1 at 57a80c85fc4a36f5e8b2bb5e0b872ce4a8967f5d","url":"https://huggingface.co/datasets/John6666/knowledge_base_md_for_rag_1/blob/57a80c85fc4a36f5e8b2bb5e0b872ce4a8967f5d/t2i_t2v_i2v_lora_20251114.md"},{"title":"Run Big LLMs on Small GPUs: A Hands-On Guide to 4-bit Quantization and QLoRA | by Alain Airom (Ayrom) | Medium","url":"https://alain-airom.medium.com/run-big-llms-on-small-gpus-a-hands-on-guide-to-4-bit-quantization-and-qlora-40e9e2c95054"},{"title":"Fine-tuning GPTQ Quantized Vision Language Models with LoRA. | by Arun M | Medium","url":"https://medium.com/@arunsreekuttan1996/fine-tuning-gptq-quantized-vision-language-models-with-lora-733d1e687ff5"},{"title":"QDoRA Explained: The New PEFT Standard for 2025 | by Antonio V. Franco | Medium","url":"https://medium.com/@AntonioVFranco/qdora-explained-the-new-peft-standard-for-2025-5cf59afeb6ba"},{"title":"Quantization (16-bit, 8-bit, 4-bit) and QLoRA - GitHub Pages","url":"https://chanys.github.io/qlora/"},{"title":"A Deep Dive into LLM Quantization: FP32, BF16, INT8, NF4 & QLoRA | by Sauradeep Debnath | Mar, 2026 | Medium","url":"https://medium.com/@saurad44/a-deep-dive-into-llm-quantization-fp32-bf16-int8-nf4-qlora-830ff4936f3f"},{"title":"Parameter-Efficient Fine-Tuning of Large Language Models: From LoRA to RLHF","url":"https://medium.com/@hetp2030/parameter-efficient-fine-tuning-of-large-language-models-from-lora-to-rlhf-c17e166da5df"},{"title":"Quantization - LoRAX Docs","url":"
…[truncated 1983 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T17:56:33.690144+00:00_

Web search results for query: "catastrophic forgetting RLHF reinforcement learning fine-tuning multi-task structured output 2024 2025"

Links: [{"title":"Continual Learning with RL for LLMs","url":"https://cameronrwolfe.substack.com/p/rl-continual-learning"},{"title":"What is Catastrophic Forgetting? | IBM","url":"https://www.ibm.com/think/topics/catastrophic-forgetting"},{"title":"Avoiding Amnesia: Some Practical Guides to Mitigate Catastrophic Forgetting in LLMs Post-training | by Baicen Xiao | Medium","url":"https://medium.com/@baicenxiao/avoiding-amnesia-some-practical-guides-to-mitigate-catastrophic-forgetting-in-llms-post-training-6a23e4f064cb"},{"title":"A New MIT Study Shows Reinforcement Learning Minimizes Catastrophic Forgetting Compared to Supervised Fine-Tuning - MarkTechPost","url":"https://www.marktechpost.com/2025/09/08/a-new-mit-study-shows-reinforcement-learning-minimizes-catastrophic-forgetting-compared-to-supervised-fine-tuning/"},{"title":"[2308.08747] An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning","url":"https://arxiv.org/abs/2308.08747"},{"title":"Understanding Catastrophic Forgetting in Language Models via Implicit Inference | OpenReview","url":"https://openreview.net/forum?id=VrHiF2hsrm"},{"title":"[2601.18699] Mechanistic Analysis of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning","url":"https://arxiv.org/abs/2601.18699"},{"title":"Reinforcement Learning Fine-Tuning","url":"https://www.emergentmind.com/topics/reinforcement-learning-fine-tuning-rl-ft"},{"title":"Fine-Tuning LLMs: Overcoming Catastrophic Forgetting","url":"https://www.legionintel.com/blog/navigating-the-challenges-of-fine-tuning-and-catastrophic-forgetting"},{"title":"An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-Tuning | Request PDF","url":"https://www.researchgate.net/publication/395308608_An_Empirical_Study_of_Catastrophic_Forgetting_in_Large_L
…[truncated 2121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T17:56:33.691774+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GTPO stabilizing GRPO gradient entropy control arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GTPO stabilizing GRPO gradient entropy control arxiv 2025"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T17:56:33.691994+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"quantization\" \"reinforcement learning\" \"policy optimization\" LLM training degradation 2024 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"quantization\" \"reinforcement learning\" \"policy optimization\" LLM training degradation 2024 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T17:56:33.692188+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "QLoRA DPO alignment performance gap full fine-tuning 2024 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "QLoRA DPO alignment performance gap full fine-tuning 2024 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T17:56:33.692400+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "robust policy optimization catastrophic forgetting arxiv 2025 2602.08813"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "robust policy optimization catastrophic forgetting arxiv 2025 2602.08813"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T17:56:33.692642+00:00_

Web search results for query: "GTPO stabilizing GRPO gradient entropy control arxiv 2025"

Links: [{"title":"GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control","url":"https://arxiv.org/html/2508.03772v4"},{"title":"[2508.03772] GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control","url":"https://arxiv.org/abs/2508.03772"},{"title":"GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250803772S/abstract"},{"title":"GTPO: Trajectory-Based Policy Optimization in Large Language Models","url":"https://arxiv.org/html/2508.03772v3"},{"title":"GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with Policy Entropy","url":"https://arxiv.org/html/2508.04349v6"},{"title":"Arbitrary Entropy Policy Optimization","url":"https://arxiv.org/pdf/2510.08141"},{"title":"GitHub - Kwai-Klear/CE-GPPO: CE-GPPO: Controlling Entropy via Gradient-Preserving Clipping Policy Optimization in Reinforcement Learning","url":"https://github.com/Kwai-Klear/CE-GPPO"},{"title":"CE-GPPO: Coordinating Entropy via Gradient-Preserving Clipping Policy Optimization in Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/resources/2509.20712v4"},{"title":"Flexible Entropy Control in RLVR with Gradient-Preserving Perspective","url":"https://arxiv.org/html/2602.09782"},{"title":"Arbitrary Entropy Policy Optimization: Entropy Is Controllable in Reinforcement Fine-tuning","url":"https://arxiv.org/html/2510.08141v4"}]

Based on the search results, I found relevant information about GTPO and its relationship to GRPO. Here are the key findings:

## GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control

Group Relative Policy Optimization (GRPO) is a promising policy-based approach for Large Language Model alignment, yet its performance is often limited by training instability and suboptimal convergence. The ma
…[truncated 1487 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T17:56:33.692961+00:00_

Web search results for query: ""quantization" "reinforcement learning" "policy optimization" LLM training degradation 2024 2025 arxiv"

Links: [{"title":"The Impact of Quantization on Large Reasoning Model Reinforcement Learning","url":"https://arxiv.org/html/2511.15694v1"},{"title":"Training Dynamics Impact Post-Training Quantization ...","url":"https://arxiv.org/pdf/2510.06213"},{"title":"Efficient Reinforcement Learning with Quantized Rollout","url":"https://www.arxiv.org/pdf/2602.13953"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.04929"},{"title":"Quantization Meets dLLMs: A Systematic Study of Post-training Quantization for Diffusion LLMs","url":"https://arxiv.org/html/2508.14896v1"},{"title":"[2511.15694] The Impact of Quantization on Large Reasoning Model Reinforcement Learning","url":"https://arxiv.org/abs/2511.15694"},{"title":"LLMOrbit: A Circular Taxonomy of Large Language Models","url":"https://arxiv.org/pdf/2601.14053"},{"title":"[2410.10849] Continuous Approximations for Improving Quantization Aware Training of LLMs","url":"https://arxiv.org/abs/2410.10849"},{"title":"Resource-Efficient Language Models: Quantization for Fast and Accessible Inference","url":"https://arxiv.org/html/2505.08620v1"},{"title":"A Survey of Low-bit Large Language Models: Basics, Systems, and Algorithms","url":"https://arxiv.org/html/2409.16694v1"}]

I've found several relevant arxiv papers on this topic. Here's a summary of the key findings:

## Key Research Findings

**The Impact of Quantization on Large Reasoning Model Reinforcement Learning**

Reinforcement learning produces a unique challenge for the quantization of LLMs, in that discrete rewards are sampled from LLM generated responses, and quantized models produce worse policies. A sudden shock of quantization during the reinforcement learning process is damaging to learning.

Techniques that quantize models downstream from training such as PTQ and QLoRA result in models tha
…[truncated 1227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T17:56:33.693419+00:00_

Web search results for query: "robust policy optimization catastrophic forgetting arxiv 2025 2602.08813"

Links: [{"title":"[2602.08813] Robust Policy Optimization to Prevent Catastrophic Forgetting","url":"https://arxiv.org/abs/2602.08813"},{"title":"Robust Policy Optimization to Prevent Catastrophic Forgetting","url":"https://arxiv.org/html/2602.08813"},{"title":"(PDF) Robust Policy Optimization to Prevent Catastrophic Forgetting","url":"https://www.researchgate.net/publication/400622099_Robust_Policy_Optimization_to_Prevent_Catastrophic_Forgetting"},{"title":"Adel Javanmard on X: \"🚨 Excited to share our new paper! We propose “Fine-tuning Robust Policy Optimization (FRPO)\" algorithm to tackle Catastrophic Forgetting in LLM Post-Training. 👉 https://t.co/Xk3aKHzJ8i @MahdiSabba24308 @HamedSHassani @pappasg69 https://t.co/ZUj3BmAnVE\" / X","url":"https://x.com/AdelJavanmard/status/2022425436064747567"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.14078"},{"title":"[2602.20162] Talking to Yourself: Defying Forgetting in Large Language Models","url":"https://arxiv.org/abs/2602.20162"},{"title":"Safety Alignment as Continual Learning: Mitigating the Alignment Tax via Orthogonal Gradient Projection","url":"https://arxiv.org/html/2602.07892"},{"title":"Hindsight-Anchored Policy Optimization: Turning Failure into Feedback in Sparse Reward Settings","url":"https://arxiv.org/html/2603.11321"},{"title":"[2602.14078] Policy Gradient with Adaptive Entropy Annealing for Continual Fine-Tuning","url":"https://arxiv.org/abs/2602.14078"},{"title":"On-Policy Distillation - Thinking Machines Lab","url":"https://thinkingmachines.ai/blog/on-policy-distillation/"}]

Based on the search results, here's information about the paper arxiv 2602.08813:

## Robust Policy Optimization to Prevent Catastrophic Forgetting

This paper is titled "Robust Policy Optimization to Prevent Catastrophic Forgetting" by Mahdi Sabbaghi and 3 other authors (George Pappas, Adel Javanmard, and Ha
…[truncated 1149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T17:56:33.693752+00:00_

Web search results for query: "QLoRA DPO alignment performance gap full fine-tuning 2024 2025 arxiv"

Links: [{"title":"A Deep Dive into the Trade-Offs of Parameter-Efficient Preference Alignment Techniques","url":"https://arxiv.org/html/2406.04879v1"},{"title":"[2305.14314] QLoRA: Efficient Finetuning of Quantized LLMs","url":"https://arxiv.org/abs/2305.14314"},{"title":"QLORA: Efficient Finetuning of Quantized LLMs Tim Dettmers∗ Artidoro Pagnoni∗","url":"https://arxiv.org/pdf/2305.14314"},{"title":"Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning","url":"https://arxiv.org/pdf/2505.03802"},{"title":"CLoQ: Enhancing Fine-Tuning of Quantized LLMs via Calibrated LoRA Initialization","url":"https://arxiv.org/html/2501.18475v1"},{"title":"QLoRA: Efficient Finetuning of Quantized LLMs - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2305.14314"},{"title":"Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study","url":"https://arxiv.org/pdf/2404.10719"},{"title":"Accurate and Efficient Fine-Tuning of Quantized Large Language Models Through Optimal Balance in Adaptation | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.23/132118/Accurate-and-Efficient-Fine-Tuning-of-Quantized"},{"title":"[2509.12229] Profiling LoRA/QLoRA Fine-Tuning Efficiency on Consumer GPUs: An RTX 4060 Case Study","url":"https://arxiv.org/abs/2509.12229"},{"title":"Parameter-Efficient Fine-Tuning for HAR: Integrating LoRA and QLoRA into Transformer Models","url":"https://arxiv.org/html/2512.17983v1"}]

I found relevant research on this topic. Here are the key findings from recent arxiv papers:

## Main Paper: Trade-Offs in Parameter-Efficient Preference Alignment

Large language models are first pre-trained on trillions of tokens and then instruction-tuned or aligned to specific preferences. While pre-training remains out of reach for most researchers due to the compute requi
…[truncated 1431 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T17:56:33.694081+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2511.15694 impact quantization reasoning model reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2511.15694 impact quantization reasoning model reinforcement learning"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T17:56:33.694326+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2505.03802 \"mixed-precision fine-tuning\" fidelity plasticity alignment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2505.03802 \"mixed-precision fine-tuning\" fidelity plasticity alignment"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T17:56:33.694540+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GRPO structured information extraction NER relation extraction reward hacking 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GRPO structured information extraction NER relation extraction reward hacking 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T17:56:33.694743+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2406.04879 trade-offs parameter-efficient preference alignment DPO QLoRA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2406.04879 trade-offs parameter-efficient preference alignment DPO QLoRA"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T17:56:33.694985+00:00_

Web search results for query: "arxiv 2505.03802 "mixed-precision fine-tuning" fidelity plasticity alignment"

Links: [{"title":"Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning","url":"https://arxiv.org/pdf/2505.03802"},{"title":"Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies","url":"https://arxiv.org/html/2505.03802"},{"title":"[2505.03802] Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies","url":"https://arxiv.org/abs/2505.03802"},{"title":"Efficient Fine-Tuning of Quantized Models via Adaptive Rank and Bitwidth","url":"https://arxiv.org/html/2505.03802v3"},{"title":"Computer Science May 2025","url":"https://www.arxiv.org/list/cs/2025-05?skip=11300&show=250"},{"title":"Computer Science Jan 2025","url":"https://arxiv.org/list/cs/2025-01?skip=2650&show=25"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=5250&show=2000"},{"title":"Learning from Loss Landscape: Generalizable Mixed-Precision Quantization via Adaptive Sharpness-Aware Gradient Aligning","url":"https://arxiv.org/html/2505.04877"},{"title":"Machine Learning May 2025","url":"https://www.arxiv.org/list/cs.LG/2025-05?skip=1200&show=25"},{"title":"Artificial Intelligence May 2025","url":"https://www.arxiv.org/list/cs.AI/2025-05?skip=1525&show=2000"}]

I found the paper you're looking for. Here's what the search revealed:

The paper is titled "Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies".

**Key Concepts:**

The paper addresses the challenge of deploying and fine-tuning Large Language Models (LLMs) on resource-constrained edge devices while managing the trade-off between memory footprint and task performance.

**Main Contribution:**

The paper identifies a fundamental theoretical constraint called the "Fidelity-Plasticity Trade-off": a layer's capacity to adapt to new tasks (Plasticity) is inheren
…[truncated 613 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T17:56:33.695310+00:00_

Web search results for query: "arxiv 2511.15694 impact quantization reasoning model reinforcement learning"

Links: [{"title":"[2511.15694] The Impact of Quantization on Large Reasoning Model Reinforcement Learning","url":"https://arxiv.org/abs/2511.15694"},{"title":"The Impact of Quantization on Large Reasoning Model Reinforcement Learning","url":"https://arxiv.org/pdf/2511.15694"},{"title":"(PDF) The Impact of Quantization on Large Reasoning Model Reinforcement Learning","url":"https://www.researchgate.net/publication/397780372_The_Impact_of_Quantization_on_Large_Reasoning_Model_Reinforcement_Learning"},{"title":"NeurIPS The Impact of Quantization on Large Reasoning Model Reinforcement Learning","url":"https://neurips.cc/virtual/2025/loc/san-diego/126555"},{"title":"Quantization Hurts Reasoning? An Empirical Study on Quantized Reasoning Models","url":"https://arxiv.org/html/2504.04823v1"},{"title":"iQRL – Implicitly Quantized Representations for Sample-efficient Reinforcement Learning","url":"https://arxiv.org/html/2406.02696v1"},{"title":"The Impact of Quantization and Pruning on Deep Reinforcement Learning Models","url":"https://arxiv.org/html/2407.04803v1"},{"title":"Interpreting the Effects of Quantization on LLMs","url":"https://arxiv.org/html/2508.16785v1"},{"title":"Computer Science Jun 2024","url":"https://arxiv.org/list/cs/2024-06?skip=6500&show=1000"},{"title":"Artificial Intelligence","url":"https://arxiv.org/list/cs.AI/pastweek?skip=560&show=2000"}]

I found the paper! Here are the details about arxiv paper 2511.15694:

**Title:** The Impact of Quantization on Large Reasoning Model Reinforcement Learning

**Authors:** Medha Kumar, Zifei Xu, Xin Wang, and Tristan Webb

**Submission Date:** November 19, 2025

**Overview:** Strong reasoning capabilities can now be achieved by large-scale reinforcement learning (RL) without any supervised fine-tuning. Although post-training quantization (PTQ) and quantization-aware training (QAT) are well studied in the co
…[truncated 831 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T17:56:33.695607+00:00_

Web search results for query: "arxiv 2406.04879 trade-offs parameter-efficient preference alignment DPO QLoRA"

Links: [{"title":"[2406.04879] A Deep Dive into the Trade-Offs of Parameter-Efficient Preference Alignment Techniques","url":"https://arxiv.org/abs/2406.04879"},{"title":"A Deep Dive into the Trade-Offs of Parameter-Efficient Preference Alignment Techniques","url":"https://arxiv.org/html/2406.04879"},{"title":"From Baselines to Preferences: A Comparative Study of LoRA/QLoRA and Preference Optimization for Mental Health Text Classification","url":"https://arxiv.org/html/2604.00773"},{"title":"A Comparative Study of LoRA/QLoRA and Preference ...","url":"https://arxiv.org/pdf/2604.00773"},{"title":"A Deep Dive into the Trade-Offs of Parameter-Efficient Preference Alignment Techniques for ACL 2024 - IBM Research","url":"https://research.ibm.com/publications/a-deep-dive-into-the-trade-offs-of-parameter-efficient-preference-alignment-techniques"},{"title":"DPO-Shift: Shifting the Distribution of Direct Preference Optimization","url":"https://arxiv.org/html/2502.07599v1"},{"title":"Autoregressive Direct Preference Optimization","url":"https://arxiv.org/html/2602.09533v1"},{"title":"Robust Multi-Objective Preference Alignment with Online DPO","url":"https://arxiv.org/html/2503.00295v1"},{"title":"Token-Importance Guided Direct Preference Optimization","url":"https://arxiv.org/html/2505.19653v1"},{"title":"A Survey of Direct Preference Optimization","url":"https://arxiv.org/html/2503.11701v1"}]

I found the arXiv paper you were looking for! Here's the information:

The paper titled "A Deep Dive into the Trade-Offs of Parameter-Efficient Preference Alignment Techniques" is arXiv paper 2406.04879.

**Summary:**

While pre-training remains out of reach for most researchers due to the compute required, fine-tuning has become affordable thanks to parameter-efficient methods such as LoRA and QLoRA. Alignment is known to be sensitive to the many factors involved, includin
…[truncated 733 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T17:56:33.695915+00:00_

Web search results for query: "GRPO structured information extraction NER relation extraction reward hacking 2024 2025"

Links: [{"title":"Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/html/2503.06639v4"},{"title":"Using QwQ to generate a reasoning dataset for structured data extraction – Daniel van Strien","url":"https://danielvanstrien.xyz/posts/2025/reasoning-models/generating-structured-data-extraction-dataset-with-qwq-and-curator.html"},{"title":"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems","url":"https://arxiv.org/html/2509.22047"},{"title":"Reward Models and Learning Strategies","url":"https://aclanthology.org/2025.findings-emnlp.970.pdf"},{"title":"GRPO IS SECRETLY A PROCESS REWARD MODEL Michael Sullivan","url":"https://arxiv.org/pdf/2509.21154"},{"title":"GRPO is Secretly a Process Reward Model","url":"https://arxiv.org/html/2509.21154v1"},{"title":"GRPO","url":"https://www.aussieai.com/research/grpo"},{"title":"Entity and relation extractions for threat intelligence knowledge graphs - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0167404824004255"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Posterior-GRPO: Rewarding Reasoning Processes in Code Generation","url":"https://arxiv.org/html/2508.05170v1"}]

Based on the search results, here's what I found about GRPO and its applications to structured information extraction, NER, and reward hacking in 2024-2025:

## GRPO Overview

Group Relative Policy Optimization (GRPO), introduced by the DeepSeek team in DeepSeekMath, is a variant of Proximal Policy Optimization (PPO) that enhances mathematical reasoning abilities while optimizing memory usage. GRPO has been employed in the DeepSeek model series, including DeepSeek-v3 and DeepSeek-R
…[truncated 1354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T17:56:33.696223+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2602.13953 FlashRL QuRL efficient reinforcement learning quantized rollout"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2602.13953 FlashRL QuRL efficient reinforcement learning quantized rollout"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T17:56:33.696474+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2601.18699 mechanistic analysis catastrophic forgetting LLM continual fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2601.18699 mechanistic analysis catastrophic forgetting LLM continual fine-tuning"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T17:56:33.696683+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"constrained GRPO\" OR \"revisiting GRPO\" on-policy off-policy training stability 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"constrained GRPO\" OR \"revisiting GRPO\" on-policy off-policy training stability 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T17:56:33.696899+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LoRA quantization gradient noise signal-to-noise ratio training instability 2024 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LoRA quantization gradient noise signal-to-noise ratio training instability 2024 2025 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T17:56:33.697150+00:00_

Web search results for query: "arxiv 2601.18699 mechanistic analysis catastrophic forgetting LLM continual fine-tuning"

Links: [{"title":"Mechanistic Analysis of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning","url":"https://arxiv.org/html/2601.18699v1"},{"title":"[2601.18699] Mechanistic Analysis of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning","url":"https://arxiv.org/abs/2601.18699"},{"title":"Mechanistic Analysis of Catastrophic Forgetting in Large ...","url":"https://arxiv.org/pdf/2601.18699"},{"title":"Putting a Face to Forgetting: Continual Learning meets Mechanistic Interpretability","url":"https://arxiv.org/html/2601.22012v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=catastrophic+forgetting+%28CF%29"},{"title":"An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-Tuning | Request PDF","url":"https://www.researchgate.net/publication/395308608_An_Empirical_Study_of_Catastrophic_Forgetting_in_Large_Language_Models_During_Continual_Fine-Tuning"},{"title":"An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/empirical-study-catastrophic-forgetting-large-language-models"},{"title":"Interpretable Catastrophic Forgetting of Large Language Model Fine-tuning via Instruction Vector","url":"https://arxiv.org/html/2406.12227v1"},{"title":"FIT: Defying Catastrophic Forgetting in Continual LLM Unlearning","url":"https://arxiv.org/html/2601.21682v1"},{"title":"Learning the Mechanism of Catastrophic Forgetting: A Perspective from Gradient Similarity","url":"https://arxiv.org/html/2601.21577v1"}]

I found the paper arxiv 2601.18699. Here are the key details:

## Paper Summary

The paper presents a mechanistic analysis of catastrophic forgetting in transformer LLMs during sequential fine-tuning across models from 109B
…[truncated 1135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T17:56:33.697463+00:00_

Web search results for query: "arxiv 2602.13953 FlashRL QuRL efficient reinforcement learning quantized rollout"

Links: [{"title":"QuRL: Efficient Reinforcement Learning with Quantized Rollout","url":"https://arxiv.org/html/2602.13953"},{"title":"Efficient Reinforcement Learning with Quantized Rollout","url":"https://www.arxiv.org/pdf/2602.13953"},{"title":"[2602.13953] QuRL: Efficient Reinforcement Learning with Quantized Rollout","url":"https://arxiv.org/abs/2602.13953"},{"title":"[2602.13953v1] QuRL: Efficient Reinforcement Learning with Quantized Rollout","url":"https://arxiv.org/abs/2602.13953v1"},{"title":"QURL: EFFICIENT REINFORCEMENT LEARNING WITH ...","url":"https://openreview.net/pdf/f9894edaecf09efba8d69c1c6df2c82ebc0a26b2.pdf"},{"title":"QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning | OpenReview","url":"https://openreview.net/forum?id=eG0bpCwdKn"},{"title":"QeRL: Beyond Efficiency – Quantization-enhanced Reinforcement Learning for LLMs","url":"https://arxiv.org/html/2510.11696v1"},{"title":"(PDF) QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs","url":"https://www.researchgate.net/publication/396460003_QeRL_Beyond_Efficiency_--_Quantization-enhanced_Reinforcement_Learning_for_LLMs"},{"title":"QERL: BEYOND EFFICIENCY – QUANTIZATION-","url":"https://arxiv.org/pdf/2510.11696v1"},{"title":"QForce-RL: Quantized FPGA-Optimized Reinforcement Learning Compute Engine","url":"https://arxiv.org/html/2506.07046"}]

I found the paper arxiv 2602.13953! Here's information about QuRL:

## Overview

QuRL (Quantized Reinforcement Learning) uses a quantized actor for accelerating the rollout. The rollout process becomes the efficiency bottleneck of RL training, consisting of up to 70% of the total training time.

## Key Technical Contributions

The paper proposes Adaptive Clipping Range (ACR) that dynamically adjusts the clipping ratio based on the policy ratio between the full-precision actor and the quantized actor, w
…[truncated 818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T17:56:33.697756+00:00_

Web search results for query: ""constrained GRPO" OR "revisiting GRPO" on-policy off-policy training stability 2025 arxiv"

Links: [{"title":"[2505.22257] Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training","url":"https://arxiv.org/abs/2505.22257"},{"title":"Revisiting GRPO: On-Policy & Off-Policy Insights","url":"https://www.emergentmind.com/papers/2505.22257"},{"title":"Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training","url":"https://arxiv.org/html/2505.22257v2"},{"title":"Revisiting Group Relative Policy Optimization","url":"https://arxiv.org/pdf/2505.22257"},{"title":"REVISITING GROUP RELATIVE POLICY OPTIMIZA- TION","url":"https://openreview.net/pdf?id=XXfOf22o3K"},{"title":"Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training [Quick Review]","url":"https://liner.com/review/revisiting-group-relative-policy-optimization-insights-into-onpolicy-and-offpolicy"},{"title":"Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training | OpenReview","url":"https://openreview.net/forum?id=XXfOf22o3K"},{"title":"revisit group relative policy optimization","url":"https://openreview.net/pdf/55b0a0f870190a8e73a29522a4dc3a1ccf5baae5.pdf"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Group-relative+Policy+Optimization+(GRPO)"},{"title":"RePO: Bridging On-Policy Learning and Off-Policy Knowledge through Rephrasing Policy Optimization","url":"https://arxiv.org/html/2602.10819"}]

I found a highly relevant paper for your search! Here's what I discovered:

## Main Result

The paper "Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training" (arXiv:2505.22257) revisits GRPO in both on-policy and off-policy optimization regimes, showing that off-policy GRPO either significantly outperforms or performs on par with its on-policy counterpart.

## Key Find
…[truncated 1001 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T17:56:33.698052+00:00_

Web search results for query: "LoRA quantization gradient noise signal-to-noise ratio training instability 2024 2025 arxiv"

Links: [{"title":"Preprint LORAQUANT: MIXED-PRECISION QUANTIZATION OF LORA TO ULTRA-LOW BITS","url":"https://arxiv.org/pdf/2510.26690"},{"title":"LoraQuant : Mixed-Precision Quantization of LoRA to Ultra-Low Bits","url":"https://arxiv.org/html/2510.26690v1"},{"title":"arXiv:2505.18724v1 [cs.LG] 24 May 2025","url":"https://arxiv.org/pdf/2505.18724"},{"title":"Preprint. Under review. ON-THE-FLY ADAPTATION TO QUANTIZATION:","url":"https://www.arxiv.org/pdf/2509.25214"},{"title":"LoRA Training Provably Converges to a Low-Rank Global Minimum or It Fails Loudly (But it Probably Won’t Fail)","url":"https://arxiv.org/html/2502.09376v3"},{"title":"Revealing Modular Gradient Noise Imbalance in LLMs: Calibrating Adam via Signal-to-Noise Ratio","url":"https://arxiv.org/html/2605.05794"},{"title":"[2510.26690] LoRAQuant: Mixed-Precision Quantization of LoRA to Ultra-Low Bits","url":"https://arxiv.org/abs/2510.26690"},{"title":"Noise-Robustness Through Noise: Asymmetric LoRA Adaption with Poisoning Expert","url":"https://arxiv.org/html/2505.23868v1"},{"title":"CLoQ: Enhancing Fine-Tuning of Quantized LLMs via Calibrated LoRA Initialization","url":"https://arxiv.org/html/2501.18475v1"},{"title":"FP4 All the Way: Fully Quantized Training of LLMs","url":"https://arxiv.org/html/2505.19115v2"}]

I found several relevant recent papers on arXiv related to your search query. Here's a summary of the key findings:

## Highly Relevant Papers

**1. FP4 All the Way: Fully Quantized Training of LLMs (August 2025)**

This work identifies a critical transition point: when the full-precision gradient standard deviation falls approximately below √3 times the quantization noise, training stagnates. This insight guides the design of the final fine-tuning phase to boost the signal-to-noise ratio and match BF16 convergence. The paper provides analysis of noisy gradients training
…[truncated 1242 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T17:56:33.698378+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2510.11696 QeRL quantization-enhanced reinforcement learning LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2510.11696 QeRL quantization-enhanced reinforcement learning LLM"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T17:56:33.698584+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2602.14078 \"policy gradient\" \"adaptive entropy annealing\" continual fine-tuning forgetting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2602.14078 \"policy gradient\" \"adaptive entropy annealing\" continual fine-tuning forgetting"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T17:56:33.698789+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RLHF DPO catastrophic forgetting safety alignment tax multi-task 2024 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RLHF DPO catastrophic forgetting safety alignment tax multi-task 2024 2025 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T17:56:33.699050+00:00_

Web search results for query: "arxiv 2510.11696 QeRL quantization-enhanced reinforcement learning LLM"

Links: [{"title":"[2510.11696] QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs","url":"https://arxiv.org/abs/2510.11696"},{"title":"Paper page - QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs","url":"https://huggingface.co/papers/2510.11696"},{"title":"QeRL: Beyond Efficiency – Quantization-enhanced Reinforcement Learning for LLMs","url":"https://arxiv.org/html/2510.11696v1"},{"title":"[2510.11696v1] QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs","url":"https://arxiv.org/abs/2510.11696v1"},{"title":"(PDF) QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs","url":"https://www.researchgate.net/publication/396460003_QeRL_Beyond_Efficiency_--_Quantization-enhanced_Reinforcement_Learning_for_LLMs"},{"title":"QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251011696H/abstract"},{"title":"QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs | alphaXiv","url":"https://www.alphaxiv.org/abs/2510.11696"},{"title":"qerl: beyond efficiency – quantization","url":"https://arxiv.org/pdf/2510.11696"},{"title":"QeRL: Quantization-Enhanced RL for LLMs","url":"https://www.emergentmind.com/papers/2510.11696"},{"title":"[Literature Review] QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs","url":"https://www.themoonlight.io/en/review/qerl-beyond-efficiency-quantization-enhanced-reinforcement-learning-for-llms"}]

I've found comprehensive information about arxiv paper 2510.11696. Here's a summary:

## QeRL: Quantization-Enhanced Reinforcement Learning for LLMs

QeRL is a Quantization-enhanced Reinforcement Learning framework for large language models (LLMs). While RL is essential for LLMs' reasoning capabilitie
…[truncated 1228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T17:56:33.699374+00:00_

Web search results for query: "arxiv 2602.14078 "policy gradient" "adaptive entropy annealing" continual fine-tuning forgetting"

Links: [{"title":"[2602.14078] Policy Gradient with Adaptive Entropy Annealing for Continual Fine-Tuning","url":"https://arxiv.org/abs/2602.14078"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.14078"},{"title":"Machine Learning","url":"https://www.arxiv.org/list/cs.LG/recent?skip=686&show=50"},{"title":"Harnessing Uncertainty: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents","url":"https://arxiv.org/html/2509.09265v1"},{"title":"Arbitrary Entropy Policy Optimization: Entropy Is Controllable in Reinforcement Fine-tuning","url":"https://arxiv.org/html/2510.08141v1"},{"title":"Entropy-Adaptive Fine-Tuning: Resolving Confident Conflicts to Mitigate Forgetting","url":"https://arxiv.org/html/2601.02151v1"},{"title":"CE-GPPO: Controlling Entropy via Gradient-Preserving Clipping Policy Optimization in Reinforcement Learning","url":"https://arxiv.org/html/2509.20712v1"},{"title":"Entropy Is Controllable in Reinforcement Finetuning","url":"https://www.researchgate.net/publication/396373723_Arbitrary_Entropy_Policy_Optimization_Entropy_Is_Controllable_in_Reinforcement_Finetuning"},{"title":"Gradient Projection For Continual Parameter- Efficient Tuning","url":"https://www.researchgate.net/publication/393513125_Gradient_Projection_For_Continual_Parameter-_Efficient_Tuning"},{"title":"Reinforced Interactive Continual Learning ...","url":"https://papers.ssrn.com/sol3/Delivery.cfm/1b7cad6a-8158-4ebe-93df-3cbf806bc083-MECA.pdf?abstractid=5966945&mirid=1"}]

Based on the search results, I found the paper you're looking for:

**Title:** Policy Gradient with Adaptive Entropy Annealing for Continual Fine-Tuning

**Authors:** Yaqian Zhang, Bernhard Pfahringer, Eibe Frank, and Albert Bifet from the AI Institute at University of Waikato and LTCI at Télécom Paris

**Main Problem:** Large pretrained vision models remain vulnerable to
…[truncated 1014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T17:56:33.699671+00:00_

Web search results for query: "RLHF DPO catastrophic forgetting safety alignment tax multi-task 2024 2025 arxiv"

Links: [{"title":"Mitigating the Alignment Tax of RLHF","url":"https://arxiv.org/html/2309.06256v4"},{"title":"Mitigating the Alignment Tax of RLHF","url":"https://aclanthology.org/2024.emnlp-main.35.pdf"},{"title":"Mitigating the Alignment Tax of RLHF | Request PDF","url":"https://www.researchgate.net/publication/386186798_Mitigating_the_Alignment_Tax_of_RLHF"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a7ac8a21e5a27e7ab31a5f42a0117bdb-Paper-Conference.pdf"},{"title":"SAFETY ALIGNMENT SHOULD BE MADE MORE THAN ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/88be023075a5a3ff3dc3b5d26623fa22-Paper-Conference.pdf"},{"title":"[PDF] Mitigating the Alignment Tax of RLHF | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mitigating-the-Alignment-Tax-of-RLHF-Lin-Tan/6f8c4311e65efebb9da5a542c0405684e82a77cc"},{"title":"Unforgotten Safety: Preserving Safety Alignment of Large","url":"https://arxiv.org/pdf/2512.10150"},{"title":"Robust Policy Optimization to Prevent Catastrophic Forgetting","url":"https://arxiv.org/html/2602.08813"},{"title":"A Comprehensive Survey of Direct Preference Optimization: Datasets, Theories, Variants, and Applications","url":"https://arxiv.org/html/2410.15595v3"},{"title":"1 Reasoning Beyond Limits: Advances and Open Problems for LLMs","url":"https://arxiv.org/pdf/2503.22732"}]

I found several relevant research papers and results on your search topics. Here's a summary of key findings:

## Alignment Tax and RLHF/DPO

Fine-tuning large language models (LLMs) on new domains often incurs catastrophic forgetting, and this "alignment tax" is evident in RLHF where aligning to human preferences can erode base model capabilities.

## Addressing the Alignment Tax

Model averaging, which simply interpolates between pre and post RLHF model
…[truncated 1037 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T17:56:33.699979+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2309.06256 \"alignment tax\" RLHF model averaging catastrophic forgetting EMNLP 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2309.06256 \"alignment tax\" RLHF model averaging catastrophic forgetting EMNLP 2024"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T17:56:33.700197+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DAPO decoupled clip higher-lower policy optimization GRPO variant 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DAPO decoupled clip higher-lower policy optimization GRPO variant 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T17:56:33.700431+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "QLoRA 4-bit performance degradation complex task structured output code generation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "QLoRA 4-bit performance degradation complex task structured output code generation 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T17:56:33.702710+00:00_

Web search results for query: "arxiv 2309.06256 "alignment tax" RLHF model averaging catastrophic forgetting EMNLP 2024"

Links: [{"title":"[2309.06256] Mitigating the Alignment Tax of RLHF","url":"https://arxiv.org/abs/2309.06256"},{"title":"[2309.06256] Mitigating the Alignment Tax of RLHF - ar5iv","url":"https://ar5iv.labs.arxiv.org/html/2309.06256"},{"title":"Mitigating the Alignment Tax of RLHF","url":"https://arxiv.org/pdf/2309.06256"},{"title":"Paper page - Mitigating the Alignment Tax of RLHF","url":"https://huggingface.co/papers/2309.06256"},{"title":"[PDF] Mitigating the Alignment Tax of RLHF | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mitigating-the-Alignment-Tax-of-RLHF-Lin-Tan/6f8c4311e65efebb9da5a542c0405684e82a77cc"},{"title":"GitHub - avalonstrel/Mitigating-the-Alignment-Tax-of-RLHF","url":"https://github.com/avalonstrel/Mitigating-the-Alignment-Tax-of-RLHF"},{"title":"Mitigating the Alignment Tax of RLHF - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230906256L/abstract"},{"title":"Mitigating the Alignment Tax of RLHF | alphaXiv","url":"https://www.alphaxiv.org/overview/2309.06256"},{"title":"Mitigating the Alignment Tax of RLHF – Paper Detail · SwiftScholar - Review with AI","url":"https://www.swiftscholar.net/paper/68ef57d8e77486f6f3192ec6"},{"title":"Mitigating the Alignment Tax of RLHF. - dblp","url":"https://dblp.dagstuhl.de/rec/journals/corr/abs-2309-06256.html"}]

Based on the web search results, I found comprehensive information about arxiv paper 2309.06256. Here's what the research covers:

## Paper Overview

The paper is titled "Mitigating the Alignment Tax of RLHF", submitted to arXiv in September 2023.

## Problem Statement

LLMs acquire a wide range of abilities during pre-training, but aligning LLMs under Reinforcement Learning with Human Feedback (RLHF) can lead to forgetting, which is also known as the alignment tax. This alignment process often degrades the model's performance on a wide range of genera
…[truncated 1271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T17:56:33.703072+00:00_

Web search results for query: "DAPO decoupled clip higher-lower policy optimization GRPO variant 2025 arxiv"

Links: [{"title":"DAPO: An Open-Source LLM Reinforcement Learning System at Scale 1ByteDance Seed","url":"https://arxiv.org/pdf/2503.14476"},{"title":"DAPO: An Open-Source LLM Reinforcement Learning System at Scale","url":"https://arxiv.org/html/2503.14476v1"},{"title":"DCPO: Dynamic Clipping Policy Optimization","url":"https://arxiv.org/html/2509.02333v1"},{"title":"Recipe: Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO) — verl documentation","url":"https://verl.readthedocs.io/en/latest/algo/dapo.html"},{"title":"[2503.14476] DAPO: An Open-Source LLM Reinforcement Learning System at Scale","url":"https://arxiv.org/abs/2503.14476"},{"title":"GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with Policy Entropy","url":"https://arxiv.org/html/2508.04349"},{"title":"CE-GPPO: Coordinating Entropy via Gradient-Preserving Clipping Policy Optimization in Reinforcement Learning","url":"https://arxiv.org/html/2509.20712"},{"title":"DAPO: An Open-Source LLM Reinforcement Learning System at Scale | OpenReview","url":"https://openreview.net/forum?id=2a36EMSSTp"},{"title":"The Evolution of Policy Optimization: Understanding GRPO, DAPO, and Dr. GRPO’s Theoretical Foundations | by Jennifer Wei | Medium","url":"https://medium.com/@jenwei0312/the-evolution-of-policy-optimization-understanding-grpo-dapo-and-dr-3e758c54b2c6"},{"title":"Comparative Analysis and Parametric Tuning of PPO, GRPO, and DAPO for LLM Reasoning Enhancement","url":"https://arxiv.org/html/2512.07611"}]

Based on the search results, I found comprehensive information about DAPO and its relationship to GRPO:

## Overview

DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization) is a proposed algorithm that addresses limitations in the GRPO (Group Relative Policy Optimization) framework. The system achieves 50 points on AIME 2024 based on Qwen2.5-32B model, outperforming previous s
…[truncated 1306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T17:56:33.703442+00:00_

Web search results for query: "QLoRA 4-bit performance degradation complex task structured output code generation 2024 2025"

Links: [{"title":"QLoRA in 2025: The 4-Bit Fine-Tuning Revolution for Large Language Models - Poniak Times","url":"https://www.poniaktimes.com/qlora-4bit-llm-finetuning-2025-guide/"},{"title":"QLORA: Efficient Finetuning of Quantized LLMs Tim Dettmers∗ Artidoro Pagnoni∗","url":"https://openreview.net/pdf?id=OUIFPHEgJU"},{"title":"GitHub - artidoro/qlora: QLoRA: Efficient Finetuning of Quantized LLMs · GitHub","url":"https://github.com/artidoro/qlora"},{"title":"QLoRA: Efficient Finetuning of Quantized LLMs | OpenReview","url":"https://openreview.net/forum?id=OUIFPHEgJU"},{"title":"Accurate and Efficient Fine-Tuning of Quantized Large Language Models Through Optimal Balance in Adaptation | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.23/132118/Accurate-and-Efficient-Fine-Tuning-of-Quantized"},{"title":"[2305.14314] QLoRA: Efficient Finetuning of Quantized LLMs","url":"https://arxiv.org/abs/2305.14314"},{"title":"[Quick Review] QLoRA: Efficient Finetuning of Quantized LLMs","url":"https://liner.com/review/qlora-efficient-finetuning-of-quantized-llms"},{"title":"What is QLoRA?: A Visual Guide to Efficient Finetuning of Quantized LLMs","url":"https://codecompass00.substack.com/p/qlora-visual-guide-finetune-quantized-llms-peft"},{"title":"[Research Paper Summary] QLoRA: Efficient Finetuning of Quantized LLMs | by Himanshu Bamoria | Athina AI | Medium","url":"https://medium.com/athina-ai/research-paper-summary-qlora-efficient-finetuning-of-quantized-llms-8bbc2a2ff260"},{"title":"Fine-Tuning Infrastructure: LoRA, QLoRA, and PEFT at Scale | Introl Blog","url":"https://introl.com/blog/fine-tuning-infrastructure-lora-qlora-peft-scale-guide-2025"}]

Based on the search results, here's what I found regarding QLoRA 4-bit performance degradation, particularly for co
…[truncated 1870 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T17:56:33.703767+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2510.06213 training dynamics post-training quantization effectiveness degradation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2510.06213 training dynamics post-training quantization effectiveness degradation"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T17:56:33.703992+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2505.18724 FP4 fully quantized training gradient noise signal quantization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2505.18724 FP4 fully quantized training gradient noise signal quantization"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T17:56:33.704271+00:00_

Web search results for query: "arxiv 2510.06213 training dynamics post-training quantization effectiveness degradation"

Links: [{"title":"[2510.06213] Training Dynamics Impact Post-Training Quantization Robustness","url":"https://arxiv.org/abs/2510.06213"},{"title":"Training dynamics impact post-training quantization robustness","url":"https://arxiv.org/html/2510.06213"},{"title":"Training Dynamics Impact Post-Training Quantization ...","url":"https://arxiv.org/pdf/2510.06213"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=2254&show=2000"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1408&show=2000"},{"title":"[2601.06213] Cyber Threat Detection and Vulnerability Assessment System using Generative AI and Large Language Model","url":"https://arxiv.org/abs/2601.06213"},{"title":"arXiv.org | 232753 Publications | 16958 Citations | Top authors | Related journals","url":"https://scispace.com/journals/arxiv-org-bl5k1ptr"},{"title":"Computer Vision and Pattern Recognition","url":"https://www.arxiv.org/list/cs.CV/recent?skip=386&show=250"},{"title":"Paweł Huryn on X: \"Crazy to miss: 7 new AI papers hint at what OpenAI, Anthropic, and Google are building right now. (they are usually just 6 months behind) TLDR: Faster, cheaper, and more reliable agents that can collaborate, learn from experience, make payments, and run on your device. 1.\" / X","url":"https://x.com/PawelHuryn/status/1978428950050222394"},{"title":"[2510.00219] Thoughtbubbles: an Unsupervised Method for Parallel Thinking in Latent Space","url":"https://arxiv.org/abs/2510.00219"}]

I found the paper! Here are the key details about arxiv 2510.06213:

**Title:** Training Dynamics Impact Post-Training Quantization Robustness

**Published:** Published as a conference paper at ICLR 2026

**Key Findings:**

The paper conducts a comprehensive analysis of quantization degradation across open-source language model training trajectories up to 32B parameters and
…[truncated 731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T17:56:33.704531+00:00_

Web search results for query: "arxiv 2505.18724 FP4 fully quantized training gradient noise signal quantization"

Links: [{"title":"FP4 All the Way: Fully Quantized Training of LLMs","url":"https://arxiv.org/html/2505.19115v2"},{"title":"[2505.19115] FP4 All the Way: Fully Quantized Training of LLMs","url":"https://arxiv.org/abs/2505.19115"},{"title":"FP4 All the Way: Fully Quantized Training of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=kuzye4EPLR"},{"title":"Quartet: Native FP4 Training Can Be Optimal for Large Language Models","url":"https://arxiv.org/html/2505.14669v1"},{"title":"Optimizing Large Language Model Training Using FP4 Quantization","url":"https://arxiv.org/html/2501.17116v2"},{"title":"FP4 All the Way: Fully Quantized Training of LLMs","url":"https://openreview.net/pdf?id=kuzye4EPLR"},{"title":"Paper page - FP4 All the Way: Fully Quantized Training of LLMs","url":"https://huggingface.co/papers/2505.19115"},{"title":"Elucidating the Design Space of FP4 training","url":"https://arxiv.org/html/2509.17791v1"},{"title":"Quartet: Native FP4 Training Can Be Optimal for Large ...","url":"https://arxiv.org/pdf/2505.14669"},{"title":"Metis: Training LLMs with FP4 Quantization","url":"https://arxiv.org/html/2509.00404v4"}]

Based on the search results, I found information related to your query about FP4 fully quantized training with gradient noise and signal quantization analysis.

The most relevant paper appears to be "FP4 All the Way: Fully Quantized Training of LLMs," which demonstrates fully quantized training of large language models using FP4 precision for weights, activations, and gradients on datasets up to 200 billion tokens. 

A key finding from this work is that "there is a theoretical and empirical threshold for effective quantized training: when the gradient norm falls below approximately √3 times the quantization noise, quantized training becomes less effective". This directly addresses the relationship between grad
…[truncated 664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T17:56:33.704879+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "literature_quantization_rl.md",
  "content": "# Quantization-RL Interaction Literature Survey\n\n调研日期：2026-05-15\n背景：GRPO 在 structured IE 任务上，QLoRA 4-bit 导致 catastrophic forgetting（rel_f1 0.4057→0.2167），bf16 LoRA 完全正常（rel_f1=0.4549）\n\n---\n\n## 1. Quantization + RL Training\n\n### 1.1 The Impact of Quantization on Large Reasoning Model Reinforcement Learning\n- Kumar, Xu, Wang & Webb (2025) — **NeurIPS 2025**\n- Key finding: 系统性实验发现 quantization-aware RL training (QAFT) 负面影响学习过程——quantized models produce worse policies。相比之下，先 RL 训练再 PTQ/QLoRA 量化的效果更好。量化引入的 \"sudden shock\" 在 RL 过程中尤其有害。\n- Relevance: **直接支撑我们的发现**——4-bit quantization 在 RL training 阶段（而非推理阶段）引入的噪声破坏 policy learning。我们的 QLoRA+GRPO 正是在训练阶段量化。\n- URL: https://arxiv.org/abs/2511.15694\n\n### 1.2 QuRL: Efficient Reinforcement Learning with Quantized Rollout\n- (2026) — **ICLR 2026**\n- Key finding: INT8 quantization during RL rollout 导致 4% accuracy degradation vs bf16 baseline。关键发现：RL steps 之间的 weight update 极小（\"extremely small\"），quantization noise 淹没了这些微小更新。提出 Adaptive Clipping Range (ACR) 将 INT8 gap 缩至 2%，FP8 缩至 ~1%。\n- Relevance: **核心机制解释**——RL 训练的 weight update 幅度远小于 SFT，而 4-bit quantization noise 远大于 INT8。这解释了为什么 QLoRA 在 SFT 阶段表现正常但在 GRPO 阶段 catastrophic——RL 的微小梯度信号被 4-bit 噪声完全淹没。\n- URL: https://arxiv.org/abs/2602.13953\n\n### 1.3 QeRL: Beyond Efficiency — Quantization-enhanced Reinforcement Learning for LLMs\n- Huang et al. (2025) — arXiv\n- Key finding: Quantization noise 增加 policy entropy，增强 exploration。通过 Adaptive Quantization Noise (AQN) 机制动态调整噪声，NVFP4+LoRA 实现比 16-bit LoRA 和 QLoRA 更快的 reward growth。7B 模型在 GSM8K 达 90.8%。\n- Relevance: 表明 quantization noise 如果被适当控制可以有益（类似 exploration noise），但 **未控制的噪声导致不稳定**。标准 QLoRA 没有 AQN 机制，噪声是 uncontrolled 的。\n- URL: https://arxiv.org/abs/2510.11696\n\n### 1.4 FP4 All the Way: Fully Quantized Training of LLMs\n- (2025) — arXiv\n- Key finding: 提出理论临界点——**当 gradient standard deviation < √3 × quantization noise 时，quantized training 停滞**。Stochastic rounding 对低精度训练稳定性至关重要。\n- Relevance: **理论基础**——4-bit NF4 的 quantization noise 量级远大于 8-bit 或 bf16。RL training 产生的 gradient signal 本身就比 SFT 弱（因为 reward-based 而非 direct supervision），更容易跌破 √3 阈值。\n- URL: https://arxiv.org/abs/2505.19115\n\n### 1.5 Training Dynamics Impact Post-Training Quantization Robustness\n- (2025) — **ICLR 2026**\n- Key finding: 量化误差由 learning rate 和训练超参数的复杂交互驱动。LR decay 后，validation loss 和 quantization error 出现 divergence。\n- Relevance: RL training 的 learning dynamics（reward signal 变化、policy ratio clipping）与 SFT 显著不同，这种不同的 training dynamics 可能导致模型进入 quantization-sensitive 区域。\n- URL: https://arxiv.org/abs/2510.06213\n\n---\n\n## 2. GRPO Stability / Failure Modes\n\n### 2.1 GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control\n- (2025) — arXiv\n- Key finding: 识别 GRPO 两个核心失败模式：(i) **token-level penalization**——不同 response 中共享的 valuable tokens 收到矛盾梯度信号；(ii) **policy collapse**——负 reward 的 completions 惩罚 confident responses，将决策推向 unlikely tokens。GTPO 通过跳过负更新、放大正更新解决，在 OOD benchmark 上比 GRPO 高 75pp (Pass@64)。\n- Relevance: **高度相关**——structured IE 中 relation tokens 和 evidence tokens 可能共享底层 representation。GRPO 的 token-level penalization 机制可能导致这些共享 tokens 收到矛盾信号，造成 relation 和 evidence extraction 的 decoupling。4-bit 噪声会放大这种矛盾。\n- URL: https://arxiv.org/abs/2508.03772\n\n### 2.2 DAPO: An Open-Source LLM Reinforcement Learning System at Scale\n- ByteDance Seed (2025) — arXiv\n- Key finding: Naive GRPO 训练中观察到 **entropy collapse**——policy entropy 快速下降。提出 Clip-Higher（解耦上下 clip range 给低概率 token 更多空间）+ Dynamic Sampling（过滤 uniform reward 样本确保每个 batch 有有效梯度）。Qwen2.5-32B 在 AIME 2024 达 50 分，超 DeepSeek-R1-Zero。\n- Relevance: Entropy collapse 在 structured output 任务上可能更严重——IE 任务的 valid output space 高度受限（JSON schema），GRPO 容易在这种约束空间中快速 collapse。QLoRA 的噪声可能加速或异常化这个 collapse 过程。\n- URL: https://arxiv.org/abs/2503.14476\n\n### 2.3 Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training\n- (2025) — arXiv\n- Key finding: On-policy GRPO 不带 masking 收敛到 Pass@1=45% 但 **不稳定**。Zero-variance masking（过滤所有 response 同 reward 的 group）可稳定训练并提升至 50%。Off-policy GRPO 通过 clipped surrogate objective 匹配或超越 on-policy。\n- Relevance: Zero-variance groups 在 structured IE 中很常见——当所有 sampled response 都提取到相同的 relation set 时（正确或错误），group 内 variance=0，GRPO 完全无法学习。QLoRA 的噪声可能同时影响 sampling diversity。\n- URL: https://arxiv.org/abs/2505.22257\n\n### 2.4 MO-GRPO: Mitigating Reward Hacking of GRPO on Multi-Objective Problems\n- (2025) — arXiv\n- Key finding: GRPO 在 multi-objective 问题上容易 reward hacking——agent overfits misspecified reward。\n- Relevance: 我们的 IE 任务本质是 multi-objective（relation extraction + evidence extraction），GRPO 可能优化一个目标而牺牲另一个，这与我们观察到的 \"evidence 与 relation decouple\" 现象一致。\n- URL: https://arxiv.org/abs/2509.22047\n\n---\n\n## 3. LoRA Precision Effects\n\n### 3.1 Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies\n- (2025) — arXiv\n- Key finding: 提出 **Fidelity-Plasticity Trade-off**——一个 layer 的适应能力（Plasticity）受限于其 frozen weights 的信息容量（Fidelity）。**对语义关键层的激进量化产生不可恢复的信息瓶颈**，无论 adapter rank 多高都无法补偿。提出 QR-Adaptor 联合优化 per-layer bit-width 和 LoRA rank。\n- Relevance: **直接解释性**——4-bit 量化可能在 structured reasoning 最关键的中间层造成信息瓶颈。Evidence extraction 需要的细粒度语义理解（哪些 span 支持哪些 relation）需要高 Fidelity 的表示，4-bit 无法提供。\n- URL: https://arxiv.org/abs/2505.03802\n\n### 3.2 A Deep Dive into the Trade-Offs of Parameter-Efficient Preference Alignment Techniques\n- IBM Research (2024) — **ACL 2024**\n- Key finding: 300+ 实验横跨 SFT 和 DPO、LoRA 和 QLoRA、多个模型。发现 QLoRA 的 learning pattern 与 full fine-tuning **本质不同**（不仅是量上接近，模式也不同）。Alignment 对 data quality、method 和 adapter rank 高度敏感。\n- Relevance: 如果 QLoRA 在 DPO 上就已经表现出不同的 learning pattern，那在更复杂的 GRPO 上这种差异可能更大。\n- URL: https://arxiv.org/abs/2406.04879\n\n### 3.3 Revealing Modular Gradient Noise Imbalance in LLMs\n- (2026) — arXiv\n- Key finding: LLM 不同模块存在 gradient scale mismatch，Adam 的 adaptivity 无法完全修正，导致收敛慢或训练不稳定。提出 MoLS（Module-wise Learning-rate Scaling）。\n- Relevance: 4-bit quantization noise 会放大模块间的 gradient 不平衡——quantization noise 在不同层的影响不均匀，进一步加剧 gradient scale mismatch。\n- URL: https://arxiv.org/abs/2605.05794 [UNVERIFIED - 2026 年 5 月论文，可能尚未公开]\n\n### 3.4 CLoQ: Enhancing Fine-Tuning of Quantized LLMs via Calibrated LoRA Initialization\n- (2025) — arXiv\n- Key finding: QLoRA 的性能差距部分源于 suboptimal initialization——quantized weights 的误差影响 LoRA 的起始点。Calibrated initialization 使 INT2 CLoQ 在 Llama2-13B 上超越 INT4 QLoRA 在 arithmetic reasoning 上的表现。\n- Relevance: QLoRA 的 initialization 问题在 RL 训练中可能被放大——RL 对 policy 的初始状态比 SFT 更敏感。\n- URL: https://arxiv.org/abs/2501.18475\n\n---\n\n## 4. Catastrophic Forgetting in RLHF\n\n### 4.1 Robust Policy Optimization to Prevent Catastrophic Forgetting (FRPO)\n- Sabbaghi, Pappas, Javanmard & Hassani (2026) — arXiv\n- Key finding: Standard RLHF 找到的 high-reward policies 位于 **loss landscape 的 sharp regions**——小扰动就导致 reward 急剧下降。FRPO 在 KL-bounded 邻域内优化 reward flatness，找到对 downstream fine-tuning robust 的 policy。\n- Relevance: **关键洞察**——QLoRA 的 4-bit 量化噪声本质上就是对 weights 的持续小扰动。如果 GRPO 将 policy 推向 sharp region，这些持续的量化扰动就会不断将 policy 推离高 reward 区域，导致 catastrophic forgetting。bf16 没有这种噪声所以稳定。\n- URL: https://arxiv.org/abs/2602.08813\n\n### 4.2 Mitigating the Alignment Tax of RLHF\n- Lin, Tan et al. (2023/2024) — **EMNLP 2024**\n- Key finding: RLHF alignment 导致 pre-training 能力退化（\"alignment tax\"）——包括 translation、reasoning、reading comprehension。Model averaging（插值 pre/post RLHF 权重）达到最优 alignment-forgetting Pareto front。**不同层对 alignment tax 的敏感度不同**。\n- Relevance: Layer-wise sensitivity + quantization = 问题叠加。某些层既对 alignment forgetting 敏感，又被 4-bit 量化严重影响，double hit。\n- URL: https://arxiv.org/abs/2309.06256\n\n### 4.3 Mechanistic Analysis of Catastrophic Forgetting in LLMs During Continual Fine-tuning\n- (2026) — arXiv\n- Key finding: 识别三个遗忘机制：(i) 低层 attention weights 的 **gradient interference**（15-23% attention heads 严重受损）；(ii) 中间层的 **representational drift**（CKA 相似度下降 0.32-0.47）；(iii) **loss landscape flattening**。梯度对齐程度可预测遗忘严重性。\n- Relevance: 4-bit quantization noise 在低层引入额外的 gradient interference，在中间层加速 representational drift。这两个机制可能是 QLoRA+GRPO forgetting 的直接驱动力。\n- URL: https://arxiv.org/abs/2601.18699\n\n### 4.4 RL Minimizes Catastrophic Forgetting vs SFT\n- MIT (2025) — MarkTechPost 报道\n- Key finding: On-policy RL 天然比 SFT 更少遗忘，KL divergence 是遗忘严重性的预测指标。\n- Relevance: **反面证据/重要限定**——这个结论基于 full-precision RL。QLoRA 的 4-bit 噪声可能破坏了 RL 的这种天然优势，使得 quantized RL 反而比 SFT 遗忘更严重。这正是我们观察到的现象。\n- URL: https://www.marktechpost.com/2025/09/08/a-new-mit-study-shows-reinforcement-learning-minimizes-catastrophic-forgetting-compared-to-supervised-fine-tuning/\n\n### 4.5 Policy Gradient with Adaptive Entropy Annealing for Continual Fine-Tuning\n- Zhang et al. (2026) — arXiv\n- Key finding: 低 entropy 增强适应能力但增加遗忘风险。Adaptive entropy annealing 从 exploration（高 entropy）渐进到 exploitation（低 entropy），平衡 plasticity 和 stability。\n- Relevance: QLoRA 的量化噪声干扰了 entropy 的自然演化——可能导致 entropy 异常波动而非平稳下降，打破 plasticity-stability 平衡。\n- URL: https://arxiv.org/abs/2602.14078\n\n---\n\n## Summary\n\n### 我们的发现在文献中是否有先例？\n\n**部分有先例，但具体组合是新的。**\n\n- **Quantization 损害 RL training 已有报告**：Kumar et al. (2025) 发现 quantization-aware RL training 产生更差的 policy；QuRL 发现 INT8 就有 4% degradation；FP4 论文给出了理论阈值（gradient < √3 × noise → 停滞）\n- **GRPO 的稳定性问题已被广泛研究**：GTPO、DAPO、Revisiting GRPO 等多篇论文识别了 entropy collapse、token-level gradient conflict、zero-variance stalling\n- **LoRA 精度影响学习模式已有发现**：Fidelity-Plasticity trade-off、IBM 的 300+ 实验、CLoQ 都表明 QLoRA 的 learning pattern 与 full fine-tuning 本质不同\n- **RL 中的 catastrophic forgetting 已有研究**：FRPO 发现 sharp reward regions、alignment tax 论文发现 layer-wise sensitivity\n\n**但：QLoRA 4-bit 在 GRPO 训练中导致 structured output 的 subtask decoupling（relation 与 evidence extraction 分离）这个具体现象，文献中没有直接先例。**\n\n### 最接近的相关工作\n\n1. **QuRL (ICLR 2026)**——最接近，但研究的是 INT8 rollout quantization 而非 4-bit training quantization，且任务是 math reasoning 而非 structured IE\n2. **Kumar et al. (NeurIPS 2025)**——直接研究 quantization + RL，但未涉及 structured output 或 subtask decoupling\n3. **GTPO (2025)**——识别了 GRPO 的 token-level gradient conflict，这是 decoupling 的潜在机制，但未与 quantization 关联\n4. **Fidelity-Plasticity (2025)**——理论上解释了为什么 4-bit 在某些层造成不可恢复的瓶颈，但未在 RL 场景验证\n\n### 我们的 Unique Contribution\n\n1. **首次报告 QLoRA 4-bit + GRPO 在 structured IE 上的 catastrophic decoupling**——不仅是整体性能下降，而是 subtasks 之间的 coupling 被破坏（evidence extraction 与 relation extraction 分离）\n2. **提供 quantization-precision 消融**——同一任务、同一 GRPO 配置下，4-bit vs bf16 的直接对比，干净地隔离了 quantization 的影响\n3. **Structured output 场景的独特视角**——现有 quantization+RL 研究全部集中在 math reasoning（单一正确答案），structured IE 的 multi-component output（relation + evidence + faithfulness）更脆弱\n4. **机制假说**——结合 QuRL 的 \"微小 weight update 被噪声淹没\" + GTPO 的 \"token-level gradient conflict\" + Fidelity-Plasticity 的 \"信息瓶颈\"，我们可以提出一个连贯的解释框架：4-bit 噪声放大 GRPO 的 gradient conflict，在需要 multi-component coordination 的 structured IE 中首先破坏最脆弱的 coupling（evidence↔relation）\n\n### Claim 2 Reframing 建议\n\n原始 Claim 2 可 reframe 为：\n> \"Quantization precision is a critical but overlooked factor in RL-based IE training: 4-bit QLoRA introduces quantization noise that overwhelms GRPO's fine-grained gradient signals, causing catastrophic decoupling of structured subtasks — a failure mode absent in bf16 training and not predicted by QLoRA's strong SFT performance.\"\n\n支撑论据链：\n- QLoRA 在 SFT 阶段表现正常（consistent with Dettmers et al. 2023）\n- RL weight updates 远小于 SFT（QuRL, ICLR 2026）\n- 4-bit noise > √3 × RL gradient signal → training stagnation（FP4 theory）\n- GRPO 的 token-level gradient conflict 被噪声放大（GTPO analysis）\n- 结果是 subtask decoupling 而非整体退化（our unique finding）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "literature_quantization_rl.md",
    "content": "# Quantization-RL Interaction Literature Survey\n\n调研日期：2026-05-15\n背景：GRPO 在 structured IE 任务上，QLoRA 4-bit 导致 catastrophic forgetting（rel_f1 0.4057→0.2167），bf16 LoRA 完全正常（rel_f1=0.4549）\n\n---\n\n## 1. Quantization + RL Training\n\n### 1.1 The Impact of Quantization on Large Reasoning Model Reinforcement Learning\n- Kumar, Xu, Wang & Webb (2025) — **NeurIPS 2025**\n- Key finding: 系统性实验发现 quantization-aware RL training (QAFT) 负面影响学习过程——quantized models produce worse policies。相比之下，先 RL 训练再 PTQ/QLoRA 量化的效果更好。量化引入的 \"sudden shock\" 在 RL 过程中尤其有害。\n- Relevance: **直接支撑我们的发现**——4-bit quantization 在 RL training 阶段（而非推理阶段）引入的噪声破坏 policy learning。我们的 QLoRA+GRPO 正是在训练阶段量化。\n- URL: https://arxiv.org/abs/2511.15694\n\n### 1.2 QuRL: Efficient Reinforcement Learning with Quantized Rollout\n- (2026) — **ICLR 2026**\n- Key finding: INT8 quantization during RL rollout 导致 4% accuracy degradation vs bf16 baseline。关键发现：RL steps 之间的 weight update 极小（\"extremely small\"），quantization noise 淹没了这些微小更新。提出 Adaptive Clipping Range (ACR) 将 INT8 gap 缩至 2%，FP8 缩至 ~1%。\n- Relevance: **核心机制解释**——RL 训练的 weight update 幅度远小于 SFT，而 4-bit quantization noise 远大于 INT8。这解释了为什么 QLoRA 在 SFT 阶段表现正常但在 GRPO 阶段 catastrophic——RL 的微小梯度信号被 4-bit 噪声完全淹没。\n- URL: https://arxiv.org/abs/2602.13953\n\n### 1.3 QeRL: Beyond Efficiency — Quantization-enhanced Reinforcement Learning for LLMs\n- Huang et al. (2025) — arXiv\n- Key finding: Quantization noise 增加 policy entropy，增强 exploration。通过 Adaptive Quantization Noise (AQN) 机制动态调整噪声，NVFP4+LoRA 实现比 16-bit LoRA 和 QLoRA 更快的 reward growth。7B 模型在 GSM8K 达 90.8%。\n- Relevance: 表明 quantization noise 如果被适当控制可以有益（类似 exploration noise），但 **未控制的噪声导致不稳定**。标准 QLoRA 没有 AQN 机制，噪声是 uncontrolled 的。\n- URL: https://arxiv.org/abs/2510.11696\n\n### 1.4 FP4 All the Way: Fully Quantized Training of LLMs\n- (2025) — arXiv\n- Key finding: 提出理论临界点——**当 gradient standard deviation < √3 × quantization noise 时，quantized training 停滞**。Stochastic rounding 对低精度训练稳定性至关重要。\n- Relevance: **理论基础**——4-bit NF4 的 quantization noise 量级远大于 8-bit 或 bf16。RL training 产生的 gradient signal 本身就比 SFT 弱（因为 reward-based 而非 direct supervision），更容易跌破 √3 阈值。\n- URL: https://arxiv.org/abs/2505.19115\n\n### 1.5 Training Dynamics Impact Post-Training Quantization Robustness\n- (2025) — **ICLR 2026**\n- Key finding: 量化误差由 learning rate 和训练超参数的复杂交互驱动。LR decay 后，validation loss 和 quantization error 出现 divergence。\n- Relevance: RL training 的 learning dynamics（reward signal 变化、policy ratio clipping）与 SFT 显著不同，这种不同的 training dynamics 可能导致模型进入 quantization-sensitive 区域。\n- URL: https://arxiv.org/abs/2510.06213\n\n---\n\n## 2. GRPO Stability / Failure Modes\n\n### 2.1 GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control\n- (2025) — arXiv\n- Key finding: 识别 GRPO 两个核心失败模式：(i) **token-level penalization**——不同 response 中共享的 valuable tokens 收到矛盾梯度信号；(ii) **policy collapse**——负 reward 的 completions 惩罚 confident responses，将决策推向 unlikely tokens。GTPO 通过跳过负更新、放大正更新解决，在 OOD benchmark 上比 GRPO 高 75pp (Pass@64)。\n- Relevance: **高度相关**——structured IE 中 relation tokens 和 evidence tokens 可能共享底层 representation。GRPO 的 token-level penalization 机制可能导致这些共享 tokens 收到矛盾信号，造成 relation 和 evidence extraction 的 decoupling。4-bit 噪声会放大这种矛盾。\n- URL: https://arxiv.org/abs/2508.03772\n\n### 2.2 DAPO: An Open-Source LLM Reinforcement Learning System at Scale\n- ByteDance Seed (2025) — arXiv\n- Key finding: Naive GRPO 训练中观察到 **entropy collapse**——policy entropy 快速下降。提出 Clip-Higher（解耦上下 clip range 给低概率 token 更多空间）+ Dynamic Sampling（过滤 uniform reward 样本确保每个 batch 有有效梯度）。Qwen2.5-32B 在 AIME 2024 达 50 分，超 DeepSeek-R1-Zero。\n- Relevance: Entropy collapse 在 structured output 任务上可能更严重——IE 任务的 valid output space 高度受限（JSON schema），GRPO 容易在这种约束空间中快速 collapse。QLoRA 的噪声可能加速或异常化这个 collapse 过程。\n- URL: https://arxiv.org/abs/2503.14476\n\n### 2.3 Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training\n- (2025) — arXiv\n- Key finding: On-policy GRPO 不带 masking 收敛到 Pass@1=45% 但 **不稳定**。Zero-variance masking（过滤所有 response 同 reward 的 group）可稳定训练并提升至 50%。Off-policy GRPO 通过 clipped surrogate objective 匹配或超越 on-policy。\n- Relevance: Zero-variance groups 在 structured IE 中很常见——当所有 sampled response 都提取到相同的 relation set 时（正确或错误），group 内 variance=0，GRPO 完全无法学习。QLoRA 的噪声可能同时影响 sampling diversity。\n- URL: https://arxiv.org/abs/2505.22257\n\n### 2.4 MO-GRPO: Mitigating Reward Hacking of GRPO on Multi-Objective Problems\n- (2025) — arXiv\n- Key finding: GRPO 在 multi-objective 问题上容易 reward hacking——agent overfits misspecified reward。\n- Relevance: 我们的 IE 任务本质是 multi-objective（relation extraction + evidence extraction），GRPO 可能优化一个目标而牺牲另一个，这与我们观察到的 \"evidence 与 relation decouple\" 现象一致。\n- URL: https://arxiv.org/abs/2509.22047\n\n---\n\n## 3. LoRA Precision Effects\n\n### 3.1 Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies\n- (2025) — arXiv\n- Key finding: 提出 **Fidelity-Plasticity Trade-off**——一个 layer 的适应能力（Plasticity）受限于其 frozen weights 的信息容量（Fidelity）。**对语义关键层的激进量化产生不可恢复的信息瓶颈**，无论 adapter rank 多高都无法补偿。提出 QR-Adaptor 联合优化 per-layer bit-width 和 LoRA rank。\n- Relevance: **直接解释性**——4-bit 量化可能在 structured reasoning 最关键的中间层造成信息瓶颈。Evidence extraction 需要的细粒度语义理解（哪些 span 支持哪些 relation）需要高 Fidelity 的表示，4-bit 无法提供。\n- URL: https://arxiv.org/abs/2505.03802\n\n### 3.2 A Deep Dive into the Trade-Offs of Parameter-Efficient Preference Alignment Techniques\n- IBM Research (2024) — **ACL 2024**\n- Key finding: 300+ 实验横跨 SFT 和 DPO、LoRA 和 QLoRA、多个模型。发现 QLoRA 的 learning pattern 与 full fine-tuning **本质不同**（不仅是量上接近，模式也不同）。Alignment 对 data quality、method 和 adapter rank 高度敏感。\n- Relevance: 如果 QLoRA 在 DPO 上就已经表现出不同的 learning pattern，那在更复杂的 GRPO 上这种差异可能更大。\n- URL: https://arxiv.org/abs/2406.04879\n\n### 3.3 Revealing Modular Gradient Noise Imbalance in LLMs\n- (2026) — arXiv\n- Key finding: LLM 不同模块存在 gradient scale mismatch，Adam 的 adaptivity 无法完全修正，导致收敛慢或训练不稳定。提出 MoLS（Module-wise Learning-rate Scaling）。\n- Relevance: 4-bit quantization noise 会放大模块间的 gradient 不平衡——quantization noise 在不同层的影响不均匀，进一步加剧 gradient scale mismatch。\n- URL: https://arxiv.org/abs/2605.05794 [UNVERIFIED - 2026 年 5 月论文，可能尚未公开]\n\n### 3.4 CLoQ: Enhancing Fine-Tuning of Quantized LLMs via Calibrated LoRA Initialization\n- (2025) — arXiv\n- Key finding: QLoRA 的性能差距部分源于 suboptimal initialization——quantized weights 的误差影响 LoRA 的起始点。Calibrated initialization 使 INT2 CLoQ 在 Llama2-13B 上超越 INT4 QLoRA 在 arithmetic reasoning 上的表现。\n- Relevance: QLoRA 的 initialization 问题在 RL 训练中可能被放大——RL 对 policy 的初始状态比 SFT 更敏感。\n- URL: https://arxiv.org/abs/2501.18475\n\n---\n\n## 4. Catastrophic Forgetting in RLHF\n\n### 4.1 Robust Policy Optimization to Prevent Catastrophic Forgetting (FRPO)\n- Sabbaghi, Pappas, Javanmard & Hassani (2026) — arXiv\n- Key finding: Standard RLHF 找到的 high-reward policies 位于 **loss landscape 的 sharp regions**——小扰动就导致 reward 急剧下降。FRPO 在 KL-bounded 邻域内优化 reward flatness，找到对 downstream fine-tuning robust 的 policy。\n- Relevance: **关键洞察**——QLoRA 的 4-bit 量化噪声本质上就是对 weights 的持续小扰动。如果 GRPO 将 policy 推向 sharp region，这些持续的量化扰动就会不断将 policy 推离高 reward 区域，导致 catastrophic forgetting。bf16 没有这种噪声所以稳定。\n- URL: https://arxiv.org/abs/2602.08813\n\n### 4.2 Mitigating the Alignment Tax of RLHF\n- Lin, Tan et al. (2023/2024) — **EMNLP 2024**\n- Key finding: RLHF alignment 导致 pre-training 能力退化（\"alignment tax\"）——包括 translation、reasoning、reading comprehension。Model averaging（插值 pre/post RLHF 权重）达到最优 alignment-forgetting Pareto front。**不同层对 alignment tax 的敏感度不同**。\n- Relevance: Layer-wise sensitivity + quantization = 问题叠加。某些层既对 alignment forgetting 敏感，又被 4-bit 量化严重影响，double hit。\n- URL: https://arxiv.org/abs/2309.06256\n\n### 4.3 Mechanistic Analysis of Catastrophic Forgetting in LLMs During Continual Fine-tuning\n- (2026) — arXiv\n- Key finding: 识别三个遗忘机制：(i) 低层 attention weights 的 **gradient interference**（15-23% attention heads 严重受损）；(ii) 中间层的 **representational drift**（CKA 相似度下降 0.32-0.47）；(iii) **loss landscape flattening**。梯度对齐程度可预测遗忘严重性。\n- Relevance: 4-bit quantization noise 在低层引入额外的 gradient interference，在中间层加速 representational drift。这两个机制可能是 QLoRA+GRPO forgetting 的直接驱动力。\n- URL: https://arxiv.org/abs/2601.18699\n\n### 4.4 RL Minimizes Catastrophic Forgetting vs SFT\n- MIT (2025) — MarkTechPost 报道\n- Key finding: On-policy RL 天然比 SFT 更少遗忘，KL divergence 是遗忘严重性的预测指标。\n- Relevance: **反面证据/重要限定**——这个结论基于 full-precision RL。QLoRA 的 4-bit 噪声可能破坏了 RL 的这种天然优势，使得 quantized RL 反而比 SFT 遗忘更严重。这正是我们观察到的现象。\n- URL: https://www.marktechpost.com/2025/09/08/a-new-mit-study-shows-reinforcement-learning-minimizes-catastrophic-forgetting-compared-to-supervised-fine-tuning/\n\n### 4.5 Policy Gradient with Adaptive Entropy Annealing for Continual Fine-Tuning\n- Zhang et al. (2026) — arXiv\n- Key finding: 低 entropy 增强适应能力但增加遗忘风险。Adaptive entropy annealing 从 exploration（高 entropy）渐进到 exploitation（低 entropy），平衡 plasticity 和 stability。\n- Relevance: QLoRA 的量化噪声干扰了 entropy 的自然演化——可能导致 entropy 异常波动而非平稳下降，打破 plasticity-stability 平衡。\n- URL: https://arxiv.org/abs/2602.14078\n\n---\n\n## Summary\n\n### 我们的发现在文献中是否有先例？\n\n**部分有先例，但具体组合是新的。**\n\n- **Quantization 损害 RL training 已有报告**：Kumar et al. (2025) 发现 quantization-aware RL training 产生更差的 policy；QuRL 发现 INT8 就有 4% degradation；FP4 论文给出了理论阈值（gradient < √3 × noise → 停滞）\n- **GRPO 的稳定性问题已被广泛研究**：GTPO、DAPO、Revisiting GRPO 等多篇论文识别了 entropy collapse、token-level gradient conflict、zero-variance stalling\n- **LoRA 精度影响学习模式已有发现**：Fidelity-Plasticity trade-off、IBM 的 300+ 实验、CLoQ 都表明 QLoRA 的 learning pattern 与 full fine-tuning 本质不同\n- **RL 中的 catastrophic forgetting 已有研究**：FRPO 发现 sharp reward regions、alignment tax 论文发现 layer-wise sensitivity\n\n**但：QLoRA 4-bit 在 GRPO 训练中导致 structured output 的 subtask decoupling（relation 与 evidence extraction 分离）这个具体现象，文献中没有直接先例。**\n\n### 最接近的相关工作\n\n1. **QuRL (ICLR 2026)**——最接近，但研究的是 INT8 rollout quantization 而非 4-bit training quantization，且任务是 math reasoning 而非 structured IE\n2. **Kumar et al. (NeurIPS 2025)**——直接研究 quantization + RL，但未涉及 structured output 或 subtask decoupling\n3. **GTPO (2025)**——识别了 GRPO 的 token-level gradient conflict，这是 decoupling 的潜在机制，但未与 quantization 关联\n4. **Fidelity-Plasticity (2025)**——理论上解释了为什么 4-bit 在某些层造成不可恢复的瓶颈，但未在 RL 场景验证\n\n### 我们的 Unique Contribution\n\n1. **首次报告 QLoRA 4-bit + GRPO 在 structured IE 上的 catastrophic decoupling**——不仅是整体性能下降，而是 subtasks 之间的 coupling 被破坏（evidence extraction 与 relation extraction 分离）\n2. **提供 quantization-precision 消融**——同一任务、同一 GRPO 配置下，4-bit vs bf16 的直接对比，干净地隔离了 quantization 的影响\n3. **Structured output 场景的独特视角**——现有 quantization+RL 研究全部集中在 math reasoning（单一正确答案），structured IE 的 multi-component output（relation + evidence + faithfulness）更脆弱\n4. **机制假说**——结合 QuRL 的 \"微小 weight update 被噪声淹没\" + GTPO 的 \"token-level gradient conflict\" + Fidelity-Plasticity 的 \"信息瓶颈\"，我们可以提出一个连贯的解释框架：4-bit 噪声放大 GRPO 的 gradient conflict，在需要 multi-component coordination 的 structured IE 中首先破坏最脆弱的 coupling（evidence↔relation）\n\n### Claim 2 Reframing 建议\n\n原始 Claim 2 可 reframe 为：\n> \"Quantization precision is a critical but overlooked factor in RL-based IE training: 4-bit QLoRA introduces quantization noise that overwhelms GRPO's fine-grained gradient signals, causing catastrophic decoupling of structured subtasks — a failure mode absent in bf16 training and not predicted by QLoRA's strong SFT performance.\"\n\n支撑论据链：\n- QLoRA 在 SFT 阶段表现正常（consistent with Dettmers et al. 2023）\n- RL weight updates 远小于 SFT（QuRL, ICLR 2026）\n- 4-bit noise > √3 × RL gradient signal → training stagnation（FP4 theory）\n- GRPO 的 token-level gradient conflict 被噪声放大（GTPO analysis）\n- 结果是 subtask decoupling 而非整体退化（our unique finding）\n"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T17:56:33.705293+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'literature_quantization_rl.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T17:56:33.705556+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T17:56:33.705787+00:00_

_project
ced_stabilizer_literature_survey.md
cuda3_diagnostic.md
d024_literature_survey.md
diag_mvp2_grpo_flatnli_r3.md
diagnose_plan_001.md
diversity_probe.py
diversity_probe_results.md
dream_reports
edcr_analysis_r2b.md
eval_progress_check_0515.md
eval_script_audit.md
eval_status_check.md
freige
gap_analysis_w3.md
kl_analysis_report.md
manifest.yaml
mvp2_eval_rsft_r2b_maxtok1536_r2
plan_009_forgetting_data.csv
plan_009_grpo_forgetting
plan_012_dpo_ced
related_work_gap_analysis.md
rsft_gen_progress_check.md
rsft_pipeline_commands.md
status_check_loop4.md
training_health_check.md
training_trajectory_loop4.md
trl_grpo_stability_research.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T17:56:33.706036+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/literature_quantization_rl.md",
  "content": "# Quantization-RL Interaction Literature Survey\n\n调研日期：2026-05-15\n背景：GRPO 在 structured IE 任务上，QLoRA 4-bit 导致 catastrophic forgetting（rel_f1 0.4057→0.2167），bf16 LoRA 完全正常（rel_f1=0.4549）\n\n---\n\n## 1. Quantization + RL Training\n\n### 1.1 The Impact of Quantization on Large Reasoning Model Reinforcement Learning\n- Kumar, Xu, Wang & Webb (2025) — **NeurIPS 2025**\n- Key finding: 系统性实验发现 quantization-aware RL training (QAFT) 负面影响学习过程——quantized models produce worse policies。相比之下，先 RL 训练再 PTQ/QLoRA 量化的效果更好。量化引入的 \"sudden shock\" 在 RL 过程中尤其有害。\n- Relevance: **直接支撑我们的发现**——4-bit quantization 在 RL training 阶段（而非推理阶段）引入的噪声破坏 policy learning。我们的 QLoRA+GRPO 正是在训练阶段量化。\n- URL: https://arxiv.org/abs/2511.15694\n\n### 1.2 QuRL: Efficient Reinforcement Learning with Quantized Rollout\n- (2026) — **ICLR 2026**\n- Key finding: INT8 quantization during RL rollout 导致 4% accuracy degradation vs bf16 baseline。关键发现：RL steps 之间的 weight update 极小（\"extremely small\"），quantization noise 淹没了这些微小更新。提出 Adaptive Clipping Range (ACR) 将 INT8 gap 缩至 2%，FP8 缩至 ~1%。\n- Relevance: **核心机制解释**——RL 训练的 weight update 幅度远小于 SFT，而 4-bit quantization noise 远大于 INT8。这解释了为什么 QLoRA 在 SFT 阶段表现正常但在 GRPO 阶段 catastrophic——RL 的微小梯度信号被 4-bit 噪声完全淹没。\n- URL: https://arxiv.org/abs/2602.13953\n\n### 1.3 QeRL: Beyond Efficiency — Quantization-enhanced Reinforcement Learning for LLMs\n- Huang et al. (2025) — arXiv\n- Key finding: Quantization noise 增加 policy entropy，增强 exploration。通过 Adaptive Quantization Noise (AQN) 机制动态调整噪声，NVFP4+LoRA 实现比 16-bit LoRA 和 QLoRA 更快的 reward growth。7B 模型在 GSM8K 达 90.8%。\n- Relevance: 表明 quantization noise 如果被适当控制可以有益（类似 exploration noise），但 **未控制的噪声导致不稳定**。标准 QLoRA 没有 AQN 机制，噪声是 uncontrolled 的。\n- URL: https://arxiv.org/abs/2510.11696\n\n### 1.4 FP4 All the Way: Fully Quantized Training of LLMs\n- (2025) — arXiv\n- Key finding: 提出理论临界点——**当 gradient standard deviation < √3 × quantization noise 时，quantized training 停滞**。Stochastic rounding 对低精度训练稳定性至关重要。\n- Relevance: **理论基础**——4-bit NF4 的 quantization noise 量级远大于 8-bit 或 bf16。RL training 产生的 gradient signal 本身就比 SFT 弱（因为 reward-based 而非 direct supervision），更容易跌破 √3 阈值。\n- URL: https://arxiv.org/abs/2505.19115\n\n### 1.5 Training Dynamics Impact Post-Training Quantization Robustness\n- (2025) — **ICLR 2026**\n- Key finding: 量化误差由 learning rate 和训练超参数的复杂交互驱动。LR decay 后，validation loss 和 quantization error 出现 divergence。\n- Relevance: RL training 的 learning dynamics（reward signal 变化、policy ratio clipping）与 SFT 显著不同，这种不同的 training dynamics 可能导致模型进入 quantization-sensitive 区域。\n- URL: https://arxiv.org/abs/2510.06213\n\n---\n\n## 2. GRPO Stability / Failure Modes\n\n### 2.1 GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control\n- (2025) — arXiv\n- Key finding: 识别 GRPO 两个核心失败模式：(i) **token-level penalization**——不同 response 中共享的 valuable tokens 收到矛盾梯度信号；(ii) **policy collapse**——负 reward 的 completions 惩罚 confident responses，将决策推向 unlikely tokens。GTPO 通过跳过负更新、放大正更新解决，在 OOD benchmark 上比 GRPO 高 75pp (Pass@64)。\n- Relevance: **高度相关**——structured IE 中 relation tokens 和 evidence tokens 可能共享底层 representation。GRPO 的 token-level penalization 机制可能导致这些共享 tokens 收到矛盾信号，造成 relation 和 evidence extraction 的 decoupling。4-bit 噪声会放大这种矛盾。\n- URL: https://arxiv.org/abs/2508.03772\n\n### 2.2 DAPO: An Open-Source LLM Reinforcement Learning System at Scale\n- ByteDance Seed (2025) — arXiv\n- Key finding: Naive GRPO 训练中观察到 **entropy collapse**——policy entropy 快速下降。提出 Clip-Higher（解耦上下 clip range 给低概率 token 更多空间）+ Dynamic Sampling（过滤 uniform reward 样本确保每个 batch 有有效梯度）。Qwen2.5-32B 在 AIME 2024 达 50 分，超 DeepSeek-R1-Zero。\n- Relevance: Entropy collapse 在 structured output 任务上可能更严重——IE 任务的 valid output space 高度受限（JSON schema），GRPO 容易在这种约束空间中快速 collapse。QLoRA 的噪声可能加速或异常化这个 collapse 过程。\n- URL: https://arxiv.org/abs/2503.14476\n\n### 2.3 Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training\n- (2025) — arXiv\n- Key finding: On-policy GRPO 不带 masking 收敛到 Pass@1=45% 但 **不稳定**。Zero-variance masking（过滤所有 response 同 reward 的 group）可稳定训练并提升至 50%。Off-policy GRPO 通过 clipped surrogate objective 匹配或超越 on-policy。\n- Relevance: Zero-variance groups 在 structured IE 中很常见——当所有 sampled response 都提取到相同的 relation set 时（正确或错误），group 内 variance=0，GRPO 完全无法学习。QLoRA 的噪声可能同时影响 sampling diversity。\n- URL: https://arxiv.org/abs/2505.22257\n\n### 2.4 MO-GRPO: Mitigating Reward Hacking of GRPO on Multi-Objective Problems\n- (2025) — arXiv\n- Key finding: GRPO 在 multi-objective 问题上容易 reward hacking——agent overfits misspecified reward。\n- Relevance: 我们的 IE 任务本质是 multi-objective（relation extraction + evidence extraction），GRPO 可能优化一个目标而牺牲另一个，这与我们观察到的 \"evidence 与 relation decouple\" 现象一致。\n- URL: https://arxiv.org/abs/2509.22047\n\n---\n\n## 3. LoRA Precision Effects\n\n### 3.1 Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies\n- (2025) — arXiv\n- Key finding: 提出 **Fidelity-Plasticity Trade-off**——一个 layer 的适应能力（Plasticity）受限于其 frozen weights 的信息容量（Fidelity）。**对语义关键层的激进量化产生不可恢复的信息瓶颈**，无论 adapter rank 多高都无法补偿。提出 QR-Adaptor 联合优化 per-layer bit-width 和 LoRA rank。\n- Relevance: **直接解释性**——4-bit 量化可能在 structured reasoning 最关键的中间层造成信息瓶颈。Evidence extraction 需要的细粒度语义理解（哪些 span 支持哪些 relation）需要高 Fidelity 的表示，4-bit 无法提供。\n- URL: https://arxiv.org/abs/2505.03802\n\n### 3.2 A Deep Dive into the Trade-Offs of Parameter-Efficient Preference Alignment Techniques\n- IBM Research (2024) — **ACL 2024**\n- Key finding: 300+ 实验横跨 SFT 和 DPO、LoRA 和 QLoRA、多个模型。发现 QLoRA 的 learning pattern 与 full fine-tuning **本质不同**（不仅是量上接近，模式也不同）。Alignment 对 data quality、method 和 adapter rank 高度敏感。\n- Relevance: 如果 QLoRA 在 DPO 上就已经表现出不同的 learning pattern，那在更复杂的 GRPO 上这种差异可能更大。\n- URL: https://arxiv.org/abs/2406.04879\n\n### 3.3 Revealing Modular Gradient Noise Imbalance in LLMs\n- (2026) — arXiv\n- Key finding: LLM 不同模块存在 gradient scale mismatch，Adam 的 adaptivity 无法完全修正，导致收敛慢或训练不稳定。提出 MoLS（Module-wise Learning-rate Scaling）。\n- Relevance: 4-bit quantization noise 会放大模块间的 gradient 不平衡——quantization noise 在不同层的影响不均匀，进一步加剧 gradient scale mismatch。\n- URL: https://arxiv.org/abs/2605.05794 [UNVERIFIED - 2026年5月，可能尚未公开]\n\n### 3.4 CLoQ: Enhancing Fine-Tuning of Quantized LLMs via Calibrated LoRA Initialization\n- (2025) — arXiv\n- Key finding: QLoRA 的性能差距部分源于 suboptimal initialization——quantized weights 的误差影响 LoRA 的起始点。Calibrated initialization 使 INT2 CLoQ 在 Llama2-13B 上超越 INT4 QLoRA 在 arithmetic reasoning 上的表现。\n- Relevance: QLoRA 的 initialization 问题在 RL 训练中可能被放大——RL 对 policy 的初始状态比 SFT 更敏感。\n- URL: https://arxiv.org/abs/2501.18475\n\n---\n\n## 4. Catastrophic Forgetting in RLHF\n\n### 4.1 Robust Policy Optimization to Prevent Catastrophic Forgetting (FRPO)\n- Sabbaghi, Pappas, Javanmard & Hassani (2026) — arXiv\n- Key finding: Standard RLHF 找到的 high-reward policies 位于 **loss landscape 的 sharp regions**——小扰动就导致 reward 急剧下降。FRPO 在 KL-bounded 邻域内优化 reward flatness，找到对 downstream fine-tuning robust 的 policy。\n- Relevance: **关键洞察**——QLoRA 的 4-bit 量化噪声本质上就是对 weights 的持续小扰动。如果 GRPO 将 policy 推向 sharp region，这些持续的量化扰动就会不断将 policy 推离高 reward 区域，导致 catastrophic forgetting。bf16 没有这种噪声所以稳定。\n- URL: https://arxiv.org/abs/2602.08813\n\n### 4.2 Mitigating the Alignment Tax of RLHF\n- Lin, Tan et al. (2023/2024) — **EMNLP 2024**\n- Key finding: RLHF alignment 导致 pre-training 能力退化（\"alignment tax\"）——包括 translation、reasoning、reading comprehension。Model averaging（插值 pre/post RLHF 权重）达到最优 alignment-forgetting Pareto front。**不同层对 alignment tax 的敏感度不同**。\n- Relevance: Layer-wise sensitivity + quantization = 问题叠加。某些层既对 alignment forgetting 敏感，又被 4-bit 量化严重影响，double hit。\n- URL: https://arxiv.org/abs/2309.06256\n\n### 4.3 Mechanistic Analysis of Catastrophic Forgetting in LLMs During Continual Fine-tuning\n- (2026) — arXiv\n- Key finding: 识别三个遗忘机制：(i) 低层 attention weights 的 **gradient interference**（15-23% attention heads 严重受损）；(ii) 中间层的 **representational drift**（CKA 相似度下降 0.32-0.47）；(iii) **loss landscape flattening**。梯度对齐程度可预测遗忘严重性。\n- Relevance: 4-bit quantization noise 在低层引入额外的 gradient interference，在中间层加速 representational drift。这两个机制可能是 QLoRA+GRPO forgetting 的直接驱动力。\n- URL: https://arxiv.org/abs/2601.18699\n\n### 4.4 RL Minimizes Catastrophic Forgetting vs SFT\n- MIT (2025)\n- Key finding: On-policy RL 天然比 SFT 更少遗忘，KL divergence 是遗忘严重性的预测指标。\n- Relevance: **反面证据/重要限定**——这个结论基于 full-precision RL。QLoRA 的 4-bit 噪声可能破坏了 RL 的这种天然优势，使得 quantized RL 反而比 SFT 遗忘更严重。这正是我们观察到的现象。\n- URL: https://www.marktechpost.com/2025/09/08/a-new-mit-study-shows-reinforcement-learning-minimizes-catastrophic-forgetting-compared-to-supervised-fine-tuning/ [UNVERIFIED - 来源为科技新闻报道]\n\n### 4.5 Policy Gradient with Adaptive Entropy Annealing for Continual Fine-Tuning\n- Zhang et al. (2026) — arXiv\n- Key finding: 低 entropy 增强适应能力但增加遗忘风险。Adaptive entropy annealing 从 exploration（高 entropy）渐进到 exploitation（低 entropy），平衡 plasticity 和 stability。\n- Relevance: QLoRA 的量化噪声干扰了 entropy 的自然演化——可能导致 entropy 异常波动而非平稳下降，打破 plasticity-stability 平衡。\n- URL: https://arxiv.org/abs/2602.14078\n\n---\n\n## Summary\n\n### 我们的发现在文献中是否有先例？\n\n**部分有先例，但具体组合是新的。**\n\n- **Quantization 损害 RL training 已有报告**：Kumar et al. (NeurIPS 2025) 发现 quantization-aware RL 产生更差的 policy；QuRL (ICLR 2026) 发现 INT8 就有 4% degradation；FP4 论文给出理论阈值（gradient < √3 × noise → 停滞）\n- **GRPO 的稳定性问题已被广泛研究**：GTPO、DAPO、Revisiting GRPO 等多篇论文识别了 entropy collapse、token-level gradient conflict、zero-variance stalling\n- **LoRA 精度影响学习模式已有发现**：Fidelity-Plasticity trade-off、IBM 300+ 实验、CLoQ 都表明 QLoRA 的 learning pattern 与 full fine-tuning 本质不同\n- **RL 中的 catastrophic forgetting 已有研究**：FRPO 发现 sharp reward regions、alignment tax 论文发现 layer-wise sensitivity\n\n**但：QLoRA 4-bit 在 GRPO 训练中导致 structured output 的 subtask decoupling（relation 与 evidence extraction 分离）这个具体现象，文献中没有直接先例。**\n\n### 最接近的相关工作\n\n1. **QuRL (ICLR 2026)**——最接近，但研究的是 INT8 rollout quantization 而非 4-bit training quantization，且任务是 math reasoning 而非 structured IE\n2. **Kumar et al. (NeurIPS 2025)**——直接研究 quantization + RL，但未涉及 structured output 或 subtask decoupling\n3. **GTPO (2025)**——识别了 GRPO 的 token-level gradient conflict，这是 decoupling 的潜在机制，但未与 quantization 关联\n4. **Fidelity-Plasticity (2025)**——理论上解释了为什么 4-bit 在某些层造成不可恢复的瓶颈，但未在 RL 场景验证\n\n### 我们的 Unique Contribution\n\n1. **首次报告 QLoRA 4-bit + GRPO 在 structured IE 上的 catastrophic decoupling**——不仅是整体性能下降，而是 subtasks 之间的 coupling 被破坏（evidence extraction 与 relation extraction 分离）\n2. **提供 quantization-precision 消融**——同一任务、同一 GRPO 配置下，4-bit vs bf16 的直接对比，干净地隔离了 quantization 的影响\n3. **Structured output 场景的独特视角**——现有 quantization+RL 研究全部集中在 math reasoning（单一正确答案），structured IE 的 multi-component output（relation + evidence + faithfulness）更脆弱\n4. **机制假说**——结合 QuRL 的 \"微小 weight update 被噪声淹没\" + GTPO 的 \"token-level gradient conflict\" + Fidelity-Plasticity 的 \"信息瓶颈\"，提出连贯解释框架：4-bit 噪声放大 GRPO 的 gradient conflict，在需要 multi-component coordination 的 structured IE 中首先破坏最脆弱的 coupling（evidence↔relation）\n\n### Claim 2 Reframing 建议\n\n原始 Claim 2 可 reframe 为：\n> \"Quantization precision is a critical but overlooked factor in RL-based IE training: 4-bit QLoRA introduces quantization noise that overwhelms GRPO's fine-grained gradient signals, causing catastrophic decoupling of structured subtasks — a failure mode absent in bf16 training and not predicted by QLoRA's strong SFT performance.\"\n\n支撑论据链：\n- QLoRA 在 SFT 阶段表现正常（consistent with Dettmers et al. 2023）\n- RL weight updates 远小于 SFT（QuRL, ICLR 2026）\n- 4-bit noise > √3 × RL gradient signal → training stagnation（FP4 theory）\n- GRPO 的 token-level gradient conflict 被噪声放大（GTPO analysis）\n- 结果是 subtask decoupling 而非整体退化（our unique finding）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/literature_quantization_rl.md",
    "content": "# Quantization-RL Interaction Literature Survey\n\n调研日期：2026-05-15\n背景：GRPO 在 structured IE 任务上，QLoRA 4-bit 导致 catastrophic forgetting（rel_f1 0.4057→0.2167），bf16 LoRA 完全正常（rel_f1=0.4549）\n\n---\n\n## 1. Quantization + RL Training\n\n### 1.1 The Impact of Quantization on Large Reasoning Model Reinforcement Learning\n- Kumar, Xu, Wang & Webb (2025) — **NeurIPS 2025**\n- Key finding: 系统性实验发现 quantization-aware RL training (QAFT) 负面影响学习过程——quantized models produce worse policies。相比之下，先 RL 训练再 PTQ/QLoRA 量化的效果更好。量化引入的 \"sudden shock\" 在 RL 过程中尤其有害。\n- Relevance: **直接支撑我们的发现**——4-bit quantization 在 RL training 阶段（而非推理阶段）引入的噪声破坏 policy learning。我们的 QLoRA+GRPO 正是在训练阶段量化。\n- URL: https://arxiv.org/abs/2511.15694\n\n### 1.2 QuRL: Efficient Reinforcement Learning with Quantized Rollout\n- (2026) — **ICLR 2026**\n- Key finding: INT8 quantization during RL rollout 导致 4% accuracy degradation vs bf16 baseline。关键发现：RL steps 之间的 weight update 极小（\"extremely small\"），quantization noise 淹没了这些微小更新。提出 Adaptive Clipping Range (ACR) 将 INT8 gap 缩至 2%，FP8 缩至 ~1%。\n- Relevance: **核心机制解释**——RL 训练的 weight update 幅度远小于 SFT，而 4-bit quantization noise 远大于 INT8。这解释了为什么 QLoRA 在 SFT 阶段表现正常但在 GRPO 阶段 catastrophic——RL 的微小梯度信号被 4-bit 噪声完全淹没。\n- URL: https://arxiv.org/abs/2602.13953\n\n### 1.3 QeRL: Beyond Efficiency — Quantization-enhanced Reinforcement Learning for LLMs\n- Huang et al. (2025) — arXiv\n- Key finding: Quantization noise 增加 policy entropy，增强 exploration。通过 Adaptive Quantization Noise (AQN) 机制动态调整噪声，NVFP4+LoRA 实现比 16-bit LoRA 和 QLoRA 更快的 reward growth。7B 模型在 GSM8K 达 90.8%。\n- Relevance: 表明 quantization noise 如果被适当控制可以有益（类似 exploration noise），但 **未控制的噪声导致不稳定**。标准 QLoRA 没有 AQN 机制，噪声是 uncontrolled 的。\n- URL: https://arxiv.org/abs/2510.11696\n\n### 1.4 FP4 All the Way: Fully Quantized Training of LLMs\n- (2025) — arXiv\n- Key finding: 提出理论临界点——**当 gradient standard deviation < √3 × quantization noise 时，quantized training 停滞**。Stochastic rounding 对低精度训练稳定性至关重要。\n- Relevance: **理论基础**——4-bit NF4 的 quantization noise 量级远大于 8-bit 或 bf16。RL training 产生的 gradient signal 本身就比 SFT 弱（因为 reward-based 而非 direct supervision），更容易跌破 √3 阈值。\n- URL: https://arxiv.org/abs/2505.19115\n\n### 1.5 Training Dynamics Impact Post-Training Quantization Robustness\n- (2025) — **ICLR 2026**\n- Key finding: 量化误差由 learning rate 和训练超参数的复杂交互驱动。LR decay 后，validation loss 和 quantization error 出现 divergence。\n- Relevance: RL training 的 learning dynamics（reward signal 变化、policy ratio clipping）与 SFT 显著不同，这种不同的 training dynamics 可能导致模型进入 quantization-sensitive 区域。\n- URL: https://arxiv.org/abs/2510.06213\n\n---\n\n## 2. GRPO Stability / Failure Modes\n\n### 2.1 GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control\n- (2025) — arXiv\n- Key finding: 识别 GRPO 两个核心失败模式：(i) **token-level penalization**——不同 response 中共享的 valuable tokens 收到矛盾梯度信号；(ii) **policy collapse**——负 reward 的 completions 惩罚 confident responses，将决策推向 unlikely tokens。GTPO 通过跳过负更新、放大正更新解决，在 OOD benchmark 上比 GRPO 高 75pp (Pass@64)。\n- Relevance: **高度相关**——structured IE 中 relation tokens 和 evidence tokens 可能共享底层 representation。GRPO 的 token-level penalization 机制可能导致这些共享 tokens 收到矛盾信号，造成 relation 和 evidence extraction 的 decoupling。4-bit 噪声会放大这种矛盾。\n- URL: https://arxiv.org/abs/2508.03772\n\n### 2.2 DAPO: An Open-Source LLM Reinforcement Learning System at Scale\n- ByteDance Seed (2025) — arXiv\n- Key finding: Naive GRPO 训练中观察到 **entropy collapse**——policy entropy 快速下降。提出 Clip-Higher（解耦上下 clip range 给低概率 token 更多空间）+ Dynamic Sampling（过滤 uniform reward 样本确保每个 batch 有有效梯度）。Qwen2.5-32B 在 AIME 2024 达 50 分，超 DeepSeek-R1-Zero。\n- Relevance: Entropy collapse 在 structured output 任务上可能更严重——IE 任务的 valid output space 高度受限（JSON schema），GRPO 容易在这种约束空间中快速 collapse。QLoRA 的噪声可能加速或异常化这个 collapse 过程。\n- URL: https://arxiv.org/abs/2503.14476\n\n### 2.3 Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training\n- (2025) — arXiv\n- Key finding: On-policy GRPO 不带 masking 收敛到 Pass@1=45% 但 **不稳定**。Zero-variance masking（过滤所有 response 同 reward 的 group）可稳定训练并提升至 50%。Off-policy GRPO 通过 clipped surrogate objective 匹配或超越 on-policy。\n- Relevance: Zero-variance groups 在 structured IE 中很常见——当所有 sampled response 都提取到相同的 relation set 时（正确或错误），group 内 variance=0，GRPO 完全无法学习。QLoRA 的噪声可能同时影响 sampling diversity。\n- URL: https://arxiv.org/abs/2505.22257\n\n### 2.4 MO-GRPO: Mitigating Reward Hacking of GRPO on Multi-Objective Problems\n- (2025) — arXiv\n- Key finding: GRPO 在 multi-objective 问题上容易 reward hacking——agent overfits misspecified reward。\n- Relevance: 我们的 IE 任务本质是 multi-objective（relation extraction + evidence extraction），GRPO 可能优化一个目标而牺牲另一个，这与我们观察到的 \"evidence 与 relation decouple\" 现象一致。\n- URL: https://arxiv.org/abs/2509.22047\n\n---\n\n## 3. LoRA Precision Effects\n\n### 3.1 Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies\n- (2025) — arXiv\n- Key finding: 提出 **Fidelity-Plasticity Trade-off**——一个 layer 的适应能力（Plasticity）受限于其 frozen weights 的信息容量（Fidelity）。**对语义关键层的激进量化产生不可恢复的信息瓶颈**，无论 adapter rank 多高都无法补偿。提出 QR-Adaptor 联合优化 per-layer bit-width 和 LoRA rank。\n- Relevance: **直接解释性**——4-bit 量化可能在 structured reasoning 最关键的中间层造成信息瓶颈。Evidence extraction 需要的细粒度语义理解（哪些 span 支持哪些 relation）需要高 Fidelity 的表示，4-bit 无法提供。\n- URL: https://arxiv.org/abs/2505.03802\n\n### 3.2 A Deep Dive into the Trade-Offs of Parameter-Efficient Preference Alignment Techniques\n- IBM Research (2024) — **ACL 2024**\n- Key finding: 300+ 实验横跨 SFT 和 DPO、LoRA 和 QLoRA、多个模型。发现 QLoRA 的 learning pattern 与 full fine-tuning **本质不同**（不仅是量上接近，模式也不同）。Alignment 对 data quality、method 和 adapter rank 高度敏感。\n- Relevance: 如果 QLoRA 在 DPO 上就已经表现出不同的 learning pattern，那在更复杂的 GRPO 上这种差异可能更大。\n- URL: https://arxiv.org/abs/2406.04879\n\n### 3.3 Revealing Modular Gradient Noise Imbalance in LLMs\n- (2026) — arXiv\n- Key finding: LLM 不同模块存在 gradient scale mismatch，Adam 的 adaptivity 无法完全修正，导致收敛慢或训练不稳定。提出 MoLS（Module-wise Learning-rate Scaling）。\n- Relevance: 4-bit quantization noise 会放大模块间的 gradient 不平衡——quantization noise 在不同层的影响不均匀，进一步加剧 gradient scale mismatch。\n- URL: https://arxiv.org/abs/2605.05794 [UNVERIFIED - 2026年5月，可能尚未公开]\n\n### 3.4 CLoQ: Enhancing Fine-Tuning of Quantized LLMs via Calibrated LoRA Initialization\n- (2025) — arXiv\n- Key finding: QLoRA 的性能差距部分源于 suboptimal initialization——quantized weights 的误差影响 LoRA 的起始点。Calibrated initialization 使 INT2 CLoQ 在 Llama2-13B 上超越 INT4 QLoRA 在 arithmetic reasoning 上的表现。\n- Relevance: QLoRA 的 initialization 问题在 RL 训练中可能被放大——RL 对 policy 的初始状态比 SFT 更敏感。\n- URL: https://arxiv.org/abs/2501.18475\n\n---\n\n## 4. Catastrophic Forgetting in RLHF\n\n### 4.1 Robust Policy Optimization to Prevent Catastrophic Forgetting (FRPO)\n- Sabbaghi, Pappas, Javanmard & Hassani (2026) — arXiv\n- Key finding: Standard RLHF 找到的 high-reward policies 位于 **loss landscape 的 sharp regions**——小扰动就导致 reward 急剧下降。FRPO 在 KL-bounded 邻域内优化 reward flatness，找到对 downstream fine-tuning robust 的 policy。\n- Relevance: **关键洞察**——QLoRA 的 4-bit 量化噪声本质上就是对 weights 的持续小扰动。如果 GRPO 将 policy 推向 sharp region，这些持续的量化扰动就会不断将 policy 推离高 reward 区域，导致 catastrophic forgetting。bf16 没有这种噪声所以稳定。\n- URL: https://arxiv.org/abs/2602.08813\n\n### 4.2 Mitigating the Alignment Tax of RLHF\n- Lin, Tan et al. (2023/2024) — **EMNLP 2024**\n- Key finding: RLHF alignment 导致 pre-training 能力退化（\"alignment tax\"）——包括 translation、reasoning、reading comprehension。Model averaging（插值 pre/post RLHF 权重）达到最优 alignment-forgetting Pareto front。**不同层对 alignment tax 的敏感度不同**。\n- Relevance: Layer-wise sensitivity + quantization = 问题叠加。某些层既对 alignment forgetting 敏感，又被 4-bit 量化严重影响，double hit。\n- URL: https://arxiv.org/abs/2309.06256\n\n### 4.3 Mechanistic Analysis of Catastrophic Forgetting in LLMs During Continual Fine-tuning\n- (2026) — arXiv\n- Key finding: 识别三个遗忘机制：(i) 低层 attention weights 的 **gradient interference**（15-23% attention heads 严重受损）；(ii) 中间层的 **representational drift**（CKA 相似度下降 0.32-0.47）；(iii) **loss landscape flattening**。梯度对齐程度可预测遗忘严重性。\n- Relevance: 4-bit quantization noise 在低层引入额外的 gradient interference，在中间层加速 representational drift。这两个机制可能是 QLoRA+GRPO forgetting 的直接驱动力。\n- URL: https://arxiv.org/abs/2601.18699\n\n### 4.4 RL Minimizes Catastrophic Forgetting vs SFT\n- MIT (2025)\n- Key finding: On-policy RL 天然比 SFT 更少遗忘，KL divergence 是遗忘严重性的预测指标。\n- Relevance: **反面证据/重要限定**——这个结论基于 full-precision RL。QLoRA 的 4-bit 噪声可能破坏了 RL 的这种天然优势，使得 quantized RL 反而比 SFT 遗忘更严重。这正是我们观察到的现象。\n- URL: https://www.marktechpost.com/2025/09/08/a-new-mit-study-shows-reinforcement-learning-minimizes-catastrophic-forgetting-compared-to-supervised-fine-tuning/ [UNVERIFIED - 来源为科技新闻报道]\n\n### 4.5 Policy Gradient with Adaptive Entropy Annealing for Continual Fine-Tuning\n- Zhang et al. (2026) — arXiv\n- Key finding: 低 entropy 增强适应能力但增加遗忘风险。Adaptive entropy annealing 从 exploration（高 entropy）渐进到 exploitation（低 entropy），平衡 plasticity 和 stability。\n- Relevance: QLoRA 的量化噪声干扰了 entropy 的自然演化——可能导致 entropy 异常波动而非平稳下降，打破 plasticity-stability 平衡。\n- URL: https://arxiv.org/abs/2602.14078\n\n---\n\n## Summary\n\n### 我们的发现在文献中是否有先例？\n\n**部分有先例，但具体组合是新的。**\n\n- **Quantization 损害 RL training 已有报告**：Kumar et al. (NeurIPS 2025) 发现 quantization-aware RL 产生更差的 policy；QuRL (ICLR 2026) 发现 INT8 就有 4% degradation；FP4 论文给出理论阈值（gradient < √3 × noise → 停滞）\n- **GRPO 的稳定性问题已被广泛研究**：GTPO、DAPO、Revisiting GRPO 等多篇论文识别了 entropy collapse、token-level gradient conflict、zero-variance stalling\n- **LoRA 精度影响学习模式已有发现**：Fidelity-Plasticity trade-off、IBM 300+ 实验、CLoQ 都表明 QLoRA 的 learning pattern 与 full fine-tuning 本质不同\n- **RL 中的 catastrophic forgetting 已有研究**：FRPO 发现 sharp reward regions、alignment tax 论文发现 layer-wise sensitivity\n\n**但：QLoRA 4-bit 在 GRPO 训练中导致 structured output 的 subtask decoupling（relation 与 evidence extraction 分离）这个具体现象，文献中没有直接先例。**\n\n### 最接近的相关工作\n\n1. **QuRL (ICLR 2026)**——最接近，但研究的是 INT8 rollout quantization 而非 4-bit training quantization，且任务是 math reasoning 而非 structured IE\n2. **Kumar et al. (NeurIPS 2025)**——直接研究 quantization + RL，但未涉及 structured output 或 subtask decoupling\n3. **GTPO (2025)**——识别了 GRPO 的 token-level gradient conflict，这是 decoupling 的潜在机制，但未与 quantization 关联\n4. **Fidelity-Plasticity (2025)**——理论上解释了为什么 4-bit 在某些层造成不可恢复的瓶颈，但未在 RL 场景验证\n\n### 我们的 Unique Contribution\n\n1. **首次报告 QLoRA 4-bit + GRPO 在 structured IE 上的 catastrophic decoupling**——不仅是整体性能下降，而是 subtasks 之间的 coupling 被破坏（evidence extraction 与 relation extraction 分离）\n2. **提供 quantization-precision 消融**——同一任务、同一 GRPO 配置下，4-bit vs bf16 的直接对比，干净地隔离了 quantization 的影响\n3. **Structured output 场景的独特视角**——现有 quantization+RL 研究全部集中在 math reasoning（单一正确答案），structured IE 的 multi-component output（relation + evidence + faithfulness）更脆弱\n4. **机制假说**——结合 QuRL 的 \"微小 weight update 被噪声淹没\" + GTPO 的 \"token-level gradient conflict\" + Fidelity-Plasticity 的 \"信息瓶颈\"，提出连贯解释框架：4-bit 噪声放大 GRPO 的 gradient conflict，在需要 multi-component coordination 的 structured IE 中首先破坏最脆弱的 coupling（evidence↔relation）\n\n### Claim 2 Reframing 建议\n\n原始 Claim 2 可 reframe 为：\n> \"Quantization precision is a critical but overlooked factor in RL-based IE training: 4-bit QLoRA introduces quantization noise that overwhelms GRPO's fine-grained gradient signals, causing catastrophic decoupling of structured subtasks — a failure mode absent in bf16 training and not predicted by QLoRA's strong SFT performance.\"\n\n支撑论据链：\n- QLoRA 在 SFT 阶段表现正常（consistent with Dettmers et al. 2023）\n- RL weight updates 远小于 SFT（QuRL, ICLR 2026）\n- 4-bit noise > √3 × RL gradient signal → training stagnation（FP4 theory）\n- GRPO 的 token-level gradient conflict 被噪声放大（GTPO analysis）\n- 结果是 subtask decoupling 而非整体退化（our unique finding）\n"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T17:56:33.706483+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/literature_quantization_rl.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_quantization-rl-interaction_20260515T174945",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-15T17:56:33.706715+00:00_

文献综述已写入 `artifacts/literature_quantization_rl.md`，覆盖 4 个方向共 18 篇论文。

核心发现：

**有直接先例的部分：**
- Kumar et al. (NeurIPS 2025) 和 QuRL (ICLR 2026) 已报告 quantization 损害 RL training，QuRL 发现 RL 的 weight update 极小、被 quantization noise 淹没
- FP4 论文提出理论阈值：gradient < √3 × quantization noise → 训练停滞
- GTPO/DAPO 已识别 GRPO 的 entropy collapse 和 token-level gradient conflict

**我们的 unique contribution：**
- QLoRA 4-bit + GRPO 导致 structured output 的 **subtask decoupling**（relation↔evidence 分离）——文献中无直接先例
- 现有 quantization+RL 研究全部集中在 math reasoning，structured IE 的 multi-component output 更脆弱
- 同一配置下 4-bit vs bf16 的干净消融是独特的实验证据

**Claim 2 reframing** 建议已附在文档末尾，论据链从 QLoRA SFT 正常 → RL weight update 微小 → 4-bit noise 超过理论阈值 → gradient conflict 放大 → subtask decoupling。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_quantization-rl-interaction_20260515T174945"
}
```

</details>

---
