# research robomm openvla oft checkpoint

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_robomm-openvla-oft-checkpoint_20260520T053545_result.json`
- **Structured JSON:** [`906cb4867238643e8a0b.json`](../../sessions/90/906cb4867238643e8a0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 agent 全部完成。汇总结果：

---

## 调研结果汇总

| 模型 | Connector 类型 | LIBERO checkpoint | 下载链接 | Vision tokens | 备注 |
|------|---------------|-------------------|----------|--------------|------|
| **RoboMM** | Cross-attention (OpenFlamingo) + UVFormer | **❌ 无** | GitHub有代码无权重 | ~64 (Perceiver 标准) | 权重标记为 TODO 未发布。训练成本 32×A100 130h（全数据集），LIBERO-only 未知 |
| **OpenVLA-OFT** | **3-layer MLP** (与 OpenVLA 相同) | **✅ 4个suite全有** | [HF: moojink/openvla-7b-oft-finetuned-libero-*](https://huggingface.co/moojink) | 256 | Action head 是 L1 regression + parallel decoding（非 flow matching）。97.1% avg SR |
| **DeeR-VLA** | Perceiver Resampler + Cross-attention | **❌ 无** (只有 CALVIN) | [HF: Yang130/DeeR-VLA](https://huggingface.co/Yang130/DeeR-VLA) (CALVIN only) | 64 | 需从零训练 LIBERO，8×V100 ~14-25h |
| **π0** | Linear projection | **✅ 有** | [HF: lerobot/pi0_libero_base](https://huggingface.co/lerobot/pi0_libero_base) | 256 (@224×224) | avg ~65% SR，社区复现有困难 |

---

## 综合建议

**立即可用（有 LIBERO checkpoint，零训练成本）：**

1. **OpenVLA-OFT** — 最容易集成。Connector 与 OpenVLA 完全相同（3-layer MLP），价值在于隔离 action head 对压缩行为的影响。如果 pruning 曲线与 OpenVLA 一致 → 证明压缩性由 connector 决定，与 action head 无关。如果不同 → 有趣的发现。**推荐优先跑。**

2. **π0** — Linear projection connector，与 MLP projector 形成直接对比。已有 LIBERO checkpoint，但性能较低（65%）且社区复现不稳定。256 vision tokens 与 OpenVLA 相同，便于直接比较。**推荐第二个跑。**

**需从零训练（成本较高）：**

3. **DeeR-VLA** — Perceiver Resampler，64 tokens。给 RoboFlamingo 失败的 connector 类型第二次机会。但需自行适配 LIBERO pipeline，8×V100 ~14-25h。**中等优先。**

4. **RoboMM** — Cross-attention，最独特的 connector 类型。但权重未发布、训练成本高（32×A100 全数据集）、LIBERO-only 训练流程未文档化。**暂不推荐，等权重发布。**

---

**修正一个信息**：之前调研报告中 OpenVLA 的 projector 标记为 "2-layer MLP"，OpenVLA-OFT 调研确认实际是 **3-layer MLP with GELU**。需在后续引用中统一。

---
