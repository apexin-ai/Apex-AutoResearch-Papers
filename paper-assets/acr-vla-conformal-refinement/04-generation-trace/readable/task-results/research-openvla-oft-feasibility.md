# research openvla oft feasibility

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_openvla-oft-feasibility_20260522T050121_result.json`
- **Structured JSON:** [`d2dd3ee76b6fb0dc062a.json`](../../sessions/d2/d2dd3ee76b6fb0dc062a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕，以下是调研报告。

---

## 1. 模型概况
- **论文**：*Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success* ([arXiv:2502.19645](https://arxiv.org/abs/2502.19645))
- **代码**：[github.com/moojink/openvla-oft](https://github.com/moojink/openvla-oft)
- **权重**：HuggingFace `moojink/openvla-7b-oft-finetuned-libero-{spatial,object,goal,10}`（每个 suite 一个 checkpoint）
- **架构**：**不是 flow matching**。基于 Llama-2 7B 骨干 + SigLIP/DinoV2 双视觉编码器，用 4 层 MLP action head 做 **L1 回归**，直接输出连续动作。核心改进是 parallel decoding + action chunking + 连续动作表示。
- **参数量**：~7B
- **显存需求**：推理 bf16 约 **15.9 GB**（单卡 A100/4090/3090 可跑）

## 2. Action Space
- **维度**：7D（3 position + 3 orientation + 1 gripper），delta end-effector pose
- **Chunk 长度**：LIBERO 实验 K=8
- **归一化**：每个维度归一化到 [-1, +1]，训练用 L1 loss（predicted vs ground-truth normalized actions，收敛到 loss < 0.01）
- **采样方式**：**完全确定性**。L1 回归直接输出均值预测，无 temperature、无随机噪声、无 flow steps。给定相同输入，输出完全相同。

## 3. LIBERO 性能
- **Fine-tuned checkpoint**：有，四个 suite 各一个
- **论文报告 SR**：
  - Spatial **97.6%**
  - Object **98.4%**
  - Goal **97.9%**
  - Long **94.5%**
  - Average **97.1%**（从原版 OpenVLA 76.5% 大幅提升）

## 4. CRM 适配评估

### Obs features 维度
- Llama-2 7B hidden dim = **4096D**（对比 SmolVLA 960D, π0.5 2048D）
- 提取位置：最后一层 Llama decoder 的 hidden states，输入 MLP action head 之前
- CRM 的 obs encoder 需新增 4096D → CRM latent 的适配层

### 核心困难：确定性模型无法采样多样 candidates

这是适配的**最大障碍**。CRM pipeline 需要 temperature > 0 采样 K 个 diverse action candidates，但 OpenVLA-OFT 是纯 L1 回归，**没有内置随机性机制**：

| VLA | 采样机制 | 多样性来源 |
|-----|----------|-----------|
| SmolVLA | autoregressive token decoding | temperature 控制 softmax |
| π0.5 | flow matching | 随机初始噪声 z₀ ~ N(0,I) |
| **OpenVLA-OFT** | L1 回归 MLP | **无** |

可能的 workaround（按可行性排序）：

1. **输入噪声注入**：在 MLP action head 的输入（4096D hidden state）上加高斯噪声 ε ~ N(0, σI)，σ 作为超参。简单但缺乏理论保障，噪声强度难调——太小无多样性，太大动作质量崩溃。
2. **MC Dropout**：推理时开启 Llama 层的 dropout，多次 forward 得到不同 hidden states。但 Llama-2 默认 dropout=0，需要 fine-tune 时加 dropout 或强行开启（效果不确定）。
3. **退回原版 OpenVLA（discrete tokens）**：原版 OpenVLA 用 256-bin 离散化 + autoregressive decoding，天然支持 temperature sampling。但性能只有 76.5% avg SR，且推理速度慢 26x。
4. **在 frozen backbone 上训练一个轻量 flow/diffusion head**：替换 MLP action head 为小型 flow matching head（类似 π0.5 的方式），既保留骨干特征又获得随机采样能力。工作量最大但最 principled。

### 其他适配工作项
- [ ] `get_vla()` / `get_action_head()` 接口适配，提取 hidden states 而非直接输出 action
- [ ] Action chunk 处理：CRM 需决定是对整个 8-step chunk 做 conformal prediction，还是只取第一步
- [ ] 归一化/反归一化对齐：确保 CRM correction delta 在 [-1,1] 归一化空间操作
- [ ] Obs feature 维度 4096D 比现有 VLA 大 2-4x，CRM 网络容量可能需调整

### 适配难度：**高**

核心原因是确定性 L1 回归与 CRM 需要的随机采样根本不兼容。SmolVLA 和 π0.5 都有天然随机性（token sampling / flow matching），适配只需调接口；OpenVLA-OFT 需要额外设计随机化方案，这本身就是一个研究问题。

### 预估工时
- 如果用 workaround 1（输入噪声注入）：**3-4 天**（接口适配 1 天 + 噪声方案调参 2-3 天）
- 如果用 workaround 4（训练 flow head）：**7-10 天**（设计+训练+调试）
- 建议：**暂缓适配**，优先完成 SmolVLA 和 π0.5 的 CRM 验证。如果确实需要第三个 VLA，噪声注入方案可作为 quick-and-dirty baseline 尝试。

---

Sources:
- [OpenVLA-OFT Paper (arXiv:2502.19645)](https://arxiv.org/abs/2502.19645)
- [OpenVLA-OFT GitHub](https://github.com/moojink/openvla-oft)
- [OpenVLA-OFT Project Page](https://openvla-oft.github.io/)
- [HuggingFace: openvla-7b-oft-finetuned-libero-spatial](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial)
- [HuggingFace: openvla-7b-oft-finetuned-libero-object](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-object)
- [HuggingFace: openvla-7b-oft-finetuned-libero-goal](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal)
- [HuggingFace: openvla-7b-oft-finetuned-libero-10](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10)

---
