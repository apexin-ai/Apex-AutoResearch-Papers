# 文献调研：Instruction-Conditioned Representation Probing in VLAs/VLMs

Date: 2026-05-15

---

## 方向 1: Probing VLM/VLA Representations

### 1.1 Häon et al. — Mechanistic Interpretability for Steering VLAs
- **引用**: Bear Häon, Kaylene Stocking, Ian Chuang, Claire Tomlin. *Mechanistic interpretability for steering vision-language-action models.* CoRL 2025, PMLR 305:2743–2762.
- **arXiv**: 2509.00328
- **核心方法**: 将 VLA (Pi0, OpenVLA) 的 feedforward activations 投影到 token embedding space，识别与动作控制因果相关的稀疏语义方向（speed, direction），用 activation steering 实现零 shot 行为调控。
- **与我们的关系**: **直接互补**。他们做 mechanistic interpretability（causal intervention），我们做 representation probing（diagnostic）。他们证明 VLA 内部存在可解释的语义方向，我们证明 trained vs untrained 的表征差异来源于哪里。他们在 LIBERO 上验证，可直接对比。
- **可引用点**: 证据表明 VLA 内部确实编码了语义丰富的方向，支持我们 probing 的合理性。他们没有做 trained vs untrained 对比，也没有分析 language instruction 的 encoding。

### 1.2 ★★★ Grant, Zhao & Wang — Not All Features Are Created Equal
- **引用**: Bryce Grant, Xijia Zhao, Peng Wang. *Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models.* arXiv:2603.19233, March 2026.
- **核心方法**: 对 6 个 VLA（π0.5, OpenVLA-OFT, X-VLA, SmolVLA, GR00T, ACT）做 activation injection + SAE + linear probes，394K+ rollout episodes，4 个 benchmark。
- **关键发现**:
  - **Vision dominates**: 注入 baseline visual activations 可恢复 near-identical 行为，language sensitivity 是 suite-dependent
  - **LIBERO-Object**: language-insensitive（100% success regardless of prompt on OFT）
  - **LIBERO-Goal**: language-critical（正确 prompt 97-100% → 错误 prompt 0-10%）
  - π0.5 Layer 17: 99.3% prompt classification accuracy，但行为不受 prompt 影响 → **"encoded but not used" paradox**
  - Cross-task injection: 0-2.6% success but 99.8% trajectory alignment → "spatially bound motor programs"
- **与我们的关系**: **最直接的竞争者/互补者**。他们做 behavioral intervention（改 prompt 看行为变化），我们做 representation probing（训 probe 看 hidden states 编码了什么）。**关键区别**: 他们没有 trained vs untrained 对比，没有 layer × timestep 的细粒度 probing。他们的 "encoded but not used" 发现恰好是我们可以深入解释的。
- **可引用点**: LIBERO-Goal 是 language-critical suite 的最佳证据；"encoded but not used" paradox 是我们 probing 要解释的现象。

### 1.3 Lu et al. — Probing OpenVLA for Symbolic States
- **引用**: Hong Lu, Hengxu Li, Prithviraj Singh Shahani, Stephanie Herbers, Matthias Scheutz. *Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture.* arXiv:2502.04558, Feb 2025.
- **核心方法**: 在 OpenVLA 的 Llama backbone 33 层上训练 linear probes，提取 symbolic predicates（on(obj1, obj2), grasped(obj) 等），集成到 DIARC 认知架构。
- **关键发现**: 所有 33 层 accuracy > 0.90（object & action states）。预期的 "object states 在前、action states 在后" 的 layer-wise pattern 未出现。
- **与我们的关系**: **方法论上最接近**。都是对 OpenVLA hidden states 做 linear probing。但他们 probe 的是 symbolic predicates（二值分类），我们 probe 的是 goal classification 和 temporal distance（连续回归 + 多分类）。他们没有 trained vs untrained 对比，没有在 vision-ambiguous 场景测试。
- **可引用点**: 确认 OpenVLA hidden states 可被 linear probe decode，支持我们方法的可行性。

### 1.4 Molinari et al. — Emergent World Representations in OpenVLA
- **引用**: Marco Molinari, Leonardo Nevali, Saharsha Navani, Omar G. Younis. *Emergent World Representations in OpenVLA.* arXiv:2509.24559, Sep 2025.
- **核心方法**: Embedding arithmetic on state representations + linear/nonlinear probes 分析 OpenVLA 是否编码 implicit world model。SAE 做 deeper analysis。
- **关键发现**: OpenVLA 确实编码 state transition knowledge（超越 baseline 的统计显著性），world model 随训练逐步涌现，集中在中间层。
- **与我们的关系**: **互补**。他们问 "VLA 是否学到了 world model"，我们问 "VLA 是否学到了 instruction grounding"。他们的 "world model in middle layers" 发现可与我们的 layer-wise probing 结果对比。
- **可引用点**: 证明 OpenVLA 中间层编码了超越 action 的结构化知识，支持我们对 instruction encoding 的 layer-wise 分析。

### 1.5 Neo et al. — Interpreting Visual Information Processing in VLMs
- **引用**: Clement Neo, Luke Ong, Philip Torr, Mor Geva, David Krueger, Fazl Barez. *Towards Interpreting Visual Information Processing in Vision-Language Models.* ICLR 2025.
- **arXiv**: 2410.07149
- **核心方法**: 分析 VLM 中 visual token 如何跨层演化——从原始视觉特征到可解释的文本概念。Ablation + logit lens。
- **关键发现**: Object information 高度 localized（移除 object-specific tokens → accuracy 下降 70%+）。Visual tokens 跨层逐步与 textual concepts 对齐。模型在 last token position 提取 object info。
- **与我们的关系**: **方法论参考**。他们的 layer-wise visual token 演化分析为我们理解 OpenVLA 中 instruction token vs vision token 的交互提供了框架。
- **可引用点**: VLM 中 visual representations 跨层演化的 canonical 分析，可用于解释我们的 layer-wise probing patterns。

---

## 方向 2: Language Grounding in Robot Learning

### 2.1 ★★★ LangForce / BayesianVLA — Information Collapse in VLAs
- **引用**: Shijie Lian et al. *BayesianVLA: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries.* arXiv:2601.15197, Jan 2026.
- **核心方法**: 识别 VLA 中的 **Information Collapse** 问题——language instruction 从视觉观测高度可预测时，模型退化为 vision-only policy。提出用 conditional PMI（pointwise mutual information）最大化 actions 与 instructions 之间的信息量。
- **关键发现**: 在 multi-task 场景中，VLA 倾向忽略 language 走 vision shortcut。LangForce 通过 Bayesian decomposition（vision-only prior + language-conditioned posterior）强制模型利用 language。
- **与我们的关系**: **理论上最直接相关**。他们从 information theory 角度解释了我们在 LIBERO-10 上观察到的现象（VLA 几乎不用 language）。我们的 probing 可以为 Information Collapse 提供 representation-level 的证据——在 vision-sufficient 场景中 instruction representation 是否退化/冗余？
- **可引用点**: Information Collapse 概念是我们整个 story 的理论框架。Vision-sufficient → language 被忽略 → vision-ambiguous → language 必须被利用。

### 2.2 Voltron — Language-Driven Representation Learning for Robotics
- **引用**: Siddharth Karamcheti, Suraj Nair, Annie S. Chen et al. *Language-Driven Representation Learning for Robotics.* RSS 2023.
- **核心方法**: 结合 language-conditioned visual reconstruction（学低级空间特征）和 visually-grounded language generation（学高级语义），在 Ego4D 视频上预训练 robot visual representations。
- **关键发现**: Language-driven representations 在需要高级语义的任务上显著优于 MAE/CLIP。三个变体（V-Cond, V-Dual, V-Gen）在 5 个 robot 任务上全面评测。
- **与我们的关系**: **互补**。Voltron 证明 language 可以改善 visual representations 的质量，但没有分析 trained representations 中 language information 的 encoding。我们的 probing 可以回答 "language-driven pretraining 到底在 hidden states 中留下了什么痕迹？"
- **可引用点**: Language 改善 robot visual representations 的 canonical work，支持我们 "language grounding matters" 的大 narrative。

### 2.3 R3M — Universal Visual Representation for Robot Manipulation
- **引用**: Suraj Nair, Aravind Rajeswaran, Vikash Kumar, Chelsea Finn, Abhinav Gupta. *R3M: A Universal Visual Representation for Robot Manipulation.* CoRL 2023, PMLR 205.
- **核心方法**: Time-contrastive learning + video-language alignment + L1 sparsity，在 Ego4D 上预训练。Frozen representation 用于下游 policy learning。
- **关键发现**: 12 个 simulated manipulation tasks 上比 scratch 高 20%+，比 CLIP/MoCo 高 10%+。真实 Franka 仅 20 demos 即可学会。
- **与我们的关系**: **Baseline 参考**。R3M 的 time-contrastive objective 与我们的 temporal distance probing 直接相关——都假设 temporal distance 反映 task progress。我们可以对比 R3M-style representations vs VLA representations 在 temporal distance probing 上的表现。
- **可引用点**: Time-contrastive learning 作为 representation quality 的 probe 的理论依据。

---

## 方向 3: Task Disambiguation via Language

### 3.1 Zhan et al. — Stable Language Guidance for VLAs
- **引用**: Zhihao Zhan, Yuhao Chen, Jiaying Zhou, Qinhan Lyu, Hao Liu, Keze Wang, Liang Lin, Guangrun Wang. *Stable Language Guidance for Vision-Language-Action Models.* ACL 2026.
- **arXiv**: 2601.04052
- **核心方法**: 识别 VLA 的 **modality collapse**——strong visual priors overwhelm sparse linguistic signals。提出 RSS（Residual Semantic Steering）: Monte Carlo Syntactic Integration + Residual Affordance Steering。
- **关键发现**: VLA 对 linguistic perturbations 极其脆弱，三类失败模式：destructive instruction overwriting, synonym reinterpretation, OOD semantic transfer。RSS 在对抗性语言扰动下维持性能。
- **与我们的关系**: **互补**。他们从 robustness 角度发现 modality collapse（= LangForce 的 information collapse），提出解决方案。我们从 representation probing 角度提供 diagnostic 证据。可以引用他们的 failure taxonomy 来 motivate 我们的研究。
- **可引用点**: Modality collapse 的三类失败模式分类，LIBERO 上的实验验证。

### 3.2 Grant et al. (同 1.2) — LIBERO-Goal 上的 Language Disambiguation
- 同论文 1.2，重点在于 LIBERO-Goal（同一 kitchen scene，10 个不同 goal）是测试 language disambiguation 的理想 benchmark。
- **关键数据**: LIBERO-Goal 上正确 prompt 97-100% vs 错误 prompt 0-10%（X-VLA, GR00T）。LIBERO-Object 上无论什么 prompt 都 100%。
- 这直接验证了我们的 hypothesis: 视觉信息不足以区分 task 时，language 变得关键。

---

## 方向 4: OpenVLA / RT-2 / Octo Interpretability

### 4.1 ★★★ VLM4VLA — Revisiting VLMs in VLA Models
- **引用**: Jianke Zhang, Xiaoyu Chen, Qiuyue Wang, Mingsheng Li, Yanjiang Guo, Yucheng Hu, Jiajun Zhang, Shuai Bai, Junyang Lin, Jianyu Chen. *VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models.* ICLR 2026.
- **arXiv**: 2601.03309
- **核心方法**: Minimal adaptation pipeline，将不同 VLM 公平转化为 VLA policy，在 Calvin/SimplerEnv/LIBERO 上评测。Modality-level ablation 分析 vision vs language 贡献。
- **关键发现**:
  - VLM 的 general capabilities（VQA, captioning 等）是 VLA 性能的 **poor predictor**
  - **Visual module 是 primary bottleneck**，不是 language
  - 注入 control-relevant visual supervision 可以提升性能（即使 frozen encoder）
  - 改善 VLM 的 embodied skills 不保证改善 VLA 控制
- **与我们的关系**: **强互补**。他们从 behavioral/benchmark 角度发现 "vision > language for VLA"，我们从 representation probing 角度提供层级证据。他们的 "vision is bottleneck" 结论与我们 LIBERO-10 上的发现一致。但在 LIBERO-Goal 上，language 应该变得重要——他们没有做这个对比。
- **可引用点**: VLM general capability ≠ VLA performance 是重要 baseline 认知。Vision module 作为 bottleneck 的 modality ablation 证据。

### 4.2 Wen et al. — Data-Centric Revisit of Pre-Trained Vision Models
- **引用**: Xin Wen, Bingchen Zhao, Yilun Chen, Jiangmiao Pang, Xiaojuan Qi. *A Data-Centric Revisit of Pre-Trained Vision Models for Robot Learning.* CVPR 2025.
- **核心方法**: 对比 DINO/iBOT/MAE 在 visuomotor control + perception 上的表现，提出 SlotMIM（object-centric representation via semantic bottleneck）。
- **关键发现**: DINO/iBOT 在 object-centric 数据上优秀但在 non-object-centric 数据上退化。Object-centric representation 是 robot learning PVM 成功的关键。
- **与我们的关系**: **Baseline 解释**。解释了为什么我们的 DINO baseline 在 temporal distance probing 上表现强劲（ρ=0.901）——DINO 的 object-centric features 天然适合 LIBERO 的 tabletop manipulation。
- **可引用点**: DINO 为什么在 robot tasks 上是 strong baseline 的 principled 解释。

---

## 最直接相关的 3 篇（Potential Direct Competitors）

| Rank | 论文 | 威胁级别 | 原因 |
|------|------|---------|------|
| 1 | **Grant et al. 2026** (Not All Features Are Created Equal) | **高** | 同样研究 VLA representations，在 LIBERO-Goal 上做了 behavioral analysis。但他们是 intervention-based（改 prompt/注入 activation），不是 probing-based（trained vs untrained hidden states）。**我们的差异化**: layer × timestep 的 diagnostic probing + trained vs untrained 对比 |
| 2 | **LangForce 2026** (BayesianVLA) | **中** | 提出 Information Collapse 理论——我们可以提供 representation-level 证据。他们是 solution paper（提出修复方法），我们是 analysis paper（诊断问题所在）。互补 > 竞争 |
| 3 | **Häon et al. 2025** (Mechanistic Interpretability for Steering VLAs) | **中** | 也做 VLA interpretability，但方向不同——他们做 causal steering（修改 activation 改变行为），我们做 diagnostic probing（分析 hidden states 编码了什么）。且他们没有分析 instruction conditioning |

---

## Novelty 定位建议

### 我们的独特贡献（无人做过的组合）

1. **Trained vs Untrained VLA 的 representation 对比**: Grant et al. 对比不同模型，Häon et al. 做单模型 steering，但没人对比 **同一架构 trained vs untrained** 的 hidden states——这直接回答 "VLA 训练到底改变了什么？"

2. **Layer × Timestep 的细粒度 instruction probing**: Lu et al. 做了 layer-wise probing 但只看 symbolic predicates；Grant et al. 看了 prompt classification 但只报告单层结果；没人做 full layer × timestep 的 instruction classification heatmap。

3. **Vision-sufficient → Vision-ambiguous 的对比叙事**: 大家要么在 LIBERO-10/Object（vision-sufficient）上发现 language 不重要，要么在 LIBERO-Goal（vision-ambiguous）上发现 language 重要。但没人系统对比这两个 regime 下的 **representation-level** 差异。我们的三段式 story（temporal distance → action prediction → instruction probing）填补这个空白。

4. **为 "encoded but not used" paradox 提供 representation-level 解释**: Grant et al. 发现 π0.5 L17 有 99.3% prompt accuracy 但行为不变。我们的 probing 可以回答：这是因为 instruction 在所有层都被编码但 action 生成路径绕过了它？还是因为 instruction encoding 集中在特定层但 action decoding 在其他层？

### 建议的 Positioning Statement

> "While recent work has established that VLA models are dominated by visual priors in standard benchmarks (Grant et al. 2026; VLM4VLA 2026) and can be steered via internal representations (Häon et al. 2025), no study has systematically probed *how VLA training reshapes the encoding of language instructions across layers and timesteps*. We address this gap by comparing trained versus untrained OpenVLA representations on vision-sufficient (LIBERO-10) and vision-ambiguous (LIBERO-Goal) tasks, revealing when and where instruction grounding emerges in VLA hidden states."

### 与已有工作的关系图

```
                    Behavioral Analysis          Representation Analysis
                    (intervention/eval)          (probing/diagnostic)
                    
Vision-sufficient   Grant 2026 (LIBERO-Object)   [Ours: MVP-1,2] temporal/action probing
(LIBERO-10/Object)  VLM4VLA 2026                  → vision dominates
                    LangForce 2026 (theory)       
                    
Vision-ambiguous    Grant 2026 (LIBERO-Goal)      [Ours: MVP-3] instruction probing
(LIBERO-Goal)       Stable Lang 2026              → language should matter
                    
Mechanistic/Causal  Häon 2025 (steering)          Molinari 2025 (world model probing)
                                                   Lu 2025 (symbolic state probing)
                                                   [Ours: trained vs untrained]
```

**我们占据了右侧列的中间位置——representation probing × vision-ambiguous scenarios × trained vs untrained comparison。这个交叉点目前是空白。**
