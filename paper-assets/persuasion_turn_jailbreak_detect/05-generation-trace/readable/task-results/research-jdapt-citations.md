# research jdapt citations

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_jdapt_citations_20260522T082145_result.json`
- **Structured JSON:** [`679ea94487772526315c.json`](../../sessions/67/679ea94487772526315c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕，以下是完整分析。

---

## J-DAPT 详细分析

**标题：** Preventing Robotic Jailbreaking via Multimodal Domain Adaptation

**作者：** Francesco Marchiori, Rohan Sinha, Christopher Agia, Alexander Robey, George J. Pappas, Mauro Conti, Marco Pavone

**发布：** 2025-09-27, arXiv preprint (无正式 venue)

**方法：**
- 多模态框架（文本 + 视觉），通过 attention-based cross-modal fusion 融合文本和视觉嵌入
- 使用 CORAL-based domain adaptation + importance-weighted training，将通用越狱数据集对齐到机器人领域
- **有受控消融**：multimodal fusion alone vs. domain adaptation alone vs. full pipeline (J-DAPT)，在多个 embedding model 上对比
- 不是单纯的"DAPT 应用"，而是多组件消融

**数据：**
- 评估域：autonomous driving, maritime robotics, quadruped navigation
- **Single-turn 攻击**，针对 LLM/VLM 控制的机器人系统
- 不涉及 multi-turn persuasion 攻击

**核心发现：**
- J-DAPT 平均拦截 98.85% 的越狱攻击
- 比最快的 LLM detector 快 9.9×
- Fusion alone 对部分模型提升大，DA alone 提升有限，full pipeline 最优

**关键话题覆盖：**
| 话题 | 是否讨论 |
|------|---------|
| Label sensitivity / label correctness | 否 |
| Representation mechanism / 为什么 DAPT works | 否（仅验证有效性，未做机制分析） |
| Benign-side FPR / distribution shift | 有限（报告了检测准确率，但未专门分析 benign 端） |
| Cross-attack OOD generalization | 否（仅跨域/跨 embedding model，非跨攻击类型 OOD） |

**与我们的关键差异：**
- J-DAPT 针对 **机器人多模态** 越狱，我们针对 **LLM 文本 multi-turn persuasion** 越狱 — 问题域完全不同
- J-DAPT 的 "domain adaptation" 是跨应用域（通用→机器人），我们的 DAPT 是 discriminative fine-tuning
- J-DAPT 无 label sensitivity 分析、无 representation mechanism 探究、无 benign adaptation
- J-DAPT 有多模态融合消融，但未做我们的 7 变体消融（compression 方向）

**我们的新颖性优势（J-DAPT 不具备的）：**
- 7 变体消融 + discriminative compression 机制发现
- 条件性标签敏感性（TOST）
- 两轴分解（attack-side vs benign-side）
- 10-shot benign adaptation
- 24.3× speedup
- Multi-turn persuasion 攻击场景

**他们有什么我们没有的：**
- 多模态（视觉+文本）融合能力
- 跨应用域（driving/maritime/quadruped）的泛化验证
- 重要性加权训练策略

---

## 补充引用

| 论文 | 标题 | Venue | 一句话摘要 | 是否引用 | 理由 |
|------|------|-------|-----------|---------|------|
| TrajGuard (2604.07727) | TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense | arXiv 2026-04 preprint | Training-free decoding-time defense，用 hidden-state trajectory 滑动窗口实时量化风险，12 种攻击上平均 95% 防御率，5.2ms/token 延迟 | **是 — Related Work** | Representation-based 方法，用 hidden states 做检测，与我们的 internal representation 路线直接相关；但它是 decoding-time single-turn defense，不涉及 multi-turn |
| SAE Jailbreak Mitigators (2602.12418) | Sparse Autoencoders are Capable LLM Jailbreak Mitigators | arXiv 2026-02 preprint | 提出 CC-Delta，用 SAE sparse features 做 inference-time mean-shift steering 防御越狱，在 sparse space 优于 dense steering，尤其 OOD 攻击 | **是 — Related Work** | Representation-based + interpretability 路线（SAE features），与我们的 representation mechanism 分析有方法论关联；他们做 steering 而非 detection，但 sparse feature 视角值得引用 |
| Jailbreaking Leaves a Trace (2602.11495) | Jailbreaking Leaves a Trace: Understanding and Detecting Jailbreak Attacks from Internal Representations of LLMs | arXiv 2026-02 preprint | 用 tensor decomposition 做 layer-wise 分析，发现越狱和正常 prompt 在内部表征有 layer-dependent 签名差异，跨 GPT-J/LLaMA/Mistral/Mamba 验证 | **是 — Related Work（高优先）** | 与我们最直接相关：都是从 internal representation 理解 jailbreak detection 机制。他们用 tensor decomposition 做可解释性，我们用 discriminative compression；互为补充视角 |
| Alon & Kamfonas 2023 (2308.14132) | Detecting Language Model Attacks with Perplexity | arXiv 2023-08 preprint | 用 GPT-2 计算 input perplexity 检测 adversarial suffix 越狱，对 suffix 攻击有效但对 human-crafted 攻击失败 | **可选引用** | 经典 perplexity-based baseline，方法论完全不同（surface-level statistical signal vs. internal representation）；在 Related Work 一句话提及 surface-level detection 方法即可 |
| Phute et al. 2023 (2308.07308) | LLM Self Defense: By Self Examination, LLMs Know They Are Being Tricked | ICLR 2024 Tiny Paper | 让 LLM 自检生成内容是否有害，无需 fine-tuning，attack success rate 降至~0% | **可选引用** | Output-based self-examination 方法，与我们的 input-side representation detection 路线不同；可在 Related Work 作为 output-side defense 的代表一句话提及 |

---

**总结判断：**
- **J-DAPT** 与我们的工作问题域差异大（robotic multimodal vs. LLM text multi-turn），但名字中的 "DAPT" 容易引起混淆，建议在论文中明确区分，Related Work 中简短提及其跨域适应思路。
- **高优先引用**：Jailbreaking Leaves a Trace（representation mechanism 最相关）、TrajGuard（hidden-state detection 路线）、SAE Mitigators（sparse representation 视角）
- **可选引用**：Alon & Kamfonas（perplexity baseline）、Phute（self-examination baseline）

Sources:
- [J-DAPT (arXiv:2509.23281)](https://arxiv.org/abs/2509.23281)
- [J-DAPT Project Page](https://j-dapt.github.io/)
- [TrajGuard (arXiv:2604.07727)](https://arxiv.org/abs/2604.07727)
- [SAE Jailbreak Mitigators (arXiv:2602.12418)](https://arxiv.org/abs/2602.12418)
- [Jailbreaking Leaves a Trace (arXiv:2602.11495)](https://arxiv.org/abs/2602.11495)
- [Alon & Kamfonas 2023 (arXiv:2308.14132)](https://arxiv.org/abs/2308.14132)
- [Phute et al. 2023 (arXiv:2308.07308)](https://arxiv.org/abs/2308.07308)

---
