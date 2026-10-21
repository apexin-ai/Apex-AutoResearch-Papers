# HarmThoughts 模型清单

## 数据集基本信息
- 来源: `ishitakakkar-10/HarmThoughts` (HuggingFace)
- 论文: 投稿中 (COLM 2026)
- 总条数: 56,931 sentences / 1,018 unique traces
- 数据粒度: 每行 = reasoning trace 中的一个句子（sentence-level annotation）
- 字段列表: `id`, `sentence_id`, `query`, `sentence`, `final_judgment`, `model_name`, `class`, `llm_annotation`, `model_response`

## 模型统计

| Code | Full Name | Base Model | Architecture | Sentences | Traces | Self-Jailbreak (broad) | Self-Jailbreak (strict/RS) | RS Sentences |
|------|-----------|-----------|-------------|-----------|--------|----------------------|--------------------------|-------------|
| ot-7b | OpenThinker-7B | Qwen2.5-7B | **Qwen** | 26,653 | 333 | 281 (84.4%) | 63 (18.9%) | 217 |
| r1-8b | DeepSeek-R1-Distill-Llama-8B | Llama-3.1-8B | **Llama** | 14,746 | 324 | 270 (83.3%) | 26 (8.0%) | 32 |
| r1-32b | DeepSeek-R1-Distill-Qwen-32B | Qwen2.5-32B | **Qwen** | 8,525 | 221 | 179 (81.0%) | 23 (10.4%) | 34 |
| QwQ | QwQ-32B | Qwen2.5-32B | **Qwen** | 7,007 | 140 | 115 (82.1%) | 11 (7.9%) | 13 |

### 定义说明
- **Self-Jailbreak (broad)**: trace 同时包含安全意识标签 (RS/RA/CR/IR/PS) 和有害执行标签 (DKE/TD/HV/CE)
- **Self-Jailbreak (strict/RS)**: trace 包含 RS (Refusal Suppression) 标签 + 有害执行标签
- **RS**: 模型在推理中出现的 refusal suppression 行为（先意识到应拒绝，然后压制拒绝继续执行）

### Annotation Taxonomy
| Label | Meaning | Count |
|-------|---------|-------|
| DKE | Domain Knowledge Execution | 22,310 |
| TD | Task Decomposition | 8,134 |
| IA | Intent Acknowledgment | 7,849 |
| FL | Formulation/Logic | 4,253 |
| RA | Risk Acknowledgment | 2,919 |
| CE | Compliance Escalation | 2,433 |
| OB | Obedience | 1,966 |
| HV | Harm Validation | 1,566 |
| AL | Autonomy Loss | 1,401 |
| IR | Intent Rationalization | 780 |
| ED | Ethical Dismissal | 750 |
| PS | Post-hoc Safety disclaimer | 678 |
| CR | Conditional Reasoning | 660 |
| CC | Context Compliance | 530 |
| PA | Permission Assumption | 406 |
| RS | Refusal Suppression | 296 |

## 架构分布

| Architecture | Models | Total Traces | Total Sentences |
|-------------|--------|-------------|----------------|
| **Qwen** | OpenThinker-7B, R1-Distill-Qwen-32B, QwQ-32B | 694 | 42,185 |
| **Llama** | R1-Distill-Llama-8B | 324 | 14,746 |

## Path A 候选分析

### 核心问题：是否有非 Qwen/Llama 架构 + reasoning + self-jailbreak？

**否。** HarmThoughts 只包含 Qwen 和 Llama 两个架构族。没有 Mistral / Gemma / 其他架构的 reasoning model。

### 但是：Llama 架构的存在部分解决 architecture confound

- **DeepSeek-R1-Distill-Llama-8B** 是 Llama-3.1-8B 架构
- 它与 Qwen 系模型表现出相似的 self-jailbreak 率（broad: 83.3% vs Qwen 系 81-84%）
- 这说明 self-jailbreak 现象不是 Qwen 特有的

### ≥100 条 jailbreak traces 要求

| 定义 | ot-7b | r1-8b | r1-32b | QwQ | 满足? |
|------|-------|-------|--------|-----|-------|
| Broad (safety+harmful) | 281 | 270 | 179 | 115 | **全部满足** |
| Strict (RS+harmful) | 63 | 26 | 23 | 11 | **均不满足** |

用 broad 定义（trace 中同时存在安全意识 + 有害执行），所有模型都有 >100 traces 可用。

### Llama vs Qwen 对比可行性

如果目标是证明 "self-jailbreak 现象跨架构存在"：
- Llama (r1-8b): 270 broad self-jailbreak traces
- Qwen (any): 575 broad self-jailbreak traces
- **完全足够做 cross-architecture 对比实验**

## 结论

1. **缺失的 26,653 条 = OpenThinker-7B**（Qwen2.5-7B 架构），是 trace 最长的模型（avg 80 sentences/trace）
2. **数据集有 2 个架构族**：Qwen (3 模型, 694 traces) + Llama (1 模型, 324 traces)
3. **没有 Mistral/Gemma 等第三架构**——如需完全排除 architecture confound，仍需外部数据
4. **但 Llama vs Qwen 对比已可行**：两个架构族的 self-jailbreak 率几乎相同 (~83%)，支持 "现象跨架构" 的论证
5. **OpenThinker-7B 的 strict RS 率最高** (18.9%)，是研究 refusal suppression 机制的最佳候选
