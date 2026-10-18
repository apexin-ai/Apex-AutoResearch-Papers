# research smolvla libero config

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_smolvla_libero_config_20260516T233302_result.json`
- **Structured JSON:** [`416ce62720dccb1b1555.json`](../../sessions/41/416ce62720dccb1b1555.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### SmolVLA LIBERO 训练配置 (arXiv:2506.01844)

| 项目 | 值 |
|------|------|
| 总参数 | 450M (VLM) + ~100M (action expert) |
| LIBERO FT 步数 | **100K steps** |
| Batch size | 64 |
| LR | 1e-4, cosine decay → 2.5e-6 |
| Optimizer | AdamW (β1=0.9, β2=0.95) |
| 冻结部分 | **VLM backbone 全冻**，只训 action expert (~100M) |
| 精度 | bfloat16 + torch.compile |
| 评估 | 10 trials/task, 10 tasks/suite, binary success |

### 关键发现：Robotics Pretraining

SmolVLA 在 LIBERO fine-tune 之前有 **200K steps 的 robotics pretraining**（481 个社区数据集，~23K episodes，10.6M frames，batch 256）。87.3% 的结果来自 pretrained base → LIBERO FT，不是 from scratch。

### 38pp Gap 分析

| 问题 | 回答 |
|------|------|
| 步数不够？ | 步数相同（都是100K），不是主因 |
| Scope不同？ | **是主因之一**：SmolVLA 冻VLM只训expert(100M)，你做Full FT可能过拟合或优化困难 |
| 预训练差异？ | **最大主因**：SmolVLA有200K步robotics预训练，你的模型没有 |
| 数据增强？ | 论文未提特殊augmentation |
| 评估协议？ | 10 episodes/task，与你的设置需对齐确认 |

### 结论

**38pp gap 最可能原因**：SmolVLA 的 87.3% 建立在 robotics pretraining 之上（相当于额外 200K steps on diverse data）。你的 Full FT 100K 是 from VLM scratch，等价于少了整个预训练阶段。次要原因是 Full FT vs Expert-only 的优化难度差异。

**建议方向**：用 `lerobot/smolvla_base`（已含 robotics pretrain）作为起点做 LIBERO FT，或只训 action expert 而非 full model。

Sources:
- [SmolVLA Paper (HTML)](https://arxiv.org/html/2506.01844v1)
- [SmolVLA HF Docs](https://huggingface.co/docs/lerobot/en/smolvla)
- [Low SR Issue #2107](https://github.com/huggingface/lerobot/issues/2107)
- [HuggingFaceVLA/smolvla_libero](https://huggingface.co/HuggingFaceVLA/smolvla_libero)

---
