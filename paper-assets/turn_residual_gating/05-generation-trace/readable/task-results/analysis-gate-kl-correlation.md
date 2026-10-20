# analysis gate kl correlation

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gate_kl_correlation_20260524T094248_result.json`
- **Structured JSON:** [`ce1a69986b7a1e83c39c.json`](../../sessions/ce/ce1a69986b7a1e83c39c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Gate-KL correlation 结果：无显著相关。**

- **Spearman(gate, KL) = 0.0613, p = 0.757** — 几乎为零，远不显著
- Pearson(gate, KL) = 0.112, p = 0.570 — 同样不显著
- Spearman(gate, delta_GAR) = 0.104, p = 0.598 — 也不显著

原假设不成立：gate 值低（gating 更强）的层并不对应更大的 TF-AR KL divergence。方向上甚至略微相反——top-5 最低 gate 层的平均 KL (0.041) 反而**低于** top-5 最高 gate 层 (0.056)。

观察细节：KL 高值集中在**深层**（L22-L27 的 KL 均 > 0.077），而这些层的 gate 值接近 1.0（几乎无 gating）。这说明 TF-AR divergence 主要由**层深度**驱动（深层累积误差更大），gate 调制强度与 exposure bias 的层级分布无关。

---
