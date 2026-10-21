# paper research bib sync

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/chats/worker_paper_research_bib_sync_20260517T174600.jsonl`
- **Structured JSON:** [`ee79948c9aa7d878930d.json`](../../sessions/ee/ee79948c9aa7d878930d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

27 recorded events

### Tool call

_source line 1 · 2026-05-17T17:50:31.284819+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T17:50:31.285369+00:00_

File content (48306 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T17:50:31.285624+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T17:50:31.285871+00:00_

1	# Literature Map for faith-evidence-ie (FREIGE)
2	# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE
3	# Updated: 2026-05-16 (W4 expanded: +11 papers from literature scan; +15 papers from Related Work survey; +17 papers from Related Work expansion; +16 papers from Related Work extension scan; +15 papers from 2026-05-16 incremental scan; +9 papers from Related Work targeted expansion; +6 papers from evidence cost literature scan; +11 papers from related work foundational survey)
4	
5	papers:
6	
7	  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===
8	
9	  - title: "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization"
10	    authors: NVIDIA Labs
11	    year: 2025
12	    venue: ICML 2026
13	    url: https://arxiv.org/abs/2601.05242
14	    category: reward_diversity
15	    role: closest_prior_work
16	    key_finding: >
17	      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，
18	      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，
19	      保留多 reward 的相对差异，显著提升训练稳定性。
20	    relevance_to_ced_stabilizer: >
21	      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），
22	      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。
23	      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。
24	
25	  - title: "DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs"
26	    authors: Xiwen Chen et al.
27	    year: 2025
28	    venue: arXiv 2505.09655
29	    url: https://arxiv.org/abs/2505.09655
30	    category: reward_diversity
31	    role: related_method
32	    key_finding: >
33	      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。
34	      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，
35	      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。
36	    relevance_to_ced_stabilizer: >
37	      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信
…[truncated 7443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T17:50:31.286068+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "AutoRE|DocKS-RAG|R1-RE|Scaling Laws for Reward Model|LoRA: Low-Rank|RL Is Neither a Panacea|DREEAM|Confronting Reward Model|Direct Preference Optimization|DeepSeekMath",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "output_mode": "content",
  "-n": "True",
  "-A": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Grep",
  "tool_args": {
    "pattern": "AutoRE|DocKS-RAG|R1-RE|Scaling Laws for Reward Model|LoRA: Low-Rank|RL Is Neither a Panacea|DREEAM|Confronting Reward Model|Direct Preference Optimization|DeepSeekMath",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "output_mode": "content",
    "-n": "True",
    "-A": "6"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T17:50:31.286321+00:00_

254:  - title: "Confronting Reward Model Overoptimization with Constrained RLHF"
255-    authors: Anonymous
256-    year: 2025
257-    venue: OpenReview
258-    url: https://openreview.net/forum?id=gkfUvn0fLU
259-    category: multi_objective_rl
260-    role: related_analysis
--
337:  - title: "R1-RE: Cross-Domain Relation Extraction with RLVR"
338-    authors: Runpeng Dai, Tong Zheng et al.
339-    year: 2025
340-    venue: arXiv 2507.04642
341-    url: https://arxiv.org/abs/2507.04642
342-    category: rl_for_ie
343-    role: direct_competitor
--
346:      将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。
347-      Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。
348-      triplet extraction 用 F1-based reward（entity weight=1, triplet weight=3）。
349-      未报告 catastrophic forgetting——GRPO 训练后在 MATH-500/IFEval/GPQA 上性能不降反升，
350-      说明句子级 RE 的简单 reward 结构足以稳定 GRPO 训练。
351-    results:
352-      sem2010_in_domain: 91.8
--
359:      (1) R1-RE 是句子级 RE，GRPO 成功；我们是文档级 RE，GRPO 失败→RSFT 成功。
360-      句子级 RE 每个 sample 只有 1 个 triple（binary classification），reward variance 天然充足；
361-      文档级 RE 每个 sample 有数十个 triple，F1 score 作为 reward 在 group 内趋于同质化（frac_zero_std→0.8）。
362:      (2) R1-RE 未报告 catastrophic forgetting，进一步支持"句子级简单 reward 可行，文档级需要 CED"的论点。
363:      (3) R1-RE 关注 OOD 泛化，无 evidence 组件；我们关注 evidence-grounded extraction quality。
364:      互补而非直接冲突——R1-RE 证明 RLVR for RE 可行，我们揭示文档级需要额外设计。
365-
366-  - title: "MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL"
367-    authors: Anonymous
368-    year: 2026
369-    venue: arXiv 2603.09478
370-    url: https://arxiv.org/abs/2603.09478
--
483:      具体 F1 未公开获取（Springer 付费墙），但声称超越 AutoRE 等 LLM baseline。
484-    results:
485-      note: "behind Springer paywall; claims SOTA over LLM baselines on DocRED/Re-DocRED/DWIE"
486-    evidence_generation: false
487-    relevance_to_rsft_docre: >
488-      规则约束方式与我们的 CED reward 在 motivation 上相似（都是引入外部知识约束），
489-  
…[truncated 3883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T17:50:31.286536+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Adaptive Focal Loss and Knowledge Distillation|Revisiting DocRED|GenRES|SAIS: Supervising|EIDER: Empowering|LMRC|DocRED: A Large-Scale|STaR: Bootstrapping|E-GRPO|ATLOP|Adaptive Thresholding and Localized",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "output_mode": "content",
  "-n": "True",
  "-A": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Adaptive Focal Loss and Knowledge Distillation|Revisiting DocRED|GenRES|SAIS: Supervising|EIDER: Empowering|LMRC|DocRED: A Large-Scale|STaR: Bootstrapping|E-GRPO|ATLOP|Adaptive Thresholding and Localized",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "output_mode": "content",
    "-n": "True",
    "-A": "6"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T17:50:31.286729+00:00_

447:  - title: "LMRC: LLM with Relation Classifier for Document-Level Relation Extraction"
448-    authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang
449-    year: 2024
450-    venue: arXiv 2408.13889
451-    url: https://arxiv.org/abs/2408.13889
452-    category: llm_docre
453-    role: related_method
--
457:      注意：LMRC 依赖 BERT-based classifier 作为预筛选，非纯 LLM 方法。
458-    results:
459-      docred_dev_ign_f1: 58.16
460-      docred_dev_f1: 59.97
461-      docred_test_ign_f1: 58.49
462-      docred_test_f1: 60.52
463-      re_docred_test_ign_f1: 74.08
--
468:      LMRC 在 DocRED test F1=60.52, Re-DocRED test F1=74.63，性能显著高于纯 LLM 方法。
469-      但它依赖 BERT classifier 预筛选，本质上是 hybrid 方法而非纯 LLM generative。
470-      与我们端到端 LLM 生成方式不同——我们通过 RSFT 的 reward-based filtering 隐式解决 class imbalance。
471-
472-  - title: "Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction"
473-    authors: Anonymous
474-    year: 2025
--
1371:  - title: "E-GRPO: Entity-Aware Reward for Group Relative Policy Optimization"
1372-    authors: Unknown
1373-    year: 2025
1374-    venue: ICLR 2026
1375-    url: https://arxiv.org/pdf/2510.24694
1376-    category: grpo_structured
1377-    role: closest_prior_work
--
1383:      E-GRPO 的 entity-aware partial credit 与我们 CED reward 的设计理念高度一致——
1384-      都是引入 task-specific fine-grained reward signal 替代 binary reward。
1385:      差异在于 E-GRPO 用 entity match 作为 reward，我们用 evidence quality (NLI-based)。
1386:      E-GRPO 是 training-time reward，CED 是 inference-time reranking。
1387-
1388-  - title: "RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs"
1389-    authors: Hangzhan Jin et al.
1390-    year: 2025
1391-    venue: arXiv 2508.16546
1392-    url: https://arxiv.org/abs/2508.16546
--
2342:  - title: "DocRED: A Large-Scale Document-Level Relation Extraction Dataset"
2343-    authors: Yuan Yao, Deming Ye, Peng Li, Xu Han, Yankai Lin, Zhenghao Liu, Zhiyuan Liu, L
…[truncated 3579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T17:50:31.286919+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "LoRA: Low-Rank Adaptation|DeepSeekMath|Scaling Laws for Reward|EIDER: Empowering",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "output_mode": "content",
  "-n": "True",
  "-A": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Grep",
  "tool_args": {
    "pattern": "LoRA: Low-Rank Adaptation|DeepSeekMath|Scaling Laws for Reward|EIDER: Empowering",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "output_mode": "content",
    "-n": "True",
    "-A": "6"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T17:50:31.287054+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T17:50:31.287175+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "LoRA|DeepSeekMath|Scaling Laws|EIDER|Direct Preference Optimization",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "output_mode": "content",
  "-n": "True",
  "-A": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Grep",
  "tool_args": {
    "pattern": "LoRA|DeepSeekMath|Scaling Laws|EIDER|Direct Preference Optimization",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "output_mode": "content",
    "-n": "True",
    "-A": "6"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T17:50:31.287465+00:00_

525:      RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE。
526-      关键设计：先抽 relation，再抽 head entity，最后抽 fact triple。
527-    results:
528-      re_docred_dev_f1_mistral: 53.01
529-      re_docred_test_f1_mistral: 51.91
530-      re_docred_dev_f1_vicuna: 54.29
531-      re_docred_test_f1_vicuna: 53.84
--
536:      backbone: "Mistral-7B / Vicuna-7B / LLaMA3-8B (QLoRA)"
537-    evidence_generation: false
538-    relevance_to_rsft_docre: >
539:      QLoRA fine-tuning for DocRE 的先例。AutoRE_LLaMA3-8B 在 Re-DocRED test F1=51.97,
540-      DocRED test F1=45.96。我们的 SFT baseline 与之类似，
541-      RSFT 在此基础上引入 reward-guided sample selection 进一步提升。
542-
543-  # === Category 9: Evidence Generation & Task Performance Trade-off ===
544-  # (NEW - 2026-05-15 evidence generation survey)
545-
--
575:      最直接的 DocRE + evidence 先例。EIDER 的核心洞察是 evidence 需要 inference-stage 融合
576-      而非 joint generation——暗示 joint generation 会引入 noise。
577-      我们的 CED reranker 是 LLM-era 版本的 inference-stage fusion：
578-      先生成多个候选（含 evidence），再用 NLI 在推理阶段选最佳。
579-      Related Work 引用点：encoder-based DocRE 中 evidence 的使用方式，与我们 generative 范式的关键差异。
580-
581-  - title: "Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales"
--
728:      (3) EvidenceRL 不涉及 task decoupling 现象（QLoRA-specific）；
729-      (4) EvidenceRL 无 inference-time reranking（CED reranker）。
730-      定位策略：EvidenceRL 证明 evidence-grounded RL 在 QA 域有效，
731-      我们揭示 DocRE structured output 带来的独特挑战（evidence tax、task decoupling）和解法（CED reranker）。
732-
733-  # === Category 14: Multi-Objective GRPO (NEW - 2026-05-15 scan) ===
734-
--
801:      QLoRA 的 compressed representation space 下，模型可能将 extraction 和 evidence
802-      两个子目标压缩到部分重叠的 proxy 空间，导致 optimization amplification
803-      使模型专注于更容易优化的 extraction 而忽略 evidence。
804-      bf16 下不复现可能因为 full-rank update 的 representation space 更充裕。
805-
806-  # === Category 16: Training Precision & RL Stability (NEW - 2026-05-15 
…[truncated 9254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T17:50:31.287667+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "EIDER: Empowering Document-level",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "output_mode": "content",
  "-n": "True",
  "-A": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Grep",
  "tool_args": {
    "pattern": "EIDER: Empowering Document-level",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "output_mode": "content",
    "-n": "True",
    "-A": "8"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T17:50:31.287803+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T17:50:31.287924+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "EIDER",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "output_mode": "content",
  "-n": "True",
  "-A": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Grep",
  "tool_args": {
    "pattern": "EIDER",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "output_mode": "content",
    "-n": "True",
    "-A": "8"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T17:50:31.288054+00:00_

575:      最直接的 DocRE + evidence 先例。EIDER 的核心洞察是 evidence 需要 inference-stage 融合
576-      而非 joint generation——暗示 joint generation 会引入 noise。
577-      我们的 CED reranker 是 LLM-era 版本的 inference-stage fusion：
578-      先生成多个候选（含 evidence），再用 NLI 在推理阶段选最佳。
579-      Related Work 引用点：encoder-based DocRE 中 evidence 的使用方式，与我们 generative 范式的关键差异。
580-
581-  - title: "Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales"
582-    authors: Resck, Raimundo, Poco
583-    year: 2024

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T17:50:31.288183+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Empowering Document-level Relation Extraction",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "output_mode": "content",
  "-n": "True",
  "-A": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Empowering Document-level Relation Extraction",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "output_mode": "content",
    "-n": "True",
    "-A": "8"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T17:50:31.288339+00:00_

563:  - title: "Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion"
564-    authors: Xie et al. (Google Research)
565-    year: 2022
566-    venue: ACL Findings 2022
567-    url: https://arxiv.org/abs/2106.08657
568-    category: evidence_generation_tradeoff
569-    role: closest_docre_precedent
570-    key_finding: >
571-      Joint 训练 RE + evidence extraction，关键创新在 inference-stage fusion：

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T17:50:31.288485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "offset": "2404",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "offset": "2404",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T17:50:31.288629+00:00_

2404	  - title: "SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction"
2405	    authors: Ruoting Xie, Jingqi Wang, Wei Cai, Runxin Xu, Baobao Chang
2406	    year: 2022
2407	    venue: NAACL 2022
2408	    url: https://aclanthology.org/2022.naacl-main.171/
2409	    category: evidence_supervised_docre
2410	    role: direct_competitor
2411	    key_finding: >
2412	      通过 supervising intermediate steps（evidence retrieval）来提升 DocRE。
2413	      两阶段 evidence retrieval：pooled evidence retrieval 区分有/无 supporting sentences 的 entity pairs，
2414	      fine-grained evidence retrieval 为每个 relation 生成 interpretable evidence。
2415	      在 DocRED/CDR/GDA 三个 benchmark 上达到 SOTA，evidence F1 超越 runner-up 5.04%。
2416	    relevance_to_freige: >
2417	      最直接的 prior work——同时做 RE 和 evidence prediction 的代表方法。
2418	      关键区别：SAIS 是 encoder-based discriminative model 用 attention supervision，
2419	      FREIGE 是 generative LLM 用 text-level evidence generation。
2420	      SAIS 发现 evidence supervision 提升 RE，而 FREIGE 发现 generative evidence 有 ~8pp cost，
2421	      这个差异正是 FREIGE 论文的核心发现之一。
2422	
2423	  # === Category 39: Knowledge Distillation for DocRE ===
2424	
2425	  - title: "Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation"
2426	    authors: Qingyu Tan, Ruidan He, Lidong Bing, Hwee Tou Ng
2427	    year: 2022
2428	    venue: Findings of ACL 2022
2429	    url: https://aclanthology.org/2022.findings-acl.132/
2430	    category: knowledge_distillation_docre
2431	    role: background
2432	    key_finding: >
2433	      KD-DocRE：用 axial attention 学习 entity pair 间依赖关系，

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T17:50:31.288817+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/ 2>/dev/null",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/ 2>/dev/null",
    "description": "List paper directory contents"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T17:50:31.288945+00:00_

acl-style
acl.sty
acl_natbib.bst
main.tex
references.bib
sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T17:50:31.289063+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T17:50:31.289179+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T17:50:31.289486+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib",
  "content": "@inproceedings{autore2024,\n  title     = {{AutoRE}: Document-Level Relation Extraction with Large Language Models},\n  author    = {{Anonymous}},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2403.14888}\n}\n\n@inproceedings{chen2025docksrag,\n  title     = {{DocKS-RAG}: Optimizing Document-Level Relation Extraction through {LLM}-Enhanced Hybrid Prompt Tuning},\n  author    = {Xu and others},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},\n  year      = {2025},\n  url       = {https://proceedings.mlr.press/v267/xu25am.html}\n}\n\n@article{dai2025r1re,\n  title   = {{R1-RE}: Cross-Domain Relation Extraction with {RLVR}},\n  author  = {Dai, Runpeng and Zheng, Tong and others},\n  journal = {arXiv preprint arXiv:2507.04642},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2507.04642}\n}\n\n@inproceedings{gao2023scaling,\n  title     = {Scaling Laws for Reward Model Overoptimization},\n  author    = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2210.10760}\n}\n\n@inproceedings{hu2022lora,\n  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2106.09685}\n}\n\n@article{jin2025rl_panacea,\n  title   = {{RL} Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for {LLMs}},\n  author  = {Jin, Hangzhan and others},\n  journal = {arXiv preprint arXiv:2508.16546},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2508.16546}\n}\n\n@inproceedings{ma2023dreeam,\n  title     = {{DREEAM}: Guiding Attention with Evidence for Improving Document-Level Relation Extraction},\n  author    = {Ma, Youmi and Wang, An and Okazaki, Naoaki},\n  booktitle = {Findings of the Association for Computational Linguistics: EACL 2023},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2302.08675}\n}\n\n@inproceedings{moskovitz2024constrained,\n  title     = {Confronting Reward Model Overoptimization with Constrained {RLHF}},\n  author    = {Moskovitz, Ted and Singh, Aaditya K. and Strouse, DJ and Sandholm, Tuomas and Salakhutdinov, Ruslan and Dragan, Anca D. and McAleer, Stephen},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://openreview.net/forum?id=gkfUvn0fLU}\n}\n\n@inproceedings{rafailov2023direct,\n  title     = {Direct Preference Optimization: Your Language Model is Secretly a Reward Model},\n  author    = {Rafailov, Rafael and Sharma, Archit and Mitchell, Eric and Ermon, Stefano and Manning, Christopher D. and Finn, Chelsea},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2305.18290}\n}\n\n@article{shao2024deepseekmath,\n  title   = {{DeepSeekMath}: Pushing the Limits of Mathematical Reasoning in Open Language Models},\n  author  = {Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Bi, Xiao and Zhang, Haowei and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},\n  journal = {arXiv preprint arXiv:2402.03300},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2402.03300}\n}\n\n@inproceedings{tan2022kddocre,\n  title     = {Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation},\n  author    = {Tan, Qingyu and He, Ruidan and Bing, Lidong and Ng, Hwee Tou},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year      = {2022},\n  url       = {https://aclanthology.org/2022.findings-acl.132/}\n}\n\n@inproceedings{tan2022redocred,\n  title     = {Revisiting {DocRED}: Addressing the False Negative Problem in Relation Extraction},\n  author    = {Tan, Qingyu and Xu, Lu and Bing, Lidong and Ng, Hwee Tou and Aljunied, Sharifah Mahani},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year      = {2022},\n  url       = {https://aclanthology.org/2022.emnlp-main.580/}\n}\n\n@inproceedings{wan2024genres,\n  title     = {{GenRES}: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models},\n  author    = {Jiang, Pengcheng and Lin, Jiacheng and Wang, Zifeng and Sun, Jimeng and Han, Jiawei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n  year      = {2024},\n  url       = {https://aclanthology.org/2024.naacl-long.155/}\n}\n\n@inproceedings{xiao2022sais,\n  title     = {{SAIS}: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction},\n  author    = {Xiao, Yuxin and Zhang, Zecheng and Mao, Yuning and Yang, Carl and Han, Jiawei},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics},\n  year      = {2022},\n  url       = {https://aclanthology.org/2022.naacl-main.171/}\n}\n\n@inproceedings{xie2022eider,\n  title     = {{EIDER}: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion},\n  author    = {Xie, Yiqing and Shen, Jiaming and Li, Sha and Mao, Yuning and Han, Jiawei},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2106.08657}\n}\n\n@article{xu2024lmrc,\n  title   = {{LMRC}: {LLM} with Relation Classifier for Document-Level Relation Extraction},\n  author  = {Li, Xingzuo and Chen, Kehai and Long, Yunfei and Zhang, Min},\n  journal = {arXiv preprint arXiv:2408.13889},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2408.13889}\n}\n\n@inproceedings{yao2019docred,\n  title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n  author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n  year      = {2019},\n  url       = {https://aclanthology.org/P19-1074/}\n}\n\n@inproceedings{zelikman2022star,\n  title     = {{STaR}: Bootstrapping Reasoning With Reasoning},\n  author    = {Zelikman, Eric and Wu, Yuhuai and Mu, Jesse and Goodman, Noah D.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2203.14465}\n}\n\n@inproceedings{zhao2025egrpo,\n  title     = {{E-GRPO}: Entity-Aware Reward for Group Relative Policy Optimization},\n  author    = {{Anonymous}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2510.24694}\n}\n\n@inproceedings{zhou2021atlop,\n  title     = {Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling},\n  author    = {Zhou, Wenxuan and Huang, Kevin and Ma, Tengyu and Huang, Jing},\n  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2010.11304}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib",
    "content": "@inproceedings{autore2024,\n  title     = {{AutoRE}: Document-Level Relation Extraction with Large Language Models},\n  author    = {{Anonymous}},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2403.14888}\n}\n\n@inproceedings{chen2025docksrag,\n  title     = {{DocKS-RAG}: Optimizing Document-Level Relation Extraction through {LLM}-Enhanced Hybrid Prompt Tuning},\n  author    = {Xu and others},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},\n  year      = {2025},\n  url       = {https://proceedings.mlr.press/v267/xu25am.html}\n}\n\n@article{dai2025r1re,\n  title   = {{R1-RE}: Cross-Domain Relation Extraction with {RLVR}},\n  author  = {Dai, Runpeng and Zheng, Tong and others},\n  journal = {arXiv preprint arXiv:2507.04642},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2507.04642}\n}\n\n@inproceedings{gao2023scaling,\n  title     = {Scaling Laws for Reward Model Overoptimization},\n  author    = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2210.10760}\n}\n\n@inproceedings{hu2022lora,\n  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2106.09685}\n}\n\n@article{jin2025rl_panacea,\n  title   = {{RL} Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for {LLMs}},\n  author  = {Jin, Hangzhan and others},\n  journal = {arXiv preprint arXiv:2508.16546},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2508.16546}\n}\n\n@inproceedings{ma2023dreeam,\n  title     = {{DREEAM}: Guiding Attention with Evidence for Improving Document-Level Relation Extraction},\n  author    = {Ma, Youmi and Wang, An and Okazaki, Naoaki},\n  booktitle = {Findings of the Association for Computational Linguistics: EACL 2023},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2302.08675}\n}\n\n@inproceedings{moskovitz2024constrained,\n  title     = {Confronting Reward Model Overoptimization with Constrained {RLHF}},\n  author    = {Moskovitz, Ted and Singh, Aaditya K. and Strouse, DJ and Sandholm, Tuomas and Salakhutdinov, Ruslan and Dragan, Anca D. and McAleer, Stephen},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://openreview.net/forum?id=gkfUvn0fLU}\n}\n\n@inproceedings{rafailov2023direct,\n  title     = {Direct Preference Optimization: Your Language Model is Secretly a Reward Model},\n  author    = {Rafailov, Rafael and Sharma, Archit and Mitchell, Eric and Ermon, Stefano and Manning, Christopher D. and Finn, Chelsea},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2305.18290}\n}\n\n@article{shao2024deepseekmath,\n  title   = {{DeepSeekMath}: Pushing the Limits of Mathematical Reasoning in Open Language Models},\n  author  = {Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Bi, Xiao and Zhang, Haowei and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},\n  journal = {arXiv preprint arXiv:2402.03300},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2402.03300}\n}\n\n@inproceedings{tan2022kddocre,\n  title     = {Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation},\n  author    = {Tan, Qingyu and He, Ruidan and Bing, Lidong and Ng, Hwee Tou},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year      = {2022},\n  url       = {https://aclanthology.org/2022.findings-acl.132/}\n}\n\n@inproceedings{tan2022redocred,\n  title     = {Revisiting {DocRED}: Addressing the False Negative Problem in Relation Extraction},\n  author    = {Tan, Qingyu and Xu, Lu and Bing, Lidong and Ng, Hwee Tou and Aljunied, Sharifah Mahani},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year      = {2022},\n  url       = {https://aclanthology.org/2022.emnlp-main.580/}\n}\n\n@inproceedings{wan2024genres,\n  title     = {{GenRES}: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models},\n  author    = {Jiang, Pengcheng and Lin, Jiacheng and Wang, Zifeng and Sun, Jimeng and Han, Jiawei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n  year      = {2024},\n  url       = {https://aclanthology.org/2024.naacl-long.155/}\n}\n\n@inproceedings{xiao2022sais,\n  title     = {{SAIS}: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction},\n  author    = {Xiao, Yuxin and Zhang, Zecheng and Mao, Yuning and Yang, Carl and Han, Jiawei},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics},\n  year      = {2022},\n  url       = {https://aclanthology.org/2022.naacl-main.171/}\n}\n\n@inproceedings{xie2022eider,\n  title     = {{EIDER}: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion},\n  author    = {Xie, Yiqing and Shen, Jiaming and Li, Sha and Mao, Yuning and Han, Jiawei},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2106.08657}\n}\n\n@article{xu2024lmrc,\n  title   = {{LMRC}: {LLM} with Relation Classifier for Document-Level Relation Extraction},\n  author  = {Li, Xingzuo and Chen, Kehai and Long, Yunfei and Zhang, Min},\n  journal = {arXiv preprint arXiv:2408.13889},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2408.13889}\n}\n\n@inproceedings{yao2019docred,\n  title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n  author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n  year      = {2019},\n  url       = {https://aclanthology.org/P19-1074/}\n}\n\n@inproceedings{zelikman2022star,\n  title     = {{STaR}: Bootstrapping Reasoning With Reasoning},\n  author    = {Zelikman, Eric and Wu, Yuhuai and Mu, Jesse and Goodman, Noah D.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2203.14465}\n}\n\n@inproceedings{zhao2025egrpo,\n  title     = {{E-GRPO}: Entity-Aware Reward for Group Relative Policy Optimization},\n  author    = {{Anonymous}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2510.24694}\n}\n\n@inproceedings{zhou2021atlop,\n  title     = {Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling},\n  author    = {Zhou, Wenxuan and Huang, Kevin and Ma, Tengyu and Huang, Jing},\n  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2010.11304}\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T17:50:31.289722+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260517T174600",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-17T17:50:31.289896+00:00_

20 个 BibTeX entries 已写入 `references.bib`。

关键信息来源说明：
- 14 个从 literature_map.yaml 获取了完整的 title/authors/venue/url
- 4 个不在 lit map 中的知名论文（LoRA, DPO, DeepSeekMath, Scaling Laws）使用了任务补充信息 + 已知作者列表
- 2 个 lit map 中 authors 为 Anonymous/Unknown 的（autore2024, zhao2025egrpo）保留 `{Anonymous}`
- SAIS 和 EIDER 的 lit map 作者信息有误，已用任务补充信息修正
- 年份/venue 均按 Director 指令修正（LMRC=2024, DocKS-RAG=ICML 2025, DREEAM=EACL 2023, Re-DocRED=EMNLP 2022, GenRES=NAACL 2024）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_bib_sync_20260517T174600"
}
```

</details>

---
