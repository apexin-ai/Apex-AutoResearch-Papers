# research tracvla libero coverage

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_tracvla_libero_coverage_20260521T003607_result.json`
- **Structured JSON:** [`3797d6306a673726d66e.json`](../../sessions/37/3797d6306a673726d66e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。以下是完整结果。

---

## 1. TraceVLA 训练配置

| 属性 | 详情 |
|------|------|
| 预训练数据 | Open X-Embodiment (OXE), 970K trajectories + 150K visual trace trajectories |
| 模型变体 | TraceVLA-7B (Llama2-based), TraceVLA-Phi3V (Phi-3-Vision 4B) |
| LIBERO 评估 | 论文在**全部 4 个 suite** 上做了 fine-tune + eval（遵循 OpenVLA 协议：LoRA r=32, 每 suite 10 tasks × 50 demos） |

## 2. 公开 Checkpoint 可用性

| Checkpoint | 来源 | Suite | 类型 |
|-----------|------|-------|------|
| `furonghuang-lab/tracevla_phi3v` | HuggingFace | N/A (OXE pretrained) | Phi3V backbone |
| `furonghuang-lab/tracevla_7b` | HuggingFace | N/A (OXE pretrained) | 7B Llama2 backbone |
| `furonghuang-lab/openvla_phi3v` | HuggingFace | N/A (OXE pretrained) | Phi3V base (no trace) |
| `openvla/openvla-7b-finetuned-libero-spatial` | HuggingFace | Spatial | **7B Llama2 only** |
| `openvla/openvla-7b-finetuned-libero-object` | HuggingFace | Object | **7B Llama2 only** |
| `openvla/openvla-7b-finetuned-libero-10` | HuggingFace | Long | **7B Llama2 only** |

**关键发现：没有任何 TraceVLA-Phi3V 的 LIBERO suite-specific fine-tuned checkpoint 发布。** 论文做了实验但未开源这些 checkpoint。LIBERO-specific checkpoints 只有 OpenVLA-7B (Llama2) 版本。

## 3. 服务器已有资源

```
/root/autodl-tmp/vla-ssd/checkpoints/
├── tracevla-phi3v/                      ← OXE-pretrained (= furonghuang-lab/tracevla_phi3v)
├── openvla-phi3v/                       ← OXE-pretrained base
├── openvla-7b/                          ← 7B base
├── openvla-7b-finetuned-libero-goal/    ← 7B LIBERO-Goal (Llama2)
├── openvla-7b-finetuned-libero-object/  ← 7B LIBERO-Object (Llama2)
├── nora-libero-goal/                    ← Qwen2.5-VL (无关模型)
└── dinov2-large/
```

已提取的特征：`phi3v_trained_libero_goal`, `phi3v_untrained_libero_goal` — 仅 Goal suite。

## 4. 对我们项目的影响分析

我们之前的 "trained vs untrained" 对比是：
- **trained** = `tracevla-phi3v`（OXE 预训练后的 VLA）
- **untrained** = 未经 VLA 训练的 base Phi-3-Vision

这个对比的核心不是"在某个 LIBERO suite 上 fine-tune 前后"，而是"VLA 训练是否改变了 LLM 表征"。

**好消息：如果沿用这个定义，扩展到其他 suite 不需要新 checkpoint。** 同样的两个模型（tracevla-phi3v + untrained phi3v）跑在不同 LIBERO suite 的 demo 数据上即可。模型不变，只是输入数据（环境布局/物体/任务）变了。

## 5. 自行训练的成本估算（如果需要 suite-specific fine-tuned checkpoint）

| 项目 | 估计 |
|------|------|
| 训练代码 | TraceVLA repo `phi3` branch 有训练脚本，LIBERO fine-tuning 需适配 |
| 每 suite 数据量 | 500 demos (10 tasks × 50) |
| Phi3V (4B) LoRA fine-tune | ~0.5–1 GPU-hour per suite (单卡 A100/A6000) |
| 3 个新 suite 总计 | ~1.5–3 GPU-hours |

## 6. 建议方案

**推荐方案：直接用现有 checkpoint 扩展到其他 suite。**

理由：
- 我们的研究问题是"VLA training 如何改变 LLM representations"，不是"per-suite fine-tuning 的影响"
- 同一对 checkpoint（trained/untrained）在不同 suite 上的表征差异，可以揭示 VLA 训练获得的通用能力在不同任务类型（spatial reasoning / object recognition / goal understanding / long-horizon planning）上的表现
- 科学价值：跨 suite 的一致性模式（如所有 suite 都在中间层出现 R² 峰值）说明 VLA 训练带来的表征变化是通用的而非 task-specific 的；不一致的模式则暴露 VLA 训练的局限性

**如果 reviewer 要求 suite-specific fine-tuning 对照**，再训练也只需 ~3 GPU-hours，成本很低。

Sources:
- [TraceVLA Paper (arXiv:2412.10345)](https://arxiv.org/abs/2412.10345)
- [TraceVLA GitHub](https://github.com/umd-huang-lab/tracevla)
- [TraceVLA HuggingFace Collection](https://huggingface.co/collections/furonghuang-lab/tracevla-677d98483d23e9cec903d076)
- [furonghuang-lab/tracevla_phi3v](https://huggingface.co/furonghuang-lab/tracevla_phi3v)
- [OpenVLA LIBERO-Spatial checkpoint](https://huggingface.co/openvla/openvla-7b-finetuned-libero-spatial)
- [OpenVLA LIBERO-Object checkpoint](https://huggingface.co/openvla/openvla-7b-finetuned-libero-object)

---
