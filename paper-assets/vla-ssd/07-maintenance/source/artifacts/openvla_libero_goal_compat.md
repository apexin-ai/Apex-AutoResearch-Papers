# OpenVLA Checkpoint × LIBERO-Goal 兼容性评估报告

> 日期: 2026-05-15 | 项目: vla-ssd

---

## Q1: OpenVLA-7B 的训练数据范围

### 训练混合物

`openvla/openvla-7b` 使用 `oxe_magic_soup_plus_minus` 混合物训练（Open-X Magic Soup++）。两阶段策略：前 70% 训练用 `oxe_magic_soup_plus`（含 DROID），后 30% 切换到 `oxe_magic_soup_plus_minus`（移除 DROID 和 `language_table`）。

最终混合物包含 **25 个真实世界机器人数据集**，~970K trajectories：

| 数据集 | 权重 | 数据集 | 权重 |
|--------|------|--------|------|
| fractal20220817_data (RT-1) | 1.0 | berkeley_fanuc_manipulation | 2.0 |
| kuka | 0.834 | cmu_stretch | 1.0 |
| bridge_orig (BridgeV2) | 1.0 | bc_z | 0.2 |
| taco_play | 2.0 | fmb_dataset | 1.0 |
| jaco_play | 1.0 | dobbe | 0.2 |
| berkeley_cable_routing | 1.0 | roboturk | 2.0 |
| viola | 2.0 | stanford_hydra | 2.0 |
| berkeley_autolab_ur5 | 2.0 | austin_buds | 1.0 |
| toto | 1.0 | nyu_franka_play | 3.0 |
| furniture_bench | 0.1 | ucsd_kitchen | 2.0 |
| austin_sailor | 1.0 | austin_sirius | 1.0 |
| dlr_edan_shared_control | 1.0 | iamlab_cmu_pickup_insert | 1.0 |
| utaustin_mutex | 1.0 | | |

### LIBERO 是否在训练数据中？

**否。三重确认：**

1. **代码级**：`prismatic/vla/datasets/rlds/oxe/mixtures.py` 中，LIBERO 数据集（`libero_spatial_no_noops`, `libero_object_no_noops`, `libero_goal_no_noops`, `libero_10_no_noops`）仅定义为**独立单数据集混合物**（用于 fine-tuning），不出现在任何预训练混合物中。
2. **论文级**：arXiv:2406.09246 仅在 Appendix E 讨论 LIBERO 作为评估/微调 benchmark。
3. **数据性质**：LIBERO 是仿真 benchmark（基于 Robosuite），OXE 全部是真实世界数据。

**结论：openvla-7b checkpoint 的预训练数据不包含任何 LIBERO 数据。**

来源：[mixtures.py](https://github.com/openvla/openvla/blob/main/prismatic/vla/datasets/rlds/oxe/mixtures.py), [vla.py](https://github.com/openvla/openvla/blob/main/prismatic/conf/vla.py), [HuggingFace model card](https://huggingface.co/openvla/openvla-7b)

---

## Q2: LIBERO-Goal 与 LIBERO-10 的场景重叠

### LIBERO-Goal（10 tasks，共享单一 kitchen scene）

| # | Task | Instruction |
|---|------|-------------|
| 1 | open_the_middle_drawer_of_the_cabinet | Open the middle drawer of the cabinet |
| 2 | open_the_top_drawer_and_put_the_bowl_inside | Open the top drawer and put the bowl inside |
| 3 | push_the_plate_to_the_front_of_the_stove | Push the plate to the front of the stove |
| 4 | put_the_bowl_on_the_plate | Put the bowl on the plate |
| 5 | put_the_bowl_on_the_stove | Put the bowl on the stove |
| 6 | put_the_bowl_on_top_of_the_cabinet | Put the bowl on top of the cabinet |
| 7 | put_the_cream_cheese_in_the_bowl | Put the cream cheese in the bowl |
| 8 | put_the_wine_bottle_on_the_rack | Put the wine bottle on the rack |
| 9 | put_the_wine_bottle_on_top_of_the_cabinet | Put the wine bottle on top of the cabinet |
| 10 | turn_on_the_stove | Turn on the stove |

**核心特征：所有 10 个 task 共享同一 kitchen scene layout（相同物体、相同空间布局），仅 goal 不同。**

### LIBERO-10（10 tasks，跨不同场景）

LIBERO-10 是 10 个 long-horizon multi-step tasks，分布在 **7 个不同场景**：

| # | Scene | Instruction |
|---|-------|-------------|
| 1 | KITCHEN_SCENE3 | Turn on the stove and put the moka pot on it |
| 2 | KITCHEN_SCENE4 | Put the black bowl in the bottom drawer of the cabinet and close it |
| 3 | KITCHEN_SCENE6 | Put the yellow and white mug in the microwave and close it |
| 4 | KITCHEN_SCENE8 | Put both moka pots on the stove |
| 5 | LIVING_ROOM_SCENE1 | Put both the alphabet soup and the cream cheese box in the basket |
| 6 | LIVING_ROOM_SCENE2 | Put both the alphabet soup and the tomato sauce in the basket |
| 7 | LIVING_ROOM_SCENE2 | Put both the cream cheese box and the butter in the basket |
| 8 | LIVING_ROOM_SCENE5 | Put the white mug on the left plate and put the yellow and white mug on the right plate |
| 9 | LIVING_ROOM_SCENE6 | Put the white mug on the plate and put the chocolate pudding to the right of the plate |
| 10 | STUDY_SCENE1 | Pick up the book and place it in the back compartment of the caddy |

### 场景重叠

**无重叠。** LIBERO-Goal 使用专属 scene（`LIBERO_Tabletop_Manipulation`：kitchen tabletop with cabinet, stove, wine rack, bowl, plate, cream cheese, wine bottle），LIBERO-10 使用 7 个完全不同的 scene layout（KITCHEN_SCENE3/4/6/8, LIVING_ROOM_SCENE1/2/5/6, STUDY_SCENE1），物体集也完全不同（moka pots, microwave, baskets, mugs, book, caddy 等）。两者的 scene 设计理念完全不同：
- LIBERO-10：测试跨场景泛化（不同场景 → 不同视觉输入）
- LIBERO-Goal：测试同场景下的 goal discrimination（相同视觉输入 → 不同 instruction）

### Action Space & Image Resolution

| 属性 | LIBERO-Goal | LIBERO-10 | 兼容性 |
|------|-------------|-----------|--------|
| Action space | 7-DoF (3 pos + 3 rot + 1 gripper) | 7-DoF (同) | ✅ 完全一致 |
| Image resolution | 128×128×3 (agentview + eye_in_hand) | 128×128×3 (同) | ✅ 完全一致 |
| Control freq | 20 Hz | 20 Hz | ✅ |
| Robot | Franka Panda | Franka Panda | ✅ |
| HDF5 结构 | `data/demo_{i}/obs/agentview_rgb` | 同 | ✅ |
| Demos/task | 50 | 50 | ✅ |

**结论：`extract_features.py` 可直接复用，无需修改数据加载代码。**

---

## Q3: Zero-shot 特征提取可行性

### 关键区分：我们做的是特征提取（probing），不是 action 评估

OpenVLA-7B 未在 LIBERO-Goal 上 fine-tune → **action 输出无意义**（zero-shot action prediction 会很差）。

但这**不影响我们的实验**：我们提取 hidden states 做 probing，不需要模型输出正确 action。只要：
1. 输入格式兼容（image + language instruction）→ ✅ 都是 128×128 RGB + 自然语言
2. Forward pass 可以正常运行 → ✅ OpenVLA 接受任意 image + text 输入
3. Hidden states 对 instruction 有响应 → ✅ LLM backbone 处理 instruction tokens，即使未 fine-tune 也会产生 instruction-dependent activations

### 为什么 zero-shot features 仍有意义

- OpenVLA-7B 在 970K trajectories 上训练了 action prediction → LLM 已学会将 visual + language token 整合为 action-relevant representation
- 即使没见过 LIBERO-Goal 的具体 scene，通用的 instruction processing 能力仍然存在
- 训练数据包含多种 "pick up X" / "put X on Y" 风格的 instruction → 语义泛化有基础
- **Untrained VLA 对比**：random LLM 也有 token embeddings 提供 partial instruction signal，但缺乏 grounded encoding

### 是否需要 fine-tune？

**不需要。** 理由：
1. Probing 目标是 instruction identity（10-way classification），不是 action quality
2. Fine-tune 反而引入 confound：fine-tuned features 包含 LIBERO-Goal task-specific knowledge，无法区分 "通用 instruction encoding" vs "task-specific memorization"
3. 与 Grant et al. 的关键差异正在于此：他们用 fine-tuned models 做 behavioral evaluation，我们用 pretrained model 做 representational probing

---

## Q4: Grant et al. 2026 (arXiv:2603.19233) 精读

### 基本信息

**"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models"**
ICLR 2026 Workshop (Multimodal Intelligence) | Case Western Reserve

### 实验规模

- 6 个 VLA 模型：π0.5 (3B), OpenVLA-OFT (7B), X-VLA (~1B), SmolVLA (450M), GR00T N1.5 (3B), ACT (80M, vision-only control)
- **394K+ rollout episodes**，跨 4 个 LIBERO suites + SimplerEnv
- 统计方法：95% Wilson score intervals, ANOVA

### 使用的 LIBERO-Goal Tasks

论文将 suites 作为整体处理，**未逐一列出** LIBERO-Goal 的具体 task names。使用了全部 4 个标准 LIBERO suites (Goal, Object, Spatial, 10) + Long (仅 GR00T)。

### Evaluation Protocol

- **Rollout-based**：在仿真环境中执行完整 trajectory，用环境内置 success criteria 判定
- **Counterfactual prompting**：6 种条件——correct prompt, null (空字符串), negation, motor command, object swap, temporal switch
- **Activation injection**：替换模型内部 activation 为另一 task 的 activation → 测因果贡献

### Fine-tuning vs Zero-shot

**Fine-tuned。** 所有模型均已在 LIBERO 数据上 fine-tune。论文分析 fine-tuned models 的机制，不涉及训练方法。

### "Language Matters" 效应量（核心数据）

**LIBERO-Goal（language-critical，shared scene）：**

| Model | Correct | Null | Wrong Object | **Δ (Correct→Wrong)** |
|-------|---------|------|-------------|----------------------|
| π0.5 | 83.3% | 80.0% | 76.7% | **-6.6 pp** (不显著, ANOVA p=0.247) |
| OpenVLA-OFT | 100% | 10% | 10% | **-90 pp** |
| X-VLA | 94% | 10% | 4-10% | **-84 to -90 pp** |
| GR00T | 97% | 0% | 0% | **-97 pp** |

**LIBERO-Object（language-immune，distinct scenes）：**

| Model | Correct | Null | Wrong Object | **Δ** |
|-------|---------|------|-------------|-------|
| π0.5 | 77.4% | 77.0% | 74.2% | **-3.2 pp** |
| OpenVLA-OFT | 100% | 100% | 100% | **0 pp** |
| X-VLA | 100% | 60% | 60-90% | **-10 to -40 pp** |

**核心结论**：语言敏感性取决于 **task structure**（scene 是否 visually ambiguous），不取决于模型架构。当场景唯一确定 task 时，language 被忽略；当多个 goal 共享同一 scene 时，language 变得关键。

### π0.5 的例外

π0.5 在 LIBERO-Goal 上也相对 language-immune (83.3%→76.7%)。可能原因：dual-pathway 架构保留了更多 visual prior，或其 flow-matching policy 对 prompt perturbation 更鲁棒。

### Linear Probe Paradox

- **π0.5 Layer 17**: 99.3% prompt classification accuracy，但行为几乎不受 prompt 影响
- **GR00T**: 100% task ID + 96.4% success prediction（32 层均一致）
- **含义**：模型在中间层密集编码了语言信息，但没有将其路由到 motor pathway。"Encoded but not used."

### 我们与 Grant 的关键差异

| 维度 | Grant et al. | 我们 |
|------|-------------|------|
| 模型状态 | Fine-tuned on LIBERO | Pretrained (未 fine-tune) |
| 分析方法 | Behavioral (rollout success) | Representational (probing hidden states) |
| 对比条件 | 6 种 prompt perturbation | Trained vs untrained VLA |
| Granularity | Per-suite aggregate | Layer × timestep × task subgroup |
| 数据需求 | 394K rollout episodes | 500 offline demos (no rollout) |
| 核心问题 | "Language 在行为上有用吗？" | "VLA 训练是否 encode instruction identity？在哪些层？" |

---

## Q5: Reviewer 风险点——数据污染分析

### 结论：**无数据污染，zero-shot 特征提取 clean**

| 检查项 | 结果 |
|--------|------|
| OpenVLA-7B 预训练数据含 LIBERO-Goal？ | ❌ 不含 |
| OpenVLA-7B 预训练数据含任何 LIBERO？ | ❌ 不含 |
| LIBERO 在 Open X-Embodiment 中？ | ❌ 不在（LIBERO 是仿真，OXE 是真实世界） |
| 代码中 LIBERO 出现在预训练 mixture？ | ❌ 仅作为 fine-tuning target |

**意义**：
- ✅ Probe 结果反映 **true representational structure**，而非 memorized LIBERO-Goal action knowledge
- ✅ Trained vs untrained 对比更 clean：trained model 的 instruction encoding 来自 970K 真实世界 trajectory 的泛化，不是 LIBERO-specific 记忆
- ✅ 如果 trained VLA 在 LIBERO-Goal 上的 instruction identity probe accuracy 显著高于 untrained → 强证据表明 VLA 训练引入了可泛化的 instruction grounding

### Reviewer 可能的 Challenge 及回应

**Q**: "OpenVLA 没在 LIBERO-Goal 上训练，features 可能完全无用？"
**A**: 我们做的是 probing（线性分类），不是 action evaluation。只要 hidden states 对 instruction tokens 有差异化响应就行。即使模型没见过 LIBERO-Goal，(1) LLM backbone 天然编码不同 instruction 的 token-level 差异，(2) VLA 训练在 970K trajectories 上学到了 instruction→action grounding，可能泛化到未见过的 instruction。Negative result 也 informative（说明 OOD instruction grounding 失效）。

**Q**: "为什么不 fine-tune 后再 probe？"
**A**: Fine-tune 引入 confound——无法区分 "通用 instruction encoding" vs "LIBERO-Goal task-specific memorization"。用 pretrained checkpoint 可以测试 VLA 训练的 **泛化** instruction encoding，这是 Grant et al.（fine-tuned）没有做的。

---

## 总结

| 问题 | 结论 |
|------|------|
| (a) Zero-shot 特征提取是否可行？ | **可行。** 输入格式完全兼容，hidden states 对 instruction 有响应，无需 action 输出正确。 |
| (b) 是否需要 fine-tune？ | **不需要，且不应该。** Fine-tune 引入 memorization confound，削弱 story。 |
| (c) 与 Grant et al. 的关键差异 | **Pretrained vs fine-tuned; representational vs behavioral; layer×timestep granularity; trained vs untrained comparison。** 我们填补的空白：VLA 训练是否引入可泛化的 instruction encoding，以及这个信号在网络的哪里。 |
| (d) 数据污染风险 | **无。** OpenVLA-7B 预训练不含任何 LIBERO 数据。 |
| (e) LIBERO-Goal vs LIBERO-10 场景重叠 | **无重叠。** 完全不同的 scene layouts。 |
| (f) Pipeline 兼容性 | **完全兼容。** 同一 HDF5 格式、action space、image resolution。extract_features.py 无需修改。 |
