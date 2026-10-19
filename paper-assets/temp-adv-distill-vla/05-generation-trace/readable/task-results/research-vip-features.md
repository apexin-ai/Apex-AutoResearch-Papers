# research vip features

**temp adv distill vla** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_vip-features_20260515T053222_result.json`
- **Structured JSON:** [`32b38985297b31e76818.json`](../../sessions/32/32b38985297b31e76818.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。以下是报告摘要：

---

## VIP Features 调研报告

**VIP (Value-Implicit Pre-training)** — ICLR 2023, Meta/UPenn。在 Ego4D 人类视频上自监督预训练，将表征学习建模为 offline goal-conditioned RL，学到时间平滑的 embedding，使得 embedding distance 隐式等价于 value function，可直接作为任意 goal-image 任务的 dense reward。

**架构**: ResNet50, 输出 1024 维 embedding, 输入 224×224 RGB。模型约 100MB，单帧推理 <5ms (GPU)，远快于 OpenVLA。

**预训练模型获取**:
- 官方 repo: [facebookresearch/vip](https://github.com/facebookresearch/vip)
- TorchRL 内置: `from torchrl.envs.transforms import VIPTransform`
- 独立安装: `pip install vip-reward`

**核心优势 vs OpenVLA features**: VIP 的 embedding distance 设计上就是 temporally smooth + 单调的，论文验证在 sim/real robot 任务上 zero-shot 即可提供 dense reward，不需要微调。相比之下 R3M 的 embedding 平滑性较差，LIV 需要语言条件。

**集成步骤**:
1. `pip install vip-reward`
2. `load_vip()` 加载预训练模型
3. 对 LIBERO 轨迹帧提取 1024 维 embedding
4. 计算 `cos_sim(emb_t, emb_goal)` 作为 progress indicator
5. 与 OpenVLA features 在相同轨迹上对比单调性和平滑性

**预估工作量**: 2-3 小时（含环境搭建、特征提取、对比实验）。

Sources:
- [VIP Paper (arXiv)](https://arxiv.org/abs/2210.00030)
- [VIP Official Repo](https://github.com/facebookresearch/vip)
- [VIP Project Page](https://sites.google.com/view/vip-rl)
- [ICLR 2023 OpenReview](https://openreview.net/forum?id=YJ7o2wetJ2)
- [TorchRL VIPTransform Docs](https://docs.pytorch.org/rl/stable/reference/generated/torchrl.envs.transforms.VIPTransform.html)

---
