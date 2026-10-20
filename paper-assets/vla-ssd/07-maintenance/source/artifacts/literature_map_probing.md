# VLA Probing Beyond Vision — Literature Survey

> 调研日期：2026-05-15
> 目标：寻找视觉不可达（vision-inaccessible）的 probing task，证明 VLA LLM 训练对表征的独特贡献

---

## 1. Action/Policy Probing

### Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models (Grant, Zhao & Wang, 2026)
- **核心方法**: 跨 6 个 VLA 模型（80M–7B）使用 activation injection、sparse autoencoders (SAEs)、linear probes 进行机制分析，394K+ rollout episodes
- **关键发现**:
  - **Visual pathway dominance**: 将 baseline activations 注入 null-prompt episodes 可恢复几乎相同的行为，说明视觉通路主导动作生成
  - **Language sensitivity is suite-dependent**: 当视觉 context 唯一确定 task 时，language 被忽略（libero_object: 60-100% 不受 prompt 影响）；当多个 goal 共享同一 scene 时，language 变得关键（libero_goal: 94%→10%）
  - **Spatially bound motor programs**: 跨 task injection 使机器人移向 source-task 位置（99.8% alignment），说明动作编码的是工作空间坐标而非抽象 task representation
  - **Expert pathway vs VLM pathway**: 多路径模型中，expert pathway injection 导致 2× 更大的行为位移
  - 识别出 82+ manipulation concepts，但 28-92% zero-effect rate
- **与我们的关联**: **极度相关**。该论文的 libero_goal 实验直接证明：当 scene 中有多个可能 goal 时，language 编码是关键的。这为我们设计 probing task 提供了直接方向——需要用 multi-goal ambiguous 场景
- **arXiv**: 2603.19233

### Mechanistic Interpretability for Steering Vision-Language-Action Models (Häon et al., 2025)
- **核心方法**: 将 transformer FFN layer 的 feedforward activations 投影到 token embedding basis，找到与动作选择因果相关的稀疏语义方向（speed、direction、height）
- **关键发现**:
  - 在 OpenVLA 和 π0 上验证，可在推理时实时调控行为（无需微调）
  - Action tokens 分布在所有层中，但在最后一层的 value vectors 中占比最大
  - Fine-tuning 主要影响 action tokens 而非 semantic tokens
  - 跨多层的 neuron clusters 产生更强的运动效果
  - 在 LIBERO-Long 和 UR5 物理平台上验证
- **与我们的关联**: 方法论直接适用于 OpenVLA。可以用他们的 activation projection 方法寻找 LLM 训练引入的非视觉语义方向（如 task phase、goal semantics）
- **arXiv**: 2509.00328

### Observing and Controlling Features in Vision-Language-Action Models (Buurmeijer, Amo Alonso, Swann & Pavone, 2026)
- **核心方法**: 在每个 transformer layer 训练 linear probe（feature observer），提出 feature-observability 和 feature-controllability 概念，通过最小干预实现行为控制
- **关键发现**:
  - Robot states 和 actions 在 VLA transformer 表征中是**线性可解码**的
  - Observations 对线性扰动具有鲁棒性，尤其早期层更稳健
  - Gripper state 控制成功率 >90%，也可控制 end-effector height 和 speed
  - 在 OpenVLA 和 π0.5 上测试，覆盖 LIBERO 和 BridgeData V2
- **与我们的关联**: 直接适用。他们的 linear probe 方法可以用来检测 LLM 训练是否引入了超越 vision encoder 的可解码信息。但需注意：如果 robot state 和 action 已经线性可解码，需要找更高层次的 probing target
- **arXiv**: 2603.05487

### VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models (Zhang et al., 2025)
- **核心方法**: 用统一的 minimal adaptation pipeline（MLP policy head, <1% 参数）将 24 个 VLM 转为 VLA，在 Calvin/SimplerEnv/LIBERO 上测试
- **关键发现**:
  - **Vision encoder 是主要性能瓶颈**: 冻结 vision encoder 导致剧烈性能下降（Qwen2.5VL-7B on Calvin: -1.23）
  - **Word embedding 冻结对 VLA 性能无显著影响**
  - **VLM 通用能力与 VLA 性能无相关性**: SimplerEnv 和 LIBERO 上线性回归分析无显著相关
  - 视觉特征优化用于多模态理解/推理的表征与低层操控需要的精细表征存在本质 domain gap
  - Embodied auxiliary task fine-tuning（VQA、pointing、depth prediction）反而损害性能
- **与我们的关联**: **直接支持我们的发现**——vision encoder dominates，language 贡献微弱。但也暗示：需要找到 language model 确实有独特贡献的维度

---

## 2. Language Grounding Probing

### LLMs Can Compensate for Deficiencies in Visual Representations (Takishita et al., 2025)
- **核心方法**: 设计 Object Part Identification (OPI) task（用 Pascal Panoptic Parts 数据集识别局部 object parts），通过 Attention Knockout (AK) ablation 和 Logit Lens 分析 VLM 各组件贡献
- **关键发现**:
  - **Decoder self-attention 影响微弱**: 阻断 decoder self-attention 仅导致轻微性能下降
  - **关键补偿能力**: 单独阻断 encoder self-attention 后，language decoder 能**大幅恢复**性能
  - **选择性恢复**: 13B 模型能完全恢复高层语义特征，但浅层视觉特征部分不可恢复
  - CLIP 文本编码器单独的 part identifiability 远低于 VLM
- **与我们的关联**: **方法论启发极大**。可以在 OpenVLA 上做类似的 attention knockout 实验：阻断 vision encoder 的 self-attention，看 LLM decoder 能否从退化的视觉输入中恢复 task-relevant 信息。这直接测试 LLM 的补偿能力
- **arXiv**: 2506.05439

### Do LLMs "know" internally when they follow instructions? (Heo et al., 2024)
- **核心方法**: 在 LLM embedding space 中用 linear probes 寻找 instruction-following dimension，在 first/middle/last token 位置、early/middle/final 层分析
- **关键发现**:
  - 模型从第一个 token 就展现可分离的 success/failure 表征（AUROC 0.74-0.88）
  - Linear probes 对 unseen tasks 泛化良好（0.7-0.8 AUROC），但对不同 instruction types 失败（~0.5 AUROC）
  - 该维度主要与 prompt phrasing 相关，而非 task familiarity 或 instruction difficulty
  - Representation engineering 沿此维度的调整可提升 instruction-following 成功率
- **与我们的关联**: 可以在 OpenVLA hidden states 中寻找类似的 "instruction-following dimension"——trained model 应比 untrained model 更清晰地编码 instruction compliance。这是一个明确的 vision-inaccessible signal
- **arXiv**: 2410.14516

### Probing Visual Language Priors in VLMs (Luo et al., 2025)
- **核心方法**: 构建 ViLP benchmark——合成 OOD 图像 + QIA triplets，测试 VLM 是否真正进行视觉推理而非依赖语言先验
- **关键发现**:
  - 人类 98%+ 准确率，GPT-4o 仅 66.17%，Claude-3.5-Sonnet 70%
  - 图像退化后 performance 急剧下降，但 "prior" accuracy 保持 ~50%——VLM 严重依赖文本推理
  - Image-DPO（对比 clean vs degraded images）可提升视觉推理
- **与我们的关联**: 提供了一种设计 probing task 的思路：构造需要超越视觉先验的 task，让 language model 的贡献可见。例如在 LIBERO 中，同一视觉 scene 对应不同 instruction 时的行为差异
- **arXiv**: 2501.00569

### LIBERO-Plus: In-depth Robustness Analysis of VLA Models (Fei et al., 2025)
- **核心方法**: 在 7 个维度（object layout、camera、robot state、language、lighting、textures、noise）对 10 个 VLA 模型进行系统扰动测试，10,030 evaluation tasks
- **关键发现**:
  - **Language signals 基本被忽略**: OpenVLA-OFT 在 blank language input 下 object suite 性能基本不变
  - **Positional memorization**: 模型对 confounding objects 有弹性，但 target objects 位移时失败——依赖记忆位置而非 object semantics
  - **Compositional gap**: 联合扰动导致比预期更差的失败，存在 representation entanglement
  - 从 95% 到 <30% 的性能骤降说明 benchmark 成绩掩盖了根本脆弱性
- **与我们的关联**: **直接确认我们的困境**——LIBERO 中 language 被忽略，models 是 visual pattern matchers。关键启示：需要设计扰动实验或 multi-goal 场景来逼出 language 的作用
- **arXiv**: 2510.13626

---

## 3. Causal/Planning Probing

### Causal Tracing of Object Representations in Large Vision Language Models (Li et al., 2025)
- **核心方法**: 提出 Fine-grained Cross-modal Causal Tracing (FCCT)——引入 Gaussian noise 扰动图像，对比 clean/corrupted/patched 三种推理，测量 Recovery Rate
- **关键发现**:
  - **Cross-modal aggregation**: 中间层 final token 的 MHSA 在聚合 visual/textual 信息中起关键作用，attention 在 Layer 15 左右达峰
  - **Hierarchical MLP progression**: 早期层编码局部嵌入 → 中间层实现跨模态交互 → 深层积累 task-relevant 表征
  - **语义迁移**: hidden states 从浅层的 vision-centric 过渡到深层的 cross-modal + task-specific
  - 提出 Intermediate Representation Injection (IRI) 作为训练无关的幻觉缓解方法
- **与我们的关联**: FCCT 方法可以直接应用于 OpenVLA——通过因果追踪确定哪些层/位置编码了超越视觉的 task structure 信息。特别是中间层的跨模态交互可能是 LLM 训练的独特贡献
- **arXiv**: 2511.05923

### CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models (Zhao et al., CVPR 2025)
- **核心方法**: 在 VLA 训练中引入 visual chain-of-thought，让模型在生成动作前先生成推理步骤（文本或视觉形式）
- **关键发现**:
  - CoT 训练显著提升 VLA 性能，尤其在需要多步推理的 long-horizon task 上
  - Textual CoT 和 visual CoT 各有优势
  - 推理过程的表征可以被 probe 解码
- **与我们的关联**: 如果 VLA 编码了 CoT-like 的推理过程（subtask ordering、goal decomposition），这些是纯视觉无法获得的。可以设计 probing task 测试模型是否隐式编码了 task decomposition

### Latent Reasoning VLA (LaRA-VLA, 2026)
- **核心方法**: 在 latent space 中执行推理和预测，不需要显式文本 CoT
- **关键发现**:
  - Latent space reasoning 可以编码 planning 信息
  - 比 explicit CoT 更高效
- **与我们的关联**: 如果 OpenVLA 的 LLM 在 hidden states 中进行了 latent reasoning，这些信息应该可以通过 probing 检测到。可以设计 subtask prediction probe 测试是否 LLM 层编码了超越当前视觉观测的 planning 信息
- **arXiv**: 2602.01166

---

## 4. Mechanistic Interpretability of VLA/VLM

### Mechanistic Interpretability Meets Vision Language Models (ICLR Blogposts 2025)
- **核心方法**: 系统综述 5 种机制可解释性方法在 VLM 上的应用：probing、activation patching、logit lens、sparse autoencoders、automated explanation
- **关键发现**:
  - Layers 1-10 处理广泛 contextual 信息，layers 15-24 聚焦提取特定 object 细节
  - **预训练模型优先 language 而非 vision**
  - Cross-modal integration 主要发生在 late layers
  - LLaVA 缺少 "text-only" attention heads，BLIP 没有 "vision-only" heads——不同架构的 modality 处理模式差异显著
- **与我们的关联**: 提供了完整的方法论工具包。特别是 activation patching 可以因果性地确定哪些层对 instruction understanding 贡献最大

### Hidden in Plain Sight: VLMs Overlook Their Visual Representations (Fu et al., 2025)
- **核心方法**: 比较 VLM 与其底层 vision encoder 在 vision-centric tasks（depth estimation、correspondence、3D awareness）的性能
- **关键发现**:
  - **巨大性能差距**: Vision encoder 在 depth estimation 上 88.7%，VLM 降至 65.3%（-21.7%）
  - Vision features 在 VLM 各层中保持完整性——信息损失发生在 linguistic processing 阶段
  - **LLM 是瓶颈**: fine-tuning LLM 组件带来最大性能提升
  - VLM 在有无图像时产生几乎相同的答案分布——继承了 language model 的 blind biases
  - DINOv2 在 5/6 视觉任务上最强，但不产生最强 VLM——说明是 misuse 而非 encoder weakness
- **与我们的关联**: 反向启示——如果 VLM/VLA 的 LLM 是瓶颈，那 probing 应该测试 LLM 是否成功利用了视觉信息（而不是仅测试视觉信息是否存在）。需要设计测试 cross-modal integration 质量的 probing task
- **arXiv**: 2506.08008

### Seeing but Not Believing: Probing the Disconnect Between Visual Attention and Answer Correctness in VLMs (Liu et al., 2025)
- **核心方法**: Layer-wise attention 分析，追踪 text tokens（浅层）到 visual tokens（深层）的注意力转移
- **关键发现**:
  - 浅层主要关注 text，深层稀疏但可靠地关注 localized evidence regions
  - **"Seeing but Not Believing"**: 深层正确关注了相关视觉证据，但最终答案仍然错误——推理瓶颈而非感知瓶颈
  - Visual Evidence Augmentation (Vea) 可在推理时提升准确率（最高 +11.1 exact match）
- **与我们的关联**: 说明 VLM/VLA 的问题不在于看不到，而在于 reasoning 阶段没有正确利用视觉信息。Probing 应聚焦于 LLM 层中 cross-modal reasoning 的质量
- **arXiv**: 2510.17771

---

## 5. Negative Results / Failure Modes in VLA Probing

### "Vision Encoder Dominates" 现象汇总

| 论文 | 发现 | 环境 |
|------|------|------|
| VLM4VLA (Zhang et al., 2025) | Word embedding 冻结无影响；vision encoder 冻结致命 | Calvin, SimplerEnv, LIBERO |
| Not All Features (Grant et al., 2026) | Null-prompt 注入 baseline activations 可恢复行为 | LIBERO, 6 models |
| LIBERO-Plus (Fei et al., 2025) | Blank language input 下性能不变；positional memorization | LIBERO, 10 models |
| Hidden in Plain Sight (Fu et al., 2025) | VLM 有无图像答案分布几乎相同 | Depth, correspondence, 3D |
| Seeing but Not Believing (Liu et al., 2025) | 正确感知但错误推理 | VQA benchmarks |

### 共性模式
1. **LIBERO 场景过于视觉可辨**: object positions、gripper state、task progress 全部可从像素直接判断
2. **Language 在 single-goal 场景中冗余**: 当视觉 context 唯一确定 task 时，language signal 被完全忽略
3. **Models 学到的是 positional shortcuts**: 位置记忆而非语义理解
4. **LLM 层存在但未被充分利用**: vision features 在 LLM 层中保持完整，但 LLM 未成功 enrich 它们

### 破局方向（来自文献的启示）
- **Multi-goal ambiguous scenes** (Grant et al.): libero_goal suite 中 language 贡献显著
- **Attention Knockout** (Takishita et al.): 阻断 vision encoder 看 LLM 能否补偿
- **Cross-modal causal tracing** (Li et al.): 追踪 LLM 层中的跨模态信息聚合
- **Instruction-following dimension** (Heo et al.): 寻找 hidden state 中的 instruction compliance 方向

---

## 综合建议

### Top-3 最值得尝试的 Probing Tasks

#### 1. Instruction-Conditioned Action Prediction（可行性 ★★★★★，预期效果 ★★★★☆）
- **原理**: 从 Grant et al. 2026 的发现出发——当多个 goal 共享同一 visual scene 时，language 编码变得关键。设计 probing task：给定相同视觉观测 + 不同 instruction，从 hidden states 预测 instruction identity 或 target action。
- **具体设计**:
  - 用 LIBERO-Goal suite（同一 scene 多个 goal）
  - 在每个 timestep 从 hidden states 训练 linear probe 预测：(a) 当前 instruction 是哪一个，(b) target object 是什么
  - 对比 vision encoder only vs. full VLA 的 probe accuracy
- **需要的数据**: LIBERO-Goal 的多 goal 轨迹数据（已有）
- **代码改动**: 在现有 probing pipeline 基础上增加 instruction identity classification head，使用 LIBERO-Goal 而非 LIBERO-Spatial/Object
- **预估工时**: 2-3 天

#### 2. Counterfactual Activation Injection + Probing（可行性 ★★★★☆，预期效果 ★★★★★）
- **原理**: 结合 Grant et al. 的 activation injection 和 Häon et al. 的 semantic direction 方法。注入 null-prompt 或 wrong-prompt 的 activations，看 probing accuracy 如何变化。如果 LLM 训练有独特贡献，wrong-prompt injection 应显著降低 task-relevant probing accuracy。
- **具体设计**:
  - 记录 correct-prompt 和 wrong-prompt 下的 layer-wise activations
  - 用 linear probe 从 correct/wrong/null activations 预测 task identity、next subtask、goal object
  - 计算 Δ accuracy 作为 language contribution 的度量
- **需要的数据**: 同一 scene 下不同 instruction 的 rollout（可从 LIBERO-Goal 收集）
- **代码改动**: activation recording + injection pipeline，需修改 forward pass
- **预估工时**: 3-5 天

#### 3. Cross-modal Causal Tracing for Task Structure（可行性 ★★★☆☆，预期效果 ★★★★★）
- **原理**: 用 Li et al. 2025 的 FCCT 方法，但应用于 OpenVLA + LIBERO。扰动 visual input，追踪哪些 LLM 层恢复了 task-relevant 信息——这些恢复的信息必然来自 language/LLM 的先验知识而非 vision。
- **具体设计**:
  - 对 visual tokens 注入 Gaussian noise
  - 在每一层逐步恢复 clean activations（patching）
  - 测量 Recovery Rate：哪些层恢复了 (a) action accuracy，(b) subtask prediction，(c) goal identification
  - 对比 trained vs untrained LLM 的恢复模式
- **需要的数据**: 标准 LIBERO 轨迹 + noise-augmented 版本
- **代码改动**: 需实现 causal tracing pipeline（noise injection + activation patching + 逐层恢复）
- **预估工时**: 5-7 天

### 额外建议

- **快速验证**: 先做 Task 1（instruction-conditioned probing on LIBERO-Goal），2-3 天可出结果。如果 LLM-trained model 在 instruction identity probing 上显著优于 vision-only，就找到了 vision-inaccessible 的贡献维度
- **关键 insight**: 不要在 LIBERO-Spatial/Object 上做（那些 single-goal 场景中 vision 足够），必须用 multi-goal ambiguous 场景
- **方法论参考**: Buurmeijer et al. 2026 的 linear probe 框架可直接复用，他们已经在 OpenVLA + LIBERO 上验证过

---

## 参考文献

1. Grant, B., Zhao, X., & Wang, P. (2026). Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models. arXiv:2603.19233.
2. Häon, B., Stocking, K., Chuang, I., & Tomlin, C. (2025). Mechanistic Interpretability for Steering Vision-Language-Action Models. arXiv:2509.00328.
3. Buurmeijer, H., Amo Alonso, C., Swann, A., & Pavone, M. (2026). Observing and Controlling Features in Vision-Language-Action Models. arXiv:2603.05487.
4. Zhang, J. et al. (2025). VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models. arXiv:2601.03309.
5. Takishita, S. et al. (2025). LLMs Can Compensate for Deficiencies in Visual Representations. arXiv:2506.05439.
6. Heo, J. et al. (2024). Do LLMs "know" internally when they follow instructions? arXiv:2410.14516.
7. Luo, T. et al. (2025). Probing Visual Language Priors in VLMs. arXiv:2501.00569.
8. Fei, S. et al. (2025). LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models. arXiv:2510.13626.
9. Li, Q. et al. (2025). Causal Tracing of Object Representations in Large Vision Language Models. arXiv:2511.05923.
10. Zhao et al. (2025). CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models. CVPR 2025.
11. LaRA-VLA (2026). Latent Reasoning VLA. arXiv:2602.01166.
12. ICLR Blogposts (2025). Mechanistic Interpretability Meets Vision Language Models.
13. Fu, S. et al. (2025). Hidden in Plain Sight: VLMs Overlook Their Visual Representations. arXiv:2506.08008.
14. Liu, Z. et al. (2025). Seeing but Not Believing: Probing the Disconnect Between Visual Attention and Answer Correctness in VLMs. arXiv:2510.17771.
