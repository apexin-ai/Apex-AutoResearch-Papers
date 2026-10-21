# analysis ood diagnostics

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ood_diagnostics_20260518T025758_result.json`
- **Structured JSON:** [`777d3498f0aa36f4deb6.json`](../../sessions/77/777d3498f0aa36f4deb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All deliverables complete. Here's the summary of results:

---

**OOD Diagnostics 完成**

输出文件：
- JSON: `/root/autodl-tmp/vla-ssd/results/ood_diagnostics.json` (11.5KB)
- Figure: `/root/autodl-tmp/vla-ssd/results/figures/fig_ood_diagnostics.pdf` (24KB) + `.png` (178KB)

**关键发现（33 层，63,728 样本）：**

| 指标 | 趋势 | 解读 |
|---|---|---|
| **Activation Magnitude** | llama2base: 16.5→90.2，trained: 16.5→51.7（最终层） | 两者 norm 都在合理范围内增长，llama2base 不存在极端爆炸或坍缩 |
| **Cosine Similarity** | L0=1.0 → L25≈0.28（最低）→ L31≈0.52 → L32≈0.02 | 前几层高度相似，中后层逐渐分化，L32（LM head 前）几乎正交，符合预期 |
| **Variance Explained (top-10 PCs)** | llama2base: 稳定在 0.59-0.74；trained: 从 0.61 降至 0.35 | **llama2base 全层维持高有效维度**（~0.60），不存在表征坍缩。trained 在深层 variance 更分散，说明微调让表征更加多样化 |

**核心结论：llama2base 处理视觉 token 的表征 NOT degenerate。**
- 激活 norm 正常（无爆炸/消失）
- top-10 PC 方差比稳定在 ~0.60（与 trained 模型早期层几乎一致），表征保持 full-rank 结构
- cosine similarity 的渐进下降是微调效果的自然体现，不是 OOD 崩溃的信号
- 这些证据支持 action probe 的 high R² 反映的是 Llama-2 已有的视觉语义编码能力，而非噪声过拟合

---
