# research deep analysis competitors

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 111
- **Recorded user turns:** 0
- **Tool calls:** 55
- **Original source:** `logs/chats/worker_research_deep_analysis_competitors_20260519T013824.jsonl`
- **Structured JSON:** [`708fa0c8e5199977fce7.json`](../../sessions/70/708fa0c8e5199977fce7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

111 recorded events

### Tool call

_source line 1 · 2026-05-19T01:55:14.756414+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Analyze Compressor-VLA paper",
  "prompt": "Fetch and deeply analyze the paper \"Compressor-VLA\" (arXiv 2511.18950). \n\nFirst try fetching the HTML version: https://arxiv.org/html/2511.18950\nIf that fails, try the PDF: https://arxiv.org/pdf/2511.18950\n\nUse WebFetch to get the content.\n\nThen provide a DETAILED structured analysis covering ALL of these dimensions:\n\n**A. 使用的 VLA 模型**\n- Specific model names (OpenVLA? SmolVLA? RT-2? other?)\n- Does it include SmolVLA?\n- Model parameter sizes\n\n**B. Vision Connector 类型**\n- pixel-shuffle / MLP projection / cross-attention / other\n- Does it analyze how different connectors affect compression?\n\n**C. 压缩方法核心机制**\n- Training-free or training-required?\n- Specific compression strategy (pruning / pooling / resampling / other)\n- Compression ratio (how many tokens reduced? FLOPs reduction?)\n\n**D. LIBERO 实验数据**\n- Which LIBERO suite (Object/Spatial/Goal/Long)?\n- How many tasks?\n- How many seeds? How many episodes?\n- Specific SR numbers (baseline vs compressed)\n- Error bars / confidence intervals?\n\n**E. 关键问题**\n- Does it analyze cliff-edge phenomenon (pruning causing SR to suddenly collapse to 0%)?\n- Does it do cross-architecture comparison (different vision connectors' pruning effects)?\n- Does it have re-encoding vs deletion control experiments?\n- Does it do closed-loop evaluation (actual execution in simulation, not just action prediction accuracy)?\n\n**F. 与我们工作的差异**\n- Our core finding: pixel-shuffle connector causes 0% SR with any token deletion (cliff-edge), MLP connector shows graceful degradation. Cross-attention re-encoding can recover performance where deletion fails.\n- Does this paper address architecture-dependent compressibility?\n- What would be our unique contribution relative to this paper?\n\nBe thorough - extract specific numbers, table data, and experimental details. Quote relevant passages when possible.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Agent",
  "tool_args": {
    "description": "Analyze Compressor-VLA paper",
    "prompt": "Fetch and deeply analyze the paper \"Compressor-VLA\" (arXiv 2511.18950). \n\nFirst try fetching the HTML version: https://arxiv.org/html/2511.18950\nIf that fails, try the PDF: https://arxiv.org/pdf/2511.18950\n\nUse WebFetch to get the content.\n\nThen provide a DETAILED structured analysis covering ALL of these dimensions:\n\n**A. 使用的 VLA 模型**\n- Specific model names (OpenVLA? SmolVLA? RT-2? other?)\n- Does it include SmolVLA?\n- Model parameter sizes\n\n**B. Vision Connector 类型**\n- pixel-shuffle / MLP projection / cross-attention / other\n- Does it analyze how different connectors affect compression?\n\n**C. 压缩方法核心机制**\n- Training-free or training-required?\n- Specific compression strategy (pruning / pooling / resampling / other)\n- Compression ratio (how many tokens reduced? FLOPs reduction?)\n\n**D. LIBERO 实验数据**\n- Which LIBERO suite (Object/Spatial/Goal/Long)?\n- How many tasks?\n- How many seeds? How many episodes?\n- Specific SR numbers (baseline vs compressed)\n- Error bars / confidence intervals?\n\n**E. 关键问题**\n- Does it analyze cliff-edge phenomenon (pruning causing SR to suddenly collapse to 0%)?\n- Does it do cross-architecture comparison (different vision connectors' pruning effects)?\n- Does it have re-encoding vs deletion control experiments?\n- Does it do closed-loop evaluation (actual execution in simulation, not just action prediction accuracy)?\n\n**F. 与我们工作的差异**\n- Our core finding: pixel-shuffle connector causes 0% SR with any token deletion (cliff-edge), MLP connector shows graceful degradation. Cross-attention re-encoding can recover performance where deletion fails.\n- Does this paper address architecture-dependent compressibility?\n- What would be our unique contribution relative to this paper?\n\nBe thorough - extract specific numbers, table data, and experimental details. Quote relevant passages when possible.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-19T01:55:14.756862+00:00_

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
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
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

_source line 3 · 2026-05-19T01:55:14.757050+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T01:55:14.757249+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2511.18950",
  "prompt": "Extract the COMPLETE content of this paper. I need ALL of the following in full detail:\n\n1. ABSTRACT - full text\n2. INTRODUCTION - full text\n3. METHOD section - complete description of the compression approach, all techniques, all algorithms\n4. Which VLA models are used (OpenVLA, SmolVLA, RT-2, etc.)? List ALL model names and parameter sizes.\n5. Vision connector types discussed (pixel-shuffle, MLP, cross-attention, etc.)\n6. Compression mechanism details: training-free or training-required? Pruning/pooling/resampling? Token reduction ratios? FLOPs reduction?\n7. EXPERIMENTS section - ALL tables with numbers, especially:\n   - LIBERO benchmark results (which suites: Object/Spatial/Goal/Long?)\n   - Number of tasks, seeds, episodes\n   - Success rate numbers for baseline vs compressed (exact numbers)\n   - Error bars or confidence intervals\n8. Any analysis of \"cliff-edge\" phenomenon (sudden collapse of performance with pruning)\n9. Any cross-architecture comparison (different vision connectors)\n10. Any re-encoding vs deletion experiments\n11. Whether evaluation is closed-loop (actual robot/simulation execution) or open-loop (action prediction only)\n12. RELATED WORK section\n13. All figure and table captions\n14. CONCLUSION\n\nPlease be as thorough as possible - extract specific numbers, percentages, and quote key passages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2511.18950",
    "prompt": "Extract the COMPLETE content of this paper. I need ALL of the following in full detail:\n\n1. ABSTRACT - full text\n2. INTRODUCTION - full text\n3. METHOD section - complete description of the compression approach, all techniques, all algorithms\n4. Which VLA models are used (OpenVLA, SmolVLA, RT-2, etc.)? List ALL model names and parameter sizes.\n5. Vision connector types discussed (pixel-shuffle, MLP, cross-attention, etc.)\n6. Compression mechanism details: training-free or training-required? Pruning/pooling/resampling? Token reduction ratios? FLOPs reduction?\n7. EXPERIMENTS section - ALL tables with numbers, especially:\n   - LIBERO benchmark results (which suites: Object/Spatial/Goal/Long?)\n   - Number of tasks, seeds, episodes\n   - Success rate numbers for baseline vs compressed (exact numbers)\n   - Error bars or confidence intervals\n8. Any analysis of \"cliff-edge\" phenomenon (sudden collapse of performance with pruning)\n9. Any cross-architecture comparison (different vision connectors)\n10. Any re-encoding vs deletion experiments\n11. Whether evaluation is closed-loop (actual robot/simulation execution) or open-loop (action prediction only)\n12. RELATED WORK section\n13. All figure and table captions\n14. CONCLUSION\n\nPlease be as thorough as possible - extract specific numbers, percentages, and quote key passages."
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T01:55:14.757579+00:00_

# Compressor-VLA: Instruction-Guided Visual Token Compression - Comprehensive Extract

## 1. ABSTRACT
The paper proposes "Compressor-VLA, a novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models." The framework achieves "a competitive success rate on the LIBERO benchmark while reducing FLOPs by 59% and the visual token count by over 3x compared to its baseline." Real-robot deployments validate "sim-to-real transferability and practical applicability."

## 2. INTRODUCTION (Key Passages)

**Problem Statement:** "The primary reason for this overhead is the high-capacity visual stream. State-of-the-art VLAs typically employ a Vision Transformer to encode each single image frame into a long sequence of visual tokens." This causes "substantial computational costs, including FLOPs and memory cost. High FLOPs will directly lead to inference latencies."

**Limitations of Prior Work:** "While effective at reducing token count, this 'hard' selection strategy risks losing crucial information. More importantly, this entire approach fails to leverage the language instruction to guide the compression process."

**Core Innovation:** "Instead of directly pruning tokens in previous works, our key insight is using a hybrid instruction-guided compressor to reconstruct a compact set of tokens."

## 3. METHOD - Complete Description

### 3.1 Overall Architecture

The framework replaces the standard projector between vision encoder and LLM backbone. It operates on:
- Visual features X ∈ ℝ^(N×D) from pre-trained vision encoder
- Language instruction embeddings from VLA's LLM backbone

**Data Processing:** "To accommodate variable-length instructions, we apply mean pooling across the sequence of language embeddings to derive a single fixed-size vector, L_pooled."

**Dual Pathway Design:**
1. **Semantic Task Compressor (STC):** Generates globally-contextualized summary Z_G ∈ ℝ^(k×D)
2. **Spatial Re
…[truncated 10487 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T01:55:14.757789+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2511.18950",
  "prompt": "I need additional specific details from this paper:\n\n1. How many seeds were used for LIBERO evaluation? How many episodes per task? Is there any mention of \"20 episodes per task\" or \"3 seeds\" or similar?\n\n2. What exactly is SP-VLA? Is it the pixel-shuffle based method? What does SP stand for?\n\n3. What exactly is SpecPrune-VLA? What is its mechanism?\n\n4. What is VLA-Cache's mechanism?\n\n5. Does the paper mention SmolVLA anywhere?\n\n6. Does the paper discuss pixel-shuffle connectors at all?\n\n7. Any discussion of MLP projection vs cross-attention vs pixel-shuffle as vision connectors?\n\n8. Does the paper discuss architecture-dependent compression sensitivity? i.e., does the compressibility depend on the type of vision connector used?\n\n9. Are there any supplementary/appendix sections with additional experiments?\n\n10. What is the exact number of evaluation episodes for LIBERO? (e.g., 500 episodes per suite = 50 per task × 10 tasks?)\n\n11. Does the paper cite or discuss EfficientVLA, FastVLA, or TinyVLA?\n\n12. Any analysis of which visual tokens are important vs unimportant? Attention map analysis?\n\n13. What is the training data used? Is it the same LIBERO demonstrations or additional data?\n\n14. Does the paper discuss the relationship between compression ratio and task complexity (e.g., Long horizon tasks being more sensitive)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2511.18950",
    "prompt": "I need additional specific details from this paper:\n\n1. How many seeds were used for LIBERO evaluation? How many episodes per task? Is there any mention of \"20 episodes per task\" or \"3 seeds\" or similar?\n\n2. What exactly is SP-VLA? Is it the pixel-shuffle based method? What does SP stand for?\n\n3. What exactly is SpecPrune-VLA? What is its mechanism?\n\n4. What is VLA-Cache's mechanism?\n\n5. Does the paper mention SmolVLA anywhere?\n\n6. Does the paper discuss pixel-shuffle connectors at all?\n\n7. Any discussion of MLP projection vs cross-attention vs pixel-shuffle as vision connectors?\n\n8. Does the paper discuss architecture-dependent compression sensitivity? i.e., does the compressibility depend on the type of vision connector used?\n\n9. Are there any supplementary/appendix sections with additional experiments?\n\n10. What is the exact number of evaluation episodes for LIBERO? (e.g., 500 episodes per suite = 50 per task × 10 tasks?)\n\n11. Does the paper cite or discuss EfficientVLA, FastVLA, or TinyVLA?\n\n12. Any analysis of which visual tokens are important vs unimportant? Attention map analysis?\n\n13. What is the training data used? Is it the same LIBERO demonstrations or additional data?\n\n14. Does the paper discuss the relationship between compression ratio and task complexity (e.g., Long horizon tasks being more sensitive)?"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T01:55:14.757947+00:00_

# Analysis of Compressor-VLA Paper Details

## Questions Answered:

**1. LIBERO Evaluation Details:**
Not explicitly stated. The paper references "LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long, which contain diverse objects, scene layouts, and language instructions. Each task suite consists of 10 tasks with 50 human-teleoperated demonstrations." However, the exact number of test episodes per task and random seeds are not specified in the provided content.

**2. SP-VLA Mechanism:**
Not detailed in this paper. It's cited as a baseline: "SP-VLA [[28]](https://arxiv.org/html/2511.18950v1#bib.bib28)]" but the paper does not explain what "SP" stands for or its mechanism.

**3. SpecPrune-VLA Mechanism:**
Not explained in the provided text. Listed only as a comparison baseline with results showing "98.2% success rate" and "1.70T FLOPs."

**4. VLA-Cache Mechanism:**
The paper states: "it caches the similar and unimportant tokens' key and value from the last generation and reuses them in the next inference."

**5. SmolVLA Mention:**
No mention of SmolVLA anywhere in the document.

**6. Pixel-Shuffle Discussion:**
No discussion of pixel-shuffle connectors in this paper.

**7. Vision Connector Comparison:**
The paper does not compare MLP projection, cross-attention, or pixel-shuffle as alternative vision connectors.

**8. Architecture-Dependent Compression Sensitivity:**
No analysis of whether compression effectiveness varies based on vision connector type is provided.

**9. Supplementary Sections:**
No appendix or supplementary material is included in the provided content.

**10. Exact LIBERO Episodes:**
Not specified. Only that each suite has "10 tasks with 50 human-teleoperated demonstrations."

**11. Related Efficient VLA Methods:**
The paper cites "EfficientVLA [[8]](https://arxiv.org/html/2511.18950v1#bib.bib8)" as a reference but does not discuss TinyVLA or FastVLA by those names.

**12. Token Importance Analysis:**
Qualitative attention visualizations are 
…[truncated 483 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T01:55:14.758118+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2511.18950",
  "prompt": "I need to find very specific details. Please look carefully for:\n\n1. The EXACT evaluation protocol for LIBERO: how many rollouts/episodes per task for evaluation? Is it 20 episodes? 50 episodes? Does it say \"we evaluate each task for X episodes\" or \"X rollouts per task\"?\n\n2. How many random seeds? Does it say \"averaged over 3 seeds\" or similar?\n\n3. Are there standard deviations or confidence intervals reported in any table or in the text?\n\n4. The exact references list - specifically citations [28] (SP-VLA), [8] (EfficientVLA), and any other efficient VLA baselines.\n\n5. Does the paper mention \"token pruning\" causing catastrophic failure or sudden performance drops?\n\n6. Any mention of \"training-free\" compression methods?\n\n7. The exact model sizes - how many parameters does OpenVLA-OFT have? Does it say 7B?\n\n8. Does the paper use only OpenVLA-OFT as base model, or does it also try the compression on other VLA architectures?\n\n9. What vision encoder is used - ViT-L? ViT-H? What resolution?\n\n10. How many visual tokens does the vision encoder produce before compression? Is it 256? 512? 729?\n\n11. The exact architecture: is it DINOv2 + SigLIP dual encoder producing 256+256=512 tokens?\n\n12. Any discussion of latency/inference speed benchmarks beyond FLOPs?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2511.18950",
    "prompt": "I need to find very specific details. Please look carefully for:\n\n1. The EXACT evaluation protocol for LIBERO: how many rollouts/episodes per task for evaluation? Is it 20 episodes? 50 episodes? Does it say \"we evaluate each task for X episodes\" or \"X rollouts per task\"?\n\n2. How many random seeds? Does it say \"averaged over 3 seeds\" or similar?\n\n3. Are there standard deviations or confidence intervals reported in any table or in the text?\n\n4. The exact references list - specifically citations [28] (SP-VLA), [8] (EfficientVLA), and any other efficient VLA baselines.\n\n5. Does the paper mention \"token pruning\" causing catastrophic failure or sudden performance drops?\n\n6. Any mention of \"training-free\" compression methods?\n\n7. The exact model sizes - how many parameters does OpenVLA-OFT have? Does it say 7B?\n\n8. Does the paper use only OpenVLA-OFT as base model, or does it also try the compression on other VLA architectures?\n\n9. What vision encoder is used - ViT-L? ViT-H? What resolution?\n\n10. How many visual tokens does the vision encoder produce before compression? Is it 256? 512? 729?\n\n11. The exact architecture: is it DINOv2 + SigLIP dual encoder producing 256+256=512 tokens?\n\n12. Any discussion of latency/inference speed benchmarks beyond FLOPs?"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T01:55:14.758299+00:00_

# Analysis of Compressor-VLA Paper Details

## 1. LIBERO Evaluation Protocol
The paper does **not explicitly state** the number of episodes per task for evaluation. It only mentions: "Each task suite consists of 10 tasks with 50 human-teleoperated demonstrations" for training data. The evaluation metrics section defines success rate calculation but not the episode count.

## 2. Random Seeds
**No mention of random seeds or multiple runs.** The paper provides no statement like "averaged over X seeds" or confidence intervals.

## 3. Standard Deviations/Confidence Intervals
**None reported.** Tables 1-4 show only point estimates with no error bars or statistical measures.

## 4. Efficient VLA Baselines
Key citations:
- **[28] SP-VLA**: "SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration"
- **[8] EfficientVLA**: "EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models"
- **[21] VLA-Cache**: "Towards efficient vision-language-action model via adaptive token caching"

## 5. Token Pruning Failure Discussion
The paper notes pruning as "task-agnostic" and states it "fails to leverage the language instruction," but does **not report catastrophic failures**. It simply argues pruning is suboptimal.

## 6. Training-Free Methods
**Yes**, EfficientVLA ([8]) is explicitly labeled as "Training-Free" in its title.

## 7. Model Size
The paper states: "LiAMA-2-7B backbone" but does **not provide total parameter count** for OpenVLA-OFT.

## 8. Base Model
**Only OpenVLA-OFT is used.** The paper compares against other VLAs (CogACT, π0) but only implements compression on OpenVLA-OFT.

## 9. Vision Encoder Specs
"two-branch vision encoder (DINOv2 and SigLIP)" - **no resolution specified** in the paper.

## 10. Pre-Compression Token Count
**512 tokens** before compression (confirmed in Table 1: "512" under baseline).

## 11. Dual Encoder Architecture
Confirmed: "DINOv2 and SigLIP" dual branches producing 512 total tokens (
…[truncated 189 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T01:55:14.758459+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.18950",
  "prompt": "Get the full abstract, author list, submission date, and any other metadata for this paper. Also check if there are any revision notes or supplementary materials linked."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2511.18950",
    "prompt": "Get the full abstract, author list, submission date, and any other metadata for this paper. Also check if there are any revision notes or supplementary materials linked."
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T01:55:14.758590+00:00_

# Compressor-VLA Paper Summary

**Title:** Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation

**Authors:** Juntao Gao, Feiyang Ye, Jing Zhang, Wenjing Qian

**Submission Date:** November 24, 2025

**arXiv ID:** 2511.18950 (Computer Science - Robotics)

## Key Contribution

The paper addresses computational efficiency in Vision-Language-Action (VLA) models for robotics. The authors propose that "standard token pruning techniques...struggle to preserve task-critical visual information," motivating their hybrid compression framework.

## Technical Approach

Compressor-VLA employs two compression modules:
- **Semantic Task Compressor:** Extracts task-relevant context
- **Spatial Refinement Compressor:** Maintains fine-grained spatial details

The system uses natural language instructions to dynamically guide which visual information gets compressed.

## Results

The framework achieves notable efficiency gains: "reducing FLOPs by 59% and the visual token count by over 3x compared to its baseline" while maintaining competitive performance on the LIBERO benchmark. Real-robot validation on dual-arm systems demonstrated practical applicability.

**Access:** Available as PDF, HTML, and TeX source on arXiv under CC BY 4.0 license.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T01:55:14.758797+00:00_

Here is the complete structured analysis:

---

## A. 使用的 VLA 模型

**Base model:** OpenVLA-OFT (LLaMA-2-7B backbone + DINOv2/SigLIP dual vision encoder), producing 512 visual tokens.

**Compared models:**
- General-purpose VLAs: OpenVLA-OFT, CogACT, π0
- Efficient VLA baselines: SP-VLA, FastV, SparseVLM, SpecPrune-VLA, VLA-Cache

**SmolVLA is NOT mentioned anywhere in the paper.** The paper only experiments with OpenVLA-OFT as the base architecture for its compression module. No other base architecture is tested with the proposed compressor.

**Parameter sizes:** Only "LLaMA-2-7B" is stated; no total parameter count for the full VLA model is given.

---

## B. Vision Connector 类型

The paper does **NOT** analyze different vision connector types. There is:
- No discussion of pixel-shuffle connectors
- No discussion of MLP projection vs cross-attention as alternative connectors
- No cross-architecture comparison of connector types

The proposed compressor itself uses cross-attention (STC) and local windowed attention (SRC) to reconstruct compressed tokens, but this **replaces** the standard projector rather than comparing different projector types.

---

## C. 压缩方法核心机制

**Training-required:** Yes. The compressor modules (STC + SRC), action head, and proprioceptive projector are fully fine-tuned. LoRA rank 32 is applied to vision encoder and LLM. Training: 150K steps, 8 GPUs, batch size 64.

**Strategy: Reconstructive compression (not pruning/deletion).** The key insight: instead of pruning tokens, use a hybrid instruction-guided compressor to **reconstruct** a compact set of new tokens via:
1. **STC (Semantic Task Compressor):** k=16 learnable queries, conditioned on language instruction via FiLM, perform cross-attention over all 512 visual tokens → produces 16 global summary tokens
2. **SRC (Spatial Refinement Compressor):** Divides feature map into local windows (w=2), downsamples each window with language-conditioned queries via local attention → produces 144 local d
…[truncated 5796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Agent",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T01:55:14.758976+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Analyze SpecPrune-VLA paper",
  "prompt": "Fetch and deeply analyze the paper \"SpecPrune-VLA\" (arXiv 2509.05614).\n\nFirst try fetching the HTML version: https://arxiv.org/html/2509.05614\nIf that fails, try the PDF: https://arxiv.org/pdf/2509.05614\n\nUse WebFetch to get the content.\n\nThen provide a DETAILED structured analysis covering ALL of these dimensions:\n\n**A. 使用的 VLA 模型**\n- Specific model names (OpenVLA? SmolVLA? RT-2? other?)\n- Does it include SmolVLA?\n- Model parameter sizes\n\n**B. Vision Connector 类型**\n- pixel-shuffle / MLP projection / cross-attention / other\n- Does it analyze how different connectors affect compression?\n\n**C. 压缩方法核心机制**\n- Training-free or training-required?\n- Specific compression strategy (pruning / pooling / resampling / other)\n- Compression ratio (how many tokens reduced? FLOPs reduction?)\n\n**D. LIBERO 实验数据**\n- Which LIBERO suite (Object/Spatial/Goal/Long)?\n- How many tasks?\n- How many seeds? How many episodes?\n- Specific SR numbers (baseline vs compressed)\n- Error bars / confidence intervals?\n\n**E. 关键问题**\n- Does it analyze cliff-edge phenomenon (pruning causing SR to suddenly collapse to 0%)?\n- Does it do cross-architecture comparison (different vision connectors' pruning effects)?\n- Does it have re-encoding vs deletion control experiments?\n- Does it do closed-loop evaluation (actual execution in simulation, not just action prediction accuracy)?\n\n**F. 与我们工作的差异**\n- Our core finding: pixel-shuffle connector causes 0% SR with any token deletion (cliff-edge), MLP connector shows graceful degradation. Cross-attention re-encoding can recover performance where deletion fails.\n- Does this paper address architecture-dependent compressibility?\n- What would be our unique contribution relative to this paper?\n\nBe thorough - extract specific numbers, table data, and experimental details. Quote relevant passages when possible.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Agent",
  "tool_args": {
    "description": "Analyze SpecPrune-VLA paper",
    "prompt": "Fetch and deeply analyze the paper \"SpecPrune-VLA\" (arXiv 2509.05614).\n\nFirst try fetching the HTML version: https://arxiv.org/html/2509.05614\nIf that fails, try the PDF: https://arxiv.org/pdf/2509.05614\n\nUse WebFetch to get the content.\n\nThen provide a DETAILED structured analysis covering ALL of these dimensions:\n\n**A. 使用的 VLA 模型**\n- Specific model names (OpenVLA? SmolVLA? RT-2? other?)\n- Does it include SmolVLA?\n- Model parameter sizes\n\n**B. Vision Connector 类型**\n- pixel-shuffle / MLP projection / cross-attention / other\n- Does it analyze how different connectors affect compression?\n\n**C. 压缩方法核心机制**\n- Training-free or training-required?\n- Specific compression strategy (pruning / pooling / resampling / other)\n- Compression ratio (how many tokens reduced? FLOPs reduction?)\n\n**D. LIBERO 实验数据**\n- Which LIBERO suite (Object/Spatial/Goal/Long)?\n- How many tasks?\n- How many seeds? How many episodes?\n- Specific SR numbers (baseline vs compressed)\n- Error bars / confidence intervals?\n\n**E. 关键问题**\n- Does it analyze cliff-edge phenomenon (pruning causing SR to suddenly collapse to 0%)?\n- Does it do cross-architecture comparison (different vision connectors' pruning effects)?\n- Does it have re-encoding vs deletion control experiments?\n- Does it do closed-loop evaluation (actual execution in simulation, not just action prediction accuracy)?\n\n**F. 与我们工作的差异**\n- Our core finding: pixel-shuffle connector causes 0% SR with any token deletion (cliff-edge), MLP connector shows graceful degradation. Cross-attention re-encoding can recover performance where deletion fails.\n- Does this paper address architecture-dependent compressibility?\n- What would be our unique contribution relative to this paper?\n\nBe thorough - extract specific numbers, table data, and experimental details. Quote relevant passages when possible.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T01:55:14.759349+00:00_

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
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
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

_source line 15 · 2026-05-19T01:55:14.759485+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T01:55:14.759615+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2509.05614",
  "prompt": "Extract the COMPLETE content of this paper. I need ALL of the following in full detail:\n\n1. ABSTRACT - full text\n2. INTRODUCTION - full text\n3. METHOD section - full description of the compression approach, all technical details\n4. EXPERIMENTS section - ALL tables with numbers, ALL experimental settings (models used, benchmarks, seeds, episodes, metrics), ALL results\n5. RELATED WORK - what prior work is discussed\n6. Any analysis of different VLA architectures (OpenVLA, SmolVLA, RT-2, etc.)\n7. Any discussion of vision connectors (pixel-shuffle, MLP, cross-attention)\n8. Compression ratios, FLOPs reduction numbers\n9. LIBERO benchmark details - which suites, how many tasks, success rates for baseline vs compressed\n10. Any discussion of cliff-edge / sudden collapse in performance when pruning\n11. Whether this is training-free or requires training\n12. Any comparison across different model architectures\n13. All figure and table captions\n14. The conclusion section\n\nPlease be as thorough as possible - extract specific numbers, percentages, and quote key passages verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2509.05614",
    "prompt": "Extract the COMPLETE content of this paper. I need ALL of the following in full detail:\n\n1. ABSTRACT - full text\n2. INTRODUCTION - full text\n3. METHOD section - full description of the compression approach, all technical details\n4. EXPERIMENTS section - ALL tables with numbers, ALL experimental settings (models used, benchmarks, seeds, episodes, metrics), ALL results\n5. RELATED WORK - what prior work is discussed\n6. Any analysis of different VLA architectures (OpenVLA, SmolVLA, RT-2, etc.)\n7. Any discussion of vision connectors (pixel-shuffle, MLP, cross-attention)\n8. Compression ratios, FLOPs reduction numbers\n9. LIBERO benchmark details - which suites, how many tasks, success rates for baseline vs compressed\n10. Any discussion of cliff-edge / sudden collapse in performance when pruning\n11. Whether this is training-free or requires training\n12. Any comparison across different model architectures\n13. All figure and table captions\n14. The conclusion section\n\nPlease be as thorough as possible - extract specific numbers, percentages, and quote key passages verbatim."
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T01:55:14.759961+00:00_

# SpecPrune-VLA: Complete Content Extraction

## 1. ABSTRACT

"Pruning is a typical acceleration technique for compute-bound models by removing computation on unimportant values. Recently, it has been applied to accelerate Vision-Language-Action (VLA) model inference. However, existing acceleration methods focus on local information from the current action step and ignore the global context, leading to >20% success rate drop and limited speedup in some scenarios."

The paper proposes SpecPrune-VLA, a training-free two-level pruning method combining:
- **Action-level static pruning**: leveraging global history and local attention to reduce visual tokens (60-70% reduction)
- **Layer-level dynamic pruning**: adaptive per-layer token importance scoring (additional 20% computation reduction)
- **Lightweight action-aware controller**: classifies actions as coarse or fine-grained based on end-effector speed

Results: "up to 1.57× speedup in LIBERO simulation and 1.70× on real-world tasks, with negligible success rate degradation"

## 2. INTRODUCTION

### Problem Statement
VLA models like RT-1 and OpenVLA are bottlenecked by the LLM backbone, which accounts for ">70% of the end-to-end latency in even the most efficient model." Modern VLAs use single-step paradigm: "the model directly predicts a sequence of low-level actions through a single LLM forward (i.e., only prefill phase) with hundreds of multimodal tokens."

The inference is "primarily compute-bound" per roofline analysis on NVIDIA A800.

### Key Insight
Existing token-pruning methods "only consider local information (e.g., the layer results in current action generation) and ignore global information across the whole model, leading to either >20% success rate loss or limited speedup in some scenarios."

Central observation: "input images in consecutive action generations exhibit high similarity due to the short temporal intervals between them."

## 3. METHODOLOGY

### 3.1 Key Insights

**Insight 1 - What Really Matt
…[truncated 11077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T01:55:14.760150+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2509.05614",
  "prompt": "I need very specific details that may have been missed in a first pass. Please extract:\n\n1. Does the paper mention \"SmolVLA\" anywhere? Search for this exact term.\n2. Does it mention \"pixel-shuffle\" or \"pixel shuffle\" anywhere?\n3. Does it mention \"cross-attention\" as a vision connector type?\n4. What EXACTLY is the vision connector used in OpenVLA-OFT? How are image tokens projected into the LLM? Is there a DinoSiglip encoder? How many visual tokens does each image produce?\n5. How many visual tokens does the baseline model use BEFORE pruning? And after pruning?\n6. For LIBERO experiments: how many seeds? How many episodes per task? How many tasks per suite?\n7. Are there error bars or confidence intervals in ANY table?\n8. Does the paper mention \"architecture-dependent\" compression or discuss that different architectures respond differently to pruning?\n9. What is the exact model size (parameters) of OpenVLA-OFT and pi0?\n10. Does it mention \"re-encoding\" or \"resampler\" or any mechanism to re-encode after token deletion?\n11. What are the exact numbers in Table 1 for ALL methods including SparseVLM?\n12. Does the paper discuss WHY some methods cause >20% SR drop?\n13. Any mention of \"graceful degradation\" vs \"catastrophic failure\" under pruning?\n14. The exact number of visual tokens before and after pruning for each model."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2509.05614",
    "prompt": "I need very specific details that may have been missed in a first pass. Please extract:\n\n1. Does the paper mention \"SmolVLA\" anywhere? Search for this exact term.\n2. Does it mention \"pixel-shuffle\" or \"pixel shuffle\" anywhere?\n3. Does it mention \"cross-attention\" as a vision connector type?\n4. What EXACTLY is the vision connector used in OpenVLA-OFT? How are image tokens projected into the LLM? Is there a DinoSiglip encoder? How many visual tokens does each image produce?\n5. How many visual tokens does the baseline model use BEFORE pruning? And after pruning?\n6. For LIBERO experiments: how many seeds? How many episodes per task? How many tasks per suite?\n7. Are there error bars or confidence intervals in ANY table?\n8. Does the paper mention \"architecture-dependent\" compression or discuss that different architectures respond differently to pruning?\n9. What is the exact model size (parameters) of OpenVLA-OFT and pi0?\n10. Does it mention \"re-encoding\" or \"resampler\" or any mechanism to re-encode after token deletion?\n11. What are the exact numbers in Table 1 for ALL methods including SparseVLM?\n12. Does the paper discuss WHY some methods cause >20% SR drop?\n13. Any mention of \"graceful degradation\" vs \"catastrophic failure\" under pruning?\n14. The exact number of visual tokens before and after pruning for each model."
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T01:55:14.760314+00:00_

# Detailed Analysis of SpecPrune-VLA Paper

## Searches for Specific Terms

1. **"SmolVLA"**: Not mentioned anywhere in the document.

2. **"Pixel-shuffle" or "pixel shuffle"**: Not mentioned in the document.

3. **"Cross-attention" as vision connector**: The paper discusses cross-attention in the context of image-to-text attention patterns but does not explicitly describe a "cross-attention vision connector" architecture.

## Vision Connector & Token Details

4. **Vision connector in OpenVLA-OFT**: The paper does not specify the exact vision encoder or connector mechanism. It mentions that models "process multimodal inputs (e.g., images + text)" but provides no details about DinoSiglip encoders or specific projection layers. The paper states the models receive "two-view images: the third-person view and the wrist view" but does not quantify initial tokens per image.

5. **Visual token counts**: The paper does not explicitly state the baseline number of visual tokens before or after pruning. It reports achieving "60% to 70% visual token" reduction at the beginning of LLM forward, and notes "57% FLOPs reduction" and "52% FLOPs reduction" but does not provide absolute token counts.

## Experimental Setup Details

6. **LIBERO experiments**: The paper does not mention the number of seeds, episodes per task, or tasks per suite. It references "four task suites" (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long) but provides no sample size details.

7. **Error bars or confidence intervals**: No error bars or confidence intervals appear in any tables. Table 1 presents point estimates only.

## Architecture & Model Analysis

8. **Architecture-dependent compression**: The paper does not discuss whether different architectures respond differently to pruning or mention "architecture-dependent" compression explicitly.

9. **Exact model parameters**: The paper does not provide parameter counts for OpenVLA-OFT or π₀.

10. **Re-encoding mechanisms**: No mention of "re-encodi
…[truncated 1223 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T01:55:14.760691+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2509.05614",
  "prompt": "I need to find additional specific details. Please look for:\n\n1. The exact per-suite SR numbers for SparseVLM in Table 1 (Spatial, Object, Goal, Long individually)\n2. Any mention of the number of visual tokens - look for numbers like 256, 512, 576, 729, 1024 tokens\n3. The paper's author list and affiliations\n4. Any references to OpenVLA's architecture - does it say \"7B\" or \"Llama\" or \"Prismatic\"?\n5. For pi0 - what is the LLM backbone? Does it mention PaliGemma, Gemma, or any specific backbone?\n6. Does the paper have a \"Limitations\" section? If so, what does it say?\n7. What is the exact arXiv submission date?\n8. Look for Table 5, Table 6, Table 7, Table 8 - any additional tables beyond Table 1-4?\n9. Does the paper reference or cite EfficientVLA, FastV, SP-VLA? What exactly does it say about each?\n10. Any mention of \"action prediction accuracy\" vs \"closed-loop success rate\" as evaluation metrics?\n11. Does the paper test on SimplerEnv or CALVIN or any benchmark besides LIBERO?\n12. What does the paper say about UniVLA? Is it tested with full LIBERO results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2509.05614",
    "prompt": "I need to find additional specific details. Please look for:\n\n1. The exact per-suite SR numbers for SparseVLM in Table 1 (Spatial, Object, Goal, Long individually)\n2. Any mention of the number of visual tokens - look for numbers like 256, 512, 576, 729, 1024 tokens\n3. The paper's author list and affiliations\n4. Any references to OpenVLA's architecture - does it say \"7B\" or \"Llama\" or \"Prismatic\"?\n5. For pi0 - what is the LLM backbone? Does it mention PaliGemma, Gemma, or any specific backbone?\n6. Does the paper have a \"Limitations\" section? If so, what does it say?\n7. What is the exact arXiv submission date?\n8. Look for Table 5, Table 6, Table 7, Table 8 - any additional tables beyond Table 1-4?\n9. Does the paper reference or cite EfficientVLA, FastV, SP-VLA? What exactly does it say about each?\n10. Any mention of \"action prediction accuracy\" vs \"closed-loop success rate\" as evaluation metrics?\n11. Does the paper test on SimplerEnv or CALVIN or any benchmark besides LIBERO?\n12. What does the paper say about UniVLA? Is it tested with full LIBERO results?"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T01:55:14.760919+00:00_

# SpecPrune-VLA: Document Analysis

## Key Findings

**Authors & Affiliations:**
The paper lists seven authors: Hanzhen Wang, Jiaming Xu, Yushun Xiang, Jiayi Pan, Yongkang Zhou, Yong-Lu Li, and Guohao Dai. Specific institutional affiliations are not detailed in the provided content.

**Model Architectures:**
- **OpenVLA-OFT**: Uses a four-layer MLP as action head for continuous action generation
- **π₀**: Employs flow-matching action expert for processing robot states and actions
- Neither backbone is explicitly named (Llama, PaliGemma specifics not mentioned)

**Visual Token Information:**
The document does not specify exact token counts (256, 512, etc.). It references "hundreds of multimodal tokens" but precise numbers aren't provided.

**Evaluation Metrics:**
The paper measures "success rate" across closed-loop tasks. The document states: "end-to-end evaluation on success rate (SR), latency and speedup."

**Additional Benchmarks Beyond LIBERO:**
- LIBERO-plus (robustness testing with perturbations)
- SimplerEnv (with WidowX-250 robotic arm and UniVLA model)
- Real-world robot tasks (Flexiv Rizon4 arm)

**SparseVLM Performance (Table 1):**
Individual suite results: Spatial 96.8%, Object 94.2%, Goal 97.6%, Long 93.6%

**Limitations Section:**
Not present in the provided excerpt.

**Submission Date:**
arXiv identifier 2509.05614v2 suggests September 2025 submission.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T01:55:14.761075+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/ideas.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/ideas.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T01:55:14.761283+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T01:55:14.761428+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/ROADMAP.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/ROADMAP.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T01:55:14.761547+00:00_

ROADMAP.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T01:55:14.761669+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/memory.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/memory.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T01:55:14.761790+00:00_

memory.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T01:55:14.761914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T01:55:14.762195+00:00_

1	# importance_margin_vla_compress — Research Dashboard
2	
3	> 最后更新: 2026-05-19 01:09 UTC | 更新原因: Round 2 submitted to Review Director, all near-term tasks complete, awaiting review report
4	
5	## 核心方向
6	Architecture-Dependent Token Compressibility in VLAs: pixel_shuffle → cliff-edge (0%), MLP → graded degradation. Cross-attention re-encoding 是核心机制 (+15pp over baseline), 75% 压缩是免费赠品。详见 paper_framing.md。
7	
8	## 当前进展
9	- **Phase**: Round 2 审稿中 — 已提交 Review Director (apr_20260519T010751_de3o)
10	- **全部 4 个 Core Claims 已确认** (D072/D073/D074)
11	- **5 Must-Fix 全解决**: MF1(语言)✅ MF2(official checkpoint)✅ MF3(baseline_control 45.0%)✅ MF4(entropy降级)✅ MF5(CogACT)✅
12	- **新增亮点**: cross-suite generalization, multi-seed robustness, OpenVLA 6-point curve, baseline_control_prune=0%
13	- **论文**: CoRL 2026 官方模板，正文 7 页，consistency check 0 critical
14	- **review_issues.yaml**: 20/20 条 resolved
15	- **GPU**: 全部实验完成，6/6 空闲
16	
17	## 实验结果总览
18	
19	### SmolVLA Cliff-Edge (confirmed across 2 checkpoints)
20	- Fine-tuned: 44.8% baseline, all pruning → 0% (7 conditions + k=0.95)
21	- Official: 59.2% baseline, k=0.5/0.9/0.95 → all 0%
22	- Extended baseline (45.0%): k=0.5 → 0%
23	
24	### OpenVLA Graded Degradation (6-point curve)
25	k=1.0→74%, k=0.95→69.4%, k=0.9→62%, k=0.7→49%, k=0.5→37.4%, k=0.3→20.6%
26	
27	### Smart Compress (cross-attention re-encoding)
28	| M | seed42 | seed43 | Mean |
29	|---|--------|--------|------|
30	| 32 | 61.6% | 59.2% | 60.4% |
31	| 64 | 61.6% | 60.0% | 60.8% |
32	| 96 | 52.6% | 58.2% | 55.4% |
33	| 128 | 59.8% | — | 59.8% |
34	| Extended baseline | 45.0% | — | 45.0% |
35	
36	### Cross-Suite Generalization (M=32, trained on Object only)
37	Object 61.6%, Spatial 53.2%, Goal 56.4% (vs hard pruning 0% on all)
38	
39	## 近期任务
40	- [x] All Must-Fix experiments complete
41	- [x] Fig 2 更新（6-point OpenVLA curve）
42	- [x] Paper Agent 整合全部新结果
43	- [x] Final consistency check + 一致性修复
44	- [x] Submit Round 2 to Review Director
45	- [ ] 等待 Round 2 审稿报告
46	- [ ] 根据报告修复后提交最终版
47
…[truncated 1916 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-19T01:55:14.762466+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T01:55:14.762627+00:00_

1	# Memory
2	
3	## 竞品实验参考
4	（待补充）
5	
6	## 决策与经验
7	
8	### CoRL 2026 模板 (2026-05-18)
9	官方模板是 .sty 文件（非 .cls）。用法：`\documentclass{article}` + `\usepackage{corl_2026}`。
10	- 来源：https://www.corl.org/contributions/instruction-for-authors
11	- 文件：corl_2026.sty, corlabbrvnat.bst
12	- 正文 8 页，References + Appendix 不计
13	- 默认 double-blind + 行号
14	- 投稿平台：OpenReview
15	- 已下载到 artifacts/corl_template/corl_2026_template_submission/
16	
17	### Fig 2 展示方案 (2026-05-18)
18	Director 决策：三条曲线。
19	- SmolVLA (our fine-tuned, 红色实线圆点): k=1.0=44.8%, k=0.95/0.9/0.7/0.5/0.3 全 0%
20	- SmolVLA (official checkpoint, 橙色虚线三角): k=1.0=59.2%, k=0.95=0%, k=0.9=0%, k=0.5=0%
21	- OpenVLA (蓝色实线方块): k=1.0=74%, k=0.7=49%, k=0.5=37.4%, k=0.3=20.6%
22	
23	### Official vs Fine-tuned Baseline 差异 (2026-05-18)
24	Official SmolVLA checkpoint 在 LIBERO-Object 上 SR=59.2%，显著高于我们 fine-tuned baseline 44.8% (+14.4pp)。
25	Smart Compress M=128 passthrough (59.8%) 几乎匹配 official checkpoint——cross-attention re-encoding 将欠优化 baseline 提升到 official 水平。
26	
27	### Official checkpoint cliff-edge 完整确认 (2026-05-18)
28	Official SmolVLA: k=1.0=59.2%, k=0.95=0%, k=0.9=0%, k=0.5=0%。与 fine-tuned model 行为完全一致，cliff-edge 是 pixel-shuffle 架构固有属性。
29	
30	### Normalization 修复经验 (2026-05-18)
31	eval_official_libero.py 在 westd 上调 official checkpoint 时，必须手动做 state normalization 和 action unnormalization。
32	- State: 从 policy_preprocessor_step_5_normalizer_processor.safetensors 加载 mean/std
33	- Action: 从 policy_postprocessor_step_1_unnormalizer_processor.safetensors 加载 mean/std
34	LeRobot 的 prepare_state() 只做 padding，不做 normalization。
35	
36	### WandB 离线模式 (2026-05-18)
37	cqa1-33015 没有 WANDB_API_KEY，训练必须加 WANDB_MODE=offline 环境变量，否则 wandb.init() 失败导致进程退出。
38	
39	### ACIS hook 版本 bug (2026-05-18)
40	cqa1 上旧版 eval_success_rate_libero.py 的 register_acis_hook 有 bug：比较 tokens.shape[1]（单 camera=64）vs mask.shape[1]（双 camera=128），永远不等，hook 被跳过。westd 修复版用 offset 追踪按 camera 分段切片。已同步修复版到 cqa1。
41	
42	### k=0.95 Cliff-edge 确认 (2026-05-18)
43	仅移除 5% tokens (7/128)
…[truncated 865 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T01:55:14.762854+00:00_

Now I have all the information needed for a comprehensive analysis. Here is the detailed structured analysis:

---

## SpecPrune-VLA (arXiv 2509.05614) 深度分析

**论文**: *SpecPrune-VLA: Efficient Two-Level Token Pruning for Vision-Language-Action Models*
**作者**: Hanzhen Wang, Jiaming Xu, Yushun Xiang, Jiayi Pan, Yongkang Zhou, Yong-Lu Li, Guohao Dai
**发表时间**: 2025 年 9 月 (arXiv v2)

---

### A. 使用的 VLA 模型

| 模型 | Action Head | 架构细节 |
|------|------------|---------|
| **OpenVLA-OFT** | 4-layer MLP (continuous action) | 未明确说明 backbone (大概率 Llama-7B + Prismatic vision encoder，但论文未说) |
| **π₀** | Flow-matching action expert | 未明确说明 backbone |
| **UniVLA** | 仅在 SimplerEnv 扩展实验中测试 | 未提供详细架构 |

- **不包含 SmolVLA**。论文全文未出现 "SmolVLA" 一词。
- **不包含 RT-2**。
- 论文未提供任何模型的参数量。

---

### B. Vision Connector 类型

**论文完全没有分析 vision connector 类型。** 以下关键术语均未出现：
- "pixel-shuffle" / "pixel shuffle" — 未提及
- "cross-attention" 作为 vision connector — 未讨论（仅在 attention pattern 分析中出现 "cross-attention" 一词）
- "MLP projection" 作为 connector 类型 — 未区分

论文将视觉编码器视为黑盒，只关注 LLM 层内的 attention pattern，不分析从 vision encoder 到 LLM 的连接方式如何影响压缩效果。

---

### C. 压缩方法核心机制

**Training-free** — 明确声明 "training-free, two-level pruning method"。

**两级剪枝架构**：

1. **Action-level Static Pruning (跨步级)**:
   - 利用前一步推理中 middle+deep layers (第 15/32 层) 的 image-to-text attention 分数识别全局重要 tokens (K_global=30)
   - 帧间 patch 相似度检测变化区域补充动态 tokens (K_dynamic=20)
   - 当前步前两层 attention 补充局部 tokens (K_local=24)
   - 最终保留: V_retain = V_global ∪ V_dynamic ∪ V_local
   - **减少 60-70% 视觉 tokens**

2. **Layer-level Dynamic Pruning (层级)**:
   - 基于 attention entropy 的逐层置信度加权
   - 在指定更新层再剪 10% 最低分 tokens
   - **额外减少约 20% 计算量**

3. **Lightweight Action-Aware Controller**:
   - 根据末端执行器速度将动作分为 coarse/fine-grained
   - 精细动作（接触物体阶段）减少剪枝激进度
   - 速度阈值: v_t^th=0.5, v_r^th=0.2

**压缩比与加速**:

| 模型 | FLOPs 剩余 | A800 加速 | RTX 3090 加速 | 真实机器人加速 |
|------|-----------|----------|-------------|-------------|
| OpenVLA-OFT | 43% | 1.46× | 1.57× | 1.70× |
| π₀ | 48% | 1.31× |
…[truncated 3937 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Agent",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T01:55:14.763037+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Analyze LightVLA paper",
  "prompt": "Fetch and deeply analyze the paper \"LightVLA\" (arXiv 2509.12594).\n\nFirst try fetching the HTML version: https://arxiv.org/html/2509.12594\nIf that fails, try the PDF: https://arxiv.org/pdf/2509.12594\n\nUse WebFetch to get the content.\n\nThen provide a DETAILED structured analysis covering ALL of these dimensions:\n\n**A. 使用的 VLA 模型**\n- Specific model names (OpenVLA? SmolVLA? RT-2? other?)\n- Does it include SmolVLA?\n- Model parameter sizes\n\n**B. Vision Connector 类型**\n- pixel-shuffle / MLP projection / cross-attention / other\n- Does it analyze how different connectors affect compression?\n\n**C. 压缩方法核心机制**\n- Training-free or training-required?\n- Specific compression strategy (pruning / pooling / resampling / other)\n- Compression ratio (how many tokens reduced? FLOPs reduction?)\n\n**D. LIBERO 实验数据**\n- Which LIBERO suite (Object/Spatial/Goal/Long)?\n- How many tasks?\n- How many seeds? How many episodes?\n- Specific SR numbers (baseline vs compressed)\n- Error bars / confidence intervals?\n\n**E. 关键问题**\n- Does it analyze cliff-edge phenomenon (pruning causing SR to suddenly collapse to 0%)?\n- Does it do cross-architecture comparison (different vision connectors' pruning effects)?\n- Does it have re-encoding vs deletion control experiments?\n- Does it do closed-loop evaluation (actual execution in simulation, not just action prediction accuracy)?\n\n**F. 与我们工作的差异**\n- Our core finding: pixel-shuffle connector causes 0% SR with any token deletion (cliff-edge), MLP connector shows graceful degradation. Cross-attention re-encoding can recover performance where deletion fails.\n- Does this paper address architecture-dependent compressibility?\n- What would be our unique contribution relative to this paper?\n\nBe thorough - extract specific numbers, table data, and experimental details. Quote relevant passages when possible.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Agent",
  "tool_args": {
    "description": "Analyze LightVLA paper",
    "prompt": "Fetch and deeply analyze the paper \"LightVLA\" (arXiv 2509.12594).\n\nFirst try fetching the HTML version: https://arxiv.org/html/2509.12594\nIf that fails, try the PDF: https://arxiv.org/pdf/2509.12594\n\nUse WebFetch to get the content.\n\nThen provide a DETAILED structured analysis covering ALL of these dimensions:\n\n**A. 使用的 VLA 模型**\n- Specific model names (OpenVLA? SmolVLA? RT-2? other?)\n- Does it include SmolVLA?\n- Model parameter sizes\n\n**B. Vision Connector 类型**\n- pixel-shuffle / MLP projection / cross-attention / other\n- Does it analyze how different connectors affect compression?\n\n**C. 压缩方法核心机制**\n- Training-free or training-required?\n- Specific compression strategy (pruning / pooling / resampling / other)\n- Compression ratio (how many tokens reduced? FLOPs reduction?)\n\n**D. LIBERO 实验数据**\n- Which LIBERO suite (Object/Spatial/Goal/Long)?\n- How many tasks?\n- How many seeds? How many episodes?\n- Specific SR numbers (baseline vs compressed)\n- Error bars / confidence intervals?\n\n**E. 关键问题**\n- Does it analyze cliff-edge phenomenon (pruning causing SR to suddenly collapse to 0%)?\n- Does it do cross-architecture comparison (different vision connectors' pruning effects)?\n- Does it have re-encoding vs deletion control experiments?\n- Does it do closed-loop evaluation (actual execution in simulation, not just action prediction accuracy)?\n\n**F. 与我们工作的差异**\n- Our core finding: pixel-shuffle connector causes 0% SR with any token deletion (cliff-edge), MLP connector shows graceful degradation. Cross-attention re-encoding can recover performance where deletion fails.\n- Does this paper address architecture-dependent compressibility?\n- What would be our unique contribution relative to this paper?\n\nBe thorough - extract specific numbers, table data, and experimental details. Quote relevant passages when possible.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-19T01:55:14.763270+00:00_

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
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
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

_source line 35 · 2026-05-19T01:55:14.763397+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-19T01:55:14.763529+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2509.12594",
  "prompt": "Extract the COMPLETE content of this paper. I need ALL of the following in full detail:\n\n1. ABSTRACT - full text\n2. INTRODUCTION - full text\n3. METHOD section - complete description of the compression approach, all techniques used\n4. EXPERIMENTS section - ALL tables with numbers, ALL experimental settings (models used, benchmarks, seeds, episodes, error bars), ALL results\n5. Which VLA models are used (OpenVLA, SmolVLA, RT-2, etc.)? List ALL model names and parameter sizes.\n6. What vision connector types are discussed (pixel-shuffle, MLP, cross-attention)?\n7. Is the compression method training-free or training-required?\n8. What compression ratios are achieved? Token reduction numbers? FLOPs reduction?\n9. LIBERO experimental details: which suites (Object/Spatial/Goal/Long), how many tasks, seeds, episodes, specific success rate numbers for baseline vs compressed\n10. Does it discuss cliff-edge phenomenon (sudden collapse to 0% SR)?\n11. Does it compare different vision connector architectures and their effect on compression?\n12. Does it do re-encoding vs deletion experiments?\n13. Is evaluation closed-loop (actual robot/simulation execution) or open-loop (action prediction only)?\n14. Related work section - what prior compression methods are discussed?\n15. Any figures showing token importance or attention patterns\n\nGive me EVERYTHING - every number, every table entry, every experimental detail. Do not summarize or skip anything."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2509.12594",
    "prompt": "Extract the COMPLETE content of this paper. I need ALL of the following in full detail:\n\n1. ABSTRACT - full text\n2. INTRODUCTION - full text\n3. METHOD section - complete description of the compression approach, all techniques used\n4. EXPERIMENTS section - ALL tables with numbers, ALL experimental settings (models used, benchmarks, seeds, episodes, error bars), ALL results\n5. Which VLA models are used (OpenVLA, SmolVLA, RT-2, etc.)? List ALL model names and parameter sizes.\n6. What vision connector types are discussed (pixel-shuffle, MLP, cross-attention)?\n7. Is the compression method training-free or training-required?\n8. What compression ratios are achieved? Token reduction numbers? FLOPs reduction?\n9. LIBERO experimental details: which suites (Object/Spatial/Goal/Long), how many tasks, seeds, episodes, specific success rate numbers for baseline vs compressed\n10. Does it discuss cliff-edge phenomenon (sudden collapse to 0% SR)?\n11. Does it compare different vision connector architectures and their effect on compression?\n12. Does it do re-encoding vs deletion experiments?\n13. Is evaluation closed-loop (actual robot/simulation execution) or open-loop (action prediction only)?\n14. Related work section - what prior compression methods are discussed?\n15. Any figures showing token importance or attention patterns\n\nGive me EVERYTHING - every number, every table entry, every experimental detail. Do not summarize or skip anything."
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-19T01:55:14.763700+00:00_

# Comprehensive Extraction: LightVLA Paper

## 1. ABSTRACT (Complete)

The paper presents LightVLA, a differentiable token pruning framework for vision-language-action models. It addresses deployment challenges on resource-constrained platforms by adaptively pruning visual tokens. The method generates dynamic queries to evaluate token importance and uses Gumbel softmax for differentiable selection. Through fine-tuning, the model learns to preserve informative tokens while pruning non-contributory ones. Key results: "59.1% reduction in FLOPs and 38.2% reduction in latency, with 2.6% improvement in task success rate." The framework requires no heuristic hyperparameters or additional trainable parameters. A variant, LightVLA∗, introduces learnable parameters for comparison.

## 2. INTRODUCTION (Complete)

VLA models combine vision, language, and action generation for robotic tasks, leveraging LLM reasoning capabilities. However, billion-scale parameters and attention-based computational costs prevent real-time deployment on edge devices like household robots and autonomous vehicles.

**Key argument**: "Performance and efficiency are not intrinsically contradictory" because visual sparsity damages both efficiency and performance. By eliminating sparsity, both metrics optimize simultaneously.

The framework uses OpenVLA-OFT as foundation, generating dynamic queries via cross-attention between visual and text tokens, then using Gumbel-softmax for differentiable token selection.

**Main contributions**:
- Empirical demonstration that performance and efficiency optimize collaterally for VLA
- Performance-driven differentiable visual token pruning framework
- State-of-the-art LIBERO results with efficiency gains
- LightVLA∗ as early exploration of learnable query-based pruning

## 3. METHOD SECTION (Complete)

### III-A Problem Definition

VLA decomposition into three components:
- Visual encoder with projector: fv
- LLM backbone: fφ
- Action head: fa

Visual tokens: Hv = fv
…[truncated 11108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-19T01:55:14.763859+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2509.12594",
  "prompt": "I need very specific details from this paper that might have been missed:\n\n1. What is the EXACT vision connector / projector used in OpenVLA-OFT? Is it pixel-shuffle, MLP projection, or something else? Search for terms like \"projector\", \"connector\", \"pixel shuffle\", \"MLP\", \"cross-attention\" in the architecture description.\n\n2. Does the paper discuss or test on ANY other VLA model besides OpenVLA-OFT? Does it apply LightVLA to SmolVLA or any non-OpenVLA model?\n\n3. How many random seeds are used for LIBERO evaluation? Search for \"seed\", \"random\", \"reproducibility\".\n\n4. Are there confidence intervals or standard deviations on the SUCCESS RATE numbers (not just token counts)?\n\n5. Does the paper mention anything about \"cliff-edge\", \"catastrophic\", \"collapse\", \"sudden drop\", \"sharp degradation\" in pruning performance?\n\n6. Does the paper discuss WHY certain pruning methods fail on VLA but work on VLM? Is there any analysis of what makes VLA different from VLM in terms of token importance?\n\n7. What does the paper say about the relationship between pruning ratio and performance? Is there any curve showing performance vs number of tokens retained?\n\n8. Does the paper mention \"re-encoding\", \"reconstruction\", \"recovery\" of pruned information?\n\n9. What specific claim does the paper make about training-free methods vs training-based methods for VLA compression?\n\n10. Quote the paper's exact phrasing about its key insight regarding \"visual sparsity\" and performance.\n\nExtract exact quotes where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2509.12594",
    "prompt": "I need very specific details from this paper that might have been missed:\n\n1. What is the EXACT vision connector / projector used in OpenVLA-OFT? Is it pixel-shuffle, MLP projection, or something else? Search for terms like \"projector\", \"connector\", \"pixel shuffle\", \"MLP\", \"cross-attention\" in the architecture description.\n\n2. Does the paper discuss or test on ANY other VLA model besides OpenVLA-OFT? Does it apply LightVLA to SmolVLA or any non-OpenVLA model?\n\n3. How many random seeds are used for LIBERO evaluation? Search for \"seed\", \"random\", \"reproducibility\".\n\n4. Are there confidence intervals or standard deviations on the SUCCESS RATE numbers (not just token counts)?\n\n5. Does the paper mention anything about \"cliff-edge\", \"catastrophic\", \"collapse\", \"sudden drop\", \"sharp degradation\" in pruning performance?\n\n6. Does the paper discuss WHY certain pruning methods fail on VLA but work on VLM? Is there any analysis of what makes VLA different from VLM in terms of token importance?\n\n7. What does the paper say about the relationship between pruning ratio and performance? Is there any curve showing performance vs number of tokens retained?\n\n8. Does the paper mention \"re-encoding\", \"reconstruction\", \"recovery\" of pruned information?\n\n9. What specific claim does the paper make about training-free methods vs training-based methods for VLA compression?\n\n10. Quote the paper's exact phrasing about its key insight regarding \"visual sparsity\" and performance.\n\nExtract exact quotes where possible."
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T01:55:14.764008+00:00_

# Detailed Analysis of LightVLA Paper

## 1. Vision Connector/Projector Architecture
The paper does NOT specify the exact projector type. It only states that visual tokens are "projected to H_v = f_v(X_I) ∈ ℝ^(L_v×D)" but provides no architectural details about whether this uses pixel-shuffle, MLP, or cross-attention mechanisms.

## 2. Testing on Non-OpenVLA Models
**No.** LightVLA is exclusively evaluated on OpenVLA-OFT. The paper compares *against* other VLA models (SmolVLA, CogACT, π0, etc.) but only applies the pruning method to OpenVLA-OFT. The authors state: "we take OpenVLA-OFT as the foundation model."

## 3. Random Seeds
The paper provides **zero information** about random seeds or reproducibility protocols. No mention of seed values, number of runs, or randomization control.

## 4. Confidence Intervals on Success Rate
**No confidence intervals or standard deviations are reported for success rates.** Table I shows only "90±15 tokens" (token count uncertainty), not performance uncertainty. This is a significant limitation.

## 5. Catastrophic Failure Discussion
The paper does **not** discuss cliff-edge effects or catastrophic performance collapse. It notes token manipulation experiments (Table IV) show "performance degradation" but uses neutral language without discussing sharp drops.

## 6. Why VLM Methods Fail on VLA
The paper provides this analysis: "specialized robotic tasks depends more on local semantics" while "VLMs focuses on global semantics." However, it offers **no detailed mechanistic explanation** of what tokens VLMs vs VLAs prioritize differently.

## 7. Pruning Ratio vs Performance Curve
The paper presents Figure 1 showing "visual tokens vs success rate" but detailed curves showing performance degradation at specific pruning levels are **absent**. Figure 1 only compares final results.

## 8. Reconstruction/Recovery Discussion
**No mention.** The paper does not discuss whether pruned information could theoretically be reconstructed or recovered
…[truncated 680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-19T01:55:14.764794+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2509.12594",
  "prompt": "I need more specific technical details:\n\n1. What is the EXACT architecture of OpenVLA-OFT's vision encoder and projector? The paper must describe this somewhere - look for \"DINOv2\", \"SigLIP\", \"projector\", \"fuse\", \"concatenate\", how the two vision encoders are combined, and how visual tokens are projected to the LLM dimension. Does it mention \"pixel shuffle\" or \"MLP\" anywhere?\n\n2. In Table I, what are the EXACT token numbers for each baseline? For example, SparseVLM says \"100 max\" - what does \"max\" mean? And SP-VLA says \"229 avg\" - what does \"avg\" mean?\n\n3. What is LightVLA* (with the star)? How does it differ from LightVLA? Give complete details.\n\n4. What does the paper say in its LIMITATIONS or CONCLUSION about what it does NOT cover?\n\n5. Does the paper cite or discuss any work on architecture-dependent compression behavior? Any mention of how different model architectures respond differently to the same compression?\n\n6. What are ALL the training-free baselines tested? What are their exact mechanisms?\n\n7. Does the paper discuss the number of LIBERO demonstration trajectories used for training vs testing?\n\n8. What is the paper's publication venue or submission target?\n\n9. Give the complete author list and affiliations.\n\n10. What does Section V (Discussion) say? Complete content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2509.12594",
    "prompt": "I need more specific technical details:\n\n1. What is the EXACT architecture of OpenVLA-OFT's vision encoder and projector? The paper must describe this somewhere - look for \"DINOv2\", \"SigLIP\", \"projector\", \"fuse\", \"concatenate\", how the two vision encoders are combined, and how visual tokens are projected to the LLM dimension. Does it mention \"pixel shuffle\" or \"MLP\" anywhere?\n\n2. In Table I, what are the EXACT token numbers for each baseline? For example, SparseVLM says \"100 max\" - what does \"max\" mean? And SP-VLA says \"229 avg\" - what does \"avg\" mean?\n\n3. What is LightVLA* (with the star)? How does it differ from LightVLA? Give complete details.\n\n4. What does the paper say in its LIMITATIONS or CONCLUSION about what it does NOT cover?\n\n5. Does the paper cite or discuss any work on architecture-dependent compression behavior? Any mention of how different model architectures respond differently to the same compression?\n\n6. What are ALL the training-free baselines tested? What are their exact mechanisms?\n\n7. Does the paper discuss the number of LIBERO demonstration trajectories used for training vs testing?\n\n8. What is the paper's publication venue or submission target?\n\n9. Give the complete author list and affiliations.\n\n10. What does Section V (Discussion) say? Complete content."
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-19T01:55:14.765007+00:00_

# Technical Details from LightVLA Paper

## 1. OpenVLA-OFT Vision Encoder Architecture

The paper states: "the two-branch vision encoder (DINOv2 and SigLIP), LLaMA-2-7B as the language model backbone." However, **the paper does NOT provide specific architectural details** about how these encoders are combined, how they fuse information, or the exact projection mechanism. It mentions initial visual tokens H_v' are "projected to H_v" but omits the projector architecture details (no mention of pixel shuffle, MLP specifics, or concatenation method).

## 2. Token Numbers in Table I

The notation meanings are:
- "max" (SparseVLM: 100 max) indicates maximum retained tokens
- "avg" (SP-VLA: 229 avg) indicates average retained tokens across the dataset

LightVLA reports: "90±15 tokens (Spatial), 78±11 tokens (Object), 64±10 tokens (Goal), 79±11 tokens (Long)" - showing adaptive selection with standard deviations.

## 3. LightVLA* Definition

LightVLA* introduces **learnable query parameters** versus LightVLA's parameter-free approach. Two variants exist:
- **Vision encoder variant**: Learnable queries Q* interact with visual tokens directly
- **Early LLM layer variant**: Queries operate at decoder layer #1-3, incorporating text attention scores via equation: "S† = LN(Q†)·LN(H_v^T) + ζ·attn"

Results show LightVLA* achieves 97.0% average success (layer #1 variant best for long-horizon tasks).

## 4. Limitations/Conclusion Coverage

The conclusion states future work targets "visual redundancy in end-to-end VLMs for autonomous driving" and "complicated spatial intelligence tasks." **The paper does NOT explicitly discuss limitations** in a dedicated section.

## 5. Architecture-Dependent Compression Behavior

**Not discussed.** The paper focuses solely on VLA application without examining how different architectures respond differentially to pruning.

## 6. Training-Free Baselines

Five training-free methods tested: FlashVLA, SP-VLA, VLA-cache, FastV, SparseVLM. All use **fixed 
…[truncated 1079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-19T01:55:14.765351+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2409.11895",
  "prompt": "This is the OpenVLA-OFT paper (or the OpenVLA paper). I need to know:\n1. What vision connector/projector does OpenVLA use? Is it pixel-shuffle, MLP, cross-attention, or something else?\n2. How are DINOv2 and SigLIP features combined?\n3. How many visual tokens does OpenVLA produce (before and after projection)?\n4. What is the exact projector architecture?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2409.11895",
    "prompt": "This is the OpenVLA-OFT paper (or the OpenVLA paper). I need to know:\n1. What vision connector/projector does OpenVLA use? Is it pixel-shuffle, MLP, cross-attention, or something else?\n2. How are DINOv2 and SigLIP features combined?\n3. How many visual tokens does OpenVLA produce (before and after projection)?\n4. What is the exact projector architecture?"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-19T01:55:14.765724+00:00_

I've reviewed the provided document, but it doesn't contain information about OpenVLA, vision connectors, DINOv2, SigLIP features, or visual token projections.

The document is a scientific paper titled "On the Euler–type gravitomagnetic orbital effects in the field of a precessing body" by Lorenzo Iorio. It discusses general relativistic effects on orbital mechanics, with applications to systems like the Juno spacecraft orbiting Jupiter and the double pulsar PSR J0737–3039 A/B.

To answer your questions about OpenVLA's architecture, vision connectors, and feature combination methods, you would need to provide the actual OpenVLA paper or documentation rather than this gravitational physics manuscript.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-19T01:55:14.765999+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2501.01811",
  "prompt": "This should be the OpenVLA-OFT paper. What vision connector/projector does it use? Is it pixel-shuffle, MLP projection, or something else? How many visual tokens does it produce? How are DINOv2 and SigLIP combined?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2501.01811",
    "prompt": "This should be the OpenVLA-OFT paper. What vision connector/projector does it use? Is it pixel-shuffle, MLP projection, or something else? How many visual tokens does it produce? How are DINOv2 and SigLIP combined?"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-19T01:55:14.766347+00:00_

I appreciate your question, but the webpage content provided does not contain information about OpenVLA-OFT or any vision connector/projector architecture. 

The page is an arXiv abstract for **QuantumBind-RBFE**, a paper about "Accurate Relative Binding Free Energy Calculations Using Neural Network Potentials" in computational chemistry and drug discovery. It discusses protein-ligand binding predictions using neural network potentials (specifically AceFF 1.0), not vision-language models.

To answer your questions about OpenVLA-OFT's vision connector, token production, and how DINOv2 and SigLIP are combined, you would need to provide the actual OpenVLA-OFT paper or relevant documentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-19T01:55:14.766497+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.11564",
  "prompt": "Is this the OpenVLA-OFT paper? If so, what vision projector/connector does it use? How are DINOv2 and SigLIP features combined? How many visual tokens? Is it pixel-shuffle or MLP?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2410.11564",
    "prompt": "Is this the OpenVLA-OFT paper? If so, what vision projector/connector does it use? How are DINOv2 and SigLIP features combined? How many visual tokens? Is it pixel-shuffle or MLP?"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-19T01:55:14.766714+00:00_

# Response

No, this is not the OpenVLA-OFT paper. The document describes **PAVLM** (Point cloud Affordance Vision-Language Model), which focuses on "identifying actionable regions on 3D objects" using point clouds and language models.

The paper centers on a different approach: it "integrates a geometric-guided propagation module with hidden embeddings from large language models (LLMs)" and uses Llama-3.1 for context-aware text generation.

The specific technical details you're asking about—vision projectors, DINOv2/SigLIP feature combination methods, visual token counts, and pixel-shuffle vs. MLP architectures—are not addressed in this abstract or metadata. You would need to consult the full paper PDF to find those implementation details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-19T01:55:14.767026+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2501.12428",
  "prompt": "Is this the Fine-Tuning OpenVLA / OpenVLA-OFT paper? What vision projector/connector does OpenVLA-OFT use? How are DINOv2 and SigLIP combined? How many visual tokens?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2501.12428",
    "prompt": "Is this the Fine-Tuning OpenVLA / OpenVLA-OFT paper? What vision projector/connector does OpenVLA-OFT use? How are DINOv2 and SigLIP combined? How many visual tokens?"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-19T01:55:14.767200+00:00_

Based on the provided content, this is **not** the Fine-Tuning OpenVLA/OpenVLA-OFT paper.

The webpage describes **SplitQuant**, a paper about neural network quantization by Jaewoo Song and Fangzhen Lin. The abstract explains that it addresses low-bit quantization challenges by "splitting each quantizable layer into three mathematically equivalent layers and applies different scaling factors."

This paper focuses on quantization techniques for deep neural networks (particularly BERT models), not on vision language models or visual projectors like OpenVLA. Therefore, your questions about vision projectors, DINOv2, SigLIP combinations, and visual token counts are not applicable to this document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-19T01:55:14.767375+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2409.11895",
  "prompt": "What is the title of this paper? Is it about OpenVLA?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2409.11895",
    "prompt": "What is the title of this paper? Is it about OpenVLA?"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-19T01:55:14.767498+00:00_

# Paper Title and Subject Matter

The title of this paper is **"On the Euler-type gravitomagnetic orbital effects in the field of a precessing body"**.

No, this paper is not about OpenVLA. Instead, it focuses on gravitational physics and general relativity. The research examines how time-dependent gravitomagnetic effects influence orbital motion when a rotating celestial body experiences precession of its spin angular momentum. The author analyzes applications to real systems including Jupiter's Juno spacecraft and the double pulsar PSR J0737-3039 A/B, as well as theoretical scenarios involving supermassive black holes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-19T01:55:14.767627+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.07000",
  "prompt": "Is this the OpenVLA paper? What vision projector/connector does it use? How are DINOv2 and SigLIP combined? How many visual tokens does OpenVLA produce? Is it pixel-shuffle or MLP?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2407.07000",
    "prompt": "Is this the OpenVLA paper? What vision projector/connector does it use? How are DINOv2 and SigLIP combined? How many visual tokens does OpenVLA produce? Is it pixel-shuffle or MLP?"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-19T01:55:14.767751+00:00_

No, this is not the OpenVLA paper. The document describes **Etalon**, which is "a comprehensive performance evaluation framework" for LLM inference systems. It focuses on evaluating metrics like latency, throughput, and introduces a "fluidity-index" metric to assess user-facing performance in real-time LLM applications.

Etalon is entirely different from OpenVLA (Open Vision Language Assistant), which concerns multimodal AI systems combining vision and language capabilities. The web page contains no information about vision projectors, DINO, SigLIP, visual tokens, or pixel-shuffle implementations—it addresses only LLM inference evaluation metrics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-19T01:55:14.768031+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/search/?searchtype=all&query=OpenVLA+open+x+embodiment",
  "prompt": "Find the arXiv paper IDs for OpenVLA and OpenVLA-OFT. List their titles, authors, and arXiv IDs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/search/?searchtype=all&query=OpenVLA+open+x+embodiment",
    "prompt": "Find the arXiv paper IDs for OpenVLA and OpenVLA-OFT. List their titles, authors, and arXiv IDs."
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-19T01:55:14.768305+00:00_

# OpenVLA Papers

## OpenVLA

**arXiv ID:** 2406.09246

**Title:** "OpenVLA: An Open-Source Vision-Language-Action Model"

**Authors:** Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, Ashwin Balakrishna, Suraj Nair, Rafael Rafailov, Ethan Foster, Grace Lam, Pannag Sanketi, Quan Vuong, Thomas Kollar, Benjamin Burchfiel, Russ Tedrake, Dorsa Sadigh, Sergey Levine, Percy Liang, Chelsea Finn

---

## OpenVLA-OFT

I could not locate a paper specifically titled "OpenVLA-OFT" in the search results provided. The results include the original OpenVLA paper and five other papers that reference or build upon OpenVLA, but none are explicitly labeled as "OpenVLA-OFT." 

If you're looking for a specific paper on fine-tuning methods for OpenVLA, the original OpenVLA paper does discuss efficient fine-tuning techniques, but there is no separate "OFT" variant listed in these results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-19T01:55:14.768503+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.09246",
  "prompt": "What vision projector/connector does OpenVLA use? Is it pixel-shuffle, MLP projection, or cross-attention? How are DINOv2 and SigLIP features combined? How many visual tokens does OpenVLA produce? Give all architectural details about the vision encoding pipeline."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2406.09246",
    "prompt": "What vision projector/connector does OpenVLA use? Is it pixel-shuffle, MLP projection, or cross-attention? How are DINOv2 and SigLIP features combined? How many visual tokens does OpenVLA produce? Give all architectural details about the vision encoding pipeline."
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-19T01:55:14.768663+00:00_

# OpenVLA Vision Encoding Architecture

Based on the provided arXiv abstract, specific architectural details about the vision projector/connector type, feature fusion mechanism, and visual token count are **not disclosed**.

The abstract only states that OpenVLA uses "a visual encoder that fuses pretrained features from DINOv2 and SigLIP," but does not specify:

- Whether pixel-shuffle, MLP projection, or cross-attention is employed
- The exact method for combining the two feature sources
- The number of visual tokens produced

To obtain these architectural specifics, you would need to consult the full paper (available via the PDF link) or the project's technical documentation at the website referenced: openvla.github.io.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-19T01:55:14.768821+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2406.09246",
  "prompt": "I need the EXACT architecture details of OpenVLA's vision encoder and projector:\n1. How are DINOv2 and SigLIP features combined/fused?\n2. What projector maps visual features to the LLM input space? Is it an MLP, pixel-shuffle, cross-attention, or something else?\n3. How many visual tokens does OpenVLA produce?\n4. What is the spatial resolution of the visual features?\nSearch for \"projector\", \"pixel\", \"shuffle\", \"MLP\", \"linear\", \"projection\", \"fuse\", \"concatenate\", \"tokens\" in the architecture description."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2406.09246",
    "prompt": "I need the EXACT architecture details of OpenVLA's vision encoder and projector:\n1. How are DINOv2 and SigLIP features combined/fused?\n2. What projector maps visual features to the LLM input space? Is it an MLP, pixel-shuffle, cross-attention, or something else?\n3. How many visual tokens does OpenVLA produce?\n4. What is the spatial resolution of the visual features?\nSearch for \"projector\", \"pixel\", \"shuffle\", \"MLP\", \"linear\", \"projection\", \"fuse\", \"concatenate\", \"tokens\" in the architecture description."
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-19T01:55:14.768979+00:00_

# OpenVLA Vision Encoder Architecture Details

Based on the provided document, here are the specific architectural details:

## Feature Fusion
The vision encoder combines two pretrained models: "input image patches are passed separately through both encoders and the resulting feature vectors are concatenated channel-wise." This describes how DINOv2 and SigLIP features are merged together.

## Projector Component
The document specifies that Prismatic (OpenVLA's backbone) uses "a small 2-layer MLP projector" that "takes the output embeddings of the visual encoder and maps them into the input space of a language model."

## Visual Token Count
The paper states that the visual encoder produces "a number of 'image patch embeddings'," but does not specify an exact token count in the provided excerpt.

## Spatial Resolution
For input images, the team "compared VLAs with 224×224px and 384×384px inputs" and selected 224×224 pixels for the final model, finding "no performance difference in our evaluations" while the higher resolution "takes 3x longer to train."

## Key Design Choice
The combination of spatial reasoning from DINOv2 with semantic features from SigLIP was deliberately chosen because "the addition of DinoV2 features has been shown to be helpful for improved spatial reasoning, which can be particularly helpful for robot control."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-19T01:55:14.769431+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/search/?searchtype=all&query=OpenVLA-OFT+fine-tuning",
  "prompt": "Find the arXiv paper for OpenVLA-OFT. List its title, arXiv ID, and authors."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/search/?searchtype=all&query=OpenVLA-OFT+fine-tuning",
    "prompt": "Find the arXiv paper for OpenVLA-OFT. List its title, arXiv ID, and authors."
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-19T01:55:14.769630+00:00_

# OpenVLA-OFT Paper

**Title:** "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success"

**arXiv ID:** 2502.19645

**Authors:** Moo Jin Kim, Chelsea Finn, Percy Liang

This paper introduces OpenVLA-OFT, which the authors describe as an "Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective." The work demonstrates significant improvements on robotic manipulation benchmarks, achieving a 97.1% success rate on LIBERO simulation tasks compared to OpenVLA's baseline of 76.5%.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-19T01:55:14.769783+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2502.19645",
  "prompt": "I need the specific architecture details of OpenVLA-OFT:\n1. Does it change the vision projector from the original OpenVLA? \n2. What is the projector type - MLP, pixel-shuffle, cross-attention?\n3. How many visual tokens does it produce? The LightVLA paper says OpenVLA-OFT has 512 visual tokens, while original OpenVLA has 256. What changed?\n4. Does it change the image resolution? From 224 to something higher?\n5. Any changes to the vision encoder (DINOv2 + SigLIP)?\n\nSearch for \"projector\", \"pixel\", \"token\", \"resolution\", \"encoder\", \"visual\" in the text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2502.19645",
    "prompt": "I need the specific architecture details of OpenVLA-OFT:\n1. Does it change the vision projector from the original OpenVLA? \n2. What is the projector type - MLP, pixel-shuffle, cross-attention?\n3. How many visual tokens does it produce? The LightVLA paper says OpenVLA-OFT has 512 visual tokens, while original OpenVLA has 256. What changed?\n4. Does it change the image resolution? From 224 to something higher?\n5. Any changes to the vision encoder (DINOv2 + SigLIP)?\n\nSearch for \"projector\", \"pixel\", \"token\", \"resolution\", \"encoder\", \"visual\" in the text."
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-19T01:55:14.769922+00:00_

# OpenVLA-OFT Architecture Details

Based on the paper, here are the key architectural specifics:

## Vision Projector
OpenVLA-OFT **retains the original projector design**. The document states: "These projected features are concatenated with language embeddings along the sequence dimension before being processed by the Llama-2 decoder."

The projector remains a **3-layer MLP with GELU activation**, identical to base OpenVLA.

## Visual Token Count
The 512 visual token figure comes from **multiple input images**, not architectural changes:

Original OpenVLA: 256 patch embeddings (single third-person camera)

OpenVLA-OFT with multiple cameras: "512 patch embeddings" arise from adding a wrist camera, effectively doubling inputs rather than changing the per-image projection.

The paper confirms: "Each query processes a 224 x 224 px image and a LIBERO task command" — **no resolution changes**.

## Vision Encoders
No modifications to the fused backbone. The system uses the original "SigLIP and DINOv2 vision transformers" unchanged, with FiLM conditioning applied *after* encoding for the ALOHA variant (OFT+).

## Summary
OpenVLA-OFT's efficiency gains stem from **algorithmic changes** (parallel decoding, continuous actions, L1 regression) rather than architectural modifications to the vision pathway. The flexibility to process additional inputs is enabled by excess computational capacity from improved action generation, not vision architecture redesign.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-19T01:55:14.770072+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-19T01:55:14.770248+00:00_

artifacts/.venv/lib/python3.14/site-packages/torchgen/packaged/autograd/README.md
artifacts/architecture_report.md
task_context/history/reviewer/loop_1.md
task_context/history/director/loop_1.md
task_context/history/agent/loop_1.md
task_context/history/agent/loop_1_1778878965.md
task_context/history/director/loop_2.md
task_context/history/agent/loop_2.md
task_context/history/director/loop_3.md
task_context/history/reviewer/loop_2.md
task_context/history/agent/loop_2_1778890120.md
task_context/history/agent/loop_3.md
task_context/history/agent/loop_3_1778900113.md
.claude/sessions/agent_175a0fc4/CLAUDE.md
.claude/sessions/agent_175a0fc4/AGENTS.md
task_context/history/agent/loop_2_1778903096.md
task_context/history/agent/loop_4.md
.claude/sessions/agent_567a8628/CLAUDE.md
.claude/sessions/agent_567a8628/AGENTS.md
task_context/history/reviewer/loop_3.md
task_context/history/director/loop_4.md
task_context/history/agent/loop_4_1778929745.md
.claude/sessions/agent_117c0105/CLAUDE.md
.claude/sessions/agent_117c0105/AGENTS.md
artifacts/mvp_imm_v8b_twostage/diagnosis.md
docs/IDEA_BRIEF.md
artifacts/dream_reports/dream_20260516T075046/best/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/median/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/median/review_report.md
artifacts/dream_reports/dream_20260516T075046/best/review_report.md
artifacts/dream_reports/dream_20260516T075046/worst/review_report.md
task_context/history/reviewer/loop_4.md
task_context/history/director/loop_5.md
task_context/history/agent/loop_5.md
artifacts/research_lora_mode_collapse_fix.md
task_context/history/reviewer/loop_5.md
task_context/history/agent/loop_5_1778944487.md
task_context/history/agent/loop_6.md
task_context/history/director/loop_6.md
artifacts/_project/chart/paper_figures_v1.md
task_context/history/reviewer/loop_6.md
task_context/history/agent/loop_7.md
.claude/sessions/agent_a95c4df4/CLAUDE.
…[truncated 2473 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-19T01:55:14.770489+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/IDEA_BRIEF.md"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-19T01:55:14.770956+00:00_

1	# Idea Brief: Mind the Gap: Importance Margin Maximization for Adversarially Robust VLA Token Compression
2	
3	
4	- **Idea ID**: `idea_008`
5	- **Created**: 2026-05-15
6	- **Approved**: 2026-05-15
7	- **Source**: foreign:be-prod-0510
8	- **Level**: top-tier
9	- **Target Venues**: CoRL 2026 (abstract May 26, paper May 29 — very tight at 12 days out; feasible only if implementation starts immediately and theory section can reuse the straightforward margin bound; ideal topical fit for VLA robustness), AAAI 2027 (deadline expected ~August 2026 — comfortable timeline for complete experiments, ablations, and theory polish; supports theoretical + empirical contributions), ICLR 2027 (deadline expected ~October 2026 — full scope with extended experiments on OpenVLA and additional compression methods; top-tier venue)
10	
11	## Seed Topic
12	
13	按照以下方向，生成1-2个优质idea，保质不求量：Token-Level Representation Surgery for VLA Robustness
14	Target: CoRL 2026 (Austin, Nov 9–12, 2026). Abstract deadline 2026-05-26 (12 days from today 2026-05-14); paper deadline 2026-05-29 (15 days).
15	Direction: Token pruning and augmentation in VLA visual representations — methods that surgically manipulate visual tokens in latent space to improve VLA generalization under realistic perturbations. The core theoretical insight is that VLA visual encoders produce highly redundant token sequences where task-irrelevant tokens (background clutter, static scene regions, occluded areas) dominate attention budgets and create brittle feature correlations. By pruning uninformative tokens and augmenting critical ones in representation space (not pixel space), we compress the effective visual input to a task-relevant manifold that is inherently more robust to distribution shift. Theoretical grounding includes: (1) Information Bottleneck — pruning enforces a tighter bottleneck that retains only task-sufficient statistics, provably improving generalization bounds; (2) Attention Entropy Reduction — concentrating attentio
…[truncated 22685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-19T01:55:14.771804+00:00_

Now I have all the information needed for a comprehensive analysis. Here is the detailed structured analysis:

---

## LightVLA (arXiv 2509.12594) -- Detailed Analysis

**Title**: LightVLA: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning  
**Authors**: Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, Xianpeng Lang  
**Affiliations**: LiAuto Inc., Tsinghua University, Chinese Academy of Sciences  
**Status**: arXiv preprint (2509.12594v2); listed as "ICRA 2026" in your IDEA_BRIEF

---

### A. 使用的 VLA 模型

- **实验对象（应用 LightVLA 的模型）**: 仅 **OpenVLA-OFT (7B)**。LightVLA 没有在任何其他 VLA 上验证。
- **对比 baseline（仅引用数据，未施加 LightVLA）**: OpenVLA (7B), SmolVLA (2.25B), CogACT (7B), π0 (3.3B), π0-fast (3.3B), NORA (3B), NORA-Long (3B), WorldVLA (7B)
- **SmolVLA**: 仅作为 Table I 中的对比项出现（SR=88.8%），**未在 SmolVLA 上测试 LightVLA 的压缩方法**
- **参数规模**: 基础模型 OpenVLA-OFT 7B（LLaMA-2-7B backbone + DINOv2 + SigLIP 双分支视觉编码器）

### B. Vision Connector 类型

- OpenVLA / OpenVLA-OFT 使用 **MLP projector**（原始 OpenVLA 为 2-layer MLP，OpenVLA-OFT 为 3-layer MLP with GELU activation）
- DINOv2 和 SigLIP 的特征通过 **channel-wise concatenation** 融合，然后经 MLP projector 映射到 LLM 输入空间
- OpenVLA-OFT 的 512 tokens 来自 **双摄像头**（第三人称 + 腕部），每个 224x224 图像产生 256 patch embeddings
- **论文完全没有分析不同 vision connector 对压缩的影响**。没有 pixel-shuffle vs MLP vs cross-attention 的对比实验。只在单一 MLP projector 架构上做了实验。

### C. 压缩方法核心机制

- **Training-required**：需要 40,000 gradient steps 微调（8x H20 GPU, batch size 64）
- **核心策略**：Differentiable token pruning via Gumbel-Softmax
  1. **Query Generation (parameter-free)**：通过 visual tokens 和 language tokens 的 cross-attention 生成 query：`Q = softmax(Hv·Hl^T / √D) · Hl`
  2. **Token Scoring**：`S = Q·Hv^T / √D`，每个 query 对每个 token 打分
  3. **Differentiable Selection**：用 Gumbel-Softmax（带衰减噪声 α）实现可微 argmax，训练时 straight-through estimator，推理时直接 argmax
- **压缩比**：
  - Token: 512 → 78 avg (84.8% reduction)，按任务变化：Spatial 90±15, Object 78±11, Goal 64±10, Long 7
…[truncated 3821 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Agent",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-19T01:55:14.772008+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Find and analyze See What Matters",
  "prompt": "Find and analyze the paper \"See What Matters: Differentiable Grid Sample Pruning for Vision-Language-Action Models\" (ICML 2026, no arXiv).\n\nStep 1: Use WebSearch to find the paper. Search for:\n- \"See What Matters Differentiable Grid Sample Pruning Vision-Language-Action\"\n- Try variations if needed\n\nStep 2: Once you find a link (could be OpenReview, project page, or other), use WebFetch to get the full paper content.\n\nStep 3: Provide a DETAILED structured analysis covering ALL of these dimensions:\n\n**A. 使用的 VLA 模型**\n- Specific model names (OpenVLA? SmolVLA? RT-2? other?)\n- Does it include SmolVLA?\n- Model parameter sizes\n\n**B. Vision Connector 类型**\n- pixel-shuffle / MLP projection / cross-attention / other\n- Does it analyze how different connectors affect compression?\n\n**C. 压缩方法核心机制**\n- Training-free or training-required?\n- Specific compression strategy (pruning / pooling / resampling / other)\n- Compression ratio (how many tokens reduced? FLOPs reduction?)\n\n**D. LIBERO 实验数据**\n- Which LIBERO suite (Object/Spatial/Goal/Long)?\n- How many tasks?\n- How many seeds? How many episodes?\n- Specific SR numbers (baseline vs compressed)\n- Error bars / confidence intervals?\n\n**E. 关键问题**\n- Does it analyze cliff-edge phenomenon (pruning causing SR to suddenly collapse to 0%)?\n- Does it do cross-architecture comparison (different vision connectors' pruning effects)?\n- Does it have re-encoding vs deletion control experiments?\n- Does it do closed-loop evaluation (actual execution in simulation, not just action prediction accuracy)?\n\n**F. 与我们工作的差异**\n- Our core finding: pixel-shuffle connector causes 0% SR with any token deletion (cliff-edge), MLP connector shows graceful degradation. Cross-attention re-encoding can recover performance where deletion fails.\n- Does this paper address architecture-dependent compressibility?\n- What would be our unique contribution relative to this paper?\n\nBe thorough - extract specific numbers, table data, and experimental details.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Agent",
  "tool_args": {
    "description": "Find and analyze See What Matters",
    "prompt": "Find and analyze the paper \"See What Matters: Differentiable Grid Sample Pruning for Vision-Language-Action Models\" (ICML 2026, no arXiv).\n\nStep 1: Use WebSearch to find the paper. Search for:\n- \"See What Matters Differentiable Grid Sample Pruning Vision-Language-Action\"\n- Try variations if needed\n\nStep 2: Once you find a link (could be OpenReview, project page, or other), use WebFetch to get the full paper content.\n\nStep 3: Provide a DETAILED structured analysis covering ALL of these dimensions:\n\n**A. 使用的 VLA 模型**\n- Specific model names (OpenVLA? SmolVLA? RT-2? other?)\n- Does it include SmolVLA?\n- Model parameter sizes\n\n**B. Vision Connector 类型**\n- pixel-shuffle / MLP projection / cross-attention / other\n- Does it analyze how different connectors affect compression?\n\n**C. 压缩方法核心机制**\n- Training-free or training-required?\n- Specific compression strategy (pruning / pooling / resampling / other)\n- Compression ratio (how many tokens reduced? FLOPs reduction?)\n\n**D. LIBERO 实验数据**\n- Which LIBERO suite (Object/Spatial/Goal/Long)?\n- How many tasks?\n- How many seeds? How many episodes?\n- Specific SR numbers (baseline vs compressed)\n- Error bars / confidence intervals?\n\n**E. 关键问题**\n- Does it analyze cliff-edge phenomenon (pruning causing SR to suddenly collapse to 0%)?\n- Does it do cross-architecture comparison (different vision connectors' pruning effects)?\n- Does it have re-encoding vs deletion control experiments?\n- Does it do closed-loop evaluation (actual execution in simulation, not just action prediction accuracy)?\n\n**F. 与我们工作的差异**\n- Our core finding: pixel-shuffle connector causes 0% SR with any token deletion (cliff-edge), MLP connector shows graceful degradation. Cross-attention re-encoding can recover performance where deletion fails.\n- Does this paper address architecture-dependent compressibility?\n- What would be our unique contribution relative to this paper?\n\nBe thorough - extract specific numbers, table data, and experimental details.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-19T01:55:14.772492+00:00_

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
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
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

_source line 71 · 2026-05-19T01:55:14.772666+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-19T01:55:14.772806+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "See What Matters Differentiable Grid Sample Pruning Vision-Language-Action Models ICML 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "tool_args": {
    "query": "See What Matters Differentiable Grid Sample Pruning Vision-Language-Action Models ICML 2026"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-19T01:55:14.772940+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"See What Matters\" \"Grid Sample Pruning\" VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"See What Matters\" \"Grid Sample Pruning\" VLA"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-19T01:55:14.773069+00:00_

Web search results for query: ""See What Matters" "Grid Sample Pruning" VLA"

Links: [{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/pdf/2510.08464"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/pdf/2509.05614"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.22991"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/pdf/2511.16449"},{"title":"SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models","url":"https://arxiv.org/pdf/2509.09090"}]

Based on the search results, I found information about "See What Matters" and Grid Sample Pruning for VLA models:

The paper addresses how Vision-Language-Action (VLA) models, which show remarkable promise in robotics manipulation, suffer from high computational costs that hinder real-time deployment, and existing token pruning methods face a fundamental trade-off where aggressive compression discards critical geometric details like contact points, leading to severe performance degradation.

The paper proposes the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA by adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, preserving essential sp
…[truncated 422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-19T01:55:14.773311+00:00_

Web search results for query: "See What Matters Differentiable Grid Sample Pruning Vision-Language-Action Models ICML 2026"

Links: [{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models","url":"https://arxiv.org/pdf/2601.16065"},{"title":"Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation","url":"https://arxiv.org/pdf/2509.22093"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/pdf/2509.05614"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/pdf/2511.16449"}]

Based on the search results, I found information about "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Models" presented at ICML 2026:

The paper proposes the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA (Vision-Language-Action models).

The work addresses a fundamental trade-off in existing token pruning methods: aggressive compression inevitably discards critical geometric details like contact points, leading to severe performance degradation. The authors argue that breaking this trade-off requires rethinking compression as a geometry-aware, continuous token resampling in the vision encoder.

By adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, GridS preserves essential spatial information while achieving
…[truncated 272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-19T01:55:14.773470+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://icml.cc/virtual/2026/poster/65010",
  "prompt": "Extract ALL information about this paper: title, authors, abstract, any links to PDF/OpenReview/project page/code. Get every detail available on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://icml.cc/virtual/2026/poster/65010",
    "prompt": "Extract ALL information about this paper: title, authors, abstract, any links to PDF/OpenReview/project page/code. Get every detail available on this page."
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-19T01:55:14.773611+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Differentiable Grid Sampler\" GridS VLA OpenReview ICML 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Differentiable Grid Sampler\" GridS VLA OpenReview ICML 2026"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-19T01:55:14.773744+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"See What Matters\" VLA pruning OpenVLA SmolVLA LIBERO experiment results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"See What Matters\" VLA pruning OpenVLA SmolVLA LIBERO experiment results"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-19T01:55:14.773872+00:00_

# Paper Information

**Title:** "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model"

**Conference:** ICML 2026 (Poster)

**Authors:** Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu

**Abstract Summary:**
The researchers propose GridS (Differentiable Grid Sampler), a module designed to reduce computational costs in Vision-Language-Action models for robotics. Rather than discarding tokens, their approach performs "task-aware, continuous resampling of visual tokens" by predicting salient coordinates and using differentiable interpolation. The method achieves "a 76% reduction in FLOPs with no degradation in the success rate" while using fewer than 10% of original visual tokens.

**Available Links:**
- **Project Page:** https://fediory.github.io/Grid-Sampler/

**Additional Notes:**
The page indicates that "Log in and register to view live content," suggesting a PDF or additional materials may be available through ICML's registration system. No direct PDF, OpenReview, or code repository links appear on this landing page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-19T01:55:14.774008+00:00_

Web search results for query: ""Differentiable Grid Sampler" GridS VLA OpenReview ICML 2026"

Links: [{"title":"ICML 2026 Workshop | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop"},{"title":"ICML 2026 | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026"},{"title":"ICML 2026 Workshop FMSD | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FFMSD"},{"title":"Determinantal point process attention over grid cell code supports out of distribution generalization","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11293867/"},{"title":"ICLR 2026 Conference Submissions","url":"https://openreview.net/submissions?page=618&venue=ICLR.cc/2026/Conference"},{"title":"Gaussian Process Inference Reveals Non-separability of Position and Velocity Tuning in Grid Cells","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12889529/"},{"title":"ICML | OpenReview","url":"https://openreview.net/group?id=ICML.cc"},{"title":"GridSample: an R package to generate household survey primary sampling units (PSUs) from gridded population data","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5518145/"},{"title":"Differential Locally Injective Grid Deformation and Optimization","url":"https://arxiv.org/pdf/2601.04494"},{"title":"Robust variability of grid cell properties within individual grid modules enhances encoding of local space","url":"https://www.biorxiv.org/content/10.1101/2024.02.27.582373.full.pdf"}]

The search results don't contain specific information about "Differentiable Grid Sampler" (GridS) for VLA on OpenReview at ICML 2026. The results show general OpenReview pages for ICML 2026 and some unrelated papers about grid cells in neuroscience and grid-based computational methods, but not the specific paper or work you're looking for.

It's possible that:
1. The paper may not yet be published or indexed on OpenReview
2. The exact title or authors may be slightly different
3. It may be under a different venue o
…[truncated 281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-19T01:55:14.774184+00:00_

Web search results for query: ""See What Matters" VLA pruning OpenVLA SmolVLA LIBERO experiment results"

Links: [{"title":"VLA Models Compared: OpenVLA vs π0 vs SmolVLA vs RT-2 (2026 Guide) | SVRC","url":"https://www.roboticscenter.ai/learn/vla-models-comparison"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://gluestick-vla.github.io/"},{"title":"Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation","url":"https://arxiv.org/pdf/2509.22093"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/pdf/2509.05614"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.22991"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/pdf/2506.12723"}]

I found search results related to VLA pruning and LIBERO experiments, though I didn't find a paper specifically titled "See What Matters". However, I did find a reference to a related work in the results. Let me provide you with the relevant findings:

The search results show several recent works on Vision-Language-Action (VLA) model pruning with LIBERO benchmark results:

1. **LightVLA**: LightVLA outperforms different VLA models and existing token pruning methods across diverse tasks on the LIBERO benchmark, achieving higher success rates with substantially reduced computational overhead, specifically reducing FLOPs and latency by 59.1% and 38
…[truncated 1132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-19T01:55:14.774570+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://fediory.github.io/Grid-Sampler/",
  "prompt": "Extract ALL details from this project page: full abstract, method details, model names used (OpenVLA, SmolVLA, RT-2, etc.), vision connector types, compression ratios, LIBERO benchmark results (success rates, tasks, suites), FLOPs reduction, all experimental numbers, tables, ablation studies, any discussion of cliff-edge phenomena or architecture-dependent effects. Be extremely thorough - capture every number and experimental detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://fediory.github.io/Grid-Sampler/",
    "prompt": "Extract ALL details from this project page: full abstract, method details, model names used (OpenVLA, SmolVLA, RT-2, etc.), vision connector types, compression ratios, LIBERO benchmark results (success rates, tasks, suites), FLOPs reduction, all experimental numbers, tables, ablation studies, any discussion of cliff-edge phenomena or architecture-dependent effects. Be extremely thorough - capture every number and experimental detail."
  }
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-19T01:55:14.774725+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:openreview.net \"See What Matters\" \"Grid Sample\" OR \"GridS\" VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:openreview.net \"See What Matters\" \"Grid Sample\" OR \"GridS\" VLA"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-19T01:55:14.774852+00:00_

# Grid Sampler (ICML 2026) - Project Details

## Abstract
The researchers address computational bottlenecks in Vision-Language-Action models by proposing "a plug-and-play module that performs task-aware, continuous resampling" through differentiable interpolation, achieving 76% FLOPs reduction without performance degradation.

## Core Method: Differentiable Grid Sampler (GridS)

**Key Innovation:** Reformulates compression as geometry-aware continuous token resampling rather than discrete patch dropping.

**Two-Stage Process:**
1. Global Coordinate Prediction
2. Grid Sampling with Geometry Injection

Uses differentiable bilinear interpolation to preserve sub-patch precision for robotic interaction details.

## Compression Achievements
- Visual token reduction: **99.6%** (down to 1 token from 256-token baseline)
- Operating compute: **6.25%-10%** of original
- FLOPs reduction: **76%** with no success rate degradation

## Experimental Results

### LIBERO Benchmark
- Tested across multiple task categories
- Performance compared against dense baselines and other pruning methods
- All calculations on single RTX Pro6000 GPU with 32 language tokens

### Real-World Robot Evaluation (SO100 arm)
Three tasks tested:
- **Pick & Place**
- **Stack Cubes**: +52.4% success rate improvement
- **Transfer Pen**

**Out-of-Distribution gains:** +28.6% OOD task success rate boost

## Authors & Affiliations
- Yixu Feng (University of Sydney)
- Zinan Zhao (City University of Hong Kong)
- Yanxiang Ma (University of Sydney)
- Chenghao Xia (StellarEdge Robotics)
- Chengbin Du (StellarEdge Robotics)
- Yunke Wang (University of Sydney)
- Chang Xu (University of Sydney)

## Resources
- ArXiv: 2605.11817
- GitHub repository available
- HuggingFace model collection provided

**Note:** No specific model names (OpenVLA, SmolVLA, RT-2), vision connector types, detailed ablation studies, or cliff-edge phenomenon discussions were included in the provided webpage content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-19T01:55:14.774994+00:00_

Web search results for query: "site:openreview.net "See What Matters" "Grid Sample" OR "GridS" VLA"

Links: [{"title":"Talk The Walk: Navigating Grids in New York City through Grounded Dialogue | OpenReview","url":"https://openreview.net/forum?id=HyxhusA9Fm"},{"title":"Spherical CNNs on Unstructured Grids | OpenReview","url":"https://openreview.net/forum?id=Bkl-43C9FQ"},{"title":"RL2Grid: Benchmarking Reinforcement Learning in Power Grid Operations | OpenReview","url":"https://openreview.net/forum?id=7J2C4QnQrl"},{"title":"MARL2Grid-TR: A Multi-Agent RL Benchmark in Power Grid Operations | OpenReview","url":"https://openreview.net/forum?id=mpAMH1OyMO"},{"title":"Towards predicting dynamic stability of power grids with Graph Neural Networks | OpenReview","url":"https://openreview.net/forum?id=v-3dUexkNn"},{"title":"A Technical Report On Grid Benchmarking using SEE V.O","url":"https://arxiv.org/pdf/cs/0703086"}]

The search results do not contain any papers matching your query. The results returned are about power grids, spherical CNNs on unstructured grids, and dialogue datasets - none of which match the specific paper you're looking for with the phrases "See What Matters," "Grid Sample," "GridS," or related to VLA (Vision Language Architecture).

The search query with `site:openreview.net` and those specific terms did not yield relevant results. You may want to try:
- Searching without the `site:` restriction to find the paper on other platforms
- Using different keywords from the paper title or abstract
- Checking OpenReview directly with a different search query format

Would you like me to help you search for this paper with different terms?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-19T01:55:14.775152+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.11817",
  "prompt": "Extract the COMPLETE abstract, all author information, and any other details available on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2605.11817",
    "prompt": "Extract the COMPLETE abstract, all author information, and any other details available on this page."
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-19T01:55:14.775312+00:00_

# Paper Summary: GridS - Differentiable Grid Sample Pruning

**arXiv ID:** 2605.11817  
**Submitted:** May 12, 2026 (revised May 17, 2026)  
**Published in:** Proceedings of the Forty-third International Conference on Machine Learning, 2026

## Authors
Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, and Chang Xu

## Abstract
The research addresses computational efficiency in Vision-Language-Action models used for robotic manipulation. The authors propose that "aggressive compression using pruning inevitably discards critical geometric details like contact points, leading to severe performance degradation." They introduce GridS (Differentiable Grid Sampler), a module enabling "task-aware, continuous resampling of visual tokens in VLA" through "adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation."

Key results include:
- Reduction to fewer than 10% of original visual tokens
- 76% reduction in FLOPs with no success rate degradation
- Validation on LIBERO benchmark and real robotic systems

## Classification
- **Primary:** Robotics (cs.RO)
- **Secondary:** Computer Vision and Pattern Recognition (cs.CV)

## Code Availability
The authors provide implementation code via GitHub (URL referenced in abstract).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-19T01:55:14.775466+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/pdf/2605.11817",
  "prompt": "Extract ALL details from this paper with maximum thoroughness:\n\n1. MODELS USED: Which VLA models are used? OpenVLA? SmolVLA? RT-2? What are their parameter sizes? What vision encoders do they use?\n\n2. VISION CONNECTOR: What type of vision connector (pixel-shuffle, MLP projection, cross-attention, perceiver resampler)? Does the paper analyze how different connectors affect compression?\n\n3. METHOD DETAILS: Is GridS training-free or training-required? What is the exact compression mechanism? How does the coordinate prediction work? What loss function is used?\n\n4. LIBERO EXPERIMENTS: Which LIBERO suites (Object/Spatial/Goal/Long)? How many tasks per suite? How many seeds? How many episodes per evaluation? What are the EXACT success rate numbers for baseline and GridS at different compression ratios? Include ALL numbers from tables.\n\n5. ABLATION STUDIES: What ablations are performed? Results?\n\n6. CLIFF-EDGE: Does the paper discuss sudden performance collapse when pruning too aggressively? Architecture-dependent compressibility?\n\n7. RE-ENCODING vs DELETION: Does the paper compare re-encoding remaining tokens vs simply deleting tokens?\n\n8. CROSS-ARCHITECTURE: Does it test on multiple VLA architectures with different vision connectors?\n\n9. ALL TABLES AND FIGURES: Extract data from every table, especially LIBERO results.\n\n10. FLOPS/LATENCY: Exact reduction numbers.\n\nBe extremely detailed - I need every number."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/pdf/2605.11817",
    "prompt": "Extract ALL details from this paper with maximum thoroughness:\n\n1. MODELS USED: Which VLA models are used? OpenVLA? SmolVLA? RT-2? What are their parameter sizes? What vision encoders do they use?\n\n2. VISION CONNECTOR: What type of vision connector (pixel-shuffle, MLP projection, cross-attention, perceiver resampler)? Does the paper analyze how different connectors affect compression?\n\n3. METHOD DETAILS: Is GridS training-free or training-required? What is the exact compression mechanism? How does the coordinate prediction work? What loss function is used?\n\n4. LIBERO EXPERIMENTS: Which LIBERO suites (Object/Spatial/Goal/Long)? How many tasks per suite? How many seeds? How many episodes per evaluation? What are the EXACT success rate numbers for baseline and GridS at different compression ratios? Include ALL numbers from tables.\n\n5. ABLATION STUDIES: What ablations are performed? Results?\n\n6. CLIFF-EDGE: Does the paper discuss sudden performance collapse when pruning too aggressively? Architecture-dependent compressibility?\n\n7. RE-ENCODING vs DELETION: Does the paper compare re-encoding remaining tokens vs simply deleting tokens?\n\n8. CROSS-ARCHITECTURE: Does it test on multiple VLA architectures with different vision connectors?\n\n9. ALL TABLES AND FIGURES: Extract data from every table, especially LIBERO results.\n\n10. FLOPS/LATENCY: Exact reduction numbers.\n\nBe extremely detailed - I need every number."
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-19T01:55:14.775606+00:00_

# Extraction of Paper Details: "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model"

## 1. MODELS USED

The paper evaluates pruning on **OpenVLA** models. Specific parameter sizes and vision encoder details are embedded in the PDF structure but not clearly extracted from the provided content. The paper mentions testing on vision-language-action models but specific model variants (parameter counts) are not explicitly stated in the accessible portions.

## 2. VISION CONNECTOR

The paper discusses **Grid Sample Pruning (GridS)** as a method that works across different vision connector architectures. However, specific connector types (pixel-shuffle, MLP, cross-attention, perceiver resampler) are not explicitly detailed in the extracted sections. The focus is on token-level pruning that should be architecture-agnostic.

## 3. METHOD DETAILS

**GridS (Differentiable Grid Sample Pruning):**
- **Training-required**: The method uses differentiable pruning with gradient-based optimization
- **Mechanism**: "Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model" indicates coordinate-prediction based token selection
- **Loss function**: Not explicitly detailed in accessible content
- The approach appears to learn which spatial regions/tokens matter most for action prediction

## 4. LIBERO EXPERIMENTS

Specific LIBERO suite numbers, exact success rates, compression ratios, and performance tables are embedded in the PDF but not clearly readable from the extracted content. References to "figure.caption" and "table.caption" entries suggest multiple tables exist, but the actual numerical data cannot be reliably extracted.

## 5. ABLATION STUDIES

Ablation studies are referenced through multiple subsections (subsection.4.1 through subsection.4.4) but specific results are not accessible in the extracted portions.

## 6. CLIFF-EDGE PHENOMENON

Not explicitly addressed in accessible content. The paper mentions "
…[truncated 1715 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-19T01:55:14.775762+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2605.11817",
  "prompt": "Extract ALL details with maximum thoroughness:\n\n1. MODELS: Which VLA models? OpenVLA? SmolVLA? RT-2? Parameter sizes? Vision encoders?\n\n2. VISION CONNECTOR: pixel-shuffle? MLP? cross-attention? Does paper analyze connector effects on compression?\n\n3. METHOD: Training-free or training-required? Exact mechanism of GridS? Loss function? How does coordinate prediction work?\n\n4. LIBERO RESULTS: ALL numbers from ALL tables. Which suites (Object/Spatial/Goal/Long)? Exact success rates? Baseline numbers? Compressed numbers? Number of seeds? Episodes?\n\n5. ABLATIONS: All ablation results.\n\n6. Does paper discuss cliff-edge / sudden collapse?\n\n7. Re-encoding vs deletion comparison?\n\n8. Cross-architecture analysis with different vision connectors?\n\n9. ALL table data - every number.\n\n10. FLOPs/latency exact numbers.\n\nBe EXHAUSTIVE."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2605.11817",
    "prompt": "Extract ALL details with maximum thoroughness:\n\n1. MODELS: Which VLA models? OpenVLA? SmolVLA? RT-2? Parameter sizes? Vision encoders?\n\n2. VISION CONNECTOR: pixel-shuffle? MLP? cross-attention? Does paper analyze connector effects on compression?\n\n3. METHOD: Training-free or training-required? Exact mechanism of GridS? Loss function? How does coordinate prediction work?\n\n4. LIBERO RESULTS: ALL numbers from ALL tables. Which suites (Object/Spatial/Goal/Long)? Exact success rates? Baseline numbers? Compressed numbers? Number of seeds? Episodes?\n\n5. ABLATIONS: All ablation results.\n\n6. Does paper discuss cliff-edge / sudden collapse?\n\n7. Re-encoding vs deletion comparison?\n\n8. Cross-architecture analysis with different vision connectors?\n\n9. ALL table data - every number.\n\n10. FLOPs/latency exact numbers.\n\nBe EXHAUSTIVE."
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-19T01:55:14.775902+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.11817 GridS VLA OpenVLA SmolVLA LIBERO success rate results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.11817 GridS VLA OpenVLA SmolVLA LIBERO success rate results"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-19T01:55:14.776047+00:00_

Web search results for query: "arxiv 2605.11817 GridS VLA OpenVLA SmolVLA LIBERO success rate results"

Links: [{"title":"SmolVLA - ArXivIQ","url":"https://arxiviq.substack.com/p/smolvla"},{"title":"[Literature Review] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://www.themoonlight.io/en/review/smolvla-a-vision-language-action-model-for-affordable-and-efficient-robotics"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"Beyond Human Demonstrations: Diffusion-Based Reinforcement Learning to Generate Data for VLA Training","url":"https://arxiv.org/pdf/2509.19752"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model","url":"https://arxiv.org/html/2509.09372v2"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation","url":"https://arxiv.org/pdf/2510.14902"}]

I found relevant results, but let me search more specifically for the arxiv paper 2605.11817 to get the exact information you're looking for.

Links: [{"title":"Hybrid rule-based and on-premises LLM pipeline for extracting CMR and CPET metrics from free-text reports in repaired tetralogy of Fallot","url":"https://www.medrxiv.org/content/10.64898/2026.01.21.26344531.full.pdf"},{"title":"Influence of Topic Familiarity and Prompt Specificity on Citation Fabrication in Mental Health Research Using Large Language Models: Experimental Study","url":"https://www.ncbi.nlm.nih.gov/pmc/ar
…[truncated 3635 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-19T01:55:14.776234+00:00_

# GridS: Comprehensive Technical Extraction

## 1. VLA MODELS EVALUATED

**Flow-matching models:**
- π0 (Black et al., 2024) - 256 visual tokens baseline
- π0.5 (Intelligence et al., 2025) - stronger backbone variant

**Auto-regressive model:**
- SmolVLA (Shukor et al., 2025) - 64 visual tokens baseline

**Comparison baselines:**
- OpenVLA (256 tokens)
- CogACT (256 tokens)
- OpenVLA-OFT (512 tokens)

Vision encoders used: SigLIP, DINOv2 (frozen, not fine-tuned)

## 2. VISION CONNECTOR

Paper does NOT analyze connector architecture. GridS operates as a "plug-and-play module" inserted between frozen vision encoder and transformer, using:
- Global average pooling → context vector
- Lightweight MLP for coordinate prediction
- Coordinate Encoder mapping coordinates to position embeddings
- No cross-attention or pixel-shuffle mechanisms discussed

## 3. METHOD: GridS MECHANISM

**Training requirement:** Training-required (joint optimization), NOT training-free

**Core pipeline:**
1. Global Coordinate Prediction: MLP predicts K continuous normalized coordinates P ∈ [0,1]^(K×2) from context vector z
2. Differentiable Bilinear Sampling: Features extracted via weighted interpolation of four nearest neighbors
3. Geometry Injection: Predicted coordinates encoded as position embeddings, added to sampled features

**Loss function:** "end-to-end using only the primary task loss—without any auxiliary supervision"

**Differentiability:** Bilinear weights ωk are linear functions of coordinates, enabling gradient flow via: ∂ℒ/∂x = Σ(∂ℒ/∂F_sampled · P_k · ∂ω_k/∂x)

## 4. LIBERO RESULTS - COMPREHENSIVE TABLE DATA

### Table 1: π0 with LIBERO (256→16 tokens)

| Suite | Baseline SR (%) | GridS16 SR (%) | Δ | GridS4 SR (%) |
|-------|-----------------|-----------------|-------|-----------------|
| Spatial | 97.2 | 98.0 | +0.8 | 96.6 |
| Object | 98.8 | 99.2 | +0.4 | 99.4 |
| Goal | 96.0 | 96.4 | +0.4 | 96.4 |
| Long | 85.6 | 90.2 | **+4.6** | 89.6 |
| **Avg SR** | **94.4** | **96.0** | **
…[truncated 4298 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-19T01:55:14.776399+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2605.11817",
  "prompt": "Focus on these specific sections:\n\n1. RELATED WORK: What prior VLA compression methods are discussed? Does it mention architecture-dependent compression effects?\n\n2. LIMITATIONS: What limitations do the authors acknowledge?\n\n3. SmolVLA details: What vision connector does SmolVLA use in their experiments? How many tokens does SmolVLA have? What are SmolVLA's LIBERO results specifically?\n\n4. How is GridS integrated differently for flow-matching (π0) vs auto-regressive (SmolVLA) architectures?\n\n5. Does the paper discuss WHY some architectures are more compressible than others?\n\n6. What is the pixel-shuffle connector? Does this paper mention it at all?\n\n7. Table 5 hyperparameters - extract all.\n\n8. Any discussion about token deletion causing catastrophic failure vs graceful degradation?\n\n9. LIBERO evaluation protocol: how many episodes per task? how many seeds?\n\n10. What benchmarks besides LIBERO are used? LIBERO-PLUS? RoboTwin?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2605.11817",
    "prompt": "Focus on these specific sections:\n\n1. RELATED WORK: What prior VLA compression methods are discussed? Does it mention architecture-dependent compression effects?\n\n2. LIMITATIONS: What limitations do the authors acknowledge?\n\n3. SmolVLA details: What vision connector does SmolVLA use in their experiments? How many tokens does SmolVLA have? What are SmolVLA's LIBERO results specifically?\n\n4. How is GridS integrated differently for flow-matching (π0) vs auto-regressive (SmolVLA) architectures?\n\n5. Does the paper discuss WHY some architectures are more compressible than others?\n\n6. What is the pixel-shuffle connector? Does this paper mention it at all?\n\n7. Table 5 hyperparameters - extract all.\n\n8. Any discussion about token deletion causing catastrophic failure vs graceful degradation?\n\n9. LIBERO evaluation protocol: how many episodes per task? how many seeds?\n\n10. What benchmarks besides LIBERO are used? LIBERO-PLUS? RoboTwin?"
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-19T01:55:14.776547+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Don't Run with Scissors\" pruning breaks VLA cliff-edge architecture connector"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Don't Run with Scissors\" pruning breaks VLA cliff-edge architecture connector"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-19T01:55:14.776698+00:00_

Web search results for query: ""Don't Run with Scissors" pruning breaks VLA cliff-edge architecture connector"

Links: [{"title":"[2510.08464] Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/abs/2510.08464"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://gluestick-vla.github.io/"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered | OpenReview","url":"https://openreview.net/forum?id=c8g57pKdXD"},{"title":"Pruning Breaks VLA Models but They Can Be Recovered","url":"https://www.researchgate.net/publication/396373210_Don't_Run_with_Scissors_Pruning_Breaks_VLA_Models_but_They_Can_Be_Recovered"},{"title":"Pruning Breaks VLA Models but They Can Be Recovered","url":"https://openreview.net/pdf/84d1865f2a64e0eefde372c576962158aecbc73f.pdf"},{"title":"How to Prune Your Tree - Friends of Trees","url":"https://friendsoftrees.org/news-resources/tree-pruning/"},{"title":"We Put Embodied AI on a 100g Device. Why Most VLAs Choke on the Edge (and the Architecture That Didn’t) - deepsense.ai","url":"https://deepsense.ai/blog/we-put-embodied-ai-on-a-100g-device-why-most-vlas-choke-on-the-edge-and-the-architecture-that-didnt/"},{"title":"Workshop Safety, a.k.a. Don't Run With Scissors","url":"https://www.kitplanes.com/running-with-scissors-shop-safety/"},{"title":"Follow Proper Pruning Techniques - Earth-Kind® Landscaping Earth-Kind® Landscaping","url":"https://aggie-horticulture.tamu.edu/earthkind/landscape/proper-pruning-techniques/"},{"title":"General Pruning Techniques | NC State Extension Publications","url":"https://content.ces.ncsu.edu/general-pruning-techniques"}]

Based on the web search results, I found relevant information about the paper "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered."

## Search Results Summary

Pruning VLA models leads to drastic degradation and increased safety violations. Recent
…[truncated 912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-19T01:55:14.776853+00:00_

# GridS Paper Analysis: Key Findings

## 1. RELATED WORK: Prior VLA Compression Methods

The paper discusses several compression approaches:

**Semantic Pruning:** Methods like SemanticVLA "prioritize salient object bodies while neglecting geometrically critical but semantically subtle regions, e.g. edges or contact points."

**Dynamic Token Pruning:** Training-free approaches (SparseVLM, VLA-Cache, EfficientVLA) that are "inherently non-differentiable, functioning as static heuristics" and "fail to align with specific application requirements."

**Architecture-dependent effects:** The paper doesn't explicitly discuss why certain architectures compress differently, though it shows π0 (256 tokens) vs SmolVLA (64 tokens) have different baseline densities.

## 2. LIMITATIONS (Appendix J)

The paper acknowledges: task-specific token sensitivities at extreme sparsity levels, geometric ambiguity in spatial tasks, vulnerability of long-horizon tasks to "error accumulation" when token budgets are strict, and overfitting tendencies in LIBERO datasets.

## 3. SmolVLA Details

- **Baseline tokens:** 64 (vs. π0's 256)
- **LIBERO results:** 79.0% average success rate across the four task suites
- **Vision connector:** Not explicitly named in the provided text
- **Architecture type:** Auto-regressive model

## 4. GridS Integration Across Architectures

The paper states GridS is "jointly optimized with the VLA policy during standard fine-tuning" and "seamlessly compatible with diverse paradigms, including auto-regressive and flow-matching models." However, no architecture-specific modifications are described.

## 5. Architecture Compressibility Discussion

The paper does not explain *why* different architectures compress at different rates. It treats compression as architecture-agnostic.

## 6. Pixel-Shuffle Connector

Not mentioned anywhere in the document.

## 7. Table 5 Hyperparameters

| Parameter | SmolVLA | π0 (LIBERO/ALOHA) | π0.5 (LIBERO) |
|-----------|---------|---------
…[truncated 1271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-19T01:55:14.777298+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2605.11817",
  "prompt": "I need SPECIFIC data from appendix sections:\n\n1. Appendix E.1 - LIBERO-PLUS results: Extract ALL numbers from tables. What are exact success rates?\n\n2. Appendix E.2 - RoboTwin results: Extract ALL numbers.\n\n3. SmolVLA LIBERO breakdown: What are the per-suite (Spatial/Object/Goal/Long) success rates for SmolVLA baseline vs GridS? Is there a table with SmolVLA LIBERO numbers?\n\n4. Table 1 COMPLETE data: I need the FULL table including SmolVLA rows. Previous extraction showed π0 and π0.5 but may have missed SmolVLA.\n\n5. What is the exact number of evaluation episodes for LIBERO? Does it say 500 episodes per task? 50? What seeds?\n\n6. Section about \"Geometry Injection\" - what exactly does this do?\n\n7. Figure 3 or 4 - attention visualization: what do the attention maps show?\n\n8. Does the paper mention OpenVLA at all in its own experiments (not just as a comparison baseline)?\n\n9. Appendix G - extreme compression to 1 token: exact numbers?\n\n10. Any mention of \"margin\" or \"importance\" scoring for tokens?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2605.11817",
    "prompt": "I need SPECIFIC data from appendix sections:\n\n1. Appendix E.1 - LIBERO-PLUS results: Extract ALL numbers from tables. What are exact success rates?\n\n2. Appendix E.2 - RoboTwin results: Extract ALL numbers.\n\n3. SmolVLA LIBERO breakdown: What are the per-suite (Spatial/Object/Goal/Long) success rates for SmolVLA baseline vs GridS? Is there a table with SmolVLA LIBERO numbers?\n\n4. Table 1 COMPLETE data: I need the FULL table including SmolVLA rows. Previous extraction showed π0 and π0.5 but may have missed SmolVLA.\n\n5. What is the exact number of evaluation episodes for LIBERO? Does it say 500 episodes per task? 50? What seeds?\n\n6. Section about \"Geometry Injection\" - what exactly does this do?\n\n7. Figure 3 or 4 - attention visualization: what do the attention maps show?\n\n8. Does the paper mention OpenVLA at all in its own experiments (not just as a comparison baseline)?\n\n9. Appendix G - extreme compression to 1 token: exact numbers?\n\n10. Any mention of \"margin\" or \"importance\" scoring for tokens?"
  }
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-19T01:55:14.777464+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://gluestick-vla.github.io/",
  "prompt": "Extract details about: which VLA architectures tested, does it discuss architecture-dependent pruning effects, cliff-edge phenomenon, vision connector analysis, LIBERO results, any comparison showing different architectures respond differently to pruning."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://gluestick-vla.github.io/",
    "prompt": "Extract details about: which VLA architectures tested, does it discuss architecture-dependent pruning effects, cliff-edge phenomenon, vision connector analysis, LIBERO results, any comparison showing different architectures respond differently to pruning."
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-19T01:55:14.777600+00:00_

# GLUESTICK VLA Architecture Analysis

## VLA Architectures Tested

The research evaluates three distinct VLA models:
- **OpenVLA**
- **WorldVLA**
- **NaVILA**

The paper states results were "averaged across OpenVLA and WorldVLA" for manipulation tasks, while NaVILA was used for navigation evaluation.

## Architecture-Dependent Effects

The webpage does not discuss whether different architectures respond differently to pruning or exhibit varying sensitivity levels. While three models are tested, the results presentation aggregates findings rather than providing comparative analysis showing how architectural differences influence pruning vulnerability.

## Other Phenomena Not Addressed

The document makes no mention of:
- Cliff-edge phenomena in pruning effects
- Vision connector analysis
- Architecture-specific pruning mechanisms

## LIBERO Results

The manipulation benchmark shows significant degradation from pruning across all task suites (Spatial, Object, Goal, Long-horizon), with "Full Sparse" experiencing drops between −55.8% to −85.2%. GLUESTICK recovery achieves −32.8% to −42.2% loss, substantially improving task success while maintaining sparsity efficiency.

## Key Limitation

The research demonstrates recovery effectiveness across models but does not analyze whether architectural components respond uniformly to the GLUESTICK correction method.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-19T01:55:14.777744+00:00_

# Detailed Data Extraction from GridS Paper

## 1. Appendix E.1 - LIBERO-PLUS Results
The document content provided does **not include** the full Appendix E sections. The text cuts off before those detailed results appear. I cannot extract the specific LIBERO-PLUS numbers you requested.

## 2. Appendix E.2 - RoboTwin Results
Similarly, the RoboTwin experimental data is **not present** in the provided excerpt.

## 3. SmolVLA LIBERO Breakdown
From Table 1, SmolVLA baseline shows:
- **64 visual tokens** | 306.78 GFLOPs | 8.91s inference time
- **Per-suite breakdown**: Spatial 81.3% | Object 92.9% | Goal 85.8% | Long 55.8%
- **Average success rate: 79.0%**

The paper does **not provide** GridS + SmolVLA comparisons in the main LIBERO table.

## 4. Table 1 Complete Data
Table 1 includes: OpenVLA, CogACT, SmolVLA, OpenVLA-OFT, π₀ baseline and variants (FastV, SparseVLM, VLA-Cache, GridS16, GridS4), plus π₀.₅ baseline and variants. SmolVLA is included as shown above.

## 5. LIBERO Evaluation Protocol
The document states: "We evaluate the performance across all four suites" but **does not explicitly specify total episode counts** per task or random seed details in the methodology section.

## 6. Geometry Injection Mechanism
The paper describes using a **Coordinate Encoder that maps predicted coordinates into position embeddings**, which are then **added to sampled features**. This restores spatial structure disrupted by sampling.

## 7. Attention Visualizations
Figure 7 shows "**Information Retention Maps**" (left side shows green areas indicating maintained information) and "**Token Self-Similarity matrices**" (right side reveals diagonal-dominant structure after GridS processing versus dense off-diagonal correlations in original features).

## 8. OpenVLA in Own Experiments
OpenVLA appears **only as a comparison baseline** in Table 1, not as a primary experimental subject for GridS evaluation.

## 9. Appendix G - K=1 Extreme Compression
The document references this exists 
…[truncated 341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-19T01:55:14.777903+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA pixel-shuffle vision connector compression pruning cliff-edge collapse architecture-dependent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA pixel-shuffle vision connector compression pruning cliff-edge collapse architecture-dependent"
  }
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-19T01:55:14.778037+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA vision connector type cross-attention perceiver resampler architecture"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA vision connector type cross-attention perceiver resampler architecture"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-19T01:55:14.778191+00:00_

Web search results for query: "VLA pixel-shuffle vision connector compression pruning cliff-edge collapse architecture-dependent"

Links: [{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models","url":"https://arxiv.org/pdf/2509.09090"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/pdf/2511.16449"},{"title":"PixelPrune: Pixel-Level Adaptive Visual Token Reduction via Predictive Coding","url":"https://arxiv.org/html/2604.00886v1"}]

Based on the search results, I found several relevant papers about Vision-Language-Action (VLA) models and visual token compression techniques. Here's what the search revealed:

## Key Findings:

**VLA Compression and Pruning Research:**

The search returned papers covering different aspects of VLA model compression:

1. **VLA-IAP (Vision-Language-Action with Interaction Alignment Pruning)**: Research shows that under extreme compression, some pruning methods suffer catastrophic failures, with performance collapsing from 40.7% accuracy at 70% token retention to 8.0% at 30% retention. This illustrates the "cliff-edge collapse" phenomenon you mentioned.

2. **Compressor-VLA**: A hybrid instruction-conditioned token compression framework designed to preserve both holistic context and fine-grained details for precise action.

3. **SQAP-VLA**: An approach addressing an observed incompatibility between quantization and token pruning that prevents combining both methods for holistic efficiency improvement.

4. **VLA-Pruner**: Reveals the dual-system property of VLA inference with 
…[truncated 637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-19T01:55:14.778355+00:00_

Web search results for query: "SmolVLA vision connector type cross-attention perceiver resampler architecture"

Links: [{"title":"Perceiver Resampler Architecture","url":"https://www.emergentmind.com/topics/perceiver-resampler-architecture"},{"title":"Visual Anchors Are Strong Information Aggregators For ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/1f84412e84da6440ca355d87184cb1b3-Paper-Conference.pdf"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"Vision Language Models | Rohit Bandaru","url":"https://rohitbandaru.github.io/blog/Vision-Language-Models/"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"Vision Large Language Models (vLLMs)","url":"https://cameronrwolfe.substack.com/p/vision-llms"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"SmolVLA Models: Compact Vision-Language-Action Systems","url":"https://www.emergentmind.com/topics/smolvla-models"},{"title":"Perceiver-VL: Efficient Vision-and-Language Modeling with Iterative   Latent Attention","url":"https://arxiv.org/pdf/2211.11701"},{"title":"Flamingo Simulation Variant Overview","url":"https://www.emergentmind.com/topics/flamingo-simulation-variant"}]

Based on the search results, here's what I found about SmolVLA's vision connector architecture:

## SmolVLA Architecture Overview

SmolVLA has two primary components: a Perception Module (SmolVLM-2) that is a pretrained compact vision-language encoder, and an Action Expert.

## Vision Connector Design

Rather than using a perceiver resampler, SmolVLA applies three key techniques: reducin
…[truncated 1073 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-19T01:55:14.778510+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenVLA vision connector architecture pixel-shuffle MLP projection DinoSigLIP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenVLA vision connector architecture pixel-shuffle MLP projection DinoSigLIP"
  }
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-19T01:55:14.778647+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "pi0 π0 VLA vision connector architecture token projection type"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "tool_args": {
    "query": "pi0 π0 VLA vision connector architecture token projection type"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-19T01:55:14.778789+00:00_

Web search results for query: "OpenVLA vision connector architecture pixel-shuffle MLP projection DinoSigLIP"

Links: [{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"GitHub - phospho-app/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/phospho-app/openvla"},{"title":"PixelVLA: Pixel-Level VLA for Robotic Manipulation","url":"https://www.emergentmind.com/topics/pixelvla"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"GitHub - dusty-nv/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation.","url":"https://github.com/dusty-nv/openvla"},{"title":"PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model","url":"https://arxiv.org/html/2511.01571v1"}]

Based on the search results, here's what I found about OpenVLA's vision connector architecture:

## OpenVLA Vision Connector Architecture

OpenVLA's model consists of a fused visual encoder with SigLIP and DinoV2 backbones that maps image inputs to image patch embeddings, a projector that takes the output embeddings and maps them into the input space of a large language model, and a Llama 2 7B language model backbone.

### Visual Encoding Process

Incoming RGB observations are divided into patches, each processed by both visual encoders and concatenated as token vectors. The visual encoder fuses features from DINOv2 (for spatial fidelity) and SigLIP (for semantic discrimination).

### Projection Mechanism

These tokens are projected into the LLM embedding space using a two-layer MLP projector. This 
…[truncated 726 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-19T01:55:14.778948+00:00_

Web search results for query: "pi0 π0 VLA vision connector architecture token projection type"

Links: [{"title":"Understanding pi0 by Physical Intelligence: A Vision-Language-Action Flow Model for General Robot Control","url":"https://blog.phospho.ai/understanding-p0-by-physical-intelligence-a-vision-language-action-flow-model-for-general-robot-control/"},{"title":"【Learning VLA】Understand π0 codebase framework【I】 • Lingyun's website","url":"https://www.avidjoyce.com/blog/pi-0"},{"title":"GitHub - allenzren/open-pi-zero: Re-implementation of pi0 vision-language-action (VLA) model from Physical Intelligence · GitHub","url":"https://github.com/allenzren/open-pi-zero"},{"title":"π0: A Vision-Language-Action Flow Model for General Robot Control","url":"https://www.pi.website/download/pi0.pdf"},{"title":"Notes on: \"π0: A Vision-Language-Action Flow Model for General Robot Control\" | cloderic.com","url":"https://www.cloderic.com/content/2025-02-27-notes-on-pi0"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"phospho starter pack documentation","url":"https://docs.phospho.ai/learn/policies"},{"title":"π0 and π0-FAST: Vision-Language-Action Models for General Robot Control","url":"https://huggingface.co/blog/pi0"},{"title":"π0.5: a Vision-Language-Action Model with Open-World Generalization","url":"https://www.pi.website/download/pi05.pdf"}]

Based on the search results, here's information about π0 (pi0), its VLA architecture, and token projection:

## Overview
π0 is a large-scale generalist VLA announced in late 2024 by Physical Intelligence, designed for general robot control.

## Architecture Components

**Vision-Language Backbone:**
π0 uses PaliGemma, a 3 billion parameter VLM pre-trained on internet-scale image-text pairs, which encodes images into embeddings that align with language tokens.

**Token Projection:**
It projects images and text into a shared token space, allowing seamles
…[truncated 910 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-19T01:55:14.779218+00:00_

Now I have all the information needed for a comprehensive analysis. Here is my detailed report.

---

## Detailed Analysis: "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model"

**Paper:** arXiv 2605.11817, ICML 2026 (Poster)
**Authors:** Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu (University of Sydney, CityU HK, StellarEdge Robotics)
**Project page:** https://fediory.github.io/Grid-Sampler/

---

### A. 使用的 VLA 模型

| Model | Type | Tokens | Notes |
|-------|------|--------|-------|
| **π0** (Physical Intelligence) | Flow-matching, ~3B (PaliGemma backbone) | 256 | Primary experimental model, GridS applied |
| **π0.5** | Flow-matching (stronger variant) | 256 | GridS applied |
| **SmolVLA** (HuggingFace) | Auto-regressive, ~450M | 64 | GridS applied in real-world experiments only |
| OpenVLA | Auto-regressive, 7B (Llama2 backbone) | 256 | Comparison baseline only, GridS NOT applied |
| CogACT | -- | 256 | Comparison baseline only |
| OpenVLA-OFT | -- | 512 | Comparison baseline only |

**SmolVLA IS included** but only for real-world robot experiments (SO-100 arm), not for LIBERO simulation benchmarks. SmolVLA's LIBERO baseline numbers (79.0% avg) appear in Table 1 but GridS+SmolVLA LIBERO results are not reported.

Vision encoders: SigLIP + DINOv2 (frozen, not fine-tuned).

### B. Vision Connector 类型

The paper does **NOT** analyze vision connector types at all.

- **π0**: Uses PaliGemma as VLM backbone; images projected into shared token space via the PaliGemma projector. Action Expert (300M params) uses flow matching.
- **SmolVLA**: Uses SmolVLM-2 as perception module; the action expert uses interleaved cross-attention and causal self-attention layers. Connector reduces tokens to 64 per frame via downsampling.
- **OpenVLA**: Uses 2-layer MLP projector between DinoSigLIP encoder and Llama2 backbone (comparison baseline only).

The paper **never mentions pixel-shuffle**. It does
…[truncated 7571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep_analysis_competitors_20260519T013824",
  "tool": "Agent",
  "elapsed_ms": 7
}
```

</details>

---

### Assistant

_source line 111 · 2026-05-19T01:55:14.779484+00:00_

四篇论文分析完成。以下是完整结构化报告。

---

## 1. Compressor-VLA (arXiv 2511.18950)

### A. VLA 模型
- **基础模型**: OpenVLA-OFT (LLaMA-2-7B + DINOv2/SigLIP 双编码器), 512 visual tokens
- **对比模型**: CogACT, π0, SP-VLA, FastV, SparseVLM, SpecPrune-VLA, VLA-Cache
- **SmolVLA**: 未涉及

### B. Vision Connector
- 未分析不同 connector 类型对压缩的影响
- 提出的 compressor 本身使用 cross-attention (STC) + local windowed attention (SRC) 替代原始 projector

### C. 压缩机制
- **Training-required**: 150K steps, 8 GPUs, batch 64, LoRA rank 32
- **策略**: Reconstructive compression (非 pruning)
  - STC: 16 learnable queries + FiLM language conditioning → 16 global tokens
  - SRC: local window (w=2) downsampling → 144 local tokens
- **压缩比**: 512 → 160 tokens (3.2×), FLOPs 3.95T → 1.62T (59% reduction)

### D. LIBERO 数据

| Method | Spatial | Object | Goal | Long | Avg | FLOPs(T) | Tokens |
|--------|---------|--------|------|------|-----|----------|--------|
| OpenVLA-OFT | 97.6 | 98.4 | 97.9 | 94.5 | 97.1 | 3.95 | 512 |
| SP-VLA | 75.4 | 85.6 | 84.4 | 54.2 | 74.9 | 3.10 | 229 |
| FastV | 96.8 | 81.0 | 96.4 | 73.0 | 86.8 | 3.18 | 256 |
| SparseVLM | 96.8 | 94.2 | 97.6 | 93.6 | 95.6 | 3.04 | 256 |
| SpecPrune-VLA | 98.2 | 96.3 | 97.7 | 94.0 | 96.6 | 1.70 | 197 |
| VLA-Cache | 99.0 | 97.7 | 97.4 | 93.6 | 97.0 | 3.28 | 212 |
| **Compressor-VLA** | **98.8** | **99.2** | **96.4** | **94.8** | **97.3** | **1.62** | **160** |

- 4 suites × 10 tasks，50 demos/task
- **无 seed 报告、无 episode 数、无 error bars**

### E. 关键问题
| 问题 | 是否涉及 |
|------|---------|
| Cliff-edge 分析 | ❌ 未讨论（但 SP-VLA Long=54.2% 隐含了此现象） |
| Cross-architecture 对比 | ❌ 仅 OpenVLA-OFT |
| Re-encoding vs deletion | ❌ 无控制实验（概念上主张 reconstruction > pruning） |
| Closed-loop 评估 | ✅ LIBERO + Mobile ALOHA 实机 |

### F. 与我们的差异
- 工程贡献：一个更好的 compressor module。不分析 WHY compression fails
- 我们的 cliff-edge 发现、connector-dependent compressibility、re-encoding vs deletion 控制实验均完全缺失

---

## 2. SpecPrune-VLA (arXiv 2509.05614)

### A. VLA 模型
- **基础模型**: OpenVLA-OFT, π₀, UniVLA (SimplerEnv only)
- **SmolVLA**: 未涉及
- 未报告参数量

### B. Vision Connector
- 完全未分析 connector 类型。视觉编码器视为黑盒，只关注 LLM 层内的 attention pattern

### C. 压缩机制
- **Training-free**: 明确声明
- **两级剪枝**:
  1. Action-level Static Pruning: 前一步 attention 分数识别全局重要 tokens (K_global=30) + 帧间 patch 相似度 (K_dynamic=20) + 当前步前两层 attention (K_local=24)
  2. Layer-level Dynamic Pruning: attention entropy 逐层再剪 10%
  3. Action-Aware Controller: 末端执行器速度 → coarse/fine 动态调整剪枝力度
- **压缩比**: FLOPs 剩余 43% (OpenVLA-OFT), 48% (π₀); 加速 1.46-1.70×

### D. LIBERO 数据

| Method | Spatial | Object | Goal | Long | Avg | Speedup |
|--------|---------|--------|------|------|-----|---------|
| Baseline | 97.6 | 96.5 | 97.9 | 94.5 | 96.6 | 1.00× |
| **SpecPrune-VLA** | **97.4** | **95.8** | **97.7** | **93.4** | **96.1** | **1.46×** |
| FastV | 94.6 | 95.8 | 94.0 | 88.8 | 93.3 | 1.44× |
| EfficientVLA | 96.5 | 91.1 | 96.0 | 72.1 | 88.9 | 1.52× |

- π₀: 94.2% → 93.5% avg, 1.31× speedup
- **无 seed、无 episode 数、无 error bars**

### E. 关键问题
| 问题 | 是否涉及 |
|------|---------|
| Cliff-edge 分析 | ❌ Fig 7 显示 SR 平滑下降，未发现突变 |
| Cross-architecture 对比 | ❌ 两个模型都是 graceful degradation |
| Re-encoding vs deletion | ❌ 纯 deletion，无 re-encoding |
| Closed-loop 评估 | ✅ LIBERO + 真实机器人 |

### F. 与我们的差异
- 核心假设是 "所有 VLA 都可以被 token pruning 加速"。我们证明这在 pixel-shuffle connector 下完全不成立
- 工程优化论文 vs 我们的科学发现论文

---

## 3. LightVLA (arXiv 2509.12594)

### A. VLA 模型
- **基础模型**: 仅 OpenVLA-OFT (7B)
- **SmolVLA**: 仅作为 Table I 对比项 (88.8% avg)，未测试 LightVLA
- 对比: OpenVLA, CogACT, π0, π0-fast, NORA, WorldVLA 等

### B. Vision Connector
- OpenVLA-OFT 使用 MLP projector (3-layer, GELU)
- DINOv2 + SigLIP channel-wise concat 后经 MLP
- **未分析不同 connector 对压缩的影响**

### C. 压缩机制
- **Training-required**: 40K steps, 8× H20 GPU, batch 64
- **策略**: Differentiable token pruning via Gumbel-Softmax
  1. Query Generation: visual × language cross-attention 生成 query
  2. Token Scoring: query 对 visual tokens 打分
  3. Gumbel-Softmax 可微选择 + straight-through estimator
- **自适应压缩**: 不同 task/timestep 保留不同 token 数
- **压缩比**: 512 → 78 avg (84.8% reduction), FLOPs 8.8T → 3.6T (59.1%)

### D. LIBERO 数据

| Method | Spatial | Object | Goal | Long | Avg | Tokens |
|--------|---------|--------|------|------|-----|--------|
| OpenVLA-OFT* | 97.6 | 94.2 | 95.2 | 92.0 | 94.8 | 512 |
| **LightVLA** | **98.4** | **98.4** | **98.2** | **94.6** | **97.4** | **78±11** |
| SmolVLA (ref) | 93.0 | 94.0 | 91.0 | 77.0 | 88.8 | — |

- 10 tasks/suite, 500 demos training, 50 trials/task
- **无 seed、无 error bars**（仅 token 数量有标准差）

### E. 关键问题
| 问题 | 是否涉及 |
|------|---------|
| Cliff-edge 分析 | ❌ 消融在 96.6-97.4% 范围，未见突变 |
| Cross-architecture 对比 | ❌ 仅 OpenVLA-OFT |
| Re-encoding vs deletion | ❌ 纯 deletion (hard selection) |
| Closed-loop 评估 | ✅ LIBERO closed-loop |

### F. 与我们的差异
- 单架构效率优化。我们的 architecture-dependent compressibility 发现完全空白
- LightVLA 恰好只在 MLP projector 的"安全"架构上实验，避开了 cliff-edge

---

## 4. See What Matters / GridS (arXiv 2605.11817, ICML 2026)

### A. VLA 模型
- **基础模型**: π0 (~3B), π0.5, SmolVLA (~450M)
- **SmolVLA**: ✅ 包含，但仅用于真实机器人实验 (SO-100 arm)，LIBERO 仅有 baseline 数据
- 对比: OpenVLA, CogACT, OpenVLA-OFT

### B. Vision Connector
- π0 使用 PaliGemma projector; SmolVLA 使用 interleaved cross-attention
- **未分析 connector 类型差异对压缩的影响**
- "pixel-shuffle" 未出现在论文中

### C. 压缩机制
- **Training-required**: joint fine-tuning 30K-50K steps
- **策略**: Differentiable Grid Sampler (GridS)
  1. Global pooling → context vector → MLP 预测 K 个连续坐标 P ∈ [0,1]^(K×2)
  2. Bilinear interpolation 从四邻近 patch 采样特征（可微）
  3. Coordinate Encoder 注入位置信息
- **压缩比**: 256 → 16 tokens (93.75%), 或 → 4 tokens (98.4%); FLOPs 216G → 51.6G (76%)
- 训练加速 3.4× (π0)

### D. LIBERO 数据 (π0)

| Method | Spatial | Object | Goal | Long | Avg |
|--------|---------|--------|------|------|-----|
| π0 baseline | 97.2 | 98.8 | 96.0 | 85.6 | 94.4 |
| **GridS-16** | **98.0** | **99.2** | **96.4** | **90.2** | **96.0** |
| GridS-4 | — | — | — | — | 95.5 |

π0.5: 96.7% → 97.7% avg

SmolVLA LIBERO baseline: 79.0% avg（未测试 GridS+SmolVLA 的 LIBERO）

真实机器人 SmolVLA (64→16 tokens): Stack Cubes 从 7.6% → 60.0%

**无 error bars（LIBERO）**。ALOHA 实验报告了 3 seeds。

### E. 关键问题
| 问题 | 是否涉及 |
|------|---------|
| Cliff-edge 分析 | ⚠️ 部分：真实机器人 K=4 时 0% SR，但未系统分析机制 |
| Cross-architecture 对比 | ❌ 测试了 π0/π0.5/SmolVLA 但未比较其压缩行为差异 |
| Re-encoding vs deletion | ❌ 无控制实验（隐含 continuous resampling > discrete deletion） |
| Closed-loop 评估 | ✅ LIBERO + ALOHA + SO-100 |

### F. 与我们的差异
- GridS 说"pruning 丢失几何信息，所以 resample"（方案论文）
- 我们说"pruning 能否 work 取决于 connector 架构，我们解释 why"（诊断/理解论文）
- GridS 测试了 SmolVLA 但未在 LIBERO 上做压缩实验，且未分析 pixel-shuffle 的 cliff-edge
- **风险**: 审稿人可能要求与 GridS 对比。应 frame 为 orthogonal（我们的分析解释了 GridS 为什么在某些架构上必要）

---

## 总结对比表

| 维度 | Compressor-VLA | SpecPrune-VLA | LightVLA | GridS (See What Matters) | **我们的工作** |
|------|---------------|---------------|----------|--------------------------|-------------|
| **Training** | Required (150K) | Free | Required (40K) | Required (30-50K) | **Free + Re-encoding** |
| **基础 VLA** | OpenVLA-OFT | OpenVLA-OFT, π₀ | OpenVLA-OFT | π0, π0.5, SmolVLA | **SmolVLA, OpenVLA** |
| **含 SmolVLA** | ❌ | ❌ | ❌ (仅对比) | ✅ (仅真实机器人) | **✅ (核心)** |
| **Connector 分析** | ❌ | ❌ | ❌ | ❌ | **✅ pixel-shuffle vs MLP vs cross-attn** |
| **压缩策略** | Reconstruction | Deletion | Deletion (learned) | Continuous resampling | **Deletion + Re-encoding 对比** |
| **Token 压缩比** | 512→160 (3.2×) | ~60-70% reduction | 512→78 (6.6×) | 256→16 (16×) | **多级对比** |
| **Cliff-edge 分析** | ❌ | ❌ | ❌ | ⚠️ 部分 | **✅ 核心发现** |
| **Cross-architecture** | ❌ | ❌ | ❌ | ❌ | **✅ 核心贡献** |
| **Re-encoding vs deletion** | ❌ | ❌ | ❌ | ❌ | **✅ 控制实验** |
| **Closed-loop eval** | ✅ | ✅ | ✅ | ✅ | **✅** |
| **Error bars** | ❌ | ❌ | ❌ | ❌ (LIBERO) | **✅ Wilson CI, multi-seed** |
| **LIBERO suites** | 4/4 | 4/4 | 4/4 | 4/4 | **4/4** |

### 我们的独特贡献 vs 全部 4 篇

1. **Cliff-edge 发现**: 4 篇论文中无一系统分析 pixel-shuffle connector 下 token deletion → 0% SR 的突变现象。这是全新发现。

2. **Architecture-dependent compressibility**: 所有 4 篇都在"安全"架构上实验（MLP projector 或 flow-matching），未探索 connector 类型如何决定压缩可行性边界。

3. **Re-encoding vs deletion 控制实验**: 4 篇中无一做过严格的控制对比。Compressor-VLA 和 GridS 隐含支持 re-encoding，但缺乏隔离变量的实验。

4. **SmolVLA 深度分析**: SmolVLA 仅在 GridS 真实机器人实验中出现，LIBERO 压缩实验中无人测试 SmolVLA。我们是第一个在 SmolVLA 上做系统性 token 压缩分析的工作。

5. **实验严谨性**: 4 篇均无 error bars（LIBERO），我们有 multi-seed + Wilson confidence interval。

6. **科学 vs 工程**: 4 篇都是"提出更好的压缩方法"，我们是"解释为什么压缩在某些架构上根本不可行"——complementary but distinct contribution。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_deep_analysis_competitors_20260519T013824"
}
```

</details>

---
