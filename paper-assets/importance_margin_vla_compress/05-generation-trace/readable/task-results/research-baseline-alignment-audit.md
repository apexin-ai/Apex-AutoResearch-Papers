# research baseline alignment audit

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_baseline_alignment_audit_20260522T122300_result.json`
- **Structured JSON:** [`9edd6bfaca74b40599eb.json`](../../sessions/9e/9edd6bfaca74b40599eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，整理对比表如下：

---

## Baseline 对齐验证结果

### π0.5 (4B)

| Suite | 我们的 Baseline SR | 论文/官方报告 SR | 差异(pp) | 匹配？ |
|-------|-------------------|-----------------|---------|--------|
| Object | 98.2% | 98.4% | -0.2 | ✅ |
| Spatial | 97.2% | 97.4% | -0.2 | ✅ |
| Goal | 未测(0%异常) | 97.6% | — | ❌ eval 异常 |
| Long | 未测(0%异常) | 93.0% | — | ❌ eval 异常 |

**来源**: [openpi/examples/libero/README.md](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/README.md), checkpoint `pi05_libero`。评估协议: 10 episodes/task × 40 tasks = 400 episodes。

**结论**: Object/Spatial 完美对齐（<0.5pp），baseline 可信。Goal/Long 的 0% 是我们 eval 的 bug，不是模型问题。

---

### OpenVLA (7B)

| Suite | 论文报告 SR (原版) | OpenVLA-OFT SR | 备注 |
|-------|-------------------|----------------|------|
| Spatial | 84.7% | ~96%+ | 原版: 3 seeds × 500 rollouts |
| Object | 88.4% | ~98%+ | |
| Goal | 79.2% | ~97%+ | |
| Long | 53.7% | 96.8% | 最大提升 suite |
| **Avg** | **76.5%** | **97.1%** | |

**来源**: [OpenVLA-OFT paper (arXiv 2502.19645)](https://arxiv.org/abs/2502.19645), [OpenVLA GitHub](https://github.com/openvla/openvla)

**备注**: 我们的 registry 中如有 OpenVLA baseline，应与原版 76.5% avg 对比（LoRA fine-tune 各 suite 独立训练）。

---

### SmolVLA (450M) ⚠️ 关键差异

| Suite | 我们的 Baseline SR | 论文报告 SR | 社区复现(官方ckpt) | 差异(vs论文) |
|-------|-------------------|------------|-------------------|-------------|
| Object | **57.2%** | **96%** | 93.0% | ⚠️ **-38.8pp** |
| Spatial | 未测 | 90% | 63.0% | — |
| Goal | 未测 | 92% | 81.0% | — |
| Long | 未测 | 71% | 56.0% | — |
| **Avg** | — | **87.3%** | **73.25%** | — |

**来源**: [SmolVLA paper (arXiv 2506.01844)](https://arxiv.org/html/2506.01844v1), [lerobot issue #3264](https://github.com/huggingface/lerobot/issues/3264), [lerobot issue #2354](https://github.com/huggingface/lerobot/issues/2354)

**⚠️ 严重问题**: 我们的 57.2% 远低于论文 (96%) 和社区复现 (93%)。可能原因：
1. **eval 配置差异** — 论文用特定的 lerobot 版本和 LIBERO 数据集版本（v3.0），max_steps 设置可能不同
2. **权重版本** — `HuggingFaceVLA/smolvla_libero` 可能有多个版本，论文用的是内部训练版本
3. **社区已知问题** — 多个 issue 报告无法复现论文结果（#3264, #2354, #1369），SmolVLA LIBERO 可复现性是已知争议
4. **动作空间/归一化** — 不同 eval 框架对 action 的处理方式不同

---

### X-VLA (880M)

| Suite | 论文报告 SR (Full FT) | 论文报告 SR (PEFT 1%) | 我们的 Baseline |
|-------|----------------------|----------------------|----------------|
| Object | 99.8% | — | 99.2% (loss, 非 SR) |
| Spatial | 98.8% | — | — |
| Goal | 98.2% | — | — |
| Long | 96.8% | — | — |
| **Avg** | **~98.1%** | **~93%** | — |

**来源**: [X-VLA paper (arXiv 2510.10274)](https://arxiv.org/html/2510.10274v1), [X-VLA GitHub](https://github.com/2toinf/X-VLA)

**备注**: 我们的 99.2% 是 normalized action loss 而非 SR，不可直接对比。需要跑 SR eval 才能验证。

---

### π0 (3.3B)

| Suite | 论文/第三方报告 SR | 我们的 Baseline |
|-------|-------------------|----------------|
| Avg | ~86.0% (SmolVLA paper 引用) | 仅有 normalized loss |

**来源**: [SmolVLA paper Table 2](https://arxiv.org/html/2506.01844v1), [LIBERO-PRO (arXiv 2510.03827)](https://arxiv.org/html/2510.03827v1)

**备注**: π0 在 openpi 中有 `pi0_libero` checkpoint，但官方未公开逐 suite 细分数字（仅 π0.5 公开了）。SmolVLA 论文引用 π0 avg=86.0%。

---

## 总结

| 模型 | Baseline 对齐状态 | 优先级 |
|------|------------------|--------|
| π0.5 | ✅ Object/Spatial 完美对齐 (≤0.2pp) | 低 — 已验证 |
| OpenVLA | ⚠️ 需确认我们的实际 SR 数字 | 中 |
| SmolVLA | ❌ **57.2% vs 论文96%，差距巨大** | **高** — 需排查 eval 配置 |
| X-VLA | ⚠️ 只有 loss 没有 SR，不可对比 | 中 |
| π0 | ⚠️ 只有 loss 没有 SR | 低 |

**关键发现**: SmolVLA 是最大风险点。但注意社区也普遍无法复现论文数字（社区 73.25% vs 论文 87.3%），这可能是 SmolVLA 论文本身的可复现性问题，而非我们独有的 bug。建议检查我们使用的 lerobot 版本、LIBERO 数据集版本、max_steps 参数是否与官方一致。

---

Sources:
- [openpi LIBERO README](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/README.md)
- [OpenVLA-OFT paper](https://arxiv.org/abs/2502.19645)
- [SmolVLA paper](https://arxiv.org/html/2506.01844v1)
- [SmolVLA reproduction issue #3264](https://github.com/huggingface/lerobot/issues/3264)
- [SmolVLA reproduction issue #2354](https://github.com/huggingface/lerobot/issues/2354)
- [X-VLA paper](https://arxiv.org/html/2510.10274v1)
- [X-VLA GitHub](https://github.com/2toinf/X-VLA)
- [LIBERO-PRO](https://arxiv.org/html/2510.03827v1)
- [π0.5 replication issues (lerobot #2114)](https://github.com/huggingface/lerobot/issues/2114)
- [HuggingFace LIBERO docs](https://huggingface.co/docs/lerobot/libero)

---
